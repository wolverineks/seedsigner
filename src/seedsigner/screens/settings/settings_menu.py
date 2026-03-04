from typing import Any, Literal, TYPE_CHECKING, cast

from seedsigner.router import Route

if TYPE_CHECKING:
    from seedsigner.router import Router
    from seedsigner.settings.settings import Settings
    from seedsigner.store import Store

from seedsigner.components import (
    Body,
    Header,
    BackButton,
    Button,
    ScrollableList,
    ScrollableListWindow,
)
from seedsigner.loopyUI import Component, Node

HWButtonInput = Literal["up", "down", "right", "left", "select"]
MenuKey = Literal[
    "language",
    "persistent_settings",
    "coordination_software",
    "denomination_display",
    "advanced",
    "i/o_test",
    "donate",
]
NavKey = Literal["back"] | MenuKey

MENU_ITEMS: list[tuple[MenuKey, str]] = [
    ("language", "Language"),
    ("persistent_settings", "Persistent Settings"),
    ("coordination_software", "Coordinator software"),
    ("denomination_display", "Denomination display"),
    ("advanced", "Advanced"),
    ("i/o_test", "I/O test"),
    ("donate", "Donate"),
]

MENU_KEYS: list[MenuKey] = [key for key, _ in MENU_ITEMS]


class SettingsMenuScreen(Component):
    def __init__(self, store: "Store", router: "Router", settings: "Settings") -> None:
        super().__init__()
        self.store = store
        self.router = router
        self.settings = settings
        self.selected = MENU_KEYS[0]
        self.scrollable_list_window = ScrollableListWindow(
            visible_count=5,
            item_count=7,
            on_blur=lambda: self.set_selected("back"),
        )

    def render(self) -> Node:
        selected = self.selected

        return [
            Header(
                left=BackButton(selected=selected == "back"),
                title="Settings",
            ),
            Body(
                *ScrollableList(
                    window=self.scrollable_list_window,
                    items=[
                        Button(
                            text="Language",
                            selected=selected == "language",
                            index=0,
                        ),
                        Button(
                            text="Persistent Settings",
                            selected=selected == "persistent_settings",
                            index=1,
                        ),
                        Button(
                            text="Coordinator software",
                            selected=selected == "coordination_software",
                            index=2,
                        ),
                        Button(
                            text="Denomination display",
                            selected=selected == "denomination_display",
                            index=3,
                        ),
                        Button(
                            text="Advanced",
                            selected=selected == "advanced",
                            index=4,
                        ),
                        Button(
                            text="I/O test",
                            selected=selected == "i/o_test",
                            index=5,
                        ),
                        Button(
                            text="Donate",
                            selected=selected == "donate",
                            index=6,
                        ),
                    ],
                )
            ),
        ]

    def handle_input(self, input: HWButtonInput):
        print(f"Input: {input}, Selected: {self.selected}")
        if input == "select":
            self.handle_select()

        elif self.selected == "back":
            if input == "left":
                self.handle_select()
            elif input == "down" or input == "right":
                self.set_selected(NAV_MAP["back"]["down"])
                self.scrollable_list_window.reset()

        elif self.selected in MENU_KEYS:
            if input == "right":
                self.handle_select()
            else:
                if NAV_MAP[self.selected].get(input):
                    self.set_selected(NAV_MAP[self.selected][input])
                    self.scrollable_list_window.handle_input(input)

    def handle_select(self):
        selected = self.selected
        router = self.router

        print(f"Selected {selected}")
        if selected == "back":
            router.go_back()
        else:
            router.navigate_to(selected)


NAV_MAP: dict[NavKey, dict[HWButtonInput, NavKey]] = {
    "back": {
        "right": "language",
        "down": "language",
    },
    "language": {
        "up": "back",
        "down": "persistent_settings",
        "left": "back",
    },
    "persistent_settings": {
        "up": "language",
        "down": "coordination_software",
        "left": "back",
    },
    "coordination_software": {
        "up": "persistent_settings",
        "down": "denomination_display",
        "left": "back",
    },
    "denomination_display": {
        "up": "coordination_software",
        "down": "advanced",
        "left": "back",
    },
    "advanced": {
        "up": "denomination_display",
        "down": "i/o_test",
        "left": "back",
    },
    "i/o_test": {
        "up": "advanced",
        "down": "donate",
        "left": "back",
    },
    "donate": {
        "up": "i/o_test",
        "left": "back",
    },
}
