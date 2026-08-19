from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .world import MoonlighterWorld

from BaseClasses import Region
from .data import DUNGEON_NAMES, SHOP_NAMES


def create_and_connect_regions(world: MoonlighterWorld):
    create_regions(world)
    connect_regions(world)

def create_regions(world: MoonlighterWorld):

    # Town serves as the origin region
    town = Region("Town", world.player, world.multiworld)
    
    regions = [
        town
    ]

    # Add a region for each of the 3 floors in each dungeon.
    # Worst case scenario we won't end up using all 3 and we just flatten it later
    regions += [
        Region(f'{dungeon} Dungeon {floor}', world.player, world.multiworld) 
            for dungeon in DUNGEON_NAMES 
            for floor in ["I", "II", "III"]
    ]

    regions += [
        # Unknown Dungeon doesn't have floors
        Region("Unknown Dungeon", world.player, world.multiworld),
    ]

    # Various shops are easier to define as regions
    # may even be worth splitting these further down the line
    regions += [
        Region(shop, world.player, world.multiworld) 
            for shop in SHOP_NAMES
    ]
    
    world.multiworld.regions += regions

def connect_regions(world: MoonlighterWorld):
    town = world.get_region("Town")

    for dungeon in DUNGEON_NAMES:
        region_1 = world.get_region(f'{dungeon} Dungeon I')
        region_2 = world.get_region(f'{dungeon} Dungeon II')
        region_3 = world.get_region(f'{dungeon} Dungeon III')

        town.connect(region_1, f'{dungeon} Dungeon I')
        region_1.connect(region_2, f'{dungeon} Dungeon II')
        region_2.connect(region_3, f'{dungeon} Dungeon III')

    for name in SHOP_NAMES:
        region = world.get_region(name)
        town.connect(region, name)

    unknown_dungeon = world.get_region("Unknown Dungeon")
    town.connect(unknown_dungeon, "Unknown Dungeon")