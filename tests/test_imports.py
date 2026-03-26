"""
Tests that all importable modules in the seedsigner package can be imported
without errors or crashes. Hardware-specific modules that require platform
libraries (RPi.GPIO, spidev, pygame) are skipped when those libraries are
not available.
"""
import importlib
import pytest


# Modules that should import cleanly on any platform
IMPORTABLE_MODULES = [
    "seedsigner.app",
    "seedsigner.colors",
    "seedsigner.dimensions",
    "seedsigner.environment",
    "seedsigner.helpers",
    "seedsigner.screen_cache",
    "seedsigner.store",
    "seedsigner.toast",
    # components
    "seedsigner.components",
    "seedsigner.components.body",
    "seedsigner.components.header",
    "seedsigner.components.helpers",
    "seedsigner.components.icon",
    "seedsigner.components.scroll_list",
    # hardware (display driver uses lazy imports, safe to import)
    "seedsigner.hardware.displays.display_driver",
    # loopyUI core
    "seedsigner.loopyUI",
    "seedsigner.loopyUI.component",
    "seedsigner.loopyUI.events.events",
    "seedsigner.loopyUI.events.types",
    "seedsigner.loopyUI.get_platform",
    "seedsigner.loopyUI.paint",
    "seedsigner.loopyUI.renderer",
    "seedsigner.loopyUI.router",
    "seedsigner.loopyUI.screen_cache",
    # router
    "seedsigner.router",
    "seedsigner.router.router",
    # screens
    "seedsigner.screens",
    "seedsigner.screens.main_menu",
    "seedsigner.screens.main_menu.components",
    "seedsigner.screens.main_menu.main_menu",
    "seedsigner.screens.not_found",
    "seedsigner.screens.not_found.not_found",
    "seedsigner.screens.power",
    "seedsigner.screens.power.components",
    "seedsigner.screens.power.power_menu",
    "seedsigner.screens.power.power_off",
    "seedsigner.screens.power.restarting",
    "seedsigner.screens.scan",
    "seedsigner.screens.scan.components",
    "seedsigner.screens.scan.scan",
    "seedsigner.screens.seeds",
    "seedsigner.screens.seeds.seeds_menu",
    "seedsigner.screens.settings",
    "seedsigner.screens.settings.components",
    "seedsigner.screens.settings.coordination_software",
    "seedsigner.screens.settings.denomination_display",
    "seedsigner.screens.settings.language",
    "seedsigner.screens.settings.persistent_settings",
    "seedsigner.screens.settings.settings_menu",
    "seedsigner.screens.tools",
    "seedsigner.screens.tools.components",
    "seedsigner.screens.tools.tools_menu",
    # settings
    "seedsigner.settings",
    "seedsigner.settings.coordination_software",
    "seedsigner.settings.default_settings",
    "seedsigner.settings.denomination_display",
    "seedsigner.settings.language",
    "seedsigner.settings.persistent_settings",
    "seedsigner.settings.schema",
    "seedsigner.settings.settings",
]

# Modules that require hardware-only libraries (RPi.GPIO, spidev) and can
# only be imported on a real Raspberry Pi.
HARDWARE_ONLY_MODULES = [
    "seedsigner.hardware.displays.ST7789",
    "seedsigner.hardware.displays.ili9341",
    "seedsigner.hardware.displays.st7789_mpy",
    "seedsigner.loopyUI.events.rpi",
]

# Modules that require pygame and are only available in desktop/simulation mode.
DESKTOP_ONLY_MODULES = [
    "seedsigner.hardware.displays.desktop_display",
    "seedsigner.loopyUI.events.desktop",
]


@pytest.mark.parametrize("module_name", IMPORTABLE_MODULES)
def test_import(module_name):
    """Verify each module can be imported without errors on any platform."""
    importlib.import_module(module_name)


@pytest.mark.parametrize("module_name", HARDWARE_ONLY_MODULES)
def test_hardware_only_import(module_name):
    """Hardware-specific modules are skipped when RPi libraries are unavailable."""
    pytest.importorskip("RPi.GPIO", reason="RPi.GPIO not available on this platform")
    importlib.import_module(module_name)


@pytest.mark.parametrize("module_name", DESKTOP_ONLY_MODULES)
def test_desktop_only_import(module_name):
    """Desktop-only modules are skipped when pygame is unavailable."""
    pytest.importorskip("pygame", reason="pygame not available on this platform")
    importlib.import_module(module_name)
