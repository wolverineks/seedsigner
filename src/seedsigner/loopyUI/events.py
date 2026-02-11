from seedsigner.app import App

# Try to detect if we're running on hardware or desktop
try:
    import RPi.GPIO as GPIO
    from seedsigner.hardware.buttons import HardwareButtons, HardwareButtonsConstants
    IS_HARDWARE = True
except (ImportError, RuntimeError):
    # RPi.GPIO not available or not running on Raspberry Pi
    IS_HARDWARE = False
    import pygame  # type: ignore


class Events:
    if not IS_HARDWARE:
        # Desktop mode: use pygame
        event_map = {
            pygame.K_UP: "up",
            pygame.K_DOWN: "down",
            pygame.K_LEFT: "left",
            pygame.K_RIGHT: "right",
            pygame.K_RETURN: "select",
        }
    else:
        # Hardware mode: map GPIO pins to inputs
        event_map = {
            HardwareButtonsConstants.KEY_UP: "up",
            HardwareButtonsConstants.KEY_DOWN: "down",
            HardwareButtonsConstants.KEY_LEFT: "left",
            HardwareButtonsConstants.KEY_RIGHT: "right",
            HardwareButtonsConstants.KEY_PRESS: "select",
        }

    @staticmethod
    def handle_events(app: App):
        if IS_HARDWARE:
            inputs = Events.get_hardware_inputs()
        else:
            events = Events.get_events()
            inputs = Events.get_inputs(events)

        for input in inputs:
            app.handle_input(input=input)

    @staticmethod
    def get_events():
        """Desktop mode: get pygame events"""
        if not IS_HARDWARE:
            return pygame.event.get()
        return []

    @staticmethod
    def get_inputs(events):
        """Desktop mode: convert pygame events to inputs"""
        inputs = []
        if not IS_HARDWARE:
            for event in events:
                if event.type == pygame.KEYDOWN and event.key in Events.event_map:
                    inputs.append(Events.event_map[event.key])
        return inputs

    @staticmethod
    def get_hardware_inputs():
        """Hardware mode: check GPIO button states"""
        inputs = []
        if IS_HARDWARE:
            buttons = HardwareButtons.get_instance()
            # Check each button
            for gpio_pin, input_name in Events.event_map.items():
                if buttons.check_for_low(key=gpio_pin):
                    inputs.append(input_name)
        return inputs
