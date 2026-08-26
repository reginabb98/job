"""Scraper for venues that block direct scraping but are listed on doNYC
(donyc.com), an events aggregator with clean schema.org-marked HTML —
covers Baby's All Right, Union Pool, and Arlene's Grocery.
"""
import re
from datetime import datetime
from zoneinfo import ZoneInfo

import requests
from bs4 import BeautifulSoup

from .base import Event

NYC = ZoneInfo("America/New_York")

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")

VENUES = {
    "Baby's All Right": "https://donyc.com/venues/baby-s-all-right",
    "Union Pool": "https://donyc.com/venues/union-pool",
    "Arlene's Grocery": "https://donyc.com/venues/arlene-s-grocery",
}


def _parse_venue(venue_name: str, url: str) -> list[Event]:
    resp = requests.get(url, headers={"User-Agent": UA}, timeout=20)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    events = []
    for card in soup.select("div.ds-listing.event-card"):
        title_el = card.select_one("span.ds-listing-event-title-text")
        date_meta = card.select_one('meta[itemprop="startDate"]')
        if not title_el or not date_meta or not date_meta.get("content"):
            continue

        try:
            # Python 3.9's fromisoformat needs "+HH:MM", not doNYC's "+HHMM"
            raw = re.sub(r"([+-]\d{2})(\d{2})$", r"\1:\2", date_meta["content"])
            local = datetime.fromisoformat(raw).astimezone(NYC)
        except ValueError:
            continue

        ticket_meta = card.select_one('span[itemprop="offers"] meta[itemprop="url"]')
        if ticket_meta and ticket_meta.get("content"):
            ticket_url = ticket_meta["content"]
        else:
            permalink = card.get("data-permalink", "")
            ticket_url = f"https://donyc.com{permalink}" if permalink else url

        events.append(Event(
            type="concert",
            name=title_el.get_text(strip=True),
            venue=venue_name,
            date=local.strftime("%Y-%m-%d"),
            time=local.strftime("%-I:%M %p"),
            url=ticket_url,
        ))
    return events


def scrape() -> list[Event]:
    all_events = []
    for venue_name, url in VENUES.items():
        try:
            all_events.extend(_parse_venue(venue_name, url))
        except Exception as e:
            print(f"[donyc] failed to scrape {venue_name}: {e}")
    return all_events


if __name__ == "__main__":
    for e in scrape():
        print(e.date, e.time, "-", e.venue, "-", e.name)
