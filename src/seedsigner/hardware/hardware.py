from dataclasses import dataclass

screen_height = 240
screen_width = 320


@dataclass
class Platform:
    screen_height = screen_height
    screen_width = screen_width
    screen_dimensions = (screen_width, screen_height)
    # screen_width = 240
