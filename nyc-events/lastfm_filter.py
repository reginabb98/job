"""Last.fm lookup: genre tags + listener counts per artist.

Replaces the original Spotify-based approach — Spotify removed `followers`
and `genres` from its public Web API artist responses entirely (confirmed
live, not a Premium-tier issue), so there's nothing there to build on
anymore. Last.fm's API has been stable for years and gives us both signals
for free with a single API key.

Credentials: sign up free at https://www.last.fm/api/account/create,
copy the API key it gives you, put it in lastfm_credentials.json as
{"api_key": "..."} or set LASTFM_API_KEY env var.
"""
import json
import os
from pathlib import Path

import requests

CREDS_FILE = Path(__file__).parent / "lastfm_credentials.json"
CACHE_FILE = Path(__file__).parent / "data" / "artist_lastfm_cache.json"

_cache = None

# Last.fm matches on exact spelling including diacritics — venues/our own
# taste list often type these plain-ASCII, which returns empty results.
ARTIST_NAME_OVERRIDES = {
    "beyonce": "Beyoncé",
    "bjork": "Björk",
    "rosalia": "Rosalía",
    "hermanos gutierrez": "Hermanos Gutiérrez",
    "silvia perez cruz": "Silvia Pérez Cruz",
    "rita payes": "Rita Payés",
}


def _load_api_key():
    key = os.environ.get("LASTFM_API_KEY")
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


def _get_artist_info(artist_name: str):
    """Return {"listeners": int, "tags": [...]} for the artist, or None."""
    key = artist_name.strip().lower()
    artist_name = ARTIST_NAME_OVERRIDES.get(key, artist_name)
    cache = _load_cache()
    if key in cache:
        return cache[key]

    api_key = _load_api_key()
    if not api_key:
        return None

    result = None
    try:
        resp = requests.get(
            "https://ws.audioscrobbler.com/2.0/",
            params={
                "method": "artist.getinfo",
                "artist": artist_name,
                "api_key": api_key,
                "format": "json",
            },
            timeout=10,
        )
        resp.raise_for_status()
        data = resp.json()
        artist = data.get("artist")
        if artist:
            listeners = int(artist.get("stats", {}).get("listeners", 0))
            tags = [t["name"] for t in artist.get("tags", {}).get("tag", [])]
            result = {"listeners": listeners, "tags": tags}
    except Exception as e:
        print(f"[lastfm] lookup failed for {artist_name!r}: {e}")

    cache[key] = result
    _save_cache()
    return result


def get_artist_listeners(artist_name: str):
    result = _get_artist_info(artist_name)
    return result["listeners"] if result else None


def get_artist_tags(artist_name: str):
    result = _get_artist_info(artist_name)
    return result["tags"] if result else None
