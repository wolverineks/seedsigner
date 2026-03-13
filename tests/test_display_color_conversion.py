"""Tests for the RGB-to-RGB565 colour conversion used by the display drivers.

The three hardware display drivers (ST7789, st7789_mpy, ili9341) all convert
24-bit RGB PIL images to 16-bit RGB-5:6:5 big-endian byte strings before
sending pixel data over SPI.  These tests verify the conversion formula
without requiring any hardware or SPI access.
"""

import numpy as np
from PIL import Image


def _rgb_to_565(image: Image.Image) -> bytes:
    """Reference implementation of the RGB-to-RGB565 conversion shared by all
    three display drivers."""
    arr = np.array(image.convert("RGB")).astype(np.uint16)
    return (
        ((arr[:, :, 0] & 0xF8) << 8)
        | ((arr[:, :, 1] & 0xFC) << 3)
        | (arr[:, :, 2] >> 3)
    ).astype(">u2").tobytes()


def test_pure_red():
    img = Image.new("RGB", (1, 1), (255, 0, 0))
    assert _rgb_to_565(img) == b"\xf8\x00"


def test_pure_green():
    img = Image.new("RGB", (1, 1), (0, 255, 0))
    assert _rgb_to_565(img) == b"\x07\xe0"


def test_pure_blue():
    img = Image.new("RGB", (1, 1), (0, 0, 255))
    assert _rgb_to_565(img) == b"\x00\x1f"


def test_white():
    img = Image.new("RGB", (1, 1), (255, 255, 255))
    assert _rgb_to_565(img) == b"\xff\xff"


def test_black():
    img = Image.new("RGB", (1, 1), (0, 0, 0))
    assert _rgb_to_565(img) == b"\x00\x00"


def test_output_length_240x240():
    img = Image.new("RGB", (240, 240), "red")
    pix = _rgb_to_565(img)
    assert len(pix) == 240 * 240 * 2


def test_output_length_320x240():
    img = Image.new("RGB", (320, 240), "blue")
    pix = _rgb_to_565(img)
    assert len(pix) == 320 * 240 * 2


def test_red_and_blue_channels_are_not_swapped():
    """Ensure R and B are in the correct positions in the 16-bit word."""
    red_img = Image.new("RGB", (1, 1), (255, 0, 0))
    blue_img = Image.new("RGB", (1, 1), (0, 0, 255))
    red_val = int.from_bytes(_rgb_to_565(red_img), "big")
    blue_val = int.from_bytes(_rgb_to_565(blue_img), "big")
    # Red should be in the top 5 bits, blue in the bottom 5 bits
    assert red_val == 0xF800
    assert blue_val == 0x001F
    assert red_val != blue_val
