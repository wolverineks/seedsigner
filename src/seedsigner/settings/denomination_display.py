from typing import Any, Literal


DenominationDisplayOption = Literal[
    "btc",
    "sats",
    "threshold",
    "hybrid",
]


DENOMINATION_OPTIONS: tuple[DenominationDisplayOption, ...] = (
    "btc",
    "sats",
    "threshold",
    "hybrid",
)


def coerce_denomination_display(value: Any) -> DenominationDisplayOption:
    if value in DENOMINATION_OPTIONS:
        return value
    raise ValueError(
        f"denomination_display must be one of: {', '.join(DENOMINATION_OPTIONS)}"
    )
