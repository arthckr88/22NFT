# Underbelly placement

Accessed 2026-10-06. Scores are 1 (poor) to 5 (favorable). They are judgments, not measurements. The app reads the same table from [data/placements.json](../data/placements.json).

The bank this table is about: two B4810 packs at **101.4 lb** each (**202.8 lb**) and the RV5 at **30.86 lb**. Together **233.66 lb**, before cables, fuses, and a box whose weight is unknown. Wheelbase **178 in**. Rear GAWR **7,275 lb**. Front GAWR **4,630 lb**. GVWR **11,000 lb**. UVW, CCC, and today’s axle weights are the yellow sticker, which is blank.

## How the axle math works

A weight \(W\) added a distance \(x\) behind the rear axle (inches, \(x = 0\) on the axle) changes the axle loads by:

\[
\Delta R = W \frac{178 + x}{178} \qquad \Delta F = -W \frac{x}{178}
\]

\(\Delta R + \Delta F = W\). Weight behind the axle loads the rear by more than \(W\) and unloads the front.

A weight a distance \(y\) forward of the rear axle (and still behind the front axle):

\[
\Delta R = W \frac{178 - y}{178} \qquad \Delta F = W \frac{y}{178}
\]

Remaining rear margin after the addition:

\[
W_\text{max} = (7275 - R_\text{now}) \frac{178}{178 + x}
\]

\(R_\text{now}\) is the rear axle weight of the coach as it sits, from a scale or from the sticker’s as-built figure. It is unknown, so **no maximum safe box weight is stated**. Putting a number on it would be an invention.

CCC remaining is `sticker CCC − added weight`. Sticker CCC is blank, so remaining CCC is **unknown**.

Ford’s 2023 BEMM lists **37.35 in** from the rear axle to the end of the EL-LWB frame, before any adapter. The rows below use that distance as a **chassis landmark**, not as a measured battery position. The 12 in and 24 in rows are labeled scenarios so the lever is visible. They are not field measurements.

### Both packs and the hub at one station (233.66 lb)

| Scenario | \(x\) behind rear axle | Rear gain | Front change |
| --- | --- | --- | --- |
| On the axle | 0 | 233.66 lb | 0 |
| Scenario, not a measurement | 12 in | 249.41 lb | −15.75 lb |
| Scenario, not a measurement | 24 in | 265.16 lb | −31.50 lb |
| At the published chassis frame end | 37.35 in | 282.69 lb | −49.03 lb |

### Split: one B4810 at \(x\), the other B4810 and the hub on the axle

| Scenario | \(x\) | Rear gain | Front change |
| --- | --- | --- | --- |
| Scenario | 24 in | 247.33 lb | −13.67 lb |
| Chassis frame end | 37.35 in | 254.94 lb | −21.28 lb |

Splitting removes about 18 lb of rear-axle load versus putting everything 24 in behind the axle (265.16 − 247.33), and about 28 lb versus the 37.35 in case. That is the whole argument for option e. It is not a large number next to a 7,275 lb axle, and it is also not zero. It only matters once \(R_\text{now}\) is known. If the coach already sits close to 7,275 lb on the rear, 280 lb is the difference between legal and not. If it sits 1,000 lb under, the lever is a handling and departure problem more than a rating problem.

Front unloading of about 15–50 lb does not, by itself, threaten the 4,630 lb front GAWR. The risk on the front is the opposite: too little weight. No Ford percentage for minimum front-axle load was pulled into this file. The BEMM note on rear overhang says the recommended limit considers that the center of gravity of body and payload is not rearward of the rear axle. Read that callout on the actual BEMM page before treating the sentence as a design limit. A tail box moves the coach CG aft. How far is unknowable without the sticker axle weights.

Panels, the washer, water, and gear are **not** in the 233.66 lb. Roof panels (either 393.9 lb or 178.8 lb; see the weight conflict) act at the roof CG, which is unmeasured. A full fresh tank is 290.5 lb at 8.3 lb/gal and sits wherever the tank sits, which is also unmeasured. The washer is 148 lb and moves with an OPEN location.

