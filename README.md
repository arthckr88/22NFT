# Andrew Rose — Alita 22NFT / Sunset Noir

Detailed scripted 3D build study, researched component envelopes, twelve Cycles render views, technical annotations, axle/energy scenarios and an embedded offline Three.js viewer.

Open **book/Alita-22NFT-Interactive-Build-Book.html** directly in a modern browser. It embeds its model, viewer code, fonts and rendered images; no network/server/CDN is needed. The PDF is the print edition. Layer controls: shell, power, solar, laundry A/B, interior, chassis and tow car. A and B are exclusive options. Power and tail presets hide the cabin and open the enclosure; the tail-case checkbox controls walls/lid. Exterior restores the complete coach.

**Installation status:** all equipment positions, roof/tail/cabinet geometry and cable/plumbing paths are ESTIMATE. Manufacturer dimensions are sourced in docs/SPECS.md. The model is a design study, not a survey or approved installation drawing. Read docs/DECISIONS.md, WALKTHROUGH.md and PROJECT-22NFT.md.

## Reproduce

Use Blender 5.2.2 LTS (or adapt the documented sky API for earlier versions), Python 3 with Pillow, Node and esbuild for rebuilding the viewer bundle.

```sh
python3 scripts/specifications.py
python3 scripts/build_analysis.py
BLENDER=blender scripts/blender_cpu.sh --python scripts/build_model.py
BLENDER=blender scripts/blender_cpu.sh --python scripts/render_view.py -- 01
# Repeat views 02 through 12 and inspect each PNG before proceeding.
python3 scripts/annotate.py
python3 scripts/build_book.py
```

On a Mac with the same headless Metal detection failure, scripts/blender_cpu.sh creates a local copied/ad-hoc-signed CPU executable and a null-safe libc shim. It never modifies installed Blender. See docs/QA.md.

Viewer bundle regeneration (esbuild installed):

```sh
esbuild scripts/viewer.js --bundle --format=iife --minify --alias:three=./book/vendor/build/three.module.js --outfile=book/viewer.bundle.js
```

A native CoreText/CoreGraphics PDF is included. Rebuild it on macOS with searchable vector text and clickable source links:

```sh
python3 scripts/pdf_layout.py
swiftc -module-cache-path .runtime/swift-cache scripts/pdf_native.swift -o .runtime/pdf_native
.runtime/pdf_native "$PWD" "$PWD/book/Alita-22NFT-Build-Book.pdf"
swiftc -module-cache-path .runtime/swift-cache scripts/pdf_verify.swift -o .runtime/pdf_verify
.runtime/pdf_verify "$PWD/book/Alita-22NFT-Build-Book.pdf" "$PWD/.runtime/pdf-pages"
```

Validate the exported model and the actual shared layer/preset functions from the repository root:

```sh
esbuild scripts/validate_model.mjs --bundle --platform=node --format=esm --alias:three=./book/vendor/build/three.module.js --outfile=.runtime/validate-model.mjs
node .runtime/validate-model.mjs
```

Browser automation was blocked by this workspace. The actual GLTFLoader, embedded gzip model, shared layer toggles and dimension/axle checks were validated in Node; no live-browser visual pass is claimed. See docs/model-validation.json and QA.md. All native PNGs and source blend/GLB are included.

## Evidence

Current OEM 2027 22NF: 26 ft length / 178 in WB / 11,000 GVWR / 13,500 GCWR / 4,630 front and 7,275 rear GAWR. Exact production unit unknown. Width 91 in and usable roof length 220 in remain estimates from earlier planning. Historical Ford upfitter reference is not current-year mounting approval.

The requested six-panel parallel branch produces 77.52 A and conflicts with the published RV5 50 A input. Orions cannot feed up-to-60 V into a 50 V-max PV input. B4810 external charging and generator/AGS interfaces need manufacturer verification.

Six-panel rows alone use ~15.50 ft with one-inch gaps; including modeled A/C band uses ~18.04 ft. Complete tail assembly estimate adds +403.45 lb rear / −114.79 lb front. Gross build additions ~998.64 lb before actual removals, driver, water/fuel and gear. No remaining payload is asserted.

Three.js MIT and font OFL licenses are in book/vendor. All RV/car/appliance geometry is generic, without manufacturer logos or badges. No red or oxblood palette.
