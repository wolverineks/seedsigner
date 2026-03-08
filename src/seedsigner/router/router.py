from typing import Literal

from seedsigner.loopyUI.router import LoopyRouter

Route = Literal[
    "main",
    "settings",
    "scan",
    "tools",
    "seeds",
    "power",
    "restart",
    "power-off",
    "new_seed_camera",
    "new_seed_dice",
    "calculate_checksum",
    "address_explorer",
    "verify_address",
    "language",
    "coordination_software",
    "persistent_settings",
    "denomination_display",
    "donate",
    "persistent_settings",
    "advanced",
    "i/o_test",
    "scan_a_seedqr",
    "create_a_seed",
    "enter_a_12_word_seed",
    "enter_a_24_word_seed",
    "not_found",
]

ROUTES: tuple[Route, ...] = (
    "main",
    "settings",
    "scan",
    "tools",
    "seeds",
    "power",
    "restart",
    "power-off",
    "new_seed_camera",
    "new_seed_dice",
    "calculate_checksum",
    "address_explorer",
    "verify_address",
    "language",
    "coordination_software",
    "persistent_settings",
    "denomination_display",
    "donate",
    "persistent_settings",
    "advanced",
    "i/o_test",
    "scan_a_seedqr",
    "create_a_seed",
    "enter_a_12_word_seed",
    "enter_a_24_word_seed",
    "not_found",
)

Router = LoopyRouter[Route]

router = LoopyRouter[Route](
    routes=ROUTES,
    initial_route="main",
)
