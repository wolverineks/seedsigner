from threading import Timer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from seedsigner.router import Router
    from seedsigner.settings.settings import Settings
    from seedsigner.store import Store


from seedsigner.components import Body, Header
from seedsigner.loopyUI import Component, Node


class RestartingScreen(Component):
    def __init__(self, store: "Store", router: "Router", settings: "Settings") -> None:
        super().__init__()
        self.store = store
        self.router = router
        self.settings = settings

    def render(self) -> Node:

        return [
            Header(title="Restarting"),
            Body(),
        ]

    def handle_on_focus(self):
        Timer(5, self.go_back).start()

    def go_back(self):
        self.router.go_back()
