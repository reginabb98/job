"""Scraper for Mercury Lounge + Bowery Ballroom (mercuryeastpresents.com).

Both venues run the same WordPress theme ("tm-venue") with the Ticketmaster
"event-discovery" plugin, so one parser covers both.
"""
import requests
from bs4 import BeautifulSoup

from .base import Event, parse_loose_date

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")

VENUES = {
    "Mercury Lounge": "https://mercuryeastpresents.com/mercurylounge/",
    "Bowery Ballroom": "https://mercuryeastpresents.com/boweryballroom/",
}


def _parse_venue(venue_name: str, url: str) -> list[Event]:
    resp = requests.get(url, headers={"User-Agent": UA}, timeout=20)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    events = []
    for section in soup.select("div.tw-section"):
        name_el = section.select_one("div.tw-name a")
        date_el = section.select_one("span.tw-event-date")
        time_el = section.select_one("span.tw-event-time")
        link_el = section.select_one("a.tw-buy-tix-btn")
        img_el = section.select_one("img.event-img")

        if not name_el or not date_el:
            continue

        date = parse_loose_date(date_el.get_text())
        if not date:
            continue

        events.append(Event(
            type="concert",
            name=name_el.get_text(strip=True),
            venue=venue_name,
            date=date,
            time=time_el.get_text(strip=True).replace("Doors:", "").strip() if time_el else "",
            url=link_el["href"] if link_el and link_el.has_attr("href") else url,
            image=img_el["src"] if img_el and img_el.has_attr("src") else "",
        ))
    return events


def scrape() -> list[Event]:
    all_events = []
    for venue_name, url in VENUES.items():
        try:
            all_events.extend(_parse_venue(venue_name, url))
        except Exception as e:
            print(f"[bowery_presents] failed to scrape {venue_name}: {e}")
    return all_events


if __name__ == "__main__":
    for e in scrape():
        print(e.date, e.time, "-", e.venue, "-", e.name)
