from typing import Any, Literal


LanguageValue = Literal[
    "english",
    "spanish",
    "japanese",
    "italian",
    "french",
    "korean",
    "russian",
]


LANGUAGE_OPTIONS: tuple[LanguageValue, ...] = (
    "english",
    "spanish",
    "japanese",
    "italian",
    "french",
    "korean",
    "russian",
)


def coerce_language(value: Any) -> LanguageValue:
    if value in LANGUAGE_OPTIONS:
        return value
    raise ValueError(f"language must be one of: {', '.join(LANGUAGE_OPTIONS)}")
