# Nobra/NobraControl Bluetooth Driver

Bluetooth driver plugin for Nobra devices running AzureFang firmware.

## Features

- Automatic device detection ("NobraControl" BLE name)
- 15-level speed control ('a' through 'o') plus stop ('p')
- Efficient: only transmits when speed changes
- Character-based command protocol

## Supported Devices

- Nobra devices with **AzureFang firmware** installed
- Device must advertise as "NobraControl"

## Setup Instructions

### 1. Prepare Your Nobra Device

1. **Power on** your Nobra device
2. **Check for green light** - this indicates AzureFang firmware is enabled
3. **If light is NOT green**:
   - Press the **outer two buttons** on the control box **simultaneously**
   - **Power cycle** the device (turn off and back on)
   - Green light should now be lit

### 2. Set Initial Vibration

Turn the main control knob so the Nobra device is **vibrating slightly**. This ensures the device is ready to respond to commands.

### 3. Pair with EOM3K

1. On your Edge-o-Matic 3000:
   - Push the knob to open the menu
   - Navigate to **Network Settings > Bluetooth Pair**
2. Select **"NobraControl"** from the device list
3. Wait for pairing to complete
4. ✅ Your EOM3K is now controlling your Nobra device!

## Installation

1. Copy `plugin.json` to your Edge-o-Matic 3000 SD card: `/plugins/nobra-driver.json`
2. Restart your device or reload plugins from the menu
3. Follow setup instructions above to pair your Nobra device

## Protocol Details

### BLE Characteristics

- **TX Characteristic**: Write-without-response - sends speed commands

### Command Format

Nobra uses single-character commands:
- `'p'` - Stop (speed 0)
- `'a'` - Speed level 1 (lowest)
- `'b'` - Speed level 2
- `'c'` through `'o'` - Speed levels 3-15
- `'o'` - Speed level 15 (highest)

### Speed Mapping

| EOM3K Speed | Nobra Level | Character |
|-------------|-------------|-----------|
| 0           | Stop        | 'p'       |
| 1-17        | 1           | 'a'       |
| 18-34       | 2           | 'b'       |
| 35-51       | 3           | 'c'       |
| ...         | ...         | ...       |
| 239-255     | 15          | 'o'       |

**Formula**: `round((speed / 255) * 15)` → map to 'a'-'o', or 'p' if 0

## Troubleshooting

### Device not detected
- **Check green light** - must be lit for AzureFang firmware
- Ensure device is powered on
- Verify Bluetooth is enabled in EOM3K settings
- Try power cycling the Nobra device

### Green light not turning on
- Press **both outer buttons** on control box simultaneously
- Power cycle the device
- If still not working, AzureFang firmware may not be installed

### Device paired but not responding
- Check that control knob is not at minimum position
- Verify device is within Bluetooth range (< 10 meters)
- Try reconnecting: unpair and pair again

### Vibration seems weak/inconsistent
- Turn the control knob slightly higher
- Ensure device battery is charged
- Check that no physical obstructions are present
15 discrete speed levels (not continuous 0-255)
- Character-based protocol for efficient transmission
- Only sends commands when speed level changes
- No response parsing required

## Firmware Requirements

**This driver requires AzureFang firmware**. If your Nobra device does not have AzureFang installed, this driver will not work.

## License

MIT License — see [LICENSE](../../LICENSE

- Based on community reverse-engineering of Nobra/AzureFang protocol
- Originally implemented as C driver (now extracted to plugin)
