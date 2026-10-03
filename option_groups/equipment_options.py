from __future__ import annotations

from Options import Choice, OptionSet, Toggle

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..world import MoonlighterWorld

class EquipmentRandomizer(Choice):
    """
    Determines the way armour and weapons are randomised
    
    - Fully Random: Shuffles all weapons and armour into the pool randomly
    - Progressive: Progressively unlocks each equipemnt type, starting with the weakest, then the second, etc.
    - Tiered: Unlocks entire tiers of equipment at a time, unlocking Tier 1 allows you to craft all Tier 1 Equipment if you have the materials
    """
    display_name = "Equipment Randomizer"

    option_fully_random = 0
    option_progressive = 1
    option_tiered = 2

    default = 1

class IncludedEquipment(OptionSet):
    """
    Choose the equipment that will be considered for dungeon logic. All equipment selected here is guaranteed to show
    up in the item pool. Other equipment may be included as filler items, but will not be considered in logic.
    Note that removing all weapons or armor from logic can make the game significantly harder

    You can use "_allweapons" or "_allarmor" to include all weapons or armor at once.
    """
    display_name = "Included Equipment"

    valid_keys = [
        "_allweapons",
        "_allarmor",
        "Fabric",
        "Iron",
        "Steel",
        "Short Sword",
        "Big Sword",
        "Spear",
        "Gloves",
        "Bow"
    ]

    default = [key for key in valid_keys.copy() if not key.startswith("_")]

class ExcludedEquipmentBehavior(Choice):
    """
    Changes whether excluded armor and weapons are added to the filler pool or entirely excluded from the item pool

    - Filler: Excluded equipment is added to the filler pool
    - Weapons Only: Only excluded weapons are added to the filler pool, excluded armor is removed
    - Armor Only: Only excluded armor is added to the filler pool, excluded weapons are removed
    - Removed: Excluded equipment is removed from the item pool entirely.
    """
    display_name = "Include Filler Equipment"

    default = 0
    option_filler = 0
    option_weapons_only = 1
    option_armor_only = 2
    option_removed = 3

class BroomOnly(Toggle):
    """
    Removes all weapons from the itempool and shops, making you beat the game with only the
    broom spear.
    """
    display_name = "Broom Only"

def is_equipment_removed(world: MoonlighterWorld, type: str):
    if type == "weapons":
        return world.options.excluded_equipment_behavior in [ExcludedEquipmentBehavior.option_armor_only, ExcludedEquipmentBehavior.option_removed] or world.options.broom_only
    if type == "armor":
        return world.options.excluded_equipment_behavior in [ExcludedEquipmentBehavior.option_weapons_only, ExcludedEquipmentBehavior.option_removed]
    raise Exception(f"Incorrect option {type} passed into is_equipment_removed")