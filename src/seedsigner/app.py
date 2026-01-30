from dataclasses import dataclass
from typing import Callable, Any
from toast import Toast


@dataclass
class App:
    on_quit: Callable
    router: Any

    modal_visible: bool = True

    def render(self):
        return [
            self.router,
            Toast(router=self.router, visible=self.modal_visible),
        ]

    def handle_input(self, input):
        if self.modal_visible:
            self.modal_visible = False
            return
        self.router.handle_input(input)
