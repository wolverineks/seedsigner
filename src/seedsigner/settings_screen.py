from typing import Literal

from seedsigner.components import Body, Header, BackButton, Button

HWButtonInput = Literal["up", "down", "select"]
NavKey = Literal[
    "language",
    "persistent_settings",
    "coordination_software",
    "denomination_display",
    "advanced",
    "i/o_test",
    "donate",
    "back",
    "power",
]

nav_map: dict[NavKey, dict[HWButtonInput, NavKey]] = {
    "back": {
        "down": "language",
    },
    "language": {
        "down": "persistent_settings",
        "up": "back",
    },
    "persistent_settings": {
        "up": "language",
        "down": "coordination_software",
    },
    "coordination_software": {
        "up": "persistent_settings",
        "down": "denomination_display",
    },
    "denomination_display": {
        "up": "coordination_software",
        "down": "advanced",
    },
    "advanced": {
        "up": "denomination_display",
        "down": "i/o_test",
    },
    "i/o_test": {
        "up": "advanced",
        "down": "donate",
    },
    "donate": {
        "up": "i/o_test",
    },
}


class SettingsScreen:
    def __init__(self, router):
        self.router = router
        self.selected: NavKey = "language"

    def render(self):
        selected = self.selected

        return [
            Header(
                left=BackButton(selected=selected == "back"),
                title="Settings",
            ),
            Body(
                [
                    Button(
                        text="Language",
                        selected=selected == "language",
                        index=0,
                    ),
                    Button(
                        text="Persistent Settings",
                        selected=selected == "persistent_settings",
                        index=1,
                    ),
                    Button(
                        text="Coordinator software",
                        selected=selected == "coordination_software",
                        index=2,
                    ),
                    Button(
                        text="Denomination display",
                        selected=selected == "denomination_display",
                        index=3,
                    ),
                    Button(
                        text="Advanced",
                        selected=selected == "advanced",
                        index=4,
                    ),
                    Button(
                        text="I/O test",
                        selected=selected == "i/o_test",
                        index=5,
                    ),
                    Button(
                        text="Donate",
                        selected=selected == "donate",
                        index=6,
                    ),
                ]
            ),
        ]

    def handle_input(self, input: HWButtonInput):
        if input == "select":
            self.handle_select()
        else:
            selected = self.selected
            if input in nav_map[selected]:
                self.selected = nav_map[selected][input]

    def handle_select(self):
        selected = self.selected
        print(f"Selected {selected}")
        if selected == "back":
            self.router.pop()
        else:
            self.router.navigate_to(selected)
