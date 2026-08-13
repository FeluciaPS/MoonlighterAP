from collections.abc import Mapping
from typing import Any
from Options import OptionError
from worlds.AutoWorld import World

from . import items, locations, options, regions, rules, web_world

class MoonlighterWorld(World):
    """
    Moonlighter is a game.
    """

    game = "Moonlighter"

    web = web_world.MoonlighterWebWorld()

    options_dataclass = options.MoonlighterOptions
    options: options.MoonlighterOptions

    # Copied from Garfield Kart
    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Town"

    # Make UT generate without yaml
    ut_can_gen_without_yaml = True


    # TODO: this shouldn't end up in v1.0 but is a good catch during development
    def pre_fill(self) -> None:
        from BaseClasses import CollectionState
        from Fill import sweep_from_pool
        state = sweep_from_pool(CollectionState(self.multiworld), self.multiworld.itempool)
        unreachable_locations = [location for location in self.get_locations() if not location.can_reach(state)]

        # I'm not good with exception types I'm sure "Exception" covers it
        if len(unreachable_locations):
            raise Exception(f"There are unreachable locations, please let Felucia know: {unreachable_locations}")
        if not len(self.multiworld.itempool):
            raise OptionError("There aren't any items in the item pool. Let Felucia know this is a bug.")

    def generate_early(self) -> None:
        pass

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_itempool(self)

    def create_item(self, name: str) -> items.MoonlighterItem:
        return items.create_item_object(self, name)

    def write_spoiler(self, spoiler_handle) -> None:
        pass

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item(self)
    
    def fill_slot_data(self) -> Mapping[str, Any]:
        slot_data = dict()

        # Pass options into slot data for the mod to use
        slot_data["options"] = self.options.as_dict(
            "goal",
            "death_link"
        )

        return slot_data
