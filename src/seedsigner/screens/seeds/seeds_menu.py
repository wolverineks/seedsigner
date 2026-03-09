from typing import Literal, TYPE_CHECKING, Tuple

if TYPE_CHECKING:
    from seedsigner.router import Router
    from seedsigner.settings import Settings
    from seedsigner.store import Store

from seedsigner.components import Body, Header, BackButton, Button
from seedsigner.loopyUI import Component, Node
from seedsigner.loopyUI.events.types import HWButtonInput


class SeedsScreen(Component):
    def __init__(self, store: "Store", router: "Router", settings: "Settings") -> None:
        super().__init__()
        self.store = store
        self.router = router
        self.settings = settings
        self.focused: NavKey = "scan_a_seedqr"

    def render(self) -> Node:
        focused = self.focused

        return [
            Header(
                left=BackButton(focused=focused == "back"),
                title="Seed",
            ),
            Body(
                Button(
                    text="Scan a SeedQR",
                    focused=focused == "scan_a_seedqr",
                ),
                Button(
                    text="Enter a 12-word seed",
                    focused=focused == "enter_a_12_word_seed",
                    y=Button.height + Body.padding,
                ),
                Button(
                    text="Enter a 24-word seed",
                    focused=focused == "enter_a_24_word_seed",
                    y=2 * (Button.height + Body.padding),
                ),
                Button(
                    text="Create a seed",
                    focused=focused == "create_a_seed",
                    y=3 * (Button.height + Body.padding),
                ),
            ),
        ]

    def handle_input(self, input: Literal["up", "down", "left", "right", "select"]):
        print(f"Handling input {input} on {self.focused}")
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


MenuKey = Literal[
    "scan_a_seedqr", "enter_a_12_word_seed", "enter_a_24_word_seed", "create_a_seed"
]
NavKey = Literal["back"] | MenuKey

Action = Tuple[Literal["navigate", "focus"], NavKey]
ACTION_MAP: dict[NavKey, dict[HWButtonInput, Action | None]] = {
    "back": {
        "up": None,
        "down": ("focus", "scan_a_seedqr"),
        "left": ("navigate", "back"),
        "right": ("navigate", "back"),
        "select": ("navigate", "back"),
    },
    "scan_a_seedqr": {
        "up": ("focus", "back"),
        "down": ("focus", "enter_a_12_word_seed"),
        "left": ("focus", "back"),
        "right": ("navigate", "scan_a_seedqr"),
        "select": ("navigate", "scan_a_seedqr"),
    },
    "enter_a_12_word_seed": {
        "up": ("focus", "scan_a_seedqr"),
        "down": ("focus", "enter_a_24_word_seed"),
        "left": ("focus", "back"),
        "right": ("navigate", "enter_a_12_word_seed"),
        "select": ("navigate", "enter_a_12_word_seed"),
    },
    "enter_a_24_word_seed": {
        "up": ("focus", "enter_a_12_word_seed"),
        "down": ("focus", "create_a_seed"),
        "left": ("focus", "back"),
        "right": ("navigate", "enter_a_24_word_seed"),
        "select": ("navigate", "enter_a_24_word_seed"),
    },
    "create_a_seed": {
        "up": ("focus", "enter_a_24_word_seed"),
        "down": None,
        "left": ("focus", "back"),
        "right": ("navigate", "create_a_seed"),
        "select": ("navigate", "create_a_seed"),
    },
}
