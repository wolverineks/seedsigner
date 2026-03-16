from time import sleep

from PIL import Image, ImageDraw  # type: ignore

from seedsigner.dimensions import Dimensions
from seedsigner.hardware.displays.display_driver import DisplayDriver


def main() -> None:
    # driver = DisplayDriver("desktop", Dimensions.width, Dimensions.height)
    driver = DisplayDriver("st7789", Dimensions.width, Dimensions.height)

    canvas = Image.new("RGB", (Dimensions.width, Dimensions.height), "black")
    draw = ImageDraw.Draw(canvas)
    draw.rectangle((0, 0, Dimensions.width - 1, Dimensions.height - 1), outline="white")
    draw.rectangle(
        (20, 20, Dimensions.width - 21, Dimensions.height - 21), outline="white"
    )
    draw.line((0, 0, Dimensions.width - 1, Dimensions.height - 1), fill="red", width=2)
    draw.line(
        (Dimensions.width - 1, 0, 0, Dimensions.height - 1), fill="green", width=2
    )

    while True:
        driver.show_image(canvas)
        sleep(1)


if __name__ == "__main__":
    main()
