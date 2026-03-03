from threading import Timer

from seedsigner.toast import toast
from seedsigner.router import router, Router
from seedsigner.settings import settings
from seedsigner.store import store
from seedsigner.screen_cache import screen_cache

Timer(2, toast.show).start()

# toast.show()


class App:
    def update(self, inputs: list[str]) -> bool:
        screen = screen_cache.get(path=router.current_route)
        for input in inputs:
            screen.handle_input(input)

        return (
            screen.has_changed()
            or toast.has_changed()
            or router.has_changed()
            or store.has_changed()
            or settings.has_changed()
        )

    def render(self):
        print(f"Rendering {router.current_route}")
        return [screen_cache.get(path=router.current_route), toast]

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
    screen = screen_cache.get(path=path)
    getattr(screen, "handle_" + method, lambda: None)()
