from typing import Any, Literal, TYPE_CHECKING

from seedsigner.components import CheckmarkButton


if TYPE_CHECKING:
    from seedsigner.router import Router
    from seedsigner.store import Store
    from seedsigner.settings import Settings

from seedsigner.components import Body, Header, BackButton
from seedsigner.loopyUI import Component, Node
from seedsigner.loopyUI.events.types import HWButtonInput


class PersistentSettingsScreen(Component):
    def __init__(self, store: "Store", router: "Router", settings: "Settings") -> None:
        super().__init__()
        self.store = store
        self.router = router
        self.settings = settings
        self.focused: NavKey = "enabled" if settings.persistent_settings else "disabled"

    def render(self) -> Node:
        focused = self.focused

        return [
            Header(
                left=BackButton(focused=focused == "back"),
                title="Persistent Settings",
            ),
            Body(
                CheckmarkButton(
                    text="Enabled",
                    focused=focused == "enabled",
                    checked=self.settings.persistent_settings,
                    slot=2,
                ),
                CheckmarkButton(
                    text="Disabled",
                    focused=focused == "disabled",
                    checked=not self.settings.persistent_settings,
                    slot=1,
                ),
            ),
        ]

    def handle_on_focus(self) -> Any:
        self.set_focused("enabled" if self.settings.persistent_settings else "disabled")

    def handle_input(self, input: HWButtonInput):
        action = ACTION_MAP[self.focused].get(input)
        if action is None:
            return

        type, key = action
        if type == "navigate":
            if key == "back":
                self.router.go_back()
        elif type == "focus":
            self.set_focused(key)
        elif type == "select":
            self.settings.persistent_settings = key == "enabled"


NavKey = Literal[
    "enabled",
    "disabled",
    "back",
]

Action = tuple[Literal["navigate", "focus", "select"], NavKey]

ACTION_MAP: dict[NavKey, dict[HWButtonInput, Action | None]] = {
    "back": {
        "up": None,
        "down": ("focus", "enabled"),
        "left": ("navigate", "back"),
        "right": ("focus", "enabled"),
        "select": ("navigate", "back"),
    },
    "enabled": {
        "up": ("focus", "back"),
        "down": ("focus", "disabled"),
        "left": ("focus", "back"),
        "right": ("select", "enabled"),
        "select": ("select", "enabled"),
    },
    "disabled": {
        "up": ("focus", "enabled"),
        "down": None,
        "left": ("focus", "back"),
        "right": ("select", "disabled"),
        "select": ("select", "disabled"),
    },
}
