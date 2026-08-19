INTERNAL_LOCATION_IDS = {
    "Golem Note 1": 1,
    "Golem Note 2": 2,
    "Golem Note 3": 3,
    "Defeat Golem King": 10,
}

LOCATION_IDS = {}

for key, value in INTERNAL_LOCATION_IDS.items():
    LOCATION_IDS[key] = int(value) + 100