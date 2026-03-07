from typing import Callable, Sequence, TypeVar

from seedsigner.loopyUI import Node


T = TypeVar("T")


class ScrollListWindow:
    def __init__(
        self,
        visible_count: int,
    ):
        super().__init__()
        self.visible_count = visible_count
        self.window = (0, visible_count)

    def update(self, selected_index: int | None = None):
        if selected_index is None:
            return

        if selected_index <= self.window[0]:
            self.window = (
                selected_index,
                selected_index + self.visible_count,
            )
        elif selected_index >= self.window[1]:
            self.window = (
                selected_index - self.visible_count + 1,
                selected_index + 1,
            )


def ScrollList(
    items: Sequence[T],
    window: ScrollListWindow,
    render_item: Callable[[T, int], Node],
) -> list[Node]:
    visible_items = items[window.window[0] : window.window[1]]

    return [render_item(item, index) for index, item in enumerate(visible_items)]
