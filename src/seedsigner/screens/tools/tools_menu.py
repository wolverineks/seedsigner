from typing import Literal, TYPE_CHECKING, Tuple

if TYPE_CHECKING:
    from seedsigner.router import Router
    from seedsigner.settings.settings import Settings
    from seedsigner.store import Store

from seedsigner.components import Header, Body, BackButton, Button
from seedsigner.loopyUI import Component, Node, HWButtonInput


class ToolsMenuScreen(Component):
    def __init__(self, store: "Store", router: "Router", settings: "Settings") -> None:
        super().__init__()
        self.store = store
        self.router = router
        self.settings = settings
        self.selected: NavKey = "new_seed_camera"

    def render(self) -> Node:
        selected = self.selected

        return [
            Header(
                left=BackButton(selected=selected == "back"),
                title="Tools",
            ),
            Body(
                Button(
                    text="New seed (camera)",
                    selected=selected == "new_seed_camera",
                ),
                Button(
                    text="New seed (dice)",
                    selected=selected == "new_seed_dice",
                    y=Button.height + Body.padding,
                ),
                Button(
                    text="Calc 12th/24th word",
                    selected=selected == "calculate_checksum",
                    y=(Button.height + Body.padding) * 2,
                ),
                Button(
                    text="Address Explorer",
                    selected=selected == "address_explorer",
                    y=(Button.height + Body.padding) * 3,
                ),
                Button(
                    text="Verify Address",
                    selected=selected == "verify_address",
                    y=(Button.height + Body.padding) * 4,
                ),
            ),
        ]

    def handle_input(self, input: HWButtonInput):
        if input == "select":
            self.handle_select()
            return

        action = ACTION_MAP[self.selected].get(input)
        if action is None:
            return

        type, key = action
        if type == "navigate":
            if key == "back":
                self.router.go_back()
            else:
                self.router.navigate_to(key)
        elif type == "focus":
            self.set_selected(key)

    def handle_select(self):
        selected = self.selected
        print(f"Selected {selected}")
        if selected == "back":
            self.router.go_back()
            return

        self.router.navigate_to(selected)


NavKey = Literal[
    "back",
    "new_seed_camera",
    "new_seed_dice",
    "calculate_checksum",
    "address_explorer",
    "verify_address",
]

Action = Tuple[Literal["navigate", "focus"], NavKey]

ACTION_MAP: dict[NavKey, dict[HWButtonInput, Action | None]] = {
    "back": {
        "up": None,
        "down": ("focus", "new_seed_camera"),
        "left": ("navigate", "back"),
        "right": ("focus", "new_seed_camera"),
    },
    "new_seed_camera": {
        "up": ("focus", "back"),
        "down": ("focus", "new_seed_dice"),
        "left": ("focus", "back"),
        "right": None,
    },
    "new_seed_dice": {
        "up": ("focus", "new_seed_camera"),
        "down": ("focus", "calculate_checksum"),
        "left": ("focus", "back"),
        "right": None,
    },
    "calculate_checksum": {
        "up": ("focus", "new_seed_dice"),
        "down": ("focus", "address_explorer"),
        "left": ("focus", "back"),
        "right": None,
    },
    "address_explorer": {
        "up": ("focus", "calculate_checksum"),
        "down": ("focus", "verify_address"),
        "left": ("focus", "back"),
        "right": None,
    },
    "verify_address": {
        "up": ("focus", "address_explorer"),
        "down": None,
        "left": ("focus", "back"),
        "right": None,
    },
}
