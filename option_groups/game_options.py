from __future__ import annotations

from Options import Toggle


class ProgressiveFloors(Toggle):
    """
    Enables Progressive Dungeon Floors.

    If enabled, instead of Dungeon Unlocks unlocking all three floors of a dungeon, adds 3 Progressive Dungeon Floor unlocks for each dungeon and unlocks floors depending on how many you have.
    """
    display_name = "Progressive Floors"