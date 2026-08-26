"""Scraper for Film Forum (filmforum.org) — "Playing This Week" tabbed grid.

Each tab (tabs-0..tabs-6 = Mon..Sun of the current week) has an HTML comment
like `<!-- 13 -->` giving the day-of-month; we combine that with the current
month/year to get a real date.
"""
from datetime import date as dt_date

import requests
from bs4 import BeautifulSoup, Comment

from .base import Event

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")

URL = "https://filmforum.org/"


def _resolve_date(day_of_month: int, today: dt_date) -> str:
    year, month = today.year, today.month
    # if the day-of-month is well before today's, it's likely rolled into next month
    if day_of_month < today.day - 15:
        month += 1
        if month > 12:
            month = 1
            year += 1
    return f"{year}-{month:02d}-{day_of_month:02d}"


def scrape() -> list[Event]:
    resp = requests.get(URL, headers={"User-Agent": UA}, timeout=20)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    today = dt_date.today()
    events = []
    for tab in soup.select("div.showtimes-container > div[id^='tabs-']"):
        comment = tab.find(string=lambda t: isinstance(t, Comment))
        if not comment or not comment.strip().isdigit():
            continue
        date = _resolve_date(int(comment.strip()), today)

        for p in tab.find_all("p"):
            title_el = p.select_one("strong a")
            if not title_el:
                continue
            times = [s.get_text(strip=True) for s in p.select("span")]
            title = title_el.get_text(" ", strip=True)
            film_url = title_el.get("href", URL)
            for t in times:
                events.append(Event(
                    type="movie",
                    name=title,
                    venue="Film Forum",
                    date=date,
                    time=t,
                    url=film_url,
                ))
    return events


if __name__ == "__main__":
    for e in scrape():
        print(e.date, e.time, "-", e.venue, "-", e.name)
