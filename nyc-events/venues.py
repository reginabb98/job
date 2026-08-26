"""Known venue metadata: address + approximate coordinates, for distance ranking.

Coordinates are approximate (good enough for relative "closer/farther" ranking,
not turn-by-turn directions).
"""
import math
from typing import Optional

HOME = {"name": "East Williamsburg (924 Metropolitan Ave)", "lat": 40.7057, "lon": -73.9260}

VENUE_COORDS = {
    "Mercury Lounge": (40.7217, -73.9878),
    "Bowery Ballroom": (40.7202, -73.9925),
    "Baby's All Right": (40.7096, -73.9578),
    "Music Hall of Williamsburg": (40.7215, -73.9575),
    "Warsaw": (40.7211, -73.9418),
    "Elsewhere": (40.7057, -73.9219),
    "Public Records": (40.6789, -73.9887),
    "TV Eye": (40.7060, -73.9226),
    "Alphaville": (40.7048, -73.9236),
    "Metrograph": (40.7147, -73.9908),
    "Film Forum": (40.7288, -74.0026),
    "IFC Center": (40.7317, -74.0016),
    "Nitehawk Cinema (Williamsburg)": (40.7138, -73.9578),
    "Nitehawk Cinema (Prospect Park)": (40.6614, -73.9724),
    "The Broadway": (40.6890, -73.9187),
    "Union Pool": (40.7215, -73.9553),
    "Arlene's Grocery": (40.7217, -73.9873),
    "Heaven Can Wait": (40.7276, -73.9803),
    "Angelika Film Center": (40.7259, -73.9959),
}


def distance_miles(venue_name: str) -> Optional[float]:
    coords = VENUE_COORDS.get(venue_name)
    if not coords:
        return None
    lat1, lon1 = math.radians(HOME["lat"]), math.radians(HOME["lon"])
    lat2, lon2 = math.radians(coords[0]), math.radians(coords[1])
    dlat, dlon = lat2 - lat1, lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    return round(3958.8 * c, 1)


# Rough door-to-door subway time in minutes from home (walk + ride + walk),
# based on actual known NYC subway routes from the L stops near Morgan Ave /
# Jefferson St (East Williamsburg). Not live MTA data (no such API is wired
# in) — hand-estimated per venue, good enough for relative "how far a schlep
# is this" judgment, not a promise of exact arrival time.
TRANSIT_MINUTES = {
    "Mercury Lounge": 28,
    "Bowery Ballroom": 30,
    "Baby's All Right": 19,
    "Music Hall of Williamsburg": 18,
    "Warsaw": 28,
    "Elsewhere": 8,
    "Public Records": 48,
    "TV Eye": 12,
    "Alphaville": 14,
    "Metrograph": 28,
    "Film Forum": 35,
    "IFC Center": 35,
    "Nitehawk Cinema (Williamsburg)": 20,
    "Nitehawk Cinema (Prospect Park)": 48,
    "The Broadway": 18,
    "Union Pool": 16,
    "Arlene's Grocery": 28,
    "Heaven Can Wait": 28,
    "Angelika Film Center": 30,
}


def transit_minutes(venue_name: str) -> Optional[int]:
    return TRANSIT_MINUTES.get(venue_name)
