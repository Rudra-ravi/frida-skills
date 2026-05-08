#!/usr/bin/env bash
set -euo pipefail

echo "== host =="
command -v frida >/dev/null && frida --version || echo "frida: not found"
command -v frida-ls-devices >/dev/null && frida-ls-devices || true

if command -v adb >/dev/null; then
  echo "== android =="
  adb devices || true
  adb shell getprop ro.product.cpu.abi 2>/dev/null || true
  adb shell /data/local/tmp/frida-server --version 2>/dev/null || true
fi

echo "== processes =="
command -v frida-ps >/dev/null && frida-ps -Uai || true
