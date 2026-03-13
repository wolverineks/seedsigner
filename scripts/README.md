# scripts/

Utility scripts for SeedSigner development and hardware verification.

## `hello_rpi.py` — bare-minimum display test

The quickest way to verify that an ST7789 240×240 display is correctly wired
to a Raspberry Pi Zero and that the software stack is working.

### What it does

Draws a simple splash screen directly on the ST7789 display using only:

- `RPi.GPIO` — GPIO control
- `spidev` — SPI bus access
- `numpy` — RGB→RGB565 pixel conversion
- `Pillow` — image creation

No app routing, no settings, no screens — just the display driver and PIL.

### Setup

Install the Pi-side dependencies (if you haven't already):

```bash
pip install RPi.GPIO==0.7.0 spidev==3.5 numpy==1.25.2 "Pillow>=10.0.0"
```

> **Note:** `ImageDraw.text(font_size=…)` requires Pillow 10.0.0 or newer.
> Pillow 9.x and earlier will raise a `TypeError`.

Or, install the full package from the repo root:

```bash
pip install -e .
pip install -r requirements-raspi.txt
```

### Run

From the repo root on the Raspberry Pi Zero:

```bash
python scripts/hello_rpi.py
```

If everything is wired correctly you will see a dark-blue splash screen with
the text **"SeedSigner"** and **"Display OK"** appear on the LCD.