## Scoring

Cost is a tier (5 = lower effort, 1 = higher), not a quote. No enclosure price was sourced.

| Option | Weight effect | Axle | Clearance / departure | Debris and water | Heat and cold | Service | Theft | Cable run | Fabrication | Cost tier |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| a. Tail beside the spare, as-is | 2 | 2 | 2 | 1 | 2 | 4 | 2 | 3 | 5 | 5 |
| b. Fabricated tail box | 2 | 2 | 3 | 4 | 3 | 4 | 4 | 3 | 2 | 2 |
| c. Spare relocated, well reused | 3 | 3 | 3 | 3 | 3 | 3 | 4 | 3 | 2 | 2 |
| d. Between the rails, near the axle | 5 | 5 | 3 | 3 | 3 | 2 | 4 | 4 | 2 | 2 |
| e. Split, one forward and one aft | 5 | 5 | 3 | 3 | 3 | 3 | 4 | 2 | 2 | 2 |
| f. Existing compartment, sealed | 4 | 3 | 4 | 4 | 3 | 5 | 3 | 3 | 4 | 3 |
| g. Under the rear lift bed | 2 | 2 | 5 | 5 | 4 | 5 | 5 | 3 | 3 | 3 |

### a. Tail beside the spare, as-is — RULED OUT as a finished install

The B4810 manual says not to use the pack in water and not to return it to service if it gets wet. An open tail pocket next to a spare is road spray, grit, and pressure washing. IP65 is a jet rating, not permission to live in that spray. No brochure gives a dry alcove there. The volume is still the place options b and c use. It is not a place to strap bare packs.

### b. Fabricated enclosure at the tail — CONDITIONAL

This is the option that matches the brief: out of sight, cabin storage untouched, using the tail volume you saw.

What has to be true, and is not yet known:

- A gap that fits two 23.94 × 14.96 × 5.71 in packs, the hub if it goes in the same box (17.72 × 19.69 × 6.30 in plus **7.87 in** of clearance on the faces the manual draws), a drain, and a door.
- The finished box stays above the departure line. Lowest point and departure angle are unpublished.
- The box does not cover the spare winch or the dump valves. If it does, it only survives by relocating that function (option c for the spare).
- Rear GAWR still has the margin in the formula above after \(x\) is measured.
- The box is bolted. Ford’s BEMM has no-weld and no-drill zones and a welding section. A weld on a Transit frame is a conversation with the chassis warranty and with Forest River, not a default.

Box weight is unknown and adds to \(W\). Steel versus aluminum is OPEN. Aluminum is what the Transit van spare-well build used (1/8 in 6061 sheet and 2 in angle) at about a 120 lb battery load. That build also cut a crossmember; this one does not. A commercial heated steel box exists for 130/148 in Transit **vans** at a listed $3,800 and does not claim the 178 in cutaway.

### c. Relocate the spare, then use the well — CONDITIONAL

Spare location and hanger type are unpublished, so the well’s size is unpublished. Sub-options for the tire:

| Spare goes to | Tradeoff |
| --- | --- |
| Hitch receiver or a bumper carrier | RULED OUT. The receiver is the Fiat tow bar |
| Rear wall of the cap | OPEN. May cover the camera, the ladder, or a door. Weight stays on a long lever |
| Another underbelly cradle forward of the axle | OPEN. Better lever for the tire. Has to miss tanks and exhaust |
| Leave it at home | OPEN, and a bad idea if you travel alone. Not chosen here |

Using the well does not remove the water problem. It still wants the sealed box from option b. Cutting the spare’s crossmember is what one van owner did, and that owner told other people not to copy it blindly. Not in this design.

### d. Between the rails, near the rear axle — CONDITIONAL

