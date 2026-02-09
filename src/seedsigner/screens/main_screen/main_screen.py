from typing import Literal, Any

from seedsigner.components import Body, Header, LargeButton, PowerButton
from seedsigner.loopyUI import Component, Node
from .components import Grid

HWButtonInput = Literal["up", "down", "left", "right", "select"]
NavKey = Literal["scan", "tools", "settings", "seed", "back", "power"]

nav_map: dict[NavKey, dict[HWButtonInput, NavKey]] = {
    "scan": {"right": "seed", "down": "tools"},
    "seed": {"left": "scan", "down": "settings", "up": "power"},
    "tools": {"right": "settings", "up": "scan"},
    "settings": {"left": "tools", "up": "seed"},
    "back": {"right": "power", "down": "scan"},
    "power": {"down": "seed"},
}


class MainScreen(Component):
    def __init__(self, router: Any):
        self.router = router
        self.selected: NavKey = "scan"

    def render(self) -> Node:
        selected = self.selected

        return [
            Header(
                title="Home",
                right=PowerButton(selected=selected == "power"),
            ),
            Body(
                ScanButton(selected=selected == "scan"),
                SeedButton(selected=selected == "seed"),
                ToolsButton(selected=selected == "tools"),
                SettingsButton(selected=selected == "settings"),
            ),
        ]

    def handle_input(self, input: Literal["up", "down", "left", "right", "select"]):
        if input == "select":
            self.handle_select()
        else:
            selected = self.selected
            if input in nav_map[selected]:
                self.selected = nav_map[selected][input]

    def handle_select(self):
        selected = self.selected
        router = self.router

        print(f"Selected {selected}")
        if selected == "back":
            router.pop()
        else:
            router.navigate_to(selected)


def ScanButton(selected: bool):
    return LargeButton(
        label="Scan",
        icon="scan",
        x=Grid.left,
        y=Grid.top,
        selected=selected,
    )


def SeedButton(selected: bool):
    return LargeButton(
        label="Seeds",
        icon="seeds",
        x=Grid.right,
        y=Grid.top,
        selected=selected,
    )


def ToolsButton(selected: bool):
    return LargeButton(
        label="Tools",
        icon="tools",
        x=Grid.left,
        y=Grid.bottom,
        selected=selected,
    )


def SettingsButton(selected: bool):
    return LargeButton(
        label="Settings",
        x=Grid.right,
        y=Grid.bottom,
        icon="gear",
        selected=selected,
    )
