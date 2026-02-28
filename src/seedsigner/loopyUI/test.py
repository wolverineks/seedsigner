from PIL import Image

from seedsigner.loopyUI.component import Component, Rect, Text
from seedsigner.loopyUI.renderer import render


class RendererSmokeTest(Component):
    def render(self):
        return [
            Rect(x=0, y=0, w=240, h=240, fill="white"),
            Rect(x=16, y=16, w=208, h=208, fill="#e8eefb", radius=14),
            Rect(x=32, y=132, w=176, h=64, fill="#4c7be8", radius=12),
            Text(x=40, y=46, text="loopyUI renderer", fill="black", size=22),
            Text(x=58, y=154, text="smoke test", fill="white", size=20),
        ]


def test_renderer_outputs_expected_canvas_and_colors(tmp_path):
    canvas = Image.new("RGB", (240, 240), "white")
    image = render(RendererSmokeTest(), canvas=canvas)

    assert image is canvas

    assert image.size == (240, 240)

    assert image.getpixel((2, 2)) == (255, 255, 255)
    assert image.getpixel((24, 24)) == (232, 238, 251)
    assert image.getpixel((40, 140)) == (76, 123, 232)

    output_file = tmp_path / "renderer_smoke_test.png"
    image.save(output_file)
    assert output_file.exists()
