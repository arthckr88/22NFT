# Alita 22NFT, 3D build model R1

Scripted Blender model and render set of the East to West Alita 22NFT with the full custom build:
Bluetti RV5 + 2x B4810 under the tail, six Callsun 275W panels in parallel, two Victron Orion-Tr
12/48 chargers, generator tie-in, Furrion Chill Cube 18K, Starlink Mini, Splendide WDV2200XCD in two
candidate locations (A bath side, B rear garage), and a flat-towed Fiat 500 Abarth.

## Layout

| Path | What |
| --- | --- |
| `scripts/specs.py` | Every dimension used, with source and status (Confirmed / Credible / Estimate) |
| `scripts/lib.py` | Geometry and material helpers (inches in, metres out) |
| `scripts/build.py` | Builds the whole scene |
| `scripts/render.py` | Camera, lighting and render settings for each shot; writes anchor positions for labels |
| `scripts/annotate.py` | Labels, leader lines and dimensions over the renders |
| `scripts/axles.py` | Axle load math, writes `docs/axles.json` |
| `scripts/export_glb.py` | Saves `model/22nft.blend` and exports `model/22nft.glb` with layer prefixes |
| `scripts/build_book.py` | Assembles the web build book in `book/` |
| `renders/` | 13 renders (1920x1080) and `annotated/` versions |
| `book/` | The published build book (HTML, images, model) |

## Reproduce

```
pip install bpy --break-system-packages   # Blender 5.2 as a Python module
cd scripts
python3 axles.py
./render_all.sh 01_exterior 02_elevation 03_roof 04_underbelly 04b_tail_section 05_xray \
  06_interior 07_desk 08_laundry_A 09_laundry_B 10_floorplan 11_axles 12_night
python3 annotate.py
python3 export_glb.py
python3 build_book.py
```

Fonts for the annotations (IBM Plex Mono, Jost) are read from `$AR_FONTS`.

Coordinates: inches, x from the rear wall forward (rear axle 94, front axle 272), +y roadside, z up from ground.
Every value marked Estimate in `specs.py` is a modelled guess to verify at the walkthrough.
