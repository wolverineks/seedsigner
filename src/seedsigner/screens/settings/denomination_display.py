from typing import Literal, TYPE_CHECKING

from seedsigner.components import CheckmarkButton


if TYPE_CHECKING:
    from seedsigner.router import Router
    from seedsigner.store import Store
    from seedsigner.settings import Settings

from seedsigner.components import Body, Header, BackButton
from seedsigner.loopyUI import Component, Node
from seedsigner.loopyUI.events.types import HWButtonInput


class DenominationDisplayScreen(Component):
    def __init__(self, store: "Store", router: "Router", settings: "Settings") -> None:
        super().__init__()
        self.store = store
        self.router = router
        self.settings = settings
        self.focused: NavKey = settings.denomination_display

    def render(self) -> Node:
        focused = self.focused

        return [
            Header(
                left=BackButton(focused=focused == "back"),
                title="Denomination",
            ),
            Body(
                CheckmarkButton(
                    text="BTC",
                    focused=focused == "btc",
                    checked=self.settings.denomination_display == "btc",
                    y=Body.button_y(4),
                    x=Body.padding,
                ),
                CheckmarkButton(
                    text="sats",
                    focused=focused == "sats",
                    checked=self.settings.denomination_display == "sats",
                    y=Body.button_y(3),
                    x=Body.padding,
                ),
                CheckmarkButton(
                    text="Threshold at 0.01",
                    focused=focused == "threshold",
                    checked=self.settings.denomination_display == "threshold",
                    y=Body.button_y(2),
                    x=Body.padding,
                ),
                CheckmarkButton(
                    text="BTC | sats hybrid",
                    focused=focused == "hybrid",
                    checked=self.settings.denomination_display == "hybrid",
                    y=Body.button_y(1),
                    x=Body.padding,
                ),
            ),
        ]

    def handle_on_focus(self) -> None:
        self.set_focused(self.settings.denomination_display)

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
            self.settings.denomination_display = key


NavKey = Literal[
    "btc",
    "sats",
    "threshold",
    "hybrid",
    "back",
]

Action = tuple[Literal["navigate", "focus", "select"], NavKey]

ACTION_MAP: dict[NavKey, dict[HWButtonInput, Action | None]] = {
    "back": {
        "up": None,
        "down": ("focus", "btc"),
        "left": ("navigate", "back"),
        "right": ("focus", "btc"),
        "select": ("navigate", "back"),
    },
    "btc": {
        "up": ("focus", "back"),
        "down": ("focus", "sats"),
        "left": ("focus", "back"),
        "right": ("select", "btc"),
        "select": ("select", "btc"),
    },
    "sats": {
        "up": ("focus", "btc"),
        "down": ("focus", "threshold"),
        "left": ("focus", "back"),
        "right": ("select", "sats"),
        "select": ("select", "sats"),
    },
    "threshold": {
        "up": ("focus", "sats"),
        "down": ("focus", "hybrid"),
        "left": ("focus", "back"),
        "right": ("select", "threshold"),
        "select": ("select", "threshold"),
    },
    "hybrid": {
        "up": ("focus", "threshold"),
        "down": None,
        "left": ("focus", "back"),
        "right": ("select", "hybrid"),
        "select": ("select", "hybrid"),
    },
}
