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
        self.selected: NavKey = settings.denomination_display

    def render(self) -> Node:
        selected = self.selected

        return [
            Header(
                left=BackButton(selected=selected == "back"),
                title="Denomination",
            ),
            Body(
                [
                    CheckmarkButton(
                        text="BTC",
                        selected=selected == "btc",
                        checked=self.settings.denomination_display == "btc",
                        index=0,
                    ),
                    CheckmarkButton(
                        text="sats",
                        selected=selected == "sats",
                        checked=self.settings.denomination_display == "sats",
                        index=1,
                    ),
                    CheckmarkButton(
                        text="Threshold at 0.01",
                        selected=selected == "threshold",
                        checked=self.settings.denomination_display == "threshold",
                        index=2,
                    ),
                    CheckmarkButton(
                        text="BTC | sats hybrid",
                        selected=selected == "hybrid",
                        checked=self.settings.denomination_display == "hybrid",
                        index=3,
                    ),
                ]
            ),
        ]

    def handle_on_focus(self) -> None:
        self.set_selected(self.settings.denomination_display)

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
            self.settings.denomination_display = selected


NavKey = Literal[
    "btc",
    "sats",
    "threshold",
    "hybrid",
    "back",
]

Action = tuple[Literal["navigate", "focus"], NavKey]

ACTION_MAP: dict[NavKey, dict[HWButtonInput, Action | None]] = {
    "back": {
        "right": ("focus", "btc"),
        "down": ("focus", "btc"),
        "left": ("navigate", "back"),
    },
    "btc": {
        "down": ("focus", "sats"),
        "up": ("focus", "back"),
        "left": ("focus", "back"),
    },
    "sats": {
        "up": ("focus", "btc"),
        "down": ("focus", "threshold"),
        "left": ("focus", "back"),
    },
    "threshold": {
        "up": ("focus", "sats"),
        "down": ("focus", "hybrid"),
        "left": ("focus", "back"),
    },
    "hybrid": {
        "up": ("focus", "threshold"),
        "left": ("focus", "back"),
    },
}
