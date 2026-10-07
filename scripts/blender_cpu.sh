#!/bin/sh
# Standard Blender on Linux: BLENDER=blender scripts/blender_cpu.sh --python scripts/build_model.py
# Mac headless fallback below leaves installed app unchanged.
set -eu
ROOT=$(CDPATH= cd -- "$(dirname "$0")/.." && pwd)
if [ -n "${BLENDER:-}" ]; then exec "$BLENDER" --background --threads 4 "$@"; fi
if [ -x /Applications/Blender.app/Contents/MacOS/Blender ]; then
 mkdir -p "$ROOT/.runtime/bin"
 cp /Applications/Blender.app/Contents/MacOS/Blender "$ROOT/.runtime/bin/BlenderCPU"
 xattr -c "$ROOT/.runtime/bin/BlenderCPU" || true
 codesign --force --sign - "$ROOT/.runtime/bin/BlenderCPU"
 ln -sfn /Applications/Blender.app/Contents/Resources "$ROOT/.runtime/Resources"
 clang -dynamiclib "$ROOT/scripts/nullsafe_strstr.c" -o "$ROOT/.runtime/nullsafe_strstr.dylib"
 export DYLD_INSERT_LIBRARIES="$ROOT/.runtime/nullsafe_strstr.dylib"
 export BLENDER_SYSTEM_RESOURCES=/Applications/Blender.app/Contents/Resources/5.2
 exec "$ROOT/.runtime/bin/BlenderCPU" --background --threads 4 "$@"
fi
exec blender --background --threads 4 "$@"
