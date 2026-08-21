from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule, True_

from .option_groups import Goal, ProgressiveFloors

if TYPE_CHECKING:
    from .world import MoonlighterWorld

def set_all_rules(world: MoonlighterWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: MoonlighterWorld) -> None:
    golem_floor_1 = world.get_entrance("Golem Dungeon I")
    golem_floor_2 = world.get_entrance("Golem Dungeon II")
    golem_floor_3 = world.get_entrance("Golem Dungeon III")
    forest_floor_1 = world.get_entrance("Forest Dungeon I")
    forest_floor_2 = world.get_entrance("Forest Dungeon II")
    forest_floor_3 = world.get_entrance("Forest Dungeon III")
    desert_floor_1 = world.get_entrance("Desert Dungeon I")
    desert_floor_2 = world.get_entrance("Desert Dungeon II")
    desert_floor_3 = world.get_entrance("Desert Dungeon III")
    tech_floor_1 = world.get_entrance("Tech Dungeon I")
    tech_floor_2 = world.get_entrance("Tech Dungeon II")
    tech_floor_3 = world.get_entrance("Tech Dungeon III")
    unknown_entrance = world.get_entrance("Unknown Dungeon")
    world.set_rule(golem_floor_1, Has("Unlock Golem Dungeon") | Has("Progressive Golem Floor", 1))
    world.set_rule(golem_floor_2, OptionFilter(ProgressiveFloors, False) | Has("Progressive Golem Floor", 2))
    world.set_rule(golem_floor_3, OptionFilter(ProgressiveFloors, False) | Has("Progressive Golem Floor", 3))
    world.set_rule(forest_floor_1, Has("Unlock Forest Dungeon") | Has("Progressive Forest Floor", 1))
    world.set_rule(forest_floor_2, OptionFilter(ProgressiveFloors, False) | Has("Progressive Forest Floor", 2))
    world.set_rule(forest_floor_3, OptionFilter(ProgressiveFloors, False) | Has("Progressive Forest Floor", 3))
    world.set_rule(desert_floor_1, Has("Unlock Desert Dungeon") | Has("Progressive Desert Floor", 1))
    world.set_rule(desert_floor_2, OptionFilter(ProgressiveFloors, False) | Has("Progressive Desert Floor", 2))
    world.set_rule(desert_floor_3, OptionFilter(ProgressiveFloors, False) | Has("Progressive Desert Floor", 3))
    world.set_rule(tech_floor_1, Has("Unlock Tech Dungeon") | Has("Progressive Tech Floor", 1))
    world.set_rule(tech_floor_2, OptionFilter(ProgressiveFloors, False) | Has("Progressive Tech Floor", 2))
    world.set_rule(tech_floor_3, OptionFilter(ProgressiveFloors, False) | Has("Progressive Tech Floor", 3))
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