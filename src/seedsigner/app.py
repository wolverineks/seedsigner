from dataclasses import dataclass
from typing import Callable
from threading import Timer

from seedsigner.toast import toast
from seedsigner.router import Router
from seedsigner.loopyUI import Component, Node

Timer(4, toast.show).start()


@dataclass
class App(Component):
    on_quit: Callable
    router: Router
    toast_visible: bool = False

    def render(self) -> Node:
        return [self.router, toast]

    def handle_input(self, input):
        self.router.handle_input(input)
