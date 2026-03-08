from typing import Any
from PIL import Image, ImageDraw

from seedsigner.dimensions import Dimensions

from .component import Rect, Text, Group, Box, Component

canvas = Image.new("RGB", (Dimensions.width, Dimensions.height), "white")


def render(component: Component, canvas: Image.Image = canvas) -> Image.Image:
    draw: ImageDraw.ImageDraw = ImageDraw.Draw(canvas)

    def recurse(node: Any, offset_x: int = 0, offset_y: int = 0) -> None:
        if isinstance(node, (list, tuple)):
            for child in node:
                recurse(child, offset_x, offset_y)
        elif hasattr(node, "render") and callable(getattr(node, "render")):
            recurse(node.render(), offset_x, offset_y)
        elif isinstance(node, Group):
            group_offset_x = offset_x + node.x
            group_offset_y = offset_y + node.y
            recurse(node.children, group_offset_x, group_offset_y)
        elif isinstance(node, Box):
            box_offset_x = offset_x + node.x
            box_offset_y = offset_y + node.y
            draw.rounded_rectangle(
                (
                    box_offset_x,
                    box_offset_y,
                    box_offset_x + node.w,
                    box_offset_y + node.h,
                ),
                fill=node.fill,
                radius=node.radius if hasattr(node, "radius") else 0,
                outline=node.outline,
                width=node.width,
            )
            recurse(
                node.children,
                box_offset_x + node.padding,
                box_offset_y + node.padding,
            )
        elif isinstance(node, Rect):
            draw.rounded_rectangle(
                (
                    node.x + offset_x,
                    node.y + offset_y,
                    node.x + offset_x + node.w,
                    node.y + offset_y + node.h,
                ),
                fill=node.fill,
                radius=node.radius if hasattr(node, "radius") else 0,
                outline=node.outline,
                width=node.width,
            )
        elif isinstance(node, Text):
            draw.text(
                (node.x + offset_x, node.y + offset_y),
                node.text,
                fill=node.fill,
                font_size=node.size,
                font=node.font,
            )
        elif node is None:
            pass
        else:
            raise ValueError(f"unrecognized node: {node}")

    recurse(component)
    return canvas
