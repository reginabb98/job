"""Match scraped events against taste_profile.json and (optionally) filter
out very small/unknown concert acts using Last.fm listener counts.
"""
import json
import re
from pathlib import Path

import lastfm_filter
import movie_taste
import tmdb_filter

PROFILE_FILE = Path(__file__).parent / "taste_profile.json"
VIBES_FILE = Path(__file__).parent / "artist_vibes.json"
CONCERT_GENRE_PROFILE_FILE = Path(__file__).parent / "data" / "concert_genre_profile.json"

GENRE_MATCH_THRESHOLD = 0.10

_profile = None
_vibes = None
_concert_genre_profile = None


def _load_profile():
    global _profile
    if _profile is None:
        _profile = json.loads(PROFILE_FILE.read_text())
    return _profile


def _load_vibes():
    global _vibes
    if _vibes is None:
        _vibes = json.loads(VIBES_FILE.read_text()) if VIBES_FILE.exists() else {}
    return _vibes


def _load_concert_genre_profile():
    global _concert_genre_profile
    if _concert_genre_profile is None:
        _concert_genre_profile = (json.loads(CONCERT_GENRE_PROFILE_FILE.read_text())
                                   if CONCERT_GENRE_PROFILE_FILE.exists() else {})
    return _concert_genre_profile


def split_artists(event_name: str) -> list[str]:
    """Break a listing name like 'Wombo, shower curtain (The Rooftop)' or
    'X with special guests Y and Z' into individual artist name guesses."""
    name = re.sub(r"\s*\[[^\]]*\]\s*$", "", event_name)  # strip trailing "[35mm Print]"
    name = re.sub(r"\s*\([^)]*\)\s*$", "", name)  # strip trailing "(Room)"
    name = re.sub(r"^.*?\bpresents?\b.*?:", "", name, flags=re.I)  # drop "X presents Y:" prefix entirely
    parts = re.split(r",|&|:|\bwith\b|\bx\b|\bb2b\b|/|\bft\.?\b|\bfeat\.?\b", name, flags=re.I)
    return [p.strip() for p in parts if p.strip()]


def _candidate_matches(candidate: str, artist: str) -> bool:
    c, a = candidate.lower().strip(), artist.lower().strip()
    if c == a:
        return True
    return bool(re.match(rf"^{re.escape(a)}\b", c))


def taste_match(event_name: str):
    """Return ('loved'|'exploring'|'throwback_vibe', matched_artist) or (None, None).

    Matches against individual split-out artist names (not a raw substring
    search on the whole listing) so short/common band names like "Hole" or
    "Garbage" don't false-positive on unrelated listings ("The Hole", "King
    Garbage").
    """
    profile = _load_profile()
    candidates = split_artists(event_name)

    for tier, key in [
        ("loved", "loved_artists"),
        ("exploring", "exploring_rockier_alt"),
        ("throwback_vibe", "throwback_alt_reference_points"),
        ("casual", "casually_liked"),
    ]:
        for artist in profile.get(key, []):
            for candidate in candidates:
                if _candidate_matches(candidate, artist):
                    return tier, artist
    return None, None


def is_low_profile(event_name: str, threshold: int) -> bool:
    """True if none of the event's artists meet the Last.fm listener threshold
    (and Last.fm lookup is actually configured/available)."""
    if not lastfm_filter.is_configured():
        return False  # can't verify -> don't hide anything

    for artist in split_artists(event_name):
        listeners = lastfm_filter.get_artist_listeners(artist)
        if listeners is None:
            continue  # unknown to Last.fm -> don't penalize on this artist alone
        if listeners >= threshold:
            return False
    return True


def genre_similarity_match(event_name: str):
    """For an artist not in your explicit taste_profile lists: check their
    Last.fm tags against your loved/exploring genre affinity profile
    (built by build_concert_genre_profile.py). Returns
    (matched_artist, tags, score, similar_artists) or (None, None, None, None).

    similar_artists names up to 3 of your loved/exploring artists that share
    the overlapping tags, so the match can say *who* it resembles instead of
    a vague "close to what you already like".

    Requires Last.fm configured and a genre profile built — degrades to no
    match without either.
    """
    if not lastfm_filter.is_configured():
        return None, None, None, None
    genre_profile = _load_concert_genre_profile()
    if not genre_profile:
        return None, None, None, None

    profile = _load_profile()
    avoid = [g.lower() for g in profile.get("avoid_genres", [])]

    best = (None, None, 0, [])
    for candidate in split_artists(event_name):
        tags = lastfm_filter.get_artist_tags(candidate)
        if not tags:
            continue
        tags_lower = " ".join(tags).lower()
        if any(g in tags_lower for g in avoid):
            continue

        score = 0
        overlap_count = {}
        overlap_weight = {}
        for t in tags:
            entry = genre_profile.get(t)
            if not entry:
                continue
            score += entry["weight"]
            for a in entry.get("artists", []):
                overlap_count[a] = overlap_count.get(a, 0) + 1
                overlap_weight[a] = overlap_weight.get(a, 0) + entry["weight"]

        # Rank by how many tags each artist actually shares with this
        # candidate (not just first-tag order) — a single shared common tag
        # like "experimental" shouldn't outrank someone sharing 2+ tags.
        ranked = sorted(overlap_count, key=lambda a: (-overlap_count[a], -overlap_weight[a]))
        similar_artists = ranked[:3]

        if score > best[2]:
            best = (candidate, tags, score, similar_artists)

    if best[2] >= GENRE_MATCH_THRESHOLD:
        return best
    return None, None, None, None


