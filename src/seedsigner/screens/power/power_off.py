from typing import Literal

from seedsigner.components import Body, Header, BackButton, Text
from seedsigner.loopyUI import Component, Node
from seedsigner.dimensions import Dimensions

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from seedsigner.router import Router
    from seedsigner.settings.settings import Settings
    from seedsigner.store import Store

HWButtonInput = Literal["up", "down", "left", "right", "select"]
ButtonId = Literal["back", "power-off", "restart"]

nav_map: dict[ButtonId, dict[HWButtonInput, ButtonId]] = {
    "back": {},
}


class PowerOffScreen(Component):
    def __init__(self, store: "Store", router: "Router", settings: "Settings") -> None:
        super().__init__()
        self.store = store
        self.router = router
        self.settings = settings
        self.selected: ButtonId = "back"

    def render(self) -> Node:
        selected = self.selected

        return [
            Header(
                left=BackButton(selected=selected == "back"),
                title="Just Unplug It",
            ),
            Body(
                Text(
                    x=int(Dimensions.width / 2) - 80,
                    y=int(Dimensions.height / 2) - 24,
                    text="It is safe to disconnect",
                ),
                Text(
                    x=int(Dimensions.width / 2) - 60,
                    y=int(Dimensions.height / 2),
                    text="power at any time.",
                ),
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
                self.set_selected(nav_map[selected][input])

    def handle_select(self):
        selected = self.selected
        print(f"Selected {selected}")
        if selected == "back":
            self.router.go_back()
        else:
            self.router.navigate_to(selected)

    def handle_shutdown(self):
        print("Shutting down...")
