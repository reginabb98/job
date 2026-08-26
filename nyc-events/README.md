# NYC Shows & Movies

A personal recommender for NYC concerts and indie/repertory movie screenings.
It scrapes a set of venue sites, then flags each listing against your music
taste (Last.fm) and film taste (Letterboxd/TMDb) so the feed highlights
things you'd actually want to go to.

## Setup

```bash
pip install -r requirements.txt
```

Copy the credential templates and fill in real keys:

```bash
cp lastfm_credentials.example.json lastfm_credentials.json
cp tmdb_credentials.example.json tmdb_credentials.json
```

- Last.fm key: sign up free at https://www.last.fm/api/account/create
- TMDb key: free account at https://www.themoviedb.org -> Settings -> API

Both credential files are gitignored — they never get committed. You can also
set `LASTFM_API_KEY` / `TMDB_API_KEY` env vars instead of using the files.

## Usage

```bash
python run.py          # scrape all venues, annotate with taste, write data/events.json
python serve.py         # serve index.html + data/ on http://127.0.0.1:8124
```

Then open http://127.0.0.1:8124.

### Rebuilding your taste profile

- `taste_profile.json` — your explicit loved/exploring/casual artist lists
  and genres to avoid (concerts). Edit by hand.
- `artist_vibes.json` — one-line vibe notes shown for matched artists. Edit
  by hand.
- `data/movie_taste.json` — built from a Letterboxd export:
  ```bash
  python import_letterboxd.py /path/to/letterboxd-export.zip
  ```
- After changing `taste_profile.json`'s artist lists or re-importing
  Letterboxd data, rebuild the genre-affinity profiles (used to catch
  artists/movies you'd probably like but haven't explicitly listed):
  ```bash
  python build_concert_genre_profile.py
  python build_movie_genre_profile.py
  ```

## How it fits together

- `scrapers/` — one module per venue (Mercury Lounge & Bowery Ballroom,
  Elsewhere, Public Records, TV Eye, The Broadway, DoNYC, Metrograph, Film
  Forum, IFC Center, Nitehawk), each returning a list of `scrapers.base.Event`.
- `run.py` — runs every scraper, de-dupes, annotates each event via `taste.py`
  and `movie_taste.py`, ranks by distance/transit via `venues.py`, writes
  `data/events.json`.
- `taste.py` — concert-side matching: explicit artist lists, then Last.fm
  genre-tag similarity against your loved artists, plus a "low profile"
  filter using Last.fm listener counts.
- `movie_taste.py` — movie-side matching against your Letterboxd history,
  plus TMDb genre-affinity discovery for films you haven't rated.
- `lastfm_filter.py` / `tmdb_filter.py` — API clients with on-disk caching
  (`data/artist_lastfm_cache.json`, `data/tmdb_cache.json`).
- `index.html` — static single-page frontend that fetches `data/events.json`
  and renders the filterable feed. `serve.py` just serves the folder.

`data/*.json` cache and profile files are checked in so the feed works out
of the box; delete any of them and rerun the relevant script to regenerate.
