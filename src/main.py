from seedsigner.loopyUI import render, Events
from seedsigner.app import App
from seedsigner.router import router
import time
import sys
from seedsigner.dimensions import Dimensions


running = True


def on_quit():
    print("quitting")
    global running
    running = False


from seedsigner.hardware.displays.display_driver import DisplayDriver

print("=" * 60)
print("SeedSigner Starting...")
print("=" * 60)
print(f"Display dimensions: {Dimensions.width}x{Dimensions.height}")
print(f"Python version: {sys.version}")

try:
    print("Initializing app...")
    app = App(router=router, on_quit=on_quit)
    print("App initialized successfully")
    
    print("Initializing display driver (st7789)...")
    driver = DisplayDriver(
        "st7789",
        Dimensions.width,
        Dimensions.height,
    )
    print(f"Display driver initialized: {driver}")
    print("=" * 60)
    print("Starting main loop...")
    print("=" * 60)
    
    loop_count = 0
    while running:
        Events.handle_events(app)
        canvas = render(app)
        driver.show_image(canvas)
        time.sleep(0)
        
        # Print status every 100 loops to show it's alive
        loop_count += 1
        if loop_count % 100 == 0:
            print(f"Main loop running... (iteration {loop_count})")
            
except Exception as e:
    print("=" * 60)
    print("ERROR during initialization or main loop:")
    print(f"Error type: {type(e).__name__}")
    print(f"Error message: {str(e)}")
    import traceback
    traceback.print_exc()
    print("=" * 60)
    sys.exit(1)

print("SeedSigner shutting down normally")

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