SHORT_SWORD_NAMES = [
    "Training Short Sword",
    "Soldier Short Sword",
    "Rusty Short Sword",
    "Knight Short Sword",
    "Venom Short Sword",
    "Commander Short Sword",
    "Reborn Short Sword",
    "King Short Sword",
    "Vampire Short Sword"
]

BIG_SWORD_NAMES = [
    "Training Big Sword",
    "Buster Big Sword",
    "Rock Big Sword",
    "Wild Big Sword",
    "Toxic Big Sword",
    "Vulcan Big Sword",
    "Blaze Big Sword",
    "Fusion Big Sword",
    "Storm Big Sword"
]

SPEAR_NAMES = [
    "Broom Spear",
    "Training Spear",
    "Warrior Spear",
    "Golem Drill Spear",
    "Wood's Spear",
    "Venom Sting Spear",
    "Monkey Spear",
    "Hell Spear",
    "Fighter Spear",
    "Lightning Rod Spear"
]

GLOVES_NAMES = [
    "Training Gloves",
    "Fighter Gloves",
    "Rough Gloves",
    "Forest Spirit Gloves",
    "Venom Twins Gloves",
    "Captain Gloves",
    "Flame Gloves",
    "Star Platinum Gloves",
    "Thunder Gloves"
]

BOW_NAMES = [
    "Training Bow",
    "Hunter Bow",
    "Catapult Bow",
    "Natural Bow",
    "Poison Bow",
    "Soldier Bow",
    "Flamethrower Bow",
    "Exeter Bow",
    "Lightning Bow"
]

ARMOR_ITEM_NAMES = [
    "Fabric Bandana",
    "Fabric Bandana II",
    "Fabric Bandana III",
    "Fabric Bandana IV",
    "Iron Helmet",
    "Iron Helmet II",
    "Iron Helmet III",
    "Iron Helmet IV",
    "Steel Helmet",
    "Steel Helmet II",
    "Steel Helmet III",
    "Steel Helmet IV",
    
    "Fabric Chestplate",
    "Fabric Chestplate II",
    "Fabric Chestplate III",
    "Fabric Chestplate IV",
    "Iron Chestplate",
    "Iron Chestplate II",
    "Iron Chestplate III",
    "Iron Chestplate IV",
    "Steel Chesplate",
    "Steel Chesplate II",
    "Steel Chesplate III",
    "Steel Chesplate IV",
    
    "Fabric Boots",
    "Fabric Boots II",
    "Fabric Boots III",
    "Fabric Boots IV",
    "Iron Boots",
    "Iron Boots II",
    "Iron Boots III",
    "Iron Boots IV",
    "Steel Boots",
    "Steel Boots II",
    "Steel Boots III",
    "Steel Boots IV"
]

# Progressive
WEAPON_TYPES = [
    "Short Sword",
    "Big Sword",
    "Spear",
    "Gloves",
    "Bow"
]

STARTING_WEAPON_NAMES = [f"Training {weapon}" for weapon in WEAPON_TYPES] + ["Broom Spear"]

ARMOR_TYPES = [
    "Fabric",
    "Iron",
    "Steel"
]

ARMOR_SLOTS = [
    "Helmet",
    "Chestplate",
    "Boots"
]

PROGRESSIVE_WEAPON_ITEM_DICT = {}
PROGRESSIVE_ARMOR_ITEM_DICT = {}

for type in WEAPON_TYPES:
    PROGRESSIVE_WEAPON_ITEM_DICT[type] = [
        f"Progressive {path} {type}" 
            # I'm open to better names than "Power" but elemental is good
            for path in ["Power", "Elemental"]
    ]

for type in ARMOR_TYPES:
    PROGRESSIVE_ARMOR_ITEM_DICT[type] = [
        f"Progressive {type} {"Bandana" if type == "Fabric" and slot == "Helmet" else slot}"
            for slot in ARMOR_SLOTS
    ]

for slot in ARMOR_SLOTS:
    PROGRESSIVE_ARMOR_ITEM_DICT[slot] = [
        f"Progressive {type} {"Bandana" if type == "Fabric" and slot == "Helmet" else slot}"
            for type in ARMOR_TYPES
    ]

PROGRESSIVE_HELMET_ITEM_NAMES = [
    f"Progressive {type} {"Bandana" if type == "Fabric" else "Helmet"}"
        for type in ARMOR_TYPES
]

PROGRESSIVE_CHESTPLATE_ITEM_NAMES = [
    f"Progressive {type} Chestplate"
        for type in ARMOR_TYPES
]

PROGRESSIVE_BOOTS_ITEM_NAMES = [
    f"Progressive {type} Boots"
        for type in ARMOR_TYPES
]

PROGRESSIVE_EQUIPMENT_ITEM_NAMES = {
    **PROGRESSIVE_WEAPON_ITEM_DICT,
    **PROGRESSIVE_ARMOR_ITEM_DICT,
}