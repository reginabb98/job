"""One-time (rerun occasionally) job: look up TMDb genres for every film in
data/movie_taste.json rated 'loved' or 'favorite', and build a genre
affinity profile at data/movie_genre_profile.json.

This is separate from run.py because it makes one TMDb call per loved film
(a few hundred) — you don't want that on every pipeline refresh, just when
your ratings meaningfully change.

Usage: python3 build_movie_genre_profile.py
"""
import json
from collections import Counter
from pathlib import Path

import tmdb_filter

MOVIE_TASTE_FILE = Path(__file__).parent / "data" / "movie_taste.json"
OUT_FILE = Path(__file__).parent / "data" / "movie_genre_profile.json"


def main():
    if not tmdb_filter.is_configured():
        print("TMDb not configured — add tmdb_credentials.json first (see tmdb_filter.py).")
        return

    profile = json.loads(MOVIE_TASTE_FILE.read_text())
    loved = [e for e in profile.values() if e["tier"] in ("loved", "favorite")]
    print(f"looking up genres for {len(loved)} loved/favorite films...")

    counts = Counter()
    checked = 0
    for entry in loved:
        genres = tmdb_filter.get_genres(entry["name"], entry.get("year", ""))
        if genres:
            counts.update(genres)
        checked += 1
        if checked % 50 == 0:
            print(f"  ...{checked}/{len(loved)}")

    total = sum(counts.values()) or 1
    weighted = {genre: round(n / total, 4) for genre, n in counts.most_common()}

    OUT_FILE.write_text(json.dumps(weighted, indent=2))
    print(f"wrote genre profile -> {OUT_FILE}")
    print(json.dumps(weighted, indent=2))


if __name__ == "__main__":
    main()
