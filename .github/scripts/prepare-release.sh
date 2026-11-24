#!/usr/bin/env bash
# Prepares the assets and release notes for a repo-wide release.
#
# Run from the repository root after `mt-sdk package` has written
# dist/packages. It:
#   - removes excluded plugins from dist/packages,
#   - merges the per-plugin checksum files into one SHA256SUMS,
#   - writes release notes to $RUNNER_TEMP/notes.md, marking which plugin
#     versions are new compared with the previous GitHub release.
#
# Environment:
#   EXCLUDE      Space-separated plugin names that are never released.
#   RUNNER_TEMP  Scratch directory (set automatically by GitHub Actions).
#   GH_TOKEN     Token for `gh`, used to read the previous release.

set -euo pipefail

exclude="${EXCLUDE:-}"
work="${RUNNER_TEMP:?RUNNER_TEMP must be set}"

mt-sdk package --dry-run --json > "$work/packages.json"

for name in $exclude; do
  rm -f dist/packages/"$name"-[0-9]*
done

if ! ls dist/packages/*.zip >/dev/null 2>&1; then
  echo "::error::No plugins left to release after exclusions."
  exit 1
fi

# One checksum file instead of one per plugin.
(cd dist/packages && cat ./*.sha256 > SHA256SUMS && rm ./*.sha256 && sha256sum -c SHA256SUMS)

prev="$(gh release list --limit 1 --json tagName --jq '.[0].tagName // empty')"
prev_assets=""
if [ -n "$prev" ]; then
  prev_assets="$(gh release view "$prev" --json assets --jq '.assets[].name')"
fi

{
  echo "Every plugin is attached below. Download the zip for the plugin you want, unzip it, and copy the folder it contains into the \`plugins\` folder on your device's SD card."
  echo
  echo "| Plugin | Version | Status |"
  echo "|--------|---------|--------|"
  jq -r --arg ex "$exclude" '($ex | split(" ")) as $skip | .packages[] | select([.name] | inside($skip) | not) | [.name, .version, .fileName] | @tsv' "$work/packages.json" |
    while IFS=$'\t' read -r name version file; do
      if printf '%s\n' "$prev_assets" | grep -qxF "$file"; then status="unchanged"; else status="**new**"; fi
      echo "| $name | $version | $status |"
    done
} > "$work/notes.md"
