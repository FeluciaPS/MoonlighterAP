INTERNAL_LOCATION_IDS = {
    "Tech Note 1": 1,
    "Tech Note 2": 2,
    "Tech Note 3": 3,
    "Defeat Energy Flux": 10,
    "Defeat Oscillator": 11,
    "Defeat Corrupted Oscillator": 12,
}

LOCATION_IDS = {}

for key, value in INTERNAL_LOCATION_IDS.items():
    LOCATION_IDS[key] = int(value) + 400