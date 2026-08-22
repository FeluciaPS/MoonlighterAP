from __future__ import annotations

from Options import Toggle


class DeathLink(Toggle):
    """
    Enables Death Link.

    If enabled, when you die all other players with Death Link enabled also die,
    and when a player with Death Link enabled dies, your character dies too.
    """
    display_name = "Death Link"