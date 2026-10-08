# Alita 22NFT build book, model R1

Renders in `renders/`, annotated views in `renders/annotated/`, model in `model/`.

## Specs

| Item | Value | Status | Source |
| --- | --- | --- | --- |
| Coach overall length | 26 ft 0 in (312 in) | Confirmed | https://easttowestrv.com/alita/22NF/13304 |
| Coach overall height | 11 ft 5 in (137 in) | Confirmed | https://www.fraserway.com/product-east-to-west/alita-motor-home-class-c/22nf |
| Coach body width | 91 in modelled | ESTIMATE | Not published by East to West |
| Interior height | 81 in | Confirmed | https://www.rvguide.com/specs/east-to-west/class-c/2026/alita/22nf.html |
| Wheelbase | 178 in | Confirmed | https://easttowestrv.com/alita/22NF/13304 |
| Front overhang (bumper to front axle) | 40 in modelled | ESTIMATE | Transit cab geometry; not published for 22NFT |
| Rear overhang (rear axle to rear wall) | 94 in (312 - 178 - 40) | ESTIMATE | Derived from the two values above |
| GVWR / GCWR | 11,000 / 13,500 lb | Confirmed | https://www.fraserway.com/product-east-to-west/alita-motor-home-class-c/22nf |
| Axle ratings | Front 4,630 lb, rear 7,275 lb | Confirmed | https://www.fraserway.com/product-east-to-west/alita-motor-home-class-c/22nf |
| Dealer-listed weight (2027 unit) | 9,031 lb, about 1,969 lb CCC | Credible | https://www.couchsrvnation.com/east-to-west/class-c-motorhome/alita/22nft1 |
| Tanks | 35 fresh / 30 grey / 30 black / 25 fuel gal | Confirmed | https://www.fraserway.com/product-east-to-west/alita-motor-home-class-c/22nf |
| Propane | 2 tanks, 9.4 gal total | Confirmed | https://www.rvguide.com/specs/east-to-west/class-c/2026/alita/22nf.html |
| Generator | 4,000 W, gasoline | Confirmed | https://www.fraserway.com/product-east-to-west/alita-motor-home-class-c/22nf |
| Awning | 16 ft Girard legless, LED strip | Confirmed | https://www.fraserway.com/product-east-to-west/alita-motor-home-class-c/22nf |
| Beds | Rear queen lift bed 60 x 80, cabover 60 x 80 | Confirmed | https://www.fraserway.com/product-east-to-west/alita-motor-home-class-c/22nf |
| Floorplan order | Front dinette, galley curbside, bath across, rear office + lift bed + garage | Credible | https://www.autoevolution.com/news/the-2026-alita-22nft-is-a-compact-motorhome-with-a-very-surprising-layout-259965.html |
| Exact cabinet positions, door location | Modelled from the floorplan order above | ESTIMATE | No dimensioned floorplan published |
| Flat roof length (cabover seam to rear cap) | 234 in modelled | ESTIMATE | Not published |
| Existing roof fixtures | 1 AC, 2 fans, 1 shower skylight, 12V panel modelled | ESTIMATE | Not published; typical Class C |
| Floor height above ground | 36 in modelled | ESTIMATE | Not published |
| Frame rail bottom above ground at tail | 19 in modelled | ESTIMATE | Not published for this chassis |
| Transit cutaway alternator | 250 A | Credible | https://specs2.auto123.com/en/specs/ford/transit-cutaway/ford-transit-cutaway-2024-t-350-rwd-156-9500-gvwr-srw-449769 |
| Rear wheels | Dual rear wheels, 27.5 in tire diameter modelled | ESTIMATE | Implied by 7,275 lb rear axle rating |
| Bluetti B4810 (each) | 23.9 x 15.0 x 5.7 in, 101 lb | Confirmed | https://solarpowersupply.eu/bluetti-b4810-battery |
| Bluetti RV5 hub | 17.7 x 19.7 x 6.3 in, 30.9 lb | Confirmed | https://bestecosolar.com/product/bluetti-rv5-power-hub/ |
| Callsun 275W panel (each) | 68.35 x 30.3 x 1.38 in, 29.8 lb | Confirmed | https://callsunsolar.com/products/275w-n-type-bifacial-solar-panel |
| Victron Orion-Tr Smart 12/48-8A (each) | 186 x 130 x 80 mm, 1.8 kg (4.0 lb) | Confirmed | https://www.akkuman.de/shop/Victron-Orion-Tr-Smart-12-48-8A-DC-DC-Ladegeraet-48V |
| Furrion Chill Cube 18K ducted | 29.5 x 29 x 14.5 in, 72.4 lb | Confirmed | https://elkhartrvparts.com/products/furrion-chill-cube-variable-speed-rv-rooftop-air-conditioner-18k-btu-heat-pump-black-ducted-2025008215 |
| Splendide WDV2200XCD | 23.5 W x 33.1 H x 22.6 D in, 148 lb | Confirmed | https://www.fisheriessupply.com/splendide-wdv2200xcd-vented-combo-washer-and-dryer/wdv2200xcd |
| Starlink Mini | 11.4 x 9.8 x 1.4 in, 2.4 lb, 40-50 W typical | Confirmed | https://www.usmobile.com/blog/starlink-mini-vs-standard/ |
| Starlink Standard (alternative) | 23.4 x 13.4 x 1.6 in, 7.05 lb, 75-100 W typical | Confirmed | https://www.usmobile.com/blog/starlink-mini-vs-standard/ |
| Fiat 500 Abarth (manual) | 144.4 L x 64.1 W x 58.7 H in, 90.6 in WB, 2,512 lb | Confirmed | https://www.fiat500usa.com/2018/02/2018-fiat-500-and-500-abarth-specs.html |
| Battery box | 52 x 18 x 7.5 in, about 25 lb empty, bottom 12 in above ground | ESTIMATE | Sized around two B4810s |
| Lift bed lowered underside | 38 in above floor modelled | ESTIMATE | Not published |

