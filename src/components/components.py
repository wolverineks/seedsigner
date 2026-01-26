from dataclasses import dataclass
from typing import Any

from draw_command import Rect, Text
from hardware import Platform


@dataclass(frozen=True)
class Header:
    height = 40
    padding = 8

    title: str
    left: Any = None
    right: Any = None

    def render(self):
        bg = Rect(x=0, y=0, w=Platform.screen_width, h=Header.height, fill="blue")

        return [
            bg,
            self.left,
            Text(x=60, y=10, text=self.title, fill="white", size=20),
            self.right,
        ]


button_padding = 4


@dataclass(frozen=True)
class BackButton:
    height = Header.height - Header.padding - Header.padding
    width = height
    x = Header.padding
    y = Header.padding

    selected: bool = False

    def render(self):
        return [
            Rect(
                x=BackButton.x,
                y=BackButton.y,
                w=BackButton.width,
                h=BackButton.height,
                fill="green" if self.selected else "red",
                radius=6,
            ),
            Text(
                x=Header.padding + button_padding,
                y=Header.padding + button_padding,
                text="<",
                fill="white",
                size=18,
            ),
        ]


@dataclass(frozen=True)
class PowerButton:
    height = Header.height - Header.padding - Header.padding
    width = height
    x = Platform.screen_width - Header.padding - width
    y = Header.padding

    selected: bool = False

    def render(self):
        return [
            Rect(
                x=PowerButton.x,
                y=PowerButton.y,
                w=PowerButton.width,
                h=PowerButton.height,
                fill="green" if self.selected else "red",
                radius=6,
            ),
            Text(
                x=PowerButton.x + button_padding,
                y=PowerButton.y + button_padding,
                text="P",
                fill="white",
                size=18,
            ),
        ]


@dataclass(init=False)
class Body:
    padding = 8
    x = 0
    y = Header.height
    width = Platform.screen_width
    height = Platform.screen_height - Header.height
    bg = Rect(
        x=x,
        y=y,
        w=width,
        h=height,
        fill="lightgray",
    )

    def __init__(self, *children):
        self.children = children

    def render(self):
        return [Body.bg, *self.children]


@dataclass(frozen=True)
class Grid:
    columns = 2
    rows = 2
    width = int(
        (Platform.screen_width - Body.padding - Body.padding - Body.padding) / columns
    )
    height = int((Platform.screen_height - Header.height - 3 * Body.padding) / rows)

    top = Header.height + Body.padding
    bottom = top + height + Body.padding
    left = Body.padding
    right = Body.padding + width + Body.padding


@dataclass(frozen=True)
class Button:
    height = 40
    width = Platform.screen_width - Body.padding - Body.padding
    x = Body.padding

    text: str
    index: int
    selected: bool

    def render(self):
        y = Header.height + Body.padding + self.index * (Button.height + Body.padding)

        return [
            Rect(
                x=Button.x,
                y=y,
                w=Button.width,
                h=Button.height,
                fill="green" if self.selected else "red",
                radius=10,
            ),
            Text(
                x=Button.x + button_padding,
                y=y,
                text=self.text,
                fill="white",
                size=18,
            ),
        ]


@dataclass(frozen=True)
class LargeButton:
    columns = 2
    rows = 2
    width = int((Platform.screen_width - 3 * (Body.padding)) / columns)
    height = int((Platform.screen_height - Header.height - 3 * Body.padding) / rows)

    text: str
    x: int
    y: int
    selected: bool

    def render(self):
        return [
            Rect(
                x=self.x,
                y=self.y,
                w=LargeButton.width,
                h=LargeButton.height,
                fill="green" if self.selected else "red",
                radius=10,
            ),
            Text(
                x=self.x + button_padding,
                y=self.y + button_padding,
                text=self.text,
                fill="white",
                size=18,
            ),
        ]
