# 22NFT Build Plan: Outside Review Packet (v2)

**Version:** v2, Wednesday, October 7, 2026 (Pacific Time). This replaces v1, which was built on the October 5–6 plan.
**What changed since v1:** AC is now a Furrion Chill Cube 18K. Washer is the vented Splendide WDV2200XCD. Battery location is decided (sealed box at the tail, packs only). Washer location is still open between bath side and rear garage. The panel weight "conflict" turned out to be a units mix-up (which unit is right is still unknown). Roof and tail math are corrected. There's a new energy budget, and answers to the v1 review.

**What I'm asking you:** Is this plan sound, safe, and right-sized? What would you change? The questions are in Section 9.

**Tags used throughout:**

- **[VERIFIED]** means a manufacturer or retailer page or manual was checked, and the source is named.
- **[CREDIBLE]** means a dealer listing, a spec database, or the team's 3D model study. Reasonable, but not confirmed.
- **[TEAM NOTE]** means it came from planning notes and wasn't re-checked today.
- **[ESTIMATE]** means it's a planning number, not a quote or a measurement.
- **[UNVERIFIED]** means it isn't published or hasn't been found.

Nothing has been bought, and there's no deposit on a coach.

---

## 1. The vehicle and the goal

**Vehicle:** An **East to West Alita 22NFT**, a small **Class C motorhome**. That means a living box built onto a van-style cutaway chassis, with a bed over the cab. The manufacturer's current page calls the floorplan **22NF**, and the two names refer to the same floorplan. The owner hasn't bought one yet. Example advertised price is about $110,995 [TEAM NOTE].

