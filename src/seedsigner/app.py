from dataclasses import dataclass
from typing import Callable

from seedsigner.toast import toast
from seedsigner.draw_command import DrawCommand
from seedsigner.router import Router

toast.show()


@dataclass
class App:
    on_quit: Callable
    router: Router
    toast_visible: bool = False

    def render(self) -> DrawCommand:
        return [self.router, toast]

    def handle_input(self, input):
        self.router.handle_input(input)
