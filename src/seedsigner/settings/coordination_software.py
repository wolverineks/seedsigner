from typing import Any, Literal, cast


CoordinationSoftwareSelection = list[
    Literal[
        "bluewallet",
        "nunchuck",
        "sparrow",
        "spector_desktop",
        "keeper",
    ]
]

COORDINATION_SOFTWARE_OPTIONS: CoordinationSoftwareSelection = [
    "bluewallet",
    "nunchuck",
    "sparrow",
    "spector_desktop",
    "keeper",
]


def coerce_coordination_software(value: Any) -> CoordinationSoftwareSelection:
    if not isinstance(value, list):
        raise TypeError("coordination_software must be a list")

    unique: CoordinationSoftwareSelection = []
    for item in cast(list[Any], value):
        if item not in COORDINATION_SOFTWARE_OPTIONS:
            raise ValueError(f"Invalid coordination software value: {item}")
        if item not in unique:
            unique.append(item)
    return unique
