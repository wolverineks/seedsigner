import os


def is_raspberry_pi():
    path = "/sys/firmware/devicetree/base/model"
    if not os.path.exists(path):
        return False
    try:
        with open(path, "r", encoding="utf-8") as f:
            return "raspberry pi" in f.read().lower()
    except OSError:  # covers ioerror, filenotfounderror, permissionerror, etc
        return False
