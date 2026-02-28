from dataclasses import dataclass
from typing import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from seedsigner.router import Router, Route

from seedsigner.components import Body, Header, BackButton, Button
from seedsigner.loopyUI import Component, Node

HWButtonInput = Literal["up", "down", "left", "right", "select"]
NavKey = Literal[
    "back",
    "scan_a_seedqr",
    "enter_a_12_word_seed",
    "enter_a_24_word_seed",
    "create_a_seed",
]

NAV_MAP: dict[NavKey, dict[HWButtonInput, NavKey]] = {
    "back": {
        "right": "scan_a_seedqr",
        "down": "scan_a_seedqr",
    },
    "scan_a_seedqr": {
        "up": "back",
        "left": "back",
        "down": "enter_a_12_word_seed",
    },
    "enter_a_12_word_seed": {
        "up": "scan_a_seedqr",
        "left": "back",
        "down": "enter_a_24_word_seed",
    },
    "enter_a_24_word_seed": {
        "up": "enter_a_12_word_seed",
        "left": "back",
        "down": "create_a_seed",
    },
    "create_a_seed": {
        "up": "enter_a_24_word_seed",
        "left": "back",
    },
}


@dataclass
class SeedsScreen(Component):
    router: "Router"
    selected: NavKey = "scan_a_seedqr"

    def render(self) -> Node:
        selected = self.selected

        return [
            Header(
                left=BackButton(selected=selected == "back"),
                title="Seed",
            ),
            Body(
                Button(
                    text="Scan a SeedQR", selected=selected == "scan_a_seedqr", index=0
                ),
                Button(
                    text="Enter a 12-word seed",
                    selected=selected == "enter_a_12_word_seed",
                    index=1,
                ),
                Button(
                    text="Enter a 24-word seed",
                    selected=selected == "enter_a_24_word_seed",
                    index=2,
                ),
                Button(
                    text="Create a seed", selected=selected == "create_a_seed", index=3
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
        router = self.router

        print(f"Selected {selected}")
        if selected == "back":
            router.go_back()
        else:
            router.navigate_to(selected)
