"""Hardware IO configuration for display drivers.

This provides the API expected by the copied display modules while keeping the
actual pin assignments configurable through environment variables.
"""

from __future__ import annotations

import os
from typing import Any


DEFAULT_HARDWARE_CONFIG = "waveshare_1.3hat"


def _env_int(name: str, default: int) -> int:
    value = os.getenv(name)
    if value is None:
        return default
    return int(value)


def _env_pin(name: str, default_line: int, gpiochip: str) -> list[Any] | str:
    value = os.getenv(name)
    if value is None:
        return [gpiochip, default_line]

    normalized = value.strip().lower()
    if normalized == "disabled":
        return "disabled"

    return [gpiochip, int(value)]


def get_hardware_pin_mapping(hardware_config: str | None = None) -> dict[str, dict[str, Any]]:
    if hardware_config in (None, "", DEFAULT_HARDWARE_CONFIG):
        gpiochip = os.getenv("SEEDSIGNER_GPIOCHIP", "/dev/gpiochip0")
        return {
            "display": {
                "dc": _env_pin("SEEDSIGNER_DISPLAY_DC", 25, gpiochip),
                "rst": _env_pin("SEEDSIGNER_DISPLAY_RST", 27, gpiochip),
                "bl": _env_pin("SEEDSIGNER_DISPLAY_BL", 24, gpiochip),
                "spi_bus": _env_int("SEEDSIGNER_DISPLAY_SPI_BUS", 0),
                "spi_device": _env_int("SEEDSIGNER_DISPLAY_SPI_DEVICE", 0),
                "cs": os.getenv("SEEDSIGNER_DISPLAY_CS", "enabled"),
            }
        }

    raise ValueError(f"Unsupported hardware config: {hardware_config}")