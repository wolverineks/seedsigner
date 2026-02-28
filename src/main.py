from time import sleep
from PIL import Image

from seedsigner.dimensions import Dimensions
from seedsigner.loopyUI import render, DesktopButtons, Component
from seedsigner.router import router, Router
from seedsigner.store import Store, store
from seedsigner.helpers import get_screen, handle_lifecycle_methods


# from seedsigner.dimensions import Dimensions
# from seedsigner.hardware.displays.display_driver import DisplayDriver


# app = App(router=router, on_quit=on_quit)
# driver = DisplayDriver(
#     "st7789",
#     Dimensions.width,
#     Dimensions.height,
# )
# while running:
#     Events.handle_events(app)
#     canvas = render(app)
#     driver.show_image(canvas)
#     time.sleep(0.01)

from seedsigner.loopyUI import Desktop


def main():
    while running:
        screen = get_screen(path=router.current_route, store=store, router=router)
        inputs = DesktopButtons.get_inputs()

        # if nothing changed, skip rendering
        if nothing_changed(store, router, screen, inputs):
            sleep(0.01)
            continue

        print(f"Inputs: {inputs}")
        for input in inputs:
            screen.handle_input(input)

        handle_lifecycle_methods(store=store, router=router)

        screen = get_screen(path=router.current_route, store=store, router=router)
        canvas = render(
            screen, Image.new("RGB", (Dimensions.width, Dimensions.height), "white")
        )
        desktop.paint(canvas)

        sleep(0.01)


running = True


def on_quit():
    # print("quitting")
    global running
    running = False


def nothing_changed(
    store: Store, router: Router, screen: Component, inputs: list[str]
) -> bool:
    return (
        store.hasnt_changed()
        and router.hasnt_changed()
        and screen.hasnt_changed()
        and len(inputs) == 0
    )


desktop = Desktop()


if __name__ == "__main__":
    main()
