from Options import Choice, OptionSet, Toggle


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
    Choose the equipment that should be included in the randomizer. Other equipment may be included
    as filler items, but will not be considered in logic.

    If no weapons or no armor is selected, they also will not appear as filler items.
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

class BroomOnly(Toggle):
    """
    Removes all weapons from the itempool and shops, making you beat the game with only the
    broom spear.
    """
    display_name = "Broom Only"