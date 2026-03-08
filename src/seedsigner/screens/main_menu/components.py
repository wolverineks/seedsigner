from dataclasses import dataclass

from seedsigner.components import Header, Dimensions, Body, LargeButton


@dataclass
class Grid:
    columns = 2
    rows = 2
    width = int(
        (Dimensions.width - Body.padding - Body.padding - Body.padding) / columns
    )
    height = int((Dimensions.height - Header.height - 3 * Body.padding) / rows)

    top = 0
    bottom = top + height + Body.padding
    left = 0
    right = Body.padding + width


def ScanButton(selected: bool):
    return LargeButton(
        label="Scan",
        icon="scan",
        x=Grid.left,
        y=Grid.top,
        selected=selected,
    )


def SeedsButton(selected: bool):
    return LargeButton(
        label="Seeds",
        icon="seeds",
        x=Grid.right,
        y=Grid.top,
        selected=selected,
    )


def ToolsButton(selected: bool):
    return LargeButton(
        label="Tools",
        icon="tools",
        x=Grid.left,
        y=Grid.bottom,
        selected=selected,
    )


def SettingsButton(selected: bool):
    return LargeButton(
        label="Settings",
        x=Grid.right,
        y=Grid.bottom,
        icon="gear",
        selected=selected,
    )
