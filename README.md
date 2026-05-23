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

Plugins are developed using the Maus-Tec Software Development Kit to compile and test the *.mtp 
Maus-Tec Plugin language. Any JSON files found in this repository are to be treated as the compiled
plugin that your device runs, and the *.mtp file is the actual code.

The MT-SDK is available here: [github.com/MausTec/mt-sdk](https://github.com/maustec/mt-sdk).

You can install it via NPM: `npm i -g @maustec/mt-sdk`

When inside a folder containing the `plugin.mtp` source, run `mt-sdk build` to generate the JSON,
and `mt-sdk test` to run the `*.test.mtp` files in the `test/` folder.

The MTP and Test MTP syntax is heavily inspired by Elixir. The plugin execution runtime is very
action sequence oriented, so the best mental model is data transformation through pipes, and pure
functions. This is why Elixir-ish.

TODO: Massive TODO, we still don't have proper documentation for the mt-sdk nor a release channel
for plugins. 

## License

MIT License — see [LICENSE](LICENSE)
