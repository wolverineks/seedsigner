from typing import Literal, Tuple

from seedsigner.components import Body, Header, BackButton, Text
from seedsigner.loopyUI import Component, Node
from seedsigner.loopyUI.events.types import HWButtonInput
from seedsigner.dimensions import Dimensions

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from seedsigner.router import Router
    from seedsigner.settings.settings import Settings
    from seedsigner.store import Store


class PowerOffScreen(Component):
    def __init__(self, store: "Store", router: "Router", settings: "Settings") -> None:
        super().__init__()
        self.store = store
        self.router = router
        self.settings = settings
        self.selected: NavKey = "back"

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
                    y=48,
                    text="It is safe to disconnect",
                ),
                Text(
                    x=int(Dimensions.width / 2) - 60,
                    y=72,
                    text="power at any time.",
                ),
            ),
        ]

    def handle_input(self, input: HWButtonInput):
        if input == "select":
            self.handle_select()
            return

        action = ACTION_MAP[self.selected].get(input)
        if action is None:
            return

        type, key = action
        if type == "navigate":
            if key == "back":
                self.router.go_back()
            else:
                self.router.navigate_to(key)
        elif type == "focus":
            self.set_selected(key)

    def handle_select(self):
        selected = self.selected
        print(f"Selected {selected}")
        if selected == "back":
            self.router.go_back()
        else:
            self.router.navigate_to(selected)

    def handle_shutdown(self):
        print("Shutting down...")


NavKey = Literal["back"]
Action = Tuple[Literal["navigate", "focus"], NavKey]

ACTION_MAP: dict[NavKey, dict[HWButtonInput, Action | None]] = {
    "back": {
        "up": None,
        "down": None,
        "left": ("navigate", "back"),
        "right": None,
    },
}
