from time import sleep
from typing import Any

from seedsigner.loopyUI import Desktop, RPI, get_platform, render
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

platform = get_platform()
display: Any
InputDevice: Any

if platform == "desktop":
    from seedsigner.loopyUI.events.desktop import DesktopButtons as InputDevice

    display = Desktop()
elif platform == "rpi":
    from seedsigner.loopyUI.events.rpi import Buttons as InputDevice

    display = RPI()
else:
    raise RuntimeError(
        "Unsupported platform. On Raspberry Pi, install requirements-raspi.txt and RPi.GPIO; on desktop, install requirements-desktop.txt."
    )


def main():
    while running:
        inputs = InputDevice.get_inputs()
        updated = app.update(inputs)
        if updated:
            canvas = render(app)
            display.paint(canvas)
            app.post_render()

        sleep(0.01)


running = True


def on_quit():
    # print("quitting")
    global running
    running = False


if __name__ == "__main__":
    main()
