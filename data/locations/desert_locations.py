INTERNAL_LOCATION_IDS = {
    "Desert Note 1": 1,
    "Desert Note 2": 2,
    "Desert Note 3": 3,
    "Defeat Naja": 10,
    "Defeat Hexa": 11,
    "Defeat Corrupted Hexa": 12,
}

LOCATION_IDS = {}

for key, value in INTERNAL_LOCATION_IDS.items():
    LOCATION_IDS[key] = int(value) + 300