Best score on axle load: \(x \approx 0\), so the rear sees about 234 lb and the front sees none of it. The packs sit in the shadow of the rails, which is better for debris than the open tail and still wet.

Blockers, all unmeasured:

- Inside clear width. The only rail number in hand is **35.400 in center-to-center** on a vendor drawing. A pack is 14.96 in on its narrow side and 23.94 in on its long side, so one pack can fit a 35 in center-to-center gap with room to spare **if** the rails are not unusually thick and **if** nothing else is in the gap. Two packs side by side on the long side are 47.9 in, which is wider than 35.4 in center-to-center and does not fit side by side. Stacked they are 11.42 in thick. Whether the vertical gap exists is a measurement.
- Tanks (35 / 30 / 30 gal) and the generator and its exhaust. A battery box does not get to cover a dump gate or an exhaust outlet.
- Service: you are on your back, aft of the axle or under the floor, every time a terminal needs a wrench.

### e. Split the packs — CONDITIONAL

One pack aft (tail box or spare well), one pack at the axle or in a forward bay. The table above is the math. Cable run and paralleling get worse: the B4810 wants matched voltages within 0.3 V and a communication link, and the RV5 wants the shortest battery cables. Two directions of cable is the cost of the better axle picture. This is the option to prefer if the sticker shows the rear axle already heavy. It is not automatically preferred if the rear axle has a wide margin and you want one box to build.

### f. Existing exterior compartment — CONDITIONAL

Rotocast slam-latch bays are the driest “outside” volume the coach already has, and the door is the service access. Count, size, and which side of the axle they sit on are unpublished. A pack’s smallest face is 14.96 × 5.71 in and its length is 23.94 in. Any bay shallower than that fails. Slam latches are not a lock; add one if this is the bay. Spending the bay spends the volume D-09 assigns to hoses and tow gear. That trade is OPEN.

The step well is the factory location for two 12 V batteries in the solar option. It is not sized in any document for a 23.94 in pack. Treat it as too small until a tape says otherwise, and do not plan the B4810s there.

### g. Under the rear lift bed — CONDITIONAL, off-brief

Dry, warm relative to the underbelly, and how van builders actually mount lithium. The dealer copy describes a rear queen **lift** bed, so a cavity under it is plausible and unmeasured. It is still at the back of a 26 ft coach, so the axle lever may be as bad as the tail. It consumes the garage and the storage the brief is protecting. Listed so it is a real alternative if the underbelly measures out, not as the recommendation.

## Ruled out regardless of score

- **Hitch-mounted boxes.** They occupy the receiver the Fiat tow bar needs.
- **Roof-mounted batteries.** High CG, unknown roof structure, bad service, and the brief is underbelly.
- **Any spot that covers a tank dump, the generator exhaust, or spare access,** unless that option moves the thing it covers. Coordinates are unknown, so this is a constraint on b, c, d, e, and f, not a pre-drawn exclusion zone.

## What “added weight” can be added up today

| Piece | Weight | Bucket |
| --- | --- | --- |
| RV5 | 30.86 lb | Spec sheet |
| Two B4810 | 202.8 lb | Spec sheet |
| Six Callsun panels | 393.9 lb on the manufacturer page, or 178.8 lb on the conflicting listing | Conflict |
| One Orion-Tr Smart 12/48-8A | 4 lb | Spec sheet |
| Splendide, either model | 148 lb | Spec sheet |
| Enclosure, mounts, desk, Starlink model, cables, tow gear, personal gear | Unknown | Not in the total |
| Fresh water | 8.3 lb/gal, tank 35 gal = 290.5 lb if full | Spec sheet rate; gallons are a choice |

Partial sum using the manufacturer panel weight: **779.6 lb**, plus water and everything unknown.

Partial sum using the retailer panel weight: **564.5 lb**, same caveat.

Neither number is a CCC result. CCC is unknown. The 779.6 lb figure is a floor on the published parts only, and it moves by 215 lb if the panel weight conflict resolves the other way.
