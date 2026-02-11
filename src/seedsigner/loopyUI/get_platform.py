import sys
from typing import Literal


def get_platform() -> Literal["rpi", "desktop", "unknown"]:
    """
    Returns one of:
    - "rpi"       : Real Raspberry Pi hardware with GPIO
    - "desktop"   : Non-RPi machine (macOS, Windows, Linux desktop) with pygame
    - "unknown"   : Unknown
    """
    # Step 1: Check for Raspberry Pi hardware via /proc/cpuinfo
    if sys.platform.startswith("linux"):
        try:
            with open("/proc/cpuinfo", "r") as f:
                cpuinfo = f.read().lower()
                if "raspberry pi" in cpuinfo or "bcm" in cpuinfo:
                    # Step 2: Confirm GPIO is available
                    try:
                        import RPi.GPIO as GPIO

                        return "rpi"
                    except ImportError:
                        return "unknown"
        except OSError:
            pass

    # Step 3: Fallback to pygame check for desktop/simulator
    try:
        import pygame

        return "desktop"
    except ImportError:
        pass

    # Fallback
    return "unknown"
