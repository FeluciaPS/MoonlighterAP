INTERNAL_LOCATION_IDS = {
    "Forest Note 1": 1,
    "Forest Note 2": 2,
    "Forest Note 3": 3,
    "Defeat Carnivorous Mutae": 10,
    "Defeat Mavu Tree": 11,
    "Defeat Corrupted Mavu Tree": 12,
}

LOCATION_IDS = {}

for key, value in INTERNAL_LOCATION_IDS.items():
    LOCATION_IDS[key] = int(value) + 200