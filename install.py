#!/usr/bin/env python3
"""Install the PDFX plugin: copy to the user plugin directory, add a marked
menu block, rescan and enable. Re-running updates in place."""
import os, re, shutil, subprocess, sys
from pathlib import Path

PLUGIN_ID = "jkarmel.pdfx"
SRC = Path(__file__).resolve().parent
CONFIG = Path(os.environ.get("XDG_CONFIG_HOME", Path.home() / ".config"))
DEST = CONFIG / "omarchy" / "plugins" / PLUGIN_ID
MENU = CONFIG / "omarchy" / "extensions" / "omarchy-menu.jsonc"
BLOCK = f'''  // BEGIN {PLUGIN_ID}
  "trigger.sign-pdf": {{"label": "Sign a PDF", "icon": "󰈙", "description": "PDFX: open a PDF to sign or fill", "aliases": ["pdfx", "pdf", "sign"], "action": "omarchy-shell pdfx-plugin open ''"}},
  // END {PLUGIN_ID}
'''


def main():
    if SRC != DEST:
        if DEST.exists():
            shutil.rmtree(DEST)
        shutil.copytree(SRC, DEST, ignore=shutil.ignore_patterns(".git", "__pycache__"))
    MENU.parent.mkdir(parents=True, exist_ok=True)
    text = MENU.read_text() if MENU.exists() else "{\n}\n"
    if MENU.exists():
        shutil.copy(MENU, MENU.with_suffix(MENU.suffix + ".bak"))
    text = re.sub(rf"  // BEGIN {re.escape(PLUGIN_ID)}\n.*?  // END {re.escape(PLUGIN_ID)}\n", "", text, flags=re.S)
    text = text.replace("{\n", "{\n" + BLOCK, 1)
    MENU.write_text(text)
    subprocess.run(["omarchy-shell", "-q", "shell", "rescanPlugins"], check=False)
    subprocess.run(["omarchy", "plugin", "enable", PLUGIN_ID], check=False)
    print(f"installed {PLUGIN_ID} to {DEST}; menu entry 'Sign a PDF' added to {MENU}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
