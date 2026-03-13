# Lovense Driver

Generic BLE driver for single-motor Lovense vibrators. Matches any device advertising with
the `LVS-` name prefix and sends `Vibrate:N;` commands over the Lovense TX characteristic.

**This driver covers:** Lush, Lush 2, Hush, Hush 2, Ambi, Domi.

**Use a device-specific driver instead for:**
- **Lovense Edge / Edge 2** → `lovense-edge` (dual independent motors)
- **Lovense Nora** → `lovense-nora` (vibration + rotation arm)
- **Lovense Max** → `lovense-max` (vibration + pneumatic air actuator)

> **Important:** If a device-specific driver is installed, do **not** also install this
> generic driver. Plugin matching is first-come-first-served; both sharing the `LVS-`
> prefix will cause one to silently win.

Speed range is 0–20. The mapping is linear with the max configurable via `maxLevel` in
plugin config (default 20).

On connect a `Battery;` command is sent to the device. The response is currently not available
to the plugin system. This is a TODO note for future us.

## Installation

Copy the `lovense/` folder into `plugins/` on your SD card and restart.
Enable Bluetooth, then scan and pair from Network Settings.

## License

MIT — see [LICENSE](../../LICENSE)