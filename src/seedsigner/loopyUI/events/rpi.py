import RPi.GPIO as GPIO


if GPIO.RPI_INFO["P1_REVISION"] == 3:  # RPi with 40-pin GPIO
    # Raspberry Pi 2 and newer models share the same pin layout.

    gpio_pins = {
        "up": 31,
        "down": 35,
        "left": 29,
        "right": 37,
        "select": 33,
        "1": 40,
        "2": 38,
        "3": 36,
    }

else:  # Older 26-pin models
    # Earlier Pi revisions expose a different set of pins.

    gpio_pins = {
        "up": 5,
        "down": 11,
        "left": 3,
        "right": 15,
        "select": 7,
        "1": 16,
        "2": 12,
        "3": 8,
    }


GPIO.setmode(GPIO.BOARD)
GPIO.setup(
    gpio_pins["up"],
    GPIO.IN,
    pull_up_down=GPIO.PUD_UP,
)
GPIO.setup(
    gpio_pins["down"],
    GPIO.IN,
    pull_up_down=GPIO.PUD_UP,
)
GPIO.setup(
    gpio_pins["left"],
    GPIO.IN,
    pull_up_down=GPIO.PUD_UP,
)
GPIO.setup(
    gpio_pins["right"],
    GPIO.IN,
    pull_up_down=GPIO.PUD_UP,
)
GPIO.setup(
    gpio_pins["select"],
    GPIO.IN,
    pull_up_down=GPIO.PUD_UP,
)
GPIO.setup(
    gpio_pins["1"],
    GPIO.IN,
    pull_up_down=GPIO.PUD_UP,
)
GPIO.setup(
    gpio_pins["2"],
    GPIO.IN,
    pull_up_down=GPIO.PUD_UP,
)
GPIO.setup(
    gpio_pins["3"],
    GPIO.IN,
    pull_up_down=GPIO.PUD_UP,
)

for pin in gpio_pins.values():
    GPIO.add_event_detect(pin, GPIO.FALLING, bouncetime=50)


class Buttons:
    @staticmethod
    def get_events() -> list[str]:
        events: list[str] = []
        for name, pin in gpio_pins.items():
            if GPIO.event_detected(pin):
                events.append(name)

        return events

    @staticmethod
    def get_inputs() -> list[str]:
        events = Buttons.get_events()
        return events