## Components

### Bluetti B4810 x2

- **Location:** Underbelly at the tail, between the spare tire and the hitch
- **Why there:** Out of sight, frees cabin storage, weight on the higher-rated rear axle
- **Dimensions:** 23.9 x 15.0 x 5.7 in each, side by side in a 52 x 18 x 7.5 in box
- **Clearances:** 12 in ground clearance (estimate)
- **Weight:** 202 lb packs + about 25 lb box
- **Service access:** Drop the box lid from below; disconnect at the box
- **Risks:** Departure angle 9.3 deg at the box vs 9.1 deg at the hitch; road spray; cold-weather self-heating needs incoming power (Bluetti to confirm)

### Bluetti RV5 hub

- **Location:** Roadside desk pedestal, on the side wall
- **Why there:** Directly above the batteries, keeps the kneehole open
- **Dimensions:** 17.7 x 19.7 x 6.3 in
- **Clearances:** Pedestal is 18 in wide x 24 in deep
- **Weight:** 30.9 lb
- **Service access:** Pedestal door; display faces into the cabinet
- **Risks:** Needs airflow: vent the pedestal toe-kick and back

### Callsun 275W x6

- **Location:** Roof, 3 behind the AC and 3 ahead of it, crosswise
- **Why there:** Six is the RV5's limit in parallel (41.1A of 50A per input)
- **Dimensions:** 68.35 x 30.3 x 1.38 in each
- **Clearances:** About 11.3 in each side to the roof edge; 2.5 in over vents
- **Weight:** 29.8 lb each, 179 lb total
- **Service access:** Walkable roof edges both sides
- **Risks:** Flat roof length is the open question; vents under panels

### Roof combiner

- **Location:** Between the rear panel group and the AC
- **Why there:** Shortest panel leads
- **Dimensions:** 6.5 x 10 x 4 in modelled
- **Clearances:** -
- **Weight:** In the 60 lb mounts/cable allowance
- **Service access:** Lid on the roof
- **Risks:** Seal the roof entry gland

### Victron Orion-Tr 12/48-8A x2

- **Location:** Under the passenger seat
- **Why there:** Close to the starter battery; 48V carries the long run
- **Dimensions:** 186 x 130 x 80 mm each
- **Clearances:** -
- **Weight:** 1.8 kg each
- **Service access:** Seat base panel
- **Risks:** Wire the remote to ignition; fuse at the starter battery

### Furrion Chill Cube 18K

- **Location:** Existing 14x14 opening, mid-roof
- **Why there:** Variable speed, heat pump, keeps the ducted ceiling
- **Dimensions:** 29.5 x 29 x 14.5 in
- **Clearances:** Starlink and a walkway beside it
- **Weight:** 72.4 lb
- **Service access:** Shroud off on the roof
- **Risks:** Ducted air box has to meet East to West's duct runs

