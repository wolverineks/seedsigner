from typing import Literal, TYPE_CHECKING

from seedsigner.components.components import CheckmarkButton


if TYPE_CHECKING:
    from seedsigner.router import Router
    from seedsigner.store import Store
    from seedsigner.settings import Settings

from seedsigner.components import Body, Header, BackButton
from seedsigner.loopyUI import Component, Node

HWButtonInput = Literal["up", "down", "right", "left", "select"]
NavKey = Literal[
    "btc",
    "sats",
    "threshold",
    "hybrid",
    "back",
]

nav_map: dict[NavKey, dict[HWButtonInput, NavKey]] = {
    "back": {
        "right": "btc",
        "down": "btc",
    },
    "btc": {
        "down": "sats",
        "up": "back",
        "left": "back",
    },
    "sats": {
        "up": "btc",
        "down": "threshold",
        "left": "back",
    },
    "threshold": {
        "up": "sats",
        "down": "hybrid",
        "left": "back",
    },
    "hybrid": {
        "up": "threshold",
        "left": "back",
    },
}


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
            self.settings.denomination_display = selected
