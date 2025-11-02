#!/usr/bin/env python3

"""
Run the Minesweeper game **from bytecode only**.

- All compiled modules must be in: GAME/__pycache__/
- You may delete every .py file in GAME/ except this run_game.py
- Works from the project root and with VS Code's ▶ Run button

How it works:
We register a MetaPathFinder that looks up modules (e.g., 'play_minesweep',
'globals', 'utils', ...) in GAME/__pycache__/NAME.cpython-XY.pyc and loads
them with SourcelessFileLoader. This bypasses the normal requirement to
import through the package directory.
"""

import os
import sys
import importlib.abc
import importlib.machinery

os.environ["TERM"] = "xterm"


# --- Paths -------------------------------------------------------------------
GAME_DIR = os.path.dirname(__file__)
PYC_DIR = os.path.join(GAME_DIR, "__pycache__")
TAG = f"cpython-{sys.version_info.major}{sys.version_info.minor}"

if not os.path.isdir(PYC_DIR):
    print(f"❌ __pycache__ not found at: {PYC_DIR}")
    sys.exit(1)

# Keep your terminal in project root if you want; imports don't rely on CWD.
# But it's harmless to set CWD to GAME for predictable relative file I/O.
try:
    os.chdir(GAME_DIR)
except Exception:
    pass

# --- Import hook: load sourceless modules from GAME/__pycache__ --------------


class GamePycFinder(importlib.abc.MetaPathFinder):
    """
    Finds top-level modules (no dots in name) in GAME/__pycache__/
    as sourceless .pyc files:
        NAME.cpython-XY.pyc
        NAME.opt-1.cpython-XY.pyc
        NAME.opt-2.cpython-XY.pyc
    """

    def __init__(self, base_dir, tag):
        self.base = base_dir
        self.tag = tag

    def _candidate_paths(self, fullname: str):
        # Only handle top-level modules (no packages)
        if "." in fullname:
            return []
        base = os.path.join(self.base, "__pycache__")
        return [
            os.path.join(base, f"{fullname}.{self.tag}.pyc"),
            os.path.join(base, f"{fullname}.opt-1.{self.tag}.pyc"),
            os.path.join(base, f"{fullname}.opt-2.{self.tag}.pyc"),
        ]

    def find_spec(self, fullname, path=None, target=None):
        for cand in self._candidate_paths(fullname):
            if os.path.exists(cand):
                loader = importlib.machinery.SourcelessFileLoader(
                    fullname, cand)
                return importlib.machinery.ModuleSpec(
                    name=fullname, loader=loader, origin=cand
                )
        return None


# Install our finder **first** so it wins
sys.meta_path.insert(0, GamePycFinder(GAME_DIR, TAG))

print("▶️  Launching Minesweeper from bytecode only…")

# Import the game entrypoint; this will load the .pyc via our finder.
# All its imports (globals, utils, etc.) are also handled by the finder.
'''
try:
    import play_minesweep  # type: ignore
except Exception as e:
    print("❌ Runtime error while loading compiled modules:\n", e)
    sys.exit(1)
'''
import traceback

print("▶️  Launching Minesweeper from bytecode only…")

try:
    import play_minesweep  # type: ignore
except Exception as e:
    print("❌ Runtime error while loading compiled modules:")
    traceback.print_exc()
    sys.exit(1)


print("🏁  Game finished.")
