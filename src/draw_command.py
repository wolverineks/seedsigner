from typing import Literal
from dataclasses import dataclass

@dataclass(frozen=True)
class Rect:
    type: Literal["rect"] = "rect"
    x: int = 0
    y: int = 0
    w: int = 240
    h: int = 240
    fill: str = "black"
    outline: str | None = None
    width: int = 1
    radius: int = 0


@dataclass(frozen=True)
class Text:
    type: Literal["text"] = "text"
    x: int = 0
    y: int = 0
    text: str = ""
    fill: str = "white"
    size: int = 16
    font: str = "regular"