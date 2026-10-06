# Power equipment specs

Accessed 2026-10-06. Structured copy: [data/power.json](../data/power.json). Items that need a written answer from Bluetti are marked **AWAITING BLUETTI**.

## Bluetti RV5

Source: [RV5 User Manual V1.0](https://s4.bluettipower.com/bluetti/purchasePageBiz/2025/09/RV5%C2%A0User%20Manual%20US%20EN-1759160161231-e9c8.pdf) (CONFIRMED).

| Item | Published value |
| --- | --- |
| Weight | 30.86 lb (14 kg) |
| Size | 17.72 × 19.69 × 6.30 in (450 × 500 × 159.9 mm) |
| Battery terminal | 48 V, 150 A max in or out |
| AC output | 120 V, 42 A, 5,000 W, 60 Hz |
| AC charge | 5,000 W max. Rated AC input 120 V, 42 A. Bypass 50 A. Default grid-current limit 12 A, raised in the app up to 50 A |
| Solar | Two ports, PV1 and PV2. Each 12–50 V, 50 A, 1,800 W. Combined 3,600 W |
| Vehicle charge on PV2 | 600 W on a 12 V battery (12–14.4 V) or 1,200 W on 24 V, 50 A. The app chooses what PV2 does |
| DC output | 12 V at 100 A / 1,360 W, or 24 V at 60 A / 1,620 W, at the 95 F row |
| Operating temperature | −4 F to 113 F, with load derating from 113 F to 131 F. Storage −4 F to 131 F. Altitude ≤ 2,000 m. Humidity 95% max |
| Certification line | UL458 |
| Clearance | At least 8 in (20 cm); the figure is drawn at ≥ 200 mm / 7.87 in |
| Mounting | Round holes for floor mounting in an RV. Keyhole slots are for stationary walls and are not for moving vehicles |
| IP rating | **Not in the spec table.** AWAITING BLUETTI |
| Two B4810 packs | Manual recommends two B4810 packs (10 kWh) for full output and says a single pack limits the load. The extracted sentence does not give the single-pack watt limit. AWAITING BLUETTI. Stacking more than four B4810 units can damage the case |

The manual says not to install the hub under pipes or where water collects, not to block the fan, and to use the shortest, thickest cables that fit. Section 4.3 lists gauge bands of 6–8 AWG, 2–4 AWG, and 0–4 AWG, and fuse notes of about 200 A (about 1.5× current), a built-in AC-input fuse, about 75 A, and “no fuse needed with the B4810.” The PDF table’s rows do not stay aligned in text extraction, so this package does **not** assign a gauge to a port from that scrambled table. AWAITING BLUETTI for the battery-cable row on a remote run.

At 95 F the manual’s lab row allows 5,000 W AC charge and 3,600 W DC charge. At 131 F those fall to 5,000 W AC charge, 3,000 W DC charge, and 4,000 W AC discharge. An underbody box in summer has to be judged against that derating, not against the 5,000 W headline.

## Bluetti B4810

Source: [B4810 user manual](https://s4.bluettipower.com/bluetti/purchasePageBiz/2025/09/B4810%20User%20Manual%20EU%20EN-FR-DE-1759213001764-45d1.pdf) (CONFIRMED). The copy fetched is the EU English/French/German edition. A US English file on a distributor site carries the same English spec block.

| Item | Published value |
| --- | --- |
| Capacity | 5.12 kWh, 51.2 V, 100 Ah |
| Weight | 101.4 lb (46 kg) |
| Size | 23.94 × 14.96 × 5.71 in (608 × 380 × 145 mm) |
| IP | IP65 |
| Charge and discharge ambient | −4 F to 131 F |
| Self-heating | Built in. The manual says it works down to −4 F. Heater watts and whether the heater needs an external source are not in the spec table. AWAITING BLUETTI |
| Voltage | 40–58.4 V |
| Charge current | 50 A recommended, 100 A max |
| Discharge | 100 A max, 200 A for 30 s |
| Cycles | 6,000 to 70% at 0.5C and 77 F |
| Cable | Larger than 4 AWG or 20 mm². No washers between the lug and the terminal bolt |
| Parallel | Up to 24. More than eight need an Edock. Two packs are inside the no-Edock range. Voltage match within 0.3 V before paralleling |

The same manual says: do not use the pack in water; if it gets wet, stop and do not put it back in service after drying; keep it off oil and dirt; give it airflow; install it clean, dry, and ventilated. IP65 (jets) and “do not use in water” are both in the document. An open mount beside the spare fails the second sentence. A sealed, drained, ventilated box is the reading that satisfies both.

“Do not invert or stack during unloading” is a handling line. The RV5 manual allows operating stacks of up to four B4810s. Operating orientation other than the bracketed install is AWAITING BLUETTI.

Two packs: **202.8 lb**, footprint of one pack 23.94 × 14.96 in, thickness 5.71 in. Stacked thickness 11.42 in, which is only the cases, before brackets, air, or the hub.

## Callsun 275 W

Source: [Callsun product page](https://callsunsolar.com/products/275w-n-type-bifacial-solar-panel) (CONFIRMED for the electrical table and the manufacturer weight).

| Item | Value |
| --- | --- |
| Pmax | 275 W |
| Vmp / Imp | 21.29 V / 12.92 A |
| Voc / Isc | 25.26 V / 13.69 A |
| Size | 68.35 × 30.16 × 1.38 in |
| Weight on that page | **65.65 lb** |
| Conflicting weight | **29.8 lb** on a retailer listing of the same panel family |
| Max series fuse | 25 A |
| Max system voltage | 1,000 V DC |
| IP | IP68 |
| List price | $249.99, marked Unavailable on 2026-10-06 |
| Temperature coefficient | Not in the spec table fetched |

Six panels, all parallel on **one** RV5 port:

- Voc stays 25.26 V at STC, inside 12–50 V.
- Isc is 6 × 13.69 = **82.14 A**, over the **50 A** port limit.
- Power is 6 × 275 = **1,650 W**, under 1,800 W. Current binds before power.

Three and three, each group parallel, PV1 and PV2 both used as solar:

- Isc 41.07 A per port, under 50 A.
- Power 825 W per port.
- 3 × 13.69 × 1.25 = **51.3 A** if a 125% PV current factor is applied on top of the port rating. Whether Bluetti’s 50 A already includes that margin is AWAITING BLUETTI.

Two panels in series: 2 × 25.26 = **50.52 V** at STC, already over the 50 V maximum, before any cold-weather rise. Series is incompatible with this hub on the published numbers. Parallel is the configuration that fits, and it has to be split across both solar ports.

The weight conflict is left standing. Six panels are either 393.9 lb or 178.8 lb. The budget tool shows both.

## Victron Orion for this alternator

The chassis is 12 V. Charging a 48 V bank from it needs a 12 V to 48 V charger.

Published match: **Orion-Tr Smart 12/48-8A isolated**, part **ORI124838120**. From the [Victron isolated Orion-Tr Smart manual](https://www.victronenergy.com/upload/documents/Orion-Tr_Smart_DC-DC_Charger_-_Isolated/34439-Orion-Tr_Smart_DC-DC_Charger-pdf-en.pdf):

- 12 V-input models: **1.8 kg (4 lb)**, **130 × 186 × 80 mm**
- Output of the 12/48-8 column: **48.2 V** nominal, adjustable, **430 W** at 25 C, **360 W** at 40 C, **8 A** continuous at 40 C
- Terminals accept up to **16 mm² (AWG 6)**
- IP43 on the electronics, IP22 on the connection area
- Multiple units may be paralleled

The Orion XS 12/12 is the wrong direction for a 48 V bank. It is the right product only if someone were charging a 12 V battery.

One 12/48-8A is a small charger next to a 10 kWh bank (360 W is about 14 hours for 5 kWh, ignoring losses, as a scale check: 5,000 Wh / 360 W ≈ 13.9 h). The RV5’s own PV2 vehicle input is 600 W at 12 V, but it consumes PV2. This build keeps PV2 for solar and uses the Orion for the alternator. How many Orions the Transit alternator can feed is OPEN: the cutaway alternator amp rating was not found. Transit smart-alternator voltage often sits near 13.5 V, so engine-run detection needs the engine-run wire or a lowered threshold (see comparables).

## Splendide

Both current RV combo models publish **148 lb** and a separate **15 A** / 120 V circuit. Max absorbed power **1,300 W**.

| | WD2100XC (vented) | WDC7100XC (ventless) |
| --- | --- | --- |
| Manual size | 23.4 in W × 33.25–33.75 in H × 22 in D | same |
| Data sheet size | 23.4 × 33–33.4 × 22.6 in | same |
| Amps | IOM 10.5 A; data sheet 11 A | same conflict |
| Vent | Metallic duct, as short as possible. Makeup air if a cabinet door is fitted | No dryer vent. Condenser. Splendide’s product page: **2.5 gal of water per hour** of dry time |
| Water per wash | — | Product page: **7.5 to 16 gal** per load |
| RV note in the manual | Put it over the axles or midship. Block it. Floor must hold **280 lb**. SecureFit bracket MK01 is the named kit | same |
| Standpipe | 1-1/4 in minimum, top 25–34 in above the bottom of the machine | same |

Model choice is OPEN. The ventless machine does not pierce the wall and does spend fresh water while it dries. The vented machine needs a metal duct that does not dump into the underbelly. A 35 gal fresh tank and a 30 gal gray tank make a 16 gal wash plus condenser water a large fraction of both tanks.

## Starlink (model OPEN)

| Kit | Dish weight | Dish size | Source |
| --- | --- | --- | --- |
| Mini | 2.43 lb without kickstand; 2.56 lb with kickstand; 3.37 lb with kickstand and 15 m cable | 11.75 × 10.2 × 1.45 in | [Mini spec sheet](https://starlink.com/public-files/specification_sheet_mini.pdf) |
| Standard (older sheet) | 6.4 lb without cable; 7.9 lb with 50 ft cable | Rectangular phased array; sheet shows 20.2 in and 11.9 in callouts on the drawing | [Standard specifications PDF](https://api.starlink.com/public-files/Starlink%20Product%20Specifications_Standard.pdf). That sheet also lists average power **50–75 W** for that generation. Do not apply 50–75 W to the Mini; its draw was not on the Mini sheet fetched |
| Standard 4 X | Package 14.83 lb. Kit line 6.4 lb, 7 lb with kickstand, 8.3 lb with kickstand and 15 m cable. IP67 | [Standard 4 X sheet](https://api.starlink.com/public-files/specification_sheet_standard.pdf) | |

Which terminal goes on the roof is OPEN. D-06 draws both footprints as alternates.

## Generator tie-in and shore

The RV5 charges from a 120 V generator on the AC input and stops at full. It wants a 3-pin inlet that is not in the box. If the coach generator is the Flex Power 4000i, that machine is published at **4,000 W** on gasoline, **3,800 W** on LP, **117–120 V**, **33.3 A**, which is inside the RV5’s 5,000 W / 42 A AC input. Confirm the installed generator is 120 V only and not a 120/240 set. Shore inlet amperage of the coach (30 A or 50 A) was not published. The RV5 default of 12 A will not fill the bank quickly; raising it in the app cannot exceed the pedestal or the coach inlet.
