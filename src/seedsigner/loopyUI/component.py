from dataclasses import dataclass
from functools import wraps
from typing import Union, List, TypeAlias, Literal, Any


DrawPrimitive: TypeAlias = Union["Rect", "Text"]
Node: TypeAlias = Union[
    DrawPrimitive,
    "Group",
    "Box",
    "Component",
    None,
    List["Node"],
    tuple["Node", ...],
]


class Component:
    def __init__(self) -> None:
        self.state: Any = None
        self.dirty: bool = True
        self.focused: Any = None

    # hack to avoid having to set dirty = False in every render method
    def __init_subclass__(cls: type["Component"], **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)

        render_method = cls.__dict__.get("render")
        if render_method is None:
            return

        if getattr(render_method, "__component_render_wrapped__", False):
            return

        @wraps(render_method)
        def wrapped_render(self: "Component", *args: Any, **kwargs: Any) -> Any:
            node = render_method(self, *args, **kwargs)
            self.dirty = False
            return node

        setattr(wrapped_render, "__component_render_wrapped__", True)
        cls.render = wrapped_render

    def set_focused(self, focused: Any) -> None:
        self.focused = focused
        self.dirty = True

    def handle_input(self, input: Any) -> Any:
        pass

    def handle_on_focus(self) -> Any:
        pass

    def handle_on_blur(self) -> Any:
        pass

    def handle_on_mount(self) -> Any:
        pass

    def handle_on_unmount(self) -> Any:
        pass

    def has_changed(self) -> bool:
        return self.dirty

    def hasnt_changed(self) -> bool:
        return not self.has_changed()

    def render(self) -> None | Node | List[Node]:
        self.dirty = False
        return None


@dataclass(frozen=True)
class Rect:
    type: Literal["rect"] = "rect"
    x: int = 0
    y: int = 0
    w: int = 240
    h: int = 240
    fill: str = "black"
    outline: str | None = None
    width: int = 0
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


@dataclass(frozen=True)
class Group:
    type: Literal["group"] = "group"
    x: int = 0
    y: int = 0
    children: tuple[Node, ...] = ()


@dataclass(frozen=True)
class Box:
    type: Literal["box"] = "box"
    x: int = 0
    y: int = 0
    w: int = 240
    h: int = 240
    padding: int = 0
    fill: str = "black"
    outline: str | None = None
    width: int = 0
    radius: int = 0
    children: tuple[Node, ...] = ()
