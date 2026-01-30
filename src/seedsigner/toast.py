from components import Button, Rect, Platform
from colors import Colors


class Toast:
    padding = 8
    width = Platform.screen_width
    height = 40
    x = 0
    y = Platform.screen_height - height
    bg = Rect(
        x=x,
        y=y,
        w=width,
        h=height,
        fill="red",
    )

    def __init__(self, router, visible, *children):
        self.children = children
        self.visible = visible
        self.router = router

    def render(self):
        return (
            [self.bg, Button(text="QWE", index=0, selected=False)]
            if self.visible
            else None
        )
