from typing import Any

from .default_settings import create_default_settings

from .coordination_software import CoordinationSoftwareSelection
from .denomination_display import DenominationDisplayOption
from .language import LanguageValue
from .persistent_settings import PersistentSettingsValue
from .schema import Schema, COERCE, SettingKey


class Settings:
    def __init__(self):
        self.values: Schema = create_default_settings()
        self.dirty = True

    ##### LANGUAGE ###############
    @property
    def language(self):
        return self.values["language"]

    @language.setter
    def language(self, value: LanguageValue):
        self.set("language", value)

    ##### PERSISTENT SETTINGS ##########
    @property
    def persistent_settings(self):
        return self.values["persistent_settings"]

    @persistent_settings.setter
    def persistent_settings(self, value: PersistentSettingsValue):
        self.set("persistent_settings", value)

    ##### COORDINATION SOFTWARE ##########
    @property
    def coordination_software(self):
        return self.values["coordination_software"]

    @coordination_software.setter
    def coordination_software(self, value: CoordinationSoftwareSelection):
        self.set("coordination_software", value)

    ##### DENOMINATION DISPLAY ##########
    @property
    def denomination_display(self):
        return self.values["denomination_display"]

    @denomination_display.setter
    def denomination_display(self, value: DenominationDisplayOption) -> None:
        self.set("denomination_display", value)

    ##### HELPER METHODS ##########
    def set(self, key: SettingKey, value: Any):
        self.values[key] = COERCE[key](value)

        self.dirty = True
        self.save()

    def has_changed(self):
        dirty = self.dirty
        self.dirty = False
        return dirty

    def load(self) -> None:
        self.values = create_default_settings()
        self.dirty = True

    def save(self) -> None:
        pass


settings = Settings()
