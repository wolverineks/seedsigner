from seedsigner.components import Rect, Dimensions
from threading import Timer
import time


HEIGHT = 40
WIDTH = Dimensions.width
FILL_COLOR = "red"
TRANSITION_DURATION = 0.3
DISPLAY_DURATION = 5.0
X = 0
OPENED_Y = Dimensions.height - HEIGHT


class Toast:
    def __init__(self):
        self.y = Dimensions.height

        self.show_start_time: float | None = None
        self.hide_start_time: float | None = None

        self.state = "closed"

    def render(self) -> Rect | None:
        if self.state == "closed":
            return None

        if self.state == "opened":
            return Rect(
                x=X,
                y=OPENED_Y,
                w=WIDTH,
                h=HEIGHT,
                fill=FILL_COLOR,
            )

        if self.state == "opening":
            if self.show_start_time is None:
                return None

            progress = get_progress(self.show_start_time)
            y = Dimensions.height - HEIGHT * progress

            return Rect(
                x=X,
                y=int(y),
                w=WIDTH,
                h=HEIGHT,
                fill=FILL_COLOR,
            )

        if self.state == "closing":
            if self.hide_start_time is None:
                return None

            progress = get_progress(self.hide_start_time)
            y = Dimensions.height - HEIGHT + HEIGHT * progress

            return Rect(
                x=X,
                y=int(y),
                w=WIDTH,
                h=HEIGHT,
                fill=FILL_COLOR,
            )

        return None

    def show(self):
        self.state = "opening"
        self.show_start_time = time.time()

        Timer(TRANSITION_DURATION, self.opened).start()
        Timer(DISPLAY_DURATION, self.hide).start()

    def opened(self):
        self.state = "opened"

    def closed(self):
        self.state = "closed"

    def hide(self):
        self.state = "closing"
        self.hide_start_time = time.time()
        Timer(TRANSITION_DURATION, self.closed).start()


def get_progress(start_time: float):
    now = time.time()
    elapsed = now - start_time
    progress = min(elapsed / TRANSITION_DURATION, 1.0)
    return progress


toast = Toast()
