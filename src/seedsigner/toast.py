from threading import Timer
import time
from dataclasses import dataclass
from typing import Optional

from seedsigner.components import Rect, Dimensions
from seedsigner.loopyUI import Component

OUTLINE_WIDTH = 1
HEIGHT = 40 - OUTLINE_WIDTH
WIDTH = Dimensions.width - OUTLINE_WIDTH
FILL_COLOR = "black"
TRANSITION_DURATION = 0.3
DISPLAY_DURATION = 5.0
X = 0
OPENED_Y = Dimensions.height - HEIGHT - 4
NOTIFICATION_COLOR = "#00F100"


@dataclass()
class Toast(Component):
    y: int = Dimensions.height  # default value

    show_start_time: Optional[float] = None
    hide_start_time: Optional[float] = None

    state: str = "closed"  # default state

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
                radius=8,
                outline=NOTIFICATION_COLOR,
                width=OUTLINE_WIDTH,
            )

        if self.state == "opening":
            if self.show_start_time is None:
                return None

            progress = get_progress(self.show_start_time)
            y = Dimensions.height - HEIGHT * ease_out_quad(progress)

            return Rect(
                x=X,
                y=int(y),
                w=WIDTH,
                h=HEIGHT,
                fill=FILL_COLOR,
                radius=8,
                outline=NOTIFICATION_COLOR,
                width=OUTLINE_WIDTH,
            )

        if self.state == "closing":
            if self.hide_start_time is None:
                return None

            progress = get_progress(self.hide_start_time)
            y = Dimensions.height - HEIGHT + HEIGHT * ease_in_quad(progress)

            return Rect(
                x=X,
                y=int(y),
                w=WIDTH,
                h=HEIGHT,
                fill=FILL_COLOR,
                radius=8,
                outline=NOTIFICATION_COLOR,
                width=OUTLINE_WIDTH,
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


def ease_out_quad(t: float) -> float:
    """Starts fast, slows down at the end"""
    return 1 - (1 - t) * (1 - t)


def ease_in_quad(t: float) -> float:
    """Starts slow, accelerates"""
    return t**2
