from . import equipment

DUNGEON_ITEMS = [
    "Unlock Golem Dungeon",
    "Unlock Forest Dungeon",
    "Unlock Desert Dungeon",
    "Unlock Tech Dungeon",

    "Progressive Golem Floor",
    "Progressive Forest Floor",
    "Progressive Desert Floor",
    "Progressive Tech Floor",

    "Golem Key",
    "Forest Key",
    "Desert Key",
    "Tech Key",
]

FILLER_ITEMS = [
    "Money"
]

DECORATION_ITEMS = [
    "Carnivorous Mutae Miniature",
    "Desert Cloth",
    "Desert Lava Idol Decoration",
    "Dimensional Fungus Colony",
    "Dimensional Whole",
    "Electric Device",
    "Energy Flux Miniature",
    "Forest Flowers",
    "Forest Ivy",
    "Forest Wood Figure Decoration",
    "Fruit Bowl",
    "Golem Banner",
    "Golem Books",
    "Golem Crystals",
    "Golem Fountain",
    "Golem Statue Decoration",
    "Lava Clock",
    "Lava Fountain",
    "Monster Skull Decoration",
    "Naja Miniature",
    "Shock Valves",
    "Shopkeeper's Pot",
    "Spectral Sconce",
    "Tech Recycled Metal Ball Decoration",
    "Tech Shelf",
]

TRAP_ITEMS = [
    "Demand Trap",
    "Enemy Trap",
    "Thief Trap",
]
# Traps are unimplemented so these are just dummy traps for now.

ITEM_IDS = {}

n = 1
for name in DUNGEON_ITEMS:
    ITEM_IDS[name] = n
    n += 1

for name in FILLER_ITEMS:
    ITEM_IDS[name] = n
    n += 1

for name in DECORATION_ITEMS:
    ITEM_IDS[name] = n
    n += 1

for name in TRAP_ITEMS:
    ITEM_IDS[name] = n
    n += 1

for value in equipment.PROGRESSIVE_EQUIPMENT_ITEM_NAMES.values():
    for name in value:
        ITEM_IDS[name] = n
        n += 1

for name in equipment.STARTING_WEAPON_NAMES:
    ITEM_IDS[name] = n
    n += 1