### Starlink Mini

- **Location:** Roadside margin beside the AC
- **Why there:** Lowest draw and smallest footprint
- **Dimensions:** 11.4 x 9.8 x 1.4 in
- **Clearances:** Clear sky view over the panels
- **Weight:** 2.4 lb + mount
- **Service access:** Bolt-down flat mount
- **Risks:** Cable entry shares the combiner gland

### Splendide WDV2200XCD

- **Location:** Option A bath side, or option B rear garage
- **Why there:** Vented: no tank water to dry
- **Dimensions:** 23.5 W x 33.1 H x 22.6 D in
- **Clearances:** Needs about 24 in of width
- **Weight:** 148 lb
- **Service access:** Front service; slide out on rails
- **Risks:** Vent hole in the wall; B needs bed-down clearance

### Transfer switch

- **Location:** Under the curbside bench
- **Why there:** Joins generator and shore before the RV5
- **Dimensions:** 6 x 6 x 8 in modelled
- **Clearances:** -
- **Weight:** small
- **Service access:** Bench lid
- **Risks:** Confirm the coach's existing switch can be reused

## Laundry A vs B

| | A, bath side | B, rear garage |
| --- | --- | --- |
| Space lost | The drawer stack beside the bath (about 24 in of base storage) | The curbside rear corner of the garage, about 24 x 24 in of floor |
| Water run | About 2 ft from the bath manifold | About 13 ft from the bath manifold, under the floor |
| Drain | Short drop into the grey tank area | About 8 ft to the grey tank; the washer's pump has to lift it |
| Vent run | About 1 ft through the roadside wall | About 1 ft through the rear wall |
| Weight position | 124 in from the rear wall: front axle +25 lb, rear +123 lb | 14 in from the rear wall: front axle -67 lb, rear +215 lb |
| Noise near the desk | About 7 ft from the desk chair | About 2 ft from the desk chair |
| Noise near the bed | Away from the bed | Directly under the lowered bed |
| Counter | Raised fold-and-charge counter fits on top | No counter: the bed comes down above it |
| Access | Load from the aisle, any time | Bed has to be up to load it |

## Axle math

Front share = weight x (x - 94) / 178, x in inches from the rear wall.

| Item | lb | x in | Front | Rear |
| --- | --- | --- | --- | --- |
| 2 x B4810 batteries | 202 | 30 | -73 | +275 |
| Battery box + mounts | 25 | 30 | -9 | +34 |
| RV5 hub | 31 | 13 | -14 | +45 |
| Solar, rear 3 panels | 89 | 58 | -18 | +107 |
| Solar, front 3 panels | 89 | 198 | +52 | +37 |
| Panel mounts, combiner, cable | 60 | 128 | +12 | +48 |
| 2 x Orion-Tr | 8 | 266 | +8 | +0 |
| 48V and AC cable runs | 40 | 140 | +10 | +30 |
| Starlink Mini + mount | 6 | 130 | +1 | +5 |
| Washer-dryer (A) | 148 | 124 | +25 | +123 |
| **Total (A)** | 699 | | -6 | +704 |

With laundry B: front -97 lb, rear +796 lb.

Recheck of the earlier figure: 203 lb at 80 in behind the axle gives +294 rear / -91 front (holds as arithmetic). The modelled box sits 64 in behind the axle: +276 rear / -73 front.

## Decisions

