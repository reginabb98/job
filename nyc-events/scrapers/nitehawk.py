"""Scraper for Nitehawk Cinema (nitehawkcinema.com) — Filmbot-powered, one page per day."""
import time
from datetime import date, timedelta

import requests
from bs4 import BeautifulSoup

from .base import Event

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")

LOCATIONS = {
    "williamsburg": "Nitehawk Cinema (Williamsburg)",
    "prospectpark": "Nitehawk Cinema (Prospect Park)",
}

DAYS_AHEAD = 10


def _scrape_day(location_slug: str, venue_name: str, day: date) -> list[Event]:
    url = f"https://nitehawkcinema.com/{location_slug}/{day.isoformat()}/0/"
    resp = requests.get(url, headers={"User-Agent": UA}, timeout=20)
    if resp.status_code != 200:
        return []
    soup = BeautifulSoup(resp.text, "html.parser")

    events = []
    for show in soup.select("li.show-container"):
        title_el = show.select_one("div.show-title")
        if not title_el:
            continue
        title = title_el.get_text(strip=True)
        detail_url = show.select_one("a.overlay-link")
        detail_href = detail_url.get("href", url) if detail_url else url

        for span in show.select("ul.showtime-button-row span.showtime"):
            time_text = next(iter(span.stripped_strings), "")
            events.append(Event(
                type="movie",
                name=title,
                venue=venue_name,
                date=day.isoformat(),
                time=time_text,
                url=span.get("href", detail_href),
            ))
    return events


def scrape() -> list[Event]:
    events = []
    today = date.today()
    for slug, venue_name in LOCATIONS.items():
        for offset in range(DAYS_AHEAD):
            day = today + timedelta(days=offset)
            try:
                events.extend(_scrape_day(slug, venue_name, day))
            except Exception as e:
                print(f"[nitehawk] failed {venue_name} {day}: {e}")
            time.sleep(0.3)
    return events


if __name__ == "__main__":
    for e in scrape():
        print(e.date, e.time, "-", e.venue, "-", e.name)
