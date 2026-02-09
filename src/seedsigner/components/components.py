from dataclasses import dataclass
from PIL import ImageFont
from typing import Tuple

from seedsigner.loopyUI import Component, Rect, Text, Node
from seedsigner.dimensions import Dimensions
from seedsigner.colors import Colors


@dataclass
class Header(Component):
    height = 40
    padding = 8

    title: str
    left: Component | None = None
    right: Component | None = None

    def render(self) -> Node:
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
class BackButton(Component):
    height = Header.height - Header.padding - Header.padding
    width = height
    x = Header.padding
    y = Header.padding

    selected: bool = False

    def render(self) -> Node:
        font, code = get_icon_info("back", 18)
        ascent = (font.getmetrics() or (0, 0))[0]
        icon_y = BackButton.y + int((BackButton.height - ascent) / 2)

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
                x=BackButton.x + 2,
                y=icon_y,
                text=code,
                fill=Colors.button.focused.text
                if self.selected
                else Colors.button.text,
                size=18,
                font=font,
            ),
        ]


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
        icon_y = PowerButton.y + int((PowerButton.height - ascent) / 2)

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
                y=icon_y,
                text=code,
                fill=Colors.button.focused.text
                if self.selected
                else Colors.button.text,
                size=18,
                font=font,
            ),
        ]


@dataclass(init=False)
class Body(Component):
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

    def __init__(self, *children: Node):
        self.children = children

    def render(self) -> Node:
        return [Body.bg, *self.children]


size = 24
font = ImageFont.load_default(size=size)


@dataclass
class Button(Component):
    height = 30
    width = Dimensions.width - Body.padding - Body.padding
    x = Body.padding

    text: str
    index: int
    selected: bool

    def render(self) -> Node:
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
                fill=Colors.button.focused.background
                if self.selected
                else Colors.button.background,
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
class LargeButton(Component):
    columns = 2
    rows = 2
    width = int((Body.width - 3 * Body.padding) / columns)
    height = int((Body.height - 3 * Body.padding) / rows)

    x: int
    y: int
    selected: bool
    icon: str
    label: str

    def render(self) -> Node:
        size = 24
        font = ImageFont.load_default(size=size)
        left, _, right, _ = font.getbbox(self.label)
        width = right - left
        ascent, descent = font.getmetrics()
        height = ascent + descent

        label_x = self.x + int(LargeButton.width / 2) - int(width / 2)
        label_y = self.y + LargeButton.height - button_padding - height

        icon_size = 48
        icon_x = self.x + int(LargeButton.width / 2) - int(icon_size / 2)
        icon_y = self.y + 4

        return [
            LargeButton.Bg(
                x=self.x,
                y=self.y,
                selected=self.selected,
            ),
            LargeButton.Icon(
                x=icon_x,
                y=icon_y,
                icon=self.icon,
                size=icon_size,
                selected=self.selected,
            ),
            LargeButton.Label(
                text=self.label,
                x=label_x,
                y=label_y,
                selected=self.selected,
            ),
        ]

    @staticmethod
    def Bg(x: int, y: int, selected: bool) -> Node:
        return Rect(
            x=x,
            y=y,
            w=LargeButton.width,
            h=LargeButton.height,
            fill=Colors.button.focused.background
            if selected
            else Colors.button.background,
            radius=10,
        )

    @staticmethod
    def Icon(
        x: int,
        y: int,
        icon: str,
        selected: bool,
        size: int,
    ):
        font, code = get_icon_info(icon=icon, size=size)

        return Text(
            x=x,
            y=y,
            text=code,
            fill="black" if selected else "white",
            size=size,
            font=font,
        )

    @staticmethod
    def Label(x: int, y: int, selected: bool, text: str) -> Node:
        return Text(
            x=x,
            y=y,
            text=text,
            fill=Colors.button.focused.text if selected else Colors.button.text,
            size=24,
        )


def get_icon_info(icon: str, size: int) -> Tuple[ImageFont.FreeTypeFont, str]:
    font = ImageFont.truetype(
        "./src/seedsigner/resources/fonts/seedsigner-icons.otf", size
    )

    icon_codes = {
        "scan": "\ue900",
        "seeds": "\ue901",
        "gear": "\ue902",
        "tools": "\ue903",
        "back": "\ue904",
        "power": "\ue910",
        "restart": "\ue911",
    }

    code = icon_codes.get(icon)
    if code is None:
        raise ValueError(f"Unknown icon: {icon}")

    return font, code
