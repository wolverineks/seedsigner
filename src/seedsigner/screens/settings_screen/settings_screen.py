from dataclasses import dataclass
from typing import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from seedsigner.router import Router
    from seedsigner.store import Store

from seedsigner.components import Body, Header, BackButton, Button
from seedsigner.loopyUI import Component, Node

HWButtonInput = Literal["up", "down", "right", "left", "select"]
NavKey = Literal[
    "language",
    "persistent_settings",
    "coordination_software",
    "denomination_display",
    "advanced",
    "i/o_test",
    "donate",
    "back",
    "power",
]

nav_map: dict[NavKey, dict[HWButtonInput, NavKey]] = {
    "back": {
        "right": "language",
        "down": "language",
    },
    "language": {
        "down": "persistent_settings",
        "up": "back",
        "left": "back",
    },
    "persistent_settings": {
        "up": "language",
        "down": "coordination_software",
        "left": "back",
    },
    "coordination_software": {
        "up": "persistent_settings",
        "down": "denomination_display",
        "left": "back",
    },
    "denomination_display": {
        "up": "coordination_software",
        "down": "advanced",
        "left": "back",
    },
    "advanced": {
        "up": "denomination_display",
        "down": "i/o_test",
        "left": "back",
    },
    "i/o_test": {
        "up": "advanced",
        "down": "donate",
        "left": "back",
    },
    "donate": {
        "up": "i/o_test",
        "left": "back",
    },
}


@dataclass
class SettingsScreen(Component):
    store: "Store"
    router: "Router"
    selected: NavKey = "language"

    def render(self) -> Node:
        selected = self.selected

        return [
            Header(
                left=BackButton(selected=selected == "back"),
                title="Settings",
            ),
            Body(
                [
                    Button(
                        text="Language",
                        selected=selected == "language",
                        index=0,
                    ),
                    Button(
                        text="Persistent Settings",
                        selected=selected == "persistent_settings",
                        index=1,
                    ),
                    Button(
                        text="Coordinator software",
                        selected=selected == "coordination_software",
                        index=2,
                    ),
                    Button(
                        text="Denomination display",
                        selected=selected == "denomination_display",
                        index=3,
                    ),
                    Button(
                        text="Advanced",
                        selected=selected == "advanced",
                        index=4,
                    ),
                    Button(
                        text="I/O test",
                        selected=selected == "i/o_test",
                        index=5,
                    ),
                    Button(
                        text="Donate",
                        selected=selected == "donate",
                        index=6,
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
                self.selected = nav_map[selected][input]

    def handle_select(self):
        selected = self.selected
        router = self.router

        print(f"Selected {selected}")
        if selected == "back":
            router.go_back()
        else:
            router.navigate_to(selected)
