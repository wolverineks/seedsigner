from seedsigner.main_screen import MainScreen
from seedsigner.power_screen import PowerScreen
from seedsigner.scan_screen import ScanScreen
from seedsigner.seed_screen import SeedScreen
from seedsigner.settings_screen import SettingsScreen
from seedsigner.tools_screen import ToolsScreen


class Router:
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
        ] = {},
        initial_screen=None,
    ):
        self.routes = routes
        self.stack = [initial_screen(self)] if initial_screen is not None else []

    def render(self):
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

    def handle_input(self, input):
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
    initial_screen=MainScreen,
)
