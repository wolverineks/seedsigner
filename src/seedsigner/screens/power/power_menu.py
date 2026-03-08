from typing import Literal, TYPE_CHECKING


if TYPE_CHECKING:
    from seedsigner.router import Router
    from seedsigner.settings.settings import Settings
    from seedsigner.store import Store

from seedsigner.components import Body, Header, BackButton
from seedsigner.loopyUI import Component, Node, HWButtonInput

from .components import ShutdownButton, RestartButton


class PowerScreen(Component):
    def __init__(self, store: "Store", router: "Router", settings: "Settings") -> None:
        super().__init__()
        self.store = store
        self.router = router
        self.settings = settings
        self.selected: ButtonId = "power-off"

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

    def handle_input(self, input: HWButtonInput):
        if input == "select":
            self.handle_select()
        elif input == "left" and self.selected == "back":
            self.handle_select()
        else:
            selected = self.selected
            if input in nav_map[selected]:
                self.set_selected(nav_map[selected][input])

    def handle_select(self):
        selected = self.selected
        print(f"Selected {selected}")
        if selected == "back":
            self.router.go_back()
        else:
            self.router.navigate_to(selected)


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
