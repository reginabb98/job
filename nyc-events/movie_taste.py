"""Match scraped movie listings against data/movie_taste.json (built by
import_letterboxd.py) to flag films the user has rated highly, liked,
watchlisted, or already seen and disliked.
"""
import json
import re
from pathlib import Path

import tmdb_filter

DATA_FILE = Path(__file__).parent / "data" / "movie_taste.json"
GENRE_PROFILE_FILE = Path(__file__).parent / "data" / "movie_genre_profile.json"

TIER_RANK = {"favorite": 4, "loved": 3, "want_to_see": 2, "seen": 1, "avoid": 0}

EXCLUDE_GENRES = {"Horror", "Documentary"}
DISCOVER_THRESHOLD = 0.30

_by_title_year = None
_by_title = None
_genre_profile = None


def normalize_title(name: str) -> str:
    name = re.sub(r"\s*\[[^\]]*\]\s*$", "", name)
    name = re.sub(r"\s*\([^)]*\)\s*$", "", name)
    name = re.sub(r"[^a-z0-9]", "", name.lower())
    name = re.sub(r"^(the|a|an)", "", name)
    return name


def _load():
    global _by_title_year, _by_title
    if _by_title_year is not None:
        return

    _by_title_year = {}
    _by_title = {}

    if not DATA_FILE.exists():
        return

    profile = json.loads(DATA_FILE.read_text())
    for entry in profile.values():
        norm = normalize_title(entry["name"])
        key = f"{norm}|{entry.get('year', '')}"
        _by_title_year[key] = entry

        existing = _by_title.get(norm)
        if existing is None or TIER_RANK[entry["tier"]] > TIER_RANK[existing["tier"]]:
            _by_title[norm] = entry


def match(name: str, year: str = ""):
    """Return (tier, rating) or (None, None)."""
    _load()
    norm = normalize_title(name)

    if year:
        entry = _by_title_year.get(f"{norm}|{year}")
        if entry:
            return entry["tier"], entry.get("rating")

    entry = _by_title.get(norm)
    if entry:
        return entry["tier"], entry.get("rating")

    return None, None


def _load_genre_profile():
    global _genre_profile
    if _genre_profile is None:
        _genre_profile = (json.loads(GENRE_PROFILE_FILE.read_text())
                           if GENRE_PROFILE_FILE.exists() else {})
    return _genre_profile


def discover_match(name: str, year: str = ""):
    """For a film with no Letterboxd history: return ('discover', genres) if
    it's not horror/documentary and scores well against the user's
    loved-genre affinity profile, else (None, None).

    Requires TMDb configured and a genre profile built via
    build_movie_genre_profile.py — degrades to (None, None) without either.
    """
    if not tmdb_filter.is_configured():
        return None, None
    genre_profile = _load_genre_profile()
    if not genre_profile:
        return None, None

    genres = tmdb_filter.get_genres(name, year)
    if not genres:
        return None, None
    if EXCLUDE_GENRES & set(genres):
        return None, None

    score = sum(genre_profile.get(g, 0) for g in genres)
    if score >= DISCOVER_THRESHOLD:
        return "discover", genres
    return None, None


def is_configured() -> bool:
    return DATA_FILE.exists()
