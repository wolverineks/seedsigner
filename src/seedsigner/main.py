# from PIL import Image, ImageDraw
# from time import sleep
# import pygame

# from hardware.hardware import Platform

# pygame.init()
# screen = pygame.display.set_mode(Platform.screen_dimensions)

# image = Image.new("RGB", Platform.screen_dimensions, "red")
# draw = ImageDraw.Draw(image)
# draw.text((120, 120), "IT WORKS", fill="white", font_size=30, anchor="mm")

# pg_img = pygame.image.fromstring(image.tobytes(), image.size, image.mode)
# pygame.event.pump()  # Pump events to keep the window responsive even when no input is read
# screen.blit(pg_img, (0, 0))
# pygame.display.flip()

# sleep(4)


from PIL import Image, ImageDraw
from time import sleep

from hardware.hardware import Platform
from hardware.displays.ST7789 import ST7789


image = Image.new("RGB", Platform.screen_dimensions, "red")
draw = ImageDraw.Draw(image)
draw.text((120, 120), "IT WORKS", fill="white", font_size=30, anchor="mm")

driver = ST7789()
driver.show_image(image, 0, 0)

sleep(4)
