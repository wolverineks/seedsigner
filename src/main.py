from seedsigner.loopyUI import render, Events
from seedsigner.app import App
from seedsigner.router import router
import time
from seedsigner.dimensions import Dimensions


running = True


def on_quit():
    print("quitting")
    global running
    running = False


from seedsigner.hardware.displays.display_driver import DisplayDriver

app = App(router=router, on_quit=on_quit)
driver = DisplayDriver(
    "st7789",
    Dimensions.width,
    Dimensions.height,
)
while running:
    Events.handle_events(app)
    canvas = render(app)
    driver.show_image(canvas)
    time.sleep(0)

# from seedsigner.loopyUI import Desktop
# desktop = Desktop()
# app = App(router=router, on_quit=on_quit)

# while running:
#     Events.handle_events(app)

#     before_render = time.time()
#     canvas = render(app)
#     after_render = time.time()

#     print("RENDER: ", after_render - before_render)

#     before_paint = time.time()
#     desktop.paint(canvas)
#     after_paint = time.time()
#     print("PAINT: ", after_paint - before_paint)