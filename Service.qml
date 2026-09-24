import QtQuick
import Quickshell
import Quickshell.Io

// Thin shell-side surface for PDFX. The app itself is the `pdfx` package;
// this plugin only launches it. `omarchy-shell pdfx-plugin open [path]`
// picks a PDF (or opens the given one) on the active workspace.
Item {
  id: root
  readonly property string helper: Qt.resolvedUrl("pdfx-menu").toString().replace(/^file:\/\//, "")

  function open(path) {
    var command = ["/usr/bin/python3", "-I", root.helper]
    if (path) command.push(path)
    Quickshell.execDetached(command)
    return true
  }

  IpcHandler {
    target: "pdfx-plugin"
    function open(path: string): bool { return root.open(path) }
    function ping(): string { return "pdfx plugin ready" }
  }
}
