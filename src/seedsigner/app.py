from seedsigner.loopyUI import DesktopButtons
from seedsigner.router import router, Router
from seedsigner.store import store
from seedsigner.screen_cache import screen_cache


class App:
    def update(self):
        inputs = DesktopButtons.get_inputs()
        screen = screen_cache.get_or_initialize(path=router.current_route)
        for input in inputs:
            screen.handle_input(input)

        return screen.has_changed() or router.has_changed() or store.has_changed()

    def render(self):
        return screen_cache.get_or_initialize(path=router.current_route)

    def post_render(self):
        handle_lifecycle_methods(router=router)


app = App()


def handle_lifecycle_methods(router: Router):
    mounted, unmounted, focused, blurred = router.changes
    for mounted_path in mounted:
        handle("on_mount", path=mounted_path)
    for focused_path in focused:
        handle("on_focus", path=focused_path)
    for blurred_path in blurred:
        handle("on_blur", path=blurred_path)
    for unmounted_path in unmounted:
        handle("on_unmount", path=unmounted_path)
        screen_cache.clear_screen(unmounted_path)


def handle(method: str, path: str):
    screen = screen_cache.get_or_initialize(path=path)
    getattr(screen, "handle_" + method, lambda: None)()
