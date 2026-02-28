from dataclasses import dataclass
from typing import Literal, TYPE_CHECKING, Any

if TYPE_CHECKING:
    from seedsigner.router import Router

from seedsigner.components import Header, Body, BackButton
from seedsigner.loopyUI import Component, Node

HWButtonInput = Literal["up", "down", "left", "right", "select"]
NavKey = Literal["back"]

nav_map: dict[NavKey, dict[HWButtonInput, NavKey]] = {
    "back": {},
}


@dataclass
class NotFoundScreen(Component):
    store: Any
    router: "Router"
    selected: NavKey = "back"

    def render(self) -> Node:
        selected = self.selected

        return [
            Header(
                left=BackButton(selected=selected == "back"),
                title="Not Found",
            ),
            Body(),
        ]

    def handle_input(self, input: Literal["up", "down", "left", "right", "select"]):
        if input == "select":
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
