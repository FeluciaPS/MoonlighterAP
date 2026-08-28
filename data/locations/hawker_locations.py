INTERNAL_LOCATION_IDS = {
    # Doesn't include the DLC as of yet
    # First 3 unlocked with dungeon access, 4th unlocked by defeating boss
    "Golem Banner": 1,
    "Golem Books": 2,
    "Golem Fountain": 3,
    "Golem Crystals": 4,
    
    "Forest Flowers": 5,
    "Forest Ivy": 6,
    "Fruit Bowl": 7,
    "Carnivorous Mutae Miniature": 8,
    
    "Desert Cloth": 9,
    "Lava Clock": 10,
    "Lava Fountain": 11,
    "Naja Miniature": 12,
    
    "Electric Device": 13,
    "Shock Valves": 14,
    "Tech Shelf": 15,
    "Energy Flux Miniature": 16
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