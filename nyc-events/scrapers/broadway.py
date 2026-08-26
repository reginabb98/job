"""Scraper for The Broadway (thebroadway.nyc/showcalendar) — Squarespace's
native event-list block, server-rendered."""
import requests
from bs4 import BeautifulSoup

from .base import Event

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")

URL = "https://www.thebroadway.nyc/showcalendar"


def scrape() -> list[Event]:
    resp = requests.get(URL, headers={"User-Agent": UA}, timeout=20)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    events = []
    for article in soup.select("article.eventlist-event--upcoming"):
        title_el = article.select_one("h1.eventlist-title a.eventlist-title-link")
        date_el = article.select_one("time.event-date")
        time_el = article.select_one("time.event-time-localized-start")

        if not title_el or not date_el or not date_el.get("datetime"):
            continue

        href = title_el.get("href", URL)
        if href.startswith("/"):
            href = "https://www.thebroadway.nyc" + href

        events.append(Event(
            type="concert",
            name=title_el.get_text(strip=True),
            venue="The Broadway",
            date=date_el["datetime"],
            time=time_el.get_text(strip=True) if time_el else "",
            url=href,
        ))
    return events


if __name__ == "__main__":
    for e in scrape():
        print(e.date, e.time, "-", e.venue, "-", e.name)
