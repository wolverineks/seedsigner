from typing import Literal, TYPE_CHECKING, NamedTuple

from seedsigner.components import CheckmarkButton, ScrollList, ScrollListWindow
from seedsigner.settings.language import LANGUAGE_OPTIONS


if TYPE_CHECKING:
    from seedsigner.router import Router
    from seedsigner.store import Store
    from seedsigner.settings import Settings

from seedsigner.components import Body, Header, BackButton
from seedsigner.loopyUI import Component, Node
from seedsigner.loopyUI.events.types import HWButtonInput


class MenuItem(NamedTuple):
    key: str
    label: str


class LanguageScreen(Component):
    def __init__(self, store: "Store", router: "Router", settings: "Settings") -> None:
        super().__init__()
        self.store = store
        self.router = router
        self.settings = settings
        self.focused: NavKey = "english"
        self.window = ScrollListWindow(visible_count=5)

    def render(self) -> Node:
        focused = self.focused

        return [
            Header(
                left=BackButton(focused=focused == "back"),
                title="Language",
            ),
            Body(
                ScrollList(
                    window=self.window,
                    render_item=self.render_item,
                    items=LANGUAGE_ITEMS,
                )
            ),
        ]

    def render_item(self, item: MenuItem, index: int):
        focused = self.focused

        return CheckmarkButton(
            text=item.label,
            focused=focused == item.key,
            checked=self.settings.language == item.key,
            y=index * (CheckmarkButton.height + Body.padding),
        )

    def handle_on_focus(self) -> None:
        language = self.settings.language
        if language in LANGUAGE_OPTIONS:
            self.set_focused(language)
            self.window.update(focused_index=KEY_TO_INDEX[language])

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
            if key != "back":
                self.window.update(focused_index=KEY_TO_INDEX[key])
        elif type == "select":
            if key != "back":
                self.settings.language = key


LANGUAGE_ITEMS = [
    MenuItem("english", "English"),
    MenuItem("spanish", "Español"),
    MenuItem("japanese", "日本語"),
    MenuItem("italian", "Italiano"),
    MenuItem("french", "Français"),
    MenuItem("korean", "한국어"),
    MenuItem("russian", "Русский"),
]

KEY_TO_INDEX = {item.key: i for i, item in enumerate(LANGUAGE_ITEMS)}

NavKey = Literal[
    "english",
    "spanish",
    "japanese",
    "italian",
    "french",
    "korean",
    "russian",
    "back",
]

Action = tuple[Literal["navigate", "focus", "select"], NavKey]

ACTION_MAP: dict[NavKey, dict[HWButtonInput, Action | None]] = {
    "back": {
        "up": None,
        "down": ("focus", "english"),
        "left": ("navigate", "back"),
        "right": ("focus", "english"),
        "select": ("navigate", "back"),
    },
    "english": {
        "up": ("focus", "back"),
        "down": ("focus", "spanish"),
        "left": ("focus", "back"),
        "right": ("select", "english"),
        "select": ("select", "english"),
    },
    "spanish": {
        "up": ("focus", "english"),
        "down": ("focus", "japanese"),
        "left": ("focus", "back"),
        "right": ("select", "spanish"),
        "select": ("select", "spanish"),
    },
    "japanese": {
        "up": ("focus", "spanish"),
        "down": ("focus", "italian"),
        "left": ("focus", "back"),
        "right": ("select", "japanese"),
        "select": ("select", "japanese"),
    },
    "italian": {
        "up": ("focus", "japanese"),
        "down": ("focus", "french"),
        "left": ("focus", "back"),
        "right": ("select", "italian"),
        "select": ("select", "italian"),
    },
    "french": {
        "up": ("focus", "italian"),
        "down": ("focus", "korean"),
        "left": ("focus", "back"),
        "right": ("select", "french"),
        "select": ("select", "french"),
    },
    "korean": {
        "up": ("focus", "french"),
        "down": ("focus", "russian"),
        "left": ("focus", "back"),
        "right": ("select", "korean"),
        "select": ("select", "korean"),
    },
    "russian": {
        "up": ("focus", "korean"),
        "down": None,
        "left": ("focus", "back"),
        "right": ("select", "russian"),
        "select": ("select", "russian"),
    },
}
