from __future__ import annotations

from dataclasses import dataclass
from Options import OptionGroup, PerGameCommonOptions
from .option_groups import *

@dataclass
class MoonlighterOptions(PerGameCommonOptions):
    # Goal Options
    goal: Goal

    # Other Options
    death_link: DeathLink

    '''
    Some option plans so I don't forget them:
    - start_with_dungeon - If disabled, only town checks will be available at the start
    - randomize_dungeon_floors - Splits dungeon unlocks into (progressive) floor unlocks
    - progressive_dungeons - Unlocks dungeons in order instead of randomly
    '''


option_groups = [
    OptionGroup(
        "Goal Options",
        [Goal],
    ),
      OptionGroup(
        "Other Randomizer Options",
        [DeathLink],
    ),
]