from dataclasses import dataclass

from seedsigner.components import Header, Body, LargeButton
from seedsigner.dimensions import Dimensions


@dataclass
class Grid:
    columns = 2
    rows = 2

    width = round(
        (Dimensions.width - Body.padding - Body.padding - Body.padding) / columns
    )
    height = round((Dimensions.height - Header.height - 3 * Body.padding) / rows)

    top = Body.padding
    bottom = top + height + Body.padding
    left = Body.padding
    right = Body.padding + width + Body.padding


def ScanButton(focused: bool):
    return LargeButton(
        label="Scan",
        icon="scan",
        x=Grid.left,
        y=Grid.top,
        focused=focused,
    )


def SeedsButton(focused: bool):
    return LargeButton(
        label="Seeds",
        icon="seeds",
        x=Grid.right,
        y=Grid.top,
        focused=focused,
    )


def ToolsButton(focused: bool):
    return LargeButton(
        label="Tools",
        icon="tools",
        x=Grid.left,
        y=Grid.bottom,
        focused=focused,
    )


def SettingsButton(focused: bool):
    return LargeButton(
        label="Settings",
        x=Grid.right,
        y=Grid.bottom,
        icon="gear",
        focused=focused,
    )
