# Edge-o-Matic 3000 Plugins

Community plugins and drivers for the Edge-o-Matic 3000.

## Structure

- **drivers/** - Bluetooth device drivers (Nobra, Lovense, etc.)
- **features/** - Session enhancement plugins (edge delay, post-orgasm control, etc.)
- **apps/** - Full application plugins (future)

## Installation

On your device's SD card, find or create a folder called `plugins`
(lowercase, at the top level of the card).

Each plugin in this repository is a named folder containing a `plugin.json`
file. Copy the whole folder (e.g. `lovense/`) into `plugins/` and restart
the device.

App `*.mpk` files should be copied to the `apps/` directory.

## Development

Plugins use the MT Actions JSON scripting system. See individual plugin READMEs for details.

An SDK to facilitate development and distribution is coming soon. When it is ready, it will be live
at [github.com/MausTec/eom-sdk](https://github.com/maustec/eom-sdk).

## License

MIT License — see [LICENSE](LICENSE)
