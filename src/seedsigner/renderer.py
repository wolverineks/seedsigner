from typing import Any
from PIL import Image, ImageDraw

from draw_command import Rect, Text
from hardware import Platform


def render(component) -> Image.Image:
    canvas: Image.Image = Image.new(
        "RGB", (Platform.screen_width, Platform.screen_height), "white"
    )
    draw: ImageDraw.ImageDraw = ImageDraw.Draw(canvas)

    def recurse(node: Any) -> None:
        # print("node", node)
        if isinstance(node, list):
            for child in node:
                recurse(child)
        elif hasattr(node, "render") and callable(getattr(node, "render")):
            recurse(node.render())
        elif isinstance(node, Rect):
            draw.rounded_rectangle(
                (
                    node.x,
                    node.y,
                    node.x + node.w,
                    node.y + node.h,
                ),
                fill=node.fill,
                radius=node.radius if hasattr(node, "radius") else 0,
            )
        elif isinstance(node, Text):
            draw.text(
                (node.x, node.y),
                node.text,
                fill=node.fill,
            )
        elif node is None:
            pass
        else:
            print("unrecognized node", node)
            raise

    recurse(component)
    return canvas
