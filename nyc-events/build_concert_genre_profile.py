"""One-time (rerun if you update taste_profile.json's artist lists): look up
Last.fm tags for every artist in your loved/exploring lists and build a
genre affinity profile at data/concert_genre_profile.json, used to flag
unfamiliar concert artists whose tags overlap with what you already like —
and to name which of your loved artists an unfamiliar act resembles.

Usage: python3 build_concert_genre_profile.py
"""
import json
from collections import Counter, defaultdict
from pathlib import Path

import lastfm_filter

PROFILE_FILE = Path(__file__).parent / "taste_profile.json"
OUT_FILE = Path(__file__).parent / "data" / "concert_genre_profile.json"


def main():
    if not lastfm_filter.is_configured():
        print("Last.fm not configured — add lastfm_credentials.json first (see lastfm_filter.py).")
        return

    profile = json.loads(PROFILE_FILE.read_text())
    artists = (profile.get("loved_artists", []) + profile.get("exploring_rockier_alt", [])
               + profile.get("casually_liked", []))
    print(f"looking up tags for {len(artists)} artists...")

    counts = Counter()
    tag_to_artists = defaultdict(list)
    for i, artist in enumerate(artists, 1):
        tags = lastfm_filter.get_artist_tags(artist)
        if tags:
            counts.update(tags)
            for t in tags:
                if artist not in tag_to_artists[t]:
                    tag_to_artists[t].append(artist)
        else:
            print(f"  (no Last.fm tags found for {artist!r})")
        if i % 10 == 0:
            print(f"  ...{i}/{len(artists)}")

    total = sum(counts.values()) or 1
    weighted = {
        tag: {"weight": round(n / total, 4), "artists": tag_to_artists[tag]}
        for tag, n in counts.most_common()
    }

    OUT_FILE.parent.mkdir(exist_ok=True)
    OUT_FILE.write_text(json.dumps(weighted, indent=2))
    print(f"wrote genre profile -> {OUT_FILE}")


if __name__ == "__main__":
    main()
