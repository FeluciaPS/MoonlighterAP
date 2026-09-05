from ..items import equipment

TRAINING_FORGE_LOCATION_IDS = {
    "Craft Training Short Sword": 10,
    "Craft Training Big Sword": 11,
    "Craft Training Spear": 12,
    "Craft Training Gloves": 13,
    "Craft Training Bow": 14,
}

WEAPON_FORGE_LOCATION_IDS = {
    # Golem

    "Craft Soldier Short Sword": 15,
    "Craft Rusty Short Sword": 16,
    "Craft Buster Big Sword": 17,
    "Craft Rock Big Sword": 18,
    "Craft Warrior Spear": 19,
    "Craft Golem Drill Spear": 20,
    "Craft Fighter Gloves": 21,
    "Craft Rough Gloves": 22,
    "Craft Hunter Bow": 23,
    "Craft Catapult Bow": 24,
    
    # Forest
    "Craft Knight Short Sword": 25,
    "Craft Venom Short Sword": 26,
    "Craft Wild Big Sword": 27,
    "Craft Toxic Big Sword": 28,
    "Craft Wood's Spear": 29,
    "Craft Venom Sting Spear": 30,
    "Craft Forest Spirit Gloves": 31,
    "Craft Venom Twins Gloves": 32,
    "Craft Natural Bow": 33,
    "Craft Poison Bow": 34,
    
    # Desert
    "Craft Commander Short Sword": 35,
    "Craft Reborn Short Sword": 36,
    "Craft Vuclan Big Sword": 37,
    "Craft Blaze Big Sword": 38,
    "Craft Monkey Spear": 39,
    "Craft Hell Spear": 40,
    "Craft Captain Gloves": 41,
    "Craft Flame Gloves": 42,
    "Craft Soldier Bow": 43,
    "Craft Flamethrower Bow": 44,
    
    # Tech
    "Craft King Short Sword": 45,
    "Craft Vampire Short Sword": 46,
    "Craft Fusion Big Sword": 47,
    "Craft Storm Big Sword": 48,
    "Craft Fighter Spear": 49,
    "Craft Lightning Rod Spear": 50,
    "Craft Star Platinum Gloves": 51,
    "Craft Thunder Gloves": 52,
    "Craft Exeter Bow": 53,
    "Craft Lightning Bow": 54,
}

# For the time being we need to consider upgrades for armour locations because
# otherwise there aren't enough locations in the pool to fit everything.
ARMOR_FORGE_LOCATION_IDS = {}
for index, name in enumerate(equipment.ARMOR_ITEM_NAMES):
    ARMOR_FORGE_LOCATION_IDS[f"Craft {name}"] = index + 55

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