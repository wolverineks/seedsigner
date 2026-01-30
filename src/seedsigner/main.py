from PIL import Image, ImageDraw
from hardware.displays.display_driver import DisplayDriver

from hardware.hardware import Platform

driver = DisplayDriver(
    "st7789",
    width=int(Platform.screen_width),
    height=int(Platform.screen_height),
)


img = Image.new("RGB", (Platform.screen_width, Platform.screen_height), "black")
draw = ImageDraw.Draw(img)
draw.text((120, 120), "IT WORKS", fill="white", anchor="mm")

driver.show_image(img)
