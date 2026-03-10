from typing import Callable, Sequence, TypeVar

from seedsigner.components.body import Body
from seedsigner.dimensions import Dimensions
from seedsigner.loopyUI import Node, Text
from .helpers import get_icon_info


T = TypeVar("T")


class ScrollListWindow:
    def __init__(
        self,
        visible_count: int,
    ):
        super().__init__()
        self.visible_count = visible_count
        self.window = (0, visible_count)

    def update(self, focused_index: int | None = None):
        if focused_index is None:
            return

        if focused_index <= self.window[0]:
            self.window = (
                focused_index,
                focused_index + self.visible_count,
            )
        elif focused_index >= self.window[1]:
            self.window = (
                focused_index - self.visible_count + 1,
                focused_index + 1,
            )


up_arrow_font, up_arrow_code = get_icon_info("up_arrow", 32)
up_arrow_bbox = up_arrow_font.getbbox(up_arrow_code)
down_arrow_font, down_arrow_code = get_icon_info("down_arrow", 32)
down_arrow_bbox = down_arrow_font.getbbox(down_arrow_code)


UpArrow = {
    "font": up_arrow_font,
    "code": up_arrow_code,
    "bbox": up_arrow_bbox,
    "width": up_arrow_bbox[2] - up_arrow_bbox[0],
    "height": up_arrow_bbox[3] - up_arrow_bbox[1],
}

DownArrow = {
    "font": down_arrow_font,
    "code": down_arrow_code,
    "bbox": down_arrow_bbox,
    "width": down_arrow_bbox[2] - down_arrow_bbox[0],
    "height": down_arrow_bbox[3] - down_arrow_bbox[1],
}


def ScrollList(
    items: Sequence[T],
    window: ScrollListWindow,
    render_item: Callable[[T, int], Node],
    spacing: int = 8,
) -> list[Node]:
    visible_items = items[window.window[0] : window.window[1]]
    up_arrow_icon = Text(
        text=UpArrow["code"],
        x=round((Dimensions.width - UpArrow["width"]) / 2) - Body.padding,
        y=-UpArrow["height"] + 4,
        font=UpArrow["font"],
    )
    down_arrow_icon = Text(
        text=DownArrow["code"],
        x=round((Dimensions.width - DownArrow["width"]) / 2) - Body.padding,
        y=Body.height - DownArrow["height"] - 4 - Body.padding,
        font=DownArrow["font"],
    )

    return [
        [render_item(item, index) for index, item in enumerate(visible_items)],
        up_arrow_icon if window.window[0] > 0 else None,
        down_arrow_icon if window.window[1] < len(items) else None,
    ]
