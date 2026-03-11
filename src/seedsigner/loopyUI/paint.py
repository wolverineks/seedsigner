# from environment import is_raspberry_pi
# from seedsigner.dimensions import Dimensions
import time
from PIL import Image

from seedsigner.dimensions import Dimensions

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
        from seedsigner.hardware.displays.display_driver import DisplayDriver

        self.driver = DisplayDriver(
            display_type="st7789",
            width=Dimensions.width,
            height=Dimensions.height,
        )

    def paint(self, canvas: Image.Image):
        self.driver.show_image(canvas)

    def destroy(self):
        pass


class Desktop:
    def __init__(self) -> None:
        import pygame  # type: ignore

        scale = 4
        pygame.init()
        self.pygame = pygame
        self.scale = scale
        self.win = pygame.display.set_mode(
            (Dimensions.width * self.scale, Dimensions.height * self.scale)
        )
        self.clock = pygame.time.Clock()

    def paint(self, canvas: Image.Image):
        before_convert = time.time()
        data: bytes = canvas.convert("RGB").tobytes()
        after_convert = time.time()
        # print("CONVERT:, ", after_convert - before_convert)

        before = time.time()
        surf = self.pygame.image.fromstring(
            data, (Dimensions.width, Dimensions.height), "RGB"
        )
        # print("FROM_STRING: ", time.time() - before)

        before = time.time()
        scaled_surf = self.pygame.transform.scale(
            surf,
            (Dimensions.width * self.scale, Dimensions.height * self.scale),
        )
        self.win.blit(scaled_surf, (0, 0))
        # print("BLIT: ", time.time() - before)

        before = time.time()
        self.pygame.display.flip()
        # print("FLIP: ", time.time() - before)

        # self.clock.tick(60)

    def destroy(self):
        self.pygame.quit()
