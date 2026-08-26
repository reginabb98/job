"""Shared Event type and helpers for all venue scrapers."""
import hashlib
import re
from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class Event:
    type: str          # "concert" or "movie"
    name: str
    venue: str
    date: str           # "YYYY-MM-DD"
    time: str = ""       # e.g. "9:00 PM" (doors/showtime, free text)
    url: str = ""
    image: str = ""
    year: str = ""        # release year, movies only, when the venue's site provides it
    genre: str = ""        # genre tag(s), when the venue's site provides them (currently Elsewhere only)

    @property
    def id(self) -> str:
        raw = f"{self.venue}|{self.name}|{self.date}|{self.time}"
        return hashlib.sha1(raw.encode()).hexdigest()[:12]

    def to_dict(self) -> dict:
        d = asdict(self)
        d["id"] = self.id
        return d


def time_sort_key(time_str: str) -> int:
    """Minutes-since-midnight for sorting, tolerant of the different formats
    each venue's site uses ("10:00pm", "10:35 AM", "23:00", "Doors: 7:30PM").
    Bare hour:minute with no AM/PM marker and hour <= 12 is assumed to be
    afternoon/evening (true for every venue we scrape that omits it)."""
    m = re.search(r"(\d{1,2}):(\d{2})\s*([AaPp][Mm])?", time_str)
    if not m:
        return 9999
    h, mm, ampm = int(m.group(1)), int(m.group(2)), m.group(3)
    if ampm:
        ampm = ampm.lower()
        if h == 12:
            h = 0
        if ampm == "pm":
            h += 12
    elif h <= 12 and h != 12:
        h += 12
    return h * 60 + mm


def format_time_display(time_str: str) -> str:
    """Normalize every venue's time format to a consistent 'H:MM AM/PM',
    preserving any prefix ("Doors: ") or suffix ("(OC)"). Uses the same
    bare-hour-is-PM heuristic as time_sort_key for venues (Film Forum) that
    omit AM/PM entirely."""
    m = re.search(r"(\d{1,2}):(\d{2})", time_str)
    if not m:
        return time_str
    h, mm = int(m.group(1)), int(m.group(2))
    prefix = time_str[:m.start()]
    rest = time_str[m.end():]

    meridiem_match = re.match(r"\s*([AaPp][Mm])", rest)
    if meridiem_match:
        ampm = "AM" if meridiem_match.group(1).lower() == "am" else "PM"
        after = rest[meridiem_match.end():].strip()
        h12 = h % 12 or 12
    else:
        after = rest.strip()
        if h > 12:
            ampm = "PM"
            h12 = h - 12
        else:
            ampm = "PM"
            h12 = h if h != 0 else 12

    formatted = f"{h12}:{mm:02d} {ampm}"
    if after:
        formatted += f" {after}"
    return f"{prefix}{formatted}"


MONTHS = {
    "jan": "01", "feb": "02", "mar": "03", "apr": "04", "may": "05", "jun": "06",
    "jul": "07", "aug": "08", "sep": "09", "oct": "10", "nov": "11", "dec": "12",
}


def extract_trailing_year(name: str, existing_year: str = "") -> tuple:
    """If a movie title ends in '(YYYY)' (a real release year, not room/tour
    noise), split it out: e.g. 'Moana (2026)' -> ('Moana', '2026'). Keeps an
    already-known year as-is."""
    if existing_year:
        return name, existing_year
    m = re.match(r"^(.*)\s+\((\d{4})\)\s*$", name)
    if m and 1900 <= int(m.group(2)) <= 2035:
        return m.group(1).strip(), m.group(2)
    return name, existing_year


def parse_loose_date(text: str, default_year: Optional[int] = None) -> Optional[str]:
    """Parse strings like 'Mon Jul 13, 2026' or 'Jul 13' into YYYY-MM-DD."""
    text = text.strip()
    m = re.search(r"([A-Za-z]{3,9})\s+(\d{1,2}),?\s*(\d{4})?", text)
    if not m:
        return None
    mon, day, year = m.groups()
    mon_key = mon.lower()[:3]
    if mon_key not in MONTHS:
        return None
    year = year or str(default_year or 2026)
    return f"{year}-{MONTHS[mon_key]}-{int(day):02d}"
