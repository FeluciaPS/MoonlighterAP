from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location
from .data import DUNGEON_NAMES, BOSS_NAMES, town_locations, golem_locations, forest_locations, desert_locations, tech_locations, hawker_locations, forge_locations

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
    **hawker_locations.LOCATION_IDS,
    **forge_locations.LOCATION_IDS
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


    # Training weapons only require 
    golem_region = world.get_region(f"Golem Dungeon I")
    training_locations = get_location_names_with_ids([*forge_locations.TRAINING_FORGE_LOCATION_IDS])
    golem_region.add_locations(training_locations, MoonlighterLocation)

    # Dungeon locations
    for dungeon_index, dungeon in enumerate(DUNGEON_NAMES):
        region_1 = world.get_region(f"{dungeon} Dungeon I")
        region_2 = world.get_region(f"{dungeon} Dungeon II")
        region_3 = world.get_region(f"{dungeon} Dungeon III")

        # Carl notes
        region_1_locations = get_location_names_with_ids([
            f"{dungeon} Note {n+1}" for n in range(3)     
        ])

        # Boss defeat
        region_3_locations = get_location_names_with_ids([f"Defeat {BOSS_NAMES[dungeon]}"])

        region_1.add_locations(region_1_locations, MoonlighterLocation)
        region_3.add_locations(region_3_locations, MoonlighterLocation)


        # Hawker locations
        hawker_locations_preboss = get_location_names_with_ids([
            location for location, value in hawker_locations.LOCATION_IDS.items()
            if value % 4 != 0
        ])
            
        hawker_locations_postboss = get_location_names_with_ids([
            location for location, value in hawker_locations.LOCATION_IDS.items()
            if value % 4 == 0
        ])
        region_1.add_locations(hawker_locations_preboss, MoonlighterLocation)
        region_3.add_locations(hawker_locations_postboss, MoonlighterLocation)

        # Forge armour locations
        # Crafting armour in the forge only requires items found on floor 1 of every dungeon
        forge_armor_locations = get_location_names_with_ids([
            location_name for location_name, location_id in forge_locations.ARMOR_FORGE_LOCATION_IDS.items()
                if (location_id - 56 - dungeon_index) % 4 == 0
        ])

        region_1.add_locations(forge_armor_locations)
        
        # Forge locations
        # Every weapon except the training weapons require floor 2 items to craft
        forge_group_start, forge_group_end = forge_locations.forge_location_groups[dungeon]

        forge_group_locations = get_location_names_with_ids([
            location_name for location_name, location_id in forge_locations.WEAPON_FORGE_LOCATION_IDS.items()
                if forge_group_start <= location_id <= forge_group_end
        ])

        region_2.add_locations(forge_group_locations, MoonlighterLocation)


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
