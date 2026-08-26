"""Scraper for IFC Center (ifccenter.com) — server-rendered weekly schedule."""
import requests
from bs4 import BeautifulSoup

from .base import Event, parse_loose_date

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")

URL = "https://www.ifccenter.com/"


def scrape() -> list[Event]:
    resp = requests.get(URL, headers={"User-Agent": UA}, timeout=20)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    events = []
    for day_div in soup.select("div.daily-schedule"):
        header = day_div.find("h3", recursive=False)
        if not header:
            continue
        date = parse_loose_date(header.get_text())
        if not date:
            continue

        film_list = day_div.find("ul", recursive=False)
        if not film_list:
            continue

        for li in film_list.find_all("li", recursive=False):
            title_el = li.select_one("div.details h3 a")
            if not title_el:
                continue
            title = title_el.get_text(strip=True)

            for time_a in li.select("ul.times li a"):
                events.append(Event(
                    type="movie",
                    name=title,
                    venue="IFC Center",
                    date=date,
                    time=time_a.get_text(strip=True),
                    url=time_a.get("href", title_el.get("href", URL)),
                ))
    return events


if __name__ == "__main__":
    for e in scrape():
        print(e.date, e.time, "-", e.venue, "-", e.name)
