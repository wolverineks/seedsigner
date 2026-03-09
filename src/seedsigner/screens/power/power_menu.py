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
        self.focused: ButtonId = "power-off"

    def render(self) -> Node:
        focused = self.focused

        return [
            Header(
                left=BackButton(focused=focused == "back"),
                title="Power/Restart",
            ),
            Body(
                ShutdownButton(focused=focused == "power-off"),
                RestartButton(focused=focused == "restart"),
            ),
        ]

    def handle_input(self, input: HWButtonInput):
        if input == "select":
            self.handle_select()
            return

        action = ACTION_MAP[self.focused].get(input)
        if action is None:
            return

        type, key = action
        if type == "navigate":
            if key == "back":
                self.router.go_back()
        elif type == "focus":
            self.set_focused(key)

    def handle_select(self):
        focused = self.focused
        print(f"Selected {focused}")
        if focused == "back":
            self.router.go_back()
        else:
            self.router.navigate_to(focused)


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
