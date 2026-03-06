from typing import Any

from seedsigner.loopyUI import Component
from seedsigner.loopyUI.screen_cache import ScreenCache
from seedsigner.router import router
from seedsigner.store import store
from seedsigner.settings import settings

from seedsigner.screens import (
    MainMenuScreen,
    ScanScreen,
    SettingsMenuScreen,
    ToolsMenuScreen,
    SeedsScreen,
    NotFoundScreen,
    PowerScreen,
    RestartingScreen,
    PowerOffScreen,
    LanguageScreen,
    DenominationDisplayScreen,
    PersistentSettingsScreen,
    CoordinationSoftwareScreen,
)

screen_classes: dict[str, type[Any]] = {
    "main": MainMenuScreen,
    "settings": SettingsMenuScreen,
    "tools": ToolsMenuScreen,
    "scan": ScanScreen,
    "seeds": SeedsScreen,
    "power": PowerScreen,
    "restart": RestartingScreen,
    "power-off": PowerOffScreen,
    "language": LanguageScreen,
    "coordination_software": CoordinationSoftwareScreen,
    "persistent_settings": PersistentSettingsScreen,
    "denomination_display": DenominationDisplayScreen,
}

not_found_screen = NotFoundScreen(store=store, router=router, settings=settings)


def make_screen(path: str) -> Component:
    screen_class = screen_classes.get(path)
    if screen_class:
        return screen_class(store=store, router=router, settings=settings)
    else:
        return not_found_screen


screen_cache = ScreenCache(make_screen=make_screen)
