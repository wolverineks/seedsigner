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
    "not_found",
)

Router = LoopyRouter[Route]

router: Router = LoopyRouter[Route](
    routes=ROUTES,
    initial_route="main",
)
