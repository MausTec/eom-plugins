# Lovense Nora Driver

BLE driver for the Lovense **Nora**: a dual-actuator toy with an internal vibration motor
and an externally rotating arm.

Matches devices advertising with the `LVS-Nora` name prefix (e.g. `LVS-Nora36`).

> **Note:** Do not install this alongside the generic `lovense` driver. Both match on the
> `LVS-` prefix and one will silently claim the device first.

## Actuators

| Actuator | Protocol command | Config option |
|----------|------------------|---------------|
| Internal vibration motor | `Vibrate:N;` | `maxVibrate` |
| Rotating external arm | `Rotate:N;` | `maxRotate` |

Setting `maxRotate` to `0` fully disables rotation commands so the arm stays still (or
at whatever speed was last set by the hardware button on the device).

Rotation direction is not managed by this driver.

## Configuration

| Option | Range | Default | Description |
|--------|-------|---------|-------------|
| `maxVibrate` | 1–20 | 20 | Maximum vibration speed |
| `maxRotate` | 0–20 | 12 | Maximum rotation speed; `0` disables rotation commands |

Both levels scale linearly with the EOM arousal output (0–255 maps to 0–max).

## Installation

Copy the `lovense-nora/` folder into `plugins/` on your SD card and restart. Enable
Bluetooth, then scan and pair from Network Settings.

## License

MIT — see [LICENSE](../../LICENSE)
