from __future__ import annotations

from Options import Toggle
from worlds.ladx.Options import DefaultOffToggle


class ProgressiveDungeonFloors(Toggle):
    """
    Enables Progressive Dungeon Floors.

    If enabled, instead of Dungeon Unlocks unlocking all three floors of a dungeon, adds 3 Progressive Dungeon Floor unlocks for each dungeon and unlocks floors depending on how many you have.
    """
    display_name = "Progressive Dungeon Floors"

class ProgressiveDungeons(DefaultOffToggle):
    """
    Enables Progressive Dungeons, unlocking dungeons in a predictable order instead of whenever you find the associated item.

    This option does not work.
    """
    display_name = "Progressive Dungeons"