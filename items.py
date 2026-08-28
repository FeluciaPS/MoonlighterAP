from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification
from .option_groups import EquipmentRandomizer
from .data.items import item_names, equipment
from .data import DUNGEON_NAMES

if TYPE_CHECKING:
    from .world import MoonlighterWorld

ITEM_NAME_TO_ID = {
    "Unlock Golem Dungeon": 1,
    "Unlock Forest Dungeon": 2,
    "Unlock Desert Dungeon": 3,
    "Unlock Tech Dungeon": 4,

    "Progressive Golem Floor": 5,
    "Progressive Forest Floor": 6,
    "Progressive Desert Floor": 7,
    "Progressive Tech Floor": 8,

    "Golem Key": 9,
    "Forest Key": 10,
    "Desert Key": 11,
    "Tech Key": 12,

    "Filler Item": 1000,
}

class MoonlighterItem(Item):
    game = "Moonlighter"


def get_random_filler_item(world: MoonlighterWorld) -> str:
    items = item_names.FILLER_ITEMS

    return world.random.choice(items)


def create_item_object(world: MoonlighterWorld, name: str):
    # Items are assumed to be useful by default
    classification = ItemClassification.useful

    # Progression items are progression items
    if name in item_names.PROGRESSION_ITEMS:
        classification = ItemClassification.progression

    if name in item_names.FILLER_ITEMS:
        classification = ItemClassification.filler

    # Equipment is sometimes a progression item
    for category in world.options.included_equipment.value:
        if category.startswith("_"):
            continue

        if world.options.equipment_randomizer == EquipmentRandomizer.progressive:
            if name in equipment.PROGRESSIVE_EQUIPMENT_ITEM_NAMES[category]:
                classification = ItemClassification.progression
                break # Early exit for a minimal performance gain
        else:
            break # other options are unimplemented so just exit

    return MoonlighterItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: MoonlighterWorld) -> None:
    itempool: list[Item] = []

    # Dungeon unlock items
    for dungeon in DUNGEON_NAMES:
        if world.options.progressive_dungeon_floors:
            itempool += [world.create_item(f"Progressive {dungeon} Floor") for _ in range(3)]
        else:
            itempool += [world.create_item(f"Unlock {dungeon} Dungeon")]

        itempool += [world.create_item(f"{dungeon} Key")]

    # Equipment items
    starting_weapon = "Broom Spear" if world.options.broom_only else world.random.choice(equipment.STARTING_WEAPON_NAMES)
    world.push_precollected(world.create_item(starting_weapon))

    if world.options.equipment_randomizer == EquipmentRandomizer.progressive:
        for category in world.options.included_equipment.value:
            if category.startswith("_"):
                continue

            itempool += [
                world.create_item(item_name)
                    for item_name in equipment.PROGRESSIVE_EQUIPMENT_ITEM_NAMES[category]
            ]

    # Compare item pool size to location size, and fill what's left with
    # filler items.
    item_count = len(itempool)
    unfilled_location_count = len(world.multiworld.get_unfilled_locations(world.player))
    filler_item_count = unfilled_location_count - item_count
    
    itempool += [
        world.create_filler() for _ in range(filler_item_count)
    ]

    # Append the item pool to the world's
    world.multiworld.itempool += itempool