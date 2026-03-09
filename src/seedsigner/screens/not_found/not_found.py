from typing import Literal, TYPE_CHECKING, Tuple


if TYPE_CHECKING:
    from seedsigner.router import Router
    from seedsigner.store import Store
    from seedsigner.settings.settings import Settings

from seedsigner.components import Header, Body, BackButton
from seedsigner.loopyUI import Component, Node, HWButtonInput


class NotFoundScreen(Component):
    def __init__(self, store: "Store", router: "Router", settings: "Settings") -> None:
        super().__init__()
        self.store = store
        self.router = router
        self.settings = settings
        self.focused: NavKey = "back"

    def render(self) -> Node:
        focused = self.focused

        return [
            Header(
                left=BackButton(focused=focused == "back"),
                title="Not Found",
            ),
            Body(),
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
            else:
                self.router.navigate_to(key)
        elif type == "focus":
            self.set_focused(key)

    def handle_select(self):
        focused = self.focused
        router = self.router

        print(f"Selected {focused}")
        if focused == "back":
            router.go_back()
        else:
            router.navigate_to(focused)


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
