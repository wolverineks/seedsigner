from dataclasses import dataclass
from threading import Timer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from seedsigner.router import Router


from seedsigner.components import Body, Header
from seedsigner.loopyUI import Component, Node


@dataclass
class RestartingScreen(Component):
    router: "Router"

    def render(self) -> Node:

        return [
            Header(
                title="Restarting",
            ),
            Body(),
        ]

    def handle_on_focus(self):
        Timer(5, self.go_back).start()

    def go_back(self):
        self.router.pop()
