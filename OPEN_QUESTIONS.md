# Open questions

Nothing in this list is decided. Tradeoffs live in [analysis/underbelly-options.md](analysis/underbelly-options.md) and [analysis/interior-layout.md](analysis/interior-layout.md).

## Your decisions

1. Washer location: bath side, or the rear lift-bed cavity. Splendide’s own RV note prefers the axle or midship. The rear adds 148 lb on the same lever as a tail battery box.
2. Washer model: vented WD2100XC (metal duct through a wall) or ventless WDC7100XC (no duct, about 2.5 gal of water per hour of drying, 7.5–16 gal per wash, against a 35 gal fresh tank and a 30 gal gray tank).
3. Rear desk: under the lift bed, instead of the lift bed, or beside it. Interior width is unpublished, so “beside it” may not fit.
4. Battery placement among the conditional options (sealed tail box, spare well after a legal spare move, between the rails, split packs, an existing bay). Bare packs in the spray, a hitch box, and roof batteries are ruled out.
5. If the tail box cannot also give the RV5 its 7.87 in of air, the hub moves to a sealed bay and the packs stay aft. That split is open.
6. Spare tire: leave it and build beside it, move it to the rear wall, or move it to a cradle forward of the axle. A hitch or bumper carrier is ruled out because of the Fiat.
7. Enclosure material: aluminum, following the van spare-well build, or steel, following the commercial van box. No quote either way.
8. Starlink generation: Mini or a Standard kit. Weights and footprints differ. See [research/bluetti-specs.md](research/bluetti-specs.md).
9. How many Orion-Tr Smart 12/48-8A chargers. One is 8 A and about 360 W at 40 C. The chassis alternator’s amp rating was not found.
10. Which Callsun weight is real: 65.65 lb on the maker’s page or 29.8 lb on a retailer listing. The difference on six panels is 215.1 lb.
11. Whether a soft-start single-speed compressor is a reason to walk away. The published feature is “Soft Start 15,000 BTU Ducted A/C w/ Heat Pump.” That wording does not establish a variable-speed compressor.
12. Model year of the Fiat, because the flat-tow speed limit in the 2017 manual is 65 mph and earlier manuals say any legal highway speed. Automatics are not flat-towable.

## Ask Bluetti in writing

1. What is the RV5’s ingress rating, and is an underbody enclosure an approved location?
2. Section 4.3’s wire table does not survive PDF extraction. Which gauge row is the 48 V battery cable, and does “no fuse needed with the B4810” still hold on a remote run of 10–15 ft?
3. What PV breaker or fuse do you require ahead of each PV input for a parallel array of Callsun 275 W panels (Isc 13.69 A, max series fuse 25 A)?
4. May PV1 and PV2 both be solar while a Victron Orion-Tr Smart 12/48 charges the bank directly, so PV2 is not used as the vehicle input?
5. B4810 self-heating: watts, what powers the heater, and the lowest ambient at which it will start.
6. Approved operating orientation in a moving vehicle. The unloading line says not to invert the pack. Is a long-side-down or short-side-down mount approved?
7. The manual says one B4810 limits output and two are recommended. What is the continuous AC limit on one pack, and on two?
8. Maximum Ethernet length from the RV5 to a B4810 and to the Epad.
9. Does a fabricated enclosure, or a bolted frame bracket, affect the warranty?
10. Confirm the single-pack sentence that was cut off in the extracted manual, and whether stacking two packs (11.42 in of cases) is an approved vehicle orientation.

## Physical measurements

The full tape list is [FIELD_MEASURE.md](FIELD_MEASURE.md). The ones that change the design:

- Yellow sticker: UVW, CCC, as-built axle weights.
- Rear overhang of the body behind the rear axle.
- Ground clearance at the lowest point and at the tail, and the departure angle.
- Inside frame-rail gap, and the free rectangle beside and behind the spare.
- Generator bay, exhaust path, and dump-valve positions.
- Which rooftop unit is installed, and whether the compressor is variable-speed.
- Interior width, ceiling height, and the clear height under the lift bed.
- Every baggage door: width, height, depth, and which side of the axle it sits on.

## Tow

- Hitch class and tongue rating from the hitch label, not from the 4,000 lb tow line.
- Scale ticket for the coach and the Abarth together against GCWR 13,500 lb. At a coach loaded to GVWR, only 2,500 lb of combined headroom remains, and published Abarth curb weights are 2,491 lb and 2,512 lb.
- Base plate, tow bar, supplemental brake, and lighting that match a manual 500 Abarth, and confirmation the receiver is free.
