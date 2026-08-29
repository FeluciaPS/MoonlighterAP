from __future__ import annotations

from dataclasses import dataclass
from Options import OptionGroup, PerGameCommonOptions
from .option_groups import *

@dataclass
class MoonlighterOptions(PerGameCommonOptions):
    # Goal Options
    goal: Goal

    # Game Options
    progressive_dungeon_floors: ProgressiveDungeonFloors
    progressive_dungeons: ProgressiveDungeons

    # Item Options
    equipment_randomizer: EquipmentRandomizer
    included_equipment: IncludedEquipment
    broom_only: BroomOnly

    # Other Options
    death_link: DeathLink

    '''
    Some option plans so I don't forget them:
    - start_with_dungeon - If disabled, only town checks will be available at the start
    - progressive_dungeons - Unlocks dungeons in order instead of randomly
    '''


option_groups = [
    OptionGroup(
        "Goal Options",
        [Goal],
    ),
    OptionGroup(
        "Game Options",
        [ProgressiveDungeonFloors, ProgressiveDungeons],
    ),
    OptionGroup(
        "Equipment Options",
        [EquipmentRandomizer, IncludedEquipment, BroomOnly]
    ),
    OptionGroup(
        "Other Randomizer Options",
        [DeathLink],
    ),
]