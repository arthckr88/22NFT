# Comparable installs

Accessed 2026-10-06. None of these is an Alita 22NF. They are the closest published builds that bear on an underbody or spare-well battery box. Owner weights and material sizes are the authors’ statements.

## 1. Ford Transit van — spare-well box, aluminum, about 120 lb

[Ford Transit USA Forum, “Rear under floor storage using spare tire location”](https://www.fordtransitusaforum.com/threads/rear-under-floor-storage-using-spare-tire-location.96179/)

A van owner (not a cutaway Class C) cut out the spare-tire crossmember and built a box to hold about **120 lb** of lithium so the cabin could keep its storage. Materials the author names: **6061** aluminum, **2 in angle at 1/8 in**, **1/8 in sheet**, sealed with **Sikaflex 221**, with 1/2 in plywood and rubber to level an uneven floor. The author checked clearance to the rear differential at full droop and left spot welds near the back uncut. The post says the author does not recommend copying it without a separate investigation.

Lessons to keep:

- The spare well is a real volume, and people do put batteries there.
- Removing a factory crossmember is a structural change. This package does **not** adopt that. D-04 bolts to rails or existing brackets and does not show a cut crossmember.
- The author’s ~120 lb is one pack class. Two B4810 packs are **202.8 lb** before the hub and the box, so the structure has to be argued at that higher load, not at 120 lb.
- Differential droop and spot welds are the kind of interference a tape and a creeper have to find. They will not be on a brochure.

## 2. Commercial Transit van box — not this wheelbase

[DIYvan preloaded under-vehicle battery box](https://diyvan.com/products/preloaded-under-vehicle-battery-box-for-ford-transit-van-fits-148wb-and-130wb)

Advertised for **130 and 148 in** Transit vans, driver side, formed steel, heated. The page lists a Blue Sea 180 A waterproof breaker, a negative post, **50 W** heat elements under each battery, a digital controller, Thinsulate caps, and Minicell foam. Price on the page: **$3,800**. The product is sold as-is with the installer taking the risk.

Use it as a pattern (steel shell, external breaker, heat pads, insulation), not as a part that fits. The Alita is on a **178 in** cutaway, and the listing does not claim that wheelbase. The $3,800 figure is that product’s price, not a quote for a one-off tail box.

## 3. Transit extended, 48 V underbody, still a question

[DIY Solar Power Forum, “Waterproof 16 kWh battery box needed”](https://diysolarforum.com/threads/waterproof-16kwh-battery-box-needed.125374/)

A 2019 Transit Extended owner wanted roughly 15 kWh of 48 V LiFePO4 underneath and could not use server-rack cases because the BMS screen and breaker face the weather. Replies: those cases are not waterproof; keep the box off exhaust and transmission heat; a welded aluminum box with a sealed front is the usual answer.

Lesson: a 48 V rack battery’s face full of ports is a bad underbody face. The B4810 is a closed pack (IP65) with terminals and a pressure valve, which is a better starting point, and the manual still says not to run it wet. The RV5 hub has a fan and a published clearance (at least 8 in) and no published IP rating. The hub is the awkward object in a sealed tail box, not the B4810.

## 4. Interior van racks — the opposite of this brief

[Van Builder HQ, 80/20 lithium install in a Transit](https://vanbuilderhq.com/lithium-battery-install-camper-van-8020-frame/) and [Roam Wired’s battery-box notes](https://roamwired.com/blog/lifepo4-battery-box-campervan)

Both put lithium **inside**, under a bed or on a framed floor, with straps or extrusion so the pack cannot move. That solves water and cold. It spends the cabin volume this brief is trying to keep. Recorded as option g, not as the plan.

## 5. Travel-trailer lithium moves — lessons, wrong chassis

Forest River Forums threads on moving lithium off the tongue into a pass-through or under a bed ([example](https://www.forestriverforums.com/threads/mounting-battery-in-pass-through-storage.387120/), [underbelly access](https://www.forestriverforums.com/threads/proper-steps-to-access-the-underbelly.360655/)):

- Owners who camp in cold moved packs inside because an exterior bay still freezes.
- Cable slack from the factory run is usually too short; extensions and a busbar show up in every write-up.
- Drilling the floor without knowing the tank on the other side is the repeated failure.
- Coroplast underbellies are opened by removing fasteners, not by carving a random hatch, and they are resealed.

The Alita is a motorhome on a Transit frame, not a trailer on a tongue. The cold-weather and “don’t drill blind” lessons still apply. The tongue-box lesson does not.

## 6. Class C spare on a long rear overhang

[iRV2, undermount spare on a Class C](https://www.irv2.com/threads/undermount-spare-tire-carrier-for-a-class-c.2209621/)

A 32 ft Class C owner already over the rear GAWR wanted the spare off a bumper carrier that sat far behind the axle and in between the rails instead. Replies mention winch-style carriers, extra threaded-rod supports because a cable alone is not the travel lock, and PVC rollers to drag the tire out.

Lesson for option c: moving the spare forward reduces its own lever arm, which is the same physics as the battery problem. A bumper or hitch carrier for the spare collides with the Fiat tow bar and is ruled out. A winch between the rails only works if the tanks and the exhaust are not already there.

## 7. Transit alternator behavior with a Victron DC-DC

[Ford Transit USA Forum, Orion XS settings](https://www.fordtransitusaforum.com/threads/victron-orion-xs-1400-settings.104617/)

Transit smart regenerative charging often holds the alternator near **13.5 V**, below the Orion’s default 14 V start. Owners either lower the engine-run thresholds or use the vehicle interface “engine run” pin instead of voltage detection. That thread is about a 12 V Orion XS, not the 12/48 charger, but the alternator behavior is a property of the van, not of the charger. Plan on an engine-run signal rather than hoping the voltage threshold is right. The alternator’s amp rating on this cutaway was not found; how many 12/48-8A units it can feed is OPEN.
