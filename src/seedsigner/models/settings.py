"""Compatibility wrapper for older display-driver imports.

Older hardware drivers imported ``seedsigner.models.settings.Settings`` and
expected a ``get_platform_default_hardware_config`` classmethod. This repo's
active settings system lives under ``seedsigner.settings`` instead, so this
module preserves the old import path for copied drivers.
"""

import os


class Settings:
    @classmethod
    def get_platform_default_hardware_config(cls) -> str:
        return os.getenv("SEEDSIGNER_HARDWARE_CONFIG", "waveshare_1.3hat")
