"""TMDb (themoviedb.org) lookup: genres, synopsis, cast/director, keywords
(a proxy for tone/vibe beyond blunt genre names), similar films, and poster
art for a movie — used to (a) exclude horror/documentaries from movie
discovery, (b) score genre fit against the user's rated-favorites genre
profile, and (c) show a rich detail view for every movie, even ones whose
own venue page doesn't list a year (Film Forum, IFC Center, Nitehawk).

Credentials: free account at themoviedb.org -> Settings -> API -> request a
key (Developer / personal use). Put it in tmdb_credentials.json as
{"api_key": "..."} or set TMDB_API_KEY env var.
"""
import json
import os
from pathlib import Path

import requests

CREDS_FILE = Path(__file__).parent / "tmdb_credentials.json"
CACHE_FILE = Path(__file__).parent / "data" / "tmdb_cache.json"

GENRE_MAP = {
    28: "Action", 12: "Adventure", 16: "Animation", 35: "Comedy", 80: "Crime",
    99: "Documentary", 18: "Drama", 10751: "Family", 14: "Fantasy", 36: "History",
    27: "Horror", 10402: "Music", 9648: "Mystery", 10749: "Romance",
    878: "Science Fiction", 10770: "TV Movie", 53: "Thriller", 10752: "War",
    37: "Western",
}

# TMDb's genre list is blunt (18 buckets). Its keywords are far more specific
# (MUBI/Letterboxd-style) — map the common ones onto short display tags we
# merge alongside the genre list, e.g. "Drama, LGBTQ+" instead of just "Drama".
KEYWORD_TAG_MAP = {
    "lgbt": "LGBTQ+", "gay theme": "LGBTQ+", "male homosexuality": "LGBTQ+",
    "lesbian": "LGBTQ+", "transgender": "LGBTQ+", "bisexual": "LGBTQ+",
    "queer": "LGBTQ+",
    "coming of age": "Coming-of-Age",
    "biopic": "Biopic", "biography": "Biopic",
    "based on true story": "True Story",
    "based on novel or book": "Book Adaptation",
    "based on play or musical": "Stage Adaptation",
    "musical": "Musical",
    "silent film": "Silent Film",
    "anime": "Anime",
    "based on video game": "Video Game Adaptation",
    "psychedelic": "Psychedelic",
    "experimental film": "Experimental",
    "docudrama": "Docudrama",
    "erotica": "Erotic",
    "found footage": "Found Footage",
    "anthology": "Anthology",
    "black and white": "Black & White",
    "remake": "Remake",
}

NOTABLE_CAST_THRESHOLD = 3.0

_cache = None


def _load_api_key():
    key = os.environ.get("TMDB_API_KEY")
    if key:
        return key
    if CREDS_FILE.exists():
        return json.loads(CREDS_FILE.read_text()).get("api_key")
    return None


def is_configured() -> bool:
    return bool(_load_api_key())


def _load_cache():
    global _cache
    if _cache is None:
        _cache = json.loads(CACHE_FILE.read_text()) if CACHE_FILE.exists() else {}
    return _cache


def _save_cache():
    CACHE_FILE.parent.mkdir(exist_ok=True)
    CACHE_FILE.write_text(json.dumps(_cache, indent=2))


def _get(path: str, api_key: str, params: dict = None):
    resp = requests.get(
        f"https://api.themoviedb.org/3{path}",
        params={"api_key": api_key, **(params or {})},
        timeout=10,
    )
    resp.raise_for_status()
    return resp.json()


def get_movie_details(title: str, year: str = ""):
    """Return {genres, overview, year, poster_url, director, cast, keywords,
    similar} for the best-matching film, or None if not found / API
    unavailable. One cached lookup does a search + 3 follow-up calls
    (credits, keywords, similar) — cheap after the first run per title."""
    cache = _load_cache()
    key = f"{title.strip().lower()}|{year}"
    if key in cache:
        return cache[key]

    api_key = _load_api_key()
    if not api_key:
        return None

    result = None
    try:
        search_params = {"query": title}
        if year:
            search_params["year"] = year
        results = _get("/search/movie", api_key, search_params).get("results", [])
        if results:
            m = results[0]
            movie_id = m["id"]
            genres = [g for g in (GENRE_MAP.get(gid) for gid in m.get("genre_ids", [])) if g]
            release_date = m.get("release_date", "")

            director, cast = "", []
            try:
                credits = _get(f"/movie/{movie_id}/credits", api_key)
                director = next((p["name"] for p in credits.get("crew", []) if p["job"] == "Director"), "")
                cast = [
                    {"name": p["name"], "notable": p.get("popularity", 0) >= NOTABLE_CAST_THRESHOLD}
                    for p in credits.get("cast", [])[:6]
                ]
            except Exception:
                pass

            keywords = []
            try:
                kw = _get(f"/movie/{movie_id}/keywords", api_key)
                keywords = [k["name"] for k in kw.get("keywords", [])[:10]]
            except Exception:
                pass

            extra_tags = []
            for k in keywords:
                tag = KEYWORD_TAG_MAP.get(k.lower())
                if tag and tag not in extra_tags:
                    extra_tags.append(tag)
            display_genres = genres + [t for t in extra_tags if t not in genres]

            similar = []
            try:
                sim = _get(f"/movie/{movie_id}/similar", api_key)
                similar = [r["title"] for r in sim.get("results", [])[:4]]
            except Exception:
                pass

            country = ""
            try:
                full = _get(f"/movie/{movie_id}", api_key)
                countries = full.get("production_countries") or []
                country = countries[0]["name"] if countries else ""
            except Exception:
                pass

            result = {
                "genres": genres,
                "display_genres": display_genres,
                "overview": m.get("overview", ""),
                "year": release_date[:4] if release_date else "",
                "poster_url": f"https://image.tmdb.org/t/p/w200{m['poster_path']}" if m.get("poster_path") else "",
                "director": director,
                "cast": cast,
                "keywords": keywords,
                "similar": similar,
                "country": country,
                "vote_count": m.get("vote_count", 0),
            }
    except Exception as e:
        print(f"[tmdb] lookup failed for {title!r}: {e}")

    cache[key] = result
    _save_cache()
    return result


def get_genres(title: str, year: str = ""):
    """Back-compat helper: just the genre list, or None."""
    details = get_movie_details(title, year)
    return details["genres"] if details else None
