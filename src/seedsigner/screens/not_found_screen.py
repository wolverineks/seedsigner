from typing import Literal, TYPE_CHECKING,

from seedsigner.components.components import BackButton

if TYPE_CHECKING:
    from seedsigner.router import Router
    from seedsigner.store import Store

from seedsigner.components import Header
from seedsigner.loopyUI import Component, Node

HWButtonInput = Literal["up", "down", "left", "right", "select"]
NavKey = Literal["back"]

NAV_MAP: dict[NavKey, dict[HWButtonInput, NavKey]] = {
    "back": {},
}


class NotFoundScreen(Component):
    def __init__(self, store: "Store", router: "Router") -> None:
        super().__init__()
        self.store = store
        self.router = router
        self.selected: NavKey = "back"

    def render(self) -> Node:
        selected = self.selected

        return [
            Header(
                left=BackButton(selected=selected == "back"),
                title="Not Found",
            ),
        ]

    def handle_input(self, input: Literal["up", "down", "left", "right", "select"]):
        if input == "select":
            self.handle_select()
        elif input == "left" and self.selected == "back":
            self.handle_select()
        else:
            selected = self.selected
            if input in NAV_MAP[selected]:
                self.set_selected(NAV_MAP[selected][input])

    def handle_select(self):
        selected = self.selected
        router = self.router

        print(f"Selected {selected}")
        if selected == "back":
            router.go_back()
        else:
            router.navigate_to(selected)
