"""Scraper for Elsewhere (elsewhere.club/events) via its embedded Next.js JSON."""
import json
import re
from datetime import datetime
from zoneinfo import ZoneInfo

import requests

from .base import Event

NYC = ZoneInfo("America/New_York")

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")

URL = "https://www.elsewhere.club/events"


def scrape() -> list[Event]:
    resp = requests.get(URL, headers={"User-Agent": UA}, timeout=20)
    resp.raise_for_status()
    m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', resp.text, re.S)
    if not m:
        print("[elsewhere] could not find __NEXT_DATA__ payload")
        return []

    data = json.loads(m.group(1))
    raw_events = data["props"]["pageProps"]["initialEventData"]["events"]

    events = []
    for e in raw_events:
        start = e.get("start_date", "")
        if not start:
            continue
        local = datetime.fromisoformat(start).astimezone(NYC)

        room = (e.get("venues") or [""])[0]
        name = f"{e.get('name', '')} ({room})" if room else e.get("name", "")
        events.append(Event(
            type="concert",
            name=name,
            venue="Elsewhere",
            date=local.strftime("%Y-%m-%d"),
            time=local.strftime("%-I:%M %p"),
            url=e.get("ticket_url", URL),
            image=(e.get("image_urls") or [""])[0],
            genre=", ".join(e.get("genres") or []),
        ))
    return events


if __name__ == "__main__":
    for e in scrape():
        print(e.date, e.time, "-", e.venue, "-", e.name)
