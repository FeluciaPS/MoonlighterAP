# Pretty much copied verbatim from
# https://github.com/NewSoupVi/Archipelago/blob/apquest/worlds/apquest/web_world.py

from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups


class MoonlighterWebWorld(WebWorld):
    game = "Moonlighter"
    theme = "partyTime"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Moonlighter for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["FeluciaPS"],
    )

    tutorials = [setup_en]

    option_groups = option_groups