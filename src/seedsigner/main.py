from PIL import Image
from renderer import render
import pygame  # type: ignore
from hardware import Platform
from app import App
from router import router
from events import Events

pygame.init()
win: pygame.Surface = pygame.display.set_mode(
    (Platform.screen_width, Platform.screen_height)
)
clock: pygame.time.Clock = pygame.time.Clock()


running = True  # 'count' is bound in the enclosing scope


def on_quit():
    print("quitting")
    # global running = False


while running:
    app = App(router=router, on_quit=on_quit)
    Events.handle_events(app)

    # "render" phase
    canvas: Image.Image = render(app)

    # pygame blit
    data: bytes = canvas.convert("RGB").tobytes()
    surf: pygame.Surface = pygame.image.fromstring(
        data, (Platform.screen_width, Platform.screen_height), "RGB"
    )
    win.blit(surf, (0, 0))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
