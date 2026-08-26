"""Scraper for Public Records (publicrecords.nyc) — WordPress + DICE ticket links."""
import re

import requests
from bs4 import BeautifulSoup

from .base import Event

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")

URL = "https://publicrecords.nyc/"

MONTHS_NUM = {m: m for m in range(1, 13)}


def _parse_date_cell(text: str, default_year: int = 2026):
    # e.g. "Tue 7.14" "Live," "7:00 pm," "Sound Room"
    m = re.search(r"(\d{1,2})\.(\d{1,2})", text)
    time_m = re.search(r"(\d{1,2}:\d{2}\s*[ap]m)", text, re.I)
    room_m = re.search(r"location[^>]*>([^<]*)", text)
    if not m:
        return None, "", ""
    month, day = int(m.group(1)), int(m.group(2))
    date = f"{default_year}-{month:02d}-{day:02d}"
    time_str = time_m.group(1) if time_m else ""
    room = room_m.group(1).strip() if room_m else ""
    return date, time_str, room


def scrape() -> list[Event]:
    resp = requests.get(URL, headers={"User-Agent": UA}, timeout=20)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    events = []
    for a in soup.select("a.event.table-row"):
        date_cell = a.select_one("div.table-cell.date")
        title_cell = a.select_one("div.table-cell.title")
        if not date_cell or not title_cell:
            continue

        date, time_str, room = _parse_date_cell(date_cell.decode_contents())
        if not date:
            continue

        name = title_cell.get_text(strip=True)
        name = re.sub(r"Get tickets\s*$", "", name).strip()

        events.append(Event(
            type="concert",
            name=name,
            venue="Public Records",
            date=date,
            time=time_str,
            url=a.get("href", URL),
        ))
    return events


if __name__ == "__main__":
    for e in scrape():
        print(e.date, e.time, "-", e.venue, "-", e.name)
