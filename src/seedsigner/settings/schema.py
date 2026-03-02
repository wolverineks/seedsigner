from typing import Any, Literal, TypedDict

from .coordination_software import (
    CoordinationSoftwareSelection,
    coerce_coordination_software,
)
from .denomination_display import (
    DenominationDisplayOption,
    coerce_denomination_display,
)
from .language import (
    LanguageValue,
    coerce_language,
)
from .persistent_settings import (
    PersistentSettingsValue,
    coerce_persistent_settings,
)


class Schema(TypedDict):
    language: LanguageValue
    persistent_settings: PersistentSettingsValue
    coordination_software: CoordinationSoftwareSelection
    denomination_display: DenominationDisplayOption


SettingKey = Literal[
    "language",
    "persistent_settings",
    "coordination_software",
    "denomination_display",
]


COERCE: dict[SettingKey, Any] = {
    "language": coerce_language,
    "persistent_settings": coerce_persistent_settings,
    "coordination_software": coerce_coordination_software,
    "denomination_display": coerce_denomination_display,
}
