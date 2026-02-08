from dataclasses import dataclass


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
        ascent = (font.getmetrics() or (0, 0))[0]

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
class PowerButton(Component):
    height = Header.height - Header.padding - Header.padding
    width = height
    x = Dimensions.width - Header.padding - width
    y = Header.padding

    selected: bool = False

    def render(self) -> Node:
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

    def __init__(self, *children):
        self.children = children

    def render(self) -> Node:
        return [Body.bg, *self.children]


from PIL import ImageFont

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
class LargeButton(Component):
    columns = 2
    rows = 2
    width = int((Dimensions.width - 3 * (Body.padding)) / columns)
    height = int((Dimensions.height - Header.height - 3 * Body.padding) / rows)

    text: str
    x: int
    y: int
    selected: bool
    icon: str = ""

    def render(self) -> Node:
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
            Icon(x=centered, y=self.y) if self.icon else None,
        ]


@dataclass()
class Icon(Component):
    x: int
    y: int
    # text: str
    # color: str | None
    # size: int | None
    # font: str

    def render(self) -> Node:
        font = ImageFont.truetype(
            "./src/seedsigner/resources/fonts/seedsigner-icons.otf",
            64,
            # "./src/seedsigner/resources/fonts/Font_Awesome_6_Free-Solid-900.otf",
            # 32,
        )

        return Text(
            x=self.x,
            y=self.y,
            text="\ue902",
            fill="white",
            size=64,
            font=font,
        )
