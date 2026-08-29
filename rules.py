from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, HasAny, HasAnyCount, Rule, True_

from .option_groups import Goal

from .data import DUNGEON_NAMES, equipment

if TYPE_CHECKING:
    from .world import MoonlighterWorld

def set_all_rules(world: MoonlighterWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def has_dungeon_entrance(dungeon: str, floor: int):
    if dungeon == "Unknown":
        return HasAll("Golem Key", "Forest Key", "Desert Key", "Tech Key")

    return Has(f"Unlock {dungeon} Dungeon") | Has(f"Progressive {dungeon} Floor", floor)


def can_enter_dungeon(world: MoonlighterWorld, dungeon: str, floor: int = 3) -> Rule:
    key_rule = has_dungeon_entrance(dungeon, floor)
    tier = world.dungeon_order.index(dungeon) if dungeon != "Unknown" else -1
    required_level = tier if floor < 3 else tier + 1

    # Hardcoding this seems easiest
    if dungeon == "Unknown":
        required_level = 4

    if required_level == 0:
        # You should always have one of the base weapons, but I think a rule is still appropriate
        return key_rule & HasAny(*equipment.STARTING_WEAPON_NAMES)

    required_items = {
        "weapon": {}
    }

    for value in equipment.PROGRESSIVE_WEAPON_ITEM_DICT.values():
        for item in value:
            required_items["weapon"][item] = required_level

    armor_items = {
        "helmet": equipment.PROGRESSIVE_HELMET_ITEM_NAMES,
        "chestplate": equipment.PROGRESSIVE_CHESTPLATE_ITEM_NAMES,
        "boots": equipment.PROGRESSIVE_BOOTS_ITEM_NAMES
    }

    for key, value in armor_items.items():
        required_items[key] = {}
        for item in value:
            required_items[key][item] = required_level

    equipment_rule = True_()

    for key, value in required_items.items():
        equipment_rule &= HasAnyCount(value)

    return key_rule & equipment_rule

def set_all_entrance_rules(world: MoonlighterWorld) -> None:
    numerals = ["I", "II", "III"]
    for dungeon in DUNGEON_NAMES:
        for floor in range(3):
            dungeon_floor = world.get_entrance(f"{dungeon} Dungeon {numerals[floor]} Entrance")
            rule = can_enter_dungeon(world, dungeon, floor + 1)
            world.set_rule(dungeon_floor, rule)

    unknown_entrance = world.get_entrance("Unknown Dungeon Entrance")
    world.set_rule(unknown_entrance, can_enter_dungeon(world, "Unknown"))

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