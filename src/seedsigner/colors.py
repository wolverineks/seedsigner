from dataclasses import dataclass


@dataclass
class Colors:
    background = "#000000"
    text = "white"

    class button:
        background = "#2C2C2C"
        text = "#FCFCFC"

        class focused:
            background = "#FF9F0A"
            text = "#000000"
