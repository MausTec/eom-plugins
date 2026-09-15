"""Shared protocol pieces for Lovense devices (1st-generation GATT profile).

Reference: buttplug.io/stpihkal/protocols/lovense/
"""

from typing import Optional

SERVICE_UUID = "FFF0"
RX_UUID = "FFF1"  # device -> app, notify
TX_UUID = "FFF2"  # app -> device, write

FAKE_MAC = "AABBCCDDEEFF"
FAKE_FIRMWARE = "11"


def common_reply(model_type: str, command: str) -> Optional[str]:
    """Reply to a command shared by all Lovense devices, or None if it's device-specific."""
    if command == "DeviceType":
        return f"{model_type}:{FAKE_FIRMWARE}:{FAKE_MAC};"
    if command == "Battery":
        return "100;"
    if command == "Status:1":
        return "2;"
    if command == "PowerOff":
        return "OK;"
    return None
