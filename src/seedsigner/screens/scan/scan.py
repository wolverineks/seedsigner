from typing import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from seedsigner.router import Router
    from seedsigner.settings.settings import Settings
    from seedsigner.store import Store

from seedsigner.components import Body, Header, BackButton
from seedsigner.loopyUI import Component, Node, HWButtonInput


class ScanScreen(Component):
    def __init__(self, store: "Store", router: "Router", settings: "Settings") -> None:
        super().__init__()
        self.store = store
        self.router = router
        self.settings = settings
        self.focused: Literal["back"] = "back"

    def render(self) -> Node:
        focused = self.focused

        return [
            Header(
                left=BackButton(focused=focused == "back"),
                title="Scan",
            ),
            Body(),
        ]

    def handle_input(self, input: HWButtonInput):
        if input == "select":
            self.handle_select()
        elif input == "left" and self.focused == "back":
            self.handle_select()

    def handle_select(self):
        focused = self.focused
        print(f"Selected {focused}")
        if focused == "back":
            self.router.go_back()
