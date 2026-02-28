from typing import Any
from PIL import Image, ImageDraw

from seedsigner.loopyUI import Rect, Text
from seedsigner.dimensions import Dimensions
from seedsigner.loopyUI.component import Component


def render(component: Component) -> Image.Image:
    canvas: Image.Image = Image.new(
        "RGB", (Dimensions.width, Dimensions.height), "white"
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
                outline=node.outline,
                width=node.width,
            )
        elif isinstance(node, Text):
            draw.text(
                (node.x, node.y),
                node.text,
                fill=node.fill,
                font_size=node.size,
                font=node.font,
            )
        elif node is None:
            pass
        else:
            print("unrecognized node", node)
            raise

    recurse(component)
    return canvas
