from typing import Any, Literal

from seedsigner.components.components import Button


class ScrollableListWindow:
    def __init__(self, on_blur: Any, item_count: int, visible_count: int):
        self.visible_count = visible_count
        self.on_blur = on_blur
        self.item_count = item_count

        self.selected_index = 0
        self.window = (0, visible_count - 1)

    def handle_input(self, input: Literal["up", "down", "left"]):
        match input:
            case "left":
                self.on_blur()
                return

            case "up":
                if self.start_of_list():
                    self.on_blur()
                    return

                if self.start_of_window():
                    self.move_window_up()

                self.selected_index -= 1

            case "down":
                if self.end_of_list():
                    return

                if self.end_of_window():
                    self.move_window_down()

                self.selected_index += 1

    def move_window_up(self):
        self.window = (
            self.window[0] - 1,
            self.window[1] - 1,
        )

    def move_window_down(self):
        self.window = (
            self.window[0] + 1,
            self.window[1] + 1,
        )

    def start_of_list(self):
        return self.selected_index == 0

    def end_of_list(self):
        return self.selected_index == self.item_count - 1

    def start_of_window(self):
        return self.selected_index == self.window[0]

    def end_of_window(self):
        return self.selected_index == self.window[1]

    def reset(self):
        self.selected_index = 0
        self.window = (0, self.visible_count - 1)


def ScrollableList(window: ScrollableListWindow, items: list[Any]):
    visible_items = items[window.window[0] : window.window[1] + 1]

    return [
        Button(
            text=item.text,
            selected=item.selected,
            index=index,
        )
        for index, item in enumerate(visible_items)
    ]
