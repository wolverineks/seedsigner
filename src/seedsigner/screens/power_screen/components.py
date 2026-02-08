from dataclasses import dataclass
from seedsigner.components import Header, Dimensions, Body


@dataclass
class Grid:
    columns = 2
    rows = 2
    width = int(
        (Dimensions.width - Body.padding - Body.padding - Body.padding) / columns
    )
    height = int((Dimensions.height - Header.height - 3 * Body.padding) / rows)

    top = Header.height + Body.padding
    bottom = top + height + Body.padding
    left = Body.padding
    right = Body.padding + width + Body.padding
