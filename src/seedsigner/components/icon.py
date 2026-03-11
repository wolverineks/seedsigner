from seedsigner.loopyUI import Text

from .helpers import get_icon_info, Code


def Icon(icon: Code, x: int, y: int, size: int):
    font, code = get_icon_info(icon, size)

    return Text(
        text=code,
        x=x,
        y=y,
        font=font,
        anchor="mb",
    )
