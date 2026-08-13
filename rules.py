from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule, True_

from .option_groups import Goal

if TYPE_CHECKING:
    from .world import MoonlighterWorld

def set_all_rules(world: MoonlighterWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: MoonlighterWorld) -> None:
    pass

def set_all_location_rules(world: MoonlighterWorld) -> None:
    pass

def set_completion_condition(world: MoonlighterWorld) -> None:

    # The "Victory" event will only exist for the goals that need it,
    # so checking which goal is set is unnecessary
    generic_rule = Has("Victory")

    # The Collector goal has no Victory event, so it needs its own rule
    # TODO: Actually write this rule
    collector_rule = OptionFilter(Goal, Goal.option_collector) & True_

    completion_rule = generic_rule | collector_rule
    world.set_completion_rule(completion_rule)