def is_disliked_genre(genre: str) -> bool:
    if not genre:
        return False
    profile = _load_profile()
    avoid = [g.lower() for g in profile.get("avoid_genres", [])]
    genre_lower = genre.lower()
    return any(g in genre_lower for g in avoid)


def popularity_label(listeners):
    """Rough size/popularity tier from a Last.fm listener count, for display."""
    if listeners is None:
        return None
    if listeners < 2_000:
        return "Just starting out"
    if listeners < 20_000:
        return "Building a following"
    if listeners < 150_000:
        return "Well-established"
    if listeners < 1_000_000:
        return "Well-known"
    return "Major artist"


def movie_reach_label(vote_count):
    """Rough 'how big vs. niche' tier from TMDb's vote_count, for display."""
    if vote_count is None:
        return None
    if vote_count < 50:
        return "Rare / very niche"
    if vote_count < 500:
        return "Niche / arthouse"
    if vote_count < 3_000:
        return "Mid-size release"
    if vote_count < 15_000:
        return "Wide release"
    return "Blockbuster"


def annotate(event_dict: dict) -> dict:
    """Add taste_flag / matched_artist / low_profile / vibe_note (concerts) or
    movie_taste_flag / movie_rating (movies) fields to an event dict."""
    profile = _load_profile()

    if event_dict["type"] == "movie":
        tier, rating = movie_taste.match(event_dict["name"], event_dict.get("year", ""))

        # Always fetch genre/synopsis for display, regardless of tier — this
        # also backfills year for venues (Film Forum, IFC, Nitehawk) whose own
        # site doesn't show one.
        details = tmdb_filter.get_movie_details(event_dict["name"], event_dict.get("year", ""))
        if details and not event_dict.get("year"):
            event_dict["year"] = details.get("year", "")

        if tier is None:
            discover_tier, _ = movie_taste.discover_match(event_dict["name"], event_dict.get("year", ""))
            tier = discover_tier
            rating = None

        event_dict["taste_flag"] = None
        event_dict["matched_artist"] = None
        event_dict["low_profile"] = False
        event_dict["movie_taste_flag"] = tier
        event_dict["movie_rating"] = rating
        event_dict["movie_genres"] = details.get("display_genres") if details else None
        event_dict["movie_overview"] = details.get("overview") if details else None
        event_dict["movie_poster"] = details.get("poster_url") if details else None
        event_dict["movie_director"] = details.get("director") if details else None
        event_dict["movie_cast"] = details.get("cast") if details else None
        event_dict["movie_keywords"] = details.get("keywords") if details else None
        event_dict["movie_similar"] = details.get("similar") if details else None
        event_dict["movie_country"] = details.get("country") if details else None
        event_dict["movie_reach"] = movie_reach_label(details.get("vote_count")) if details else None
        return event_dict

    candidates = split_artists(event_dict["name"])
    event_dict["display_name"] = candidates[0] if candidates else event_dict["name"]

    tier, artist = taste_match(event_dict["name"])
    vibe_note = _load_vibes().get(artist) if artist else None
    genre_match_tags = None
    genre_match_score = None
    similar_artists = None

    if tier is None:
        genre_artist, tags, score, sim_artists = genre_similarity_match(event_dict["name"])
        if genre_artist:
            tier = "genre_match"
            artist = genre_artist
            genre_match_tags = tags
            genre_match_score = score
            similar_artists = sim_artists
            # No vibe_note here on purpose: genre tags now show inline on the
            # compact card (no click needed), and "Similar to ..." lives in
            # the expanded detail panel only, per user preference.

    event_dict["taste_flag"] = tier
    event_dict["matched_artist"] = artist
    event_dict["genre_match_tags"] = genre_match_tags
    event_dict["genre_match_score"] = genre_match_score
    event_dict["similar_artists"] = similar_artists

    # Popularity/size info for display on every concert, not just unmatched ones.
    headliner = artist or (split_artists(event_dict["name"]) or [event_dict["name"]])[0]
    listeners = lastfm_filter.get_artist_listeners(headliner) if lastfm_filter.is_configured() else None
    event_dict["artist_listeners"] = listeners
    event_dict["artist_popularity"] = popularity_label(listeners)
    if not genre_match_tags:
        event_dict["artist_tags"] = lastfm_filter.get_artist_tags(headliner) if lastfm_filter.is_configured() else None
    else:
        event_dict["artist_tags"] = genre_match_tags
    event_dict["vibe_note"] = vibe_note
    event_dict["movie_taste_flag"] = None
    event_dict["movie_rating"] = None

    # Size filter applies to genre_match too (an algorithmic guess about an
    # unfamiliar act) — only skip it for artists explicitly in your taste
    # lists, where you already know you like them regardless of how small
    # they are.
    low_profile = False
    if tier is None or tier == "genre_match":
        threshold = profile.get("min_monthly_listeners", 8000)
        low_profile = is_low_profile(event_dict["name"], threshold)
    event_dict["low_profile"] = low_profile

    event_dict["genre_dislike"] = tier is None and is_disliked_genre(event_dict.get("genre", ""))
    return event_dict
