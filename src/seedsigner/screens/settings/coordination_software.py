from typing import Literal, TYPE_CHECKING

from seedsigner.components import CheckboxButton
from seedsigner.settings.coordination_software import (
    COORDINATION_SOFTWARE_OPTIONS,
)

if TYPE_CHECKING:
    from seedsigner.router import Router
    from seedsigner.store import Store
    from seedsigner.settings import Settings

from seedsigner.components import Body, Header, BackButton
from seedsigner.loopyUI import Component, Node
from seedsigner.loopyUI.events.types import HWButtonInput


class CoordinationSoftwareScreen(Component):
    def __init__(self, store: "Store", router: "Router", settings: "Settings") -> None:
        super().__init__()
        self.store = store
        self.router = router
        self.settings = settings
        self.selected: NavKey = "bluewallet"

    def render(self) -> Node:
        selected = self.selected

        return [
            Header(
                left=BackButton(selected=selected == "back"),
                title="Coordinator Software",
            ),
            Body(
                [
                    CheckboxButton(
                        text="BlueWallet",
                        selected=selected == "bluewallet",
                        checked="bluewallet" in self.settings.coordination_software,
                        index=0,
                    ),
                    CheckboxButton(
                        text="Nunchuk",
                        selected=selected == "nunchuck",
                        checked="nunchuck" in self.settings.coordination_software,
                        index=1,
                    ),
                    CheckboxButton(
                        text="Sparrow",
                        selected=selected == "sparrow",
                        checked="sparrow" in self.settings.coordination_software,
                        index=2,
                    ),
                    CheckboxButton(
                        text="Spector Desktop",
                        selected=selected == "spector_desktop",
                        checked="spector_desktop"
                        in self.settings.coordination_software,
                        index=3,
                    ),
                    CheckboxButton(
                        text="Keeper",
                        selected=selected == "keeper",
                        checked="keeper" in self.settings.coordination_software,
                        index=4,
                    ),
                ]
            ),
        ]

    def handle_input(self, input: HWButtonInput):
        if input == "select":
            self.handle_select()
        elif input == "left" and self.selected == "back":
            self.handle_select()
        else:
            selected = self.selected
            if input in nav_map[selected]:
                self.set_selected(nav_map[selected][input])

    def handle_select(self):
        selected = self.selected
        router = self.router

        print(f"Selected {selected}")
        if selected == "back":
            router.go_back()
        else:
            if selected not in COORDINATION_SOFTWARE_OPTIONS:
                return

            current = list(self.settings.coordination_software)
            option = selected
            if option in current:
                current.remove(option)
            else:
                current.append(option)
            self.settings.coordination_software = current


NavKey = Literal[
    "bluewallet",
    "nunchuck",
    "sparrow",
    "spector_desktop",
    "keeper",
    "back",
]

nav_map: dict[NavKey, dict[HWButtonInput, NavKey]] = {
    "back": {
        "right": "bluewallet",
        "down": "bluewallet",
    },
    "bluewallet": {
        "down": "nunchuck",
        "up": "back",
        "left": "back",
    },
    "nunchuck": {
        "up": "bluewallet",
        "down": "sparrow",
        "left": "back",
    },
    "sparrow": {
        "up": "nunchuck",
        "down": "spector_desktop",
        "left": "back",
    },
    "spector_desktop": {
        "up": "sparrow",
        "down": "keeper",
        "left": "back",
    },
    "keeper": {
        "up": "spector_desktop",
        "left": "back",
    },
}
