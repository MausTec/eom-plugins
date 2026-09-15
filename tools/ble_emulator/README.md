# BLE Device Emulator

macOS CoreBluetooth peripheral emulator for testing eom-plugins BLE drivers
without physical hardware. Advertises as a real device would and replies to
protocol commands, so a real EoM can connect to it and you can watch the traffic.

## Setup

    pip install pyobjc-core pyobjc-framework-Cocoa pyobjc-framework-CoreBluetooth

## Run

    cd tools/ble_emulator
    python3 run.py <device>

`<device>` is one of: lovense, lovense-edge, lovense-max, lovense-nora, nobra.

First run may trigger a macOS Bluetooth permission prompt, you'll have to approve it
for this terminal in System Settings > Privacy & Security > Bluetooth, then re-run.

Device connections may prompt a pairing request with PIN (this only happened when testing
with official mobile apps).

## Adding a device

Add a module under `devices/` exporting `PROFILE = DeviceProfile(...)` (see
`emulator.py` for the field list), then register it in `devices/__init__.py`.
Lovense devices share `devices/lovense_common.py` for the DeviceType/Battery/
Status/PowerOff handshake. Go reference buttplug.io/stpihkal/protocols/lovense/ for
the full protocol reference.
