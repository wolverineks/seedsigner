"""Desktop display driver that mimics the Waveshare LCD using pygame."""

from PIL import Image
import pygame  # type: ignore
from seedsigner.dimensions import Dimensions

DARK_BLUE = (0, 0, 80)


class DesktopDisplay:
    """A pygame-backed display used when running SeedSigner on a PC."""

    def __init__(self, width: int = 240, height: int = 240, scale: int = 4):
        pygame.init()
        self.width = width
        self.height = height
        self.scale = scale
        self.win: pygame.Surface = pygame.display.set_mode(
            (self.width * self.scale, self.height * self.scale)
        )
        self.clock: pygame.time.Clock = pygame.time.Clock()

    def show_image(self, image: Image.Image, x_start: int = 0, y_start: int = 0):
        data: bytes = image.convert("RGB").tobytes()
        surf: pygame.Surface = pygame.image.fromstring(
            data, (Dimensions.width, Dimensions.height), "RGB"
        )
        scaled_surf: pygame.Surface = pygame.transform.scale(
            surf,
            (self.width * self.scale, self.height * self.scale),
        )
        self.win.blit(scaled_surf, (0, 0))
        pygame.display.flip()

        self.clock.tick(60)

        # Pump events to keep the window responsive even when no input is read
        # self.pygame.event.pump()
        # self.pygame.display.flip()
