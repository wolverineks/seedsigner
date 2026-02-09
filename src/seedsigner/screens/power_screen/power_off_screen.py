from dataclasses import dataclass
from typing import Literal
import pygame  # type: ignore

from seedsigner.components import Body, Header, BackButton
from seedsigner.loopyUI import Component, Node

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from router import Router

HWButtonInput = Literal["up", "down", "left", "right", "select"]
ButtonId = Literal["back", "power-off", "restart"]

nav_map: dict[ButtonId, dict[HWButtonInput, ButtonId]] = {
    "back": {},
}


@dataclass
class PowerOffScreen(Component):
    router: "Router"
    selected: ButtonId = "back"

    def render(self) -> Node:
        selected = self.selected

        return [
            Header(
                left=BackButton(selected=selected == "back"),
                title="Just Unplug It",
            ),
            Body(),
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

    def handle_shutdown(self):
        print("Shutting down...")
        custom_quit_event = pygame.event.Event(pygame.QUIT)
        pygame.event.post(custom_quit_event)
