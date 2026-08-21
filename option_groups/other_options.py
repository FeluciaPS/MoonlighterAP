from __future__ import annotations

from Options import Toggle


class DeathLink(Toggle):
    """
    Enables Death Link.

    If enabled, when you die all other players with Death Link enabled also die,
    and when a player with Death Link enabled dies, your character dies too.
    """
    display_name = "Death Link"

class ProgressiveFloors(Toggle):
    """
    Enables Progressive Dungeon Floors.

    If enabled, instead of Dungeon Unlocks unlocking all three floors of a dungeon, adds 3 Progressive Dungeon Floor unlocks for each dungeon and unlocks floors depending on how many you have.
    """
    display_name = "Progressive Floors"