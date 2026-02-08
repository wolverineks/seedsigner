import pygame  # type: ignore

from seedsigner.renderer import render
from seedsigner.dimensions import Dimensions
from seedsigner.app import App
from seedsigner.router import router
from seedsigner.events import Events

pygame.init()
win: pygame.Surface = pygame.display.set_mode((Dimensions.width, Dimensions.height))
clock: pygame.time.Clock = pygame.time.Clock()


running = True


def on_quit():
    print("quitting")
    # global running = False


app = App(router=router, on_quit=on_quit)

while running:
    Events.handle_events(app)

    canvas = render(app)

    # pygame blit
    data: bytes = canvas.convert("RGB").tobytes()
    surf: pygame.Surface = pygame.image.fromstring(
        data, (Dimensions.width, Dimensions.height), "RGB"
    )
    win.blit(surf, (0, 0))
    pygame.display.flip()

    clock.tick(60)


pygame.quit()
