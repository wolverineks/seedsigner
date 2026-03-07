from typing import Literal, TYPE_CHECKING, NamedTuple, Tuple


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
KEY_TO_INDEX: dict[MenuKey, int] = {
    item.key: index for index, item in enumerate(MENU_ITEMS)
}


class SettingsMenuScreen(Component):
    def __init__(self, store: "Store", router: "Router", settings: "Settings") -> None:
        super().__init__()
        self.store = store
        self.router = router
        self.settings = settings
        self.selected: MenuKey | Literal["back"] = MENU_ITEMS[0].key
        self.window = ScrollListWindow(visible_count=5)

    def render(self) -> Node:
        selected = self.selected

        return [
            Header(
                left=BackButton(selected=selected == "back"),
                title="Settings",
            ),
            Body(
                ScrollList(
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
        if input == "select":
            self.handle_select()
            return

        action = NAV_MAP[self.selected].get(input)
        if action is None:
            return

        type, key = action
        if type == "navigate":
            if key == "back":
                self.router.go_back()
            else:
                self.router.navigate_to(key)
        elif type == "focus":
            self.set_selected(key)  # set_focus
            if key != "back":
                self.window.update(selected_index=KEY_TO_INDEX[key])

    def handle_select(self):
        selected = self.selected
        router = self.router

        print(f"Selected {selected}")
        if selected == "back":
            router.go_back()
        else:
            router.navigate_to(selected)


Action = Tuple[Literal["navigate", "focus"], NavKey]
NAV_MAP: dict[NavKey, dict[HWButtonInput, Action | None]] = {
    "back": {
        "up": None,
        "down": ("focus", "language"),
        "right": ("focus", "language"),
        "left": ("navigate", "back"),
    },
    "language": {
        "up": ("focus", "back"),
        "down": ("focus", "persistent_settings"),
        "left": ("focus", "back"),
        "right": ("navigate", "language"),
    },
    "persistent_settings": {
        "up": ("focus", "language"),
        "down": ("focus", "coordination_software"),
        "left": ("focus", "back"),
        "right": ("navigate", "persistent_settings"),
    },
    "coordination_software": {
        "up": ("focus", "persistent_settings"),
        "down": ("focus", "denomination_display"),
        "left": ("focus", "back"),
        "right": ("navigate", "coordination_software"),
    },
    "denomination_display": {
        "up": ("focus", "coordination_software"),
        "down": ("focus", "advanced"),
        "left": ("focus", "back"),
        "right": ("navigate", "denomination_display"),
    },
    "advanced": {
        "up": ("focus", "denomination_display"),
        "down": ("focus", "i/o_test"),
        "left": ("focus", "back"),
        "right": ("navigate", "advanced"),
    },
    "i/o_test": {
        "up": ("focus", "advanced"),
        "down": ("focus", "donate"),
        "left": ("focus", "back"),
        "right": ("navigate", "i/o_test"),
    },
    "donate": {
        "up": ("focus", "i/o_test"),
        "down": None,
        "left": ("focus", "back"),
        "right": ("navigate", "donate"),
    },
}
