from typing import Any


class DesktopButtons:
    @staticmethod
    def get_events() -> list[Any]:
        import pygame  # type: ignore

        return pygame.event.get()

    @staticmethod
    def get_inputs() -> list[str]:
        import pygame  # type: ignore

        button_map = {
            pygame.K_UP: "up",
            pygame.K_DOWN: "down",
            pygame.K_LEFT: "left",
            pygame.K_RIGHT: "right",
            pygame.K_RETURN: "select",
        }

        inputs: list[str] = []
        events = DesktopButtons.get_events()

        for event in events:
            if event.type == pygame.KEYDOWN and event.key in button_map:
                inputs.append(button_map[event.key])

        return inputs
