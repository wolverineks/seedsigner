from typing import List, Any, Literal
from seedsigner.screens import (
    MainScreen,
    PowerScreen,
    ScanScreen,
    SeedScreen,
    SettingsScreen,
    ToolsScreen,
)

from seedsigner.loopyUI import Component, Node


class Router(Component):
    def __init__(
        self,
        routes: dict[
            str,
            type[MainScreen]
            | type[SettingsScreen]
            | type[SeedScreen]
            | type[ToolsScreen]
            | type[ScanScreen]
            | type[PowerScreen],
        ],
        initial_screen: str,
    ):
        self.routes = routes
        self.stack: List[Component] = [routes[initial_screen](self)]

    def render(self) -> Node:
        return self.current_screen()

    def navigate_to(self, route, *params):
        screen_cls = self.routes.get(route)
        if screen_cls:
            print(f"Navigating to {screen_cls}")
            self.stack.append(screen_cls(self, *params))
        else:
            print(f"Route {route} not found")

    def pop(self):
        if len(self.stack) > 1:
            screen = self.current_screen()
            print(f"Popping {screen} from stack")
            self.stack.pop()
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
    },
    initial_screen="main",
)
