from threading import Timer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from seedsigner.router import Router
    from seedsigner.settings.settings import Settings
    from seedsigner.store import Store


from seedsigner.components import Body, Header
from seedsigner.loopyUI import Component, Node, Text


class RestartingScreen(Component):
    def __init__(self, store: "Store", router: "Router", settings: "Settings") -> None:
        super().__init__()
        self.store = store
        self.router = router
        self.settings = settings

    def render(self) -> Node:

        return [
            Header(title="Restarting"),
            Body(
                Text(
                    x=30,
                    y=24,
                    text="Seedsigner is restarting.",
                ),
                Text(
                    x=24,
                    y=48,
                    text="All in-memory data will be",
                ),
                Text(
                    x=80,
                    y=72,
                    text="wiped.",
                ),
            ),
        ]

    def handle_on_focus(self):
        Timer(5, self.go_back).start()

    def go_back(self):
        self.router.go_back()
