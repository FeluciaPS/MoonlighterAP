from __future__ import annotations

from Options import Toggle, DefaultOnToggle


class ProgressiveDungeonFloors(DefaultOnToggle):
    """
    Enables Progressive Dungeon Floors.

    If enabled, instead of Dungeon Unlocks unlocking all three floors of a dungeon, adds 3 Progressive Dungeon Floor unlocks for each dungeon and unlocks floors depending on how many you have.
    """
    display_name = "Progressive Dungeon Floors"

class ProgressiveDungeons(Toggle):
    """
    Enables Progressive Dungeons, unlocking dungeons in a predictable order instead of whenever you find the associated item.

    This option does not work.
    """
    display_name = "Progressive Dungeons"

class RequireSale(Toggle):
    """
    Enables Sale of Archipelago Items.

    If enabled, instead of locations sending checks directly, they drop inventory items that must be sold in your shop to send the check.
    """
    display_name = "Require Sale"

class EarlyDungeon(Toggle):
    """
    Guarantees a dungeon unlock will appear early in the game, if this is enabled your first dungeon unlock will always be in a 
    location that is available in sphere 1 in your multiworld (meaning items are required to access it)
    
    As of now, turning this off has a chance to cause generation failures (though at least 90% of generations should still succeed)

    Down the line I may add an option to specifically put it in your own world, but that's a future me problem -Felucia"""
    display_name = "Early Dungeon"