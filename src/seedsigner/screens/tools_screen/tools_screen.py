from typing import Literal

from seedsigner.components import Header, Body, BackButton, Button
from seedsigner.loopyUI import Component, Node


class ToolsScreen(Component):
    def __init__(self, router):
        self.router = router
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
                    index=0,
                ),
                Button(
                    text="New seed (dice)",
                    selected=selected == "new_seed_dice",
                    index=1,
                ),
                Button(
                    text="Calc 12th/24th word",
                    selected=selected == "calculate_checksum",
                    index=2,
                ),
                Button(
                    text="Address Explorer",
                    selected=selected == "address_explorer",
                    index=3,
                ),
                Button(
                    text="Verify Address",
                    selected=selected == "verify_address",
                    index=4,
                ),
            ),
        ]

    def handle_input(self, input: Literal["up", "down", "left", "right", "select"]):
        if input == "select":
            self.handle_select()
        elif input == "left" and self.selected == "back":
            self.handle_select()
        else:
            selected = self.selected
            if input in NAV_MAP[selected]:
                self.selected = NAV_MAP[selected][input]

    def handle_select(self):
        selected = self.selected
        print(f"Selected {selected}")
        if selected == "back":
            self.router.pop()
        else:
            self.router.navigate_to(selected)


HWButtonInput = Literal["up", "down", "left", "right", "select"]
NavKey = Literal[
    "back",
    "new_seed_camera",
    "new_seed_dice",
    "calculate_checksum",
    "address_explorer",
    "verify_address",
]

NAV_MAP: dict[NavKey, dict[HWButtonInput, NavKey]] = {
    "back": {
        "right": "new_seed_camera",
        "down": "new_seed_camera",
    },
    "new_seed_camera": {
        "up": "back",
        "down": "new_seed_dice",
        "left": "back",
    },
    "new_seed_dice": {
        "up": "new_seed_camera",
        "down": "calculate_checksum",
        "left": "back",
    },
    "calculate_checksum": {
        "up": "new_seed_dice",
        "down": "address_explorer",
        "left": "back",
    },
    "address_explorer": {
        "up": "calculate_checksum",
        "down": "verify_address",
        "left": "back",
    },
    "verify_address": {
        "up": "address_explorer",
        "left": "back",
    },
}
