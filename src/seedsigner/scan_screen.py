from typing import Literal

from seedsigner.components import Body, Header, BackButton

HWButtonInput = Literal["up", "down", "left", "right", "select"]


class ScanScreen:
    def __init__(self, router):
        self.router = router
        self.state: dict[Literal["selected"], Literal["back"]] = {"selected": "back"}

    def render(self):
        selected = self.state["selected"]

        return [
            Header(
                left=BackButton(selected=selected == "back"),
                title="Scan",
            ),
            Body(),
        ]

    def handle_input(self, input: Literal["select"]):
        if input == "select":
            self.handle_select()

    def handle_select(self):
        selected = self.state["selected"]
        print(f"Selected {selected}")
        if selected == "back":
            self.router.pop()
