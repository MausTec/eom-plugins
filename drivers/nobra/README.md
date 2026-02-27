# Nobra Driver

BLE driver for Nobra devices running AzureFang firmware. Matches on the exact name
`NobraControl` and sends single-character speed commands (`p` for stop, `a`–`o` for
levels 1–15).

The device needs to be in AzureFang mode (green indicator light) before pairing. If it
isn't, hold both outer buttons on the control box and power-cycle the unit.

Max level is configurable via `maxLevel` in plugin config (default 15).

## Installation

Copy `plugin.json` to `/plugins/` on your SD card and restart. Enable Bluetooth, then scan
and pair from Network Settings.

## License

MIT — see [LICENSE](../../LICENSE)
