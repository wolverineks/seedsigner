from dataclasses import dataclass
from typing import Callable, Any


@dataclass
class App:
    on_quit: Callable
    router: Any

    def render(self):
        return self.router.current_screen()

    def handle_input(self, input):
        screen = self.router.current_screen()
        screen.handle_input(input)
