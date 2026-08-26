"""Scraper for Metrograph (metrograph.com/nyc/) — WordPress, server-rendered calendar grid."""
import re

import requests
from bs4 import BeautifulSoup

from .base import Event

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")

URL = "https://metrograph.com/nyc/"


def scrape() -> list[Event]:
    resp = requests.get(URL, headers={"User-Agent": UA}, timeout=20)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    events = []
    for day_div in soup.select("div.calendar-list-day"):
        day_id = day_div.get("id", "")
        date = day_id.replace("calendar-list-day-", "") if day_id.startswith("calendar-list-day-") else ""
        if not date:
            continue

        for item in day_div.select("div.item.film-thumbnail"):
            title_el = item.select_one("h4 a.title")
            if not title_el:
                continue
            title = title_el.get_text(strip=True)
            film_url = title_el.get("href", URL)

            meta_el = item.select_one("div.film-metadata")
            year_match = re.search(r"\b(19|20)\d{2}\b", meta_el.get_text()) if meta_el else None
            year = year_match.group(0) if year_match else ""

            for a in item.select("div.showtimes a"):
                if "sold_out" in (a.get("class") or []):
                    continue
                events.append(Event(
                    type="movie",
                    name=title,
                    venue="Metrograph",
                    date=date,
                    time=a.get_text(strip=True),
                    url=a.get("href", film_url),
                    year=year,
                ))
    return events


if __name__ == "__main__":
    for e in scrape():
        print(e.date, e.time, "-", e.venue, "-", e.name)
