#!/usr/bin/env python3
"""CLI entry point. Usage: python3 run.py <device>"""

import sys

from devices import PROFILES
from emulator import run


def main() -> None:
    if len(sys.argv) != 2 or sys.argv[1] not in PROFILES:
        print("Usage: python3 run.py <device>")
        print(f"Available devices: {', '.join(sorted(PROFILES))}")
        raise SystemExit(1)

    run(PROFILES[sys.argv[1]])


if __name__ == "__main__":
    main()
