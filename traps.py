from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .world import MoonlighterWorld

def get_trap_names(trap_item_count: int, world: MoonlighterWorld):
    weights = world.options.trap_weights.value
    total_weight = sum(weights.values())

    # Create a perfectly weighted trap pool
    perfect_distribution = {
        trap: trap_item_count * (weight / total_weight) 
            for trap, weight in weights.items()
    }

    # Fill in everything that perfectly fits by rounding down the shares
    trap_pool = {
        trap: int(count) 
            for trap, count in perfect_distribution.items()
    }

    # Grab a sorted list of all the remainders
    remainders = sorted(
        weights.keys(), 
        key=lambda i: perfect_distribution[i] - trap_pool[i], 
        reverse=True
    )

    # Fill in the rest according to the sorted list
    to_add = trap_item_count - sum(trap_pool.values())

    for trap_name in remainders[:to_add]:
        trap_pool[trap_name] += 1

    return [
        trap 
            for trap, count in trap_pool.items() 
            for _ in range(count)
    ]