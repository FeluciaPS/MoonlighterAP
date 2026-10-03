INTERNAL_LOCATION_IDS = {
    # Doesn't include the DLC as of yet
    # First 3 unlocked with dungeon access, 4th unlocked by defeating boss
    "Buy Golem Banner": 1,
    "Buy Golem Books": 2,
    "Buy Golem Fountain": 3,
    "Buy Golem Crystals": 4,
    
    "Buy Forest Flowers": 5,
    "Buy Forest Ivy": 6,
    "Buy Fruit Bowl": 7,
    "Buy Carnivorous Mutae Miniature": 8,
    
    "Buy Desert Cloth": 9,
    "Buy Lava Clock": 10,
    "Buy Lava Fountain": 11,
    "Buy Naja Miniature": 12,
    
    "Buy Electric Device": 13,
    "Buy Shock Valves": 14,
    "Buy Tech Shelf": 15,
    "Buy Energy Flux Miniature": 16
}

LOCATION_IDS = {}

# Used in locations.py to create checks
hawker_location_groups = {
    "Golem": (1, 4),
    "Forest": (5, 8),
    "Desert": (9, 12),
    "Tech": (13, 16),
}

for key, value in INTERNAL_LOCATION_IDS.items():
    LOCATION_IDS[key] = int(value) + 500