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
            return

        action = ACTION_MAP[self.selected].get(input)
        if action is None:
            return

        type, key = action
        if type == "navigate":
            if key == "back":
                self.router.go_back()
        elif type == "focus":
            self.set_selected(key)

    def handle_select(self):
        selected = self.selected
        print(f"Selected {selected}")
        if selected == "back":
            self.router.go_back()
        else:
            self.router.navigate_to(selected)


ButtonId = Literal["back", "power-off", "restart"]

Action = tuple[Literal["navigate", "focus"], ButtonId]

ACTION_MAP: dict[ButtonId, dict[HWButtonInput, Action | None]] = {
    "back": {
        "right": ("focus", "power-off"),
        "down": ("focus", "power-off"),
        "left": ("navigate", "back"),
    },
    "power-off": {
        "up": ("focus", "back"),
        "right": ("focus", "restart"),
        "left": ("focus", "back"),
    },
    "restart": {
        "up": ("focus", "back"),
        "left": ("focus", "power-off"),
    },
}
