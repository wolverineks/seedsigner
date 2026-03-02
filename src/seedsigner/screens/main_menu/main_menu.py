from typing import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from seedsigner.router import Router
    from seedsigner.store import Store

from seedsigner.components import Body, Header, PowerButton
from seedsigner.loopyUI import Component, Node
from .components import ScanButton, SeedsButton, SettingsButton, ToolsButton

HWButtonInput = Literal["up", "down", "left", "right", "select"]
NavKey = Literal["scan", "tools", "settings", "seeds", "back", "power"]


NAV_MAP: dict[NavKey, dict[HWButtonInput, NavKey]] = {
    "scan": {"right": "seeds", "down": "tools"},
    "seeds": {"left": "scan", "down": "settings", "up": "power"},
    "tools": {"right": "settings", "up": "scan"},
    "settings": {"left": "tools", "up": "seeds"},
    "back": {"right": "power", "down": "scan"},
    "power": {"down": "seeds"},
}


class MainScreen(Component):
    def __init__(self, store: "Store", router: "Router") -> None:
        super().__init__()
        self.store = store
        self.router = router
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
        else:
            selected = self.selected
            if input in NAV_MAP[selected]:
                self.set_selected(NAV_MAP[selected][input])

    def handle_select(self):
        selected = self.selected
        router = self.router

        if selected == "back":
            router.go_back()
        else:
            router.navigate_to(selected)
