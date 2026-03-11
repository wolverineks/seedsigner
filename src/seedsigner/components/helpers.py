from PIL import ImageFont
from typing import Tuple, Literal


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
        "up_arrow": (
            seedsigner_icons_path,
            "\ue90e",
        ),
        "down_arrow": (
            seedsigner_icons_path,
            "\ue90d",
        ),
    }

    code = icon_codes.get(icon)
    if code is None:
        raise ValueError(f"Unknown icon: {icon}")

    return ImageFont.truetype(code[0], size), code[1]
Code = Literal[
    "scan",
    "seeds",
    "gear",
    "tools",
    "back",
    "power",
    "restart",
    "checkmark",
    "checkbox-checked",
    "checkbox-unchecked",
    "sdcard",
    "up_arrow",
    "down_arrow",
]
