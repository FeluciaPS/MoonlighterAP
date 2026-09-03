from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .world import MoonlighterWorld

from .data.items import item_names

def get_trap_names (trap_item_count: int, world: MoonlighterWorld):
    Weights = [[trap, world.options.trap_weights[trap] / 100] for trap in item_names.TRAP_ITEMS]
    Totalweight = sum(Weight[1] for Weight in Weights)
    trap_pool = []
    for Weight in Weights:
        if Weight[1] == 0: continue
        Weight[1] = round((Weight[1] * trap_item_count) / Totalweight)
        trap_pool += [Weight[0] for _ in range(Weight[1])]
    roundingerror = trap_item_count - len(trap_pool)
    while roundingerror > 0:
        trap_pool += world.random.choice([(Weight[0] for _ in range(Weight[1])) for Weight in Weights])
        roundingerror -= 1
    while roundingerror < 0:
        trap_pool.remove(world.random.choice(trap_pool))
        roundingerror += 1
    return trap_pool