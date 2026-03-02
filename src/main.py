from time import sleep

from seedsigner.loopyUI import render
from seedsigner.app import app


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

from seedsigner.loopyUI import Desktop, DesktopButtons


def main():
    while running:
        inputs = DesktopButtons.get_inputs()
        updated = app.update(inputs)
        if updated:
            canvas = render(app)
            desktop.paint(canvas)
            app.post_render()

        sleep(0.01)


running = True


def on_quit():
    # print("quitting")
    global running
    running = False


desktop = Desktop()


if __name__ == "__main__":
    main()
