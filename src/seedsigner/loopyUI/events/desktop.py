import pygame  # type: ignore


class DesktopButtons:
    button_map = {
        pygame.K_UP: "up",
        pygame.K_DOWN: "down",
        pygame.K_LEFT: "left",
        pygame.K_RIGHT: "right",
        pygame.K_RETURN: "select",
    }

    @staticmethod
    def get_events() -> list[pygame.event.Event]:
        return pygame.event.get()

    @staticmethod
    def get_inputs() -> list[str]:
        inputs: list[str] = []
        events = DesktopButtons.get_events()

        for event in events:
            if event.type == pygame.KEYDOWN and event.key in DesktopButtons.button_map:
                inputs.append(DesktopButtons.button_map[event.key])

        return inputs
