"""Nobra control box: single-character speed commands, no reply protocol.

Service UUID is from the plugin's match block; the write characteristic UUID
isn't independently documented anywhere public, so it's a best guess following
the service UUID's numbering — replace it if a real unit proves otherwise.
"""

from emulator import DeviceProfile

SERVICE_UUID = "0000ABF0-0000-1000-8000-00805F9B34FB"
TX_UUID = "0000ABF1-0000-1000-8000-00805F9B34FB"

_LEVELS = "abcdefghijklmno"  # 'a'-'o' = levels 1-15


def _on_command(command: str) -> None:
    if command == "p":
        print("[nobra] stop")
    elif command in _LEVELS:
        print(f"[nobra] level {_LEVELS.index(command) + 1}")
    return None


PROFILE = DeviceProfile(
    name="NobraControl",
    service_uuid=SERVICE_UUID,
    tx_uuid=TX_UUID,
    on_command=_on_command,
)
