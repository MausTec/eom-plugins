# Lovense Driver

BLE driver for Lovense vibrators. Matches any device advertising with the `LVS-` name prefix
and sends `Vibrate:N;` commands over the Lovense TX characteristic.

Speed range is 0–20. The mapping is linear with the max configurable via `maxLevel` in plugin
config (default 20).

## Installation

Copy `plugin.json` to `/plugins/` on your SD card and restart. Enable Bluetooth, then scan and
pair from Network Settings.

## License

MIT — see [LICENSE](../../LICENSE)