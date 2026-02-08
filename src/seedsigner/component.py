from dataclasses import dataclass
from typing import Union, List, TypeAlias, Literal, Any

DrawPrimitive: TypeAlias = Union["Rect", "Text"]
Node: TypeAlias = Union[DrawPrimitive, "Component", None, List["Node"]]


class Component:
    def handle_input(self, input: Any) -> Any:
        pass

    def render(self) -> Node:
        raise NotImplementedError("Subclasses must implement render")


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
    fill: str | None = "white"
    size: int | None = 16
    font: Any | None = None
