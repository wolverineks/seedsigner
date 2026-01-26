from typing import Literal

from components.components import Header, Body, BackButton, Button

HWButtonInput = Literal["up", "down", "left", "right", "select"]
NavKey = Literal["scan", "tools", "settings", "seed", "back", "power"]

nav_map: dict[NavKey, dict[HWButtonInput, NavKey]] = {
    "back": {"down": "scan"},
    "scan": {"down": "tools", "up": "back"},
    "tools": {"up": "scan", "down": "seed"},
    "seed": {"up": "tools"},
}


class ToolsScreen:
    def __init__(self, router):
        self.router = router
        self.state: dict[Literal["selected"], NavKey] = {"selected": "scan"}

    def render(self):
        selected = self.state["selected"]

        return [
            Header(
                left=BackButton(selected=selected == "back"),
                title="Settings",
            ),
            Body(
                Button(text="Scan", selected=selected == "scan", index=0),
                Button(text="Tools", selected=selected == "tools", index=1),
                Button(text="Seed", selected=selected == "seed", index=2),
            ),
        ]

    def handle_input(self, input: Literal["up", "down", "left", "right", "select"]):
        if input == "select":
            self.handle_select()
        else:
            selected = self.state["selected"]
            if input in nav_map[selected]:
                self.state["selected"] = nav_map[selected][input]

    def handle_select(self):
        selected = self.state["selected"]
        print(f"Selected {selected}")
        if selected == "back":
            self.router.pop()
        else:
            self.router.navigate_to(selected)
