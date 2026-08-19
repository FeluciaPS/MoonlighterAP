from __future__ import annotations

from Options import Choice


class Goal(Choice):
    """
    Determines what the goal is for beating the game.
    - 5th Dungeon: Collect 4 dungeon keys and enter the 5th dungeon.
    - Pirate Boss: Collect 4 dungeon keys, enter the 5th dungeon, and defeat the Last Dimensional Pirate. (Not tested)
    - Collector: Discover 100% of the Notebook. (Not implemented)
    """
    display_name = "Goal"

    default = 1
    option_5th_dungeon = 0
    option_pirate_boss = 1
    option_collector = 2
    