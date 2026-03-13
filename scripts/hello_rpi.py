#!/usr/bin/env python3
"""Bare-minimum script to get something on the ST7789 screen of a Raspberry Pi Zero.

No app infrastructure needed — just the display driver and Pillow.

Requirements (install on the Pi before running):
    pip install RPi.GPIO==0.7.0 spidev==3.5 numpy==1.25.2 "Pillow>=10.0.0"

Note: the ``font_size`` keyword argument to ``ImageDraw.text`` was added in
Pillow 10.0.0.  Pillow 9.x and earlier will raise a TypeError here.

Usage:
    python scripts/hello_rpi.py
"""

import sys
import os

# Allow running from the repo root without a full package install.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from PIL import Image, ImageDraw
from seedsigner.hardware.displays.ST7789 import ST7789

WIDTH, HEIGHT = 240, 240

# ----- Build a simple image -----
img = Image.new("RGB", (WIDTH, HEIGHT), "#1a1a2e")
draw = ImageDraw.Draw(img)

# Accent bar at the top
draw.rectangle([0, 0, WIDTH, 4], fill="#4c7be8")

# Title
draw.text((WIDTH // 2, 80), "SeedSigner", fill="white", font_size=30, anchor="mm")

# Status line
draw.text((WIDTH // 2, 130), "Display OK", fill="#00e676", font_size=22, anchor="mm")

# Board label
draw.text((WIDTH // 2, 170), "RPi Zero", fill="#aaaaaa", font_size=18, anchor="mm")

# Accent bar at the bottom
draw.rectangle([0, HEIGHT - 4, WIDTH, HEIGHT], fill="#4c7be8")

# ----- Send to the display -----
display = ST7789()
display.show_image(img, 0, 0)

print("Done — image is now showing on the ST7789 display.")
