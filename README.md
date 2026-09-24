# PDFX plugin for Omarchy

Shell-side surface for [PDFX](https://github.com/jkarmel/pdfx), the native PDF
signing and form-filling app. The app is the `pdfx` package; this plugin adds:

- **Sign a PDF** in the Omarchy menu: picks a file with the system chooser and
  opens it in PDFX on the current workspace.
- **IPC target** `pdfx-plugin` for keybindings: `omarchy-shell pdfx-plugin open`
  (or `open /path/to/file.pdf`).
- **First-run install**: if `pdfx` is missing, a terminal opens with
  `omarchy pkg add pdfx`.

## Install

```bash
omarchy plugin add https://github.com/jkarmel/omarchy-pdfx-plugin.git --enable --yes
python3 ~/.config/omarchy/plugins/jkarmel.pdfx/install.py   # adds the menu entry
```

Keybinding example for `~/.config/hypr/bindings.lua`:

```lua
o.bind("SUPER + SHIFT + P", "Sign a PDF", "omarchy-shell pdfx-plugin open ''")
```

No shell code from this plugin runs until you use the menu entry or IPC.
