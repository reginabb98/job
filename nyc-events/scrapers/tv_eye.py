"""Scraper for TV Eye (tveyenyc.com) — "See Tickets" WordPress plugin listing."""
import requests
from bs4 import BeautifulSoup

from .base import Event, parse_loose_date

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")

URL = "https://tveyenyc.com/calendar/"


def scrape() -> list[Event]:
    resp = requests.get(URL, headers={"User-Agent": UA}, timeout=20)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    events = []
    for card in soup.select("div.seetickets-list-event-container"):
        title_el = card.select_one("p.title a")
        date_el = card.select_one("p.date")
        doors_el = card.select_one("span.see-doortime")
        show_el = card.select_one("span.see-showtime")

        if not title_el or not date_el:
            continue

        date = parse_loose_date(date_el.get_text())
        if not date:
            continue

        time_str = ""
        if doors_el and doors_el.get_text(strip=True):
            time_str = f"Doors: {doors_el.get_text(strip=True)}"
        elif show_el and show_el.get_text(strip=True):
            time_str = f"Show: {show_el.get_text(strip=True)}"

        events.append(Event(
            type="concert",
            name=title_el.get_text(strip=True),
            venue="TV Eye",
            date=date,
            time=time_str,
            url=title_el.get("href", URL),
        ))
    return events


if __name__ == "__main__":
    for e in scrape():
        print(e.date, e.time, "-", e.venue, "-", e.name)
