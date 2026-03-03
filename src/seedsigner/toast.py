from threading import Timer
import time
from dataclasses import dataclass
from typing import Optional

from seedsigner.components import Rect, Dimensions
from seedsigner.loopyUI import Component
from seedsigner.loopyUI.renderer import Text
from seedsigner.components import get_icon_info

OUTLINE_WIDTH = 1
HEIGHT = 40 + (OUTLINE_WIDTH * 2)
SCREEN_PADDING = 2
WIDTH = Dimensions.width - (OUTLINE_WIDTH * 2) - (SCREEN_PADDING * 2)
FILL_COLOR = "black"
TRANSITION_DURATION = 0.3
DISPLAY_DURATION = 5.0
X = 0
OPENED_Y = Dimensions.height - HEIGHT - SCREEN_PADDING
CLOSED_Y = Dimensions.height + OUTLINE_WIDTH
NOTIFICATION_COLOR = "#00F100"
TRAVEL_DISTANCE = HEIGHT + SCREEN_PADDING
PADDING = 4

font, code = get_icon_info("sdcard", 32)


@dataclass()
class Toast(Component):
    show_start_time: Optional[float] = None
    hide_start_time: Optional[float] = None

    state: str = "closed"  # default state
    dirty: bool = False  # default dirty state
    message: Optional[str] = None  # default message

    def render(self):
        if self.state == "closed":
            return None

        y = get_y(self.state, self.show_start_time, self.hide_start_time)

        return [
            bg(y),
            icon(y),
            message(self.message or "", y),
        ]

    def show(self, message: str):
        self.message = message
        self.state = "opening"
        self.dirty = True
        self.show_start_time = time.time()
        Timer(TRANSITION_DURATION, self.opened).start()

    def opened(self):
        self.state = "opened"
        self.dirty = True
        Timer(DISPLAY_DURATION, self.hide).start()

    def closed(self):
        self.dirty = True
        self.message = None
        self.state = "closed"

    def hide(self):
        self.dirty = True
        self.state = "closing"
        self.hide_start_time = time.time()
        Timer(TRANSITION_DURATION, self.closed).start()

    def has_changed(self):
        if self.state in ["opening", "closing"]:
            return True
        dirty = self.dirty
        self.dirty = False
        return dirty


def get_y(state, show_start_time, hide_start_time):
    if state == "opening":
        if show_start_time is None:
            raise ValueError("show_start_time should not be None when state is opening")

        return int(
            CLOSED_Y - (TRAVEL_DISTANCE * ease_out_quad(get_progress(show_start_time)))
        )

    if state == "closing":
        if hide_start_time is None:
            raise ValueError("hide_start_time should not be None when state is closing")

        return int(
            OPENED_Y + (TRAVEL_DISTANCE * ease_in_quad(get_progress(hide_start_time)))
        )

    if state == "opened":
        return OPENED_Y

    if state == "closed":
        return CLOSED_Y

    raise ValueError(f"unrecognized state: {state}")


def get_progress(start_time: float):
    now = time.time()
    elapsed = now - start_time
    progress = min(elapsed / TRANSITION_DURATION, 1.0)
    return progress


toast = Toast()


def bg(y):
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


def icon(y):
    return Text(
        x=X + PADDING,
        y=int(y) + PADDING,
        text=code,
        fill=NOTIFICATION_COLOR,
        size=32,
        font=font,
    )


def message(text: str, y: int):
    return Text(
        x=X + 48,
        y=int(y) + PADDING,
        text=text,
        fill=NOTIFICATION_COLOR,
        size=24,
    )


def ease_out_quad(t: float) -> float:
    """Starts fast, slows down at the end"""
    return 1 - (1 - t) * (1 - t)


def ease_in_quad(t: float) -> float:
    """Starts slow, accelerates"""
    return t**2
