"""Scraper for venues that block direct scraping but are listed on doNYC
(donyc.com), an events aggregator.

doNYC's site is a SvelteKit app: each venue page embeds its event list as a
JavaScript object literal (not strict JSON) in an inline <script>, 10 events
per page, paginated with ?page=N. We pull every page and read the fields we
need with small regexes rather than trying to evaluate the JS.
"""
import json
import re
from datetime import datetime
from zoneinfo import ZoneInfo

import requests

from .base import Event

NYC = ZoneInfo("America/New_York")

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")

# Display name -> doNYC venue slug (https://donyc.com/venues/<slug>)
VENUES = {
    "Baby's All Right": "baby-s-all-right",
    "Union Pool": "union-pool",
    "Arlene's Grocery": "arlene-s-grocery",
    "Le Poisson Rouge": "le-poisson-rouge",
    # TV Eye's own site now returns 403 to scrapers; doNYC lists it fine.
    "TV Eye": "tv-eye",
}

MAX_PAGES = 15  # 150 events per venue is far more than any of them list

# One embedded event object. Each ends with its nested venue:{...} object.
_EVENT_RE = re.compile(r'\{id:\d+,type:"event".*?venue:\{[^{}]*\}\}', re.S)
_STR = r'"((?:[^"\\]|\\.)*)"'


def _field(blob: str, key: str) -> str:
    m = re.search(rf'\b{key}:{_STR}', blob)
    if not m:
        return ""
    try:
        return json.loads(f'"{m.group(1)}"')  # decode \" é etc.
    except ValueError:
        return m.group(1)


def _parse_page(html: str) -> list[dict]:
    out = []
    for blob in _EVENT_RE.findall(html):
        # Skip long-running "multi_day" listings (weekly open mics, months-long
        # residencies) — they'd show up on every single day of the feed.
        if _field(blob, "event_type") == "multi_day":
            continue
        begin = _field(blob, "tz_adjusted_begin_time")
        if not begin:
            continue
        try:
            local = datetime.fromisoformat(begin).astimezone(NYC)
        except ValueError:
            continue
        genres = re.search(r'\bgenres:\[([^\]]*)\]', blob)
        out.append({
            "title": _field(blob, "title"),
            "permalink": _field(blob, "permalink"),
            "image": _field(blob, "image_url"),
            "category": _field(blob, "category"),
            "genres": re.findall(_STR, genres.group(1)) if genres else [],
            "local": local,
        })
    return out


def _has_next(html: str) -> bool:
    return bool(re.search(r'has_next:true', html))


def fetch_listing(path: str) -> list[dict]:
    """All events on a doNYC listing path (e.g. 'venues/tv-eye'), every page."""
    events = []
    for page in range(1, MAX_PAGES + 1):
        resp = requests.get(f"https://donyc.com/{path}", params={"page": page},
                            headers={"User-Agent": UA}, timeout=20)
        resp.raise_for_status()
        events.extend(_parse_page(resp.text))
        if not _has_next(resp.text):
            break
    return events


def _to_event(raw: dict, venue_name: str, event_type: str = "concert") -> Event:
    return Event(
        type=event_type,
        name=raw["title"],
        venue=venue_name,
        date=raw["local"].strftime("%Y-%m-%d"),
        time=raw["local"].strftime("%-I:%M %p"),
        url=f"https://donyc.com{raw['permalink']}" if raw["permalink"] else "",
        image=raw["image"],
        genre=", ".join(raw["genres"][:2]),
    )


def scrape() -> list[Event]:
    all_events = []
    for venue_name, slug in VENUES.items():
        try:
            raws = fetch_listing(f"venues/{slug}")
            all_events.extend(_to_event(r, venue_name) for r in raws)
        except Exception as e:
            print(f"[donyc] failed to scrape {venue_name}: {e}")
    return all_events


if __name__ == "__main__":
    for e in scrape():
        print(e.date, e.time, "-", e.venue, "-", e.name, "|", e.genre)
