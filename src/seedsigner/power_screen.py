from typing import Literal
import pygame  # type: ignore

from seedsigner.components import Body, Header, LargeButton, BackButton, Grid

HWButtonInput = Literal["up", "down", "left", "right", "select"]
ButtonId = Literal["back", "shutdown", "restart"]

nav_map: dict[ButtonId, dict[HWButtonInput, ButtonId]] = {
    "back": {"right": "shutdown", "down": "shutdown"},
    "shutdown": {"up": "back", "right": "restart"},
    "restart": {"up": "back", "left": "shutdown"},
}


class PowerScreen:
    def __init__(self, router):
        self.router = router
        self.state: dict[Literal["selected"], ButtonId] = {"selected": "shutdown"}

    def render(self):
        selected = self.state["selected"]

        return [
            Header(
                left=BackButton(selected=selected == "back"),
                title="Power",
            ),
            Body(
                ShutdownButton(selected=selected == "shutdown"),
                RestartButton(selected=selected == "restart"),
            ),
        ]

    def handle_input(self, input: Literal["up", "down", "left", "right", "select"]):
        if input == "select":
            self.handle_select()
        else:
            selected = self.state["selected"]
            if input in nav_map[selected]:
                self.state["selected"] = nav_map[selected][input]

    def handle_select(self):
        selected = self.state["selected"]
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
        text="Shutdown",
        x=Grid.left,
        y=Grid.top,
        selected=selected,
    )


def RestartButton(selected: bool):
    return LargeButton(
        text="Restart",
        x=Grid.right,
        y=Grid.top,
        selected=selected,
    )
