# Edge-o-Matic 3000 Plugins

Community plugins and drivers for the Edge-o-Matic 3000.

## Structure

- **drivers/** - Bluetooth device drivers (Nobra, Lovense, etc.)
- **features/** - Session enhancement plugins (edge delay, post-orgasm control, etc.)
- **apps/** - Full application plugins (future)

## Installation

Download plugins from the
[Releases page](https://github.com/MausTec/eom-plugins/releases). Each plugin is
released on its own, as a zip named after the plugin and version, for example
`lovense-driver-1.0.0.zip`.

1. On your device's SD card, find or create a folder called `plugins`
   (lowercase, at the top level of the card).
2. Unzip the plugin you downloaded. It contains a folder named after the plugin
   (e.g. `lovense-driver/`) with a `plugin.json` inside.
3. Copy that whole folder into `plugins/` and restart the device.

Every release also has a matching `.sha256` file if you want to verify your
download.

The source code in this repository is not directly installable: it needs to be
compiled first, which is what the release zips are. Do not copy folders out of
a clone of this repository.

App `*.mpk` files should be copied to the `apps/` directory.

## Development

Plugins are developed using the Maus-Tec Software Development Kit to compile and test the `*.mtp`
Maus-Tec Plugin language. The `*.mtp` file is the source code. A `plugin.json` is the compiled
artifact that your device runs, so it is **not** committed to this repository, and pull requests
that edit one will be rejected. Change the `.mtp` source instead.

The MT-SDK is available here: [github.com/MausTec/mt-sdk](https://github.com/maustec/mt-sdk).

You can install it via NPM: `npm i -g @maustec/mt-sdk`. The version this repository is built with is
pinned in [`.mt-sdk-version`](.mt-sdk-version); install that exact version to get the same output as CI.

From the root of this repository:

```sh
mt-sdk build     # compile every plugin to <plugin>/dist/plugin.json
mt-sdk test      # run every *.test.mtp file under each plugin's tests/ folder
mt-sdk package   # create dist/packages/<name>-<version>.zip (+ .sha256) for each plugin
```

Pull requests are built and tested automatically. A PR should include updated tests under the
plugin's `tests/` folder whenever behavior changes.

The MTP and Test MTP syntax is heavily inspired by Elixir. The plugin execution runtime is very
action sequence oriented, so the best mental model is data transformation through pipes, and pure
functions. This is why Elixir-ish.

## Releasing

Releases are cut per plugin. Bump the plugin's `@version` in its `plugin.mtp`, merge it, then push a
tag named `<plugin-name>-v<version>`, where the plugin name is the `name` in its compiled
`plugin.json` (for example `lovense-driver`):

```sh
git tag lovense-driver-v1.0.1
git push origin lovense-driver-v1.0.1
```

The release workflow runs the tests, checks that the tag matches the plugin's name and version,
packages it with `mt-sdk package`, and attaches the zip and checksum to a GitHub release. Publishing
to Maus Hub will be added to this workflow when `mt-sdk release` is available.

## License

MIT License — see [LICENSE](LICENSE)
