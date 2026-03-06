from typing import Literal, TYPE_CHECKING, NamedTuple


if TYPE_CHECKING:
    from seedsigner.router import Router
    from seedsigner.settings.settings import Settings
    from seedsigner.store import Store

from seedsigner.components import (
    Body,
    Header,
    BackButton,
    Button,
    ScrollList,
    ScrollListWindow,
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


class MenuItem(NamedTuple):
    key: MenuKey
    label: str


MENU_ITEMS: list[MenuItem] = [
    MenuItem("language", "Language"),
    MenuItem("persistent_settings", "Persistent Settings"),
    MenuItem("coordination_software", "Coordinator software"),
    MenuItem("denomination_display", "Denomination display"),
    MenuItem("advanced", "Advanced"),
    MenuItem("i/o_test", "I/O test"),
    MenuItem("donate", "Donate"),
]

MENU_KEYS: list[MenuKey] = [item.key for item in MENU_ITEMS]


class SettingsMenuScreen(Component):
    def __init__(self, store: "Store", router: "Router", settings: "Settings") -> None:
        super().__init__()
        self.store = store
        self.router = router
        self.settings = settings
        self.selected = MENU_ITEMS[0].key
        self.window = ScrollListWindow(
            on_blur=lambda: self.set_selected("back"),
            visible_count=5,
        )

    def render(self) -> Node:
        selected = self.selected

        return [
            Header(
                left=BackButton(selected=selected == "back"),
                title="Settings",
            ),
            Body(
                *ScrollList(
                    window=self.window,
                    render_item=self.render_item,
                    items=MENU_ITEMS,
                )
            ),
        ]

    def render_item(self, item: MenuItem, index: int):
        selected = self.selected

        return Button(
            text=item.label,
            selected=selected == item.key,
            index=index,
        )

    def handle_input(self, input: HWButtonInput):
        #### BACK BUTTON ####
        if self.selected == "back":
            if input in ["select", "left"]:
                self.router.go_back()

            elif NAV_MAP["back"].get(input):
                self.set_selected(NAV_MAP["back"][input])
                self.window.focus()

        #### MENU KEYS ####
        elif self.selected in MENU_KEYS:
            if input in ["select", "right"]:
                self.router.navigate_to(self.selected)

            elif input == "left":
                self.set_selected("back")

            else:
                if NAV_MAP[self.selected].get(input):
                    self.set_selected(NAV_MAP[self.selected][input])
                    self.window.handle_input(
                        selected_index=(
                            MENU_KEYS.index(self.selected)
                            if self.selected in MENU_KEYS
                            else -1
                        ),
                    )


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
