# Floorplans, compartments, and what is actually published

Accessed 2026-10-06. Extracted dimensions live in [data/compartments.json](../data/compartments.json).

## Documents found

| Document | What it contains | What it does not contain |
| --- | --- | --- |
| [2027 22NF floorplan](https://www.easttowestrv.com/alita/22NF/15661) | Wheelbase, GVWR, GCWR, both GAWRs, fuel, length, height, tank gallons, 16 ft awning, feature list. Cabover bunk **60 × 80 in** | A drawing with cabinet sizes. Exterior width (printed TBD). LP capacity (printed TBD). UVW. CCC. Compartment schedule |
| [Alita brand page](https://www.easttowestrv.com/alita) | Same feature list and the 26 ft / 11,000 lb / 25 gal summary | A second floorplan with different numbers. 23TK is a different plan at the same published length and GVWR |
| [Printable floorplan index](https://www.easttowestrv.com/print/floorplans/alita) | 22NF and 23TK summary rows | Dimensions beyond that summary |
| [2024 Alita brochure PDF](https://www.easttowestrv.com/files/brochures/2024/2024alitabrochure.pdf) | Chassis pitch (AWD 350, 310 hp, 400 lb-ft, 178 in), 4,000 W generator, 81 in ceiling, solar option in the step well | A dimensioned 22NF interior |
| [Later Alita brochure](https://assets-cdn.interactcp.com/interactrv/brand_brochure/brand_brochure_202508250652544419744375.pdf?modified=0825202518525444) | Same chassis pitch. Interior ceiling stated as **7 ft** | A dimensioned interior. The file’s modified stamp is 2025-08-25 |
| [RV Guide 2026](https://www.rvguide.com/specs/east-to-west/class-c/2026/alita/22nf.html) and [2027](https://www.rvguide.com/specs/east-to-west/class-c/2027/alita/22nf.html) | Third-party equipment flags: spare, pass-through, receiver, one axle, exterior ladder, rear bumper drain-hose carrier, washer/dryer prewire listed as no | Measured cabinets. The 2027 page did not return a full fetch (HTTP 406); the 2026 page did |
| [Parris RV 22NF, Payson](https://www.parrisrv.com/product/new-2027-east-to-west-alita-22nf-3652054-16) | Walkthrough prose and a spec table | A floorplan image with scales |
| [RV Wholesalers 22NFT](https://www.rvwholesalers.com/inventory/New-East-to-West-Alita-22NFT-Class-C-Motorhome-RV-For-Sale/latest) | Discontinued 22NFT listing. Feature differences (Coleman-Mach 15k, 8 cu ft fridge). Weights all N/A | Photos of the actual floor (the page says the images are not actual) |

No iRV2 or Forest River forum thread of an owner measuring a 22NF or 22NFT was found. No dealer walkthrough video transcript with a tape on a compartment was found.

## Interior, from the dealer walkthrough (credible, not a drawing)

Parris RV’s copy of a 2027 22NF describes this sequence:

1. Swivel driver and passenger seats, and a **60 × 80 in** cabover with a cargo net.
2. A booth dinette.
3. Kitchen: deep stainless sink, portable induction cooktop, convection microwave, **6 cu ft** 12 V refrigerator, solid-surface counters with an extension.
4. A full bath with a shower and a counter, across from the kitchen.
5. A rear **60 × 80 in queen lift bed**.

The manufacturer feature list confirms the cabover size, the induction cooktop, the 6 cu ft fridge, the ducted air conditioner, and the slide-out toppers. It does not, in the bullets fetched, name the rear bed. “Queen lift” is the dealer’s phrase. The spec table on that dealer page says the coach sleeps 3, while RV Guide’s 2026 page says a maximum of 4 and its 2027 index has been summarized as 6. Sleeping count is a conflict. The two 60 × 80 surfaces (cabover and rear bed) are the only bed sizes in hand.

“Slide box construction” and “slide-out toppers” mean a slide exists. Which wall it is on, and how long it is, were not published.

Washer/dryer prewire is “No” on RV Guide. The manufacturer list does not mention a washer. A Splendide install is a new circuit, new plumbing, and a new vent path if the vented model is chosen.

## Exterior compartments

Published facts:

- Rotocast exterior storage compartments and slam-latch baggage doors (manufacturer).
- Outside shower, exterior LP quick-connect, black-tank flush, exterior TV hookups (manufacturer).
- Pass-through storage flagged standard by RV Guide, not by the manufacturer bullets.
- Rear bumper drain-hose carrier flagged by RV Guide.
- Side-port solar hookup, separate from the roof (manufacturer). The factory solar option is **200 W**, not six 275 W panels.
- Optional batteries go in the **step well**, not in a frame box.

Not published, and not invented here:

- How many baggage doors.
- Door width, height, or interior depth of any bay.
- Which bay is pass-through, and whether it is full-width.
- Where the generator sits, where the exhaust exits, where the spare hangs, where the tanks sit relative to the rails.

Those are the D-01, D-02, and D-09 field measurements.

## Underbelly

Nothing in the manufacturer set describes frame crossmembers, tank hangers, wiring runs, or the spare hanger on the finished coach. The only underbody numbers that exist in the file are chassis-level, from Ford and from a suspension vendor:

- 178 in wheelbase (coach page and Ford EL-LWB).
- 37.35 in from rear axle to the end of the chassis frame, adapter excluded (2023 BEMM).
- Up to 80 in of rear frame extension allowed on that 178 in chassis (2023 BEMM).
- 35.400 in center-to-center of the rails on a Kelderman 2014+ Transit 350HD DRW cutaway drawing. Inside clear width is less than that by the rail thickness, which is not on that callout.

A finished 26 ft body on a 178 in wheelbase has **134 in** of overhang to split between the nose and the tail. How much of that 134 in is behind the rear axle is the measurement that decides whether a tail battery box is aft of the axle, and by how much.
