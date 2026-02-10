from dataclasses import dataclass
from typing import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from seedsigner.router import Router


from seedsigner.components import Body, Header, BackButton
from seedsigner.loopyUI import Component, Node
from .components import ShutdownButton, RestartButton

HWButtonInput = Literal["up", "down", "left", "right", "select"]
ButtonId = Literal["back", "power-off", "restart"]

nav_map: dict[ButtonId, dict[HWButtonInput, ButtonId]] = {
    "back": {
        "right": "power-off",
        "down": "power-off",
    },
    "power-off": {
        "up": "back",
        "right": "restart",
        "left": "back",
    },
    "restart": {
        "up": "back",
        "left": "power-off",
    },
}


@dataclass
class PowerScreen(Component):
    router: "Router"
    selected: ButtonId = "power-off"

    def render(self) -> Node:
        selected = self.selected

        return [
            Header(
                left=BackButton(selected=selected == "back"),
                title="Power/Restart",
            ),
            Body(
                ShutdownButton(selected=selected == "power-off"),
                RestartButton(selected=selected == "restart"),
            ),
        ]

    def handle_input(self, input: Literal["up", "down", "left", "right", "select"]):
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
        print(f"Selected {selected}")
        if selected == "back":
            self.router.pop()
        else:
            self.router.navigate_to(selected)
