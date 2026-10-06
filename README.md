# 22NFT build

Research, concept drawings, and a planner for living and working in an East to West Alita 22NFT (the current manufacturer page calls the floorplan 22NF), with a Bluetti RV5, two B4810 packs, six Callsun 275 W panels in parallel, a Victron Orion from the Transit alternator, a Splendide washer-dryer, Starlink, and a flat-towed manual Fiat 500 Abarth.

Nothing here is a fabrication drawing. Every sheet is stamped **CONCEPT — NOT FOR FABRICATION UNTIL FIELD-MEASURED.** Numbers are sourced in [SOURCES.md](SOURCES.md) or marked estimate. The VIN yellow sticker overrides published weights. UVW and CCC were not published.

## What’s in the repo

| Path | Contents |
| --- | --- |
| [research/](research/) | Vehicle specs, floorplans, comparable builds, power-equipment specs |
| [analysis/](analysis/) | Underbelly options and the axle math, enclosure requirements, interior layout. Washer location is left open |
| [designs/](designs/) | Sheets D-01 through D-09, SVG and PNG |
| [data/](data/) | JSON the planner reads |
| [app/index.html](app/index.html) | Weight, electrical, placement, bill of materials, pre-deposit checklist |
| [FIELD_MEASURE.md](FIELD_MEASURE.md) | Tape checklist for a dealer unit |
| [OPEN_QUESTIONS.md](OPEN_QUESTIONS.md) | Decisions, measurements, and the questions to send Bluetti |
| [SUMMARY.md](SUMMARY.md) | Ranked placements, risks, weight, unverified count |

## Open the planner

From the repository root:

```bash
python3 -m http.server 8765
```

Then open `http://localhost:8765/app/`.

The page loads `../data/*.json`. Opening the HTML file directly from disk will not load those files. There is no build step and no server-side app. Checkbox and input state is stored in `localStorage` under `n22ft-planner-v1`. Every read and write is in a try/catch, and the page still runs if storage is blocked.

The weight tab stays neutral until you type the yellow-sticker CCC. Axle results stay hidden until you type a lever arm, so a blank is not treated as zero.

## Read the drawings

Sheets are 1600×1100 SVG, with a PNG beside each one. The title block carries the project name, sheet number, title, scale, date, revision, the concept stamp, and the sources for any dimension on that sheet.

| Sheet | What it shows |
| --- | --- |
| D-01 | Side and rear elevations. Bays, spare, generator, and the tail-box candidate. Sizes that were not published are marked |
| D-02 | Underbelly plan. Candidate locations colored by the placement scores |
| D-03 | Axle diagram and the lever-arm arithmetic |
| D-04 | Tail box. Case sizes are the published B4810 and RV5 dimensions. Bolt pitch is blank |
| D-05 | One-line power. Six panels as two parallel groups of three |
| D-06 | Roof packing test around the AC, fan, antenna, and Starlink |
| D-07 | Interior as described in the sources, and both washer options |
| D-08 | Rear wall and the two washer elevations |
| D-09 | Storage assignments. The doors are slots until you measure them |

`designs/render_sheets.py` redraws the SVG files. It is not required to view them.

## How to read a number

- **CONFIRMED** — East to West, Ford’s body-builder manual where cited, or the equipment maker’s own document.
- **CREDIBLE** — a dealer listing, an owner thread, or a vendor drawing that is not this exact coach.
- **CONFLICT** — two sources disagree. Both numbers are kept.
- **UNVERIFIED** — not found. The planner leaves it blank.
- **ESTIMATE — VERIFY** — a scenario lever arm, or a weight you type yourself.
- **AWAITING BLUETTI** — the manual is silent or the table did not survive extraction. The questions are in OPEN_QUESTIONS.md.
