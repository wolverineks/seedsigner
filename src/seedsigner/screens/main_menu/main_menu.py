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
        self.selected: NavKey = "scan"

    def render(self) -> Node:
        selected = self.selected

        return [
            Header(
                title="Home",
                right=PowerButton(selected=selected == "power"),
            ),
            Body(
                ScanButton(selected=selected == "scan"),
                SeedsButton(selected=selected == "seeds"),
                ToolsButton(selected=selected == "tools"),
                SettingsButton(selected=selected == "settings"),
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
        router = self.router

        if selected == "back":
            router.go_back()
        else:
            router.navigate_to(selected)


NavKey = Literal["scan", "tools", "settings", "seeds", "back", "power"]

Action = Tuple[Literal["navigate", "focus"], NavKey]

ACTION_MAP: dict[NavKey, dict[HWButtonInput, Action | None]] = {
    "scan": {
        "up": None,
        "down": ("focus", "tools"),
        "left": None,
        "right": ("focus", "seeds"),
    },
    "seeds": {
        "up": ("focus", "power"),
        "down": ("focus", "settings"),
        "left": ("focus", "scan"),
        "right": None,
    },
    "tools": {
        "up": ("focus", "scan"),
        "down": None,
        "left": None,
        "right": ("focus", "settings"),
    },
    "settings": {
        "up": ("focus", "seeds"),
        "down": None,
        "left": ("focus", "tools"),
        "right": None,
    },
    "back": {
        "up": None,
        "down": ("focus", "scan"),
        "left": ("navigate", "back"),
        "right": ("focus", "power"),
    },
    "power": {
        "up": None,
        "down": ("focus", "seeds"),
        "left": None,
        "right": None,
    },
}
