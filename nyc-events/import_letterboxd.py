"""One-off import: turn a Letterboxd data export zip into data/movie_taste.json.

Usage: python3 import_letterboxd.py /path/to/letterboxd-export.zip

Tiers (highest wins if a film qualifies for more than one):
  favorite     - on the "all-time-favorites" list
  loved        - rating >= 4.5, or in likes/films.csv
  want_to_see  - on the watchlist and not yet watched
  seen         - watched, no strong signal either way
  avoid        - watched with rating <= 2.0 (so we don't recommend a rewatch)
"""
import csv
import io
import json
import re
import sys
import zipfile
from pathlib import Path

OUT_FILE = Path(__file__).parent / "data" / "movie_taste.json"


def normalize_title(name: str) -> str:
    name = re.sub(r"\s*\[[^\]]*\]\s*$", "", name)
    name = re.sub(r"\s*\([^)]*\)\s*$", "", name)
    name = re.sub(r"[^a-z0-9]", "", name.lower())
    name = re.sub(r"^(the|a|an)", "", name)
    return name


def read_csv_rows(zf: zipfile.ZipFile, path: str, header_row: int = 0):
    try:
        raw = zf.read(path).decode("utf-8")
    except KeyError:
        return []
    lines = raw.splitlines()[header_row:]
    return list(csv.DictReader(lines))


def main():
    if len(sys.argv) < 2:
        print("usage: python3 import_letterboxd.py /path/to/export.zip")
        sys.exit(1)

    zf = zipfile.ZipFile(sys.argv[1])
    names = zf.namelist()

    ratings = read_csv_rows(zf, "ratings.csv")
    watched = read_csv_rows(zf, "watched.csv")
    watchlist = read_csv_rows(zf, "watchlist.csv")
    liked = read_csv_rows(zf, "likes/films.csv")
    favorites_path = next((n for n in names if n.endswith("all-time-favorites.csv")), None)
    favorites = read_csv_rows(zf, favorites_path, header_row=4) if favorites_path else []

    profile = {}

    def entry(name, year):
        key = f"{normalize_title(name)}|{year}"
        if key not in profile:
            profile[key] = {"name": name, "year": year, "tier": None, "rating": None}
        return profile[key]

    for row in watched:
        e = entry(row["Name"], row.get("Year", ""))
        e["tier"] = e["tier"] or "seen"

    for row in ratings:
        e = entry(row["Name"], row.get("Year", ""))
        rating = float(row["Rating"])
        e["rating"] = rating
        if rating >= 4.5:
            e["tier"] = "loved"
        elif rating <= 2.0:
            e["tier"] = "avoid"

    for row in liked:
        e = entry(row["Name"], row.get("Year", ""))
        e["tier"] = "loved"

    for row in watchlist:
        e = entry(row["Name"], row.get("Year", ""))
        if e["tier"] is None:
            e["tier"] = "want_to_see"

    for row in favorites:
        if not row.get("Name"):
            continue
        e = entry(row["Name"], row.get("Year", ""))
        e["tier"] = "favorite"

    OUT_FILE.parent.mkdir(exist_ok=True)
    OUT_FILE.write_text(json.dumps(profile, indent=2))

    tiers = {}
    for e in profile.values():
        tiers[e["tier"]] = tiers.get(e["tier"], 0) + 1
    print(f"imported {len(profile)} films -> {OUT_FILE}")
    print("tier counts:", tiers)


if __name__ == "__main__":
    main()