| Item | Value | Status |
|---|---|---|
| Chassis / engine | Ford Transit 350 AWD, 3.5 L EcoBoost V6 gasoline, 10-speed automatic | VERIFIED (brochure). One third-party listing shows 2WD for 2027, so check the VIN |
| Length / height / wheelbase | 26 ft 0 in / 11 ft 5 in / 178 in | VERIFIED |
| Width | Not published (the team's 3D model assumes 91 in) | UNVERIFIED |
| GVWR / GCWR | 11,000 lb max coach / 13,500 lb max coach plus towed car | VERIFIED |
| Axle ratings | Front 4,630 lb, rear 7,275 lb | VERIFIED |
| Cargo capacity (CCC) | Not published. One dealer unit's sticker read **1,765 lb** [TEAM NOTE]. A different dealer listing implies about 1,969 lb [CREDIBLE] | Read the yellow sticker on the actual coach |
| Tanks | Fresh 35 / grey 30 / black 30 / fuel 25 gal | VERIFIED |
| Generator | 4,000 W gasoline | VERIFIED |
| Alternator | 250 A | CREDIBLE (spec database for a 2024 Transit cutaway). Check the build sheet |
| Factory AC | 15,000 BTU ducted, heat pump, 14×14 in roof opening. The ceiling is already ducted | VERIFIED. **Being replaced** (Section 3.4) |
| Layout | Cab, cab-over bunk (60×80), dinette, kitchen (induction, 6 cu ft 12 V fridge), dry bath, rear office desk and queen **lift bed** with a "garage" space underneath | VERIFIED / dealer description |

**Goal:**

- **Who and how:** One person living and working in it **full-time**.
- **Work:** It's a **mobile office for remote video and creative editing**, with a seated desk, monitors, and Starlink satellite internet.
- **Off-grid:** It needs to **boondock** well (camp without hookups) using battery, solar, and alternator charging, with the generator as backup. Hot-weather use (Las Vegas, around 100°F) is a design case.
- **Laundry:** An **on-board washer-dryer is a hard requirement.**
- **Towing:** The owner will **flat-tow a manual Fiat 500 Abarth**. The hitch receiver is reserved for that.
- **Owner's rules:** Keep his design. Don't cut the washer. Prices only from real listings. Buy nothing without his go-ahead. **Tape-measure a real unit before any deposit.**

---

## 2. Quick glossary

| Term | Meaning |
|---|---|
| Boondocking | Camping with no hookups |
| House bank | Batteries for the living area, separate from the van's starter battery |
| 48 V system | A high-voltage battery bank. Less current for the same power, so thinner wires than 12 V |
| kWh | Energy. 1 kWh = 1,000 W for one hour |
| Inverter | Turns battery DC into 120 V household AC, losing about 10% |
| PV input | A solar input on the charge controller |
| Voc / Isc | A panel's highest voltage (no load) and highest current (shorted). Used for controller limits and fuse sizing |
| Max series fuse | The largest fuse the panel maker allows on one panel. It protects against current flowing backward into a faulted panel |
| Blocking diode | A one-way valve for current. Wastes a little power as heat |
| DC-DC charger | Charges the house bank from the alternator while driving (here, 12 V in, 48 V out) |
| SOC | State of charge (battery %) |
| BTU | Heating or cooling capacity |
| Ducted AC | Pushes air through ceiling ducts to several vents, instead of blowing from one box |
| Variable-speed compressor | Slows down once the coach is cool, using much less power than on/off units |
| Heat pump | An AC that also heats by running in reverse |
| Grey tank | Holds sink, shower, and washer water |
| GVWR / GAWR / GCWR / CCC | Max loaded weight / max per axle / max coach plus car / cargo capacity left after the empty weight |
| Lever arm | Weight hung behind the rear axle adds *more* than its own weight to the rear axle and lightens the front |

---

## 3. The build spec

### 3.1 Layout

| Area | Plan | Status |
|---|---|---|
| Cab, cab-over, dinette, kitchen | Stay as built | Decided |
| **Rear office** | Seated desk (29–30 in), **kneehole kept open** | Decided |
| **Washer-dryer** | **Splendide WDV2200XCD (vented)** in its own cabinet replacing the **bath-side drawer stack** (needs about 24 in of width), separate from the desk so the spin doesn't shake it. Raised counter on top for folding and charging. Dedicated 15 A circuit, hot and cold water, standpipe, and a short metal vent through the wall | Washer model decided. **Location open:** (A) bath side, as in the October 5 plan, or (B) rear garage under the lift bed. Both are rendered in the 3D studies (Section 6). The cabinet details here describe A |
| **RV5 power hub** | **Inside** (the 3D model puts it in the roadside desk pedestal, just behind the battery box, with the 48 V cable through the floor), or in a dry exterior bay. **Never in the sealed battery box**, because it needs about 7.87 in of open air around it | Decided rule. Exact spot to confirm |
| **Batteries** | Sealed box under the tail, by the spare tire (Section 3.3) | **Decided. Please check this choice** |
| Bluetti Epad (control screen) | At the desk or inside the entry | Planned |
| Finishes | Open | Open |

### 3.2 Electrical overview

```
 6 × Callsun 275 W (roof)
   ├─ 3 in parallel ─ 25 A fuse per panel ─ PV breaker ─► RV5 PV1
   └─ 3 in parallel ─ 25 A fuse per panel ─ PV breaker ─► RV5 PV2
 Alternator (12 V) ─ fuse at battery ─► 2 × Victron Orion-Tr Smart 12/48 (ignition-switched) ─► fuse ─► 48 V packs
 Shore (hardwired surge protector) / generator ─► transfer switch ─► RV5 AC input
 RV5 hub (inside) ◄─ short 48 V cable, fuse at the packs ─► 2 × B4810 in sealed tail box
   ├─ 120 V AC out (5,000 W): Chill Cube AC, washer (own 15 A breaker), induction, desk, Starlink
   └─ 12 V DC out: lights, pump, fans, fridge
 Main disconnect reachable without crawling under the coach
```

### 3.3 Batteries and power hub (Bluetti)

| Item | Spec | Status |
|---|---|---|
| **Bluetti RV5** hub (inverter, charger, and solar controller in one) | 120 V out 5,000 W. AC charging up to 5,000 W. Two solar inputs, each **12–50 V, 50 A, 1,800 W**. 48 V battery terminal 150 A max. 12 V DC out up to 1,360 W. 30.86 lb, 17.72 × 19.69 × 6.30 in. Needs **≥7.87 in of clearance** for air. **No published water rating.** Derates above 113°F | VERIFIED (RV5 manual) |
| **Bluetti B4810** × 2 | Each **5.12 kWh, 51.2 V, 100 Ah**, LiFePO4, **101.4 lb**, 23.94 × 14.96 × 5.71 in, **IP65**, self-heating to −4°F. Charge 50 A recommended / 100 A max | VERIFIED (B4810 manual) |
| Bank total | **10.24 kWh**, 202.8 lb. About 7.4 kWh usable as AC power after an 80% depth-of-discharge window and inverter losses | Capacity VERIFIED. Usable figure is an [ESTIMATE] |

**Decided placement: a sealed box under the tail, by the spare tire, packs only.**

- **Box:** The 3D model sizes it at about **52 × 18 × 7.5 in**, about 25 lb empty, with its bottom about 12 in above the ground. It sits between the spare and the hitch, **about 64 in behind the rear axle** [ESTIMATE]. At 64 in behind the axle it sits past the end of Ford's frame (37.35 in), so it bolts to the coach builder's **frame extension**, not welded. Confirm the extension's strength and bolt points at the walkthrough. Baffled vent, low-corner drain, lockable lid, skid protection. It mustn't cover dump valves, the exhaust, or spare access.
- **Why sealed:** The B4810 manual says IP65 but also "do not use in water; if wet, do not return to service." Bare packs in road spray are ruled out.
- **Why the hub stays out:** The RV5 needs about 7.87 in of air and has no water rating.
- **Axle effect** (static lever math, 178 in wheelbase, box 64 in behind the rear axle) [ESTIMATE until measured]:

| Load at the box | Rear axle | Front axle |
|---|---|---|
| Packs plus box, about 228 lb (as decided: 202.8 lb packs + about 25 lb box) | **+310 lb** | **−82 lb** |
| Packs only, 202.8 lb (for comparison) | +276 lb | −73 lb |
| Packs plus hub, 233.66 lb (if the hub were also at the tail) | **+318 lb** | **−84 lb** |

  v1 used 37.35 in, which is where Ford's frame ends, not where the spare is. Either way the added load is small next to the 7,275 lb rear rating. **Whether the rear axle stays under its rating depends on the coach's real axle weight, so weigh it.**
- **Known risks** (from the 3D study) [ESTIMATE]:
  - Departure angle at the box is about 9.3° vs 9.1° at the hitch.
  - Road spray and heat.
  - Self-heating in the cold needs power from somewhere (Bluetti to confirm).
  - Packs side by side need a box wider than the frame-rail gap, so they hang below or around the rails.

**Reviewer:** We've decided on this. Please **check the choice**. Is a sealed tail box sound for weight, water, heat, cold, and service, or would you move the packs?

### 3.4 Air conditioning: Furrion Chill Cube 18K (ducted, variable speed, heat pump)

| Item | Value | Status |
|---|---|---|
| Unit | **Furrion Chill Cube 18K**, variable-speed rooftop AC with heat pump, **ducted**, R32 refrigerant. Example part **#2025008216** (white). A black version is #2025008215 (reported 12k heating) | Part numbers VERIFIED: elkhartrvparts.com. Black-unit heating figure is [TEAM NOTE] |
| Cooling / heating | 18,000 BTU / 15,000 BTU (white model). Heat pump effective above about 40°F | BTU VERIFIED (Elkhart RV Parts). 40°F figure is [TEAM NOTE] |
| Compressor | **Variable speed, 30–100% output.** Lippert says no aftermarket soft start is needed in most installs, and claims cooling above 105°F outside | Variable speed VERIFIED (Furrion). 30–100% and the 105°F claim are [CREDIBLE], retailer quoting Lippert, not independently tested |
| Electrical | 115 V AC. Team research found a spec sheet max of **1,330 W / 11.6 A**, and owners report about **350–800 W** holding temperature | 115 V VERIFIED. Watts are [TEAM NOTE] |
| Size / weight | Fits the standard 14×14 in opening. Roof unit 29.5 × 29 × 14.5 in, **72.4 lb** | VERIFIED |
| Ducting | Feeds the coach's **existing ceiling ducts** through Furrion's **Chill Cube 18K ducted air distribution box with remote (FACT18VSDA-PS-AM, $165.19, sold separately)**. Wall thermostat FACW13VSDA-BL-AM ($105.80) is optional. Whether the box mates to East to West's duct layout needs a ceiling photo and Furrion's confirmation before buying | Part and price VERIFIED: elkhartrvparts.com. Fit UNVERIFIED |
| Price | **$1,329.00** (sale; regular $1,727.70), in stock (October 7) | VERIFIED: elkhartrvparts.com #2025008216. Furrion's own product page loaded on one check and returned "404 not found" on another |
| Power path | Runs through the RV5's 120 V inverter (about 10% loss). It shares the 5,000 W output with the washer (up to 1,300 W) and induction cooktop | — |

v1's plan (keep the factory Coleman unit, add a soft starter if it's a 2026 coach, and wait for a ducted 48 V Turbro that isn't sold) is **dropped**. There's no soft starter, no install kit, and no Turbro watch.

### 3.5 Solar (Callsun 275 W)

| Item | Value | Status |
|---|---|---|
| Panel | Callsun 275 W N-Type bifacial (CN275W/CS275W): Voc 25.26 V, Vmp 21.29 V, Imp 12.92 A, Isc 13.69 A, **max series fuse 25 A**, 68.35 × 30.16 × 1.38 in | VERIFIED: Callsun page and manual |
| Price / stock | **$249.99** each. **Sold out** as of October 7 | VERIFIED |
| **Weight** | **65.65 lb** on Callsun's page vs **29.8 lb** on a retailer listing. 29.8 kg = 65.7 lb, so this is **one number with the unit mislabeled in one place**, not two measurements. **Which unit is right is unknown.** Six panels weigh either **about 179 lb or about 394 lb** | UNVERIFIED. The box or label decides |
| Bifacial | Collects light from the back. **Useless on a flat roof.** If the panels are the heavy figure, that's weight for nothing | — |
| Array | **6 panels = 1,650 W.** Three in parallel on PV1, three in parallel on PV2 | Decided |

**Why this wiring:** Two in series = 50.52 V open-circuit at 77°F, over the RV5's 50 V limit, so series is out. Six on one input = 82.14 A, over 50 A. Three per input = **41.07 A short-circuit** and about 825 W.

**Panel action items:**

- Check the panel's box or label for the real weight.
- If it's 65.7 lb, and since they're sold out anyway, **consider a lighter panel with the same dimensions** and similar voltage and current, so it still fits the RV5's 12–50 V window and the fuse plan.

### 3.6 Roof fit (the number one measurement)

- v1's "17 ft × 60 in" figure **ignored the AC sitting mid-roof.** A 30.16 in panel can't fit beside a 29.5 in-wide AC on a coach about 91 in wide once edge and walk margins are taken.
- **2 × 3 layout** (two panels side by side, three rows deep, long side front-to-back): about **205 in** of panel length (3 × 68.35) **plus the AC footprint** and gaps [ESTIMATE].
- **One crosswise row** (panels across the roof): about **233 in** needed against **about 234 in** of flat roof (from the 3D model's estimate of the cab-over seam to the rear cap) [ESTIMATE]. That leaves essentially no margin. The 3D model splits it as three panels behind the AC and three ahead, with roof fans and the skylight under panels on taller brackets.
- **Roof length (cab-over seam to rear cap) and the AC opening's position are the first things to measure.** If the roof is short, the array shrinks.
- Also on the roof: a Starlink Mini dish beside the AC, a combiner box, and a sealed cable entry. Mounting hardware weight is an estimate (30–60 lb).

### 3.7 Fusing and protection (answers to the v1 questions)

- **Three in parallel with one 25 A fuse per panel is the standard fix.** If one panel faults, the other two can push about 27.4 A back into it. That's above 25 A, so the faulted panel's fuse blows, and that's exactly what it's for. **No blocking diodes needed.** They'd waste about 6 W each as heat [ESTIMATE]. Don't upsize the fuses past 25 A.
- **Callsun's written OK on three-in-parallel is nice to have, not a blocker.**
- **125% factor:** That safety factor sizes **wire and fuses**, not the controller's input rating. So 41.07 A against a 50 A input is fine **if** Bluetti's 50 A means the input tolerates 50 A of **short-circuit** current. **Ask Bluetti that directly.**
- **Battery cable:** Larger than 4 AWG (Bluetti); 2 AWG or bigger, as short as possible. Calculated drop at 150 A over 10 ft one-way is 0.47 V [ESTIMATE].
- **Fuse at the packs** on **any 48 V run longer than a couple of feet.** The tail box to an inside hub qualifies.
- **Hardwired surge protector on the shore-power inlet.**
- **Generator:** charge in its Standard or Silent mode, not Turbo, and set the RV5's grid-draw limit below what the generator can supply continuously.
- **Orion input fuse** at the starter battery, sized from the Orion manual.
- **Main disconnect** reachable without going under the coach.

### 3.8 Alternator charging

- **Two Victron Orion-Tr Smart 12/48-8A isolated** (ORI124838120), in parallel, under the passenger seat near the starter battery. Ignition-switched so they can't drain it. One 48 V run goes back to the packs.
- Each puts out about 360–430 W (about 760 W for two) and weighs 4 lb [VERIFIED: Victron manual]. Together they pull about 65 A from a **250 A alternator** [alternator rating CREDIBLE]. Price about **$244 each, about $490 for both** [TEAM NOTE, October 4; re-verify].
- **Battery % accuracy:** The Orions charge the packs directly, bypassing the RV5's meter. The packs talk to the RV5 over a data link, so their own battery management system **probably keeps the % accurate** [CREDIBLE, not confirmed by Bluetti].
- **If Bluetti says no to direct charging, the fallback is Option A:** three panels on PV1 (about 825 W) and the RV5's built-in alternator input on PV2 (600 W). No Orions.

### 3.9 Water and laundry

| Item | Value | Status |
|---|---|---|
| Washer-dryer | **Splendide WDV2200XCD, vented.** 120 V, 11 A, 1,300 W max class, 148 lb, 33⅛ H × 23½ W × 22⅝ D in. 15 lb wash / 11 lb dry. About **8 gal per normal wash** (7.5–16 gal range) | VERIFIED: Fisheries Supply listing |
| Price | **$1,512.81**, 2 in stock (October 7) | VERIFIED: fisheriessupply.com |
| Install needs | Dedicated 15 A circuit, hot and cold water, 1¼ in standpipe (top 25–34 in above the machine base), a short **metal** dryer vent through the sidewall, and a floor rated ≥280 lb | From Splendide's **ventless-model** manuals. **Re-check all of it in the WDV2200XCD manual**, plus vent diameter and maximum vent run |

**Why vented beat ventless:** The ventless model (WDC7100XC) uses about **2.5 gal of water per hour of drying** to condense the steam, on top of the wash water. All of it goes into a **30 gal grey tank**, so a single load could nearly fill the tank. The vented model dries with no water, at the cost of one wall vent.

**Laundry rule:** Grey-tank size decides **when** laundry runs, not **whether**. Wash when you can dump, and use campground laundry when the tanks are low. **The Splendide stays and isn't up for removal.**

### 3.10 Storage

- Cab-over, dinette, and kitchen storage stay.
- The hub takes part of the desk pedestal. With washer location A, the washer takes one drawer stack.
- The batteries leave the cabin, so the garage under the lift bed is freed for cameras, light stands, and luggage, unless the washer goes there (location B).
- Exterior bays (count and sizes unpublished) get hoses, tow-bar gear, blocks, and spares. The factory step-well is too small for a B4810.

### 3.11 Towing

- Manual Fiat 500 Abarth, flat-towed. The 2017 manual caps flat-towing at 65 mph. Curb weight is **2,491–2,512 lb** [VERIFIED].
- **Towing margin is tight but real unless the coach is loaded to its full GVWR.** GCWR is 13,500 lb and the car is 2,491–2,512 lb, so the coach can weigh at most about 10,988–11,009 lb while towing, minus the tow kit. In practice, **towing margin ≈ spare cargo capacity − 12 lb − tow kit.** With 160–450 lb of spare cargo (Section 4.2), that's about **150–440 lb before the tow kit.** Only a coach at the full 11,000 lb GVWR is over. Rule: **coach weight ≤ 13,500 − car − tow kit.** **Weigh the coach and car together.**
- Needs a base plate, tow bar, supplemental brake, and lighting. Hitch class and tongue rating come from the hitch label.

### 3.12 Ops gates (check on a real coach before any deposit)

| Gate | Check |
|---|---|
| **Tape and measure first** | No deposit or orders until a real unit is measured and the owner says go |
| **Roof length** (number one) | Cab-over seam to rear cap, plus the AC opening's position. One crosswise row needs about 233 in |
| **Washer location** | A: the bath-side drawer stack must be ≥ 24 in wide for the 23½ in washer and cabinet, with a wall for the vent. B: garage depth and height under the lift bed |
| **Cargo** | Yellow-sticker CCC and as-built axle weights (Section 4.2) |
| **Roof + AC** | Clear roof width and length with the Chill Cube in place. Photograph the ceiling duct assembly |
| **Tail** | Ground-to-frame height, spare position, receiver height, clear length from the rear axle to the bumper, and the frame extension's strength and bolt points. The box needs about 52 × 18 × 7.5 in with its bottom ≥12 in up |
| **Grey tank** | Size and location |
| **Year** | 2026 or 2027, coach and chassis. Affects specs and warranty paperwork. With the Chill Cube, a soft starter is no longer the issue |
| **Also** | Alternator rating, desk-pedestal size for the RV5, generator and transfer-switch make and location, body width |

---

## 4. Energy budget and weight

### 4.1 Energy budget (all ESTIMATE)

| Item | kWh/day |
|---|---|
| Editing workstation and monitors (250–400 W × 8 h) | 2.0–3.2 |
| Starlink Mini, always on (40–50 W rated) | 1.0–1.2 |
| Fridge (12 V) | 0.8–1.2 |
| Induction cooking | 0.8–1.5 |
| Lights, water pump, fans, device charging | 0.4–0.8 |
| RV5 standby and inverter overhead (30–60 W × 24 h; unpublished) | 0.7–1.4 |
| Laundry averaged over the week (about 2 loads) | 0.4–0.7 |
| **Daily use without AC** | **about 6–10** |
| **Solar, summer** (1,650 W × 5–6 sun hours × 0.70–0.75 for flat, hot panels) | **about 5.8–7.4** |
| **Solar, winter or cloudy** (2.5–3.5 sun hours) | **about 3–4.3** |
| Battery bank | 10.24 kWh nominal (about 7.4 kWh usable as AC) |

**What it means:**

- In summer, solar roughly covers daily life without AC, and the bank absorbs the swings.
- In winter or cloud it falls about **3–7 kWh/day** short. The gap gets made up by driving (about 0.72–0.76 kWh per hour from the two Orions), the generator (about 3 kWh per hour of charging), or hookups.
- **24/7 AC at 100°F doesn't work on solar and battery.**
  - At an assumed 1.2 kW average, AC alone is about 29 kWh/day.
  - That needs the **generator** (roughly 8–10 hours a day) **or hookups**.
- A mild-weather night at the Chill Cube's reported low end (about 350–550 W [TEAM NOTE]) is a different story; the bank can carry several hours of that.
- A single wash-and-dry cycle is about 1.5–2.5 kWh. Run it on sunny days or with the generator.

### 4.2 Weight (ESTIMATE)

| Item | lb |
|---|---|
| Build additions (batteries, box, hub, Orions, AC, washer, panels, mounts, cables, Starlink) | about 700 |
| Fresh water (35 gal × 8.3 lb) | about 290 |
| Personal gear | 300–400 |
| **Total against 1,765 lb CCC** | **leaves about 350–450 lb spare** |

**Important caveat:** The ~700 lb build figure comes from the 3D study, which used **29.8 lb per panel.** If the panels are actually **65.7 lb** each, add about **215 lb**, and spare capacity drops to about **160–260 lb**. The AC swap also only nets the difference between the Chill Cube (72.4 lb) and the factory unit, whose weight isn't known.

**Action:** Read the sticker, then **weigh the coach and car together** (per axle and combined).

---

## 5. Bill of materials

Prices are from real listings. **Many big items are still unpriced,** so the total covers **priced lines only**. No tax, shipping, or labor.

| # | Item | Qty | Unit | Line | Source / status |
|---|---|---|---|---|---|
| 1 | Bluetti RV5 hub | 1 | — | — | Unpriced (Bluetti kit price showed unavailable on October 6) |
| 2 | Bluetti B4810 5.12 kWh | 2 | — | — | Unpriced |
| 3 | Bluetti Epad | 1 | — | — | Unpriced |
| 4 | **Callsun 275 W panel** (or a lighter same-size substitute) | 6 | $249.99 | **$1,499.94** | VERIFIED list price, **sold out** |
| 5 | Combiner with per-panel 25 A fuses, PV breakers | 2 | — | — | Unpriced |
| 6 | Roof rack and mounts, sealed cable entry | 1 set | — | — | Unpriced |
| 7 | **Victron Orion-Tr Smart 12/48-8A** | 2 | ~$244 | **~$490** | TEAM NOTE, re-verify |
| 8 | **Furrion Chill Cube 18K ducted heat pump** (#2025008216) | 1 | $1,329.00 | **$1,329.00** | VERIFIED: Elkhart RV Parts, in stock |
| 8a | **Chill Cube 18K ducted air distribution box with remote** (FACT18VSDA-PS-AM) | 1 | $165.19 | **$165.19** | VERIFIED price: Elkhart RV Parts. Sold separately; confirm duct fit with Furrion |
| 8b | Furrion single-zone wall thermostat (FACW13VSDA-BL-AM), optional | 0–1 | $105.80 | — | Not in total |
| 9 | **Splendide WDV2200XCD** vented washer-dryer | 1 | $1,512.81 | **$1,512.81** | VERIFIED: Fisheries Supply, in stock |
| 10 | Washer install (bracket, standpipe, vent, 15 A breaker, water lines, cabinet) | — | — | — | Unpriced |
| 11 | Sealed tail battery box (fabricated, bolted) | 1 | — | — | Unpriced |
| 12 | 48 V cable (2 AWG+), fuse at the packs, main disconnect, Orion input fuse | — | — | — | Unpriced |
| 13 | Hardwired shore-inlet surge protector | 1 | — | — | Unpriced |
| 14 | Starlink **Mini** | 1 | — | — | Unpriced |
| 15 | Rear desk / pedestal work | — | — | — | Unpriced |
| 16 | Flat-tow kit for manual Abarth | 1 | — | — | Unpriced |
| 17 | Shop labor | — | — | — | Unknown |

**Priced lines total:** $1,499.94 + $490 + $1,329.00 + $165.19 + $1,512.81 = **≈ $4,996.94** (≈ $5,102.74 with the optional thermostat). That's a floor, not the build cost. The Bluetti hub and batteries, battery box, cabling, install, tow kit, and labor are probably most of the money.

**Cut as over-built:** Turbro weekly watch (dropped). Bluetti **Epanel** distribution panel (not needed). **Starlink Standard** (the Mini is enough).

---

## 6. Drawings and 3D renders

All drawings and renders are in repo **arthckr88/22NFT** (draft pull requests; none merged). JPG/PNG copies are in **`22nft-images/`** next to this file. **In a chat window, attach the images separately; they won't render from paths.**

### 6.1 Concept sheets (PR #1, October 6), `D-01.png` to `D-09.png`

These are 2D, not to scale, and stamped "concept, not for fabrication."

| File | Shows | Stale? |
|---|---|---|
| D-01 | Exterior elevations, tail-box candidate, keep-clear zones | OK as concept |
| D-02 | Underbelly plan, battery options color-coded | OK. The tail box is now the decided option |
| D-03 | Axle lever math | **Stale.** Uses 37.35 in (frame end), not about 64 in (spare) |
| D-04 | Tail enclosure concept | **Stale.** Draws the RV5 hub as possibly inside the box. The hub now stays out |
| D-05 | Electrical one-line, 3 + 3 parallel, per-panel ≤25 A fuses, Orion | Mostly current. Lacks the pack fuse and surge protector |
| D-06 | Roof packing test | **Stale.** Still shows the **factory 15,000 BTU (Coleman) AC**, not the Chill Cube |
| D-07 | Interior floor plan | OK on location: shows both washer locations, which are still open. Doesn't name the vented model |
| D-08 | Interior elevations | OK on location (A and B). Standpipe height is from the ventless manual; re-check |
| D-09 | Exterior storage map | OK as placeholders |

### 6.2 3D build study (PR #2, October 7 early morning), `PR2-*.jpg`

A Blender model with 12 renders (1920×1080) and 8 annotated views, plus axle and energy scenarios. Every location in it is ESTIMATE.

- `PR2-01`: exterior, three-quarter view with tow car
- `PR2-02`: side elevation
- `PR2-03`: roof plan (crosswise panels split around a mid-roof AC)
- `PR2-04`: tail and underbody
- `PR2-05`: ghosted power-system X-ray
- `PR2-06`: interior wide
- `PR2-07`: desk
- `PR2-08`: laundry option A
- `PR2-09`: laundry option B
- `PR2-10`: top-down floor plan
- `PR2-11`: chassis/axle side view
- `PR2-12`: night exterior
- Annotated versions: `PR2-02/03/04/05/08/09/10/11-annotated.jpg`

**Stale points in PR #2:**

- It places the **RV5 hub in the tail enclosure**. Now it stays out.
- It treats "all six parallel" as the topology, with 3 + 3 only as an alternative. 3 + 3 is the plan.
- It models **Starlink Standard**. The Mini is the pick.
- It shows **two washer locations** (still correct; location is open).

### 6.3 3D build book R1 (PR #3, October 7 late morning), `PR3-*.jpg`

A revised model, render book, and axle table. It puts the **RV5 in the desk pedestal** and the **packs in a 52 × 18 × 7.5 in box about 64 in behind the rear axle**, with Chill Cube, Starlink Mini, and Orions under the passenger seat.

- `PR3-01_exterior`
- `PR3-02_elevation`
- `PR3-03_roof`
- `PR3-04_underbelly`
- `PR3-04b_tail_section`
- `PR3-05_xray`
- `PR3-06_interior`
- `PR3-07_desk`
- `PR3-08_laundry_A`
- `PR3-09_laundry_B`
- `PR3-10_floorplan`
- `PR3-11_axles`
- `PR3-12_night`
- Annotated versions: `PR3-02/03/04/04b/05/08/09/10/11-annotated.jpg`

**Stale points in PR #3:**

- It uses **29.8 lb per panel** (179 lb total). If the panels are 65.7 lb, its roof and weight totals are about 215 lb light.
- Its axle figure for the tail box (+276 / −73) is packs only. With the box it's +310 / −82.

---

## 7. Build order

1. **Send the Bluetti email first.** Ask:
   - Can the Orions charge the B4810s directly?
   - Does the battery % stay accurate?
   - Is the 50 A PV input a short-circuit current limit?
   - Which battery-cable gauge, and what fuse at the packs?
   - Is underbody mounting OK for the packs?
   - What powers the self-heating?

   The answer sets **plan vs Option A**. The Callsun three-in-parallel question can go too, but it doesn't block anything.
2. **Earn and fund.** Financing is parked, no deposit.
3. **Tape-measure a real unit.** Roof length and AC position first, then the gates in Section 3.12. Read the yellow sticker.
4. **Go / no-go**, purchase, then **weigh coach and car**.
5. **Power core:** tail box with packs, a fuse at the packs, a short 2 AWG+ run to the RV5 inside, the main disconnect, and the Epad. Connect 12 V loads, then the transfer switch and **shore surge protector**.
6. **Roof:** once Furrion confirms the air distribution box fits the factory ducts, the Chill Cube in the 14×14 opening, then the rack, panels (3 + 3, 25 A per panel), combiner, PV breakers, and sealed entries with written roof-warranty coverage. Panels depend on stock or a lighter substitute.
7. **Orions** (or Option A wiring) with input fuses.
8. **Washer** at location A or B: cabinet, circuit, water, standpipe, metal vent (specs from the WDV2200XCD manual).
9. Desk and pedestal finish, **Starlink Mini**, then the **tow kit** and a final combined weigh.

---

## 8. Open risks

1. **The Bluetti answer.** The Orions charging the packs directly is undocumented. Option A is the fallback.
2. **Roof length.** One crosswise row needs about 233 in against about 234 in estimated. A short roof means fewer panels.
3. **Weight.** Spare cargo is about 160–450 lb depending on the true panel weight. Rear-axle margin is unknown until weighed. Towing margin is about the spare cargo minus 12 lb minus the tow kit, so roughly 150–440 lb before the kit. It's negative only at full GVWR.
4. **Panels sold out**, and possibly heavy (394 lb if 65.7 lb each) with a feature that's useless on a roof. If the label confirms the heavy figure, a lighter substitute is worth finding.
5. **Tail box.** Departure angle, spray, heat, cold-weather self-heating power, and service from underneath.
6. **Chill Cube duct fit** to the factory ceiling. Real power draw at 100°F isn't independently published.
7. **Hot-weather AC** depends on the generator. Is that acceptable for the Vegas use case?
8. **Laundry** limited by the 30 gal grey tank. Washer location A vs B is still open.
9. **Unpriced big items** (Bluetti hub and batteries, box, labor).

---

## 9. Questions for the reviewer

1. **Battery placement:** Check the decided sealed tail box (packs only, about 64 in behind the rear axle, hub inside). Is it sound? What would make you move it?
2. **Electrical safety:** Is **3 + 3 parallel with a 25 A fuse per panel and no diodes** right? Is a fuse at the packs, 2 AWG+ cable, a reachable disconnect, and a shore surge protector enough? Anything missing (for example a battery monitor, fire or thermal protection, ground-fault protection)?
3. **Sizing:** Does the energy budget (about 5–6.5 kWh/day use; about 5.5–6 summer and about 3 winter solar; 10.24 kWh bank) hold up for a full-time editor? Is 10 kWh enough, too little, or too much?
4. **AC:** Is the Chill Cube 18K through a 5,000 W inverter the right call? Is "generator or hookups for 24/7 AC at 100°F" an acceptable compromise?
5. **Weight:** Spare cargo is about 160–450 lb, and towing margin is about the same minus the tow kit. The coach must stay under 13,500 lb minus the car (2,491–2,512 lb) minus the tow kit. Is that enough margin? What would you cut or move?
6. **Washer location:** A (bath side) or B (rear garage)? Why?
7. **Panels:** Keep the Callsun 275s (if they come back) or switch to a lighter same-size panel? Any panel you'd suggest that fits the RV5's 12–50 V, 50 A inputs?
8. **Over-built / missing:** What else would you cut, and what's missing?
9. **Would you build it this way?** If not, what's your version, and what would you do first?

---

## Appendix: Key sources

- East to West 22NF floorplan: https://www.easttowestrv.com/alita/22NF/15661
- Bluetti RV5 manual: https://s4.bluettipower.com/bluetti/purchasePageBiz/2025/09/RV5%C2%A0User%20Manual%20US%20EN-1759160161231-e9c8.pdf
- Bluetti B4810 manual: https://s4.bluettipower.com/bluetti/purchasePageBiz/2025/09/B4810%20User%20Manual%20EU%20EN-FR-DE-1759213001764-45d1.pdf
- Callsun 275 W: https://callsunsolar.com/products/275w-n-type-bifacial-solar-panel
- Victron Orion-Tr Smart isolated manual: https://www.victronenergy.com/upload/documents/Orion-Tr_Smart_DC-DC_Charger_-_Isolated/34439-Orion-Tr_Smart_DC-DC_Charger-pdf-en.pdf
- Furrion Chill Cube 18K ducted heat pump (Elkhart RV Parts): https://elkhartrvparts.com/products/furrion-chill-cube-variable-speed-rv-rooftop-air-conditioner-18k-btu-heat-pump-ducted-2025008216
- Furrion product page (loaded on one check, 404 on another, October 7): https://furrion.com/products/furrion-chill-cube-variable-speed-rv-rooftop-air-conditioner-r32-18k-btu-ducted-chill-cube-18k-ducted
- Splendide WDV2200XCD (Fisheries Supply): https://www.fisheriessupply.com/splendide-wdv2200xcd-vented-combo-washer-and-dryer/wdv2200xcd
- Repo and PRs: https://github.com/arthckr88/22NFT/pull/1, /pull/2, /pull/3
