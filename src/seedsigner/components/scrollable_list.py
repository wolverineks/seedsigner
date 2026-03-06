from typing import Callable, List, Any


class ScrollListWindow:
    def __init__(
        self,
        on_blur: Callable,
        visible_count: int,
    ):
        super().__init__()
        self.on_blur = on_blur
        self.visible_count = visible_count
        self.window = (0, visible_count)

    def handle_input(self, selected_index: int):
        if self.start_of_list(selected_index):
            self.on_blur()
            return

        self.sync_window(selected_index)

    def sync_window(self, selected_index: int):
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

    def start_of_list(self, selected_index: int):
        return selected_index < 0

    def focus(self):
        self.window = (0, self.visible_count)


def ScrollList(items: List[Any], window: ScrollListWindow, render_item):
    visible_items = items[window.window[0] : window.window[1]]

    return [render_item(item, index) for index, item in enumerate(visible_items)]
