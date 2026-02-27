# Hello World

Test fixture plugin. On `modeSet` it reads `runCount` from plugin config, increments it,
saves it back, and logs the result along with the current `wifi_on` system config value.

Also logs incoming `speedChange` events, which is useful for confirming event dispatch
without BLE hardware.

Not intended for production use.

## What to verify

- Serial log shows `hello-world: run #N` on each boot (N increments)
- `wifi_on` value in log matches device settings
- Speed changes produce log lines when the device is in an active session

## Installation

Copy `plugin.json` to `/plugins/` on your SD card and restart.

## License

MIT — see [LICENSE](../../LICENSE)
