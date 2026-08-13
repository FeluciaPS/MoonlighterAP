from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import MoonlighterWorld

# Location names and IDs are probably going to be moved to the /data folder
# but for now there's a placeholder
LOCATION_NAME_TO_ID = {}


class MoonlighterLocation(Location):
    game = "Moonlighter"


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: MoonlighterWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: MoonlighterWorld) -> None:
    pass


def create_events(world: MoonlighterWorld) -> None:
    unknown_dungeon = world.get_region("Unknown Dungeon")

    # Victory events dictate the victory condition later
    if world.options.goal == "5th_dungeon":
        unknown_dungeon.add_event(
            "Enter Unknown Dungeon", "Victory", location_type=MoonlighterLocation, item_type=items.MoonlighterItem
        )
    else:
        unknown_dungeon.add_event(
            "Defeat Last Dimensional Pirate", "Victory", location_type=MoonlighterLocation, item_type=items.MoonlighterItem
        )
