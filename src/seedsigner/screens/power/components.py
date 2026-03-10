from dataclasses import dataclass
from seedsigner.components import Body, LargeButton
from seedsigner.dimensions import Dimensions


@dataclass
class Grid:
    columns = 2
    width = round(
        (Dimensions.width - Body.padding - Body.padding - Body.padding) / columns
    )
    left = Body.padding
    right = Body.padding + width + Body.padding


def ShutdownButton(focused: bool):
    return LargeButton(
        label="Shutdown",
        icon="power",
        x=Grid.left,
        y=48,
        focused=focused,
    )


def RestartButton(focused: bool):
    return LargeButton(
        label="Restart",
        icon="restart",
        x=Grid.right,
        y=48,
        focused=focused,
    )
