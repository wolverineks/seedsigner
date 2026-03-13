"""
Tests for display driver RGB565 color conversion.

The ST7789 and ILI9341 display drivers must convert PIL RGB images to
16-bit RGB565 big-endian format for transmission over SPI.  Previously,
this was done via ``Image.convert("BGR;16")`` which was removed from
modern Pillow and raises ``ValueError: image has wrong mode``.  The
fix uses NumPy to perform the same conversion correctly.
"""

import numpy as np
from PIL import Image


def rgb_to_rgb565_bytes(image: Image.Image) -> bytes:
    """Convert a PIL RGB image to 16-bit RGB565 big-endian bytes.

    This is the helper extracted from the fixed display drivers so that
    the conversion logic can be tested independently of the hardware.
    """
    arr = np.array(image.convert("RGB")).astype(np.uint16)
    return (
        ((arr[:, :, 0] & 0xF8) << 8)
        | ((arr[:, :, 1] & 0xFC) << 3)
        | (arr[:, :, 2] >> 3)
    ).astype(">u2").tobytes()


def _parse_rgb565(high: int, low: int):
    """Return (r8, g8, b8) approximation from a big-endian RGB565 pixel."""
    val = (high << 8) | low
    r5 = (val >> 11) & 0x1F
    g6 = (val >> 5) & 0x3F
    b5 = val & 0x1F
    return round(r5 * 255 / 31), round(g6 * 255 / 63), round(b5 * 255 / 31)


class TestRgb565Conversion:
    def test_black_encodes_as_all_zeros(self):
        img = Image.new("RGB", (1, 1), (0, 0, 0))
        data = rgb_to_rgb565_bytes(img)
        assert data == b"\x00\x00"

    def test_white_encodes_as_all_ones(self):
        img = Image.new("RGB", (1, 1), (255, 255, 255))
        data = rgb_to_rgb565_bytes(img)
        assert data == b"\xff\xff"

    def test_red_encodes_correctly(self):
        # Pure red: R=11111, G=000000, B=00000 → 0xF800
        img = Image.new("RGB", (1, 1), (255, 0, 0))
        data = rgb_to_rgb565_bytes(img)
        assert data == b"\xf8\x00"

    def test_green_encodes_correctly(self):
        # Pure green: R=00000, G=111111, B=00000 → 0x07E0
        img = Image.new("RGB", (1, 1), (0, 255, 0))
        data = rgb_to_rgb565_bytes(img)
        assert data == b"\x07\xe0"

    def test_blue_encodes_correctly(self):
        # Pure blue: R=00000, G=000000, B=11111 → 0x001F
        img = Image.new("RGB", (1, 1), (0, 0, 255))
        data = rgb_to_rgb565_bytes(img)
        assert data == b"\x00\x1f"

    def test_output_length_matches_pixel_count(self):
        img = Image.new("RGB", (240, 240), (0, 0, 0))
        data = rgb_to_rgb565_bytes(img)
        assert len(data) == 240 * 240 * 2

    def test_red_channel_not_swapped_with_blue(self):
        # If R and B were swapped, red would encode as blue (0x001F).
        img = Image.new("RGB", (1, 1), (255, 0, 0))
        data = rgb_to_rgb565_bytes(img)
        high, low = data[0], data[1]
        r8, g8, b8 = _parse_rgb565(high, low)
        # Red channel should dominate; blue should be near zero
        assert r8 > 200
        assert b8 < 20

    def test_does_not_raise_on_rgb_image(self):
        """Regression: Image.convert('BGR;16') raises ValueError on modern Pillow."""
        img = Image.new("RGB", (240, 240), (255, 159, 10))
        # Must not raise ValueError or any other exception
        data = rgb_to_rgb565_bytes(img)
        assert len(data) == 240 * 240 * 2
