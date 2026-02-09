from dataclasses import dataclass
from typing import Literal
import pygame  # type: ignore

from seedsigner.components import Body, Header, LargeButton, BackButton, Dimensions
from seedsigner.loopyUI import Component, Node

HWButtonInput = Literal["up", "down", "left", "right", "select"]
ButtonId = Literal["back", "shutdown", "restart"]

nav_map: dict[ButtonId, dict[HWButtonInput, ButtonId]] = {
    "back": {
        "right": "shutdown",
        "down": "shutdown",
    },
    "shutdown": {
        "up": "back",
        "right": "restart",
        "left": "back",
    },
    "restart": {
        "up": "back",
        "left": "shutdown",
    },
}


class PowerScreen(Component):
    def __init__(self, router):
        self.router = router
        self.selected: ButtonId = "shutdown"

    def render(self) -> Node:
        selected = self.selected

        return [
            Header(
                left=BackButton(selected=selected == "back"),
                title="Power/Restart",
            ),
            Body(
                ShutdownButton(selected=selected == "shutdown"),
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
        elif selected == "shutdown":
            self.handle_shutdown()
        else:
            self.router.navigate_to(selected)

    def handle_shutdown(self):
        print("Shutting down...")
        custom_quit_event = pygame.event.Event(pygame.QUIT)
        pygame.event.post(custom_quit_event)


def ShutdownButton(selected: bool):
    return LargeButton(
        label="Shutdown",
        icon="power",
        x=Grid.left,
        y=Body.y + int((Body.height - LargeButton.height) / 2),
        selected=selected,
    )


def RestartButton(selected: bool):
    return LargeButton(
        label="Restart",
        icon="restart",
        x=Grid.right,
        y=Body.y + int((Body.height - LargeButton.height) / 2),
        selected=selected,
    )


@dataclass
class Grid:
    columns = 2
    width = int(
        (Dimensions.width - Body.padding - Body.padding - Body.padding) / columns
    )
    left = Body.padding
    right = Body.padding + width + Body.padding
