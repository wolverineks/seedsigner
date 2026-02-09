from dataclasses import dataclass
from seedsigner.components import Dimensions, Body, LargeButton


@dataclass
class Grid:
    columns = 2
    width = int(
        (Dimensions.width - Body.padding - Body.padding - Body.padding) / columns
    )
    left = Body.padding
    right = Body.padding + width + Body.padding


def ShutdownButton(selected: bool):
    return LargeButton(
        label="Shutdown",
        icon="power",
        x=Grid.left,
        y=Body.y + int((Body.height - LargeButton.height) / 2),
        selected=selected,
    )


def RestartButton(selected: bool):
    return LargeButton(
        label="Restart",
        icon="restart",
        x=Grid.right,
        y=Body.y + int((Body.height - LargeButton.height) / 2),
        selected=selected,
    )
