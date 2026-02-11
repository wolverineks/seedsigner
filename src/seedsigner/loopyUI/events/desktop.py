import pygame  # type: ignore

from seedsigner.app import App


class Events:
    event_map = {
        pygame.K_UP: "up",
        pygame.K_DOWN: "down",
        pygame.K_LEFT: "left",
        pygame.K_RIGHT: "right",
        pygame.K_RETURN: "select",
    }

    @staticmethod
    def handle_events(app: App):
        events = Events.get_events()
        inputs = Events.get_inputs(events)

        for input in inputs:
            app.handle_input(input=input)

    @staticmethod
    def get_events() -> list[pygame.event.Event]:
        return pygame.event.get()

    @staticmethod
    def get_inputs(events: list[pygame.event.Event]) -> list[str]:
        inputs: list[str] = []
        for event in events:
            if event.type == pygame.KEYDOWN and event.key in Events.event_map:
                inputs.append(Events.event_map[event.key])

        return inputs
