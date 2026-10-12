from __future__ import annotations

from ..data.items import item_names
from Options import Toggle, Range, OptionCounter, Visibility


class Traps(Toggle):
    """
    Enables Traps.

    Traps replace filler items in your item pool with traps with negative effects.
    """
    display_name = "Enable Traps"
    visibility = Visibility.none
    
class TrapPercentage(Range):
    """
    What percentage of filler items should be replaced with traps.
    """
    display_name = "Trap Percentage"
    range_start = 0
    range_end = 100
    default = 25
    visibility = Visibility.none

class TrapWeights(OptionCounter):
    """
    Set the weight of each trap in the trap pool.
    """
    display_name  = "Trap Weights"
    min = 1
    max = 100
    default = {trap: 50 for trap in item_names.TRAP_ITEMS}
    valid_keys = item_names.TRAP_ITEMS
    visibility = Visibility.none