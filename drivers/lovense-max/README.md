# Lovense Max Driver

BLE driver for the Lovense **Max** and **Max 2**: a sleeve-style device combining a
vibration motor with a pneumatic air pump that creates a contracting/stroking sensation.

Matches devices advertising with the `LVS-Max` name prefix (e.g. `LVS-Max20`).

> **Note:** Do not install this alongside the generic `lovense` driver. Both match on the
> `LVS-` prefix and one will silently claim the device first.

## Actuators

| Actuator | Protocol command | Notes |
|----------|------------------|-------|
| Vibration motor | `Vibrate:N;` (0–20) | Follows EoM speed signal |
| Air pump | `Air:Level:N;` (0–5) | Oscillates between `airMin` and `airMax` via `tick` |

## Configuration

| Option | Range | Default | Description |
|--------|-------|---------|-------------|
| `maxLevel` | 1–20 | 20 | Maximum vibration speed |
| `airMin` | 0–5 | 1 | Air level at the deflated end of each stroke |
| `airMax` | 0–5 | 4 | Air level at the inflated end of each stroke |
| `oscPeriodMs` | 500–10000 | 2000 | Duration of one full inflate/deflate cycle (ms) |
| `oscEnabled` | bool | true | Disable to stop oscillation (holds at `airMin`) |
| `oscPeriodMinMs` | 200–10000 | 400 | Oscillation period at full vibration speed (ms); only used when `oscSpeedLinked` is enabled |
| `oscSpeedLinked` | bool | false | Scale oscillation speed with the EoM speed signal (`oscPeriodMs` at idle → `oscPeriodMinMs` at full speed) |

## Installation

Copy the `lovense-max/` folder into `plugins/` on your SD card and restart. Enable
Bluetooth, then scan and pair from Network Settings.

## TODO

A note to future-me: I noticed that the getPluginConfig takes a default, but the defaults
are already defined in the config schema. 

## License

MIT — see [LICENSE](../../LICENSE)
