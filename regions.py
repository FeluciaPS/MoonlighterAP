from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .world import MoonlighterWorld

from BaseClasses import Region

# TODO: Names like this should probably be exiled to a file
# but that's a future me problem
DUNGEON_NAMES = [
    "Golem",
    "Forest",
    "Desert",
    "Tech",
    # "Unknown" doesn't belong here, because it's not a real dungeon
]

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

        # Various shops are easier to define as locations
        # may even be worth splitting these further down the line
        Region("Hawker", world.player, world.multiworld),
        Region("Le Retailer", world.player, world.multiworld),
        Region("The Wooden Hat", world.player, world.multiworld),
        Region("Vulcan's Forge", world.player, world.multiworld),
        # The Banker isn't real and cannot hurt you.
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

    for name in ["Unknown Dungeon", "Hawker", "Le Retailer", "The Wooden Hat", "Vulcan's Forge"]:
        region = world.get_region(name)
        town.connect(region, name)