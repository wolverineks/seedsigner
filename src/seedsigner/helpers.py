from seedsigner.loopyUI import Component
from seedsigner.loopyUI.screen_cache import ScreenCache
from seedsigner.router import Router
from seedsigner.store import Store

from seedsigner.screens import (
    MainScreen,
    ScanScreen,
    SettingsScreen,
    ToolsScreen,
    SeedsScreen,
    NotFoundScreen,
    PowerScreen,
    RestartingScreen,
    PowerOffScreen,
)

screen_cache = ScreenCache()

screen_classes: dict[str, type[Component]] = {
    # wrap with connect
    "main": MainScreen,
    "settings": SettingsScreen,
    "tools": ToolsScreen,
    "scan": ScanScreen,
    "seeds": SeedsScreen,
    "power": PowerScreen,
    "restart": RestartingScreen,
    "power-off": PowerOffScreen,
    "not_found": NotFoundScreen,
}


def make_screen(router: Router, store: Store) -> Component:
    path = router.current_route
    screen_class = screen_classes.get(path)
    if screen_class:
        return screen_class(store=store, router=router)
    else:
        return NotFoundScreen(store=store, router=router)


def get_screen(path: str, store: Store, router: Router):
    return screen_cache.get_or_initialize(
        path=path, make_screen=lambda: make_screen(router=router, store=store)
    )


def handle_lifecycle_methods(
    store: Store,
    router: Router,
):
    mounted, unmounted, focused, blurred = router.changes
    for mounted_path in mounted:
        handle("on_mount", path=mounted_path, store=store, router=router)
    for focused_path in focused:
        handle("on_focus", path=focused_path, store=store, router=router)
    for blurred_path in blurred:
        handle("on_blur", path=blurred_path, store=store, router=router)
    for unmounted_path in unmounted:
        handle("on_unmount", path=unmounted_path, store=store, router=router)
        screen_cache.cache.pop(unmounted_path, None)


def handle(method: str, path: str, router: Router, store: Store):
    screen = get_screen(path=path, store=store, router=router)
    getattr(screen, "handle_" + method, lambda: None)()
