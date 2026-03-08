from dataclasses import dataclass
from PIL import ImageFont

from seedsigner.loopyUI import Component, Text, Node, Box
from seedsigner.dimensions import Dimensions
from seedsigner.colors import Colors
from .helpers import get_icon_info


@dataclass
class Header(Component):
    height = 40
    width = Dimensions.width
    padding = 8

    left: Component | None = None
    right: Component | None = None

    title: str = ""

    def render(self) -> Node:
        size = 20
        font = ImageFont.load_default(size=size)
        left, _, right, _ = font.getbbox(self.title)
        width = right - left

        text_x = int(Header.width / 2) - int(width / 2)

        return Box(
            x=0,
            y=0,
            w=Dimensions.width,
            h=Header.height,
            fill=Colors.background,
            children=(
                self.left,
                Text(x=text_x, y=10, text=self.title, fill=Colors.text, size=size),
                self.right,
            ),
        )


@dataclass
class PowerButton(Component):
    height = Header.height - Header.padding - Header.padding
    width = height
    x = Dimensions.width - Header.padding - width
    y = Header.padding

    selected: bool = False

    def render(self) -> Node:
        font, code = get_icon_info("power", 18)
        ascent = (font.getmetrics() or (0, 0))[0]
        left, _, right, _ = font.getbbox(code)
        icon_y = int((PowerButton.height - ascent) / 2)
        icon_x = int((PowerButton.width - (right - left)) / 2)

        return Box(
            x=PowerButton.x,
            y=PowerButton.y,
            w=PowerButton.width,
            h=PowerButton.height,
            fill=Colors.button.focused.background
            if self.selected
            else Colors.button.background,
            radius=6,
            children=(
                Text(
                    x=icon_x,
                    y=icon_y,
                    text=code,
                    fill=Colors.button.focused.text
                    if self.selected
                    else Colors.button.text,
                    size=18,
                    font=font,
                ),
            ),
        )


@dataclass
class BackButton(Component):
    height = Header.height - Header.padding - Header.padding
    width = height
    x = Header.padding
    y = Header.padding

    selected: bool = False

    def render(self) -> Node:
        font, code = get_icon_info("back", 18)
        ascent = (font.getmetrics() or (0, 0))[0]
        left, _, right, _ = font.getbbox(code)
        icon_y = int((BackButton.height - ascent) / 2)
        icon_x = int((BackButton.width - (right - left)) / 2)

        return Box(
            x=BackButton.x,
            y=BackButton.y,
            w=BackButton.width,
            h=BackButton.height,
            fill=Colors.button.focused.background
            if self.selected
            else Colors.button.background,
            radius=6,
            children=(
                Text(
                    x=icon_x,
                    y=icon_y,
                    text=code,
                    fill=Colors.button.focused.text
                    if self.selected
                    else Colors.button.text,
                    size=18,
                    font=font,
                ),
            ),
        )
