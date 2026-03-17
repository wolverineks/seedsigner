from time import sleep

from PIL import Image, ImageDraw  # type: ignore

from seedsigner.hardware.displays.display_driver import DisplayDriver


def main() -> None:
    # driver = DisplayDriver("desktop", 240, 240)
    driver = DisplayDriver("st7789", 240, 240)

    canvas = Image.new("RGB", (240, 240), "black")
    draw = ImageDraw.Draw(canvas)
    draw.rectangle((0, 0, 240 - 1, 240 - 1), outline="white")
    draw.rectangle(
        (20, 20, 240 - 21, 240 - 21), outline="white"
    )
    draw.line((0, 0, 240 - 1, 240 - 1), fill="red", width=2)
    draw.line(
        (240 - 1, 0, 0, 240 - 1), fill="green", width=2
    )

    while True:
        driver.show_image(canvas)
        sleep(1)


if __name__ == "__main__":
    main()
