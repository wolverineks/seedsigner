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
        self.focused: NavKey = "bluewallet"

    def render(self) -> Node:
        focused = self.focused

        return [
            Header(
                left=BackButton(focused=focused == "back"),
                title="Coordinator Software",
            ),
            Body(
                [
                    CheckboxButton(
                        text="BlueWallet",
                        focused=focused == "bluewallet",
                        checked="bluewallet" in self.settings.coordination_software,
                        index=0,
                    ),
                    CheckboxButton(
                        text="Nunchuk",
                        focused=focused == "nunchuck",
                        checked="nunchuck" in self.settings.coordination_software,
                        index=1,
                    ),
                    CheckboxButton(
                        text="Sparrow",
                        focused=focused == "sparrow",
                        checked="sparrow" in self.settings.coordination_software,
                        index=2,
                    ),
                    CheckboxButton(
                        text="Spector Desktop",
                        focused=focused == "spector_desktop",
                        checked="spector_desktop"
                        in self.settings.coordination_software,
                        index=3,
                    ),
                    CheckboxButton(
                        text="Keeper",
                        focused=focused == "keeper",
                        checked="keeper" in self.settings.coordination_software,
                        index=4,
                    ),
                ]
            ),
        ]

    def handle_input(self, input: HWButtonInput):
        action = ACTION_MAP[self.focused].get(input)
        if action is None:
            return

        type, key = action
        if type == "navigate":
            if key == "back":
                self.router.go_back()
        elif type == "focus":
            self.set_focused(key)
        elif type == "select":
            if key not in COORDINATION_SOFTWARE_OPTIONS:
                return

            current = list(self.settings.coordination_software)
            option = key
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

Action = tuple[Literal["navigate", "focus", "select"], NavKey]

ACTION_MAP: dict[NavKey, dict[HWButtonInput, Action | None]] = {
    "back": {
        "up": None,
        "down": ("focus", "bluewallet"),
        "left": ("navigate", "back"),
        "right": ("focus", "bluewallet"),
        "select": ("navigate", "back"),
    },
    "bluewallet": {
        "up": ("focus", "back"),
        "down": ("focus", "nunchuck"),
        "left": ("focus", "back"),
        "right": ("select", "bluewallet"),
        "select": ("select", "bluewallet"),
    },
    "nunchuck": {
        "up": ("focus", "bluewallet"),
        "down": ("focus", "sparrow"),
        "left": ("focus", "back"),
        "right": ("select", "nunchuck"),
        "select": ("select", "nunchuck"),
    },
    "sparrow": {
        "up": ("focus", "nunchuck"),
        "down": ("focus", "spector_desktop"),
        "left": ("focus", "back"),
        "right": ("select", "sparrow"),
        "select": ("select", "sparrow"),
    },
    "spector_desktop": {
        "up": ("focus", "sparrow"),
        "down": ("focus", "keeper"),
        "left": ("focus", "back"),
        "right": ("select", "spector_desktop"),
        "select": ("select", "spector_desktop"),
    },
    "keeper": {
        "up": ("focus", "spector_desktop"),
        "down": None,
        "left": ("focus", "back"),
        "right": ("select", "keeper"),
        "select": ("select", "keeper"),
    },
}
