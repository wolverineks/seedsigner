from dataclasses import dataclass

from PIL import ImageFont

from seedsigner.components.header import Header
from seedsigner.loopyUI import Component, Node, Box, Text
from seedsigner.dimensions import Dimensions
from seedsigner.colors import Colors
from .helpers import get_icon_info


@dataclass(init=False)
class Body(Component):
    padding = 8
    x = 0
    y = Header.height
    width = Dimensions.width
    height = Dimensions.height - Header.height

    def __init__(self, *children: Node):
        self.children = children

    def render(self) -> Node:
        return Box(
            x=Body.x,
            y=Body.y,
            w=Body.width,
            h=Body.height,
            padding=Body.padding,
            fill=Colors.background,
            children=self.children,
        )


@dataclass
class Button(Component):
    height = 30
    width = Dimensions.width - Body.padding - Body.padding
    x: int = 0
    y: int = 0
    text: str = ""
    selected: bool = False

    def render(self) -> Node:
        size = 24
        font = ImageFont.load_default(size=size)
        ascent = font.getmetrics()[0]

        text_y = int((Button.height - ascent) / 2)

        return Box(
            x=self.x,
            y=self.y,
            w=Button.width,
            h=Button.height,
            fill=Colors.button.focused.background
            if self.selected
            else Colors.button.background,
            radius=10,
            children=(
                Text(
                    x=4,
                    y=text_y,
                    text=self.text,
                    fill=Colors.button.focused.text
                    if self.selected
                    else Colors.button.text,
                    size=18,
                ),
            ),
        )


@dataclass
class CheckmarkButton(Component):
    height = 30
    width = Dimensions.width - Body.padding - Body.padding
    x: int = 0
    y: int = 0

    text: str = ""
    index: int = 0
    selected: bool = False
    checked: bool = False

    def render(self) -> Node:
        size = 24
        font = ImageFont.load_default(size=size)
        button_y = self.y + self.index * (Button.height + Body.padding)
        ascent = font.getmetrics()[0]

        text_y = int((Button.height - ascent) / 2)

        font, code = get_icon_info("checkmark", 16)
        ascent = font.getmetrics()[0]

        checkmark_y = int((Button.height - ascent) / 2)
        checkmark = Text(
            x=4,
            y=checkmark_y,
            text=code,
            fill="black" if self.selected else "white",
            size=16,
            font=font,
        )

        return Box(
            x=self.x,
            y=button_y,
            w=Button.width,
            h=Button.height,
            fill=Colors.button.focused.background
            if self.selected
            else Colors.button.background,
            radius=10,
            children=(
                checkmark if self.checked else None,
                Text(
                    x=24,
                    y=text_y,
                    text=self.text,
                    fill=Colors.button.focused.text
                    if self.selected
                    else Colors.button.text,
                    size=18,
                ),
            ),
        )


@dataclass
class CheckboxButton(Component):
    height = 30
    width = Dimensions.width - Body.padding - Body.padding
    x: int = 0
    y: int = 0

    text: str = ""
    index: int = 0
    selected: bool = False
    checked: bool = False

    def render(self) -> Node:
        size = 24
        font = ImageFont.load_default(size=size)
        button_y = self.y + self.index * (Button.height + Body.padding)
        ascent = font.getmetrics()[0]

        text_y = int((Button.height - ascent) / 2)

        font, code = get_icon_info(
            "checkbox-checked" if self.checked else "checkbox-unchecked", 16
        )
        ascent = font.getmetrics()[0]

        fill = "white"
        if self.selected:
            fill = "black"
        if self.checked and not self.selected:
            fill = "green"

        checkbox_y = int((Button.height - ascent) / 2)
        checkbox = Text(
            x=4,
            y=checkbox_y,
            text=code,
            fill=fill,
            size=16,
            font=font,
        )

        return Box(
            x=self.x,
            y=button_y,
            w=Button.width,
            h=Button.height,
            fill=Colors.button.focused.background
            if self.selected
            else Colors.button.background,
            radius=10,
            children=(
                checkbox,
                Text(
                    x=24,
                    y=text_y,
                    text=self.text,
                    fill=Colors.button.focused.text
                    if self.selected
                    else Colors.button.text,
                    size=18,
                ),
            ),
        )


@dataclass
class LargeButton(Component):
    columns = 2
    rows = 2
    width = int((Body.width - 3 * Body.padding) / columns)
    height = int((Body.height - 3 * Body.padding) / rows)

    selected: bool = False
    icon: str = ""
    label: str = ""

    x: int = 0
    y: int = 0

    def render(self) -> Node:
        size = 24
        font = ImageFont.load_default(size=size)
        left, _, right, _ = font.getbbox(self.label)
        width = right - left
        ascent, descent = font.getmetrics()
        height = ascent + descent

        label_x = int(LargeButton.width / 2) - int(width / 2)
        label_y = LargeButton.height - 4 - height

        icon_size = 48
        icon_x = int(LargeButton.width / 2) - int(icon_size / 2)
        icon_y = 4

        return Box(
            x=self.x,
            y=self.y,
            w=LargeButton.width,
            h=LargeButton.height,
            fill=Colors.button.focused.background
            if self.selected
            else Colors.button.background,
            radius=10,
            children=(
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
            ),
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
