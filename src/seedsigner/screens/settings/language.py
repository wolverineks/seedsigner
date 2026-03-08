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
        self.selected: NavKey = "english"

    def render(self) -> Node:
        selected = self.selected

        return [
            Header(
                left=BackButton(selected=selected == "back"),
                title="Language",
            ),
            Body(
                [
                    CheckmarkButton(
                        text="English",
                        selected=selected == "english",
                        checked=self.settings.language == "english",
                        index=0,
                    ),
                    CheckmarkButton(
                        text="Español",
                        selected=selected == "spanish",
                        checked=self.settings.language == "spanish",
                        index=1,
                    ),
                    CheckmarkButton(
                        text="日本語",
                        selected=selected == "japanese",
                        checked=self.settings.language == "japanese",
                        index=2,
                    ),
                    CheckmarkButton(
                        text="Italiano",
                        selected=selected == "italian",
                        checked=self.settings.language == "italian",
                        index=3,
                    ),
                    CheckmarkButton(
                        text="Français",
                        selected=selected == "french",
                        checked=self.settings.language == "french",
                        index=4,
                    ),
                    CheckmarkButton(
                        text="한국어",
                        selected=selected == "korean",
                        checked=self.settings.language == "korean",
                        index=5,
                    ),
                    CheckmarkButton(
                        text="Русский",
                        selected=selected == "russian",
                        checked=self.settings.language == "russian",
                        index=6,
                    ),
                ]
            ),
        ]

    def handle_on_focus(self) -> None:
        language = self.settings.language
        if language in LANGUAGE_OPTIONS:
            self.set_selected(language)

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
            self.settings.language = selected


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

Action = tuple[Literal["navigate", "focus"], NavKey]

ACTION_MAP: dict[NavKey, dict[HWButtonInput, Action | None]] = {
    "back": {
        "right": ("focus", "english"),
        "down": ("focus", "english"),
        "left": ("navigate", "back"),
    },
    "english": {
        "down": ("focus", "spanish"),
        "up": ("focus", "back"),
        "left": ("focus", "back"),
    },
    "spanish": {
        "up": ("focus", "english"),
        "down": ("focus", "japanese"),
        "left": ("focus", "back"),
    },
    "japanese": {
        "up": ("focus", "spanish"),
        "down": ("focus", "italian"),
        "left": ("focus", "back"),
    },
    "italian": {
        "up": ("focus", "japanese"),
        "down": ("focus", "french"),
        "left": ("focus", "back"),
    },
    "french": {
        "up": ("focus", "italian"),
        "down": ("focus", "korean"),
        "left": ("focus", "back"),
    },
    "korean": {
        "up": ("focus", "french"),
        "down": ("focus", "russian"),
        "left": ("focus", "back"),
    },
    "russian": {
        "up": ("focus", "korean"),
        "left": ("focus", "back"),
    },
}
