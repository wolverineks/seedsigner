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
        self.focused: NavKey = "new_seed_camera"

    def render(self) -> Node:
        focused = self.focused

        return [
            Header(
                left=BackButton(focused=focused == "back"),
                title="Tools",
            ),
            Body(
                Button(
                    text="New seed (camera)",
                    focused=focused == "new_seed_camera",
                    slot=5,
                ),
                Button(
                    text="New seed (dice)",
                    focused=focused == "new_seed_dice",
                    slot=4,
                ),
                Button(
                    text="Calc 12th/24th word",
                    focused=focused == "calculate_checksum",
                    slot=3,
                ),
                Button(
                    text="Address Explorer",
                    focused=focused == "address_explorer",
                    slot=2,
                ),
                Button(
                    text="Verify Address",
                    focused=focused == "verify_address",
                    slot=1,
                ),
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
            else:
                self.router.navigate_to(key)
        elif type == "focus":
            self.set_focused(key)


NavKey = Literal[
    "back",
    "new_seed_camera",
    "new_seed_dice",
    "calculate_checksum",
    "address_explorer",
    "verify_address",
]

Action = Tuple[Literal["navigate", "focus", "select"], NavKey]

ACTION_MAP: dict[NavKey, dict[HWButtonInput, Action | None]] = {
    "back": {
        "up": None,
        "down": ("focus", "new_seed_camera"),
        "left": ("navigate", "back"),
        "right": ("focus", "new_seed_camera"),
        "select": ("navigate", "back"),
    },
    "new_seed_camera": {
        "up": ("focus", "back"),
        "down": ("focus", "new_seed_dice"),
        "left": ("focus", "back"),
        "right": ("navigate", "new_seed_camera"),
        "select": ("navigate", "new_seed_camera"),
    },
    "new_seed_dice": {
        "up": ("focus", "new_seed_camera"),
        "down": ("focus", "calculate_checksum"),
        "left": ("focus", "back"),
        "right": ("navigate", "new_seed_dice"),
        "select": ("navigate", "new_seed_dice"),
    },
    "calculate_checksum": {
        "up": ("focus", "new_seed_dice"),
        "down": ("focus", "address_explorer"),
        "left": ("focus", "back"),
        "right": ("navigate", "calculate_checksum"),
        "select": ("navigate", "calculate_checksum"),
    },
    "address_explorer": {
        "up": ("focus", "calculate_checksum"),
        "down": ("focus", "verify_address"),
        "left": ("focus", "back"),
        "right": ("navigate", "address_explorer"),
        "select": ("navigate", "address_explorer"),
    },
    "verify_address": {
        "up": ("focus", "address_explorer"),
        "down": None,
        "left": ("focus", "back"),
        "right": ("navigate", "verify_address"),
        "select": ("navigate", "verify_address"),
    },
}
