from dataclasses import dataclass
from PIL import ImageFont
from typing import Tuple

from seedsigner.loopyUI import Component, Rect, Text, Node
from seedsigner.dimensions import Dimensions
from seedsigner.colors import Colors
from .helpers import _offset_node


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
            Text(x=text_x, y=10, text=self.title, fill=Colors.text, size=size),
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
        offset_x = Body.x + Body.padding
        offset_y = Body.y + Body.padding
        relative_children = [
            _offset_node(child, offset_x, offset_y) for child in self.children
        ]
        return [Body.bg, *relative_children]


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

        text_y = self.y + int((Button.height - ascent) / 2)

        return [
            Rect(
                x=self.x,
                y=self.y,
                w=Button.width,
                h=Button.height,
                fill=Colors.button.focused.background
                if self.selected
                else Colors.button.background,
                radius=10,
            ),
            None,
            Text(
                x=self.x + button_padding,
                y=text_y,
                text=self.text,
                fill=Colors.button.focused.text
                if self.selected
                else Colors.button.text,
                size=18,
            ),
        ]


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

        text_y = button_y + int((Button.height - ascent) / 2)

        font, code = get_icon_info("checkmark", 16)
        ascent = font.getmetrics()[0]

        checkmark_y = button_y + int((Button.height - ascent) / 2)
        checkmark = Text(
            x=self.x + button_padding,
            y=checkmark_y,
            text=code,
            fill="black" if self.selected else "white",
            size=16,
            font=font,
        )

        return [
            Rect(
                x=self.x,
                y=button_y,
                w=Button.width,
                h=Button.height,
                fill=Colors.button.focused.background
                if self.selected
                else Colors.button.background,
                radius=10,
            ),
            checkmark if self.checked else None,
            Text(
                x=self.x + button_padding + 24,
                y=text_y,
                text=self.text,
                fill=Colors.button.focused.text
                if self.selected
                else Colors.button.text,
                size=18,
            ),
        ]


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

        text_y = button_y + int((Button.height - ascent) / 2)

        font, code = get_icon_info(
            "checkbox-checked" if self.checked else "checkbox-unchecked", 16
        )
        ascent = font.getmetrics()[0]

        fill = "white"
        if self.selected:
            fill = "black"
        if self.checked and not self.selected:
            fill = "green"

        checkbox_y = button_y + int((Button.height - ascent) / 2)
        checkbox = Text(
            x=self.x + button_padding,
            y=checkbox_y,
            text=code,
            fill=fill,
            size=16,
            font=font,
        )

        return [
            Rect(
                x=self.x,
                y=button_y,
                w=Button.width,
                h=Button.height,
                fill=Colors.button.focused.background
                if self.selected
                else Colors.button.background,
                radius=10,
            ),
            checkbox,
            Text(
                x=self.x + button_padding + 24,
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

    x: int = 0
    y: int = 0
    selected: bool = False
    icon: str = ""
    label: str = ""

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
    fonts_path = "./src/seedsigner/resources/fonts/"
    seedsigner_icons_path = f"{fonts_path}seedsigner-icons.otf"
    font_awesome_path = f"{fonts_path}Font_Awesome_6_Free-Solid-900.otf"

    icon_codes = {
        "scan": (
            seedsigner_icons_path,
            "\ue900",
        ),
        "seeds": (
            seedsigner_icons_path,
            "\ue901",
        ),
        "gear": (
            seedsigner_icons_path,
            "\ue902",
        ),
        "tools": (
            seedsigner_icons_path,
            "\ue903",
        ),
        "back": (
            seedsigner_icons_path,
            "\ue904",
        ),
        "power": (
            seedsigner_icons_path,
            "\ue910",
        ),
        "restart": (
            seedsigner_icons_path,
            "\ue911",
        ),
        "checkmark": (
            font_awesome_path,
            "\uf00c",
        ),
        "checkbox-checked": (
            seedsigner_icons_path,
            "\ue907",
        ),
        "checkbox-unchecked": (
            seedsigner_icons_path,
            "\ue906",
        ),
        "sdcard": (
            seedsigner_icons_path,
            "\ue91f",
        ),
    }

    code = icon_codes.get(icon)
    if code is None:
        raise ValueError(f"Unknown icon: {icon}")

    return ImageFont.truetype(code[0], size), code[1]
