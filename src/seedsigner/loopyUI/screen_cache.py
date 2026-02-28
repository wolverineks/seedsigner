from typing import Callable

from seedsigner.loopyUI import Component


class ScreenCache:
    def __init__(self):
        self.cache: dict[str, Component] = {}

    def get_or_initialize(
        self, path: str, make_screen: Callable[[], Component]
    ) -> Component:
        if path not in self.cache:
            self.cache[path] = make_screen()
        return self.cache[path]

    def clear_screen(self, path: str):
        if path in self.cache:
            del self.cache[path]