- **Coach length:** Used East to West's 26 ft. One review quotes 24 ft; the manufacturer page wins.
- **Body width:** East to West does not publish it. Modelled at 91 in, the same figure used earlier in this thread. ESTIMATE.
- **Front overhang:** Modelled at 40 in from the Transit cab shape, which puts the rear overhang at 94 in. ESTIMATE.
- **Floor and roof heights:** Floor 36 in above ground and roof 121 in, so 81 in interior height (confirmed) and 137 in overall with the AC (confirmed) both hold.
- **Rear wheels:** Modelled as dual rear wheels, implied by the 7,275 lb rear axle rating. ESTIMATE.
- **Floorplan positions:** No dimensioned floorplan is published. The order of rooms follows East to West and dealer descriptions; exact cabinet positions are modelled. ESTIMATE.
- **Entry door:** Curbside, behind the cab, opening into the dinette area. ESTIMATE.
- **AC position:** The Chill Cube stays in the existing 14x14 opening, modelled mid-roof at 130 in from the rear wall. Panels split into a rear group of 3 and a front group of 3 around it. ESTIMATE until the opening is measured.
- **Panel orientation:** All six panels run crosswise (68.35 in across the roof) because roof length is the scarce dimension.
- **Roof vents:** The bath fan, galley fan, cabover fan and shower skylight end up under panels. Modelled with low-profile covers on taller Z-brackets (2.5 in clearance). Swap any tall dome cover for a low-profile one.
- **Starlink:** You said Starlink, not which dish. Modelled the Starlink Mini on a flat mount beside the AC: 40-50 W typical against 75-100 W for the Standard, and it fits the side margin. The Standard (23.4 x 13.4 in) would also fit there.
- **Combiner:** One roof combiner between the rear panel group and the AC, feeding PV1 and PV2 as two trunk runs down a rear-corner chase.
- **RV5 location:** Inside the roadside desk pedestal, on the side wall, directly above the battery box. Keeps the kneehole open and the 48V run to the packs short.
- **Battery box position:** Centred 30 in from the rear wall (64 in behind the rear axle), between the spare tire and the hitch, hung from the frame rails with its bottom 12 in above ground. ESTIMATE.
- **Spare tire:** Kept in place under the frame, ahead of the battery box.
- **Exhaust:** Routed to exit curbside ahead of the battery box so the box is not in the exhaust stream.
- **Orion-Tr chargers:** Under the passenger seat near the starter battery: a short 12V lead, then one 48V run back along the curbside frame rail. Lower current over the long run than placing them at the tail.
- **Generator tie-in:** Generator and shore power meet at a transfer switch under the curbside bench, then one 120V run under the floor to the RV5 AC input. Run the RV5 in Standard or Silent charge mode on the generator.
- **Laundry A:** Bath side, between the bath wall and the fridge, replacing the drawer stack. Fridge moved one slot forward in the model to make the adjacency work. ESTIMATE.
- **Laundry B:** Rear garage, curbside rear corner under the lift bed, vented through the rear wall. The load hatch is modelled on the curbside wall ahead of it.
- **Lift bed:** Shown raised (office mode) in every render. Lowered underside modelled at 38 in above the floor. ESTIMATE.
- **Tail lamps:** Rendered as smoked lenses so no red tones appear anywhere; the real coach keeps its legal red lamps.
- **Tow car:** Generic small hatch built to Abarth dimensions (144.4 x 64.1 x 58.7 in, 90.6 in wheelbase), no badges.
- **Interior palette:** Charcoal walls, walnut cabinetry and desk, dark oak floor, graphite upholstery, brass pulls, warm 2700K-look lighting. No red or oxblood.
- **GitHub:** The repo cloned, but this session's GitHub link has no push access to arthckr88/22NFT. Everything was committed on branch render/full-3d-build locally and delivered as files here.

## Verify at walkthrough

- [ ] **Flat roof length** (Measure first): From the cabover seam to the rear cap. The build needs about 233 in; the model assumes 234 in.
- [ ] **14x14 AC opening position** (Measure first): Distance from the rear wall. It decides how the panels split.
- [ ] **Tail space and heights** (Measure first): Ground to frame bottom at the tail, spare tire position, receiver height. The box needs about 52 x 18 x 7.5 in with its bottom at 12 in or higher.
- [ ] **Rear axle weight** (Measure): Weigh the loaded coach per axle. The build adds 700-800 lb almost all on the rear axle (7,275 lb rated).
- [ ] **Body width** (Measure): Outside and inside, at the roof and at the floor.
- [ ] **Roof fixtures** (Measure): Positions and heights of the fans, skylight and antenna.
- [ ] **Drawer stack width** (Measure): Bath side: the washer needs about 24 in.
- [ ] **Lift bed lowered height** (Measure): Underside height above the floor when down; option B needs 34 in or more.
- [ ] **Desk pedestal** (Check): Inside width and depth for the RV5 (17.7 x 19.7 x 6.3 in).
- [ ] **Ducted air box fit** (Check): Photograph the stock ceiling assembly and duct openings for the Chill Cube box.
- [ ] **Grey tank** (Check): Location and inlet height, for both laundry drains.
- [ ] **Generator and transfer switch** (Check): Make, model, and where the existing transfer switch sits.
- [ ] **Floor height** (Check): Ground to the floor at the door.
- [ ] **Alternator** (Check): Single or dual 250A from the build sheet.
- [ ] **Model year** (Check): 2026 or 2027.
