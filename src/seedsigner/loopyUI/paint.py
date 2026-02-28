# from environment import is_raspberry_pi
# from seedsigner.dimensions import Dimensions
import pygame  # type: ignore
from PIL import Image
from seedsigner.dimensions import Dimensions
import time

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


class RPI:
    def __init__(self) -> None:

        from seedsigner.hardware.displays.ST7789 import ST7789

        self.driver = ST7789()

    def paint(self, canvas: Image.Image):
        from PIL import Image

        pil_img = Image.frombytes(
            "RGB", (Dimensions.screen_width, Dimensions.screen_height), canvas
        )

        self.driver.show_image(pil_img)

    def destroy(self):
        pygame.quit()


class Desktop:
    def __init__(self) -> None:
        pygame.init()
        self.win: pygame.Surface = pygame.display.set_mode(
            (Dimensions.width, Dimensions.height)
        )
        self.clock: pygame.time.Clock = pygame.time.Clock()

    def paint(self, canvas: Image.Image):
        before_convert = time.time()
        data: bytes = canvas.convert("RGB").tobytes()
        after_convert = time.time()
        # print("CONVERT:, ", after_convert - before_convert)

        before = time.time()
        surf: pygame.Surface = pygame.image.fromstring(
            data, (Dimensions.width, Dimensions.height), "RGB"
        )
        # print("FROM_STRING: ", time.time() - before)

        before = time.time()
        self.win.blit(surf, (0, 0))
        # print("BLIT: ", time.time() - before)

        before = time.time()
        pygame.display.flip()
        # print("FLIP: ", time.time() - before)

        # self.clock.tick(60)

    def destroy(self):
        pygame.quit()
