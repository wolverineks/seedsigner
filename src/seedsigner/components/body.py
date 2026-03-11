from dataclasses import dataclass
from typing import Literal
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

    @staticmethod
    def slot_y(slot: int, height: int = 30) -> int:
        return Body.height - (height + Body.padding) * slot


@dataclass
class Button(Component):
    height = 30
    width = Dimensions.width - Body.padding - Body.padding
    slot: int = 1
    text: str = ""
    focused: bool = False
    type: Literal["standard", "danger"] = "standard"

    def render(self) -> Node:
        size = 24
        font = ImageFont.load_default(size=size)
        ascent = font.getmetrics()[0]

        text_y = round((Button.height - ascent) / 2)
        text_color = (
            "red"
            if self.type == "danger"
            else Colors.button.focused.text
            if self.focused
            else Colors.button.text
        )

        return Box(
            x=Body.padding,
            y=Body.slot_y(self.slot, Button.height),
            w=Button.width,
            h=Button.height,
            fill=Colors.button.focused.background
            if self.focused
            else Colors.button.background,
            radius=10,
            children=(
                Text(
                    x=4,
                    y=text_y,
                    text=self.text,
                    fill=text_color,
                    size=18,
                ),
            ),
        )


@dataclass
class CheckmarkButton(Component):
    height = 30
    width = Dimensions.width - Body.padding - Body.padding
    slot: int = 1

    text: str = ""
    index: int = 0
    focused: bool = False
    checked: bool = False

    def render(self) -> Node:
        size = 24
        font = ImageFont.load_default(size=size)
        ascent = font.getmetrics()[0]

        text_y = round((Button.height - ascent) / 2)

        font, code = get_icon_info("checkmark", 16)
        ascent = font.getmetrics()[0]

        checkmark_y = round((Button.height - ascent) / 2)
        checkmark = Text(
            x=4,
            y=checkmark_y,
            text=code,
            fill="black" if self.focused else "white",
            size=16,
            font=font,
        )

        return Box(
            x=Body.padding,
            y=Body.slot_y(self.slot, CheckmarkButton.height),
            w=Button.width,
            h=Button.height,
            fill=Colors.button.focused.background
            if self.focused
            else Colors.button.background,
            radius=10,
            children=(
                checkmark if self.checked else None,
                Text(
                    x=24,
                    y=text_y,
                    text=self.text,
                    fill=Colors.button.focused.text
                    if self.focused
                    else Colors.button.text,
                    size=18,
                ),
            ),
        )


@dataclass
class CheckboxButton(Component):
    height = 30
    width = Dimensions.width - Body.padding - Body.padding
    slot: int = 1

    text: str = ""
    index: int = 0
    focused: bool = False
    checked: bool = False

    def render(self) -> Node:
        size = 24
        font = ImageFont.load_default(size=size)
        ascent = font.getmetrics()[0]

        text_y = round((Button.height - ascent) / 2)

        font, code = get_icon_info(
            "checkbox-checked" if self.checked else "checkbox-unchecked", 16
        )
        ascent = font.getmetrics()[0]

        fill = "white"
        if self.focused:
            fill = "black"
        if self.checked and not self.focused:
            fill = "green"

        checkbox_y = round((Button.height - ascent) / 2)
        checkbox = Text(
            x=4,
            y=checkbox_y,
            text=code,
            fill=fill,
            size=16,
            font=font,
        )

        return Box(
            x=Body.padding,
            y=Body.slot_y(self.slot, CheckboxButton.height),
            w=Button.width,
            h=Button.height,
            fill=Colors.button.focused.background
            if self.focused
            else Colors.button.background,
            radius=10,
            children=(
                checkbox,
                Text(
                    x=24,
                    y=text_y,
                    text=self.text,
                    fill=Colors.button.focused.text
                    if self.focused
                    else Colors.button.text,
                    size=18,
                ),
            ),
        )


@dataclass
class LargeButton(Component):
    columns = 2
    rows = 2
    width = round((Body.width - 3 * Body.padding) / columns)
    height = round((Body.height - 3 * Body.padding) / rows)

    focused: bool = False
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

        label_x = round(LargeButton.width / 2) - round(width / 2)
        label_y = LargeButton.height - 4 - height

        icon_size = 48
        icon_x = round(LargeButton.width / 2) - round(icon_size / 2)
        icon_y = 4

        return Box(
            x=self.x,
            y=self.y,
            w=LargeButton.width,
            h=LargeButton.height,
            fill=Colors.button.focused.background
            if self.focused
            else Colors.button.background,
            radius=10,
            children=(
                LargeButton.Icon(
                    x=icon_x,
                    y=icon_y,
                    icon=self.icon,
                    size=icon_size,
                    focused=self.focused,
                ),
                LargeButton.Label(
                    text=self.label,
                    x=label_x,
                    y=label_y,
                    focused=self.focused,
                ),
            ),
        )

    @staticmethod
    def Icon(
        x: int,
        y: int,
        icon: str,
        focused: bool,
        size: int,
    ):
        font, code = get_icon_info(icon=icon, size=size)

        return Text(
            x=x,
            y=y,
            text=code,
            fill="black" if focused else "white",
            size=size,
            font=font,
        )

    @staticmethod
    def Label(x: int, y: int, focused: bool, text: str) -> Node:
        return Text(
            x=x,
            y=y,
            text=text,
            fill=Colors.button.focused.text if focused else Colors.button.text,
            size=24,
        )
