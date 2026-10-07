"""Single source of truth for every dimension used by the model.

status: C = Confirmed (manufacturer / spec sheet), R = Credible (dealer,
retailer or owner report), E = ESTIMATE (not published; modelled value).
All lengths in inches, weights in lb.
"""

SPECS = [
    # item, value, source, status
    ("Coach overall length", "26 ft 0 in (312 in)", "https://easttowestrv.com/alita/22NF/13304", "C"),
    ("Coach overall height", "11 ft 5 in (137 in)", "https://www.fraserway.com/product-east-to-west/alita-motor-home-class-c/22nf", "C"),
    ("Coach body width", "91 in modelled", "Not published by East to West", "E"),
    ("Interior height", "81 in", "https://www.rvguide.com/specs/east-to-west/class-c/2026/alita/22nf.html", "C"),
    ("Wheelbase", "178 in", "https://easttowestrv.com/alita/22NF/13304", "C"),
    ("Front overhang (bumper to front axle)", "40 in modelled", "Transit cab geometry; not published for 22NFT", "E"),
    ("Rear overhang (rear axle to rear wall)", "94 in (312 - 178 - 40)", "Derived from the two values above", "E"),
    ("GVWR / GCWR", "11,000 / 13,500 lb", "https://www.fraserway.com/product-east-to-west/alita-motor-home-class-c/22nf", "C"),
    ("Axle ratings", "Front 4,630 lb, rear 7,275 lb", "https://www.fraserway.com/product-east-to-west/alita-motor-home-class-c/22nf", "C"),
    ("Dealer-listed weight (2027 unit)", "9,031 lb, about 1,969 lb CCC", "https://www.couchsrvnation.com/east-to-west/class-c-motorhome/alita/22nft1", "R"),
    ("Tanks", "35 fresh / 30 grey / 30 black / 25 fuel gal", "https://www.fraserway.com/product-east-to-west/alita-motor-home-class-c/22nf", "C"),
    ("Propane", "2 tanks, 9.4 gal total", "https://www.rvguide.com/specs/east-to-west/class-c/2026/alita/22nf.html", "C"),
    ("Generator", "4,000 W, gasoline", "https://www.fraserway.com/product-east-to-west/alita-motor-home-class-c/22nf", "C"),
    ("Awning", "16 ft Girard legless, LED strip", "https://www.fraserway.com/product-east-to-west/alita-motor-home-class-c/22nf", "C"),
    ("Beds", "Rear queen lift bed 60 x 80, cabover 60 x 80", "https://www.fraserway.com/product-east-to-west/alita-motor-home-class-c/22nf", "C"),
    ("Floorplan order", "Front dinette, galley curbside, bath across, rear office + lift bed + garage", "https://www.autoevolution.com/news/the-2026-alita-22nft-is-a-compact-motorhome-with-a-very-surprising-layout-259965.html", "R"),
    ("Exact cabinet positions, door location", "Modelled from the floorplan order above", "No dimensioned floorplan published", "E"),
    ("Flat roof length (cabover seam to rear cap)", "234 in modelled", "Not published", "E"),
    ("Existing roof fixtures", "1 AC, 2 fans, 1 shower skylight, 12V panel modelled", "Not published; typical Class C", "E"),
    ("Floor height above ground", "36 in modelled", "Not published", "E"),
    ("Frame rail bottom above ground at tail", "19 in modelled", "Not published for this chassis", "E"),
    ("Transit cutaway alternator", "250 A", "https://specs2.auto123.com/en/specs/ford/transit-cutaway/ford-transit-cutaway-2024-t-350-rwd-156-9500-gvwr-srw-449769", "R"),
    ("Rear wheels", "Dual rear wheels, 27.5 in tire diameter modelled", "Implied by 7,275 lb rear axle rating", "E"),
    ("Bluetti B4810 (each)", "23.9 x 15.0 x 5.7 in, 101 lb", "https://solarpowersupply.eu/bluetti-b4810-battery", "C"),
    ("Bluetti RV5 hub", "17.7 x 19.7 x 6.3 in, 30.9 lb", "https://bestecosolar.com/product/bluetti-rv5-power-hub/", "C"),
    ("Callsun 275W panel (each)", "68.35 x 30.3 x 1.38 in, 29.8 lb", "https://callsunsolar.com/products/275w-n-type-bifacial-solar-panel", "C"),
    ("Victron Orion-Tr Smart 12/48-8A (each)", "186 x 130 x 80 mm, 1.8 kg (4.0 lb)", "https://www.akkuman.de/shop/Victron-Orion-Tr-Smart-12-48-8A-DC-DC-Ladegeraet-48V", "C"),
    ("Furrion Chill Cube 18K ducted", "29.5 x 29 x 14.5 in, 72.4 lb", "https://elkhartrvparts.com/products/furrion-chill-cube-variable-speed-rv-rooftop-air-conditioner-18k-btu-heat-pump-black-ducted-2025008215", "C"),
    ("Splendide WDV2200XCD", "23.5 W x 33.1 H x 22.6 D in, 148 lb", "https://www.fisheriessupply.com/splendide-wdv2200xcd-vented-combo-washer-and-dryer/wdv2200xcd", "C"),
    ("Starlink Mini", "11.4 x 9.8 x 1.4 in, 2.4 lb, 40-50 W typical", "https://www.usmobile.com/blog/starlink-mini-vs-standard/", "C"),
    ("Starlink Standard (alternative)", "23.4 x 13.4 x 1.6 in, 7.05 lb, 75-100 W typical", "https://www.usmobile.com/blog/starlink-mini-vs-standard/", "C"),
    ("Fiat 500 Abarth (manual)", "144.4 L x 64.1 W x 58.7 H in, 90.6 in WB, 2,512 lb", "https://www.fiat500usa.com/2018/02/2018-fiat-500-and-500-abarth-specs.html", "C"),
    ("Battery box", "52 x 18 x 7.5 in, about 25 lb empty, bottom 12 in above ground", "Sized around two B4810s", "E"),
    ("Lift bed lowered underside", "38 in above floor modelled", "Not published", "E"),
]

