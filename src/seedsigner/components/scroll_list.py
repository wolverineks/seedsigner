from typing import Callable, Sequence, TypeVar

from seedsigner.dimensions import Dimensions
from seedsigner.loopyUI import Node
from .body import Body
from .icon import Icon


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


def ScrollList(
    items: Sequence[T],
    window: ScrollListWindow,
    render_item: Callable[[T, int], Node],
) -> list[Node]:
    visible_items = items[window.window[0] : window.window[1]]
    up_arrow_icon = Icon(
        icon="up_arrow",
        x=round(Dimensions.width / 2),
        y=16,
        size=32,
    )
    down_arrow_icon = Icon(
        icon="down_arrow",
        x=round(Dimensions.width / 2),
        y=Body.height + 8,
        size=32,
    )

    return [
        [render_item(item, index) for index, item in enumerate(visible_items)],
        up_arrow_icon if window.window[0] > 0 else None,
        down_arrow_icon if window.window[1] < len(items) else None,
    ]