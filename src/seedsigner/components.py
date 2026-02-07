from dataclasses import dataclass
from typing import Any, List

from seedsigner.draw_command import Rect, Text, DrawCommand
from seedsigner.dimensions import Dimensions
from seedsigner.colors import Colors


@dataclass
class Header:
    height = 40
    padding = 8

    title: str
    left: Any = None
    right: Any = None

    def render(self):
        bg = Rect(
            x=0,
            y=0,
            w=Dimensions.width,
            h=Header.height,
            fill=Colors.background,
        )

        return [
            bg,
            self.left,
            Text(x=60, y=10, text=self.title, fill=Colors.text, size=20),
            self.right,
        ]


button_padding = 4


@dataclass
class BackButton:
    height = Header.height - Header.padding - Header.padding
    width = height
    x = Header.padding
    y = Header.padding

    selected: bool = False

    def render(self):
        ascent = font.getmetrics()[0]

        text_y = BackButton.y + int((BackButton.height - ascent) / 2)

        return [
            Rect(
                x=BackButton.x,
                y=BackButton.y,
                w=BackButton.width,
                h=BackButton.height,
                fill=Colors.button.focused.background
                if self.selected
                else Colors.button.background,
                radius=6,
            ),
            Text(
                x=Header.padding + button_padding,
                y=text_y,
                text="<",
                fill=Colors.button.focused.text
                if self.selected
                else Colors.button.text,
                size=18,
            ),
        ]


@dataclass
class PowerButton:
    height = Header.height - Header.padding - Header.padding
    width = height
    x = Dimensions.width - Header.padding - width
    y = Header.padding

    selected: bool = False

    def render(self):
        return [
            Rect(
                x=PowerButton.x,
                y=PowerButton.y,
                w=PowerButton.width,
                h=PowerButton.height,
                fill=Colors.button.focused.background
                if self.selected
                else Colors.button.background,
                radius=6,
            ),
            Text(
                x=PowerButton.x + button_padding,
                y=PowerButton.y + button_padding,
                text="P",
                fill=Colors.button.focused.text
                if self.selected
                else Colors.button.text,
                size=18,
            ),
        ]


@dataclass(init=False)
class Body:
    padding = 8
    x = 0
    y = Header.height
    width = Dimensions.width
    height = Dimensions.height - Header.height
    bg = Rect(
        x=x,
        y=y,
        w=width,
        h=height,
        fill=Colors.background,
    )

    def __init__(self, *children: List[DrawCommand]):
        self.children = children

    def render(self) -> List[DrawCommand]:
        return [Body.bg, *self.children]


@dataclass
class Grid:
    columns = 2
    rows = 2
    width = int(
        (Dimensions.width - Body.padding - Body.padding - Body.padding) / columns
    )
    height = int((Dimensions.height - Header.height - 3 * Body.padding) / rows)

    top = Header.height + Body.padding
    bottom = top + height + Body.padding
    left = Body.padding
    right = Body.padding + width + Body.padding


from PIL import ImageFont

size = 24
font = ImageFont.load_default(size=size)


@dataclass
class Button:
    height = 30
    width = Dimensions.width - Body.padding - Body.padding
    x = Body.padding

    text: str
    index: int
    selected: bool

    def render(self) -> List[DrawCommand | None]:
        button_y = (
            Header.height + Body.padding + self.index * (Button.height + Body.padding)
        )
        ascent = font.getmetrics()[0]

        text_y = button_y + int((Button.height - ascent) / 2)

        return [
            Rect(
                x=Button.x,
                y=button_y,
                w=Button.width,
                h=Button.height,
                fill="orange" if self.selected else "gray",
                radius=10,
            ),
            None,
            Text(
                x=Button.x + button_padding,
                y=text_y,
                text=self.text,
                fill=Colors.button.focused.text
                if self.selected
                else Colors.button.text,
                size=18,
            ),
        ]


@dataclass
class LargeButton:
    columns = 2
    rows = 2
    width = int((Dimensions.width - 3 * (Body.padding)) / columns)
    height = int((Dimensions.height - Header.height - 3 * Body.padding) / rows)

    text: str
    x: int
    y: int
    selected: bool

    def render(self) -> List[DrawCommand]:
        left, _, right, _ = font.getbbox(self.text)
        width = right - left
        ascent, descent = font.getmetrics()
        height = ascent + descent

        centered = self.x + int(LargeButton.width / 2) - int(width / 2)
        bottom = self.y + LargeButton.height - height - button_padding

        return [
            Rect(
                x=self.x,
                y=self.y,
                w=LargeButton.width,
                h=LargeButton.height,
                fill=Colors.button.focused.background
                if self.selected
                else Colors.button.background,
                radius=10,
            ),
            Text(
                x=centered,
                y=bottom,
                text=self.text,
                fill=Colors.button.focused.text
                if self.selected
                else Colors.button.text,
                size=size,
            ),
        ]
