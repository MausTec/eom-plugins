# Edge-o-Matic 3000 Plugins

Community plugins and drivers for the Edge-o-Matic 3000.

## Structure

- **drivers/** - Bluetooth device drivers (Nobra, Lovense, etc.)
- **features/** - Session enhancement plugins (edge delay, post-orgasm control, etc.)
- **apps/** - Full application plugins (future)

## Installation

Download plugins from the
[latest release](https://github.com/MausTec/eom-plugins/releases/latest). Every
release contains every plugin, each as a zip named after the plugin and its
version, for example `lovense-driver-1.0.0.zip`. Only download the plugins you
need; drivers for similar devices (such as the Lovense ones) should not be
installed together unless their descriptions say so.

1. On your device's SD card, find or create a folder called `plugins`
   (lowercase, at the top level of the card).
2. Unzip the plugin you downloaded. It contains a folder named after the plugin
   (e.g. `lovense-driver/`) with a `plugin.json` inside.
3. Copy that whole folder into `plugins/` and restart the device.

Every release also has a `SHA256SUMS` file if you want to verify your downloads
(`sha256sum -c SHA256SUMS`).

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

Releases are repo-wide: one GitHub release contains the package of every plugin, so the latest
release always has everything. Plugins keep their own versions (the `@version` in each
`plugin.mtp`); the release notes mark which plugin versions are new in that release.

1. Bump `@version` in the `plugin.mtp` of each plugin that changed, and merge to `main`.
2. Push **one** tag named `release-YYYY.MM.DD` (add `-2`, `-3`, ... for more than one release in a
   day):

   ```sh
   git tag release-2026.11.24
   git push origin release-2026.11.24
   ```

   Don't push several tags at once. GitHub apparently does not run workflows when more than three tags are
   pushed together. Alternatively, run the **Release** workflow from the Actions tab and enter the
   tag name; it creates the tag for you.

The release workflow runs the tests, packages every plugin with `mt-sdk package`, and attaches the
zips and a `SHA256SUMS` file to the release. Example and concept plugins that are
listed in the workflow's `EXCLUDE` variable are skipped. Publishing to Maus-Hub will be added to this workflow
when `mt-sdk release` is available.

## License

MIT License — see [LICENSE](LICENSE)
