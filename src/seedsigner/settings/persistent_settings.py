from typing import Any


PersistentSettingsValue = bool


def coerce_persistent_settings(value: Any) -> PersistentSettingsValue:
    if isinstance(value, bool):
        return value
    raise TypeError("persistent_settings must be a bool")
