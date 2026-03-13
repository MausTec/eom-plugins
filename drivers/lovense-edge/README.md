# Lovense Edge Driver

BLE driver for the Lovense **Edge** and **Edge 2**: dual-motor adjustable prostate vibrators
with independent motor control.

Matches devices advertising with the `LVS-Edge` name prefix. You can adjust the match in the JSON
if you want to match other devices supporting 2 vibration motors, but I don't know of any right now
that exist.

> **Note:** Do not install this alongside the generic `lovense` driver. Both match on the
> `LVS-` prefix and one will silently claim the device first.

This is less useful for the Edge-o-Matic since this is a backend toy and the EoM is already connected
to the user's backend port, but the driver exists for ~~prostate~~ posterity.

## Motors

The Edge has two physically separate vibration motors:

| Motor | Protocol command | Config option |
|-------|------------------|---------------|
| Motor 1 (insertable tip) | `Vibrate:N;` | `motor1MaxLevel` |
| Motor 2 (external arm) | `Vibrate2:N;` | `motor2MaxLevel` |

Both motors receive the same EOM speed signal and ramp to their respective configured
maximums. To effectively disable a motor, set its max level to `0` and it will receive
`Vibrate:N;` with level `0` on every speed change, keeping it stopped.

## Configuration

| Option | Range | Default | Description |
|--------|-------|---------|-------------|
| `motor1MaxLevel` | 0–20 | 20 | Maximum speed for Motor 1 (tip) |
| `motor2MaxLevel` | 0–20 | 20 | Maximum speed for Motor 2 (arm) |

Both levels scale linearly with the EOM arousal output (0–255 maps to 0–maxLevel).

## Installation

Copy the `lovense-edge/` folder into `plugins/` on your SD card and restart. Enable
Bluetooth, then scan and pair from Network Settings.

## License

MIT — see [LICENSE](../../LICENSE)
