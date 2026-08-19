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
    golem_entrance = world.get_entrance("Golem Dungeon I")
    forest_entrance = world.get_entrance("Forest Dungeon I")
    desert_entrance = world.get_entrance("Desert Dungeon I")
    tech_entrance = world.get_entrance("Tech Dungeon I")
    unknown_entrance = world.get_entrance("Unknown Dungeon")

    world.set_rule(golem_entrance, Has("Unlock Golem Dungeon"))
    world.set_rule(forest_entrance, Has("Unlock Forest Dungeon"))
    world.set_rule(desert_entrance, Has("Unlock Desert Dungeon"))
    world.set_rule(tech_entrance, Has("Unlock Tech Dungeon"))
    world.set_rule(unknown_entrance, HasAll("Golem Key", "Forest Key", "Desert Key", "Tech Key"))

def set_all_location_rules(world: MoonlighterWorld) -> None:
    pass

def set_completion_condition(world: MoonlighterWorld) -> None:

    # The "Victory" event will only exist for the goals that need it,
    # so checking which goal is set is unnecessary
    generic_rule = Has("Victory")

    # The Collector goal has no Victory event, so it needs its own rule
    # TODO: Actually write this rule
    collector_rule = OptionFilter(Goal, Goal.option_collector) & True_()

    completion_rule = generic_rule | collector_rule
    world.set_completion_rule(completion_rule)