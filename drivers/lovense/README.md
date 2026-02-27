# Lovense Bluetooth Driver

Bluetooth driver plugin for Lovense-compatible vibration devices.

## Features

- Automatic device detection (devices starting with "LVS-")
- Speed mapping: 0-255 (EOM3K) → 0-20 (Lovense)
- Async command queuing to prevent transmission conflicts
- Clean connection/disconnection handling

## Supported Devices

Any Lovense-compatible device that:
- Advertises with name starting with "LVS-"
- Supports standard Lovense BLE command protocol
- Has TX (write) and RX (notify) characteristics

## Installation

1. Copy `plugin.json` to your Edge-o-Matic 3000 SD card: `/plugins/lovense-driver.json`
2. Restart your device or reload plugins from the menu
3. Enable Bluetooth from Network Settings
4. Scan for and pair with your Lovense device

## Protocol Details

### BLE Characteristics

- **TX Characteristic**: Write property - sends commands to device
- **RX Characteristic**: Notify property - receives responses from device

### Commands

- `Vibrate:<speed>` - Set vibration speed (0-20)

### Speed Mapping

| EOM3K Speed | Lovense Speed |
|-------------|---------------|
| 0           | 0             |
| 1-13        | 1             |
| 14-26       | 2             |
| ...         | ...           |
| 242-254     | 19            |
| 255         | 20            |

**Formula**: `lovense_speed = (eom_speed == 255) ? 20 : eom_speed / 13`

## Troubleshooting

### Device not detected
- Ensure device is powered on and in pairing mode
- Check that device name starts with "LVS-"
- Verify Bluetooth is enabled in EOM3K settings

### Commands not responding
- Check that device is within Bluetooth range
- Verify the device control knob is not at minimum
- Try reconnecting the device

### Speed seems incorrect
- This is normal - Lovense uses 0-20 scale vs EOM3K's 0-255
- The driver automatically maps between these ranges

## License

MIT License — see [LICENSE](../../LICENSE)