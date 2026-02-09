from dataclasses import dataclass
from typing import Literal, Any

from seedsigner.components import Body, Header, BackButton
from seedsigner.loopyUI import Component, Node

HWButtonInput = Literal["up", "down", "left", "right", "select"]


@dataclass
class ScanScreen(Component):
    router: Any
    selected: Literal["back"] = "back"

    def render(self) -> Node:
        selected = self.selected

        return [
            Header(
                left=BackButton(selected=selected == "back"),
                title="Scan",
            ),
            Body(),
        ]

    def handle_input(self, input: Literal["select"]):
        if input == "select":
            self.handle_select()
        elif input == "left" and self.selected == "back":
            self.handle_select()

    def handle_select(self):
        selected = self.selected
        print(f"Selected {selected}")
        if selected == "back":
            self.router.pop()
