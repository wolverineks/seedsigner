from typing import List, Any, Literal
from seedsigner.screens import (
    MainScreen,
    PowerScreen,
    ScanScreen,
    SeedScreen,
    SettingsScreen,
    ToolsScreen,
    RestartingScreen,
    PowerOffScreen,
)

from seedsigner.loopyUI import Component, Node

Route = Literal[
    "main",
    "settings",
    "scan",
    "tools",
    "seed",
    "power",
    "restart",
    "power-off",
]


class Router(Component):
    def __init__(
        self,
        routes: dict[str, type[Component]],
        initial_screen: str,
    ):
        self.routes = routes
        screen_cls = routes[initial_screen]
        self.stack = [screen_cls(self)]

    def render(self) -> Node:
        return self.current_screen()

    def navigate_to(self, route: Route, *params: Any):
        screen_cls = self.routes.get(route)
        if screen_cls:
            current_screen = self.current_screen()
            print("Blurring: ", current_screen)
            current_screen.handle_on_blur()

            next_screen = screen_cls(self, *params)
            print("Mounting: ", next_screen)
            next_screen.handle_on_mount()

            print("Focusing: ", next_screen)
            next_screen.handle_on_focus()

            self.stack.append(next_screen)

        else:
            print(f"Route {route} not found")

    def pop(self):
        if len(self.stack) > 1:
            current_screen = self.current_screen()
            print("Blurring: ", current_screen)
            current_screen.handle_on_blur()

            print("Unmounting: ", current_screen)
            current_screen.handle_on_unmount()

            self.stack.pop()

            next_screen = self.current_screen()
            print("Focusing: ", next_screen)
            next_screen.handle_on_focus()

        else:
            print("Cannot pop the last screen")

    def current_screen(self):
        return self.stack[-1]

    def handle_input(self, input: Any) -> Any:
        return self.current_screen().handle_input(input)


router = Router(
    {
        "main": MainScreen,
        "settings": SettingsScreen,
        "scan": ScanScreen,
        "tools": ToolsScreen,
        "seed": SeedScreen,
        "power": PowerScreen,
        "restart": RestartingScreen,
        "power-off": PowerOffScreen,
    },
    initial_screen="main",
)
