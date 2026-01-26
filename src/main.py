from PIL import Image
from renderer import render
import pygame  # type: ignore
from hardware import Platform
from router import router

# loop
pygame.init()
win: pygame.Surface = pygame.display.set_mode(
    (Platform.screen_width, Platform.screen_height)
)
clock: pygame.time.Clock = pygame.time.Clock()

running: bool = True

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                router.current_screen().handle_input("up")
            elif e.key == pygame.K_DOWN:
                router.current_screen().handle_input("down")
            elif e.key == pygame.K_LEFT:
                router.current_screen().handle_input("left")
            elif e.key == pygame.K_RIGHT:
                router.current_screen().handle_input("right")
            elif e.key == pygame.K_RETURN:
                router.current_screen().handle_input("select")

    # "render" phase
    canvas: Image.Image = render(router.current_screen())

    # pygame blit
    data: bytes = canvas.convert("RGB").tobytes()
    surf: pygame.Surface = pygame.image.fromstring(
        data, (Platform.screen_width, Platform.screen_height), "RGB"
    )
    win.blit(surf, (0, 0))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
