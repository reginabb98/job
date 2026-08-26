"""Run all scrapers, annotate with taste/distance, and write data/events.json."""
import json
from datetime import datetime
from pathlib import Path

from scrapers import bowery_presents, elsewhere, public_records, tv_eye, broadway, donyc
from scrapers import metrograph, film_forum, ifc_center, nitehawk
from scrapers.base import time_sort_key, extract_trailing_year, format_time_display
import taste
import venues

DATA_FILE = Path(__file__).parent / "data" / "events.json"

SCRAPERS = [
    bowery_presents,
    elsewhere,
    public_records,
    tv_eye,
    broadway,
    donyc,
    metrograph,
    film_forum,
    ifc_center,
    nitehawk,
]


def main():
    all_events = []
    for module in SCRAPERS:
        name = module.__name__.split(".")[-1]
        try:
            events = module.scrape()
            print(f"[run] {name}: {len(events)} events")
            all_events.extend(events)
        except Exception as e:
            print(f"[run] {name} FAILED: {e}")

    seen = {}
    for e in all_events:
        d = e.to_dict()
        d["time"] = format_time_display(d["time"])
        d["time_minutes"] = time_sort_key(d["time"])
        if d["type"] == "movie":
            d["name"], d["year"] = extract_trailing_year(d["name"], d.get("year", ""))
        d["distance_mi"] = venues.distance_miles(d["venue"])
        d["transit_min"] = venues.transit_minutes(d["venue"])
        taste.annotate(d)
        seen[d["id"]] = d  # de-dupe by content hash

    result = sorted(seen.values(), key=lambda d: (d["date"], d["time_minutes"]))

    DATA_FILE.parent.mkdir(exist_ok=True)
    DATA_FILE.write_text(json.dumps({
        "generated_at": datetime.now().isoformat(),
        "events": result,
    }, indent=2))
    print(f"[run] wrote {len(result)} events to {DATA_FILE}")


if __name__ == "__main__":
    main()
