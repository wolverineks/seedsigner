from typing import Any, Literal, TYPE_CHECKING

from seedsigner.components.components import CheckmarkButton


if TYPE_CHECKING:
    from seedsigner.router import Router
    from seedsigner.store import Store
    from seedsigner.settings import Settings

from seedsigner.components import Body, Header, BackButton
from seedsigner.loopyUI import Component, Node

HWButtonInput = Literal["up", "down", "right", "left", "select"]
NavKey = Literal[
    "enabled",
    "disabled",
    "back",
]

nav_map: dict[NavKey, dict[HWButtonInput, NavKey]] = {
    "back": {
        "right": "enabled",
        "down": "enabled",
    },
    "enabled": {
        "down": "disabled",
        "up": "back",
        "left": "back",
    },
    "disabled": {
        "up": "enabled",
        "left": "back",
    },
}


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
        elif input == "left" and self.selected == "back":
            self.handle_select()
        else:
            selected = self.selected
            if input in nav_map[selected]:
                self.set_selected(nav_map[selected][input])

    def handle_select(self):
        selected = self.selected
        router = self.router

        print(f"Selected {selected}")
        if selected == "back":
            router.go_back()
        else:
            self.settings.persistent_settings = selected == "enabled"
