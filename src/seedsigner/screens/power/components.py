from dataclasses import dataclass
from seedsigner.components import Body, LargeButton
from seedsigner.dimensions import Dimensions


@dataclass
class Grid:
    columns = 2
    width = int((Dimensions.width - Body.padding) / columns)
    left = 0
    right = width


def ShutdownButton(selected: bool):
    return LargeButton(
        label="Shutdown",
        icon="power",
        x=Grid.left,
        y=36,
        selected=selected,
    )


def RestartButton(selected: bool):
    return LargeButton(
        label="Restart",
        icon="restart",
        x=Grid.right,
        y=36,
        selected=selected,
    )
