from dataclasses import asdict, dataclass
from typing import Any, Optional


@dataclass
class SettingsValues:
    language: str = "english"
    persistent_settings: bool = True
    coordination_software: str = "sparrow"
    denomination_display: str = "btc"


DEFAULT_SETTINGS: dict[str, Any] = asdict(SettingsValues())


class Settings:
    def __init__(self, initial: Optional[dict[str, Any]] = None) -> None:
        self.values = SettingsValues()
        self.dirty = True
        if initial:
            self.load(initial)

    @property
    def language(self) -> str:
        self.dirty = False
        return self.values.language

    @language.setter
    def language(self, value: str) -> None:
        self.set("language", value)

    def set(self, key: str, value: Any) -> None:
        if not hasattr(self.values, key):
            raise AttributeError(f"Unknown setting: {key}")
        setattr(self.values, key, value)
        self.dirty = True
        self.save()

    def has_changed(self) -> bool:
        return self.dirty

    def load(self, loaded: Optional[dict[str, Any]] = None) -> None:
        values = DEFAULT_SETTINGS if loaded is None else loaded
        for key, value in values.items():
            if hasattr(self.values, key):
                setattr(self.values, key, value)
        self.dirty = True

    def save(self) -> None:
        pass


settings = Settings()
