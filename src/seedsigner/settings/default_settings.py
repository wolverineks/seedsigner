from .schema import Schema


def create_default_settings() -> Schema:
    return {
        "language": "english",
        "persistent_settings": True,
        "coordination_software": [
            "bluewallet",
            "nunchuck",
            "sparrow",
            "spector_desktop",
            "keeper",
        ],
        "denomination_display": "btc",
    }
