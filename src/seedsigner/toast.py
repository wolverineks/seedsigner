from seedsigner.components import Rect, Dimensions
from threading import Timer


class Toast:
    padding = 8
    width = Dimensions.width
    height = 40
    x = 0
    y = Dimensions.height - height
    bg = Rect(
        x=x,
        y=y,
        w=width,
        h=height,
        fill="red",
    )

    def __init__(self):
        self.visible: bool = False

    def render(self):
        return [self.bg] if self.visible else None

    def show(self):
        self.visible = True
        Timer(5, self.hide).start()

        return

    def hide(self):
        self.visible = False
        return


toast = Toast()
