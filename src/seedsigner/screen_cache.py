from typing import Any

from seedsigner.loopyUI import Component
from seedsigner.loopyUI.screen_cache import ScreenCache
from seedsigner.router import router
from seedsigner.store import store
from seedsigner.settings import settings

from seedsigner.screens import (
    MainMenuScreen,
    ScanScreen,
    SettingsScreen,
    ToolsScreen,
    SeedsScreen,
    NotFoundScreen,
    PowerScreen,
    RestartingScreen,
    PowerOffScreen,
    LanguageScreen,
)

screen_classes: dict[str, type[Any]] = {
    "main": MainMenuScreen,
    "settings": SettingsScreen,
    "tools": ToolsScreen,
    "scan": ScanScreen,
    "seeds": SeedsScreen,
    "power": PowerScreen,
    "restart": RestartingScreen,
    "power-off": PowerOffScreen,
    "language": LanguageScreen,
}

not_found_screen = NotFoundScreen(store=store, router=router, settings=settings)


def make_screen(path: str) -> Component:
    screen_class = screen_classes.get(path)
    if screen_class:
        return screen_class(store=store, router=router, settings=settings)
    else:
        return not_found_screen


screen_cache = ScreenCache(make_screen=make_screen)
