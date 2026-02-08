# from environment import is_raspberry_pi
# from seedsigner.dimensions import Dimensions


# class Painter:
#     @staticmethod
#     def paint(canvas):
#         if is_raspberry_pi():
#             return Painter.paint_rpi(canvas)

#         else:
#             return Painter.paint_desktop(canvas)

#     def paint_rpi(self, canvas):
#         from PIL import Image
#         from seedsigner.display_driver.st7789_mpy import ST7789

#         data = canvas
#         pil_img = Image.frombytes(
#             "RGB", (Dimensions.screen_width, Dimensions.screen_height), data
#         )

#         driver = ST7789()
#         driver.show_image(pil_img)

#     def paint_desktop(self, canvas):
#         import pygame

#         data: bytes = canvas.convert("RGB").tobytes()
#         surf: pygame.Surface = pygame.image.fromstring(
#             data, (Dimensions.screen_width, Dimensions.screen_height), "RGB"
#         )
#         win.blit(surf, (0, 0))
#         pygame.display.flip()