# Key modelled positions (inches, x from rear wall)
X_REAR_AXLE = 94.0
X_FRONT_AXLE = 272.0
WHEELBASE = X_FRONT_AXLE - X_REAR_AXLE  # 178
FLOOR_Z = 36.0
ROOF_Z = 121.0
CEIL_Z = 117.0
BODY_W = 91.0
HALF = BODY_W / 2

PANEL_L = 68.35   # across the coach
PANEL_W = 30.3    # along the coach
PANEL_GAP = 1.0
PANELS_REAR_X0 = 12.0
PANELS_FRONT_X0 = 152.0
AC_X = 130.0      # centre of the 14x14 opening (ESTIMATE)

BOX = dict(x0=21.0, x1=39.0, y0=-26.0, y1=26.0, z0=12.0, z1=19.5)
SPARE_X = 60.0

# Component masses for the axle calculation: name, lb, x position (in from rear)
MASSES = [
    ("2 x B4810 batteries", 202.0, 30.0),
    ("Battery box + mounts", 25.0, 30.0),
    ("RV5 hub", 30.9, 13.0),
    ("Solar, rear 3 panels", 89.4, 58.5),
    ("Solar, front 3 panels", 89.4, 198.5),
    ("Panel mounts, combiner, cable", 60.0, 128.0),
    ("2 x Orion-Tr", 7.9, 266.0),
    ("48V and AC cable runs", 40.0, 140.0),
    ("Starlink Mini + mount", 6.0, 130.0),
]
WASHER = ("Washer-dryer", 148.0)
WASHER_X = {"A": 124.0, "B": 14.0}


def axle_split(w, x):
    """Return (front, rear) load change in lb for weight w at x."""
    front = w * (x - X_REAR_AXLE) / WHEELBASE
    return front, w - front
