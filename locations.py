from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location
from .data import DUNGEON_NAMES, BOSS_NAMES, town_locations, golem_locations, forest_locations, desert_locations, tech_locations

from .items import MoonlighterItem
from .option_groups import goal_options

if TYPE_CHECKING:
    from .world import MoonlighterWorld

# Location names and IDs are probably going to be moved to the /data folder
# but for now there's a placeholder
LOCATION_NAME_TO_ID = {
    **town_locations.LOCATION_IDS,
    **golem_locations.LOCATION_IDS,
    **forest_locations.LOCATION_IDS,
    **desert_locations.LOCATION_IDS,
    **tech_locations.LOCATION_IDS,
}


class MoonlighterLocation(Location):
    game = "Moonlighter"


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: MoonlighterWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: MoonlighterWorld) -> None:
    # Town locations
    town = world.get_region("Town")

    town_locations = get_location_names_with_ids(["Tree Money"])
    town.add_locations(town_locations, MoonlighterLocation)

    # Dungeon locations
    for dungeon in DUNGEON_NAMES:
        region_1 = world.get_region(f"{dungeon} Dungeon I")
        region_3 = world.get_region(f"{dungeon} Dungeon III")

        region_1_locations = get_location_names_with_ids([
            f"{dungeon} Note {n+1}" for n in range(3)
        ])

        region_3_locations = get_location_names_with_ids([f"Defeat {BOSS_NAMES[dungeon]}"])

        region_1.add_locations(region_1_locations, MoonlighterLocation)
        region_3.add_locations(region_3_locations, MoonlighterLocation)


def create_events(world: MoonlighterWorld) -> None:
    unknown_dungeon = world.get_region("Unknown Dungeon")

    # Victory events dictate the victory condition later
    if world.options.goal == goal_options.Goal.option_5th_dungeon:
        unknown_dungeon.add_event(
            "Enter Unknown Dungeon", "Victory", location_type=MoonlighterLocation, item_type=MoonlighterItem
        )
    elif world.options.goal == goal_options.Goal.option_pirate_boss:
        unknown_dungeon.add_event(
            "Defeat Last Dimensional Pirate", "Victory", location_type=MoonlighterLocation, item_type=MoonlighterItem
        )
