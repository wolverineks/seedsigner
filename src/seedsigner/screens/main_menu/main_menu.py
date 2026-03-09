from typing import Literal, TYPE_CHECKING, Tuple

if TYPE_CHECKING:
    from seedsigner.router import Router
    from seedsigner.settings import Settings
    from seedsigner.store import Store

from seedsigner.components import Body, Header, PowerButton
from seedsigner.loopyUI import Component, Node
from seedsigner.loopyUI.events.types import HWButtonInput
from .components import ScanButton, SeedsButton, SettingsButton, ToolsButton


class MainMenuScreen(Component):
    def __init__(self, store: "Store", router: "Router", settings: "Settings") -> None:
        super().__init__()
        self.store = store
        self.router = router
        self.settings = settings
        self.focused: NavKey = "scan"

    def render(self) -> Node:
        focused = self.focused

        return [
            Header(
                title="Home",
                right=PowerButton(focused=focused == "power"),
            ),
            Body(
                ScanButton(focused=focused == "scan"),
                SeedsButton(focused=focused == "seeds"),
                ToolsButton(focused=focused == "tools"),
                SettingsButton(focused=focused == "settings"),
            ),
        ]

    def handle_input(self, input: HWButtonInput):
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


NavKey = Literal["scan", "tools", "settings", "seeds", "back", "power"]

Action = Tuple[Literal["navigate", "focus", "select"], NavKey]

ACTION_MAP: dict[NavKey, dict[HWButtonInput, Action | None]] = {
    "scan": {
        "up": None,
        "down": ("focus", "tools"),
        "left": None,
        "right": ("focus", "seeds"),
        "select": ("navigate", "scan"),
    },
    "seeds": {
        "up": ("focus", "power"),
        "down": ("focus", "settings"),
        "left": ("focus", "scan"),
        "right": None,
        "select": ("navigate", "seeds"),
    },
    "tools": {
        "up": ("focus", "scan"),
        "down": None,
        "left": None,
        "right": ("focus", "settings"),
        "select": ("navigate", "tools"),
    },
    "settings": {
        "up": ("focus", "seeds"),
        "down": None,
        "left": ("focus", "tools"),
        "right": None,
        "select": ("navigate", "settings"),
    },
    "power": {
        "up": None,
        "down": ("focus", "seeds"),
        "left": None,
        "right": None,
        "select": ("navigate", "power"),
    },
}
