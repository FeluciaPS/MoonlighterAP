from ..items import equipment

TRAINING_FORGE_LOCATION_IDS = {
    "Training Short Sword": 10,
    "Training Big Sword": 11,
    "Training Spear": 12,
    "Training Gloves": 13,
    "Training Bow": 14,
}

WEAPON_FORGE_LOCATION_IDS = {
    # Golem

    "Soldier Short Sword": 15,
    "Rusty Short Sword": 16,
    "Buster Big Sword": 17,
    "Rock Big Sword": 18,
    "Warrior Spear": 19,
    "Golem Drill Spear": 20,
    "Fighter Gloves": 21,
    "Rough Gloves": 22,
    "Hunter Bow": 23,
    "Catapult Bow": 24,
    
    # Forest
    "Knight Short Sword": 25,
    "Venom Short Sword": 26,
    "Wild Big Sword": 27,
    "Toxic Big Sword": 28,
    "Wood's Spear": 29,
    "Venom Sting Spear": 30,
    "Forest Spirit Gloves": 31,
    "Venom Twins Gloves": 32,
    "Natural Bow": 33,
    "Poison Bow": 34,
    
    # Desert
    "Commander Short Sword": 35,
    "Reborn Short Sword": 36,
    "Vuclan Big Sword": 37,
    "Blaze Big Sword": 38,
    "Monkey Spear": 39,
    "Hell Spear": 40,
    "Captain Gloves": 41,
    "Flame Gloves": 42,
    "Soldier Bow": 43,
    "Flamethrower Bow": 44,
    
    # Tech
    "King Short Sword": 45,
    "Vampire Short Sword": 46,
    "Fusion Big Sword": 47,
    "Storm Big Sword": 48,
    "Fighter Spear": 49,
    "Lightning Rod Spear": 50,
    "Star Platinum Gloves": 51,
    "Thunder Gloves": 52,
    "Exeter Bow": 53,
    "Lightning Bow": 54,
}

# For the time being we need to consider upgrades for armour locations because
# otherwise there aren't enough locations in the pool to fit everything.
ARMOR_FORGE_LOCATION_IDS = {}
for index, name in enumerate(equipment.ARMOR_ITEM_NAMES):
    ARMOR_FORGE_LOCATION_IDS[f"{name}"] = index + 55

INTERNAL_LOCATION_IDS = {
    **ARMOR_FORGE_LOCATION_IDS,
    **TRAINING_FORGE_LOCATION_IDS,
    **WEAPON_FORGE_LOCATION_IDS
}

# Used in locations.py to create checks
forge_location_groups = {
    "Golem": (15, 24),
    "Forest": (25, 34),
    "Desert": (35, 44),
    "Tech": (45, 54),
}

LOCATION_IDS = {}

for key, value in INTERNAL_LOCATION_IDS.items():
    LOCATION_IDS[key] = int(value) + 600