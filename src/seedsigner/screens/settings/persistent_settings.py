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
        self.selected: NavKey = (
            "enabled" if settings.persistent_settings else "disabled"
        )

    def render(self) -> Node:
        selected = self.selected

        return [
            Header(
                left=BackButton(selected=selected == "back"),
                title="Persistent Settings",
            ),
            Body(
                [
                    CheckmarkButton(
                        text="Enabled",
                        selected=selected == "enabled",
                        checked=self.settings.persistent_settings,
                        index=0,
                    ),
                    CheckmarkButton(
                        text="Disabled",
                        selected=selected == "disabled",
                        checked=not self.settings.persistent_settings,
                        index=1,
                    ),
                ]
            ),
        ]

    def handle_on_focus(self) -> Any:
        self.set_selected(
            "enabled" if self.settings.persistent_settings else "disabled"
        )

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
        router = self.router

        print(f"Selected {selected}")
        if selected == "back":
            router.go_back()
        else:
            self.settings.persistent_settings = selected == "enabled"


NavKey = Literal[
    "enabled",
    "disabled",
    "back",
]

Action = tuple[Literal["navigate", "focus"], NavKey]

ACTION_MAP: dict[NavKey, dict[HWButtonInput, Action | None]] = {
    "back": {
        "right": ("focus", "enabled"),
        "down": ("focus", "enabled"),
        "left": ("navigate", "back"),
    },
    "enabled": {
        "down": ("focus", "disabled"),
        "up": ("focus", "back"),
        "left": ("focus", "back"),
    },
    "disabled": {
        "up": ("focus", "enabled"),
        "left": ("focus", "back"),
    },
}
