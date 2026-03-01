from typing import Callable

from seedsigner.loopyUI import Component


class ScreenCache:
    def __init__(self, make_screen: Callable[[str], Component]):
        self.cache: dict[str, Component] = {}
        self.make_screen = make_screen

    def get_or_initialize(self, path: str) -> Component:
        if path not in self.cache:
            self.cache[path] = self.make_screen(path)
        return self.cache[path]

    def clear_screen(self, path: str):
        if path in self.cache:
            del self.cache[path]
