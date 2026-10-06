# Enclosure requirements

For options b, c, d, and e. Option a is ruled out as a bare install. This is a requirements list, not a fabrication drawing. D-04 is the concept of the tail box. Nothing here is approved for cutting metal until the field sheet is filled in.

## What the box is protecting

The B4810 is IP65 and the manual still says to keep it dry, out of water, and out of oil and dirt, and to ventilate it. The RV5 manual says not to put the hub where water collects, to leave at least **7.87 in** around it, and to keep the fan clear. The RV5 has **no published IP rating** (AWAITING BLUETTI). The Orion-Tr Smart is IP43 on the electronics and IP22 at the terminals, and Victron says to install it dry.

Target for the box, as a planning statement rather than a certified rating: the interior stays dry in rain and road spray (a sealed shell with a labyrinth or downward vent, not an open belly hole), and water that gets past the door drains out instead of pooling on the packs. Do not claim the box is IP65. The packs already are, and the hub may not be.

## Heat, cold, and the heater

B4810 charge and discharge ambients are **−4 F to 131 F**, with self-heating. Heater watts are not published (AWAITING BLUETTI). The RV5 derates DC charge at **131 F** (3,000 W versus 3,600 W at 95 F) and AC discharge (4,000 W versus 5,000 W).

So the box has two opposite jobs:

- In winter, the packs need enough insulation that self-heating can hold them above the cutoff, and a path for the heater’s watts. Do not add a second heater until Bluetti says the internal one is not enough and what may power it. The DIYvan van-box pattern (50 W pads, a controller, foam, Thinsulate caps) is a reference design for packs that do **not** already heat themselves. Copying it onto a B4810 without the heater spec risks heating a pack that is also heating itself.
- In summer, the RV5’s fan needs an intake and a discharge that are not the same hole, and the box cannot become a closed oven on asphalt. A fully sealed box with the hub inside fights the 7.87 in airflow note. Practical split, left OPEN: packs in the sealed underbody box, hub in that box only if a ducted fan can meet the clearance, otherwise hub in the driest nearby compartment (option f) with a short 48 V run. The brief wants both out of the cabin. It does not require them in one shell.

Insulation thickness is not specified. Any number would be a guess.

## Vibration, drainage, corrosion

- Bolt the packs with the **fixed mounting brackets** in the B4810 kit. The RV5 uses its **round** floor holes in a vehicle, not the keyhole slots.
- Isolate with a rubber pad. Thickness is not specified.
- Drain the shell at its low aft corner, with a duckbill or a short tube aimed away from the packs. A drain that cannot clog is part of the water requirement.
- Dissimilar metals: aluminum box, steel frame, copper lugs. Isolate the bolted joints and use a joint compound on lugs. The van build used Sikaflex 221 on aluminum seams; that is one owner’s sealant, not a specification for this coach.
- Road film will sandblast the lowest surface. A skid plate or a turned-up leading edge belongs on any tail box. Height of that plate is a departure-angle measurement.

## Frame attachment

**Bolted, not welded,** as the planning default.

Ford’s 2023 BEMM discusses welding, boron steel, and no-drill zones, and it specifies M12 grade 10.9 hardware and torques for the **rear frame extension adapter** (66.4–76 ft-lb on the hardware in that figure). Those torques are for Ford’s extension joint, not a license to drill the rail wherever a box wants a hole. Use existing body-mount holes or a bracket that clamps the rail only after the no-drill zones are checked on the unit. A weld is a chassis-warranty question for the Ford dealer and for Forest River. This file does not claim the warranty is void, and it does not claim a weld is acceptable.

The Kelderman center-to-center figure (35.400 in) is not a bolt pattern. D-04 leaves the bolt spacing as “field measure.”

## Service, lock, fusing

- A hinged door large enough to torque the M8 terminals and to pull one pack without dropping the box.
- A lock. Slam latches on the coach’s baggage doors are not a battery lock.
- RV5 manual: “no fuse needed with the B4810” in the scrambled 4.3 table, and also a ~200 A note at about 1.5× current for a battery connection in that same table. Those two lines have to be reconciled in writing (AWAITING BLUETTI) before a remote underbody run is fused. A disconnect you can open without lying under the coach belongs in the circuit even if the pack-to-hub fuse is waived. Location OPEN: in the box, reachable from the door, not buried behind a pack.
- Orion: Victron’s terminal size caps the cable at AWG 6. A fuse on the 12 V input is required by ordinary DC-DC practice; the exact amp value follows the Orion manual’s input current once the number of units is chosen. One 360 W unit at 12 V is on the order of 30–40 A before efficiency, which is why the alternator rating matters. Input amps are not printed as a single number in the extract used here, so the fuse amp is not filled in.

## 48 V cable and voltage drop

B4810: cable **larger than 4 AWG** (20 mm²). RV5: shortest and thickest, with 0–4 AWG appearing in the gauge list and the row assignment unconfirmed.

Drop below is **calculated**, not measured on a cable. Solid-round copper at 20 C, diameter from the ASTM B258 AWG formula, resistivity \(1.724 \times 10^{-8}\ \Omega\cdot\mathrm{m}\). Stranded cable at operating temperature is higher. Round trip, \(V = 2 I R L\).

Current cases: the terminal maximum **150 A**, and 5,000 W / 51.2 V = **97.7 A**.

| Cable | Ω per 1,000 ft (this calculation) | 10 ft one-way at 150 A | 15 ft one-way at 150 A |
| --- | --- | --- | --- |
| 4 AWG | 0.248 | 0.75 V (1.5% of 51.2 V) | 1.12 V (2.2%) |
| 2 AWG | 0.156 | 0.47 V (0.9%) | 0.70 V (1.4%) |
| 1/0 | 0.098 | 0.29 V (0.6%) | 0.44 V (0.9%) |
| 2/0 | 0.078 | 0.23 V (0.5%) | 0.35 V (0.7%) |

4 AWG is the size the B4810 manual says to exceed. On a 10–15 ft run at 150 A it is still a small percentage of 51.2 V in this 20 C solid-wire model, and it is the wrong side of the manual’s “larger than 4 AWG.” Use 2 AWG or larger for the pack-to-hub run, keep it short, and confirm the row with Bluetti. Run length itself is a field measurement (D-05). The percentages are not a code pass/fail. The manual’s instruction is “shortest and thickest,” which is stricter than a 3% habit of thumb.

Solar homeruns are in the 6–8 AWG band in the same scrambled table. Six panels at 82 A cannot share one conductor into one port anyway. Each group of three at 41 A of Isc wants its own fused pair, sized when the breaker rating is confirmed.

## What the tail box is not allowed to cover

Dump valves, generator exhaust, and the spare, unless the spare is relocated under option c and the new spare location is itself clear of the tow bar. Exhaust heat is called out in the Transit underbody discussions as a reason boxes get cooked. The generator bay location is unknown, so D-04 shows the exhaust as a no-build zone rather than as a located pipe.
