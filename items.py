from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification
from .data.items import item_names

if TYPE_CHECKING:
    from .world import MoonlighterWorld

ITEM_NAME_TO_ID = {
    "Unlock Golem Dungeon": 1,
    "Unlock Forest Dungeon": 2,
    "Unlock Desert Dungeon": 3,
    "Unlock Tech Dungeon": 4,

    "Golem Key": 5,
    "Forest Key": 6,
    "Desert Key": 7,
    "Tech Key": 8,

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

    return MoonlighterItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: MoonlighterWorld) -> None:
    itempool: list[Item] = []

    itempool += [
        world.create_item(item) for item in item_names.PROGRESSION_ITEMS
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