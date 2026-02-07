from typing import Literal

from seedsigner.components import Body, Header, BackButton, Button

HWButtonInput = Literal["up", "down", "left", "right", "select"]
NavKey = Literal[
    "back",
    "scan_a_seedqr",
    "enter_a_12_word_seed",
    "enter_a_24_word_seed",
    "create_a_seed",
]

NAV_MAP: dict[NavKey, dict[HWButtonInput, NavKey]] = {
    "back": {
        "down": "scan_a_seedqr",
    },
    "scan_a_seedqr": {
        "up": "back",
        "down": "enter_a_12_word_seed",
    },
    "enter_a_12_word_seed": {
        "up": "scan_a_seedqr",
        "down": "enter_a_24_word_seed",
    },
    "enter_a_24_word_seed": {
        "up": "enter_a_12_word_seed",
        "down": "create_a_seed",
    },
    "create_a_seed": {
        "up": "enter_a_24_word_seed",
    },
}


class SeedScreen:
    def __init__(self, router):
        self.router = router
        self.state: dict[Literal["selected"], NavKey] = {"selected": "scan_a_seedqr"}

    def render(self):
        selected = self.state["selected"]

        return [
            Header(
                left=BackButton(selected=selected == "back"),
                title="Seed",
            ),
            Body(
                Button(
                    text="Scan a SeedQR", selected=selected == "scan_a_seedqr", index=0
                ),
                Button(
                    text="Enter a 12-word seed",
                    selected=selected == "enter_a_12_word_seed",
                    index=1,
                ),
                Button(
                    text="Enter a 24-word seed",
                    selected=selected == "enter_a_24_word_seed",
                    index=2,
                ),
                Button(
                    text="Create a seed", selected=selected == "create_a_seed", index=3
                ),
            ),
        ]

    def handle_input(self, input: Literal["up", "down", "left", "right", "select"]):
        if input == "select":
            self.handle_select()
        else:
            selected = self.state["selected"]
            if input in NAV_MAP[selected]:
                self.state["selected"] = NAV_MAP[selected][input]

    def handle_select(self):
        selected = self.state["selected"]
        print(f"Selected {selected}")
        if selected == "back":
            self.router.pop()
        else:
            self.router.navigate_to(selected)
