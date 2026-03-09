from typing import Literal, TYPE_CHECKING

from seedsigner.components import CheckmarkButton
from seedsigner.settings.language import LANGUAGE_OPTIONS


if TYPE_CHECKING:
    from seedsigner.router import Router
    from seedsigner.store import Store
    from seedsigner.settings import Settings

from seedsigner.components import Body, Header, BackButton
from seedsigner.loopyUI import Component, Node
from seedsigner.loopyUI.events.types import HWButtonInput


class LanguageScreen(Component):
    def __init__(self, store: "Store", router: "Router", settings: "Settings") -> None:
        super().__init__()
        self.store = store
        self.router = router
        self.settings = settings
        self.focused: NavKey = "english"

    def render(self) -> Node:
        focused = self.focused

        return [
            Header(
                left=BackButton(focused=focused == "back"),
                title="Language",
            ),
            Body(
                CheckmarkButton(
                    text="English",
                    focused=focused == "english",
                    checked=self.settings.language == "english",
                    index=0,
                ),
                CheckmarkButton(
                    text="Español",
                    focused=focused == "spanish",
                    checked=self.settings.language == "spanish",
                    index=1,
                ),
                CheckmarkButton(
                    text="日本語",
                    focused=focused == "japanese",
                    checked=self.settings.language == "japanese",
                    index=2,
                ),
                CheckmarkButton(
                    text="Italiano",
                    focused=focused == "italian",
                    checked=self.settings.language == "italian",
                    index=3,
                ),
                CheckmarkButton(
                    text="Français",
                    focused=focused == "french",
                    checked=self.settings.language == "french",
                    index=4,
                ),
                CheckmarkButton(
                    text="한국어",
                    focused=focused == "korean",
                    checked=self.settings.language == "korean",
                    index=5,
                ),
                CheckmarkButton(
                    text="Русский",
                    focused=focused == "russian",
                    checked=self.settings.language == "russian",
                    index=6,
                ),
            ),
        ]

    def handle_on_focus(self) -> None:
        language = self.settings.language
        if language in LANGUAGE_OPTIONS:
            self.set_focused(language)

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
        elif type == "select":
            self.settings.language = key


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
