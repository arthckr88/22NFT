#!/usr/bin/env python3
"""Render conceptual D-01..D-09 sheets. Not a fabrication tool."""

from pathlib import Path

OUT = Path(__file__).resolve().parent
W, H = 1600, 1100
STAMP = "CONCEPT — NOT FOR FABRICATION UNTIL FIELD-MEASURED."
DATE = "2026-10-06"


def esc(text):
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def sheet(sheet_no, title, scale, sources, body):
    tb = f"""
    <rect x="36" y="1000" width="1528" height="72" fill="#1c1915" />
    <text x="52" y="1028" fill="#f4efe6" font-family="ui-sans-serif,sans-serif" font-size="16" font-weight="700">22NFT BUILD</text>
    <text x="52" y="1052" fill="#d9c7a6" font-family="ui-sans-serif,sans-serif" font-size="13">{esc(sheet_no)}  {esc(title)}</text>
    <text x="760" y="1028" fill="#f4efe6" font-family="ui-sans-serif,sans-serif" font-size="13">Scale: {esc(scale)}</text>
    <text x="760" y="1052" fill="#d9c7a6" font-family="ui-sans-serif,sans-serif" font-size="12">Rev A   {DATE}</text>
    <text x="1080" y="1028" fill="#f0c7c0" font-family="ui-sans-serif,sans-serif" font-size="11">{esc(STAMP)}</text>
    <text x="1080" y="1052" fill="#b7c4c0" font-family="ui-sans-serif,sans-serif" font-size="11">Sources: {esc(sources)}</text>
    """
    svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <rect width="100%" height="100%" fill="#f6f3ec"/>
  <text x="48" y="42" fill="#8c2f2f" font-family="ui-sans-serif,sans-serif" font-size="15" font-weight="700">{esc(STAMP)}</text>
  <text x="48" y="68" fill="#3d3832" font-family="ui-sans-serif,sans-serif" font-size="22" font-weight="700">{esc(sheet_no)} — {esc(title)}</text>
  {body}
  {tb}
</svg>
"""
    (OUT / f"{sheet_no}.svg").write_text(svg)


def d01():
    body = """
    <text x="48" y="100" fill="#5c564e" font-family="ui-sans-serif,sans-serif" font-size="13">Coach outline uses published 26 ft 0 in length and 11 ft 5 in height. Width is TBD. Compartment count, doors, spare hanger, and generator bay are unpublished. Candidate tail box is a location, not a fit.</text>
    <g font-family="ui-sans-serif,sans-serif" font-size="12" fill="#2c2824">
      <text x="48" y="132" font-weight="700">Driver side — NOT TO SCALE</text>
      <rect x="48" y="148" width="700" height="150" fill="#efe8dc" stroke="#2c2824" stroke-width="2"/>
      <path d="M48 220 L110 148 L180 148 L180 298 L48 298 Z" fill="#e4dccb" stroke="#2c2824"/>
      <text x="70" y="250">Cab</text>
      <rect x="200" y="168" width="70" height="90" fill="none" stroke="#2c2824" stroke-dasharray="4 3"/>
      <text x="208" y="278">door?</text>
      <rect x="290" y="250" width="80" height="40" fill="#d7e3ef" stroke="#2c2824"/>
      <rect x="390" y="250" width="80" height="40" fill="#d7e3ef" stroke="#2c2824"/>
      <rect x="490" y="250" width="80" height="40" fill="#d7e3ef" stroke="#2c2824"/>
      <text x="300" y="246">Bays — count UNVERIFIED</text>
      <rect x="600" y="200" width="130" height="70" fill="#f3d39a" stroke="#8a5a12" stroke-dasharray="6 3"/>
      <text x="612" y="240">Tail box</text>
      <text x="612" y="256">candidate b</text>
      <text x="400" y="320">26 ft 0 in overall (CONFIRMED) — door stations not measured</text>

      <text x="820" y="132" font-weight="700">Curb side — NOT TO SCALE</text>
      <rect x="820" y="148" width="700" height="150" fill="#efe8dc" stroke="#2c2824" stroke-width="2"/>
      <path d="M1450 220 L1520 148 L1520 298 L1450 298 Z" fill="#e4dccb" stroke="#2c2824"/>
      <text x="1460" y="250">Cab</text>
      <rect x="860" y="175" width="280" height="28" fill="#c9d7c2" stroke="#2c2824"/>
      <text x="870" y="194">Awning 16 ft (CONFIRMED) — side not stated, drawn curb as a convention</text>
      <rect x="900" y="230" width="50" height="60" fill="none" stroke="#2c2824"/>
      <text x="904" y="264">entry</text>
      <rect x="1000" y="250" width="90" height="40" fill="#d7e3ef" stroke="#2c2824"/>
      <rect x="1110" y="250" width="90" height="40" fill="#d7e3ef" stroke="#2c2824"/>
      <text x="1000" y="246">Bays UNVERIFIED</text>
      <rect x="1240" y="210" width="140" height="60" fill="#f6d4d0" stroke="#8c2f2f" stroke-dasharray="5 3"/>
      <text x="1252" y="236">Generator</text>
      <text x="1252" y="252">location UNVERIFIED</text>

      <text x="48" y="380" font-weight="700">Rear — NOT TO SCALE</text>
      <rect x="48" y="396" width="360" height="280" fill="#efe8dc" stroke="#2c2824" stroke-width="2"/>
      <circle cx="228" cy="560" r="46" fill="none" stroke="#2c2824" stroke-width="3"/>
      <text x="188" y="564">Spare</text>
      <text x="150" y="630">hanger UNVERIFIED</text>
      <rect x="70" y="430" width="120" height="70" fill="#f3d39a" stroke="#8a5a12" stroke-dasharray="6 3"/>
      <text x="82" y="460">Box b</text>
      <text x="82" y="478">if it fits</text>
      <rect x="250" y="430" width="120" height="50" fill="#f6d4d0" stroke="#8c2f2f"/>
      <text x="262" y="460">Exhaust</text>
      <text x="70" y="700">Do not cover dumps, exhaust, or the spare.</text>
      <text x="70" y="718">Hitch box is RULED OUT (Fiat tow bar).</text>

      <text x="460" y="380" font-weight="700">Legend</text>
      <rect x="460" y="400" width="28" height="18" fill="#d7e3ef" stroke="#2c2824"/>
      <text x="498" y="414">Published as existing, size unknown</text>
      <rect x="460" y="428" width="28" height="18" fill="#f3d39a" stroke="#8a5a12"/>
      <text x="498" y="442">Candidate battery enclosure</text>
      <rect x="460" y="456" width="28" height="18" fill="#f6d4d0" stroke="#8c2f2f"/>
      <text x="498" y="470">Keep clear — location not fixed</text>
      <text x="460" y="510">Height 11 ft 5 in is CONFIRMED and is not</text>
      <text x="460" y="528">drawn to the same scale as the length.</text>
      <text x="460" y="560">Chassis frame ends 37.35 in behind the</text>
      <text x="460" y="578">rear axle on the 2023 Ford BEMM EL-LWB</text>
      <text x="460" y="596">column, adapter excluded. The body overhang</text>
      <text x="460" y="614">past that frame is UNVERIFIED.</text>
    </g>
    """
    sheet("D-01", "Exterior elevations", "NOT TO SCALE", "East to West 22NF floorplan; Ford BEMM 2023", body)


def d02():
    body = """
    <text x="48" y="100" fill="#5c564e" font-family="ui-sans-serif,sans-serif" font-size="13">Plan looking up. Rail center-to-center 35.400 in is a Kelderman cutaway drawing, not an Alita measurement. Inside gap, tanks, exhaust, and the spare are UNVERIFIED. Colors follow the placement scores.</text>
    <g font-family="ui-sans-serif,sans-serif" font-size="12" fill="#2c2824">
      <rect x="180" y="220" width="1200" height="70" fill="none" stroke="#2c2824" stroke-width="8"/>
      <rect x="180" y="520" width="1200" height="70" fill="none" stroke="#2c2824" stroke-width="8"/>
      <text x="180" y="205">Rails: CTC 35.400 in is CREDIBLE. Inside width UNKNOWN.</text>
      <line x1="520" y1="150" x2="520" y2="640" stroke="#2c2824" stroke-width="6"/>
      <text x="530" y="148">Rear axle (single). Station along the body UNKNOWN.</text>
      <text x="200" y="148">Front of coach</text>
      <text x="980" y="148">Tail. Rear share of the 134 in combined overhang UNKNOWN.</text>

      <rect x="1180" y="310" width="160" height="180" fill="#f6d4d0" stroke="#a33b32" stroke-dasharray="6 3"/>
      <text x="1192" y="340">a RULED OUT</text>
      <text x="1192" y="358">bare tail / spare</text>
      <text x="1192" y="376">open to spray</text>

      <rect x="1000" y="320" width="160" height="160" fill="#f3d39a" stroke="#8a5a12" stroke-width="2"/>
      <text x="1012" y="350">b CONDITIONAL</text>
      <text x="1012" y="368">sealed tail box</text>
      <text x="1012" y="386">score: axle 2</text>

      <rect x="560" y="330" width="200" height="140" fill="#cfe3d6" stroke="#2f6f4e" stroke-width="2"/>
      <text x="572" y="360">d CONDITIONAL</text>
      <text x="572" y="378">between rails</text>
      <text x="572" y="396">near axle</text>
      <text x="572" y="414">score: axle 5</text>

      <rect x="300" y="330" width="160" height="120" fill="#cfe3d6" stroke="#2f6f4e"/>
      <text x="312" y="360">e forward pack</text>
      <text x="312" y="378">CONDITIONAL</text>
      <rect x="820" y="400" width="150" height="80" fill="#cfe3d6" stroke="#2f6f4e"/>
      <text x="832" y="435">e aft pack</text>
      <text x="832" y="455">between rails</text>

      <rect x="780" y="600" width="180" height="70" fill="#e7e0d2" stroke="#5c564e" stroke-dasharray="4 3"/>
      <text x="792" y="630">Tanks 35/30/30 gal</text>
      <text x="792" y="648">location UNKNOWN</text>
      <rect x="980" y="600" width="150" height="70" fill="#f6d4d0" stroke="#8c2f2f" stroke-dasharray="4 3"/>
      <text x="992" y="630">Generator + exhaust</text>
      <text x="992" y="648">UNKNOWN — keep clear</text>
      <circle cx="1280" cy="430" r="36" fill="none" stroke="#2c2824" stroke-width="3"/>
      <text x="1256" y="434">spare</text>

      <text x="48" y="760">Crossmembers: not published. Do not cut one. The Transit van spare-well build that removed a crossmember is a warning, not a detail to copy.</text>
      <text x="48" y="784">Hitch receiver at the tail is reserved for the Fiat tow bar. No battery box on the hitch.</text>
      <text x="48" y="820" font-weight="700">Color</text>
      <rect x="48" y="836" width="24" height="16" fill="#cfe3d6" stroke="#2f6f4e"/>
      <text x="80" y="849">Better axle score (d, e)</text>
      <rect x="280" y="836" width="24" height="16" fill="#f3d39a" stroke="#8a5a12"/>
      <text x="312" y="849">Tail box (b) — fits the brief, costs rear margin</text>
      <rect x="680" y="836" width="24" height="16" fill="#f6d4d0" stroke="#a33b32"/>
      <text x="712" y="849">Ruled out or keep-clear</text>
    </g>
    """
    sheet("D-02", "Underbelly plan", "NOT TO SCALE", "Kelderman 10005559 CTC; East to West tanks; B4810 manual", body)


def d03():
    body = """
    <g font-family="ui-sans-serif,sans-serif" font-size="14" fill="#2c2824">
      <text x="48" y="110">Wheelbase 178 in CONFIRMED. GAWR front 4,630 lb. GAWR rear 7,275 lb. GVWR 11,000 lb. As-built axle weights UNKNOWN (yellow sticker).</text>
      <line x1="200" y1="280" x2="1200" y2="280" stroke="#2c2824" stroke-width="4"/>
      <circle cx="360" cy="280" r="28" fill="#efe8dc" stroke="#2c2824" stroke-width="3"/>
      <circle cx="1000" cy="280" r="28" fill="#efe8dc" stroke="#2c2824" stroke-width="3"/>
      <text x="320" y="250">Front axle</text>
      <text x="300" y="340">GAWR 4,630</text>
      <text x="960" y="250">Rear axle</text>
      <text x="940" y="340">GAWR 7,275</text>
      <text x="620" y="260">178 in</text>
      <line x1="1000" y1="220" x2="1280" y2="220" stroke="#8a5a12" stroke-width="2" stroke-dasharray="6 3"/>
      <text x="1040" y="210">x = field measure, aft</text>
      <rect x="1220" y="190" width="80" height="40" fill="#f3d39a" stroke="#8a5a12"/>
      <text x="1232" y="214">W</text>

      <text x="48" y="400" font-weight="700">For W behind the rear axle by x inches</text>
      <text x="48" y="428">Rear gain = W × (178 + x) / 178</text>
      <text x="48" y="452">Front change = − W × x / 178</text>
      <text x="48" y="476">They sum to W. Maximum W at that x = (7275 − rear axle now) × 178 / (178 + x).</text>
      <text x="48" y="500">Rear axle now is blank, so no maximum box weight is stated.</text>

      <text x="48" y="545" font-weight="700">Worked rows for W = 233.66 lb (two B4810 at 101.4 plus RV5 at 30.86). 12 in and 24 in are scenarios, not measurements. 37.35 in is the Ford chassis frame end.</text>
      <text x="48" y="580">x = 0 in      rear +233.66 lb    front 0</text>
      <text x="48" y="604">x = 12 in     rear +249.41 lb    front −15.75 lb     ESTIMATE — VERIFY as a position</text>
      <text x="48" y="628">x = 24 in     rear +265.16 lb    front −31.50 lb     ESTIMATE — VERIFY as a position</text>
      <text x="48" y="652">x = 37.35 in  rear +282.69 lb    front −49.03 lb     chassis landmark, not a proven fit</text>
      <text x="48" y="690">Split, one 101.4 lb pack at 24 in and the other pack plus hub on the axle: rear +247.33 lb, front −13.67 lb.</text>
      <text x="48" y="714">Same split at 37.35 in: rear +254.94 lb, front −21.28 lb.</text>

      <text x="48" y="760">CCC remaining = sticker CCC − added weight. Sticker CCC is blank.</text>
      <text x="48" y="784">Partial parts sum, manufacturer panel weight: 779.6 lb before enclosure, desk, Starlink model, cables, tow gear, water, and personal gear.</text>
      <text x="48" y="808">If the conflicting 29.8 lb panel weight is the true one, that partial sum is 564.5 lb. Water is 8.3 lb/gal extra.</text>
      <text x="48" y="844">GCWR 13,500 − GVWR 11,000 = 2,500 lb of combined headroom when the coach is at GVWR. Abarth curb weight is about 2,491–2,512 lb. Weigh both.</text>
    </g>
    """
    sheet("D-03", "Weight and balance", "NOT TO SCALE", "East to West GAWR; B4810 and RV5 manuals; Ford BEMM 37.35 in", body)


def d04():
    body = """
    <g font-family="ui-sans-serif,sans-serif" font-size="13" fill="#2c2824">
      <text x="48" y="104">Internal sizes are the published case sizes. Shell size, bolt spacing, and ground clearance are FIELD MEASURE. Box weight unknown.</text>
      <text x="48" y="140" font-weight="700">Plan — cases only, clearance not included</text>
      <rect x="48" y="160" width="239" height="150" fill="#d9e6f5" stroke="#2c2824" stroke-width="2"/>
      <text x="60" y="230">B4810</text>
      <text x="60" y="248">23.94 × 14.96 in</text>
      <rect x="300" y="160" width="239" height="150" fill="#d9e6f5" stroke="#2c2824" stroke-width="2"/>
      <text x="312" y="230">B4810</text>
      <text x="312" y="248">23.94 × 14.96 in</text>
      <rect x="560" y="160" width="197" height="177" fill="#f3d39a" stroke="#8a5a12" stroke-width="2"/>
      <text x="572" y="230">RV5 hub</text>
      <text x="572" y="248">17.72 × 19.69 in</text>
      <text x="572" y="266">needs ≥ 7.87 in air</text>
      <text x="48" y="360">End to end on the long side: 47.88 in.</text>
      <text x="48" y="380">That is wider than 35.400 in rail CTC.</text>
      <text x="48" y="400">Short side by side: 29.92 in. Fit is unproven.</text>
      <text x="48" y="420">Stacked cases only: 11.42 in thick.</text>

      <text x="48" y="460" font-weight="700">Side — concept</text>
      <rect x="48" y="480" width="520" height="120" fill="#efe8dc" stroke="#2c2824" stroke-width="2"/>
      <rect x="70" y="520" width="200" height="57" fill="#d9e6f5" stroke="#2c2824"/>
      <text x="80" y="554">Pack 5.71 in thick</text>
      <rect x="290" y="505" width="160" height="63" fill="#f3d39a" stroke="#8a5a12"/>
      <text x="300" y="542">Hub 6.30 in</text>
      <line x1="48" y1="610" x2="568" y2="610" stroke="#2c2824" stroke-width="4"/>
      <text x="48" y="640">Lowest point vs departure: UNKNOWN. Skid and drain aft. Do not cover exhaust.</text>

      <text x="820" y="140" font-weight="700">End and door</text>
      <rect x="820" y="160" width="280" height="220" fill="#efe8dc" stroke="#2c2824" stroke-width="2"/>
      <rect x="850" y="200" width="220" height="140" fill="none" stroke="#8a5a12" stroke-width="3"/>
      <text x="900" y="270">Access door</text>
      <text x="880" y="290">lock, not a slam latch</text>
      <text x="860" y="420">Vent in high, vent out low,</text>
      <text x="860" y="440">both baffled against spray.</text>
      <text x="860" y="470">Drain at the low corner.</text>
      <text x="860" y="510">Mount: BOLTED to rail or</text>
      <text x="860" y="530">existing bracket. Weld is a</text>
      <text x="860" y="550">warranty question, not the default.</text>
      <text x="860" y="590">Bolt pitch: FIELD MEASURE.</text>
      <text x="860" y="630">No cut crossmember.</text>
      <text x="48" y="680">If the hub's 7.87 in air will not fit, packs stay here and the hub moves to a sealed bay (option f). OPEN.</text>
      <text x="48" y="708">Bare packs in this zone, with no shell, are ruled out. The B4810 manual says not to use the pack in water.</text>
    </g>
    """
    sheet("D-04", "Tail battery enclosure", "NOT TO SCALE", "B4810 manual dimensions; RV5 manual clearance; Kelderman CTC", body)


def d05():
    body = """
    <g font-family="ui-sans-serif,sans-serif" font-size="13" fill="#2c2824">
      <text x="48" y="104">Parallel only. Two panels in series are 50.52 V at STC, over the RV5 50 V maximum. All six on one port are 82.14 A Isc, over the 50 A port.</text>
      <rect x="48" y="130" width="220" height="70" fill="#efe8dc" stroke="#2c2824"/>
      <text x="60" y="160">3× Callsun 275 W</text>
      <text x="60" y="178">parallel · Isc 41.07 A</text>
      <rect x="48" y="220" width="220" height="70" fill="#efe8dc" stroke="#2c2824"/>
      <text x="60" y="250">3× Callsun 275 W</text>
      <text x="60" y="268">parallel · Isc 41.07 A</text>
      <text x="280" y="170">fuse each module ≤ 25 A</text>
      <text x="280" y="188">(panel max series fuse)</text>
      <text x="280" y="255">1.56 × 13.69 A = 21.4 A</text>
      <text x="280" y="273">so a 25 A fuse is the band</text>
      <line x1="268" y1="165" x2="520" y2="165" stroke="#2c2824"/>
      <line x1="268" y1="255" x2="520" y2="255" stroke="#2c2824"/>
      <rect x="520" y="140" width="200" height="50" fill="#f3d39a" stroke="#8a5a12"/>
      <text x="532" y="170">PV breaker — AWAITING</text>
      <rect x="520" y="230" width="200" height="50" fill="#f3d39a" stroke="#8a5a12"/>
      <text x="532" y="260">PV breaker — AWAITING</text>
      <line x1="720" y1="165" x2="860" y2="220" stroke="#2c2824"/>
      <line x1="720" y1="255" x2="860" y2="250" stroke="#2c2824"/>
      <rect x="860" y="180" width="240" height="120" fill="#d9e6f5" stroke="#2c2824" stroke-width="2"/>
      <text x="872" y="210">RV5</text>
      <text x="872" y="230">PV1 and PV2 solar</text>
      <text x="872" y="248">each 50 A / 1800 W / 50 V</text>
      <text x="872" y="266">combined 3600 W</text>
      <text x="872" y="284">array STC 1650 W total</text>

      <rect x="860" y="340" width="240" height="90" fill="#d9e6f5" stroke="#2c2824"/>
      <text x="872" y="370">2× B4810 parallel</text>
      <text x="872" y="388">51.2 V · 100 Ah each</text>
      <text x="872" y="406">cable &gt; 4 AWG · length FIELD</text>
      <line x1="980" y1="300" x2="980" y2="340" stroke="#2c2824"/>
      <text x="990" y="328">150 A terminal max</text>

      <rect x="48" y="360" width="300" height="90" fill="#efe8dc" stroke="#2c2824"/>
      <text x="60" y="390">Chassis alternator 12 V</text>
      <text x="60" y="408">amps UNKNOWN</text>
      <text x="60" y="426">engine-run signal, not 14 V hope</text>
      <line x1="348" y1="405" x2="470" y2="405" stroke="#2c2824"/>
      <rect x="470" y="370" width="280" height="80" fill="#efe8dc" stroke="#2c2824"/>
      <text x="482" y="400">Orion-Tr Smart 12/48-8A</text>
      <text x="482" y="418">360 W at 40 C · qty OPEN</text>
      <text x="482" y="436">to the 48 V bank, not via PV2</text>

      <rect x="48" y="500" width="250" height="70" fill="#efe8dc" stroke="#2c2824"/>
      <text x="60" y="530">Generator ~4000 W</text>
      <text x="60" y="548">brand UNVERIFIED · 120 V?</text>
      <rect x="320" y="500" width="220" height="70" fill="#efe8dc" stroke="#2c2824"/>
      <text x="332" y="530">Shore</text>
      <text x="332" y="548">30 A or 50 A UNKNOWN</text>
      <line x1="540" y1="535" x2="860" y2="280" stroke="#2c2824"/>
      <text x="560" y="500">AC input of RV5 · 120 V · 42 A rated · 5000 W charge</text>

      <rect x="1180" y="180" width="340" height="200" fill="#f6f3ec" stroke="#2c2824"/>
      <text x="1194" y="210">AC out 120 V 5000 W</text>
      <text x="1194" y="234">Washer on its own 15 A</text>
      <text x="1194" y="258">Desk and Starlink on other branches</text>
      <text x="1194" y="282">DC out 12 V / 24 V to coach loads</text>
      <text x="1194" y="306">Epad inside, not in the box</text>
      <text x="1194" y="340">Main disconnect: reachable</text>
      <text x="1194" y="358">without crawling under. Location OPEN.</text>
      <text x="48" y="640">3 × 13.69 × 1.25 = 51.3 A. If the 50 A port rating does not already include that factor, three panels per port is also over. AWAITING BLUETTI.</text>
      <text x="48" y="668">Voltage drop at 150 A, 20 C solid copper, round trip, calculated: 2 AWG is 0.47 V at 10 ft and 0.70 V at 15 ft. Use larger than 4 AWG. Confirm gauge with Bluetti.</text>
    </g>
    """
    sheet("D-05", "Electrical one-line", "NOT TO SCALE", "RV5 manual; B4810 manual; Callsun 275; Victron Orion-Tr", body)


def d06():
    body = """
    <g font-family="ui-sans-serif,sans-serif" font-size="13" fill="#2c2824">
      <text x="48" y="104">Roof length of the house (excluding cab) is unpublished. Panel size 68.35 × 30.16 in is CONFIRMED. Positions of the AC, fan, and antenna are not. This is a packing test, not a layout to drill.</text>
      <rect x="80" y="160" width="1100" height="520" fill="#efe8dc" stroke="#2c2824" stroke-width="2"/>
      <text x="90" y="190">Forward (cab is ahead of this rectangle — cap length UNKNOWN)</text>
      <rect x="140" y="220" width="300" height="140" fill="#f6d4d0" stroke="#8c2f2f"/>
      <text x="160" y="290">AC 15,000 BTU ducted</text>
      <text x="160" y="308">footprint UNKNOWN</text>
      <text x="160" y="326">variable-speed UNVERIFIED</text>
      <circle cx="560" cy="280" r="40" fill="#f6d4d0" stroke="#8c2f2f"/>
      <text x="520" y="340">Maxxair</text>
      <rect x="640" y="240" width="80" height="80" fill="#f6d4d0" stroke="#8c2f2f"/>
      <text x="648" y="340">Air 360+</text>
      <rect x="780" y="230" width="118" height="102" fill="#d9e6f5" stroke="#24527a" stroke-dasharray="5 3"/>
      <text x="790" y="275">Starlink</text>
      <text x="790" y="293">Mini 11.75×10.2</text>
      <text x="790" y="311">OR Standard</text>
      <text x="790" y="355">model OPEN</text>

      <rect x="140" y="400" width="304" height="134" fill="#cfe3d6" stroke="#2f6f4e"/>
      <rect x="460" y="400" width="304" height="134" fill="#cfe3d6" stroke="#2f6f4e"/>
      <rect x="780" y="400" width="304" height="134" fill="#cfe3d6" stroke="#2f6f4e"/>
      <text x="160" y="470">275 W long side fore-aft</text>
      <rect x="140" y="550" width="304" height="110" fill="#cfe3d6" stroke="#2f6f4e"/>
      <rect x="460" y="550" width="304" height="110" fill="#cfe3d6" stroke="#2f6f4e"/>
      <rect x="780" y="550" width="304" height="110" fill="#cfe3d6" stroke="#2f6f4e"/>
      <text x="150" y="700">Six rectangles are the panels. They are drawn smaller than 68 in on this sheet so the roof notes fit. Do not scale the drawing.</text>
      <text x="80" y="740">Cable entry: use the factory side-port solar hookup only if its gauge and location suit two homeruns. Otherwise a new gland. FIELD. Do not drill a tank.</text>
      <text x="80" y="768">Walk margins and a path to the AC are required and are not drawn, because the roof gear has no published coordinates.</text>
      <text x="80" y="800">Weight on the roof: 6 × 65.65 lb = 393.9 lb per Callsun, or 6 × 29.8 lb = 178.8 lb per the conflicting listing, plus mounts (unknown) and Starlink (model open).</text>
    </g>
    """
    sheet("D-06", "Roof plan", "NOT TO SCALE", "Callsun dimensions; East to West feature list; Starlink spec sheets", body)


def d07():
    body = """
    <g font-family="ui-sans-serif,sans-serif" font-size="13" fill="#2c2824">
      <text x="48" y="104">Existing plan is the dealer walkthrough sequence plus the manufacturer cabover size. It is not a factory drawing. Proposed plan shows both washer options and does not pick one.</text>
      <text x="48" y="140" font-weight="700">Existing — NOT TO SCALE</text>
      <rect x="48" y="160" width="700" height="280" fill="#efe8dc" stroke="#2c2824" stroke-width="2"/>
      <rect x="60" y="175" width="120" height="250" fill="#e4dccb" stroke="#2c2824"/>
      <text x="78" y="300">Cab +</text>
      <text x="78" y="318">60×80</text>
      <text x="78" y="336">cabover</text>
      <rect x="200" y="190" width="140" height="100" fill="#d7e3ef" stroke="#2c2824"/>
      <text x="220" y="245">Dinette</text>
      <rect x="200" y="310" width="160" height="110" fill="#d7e3ef" stroke="#2c2824"/>
      <text x="230" y="370">Kitchen</text>
      <rect x="380" y="190" width="150" height="230" fill="#e7d6d2" stroke="#2c2824"/>
      <text x="420" y="300">Bath</text>
      <text x="400" y="318">center?</text>
      <rect x="550" y="190" width="180" height="230" fill="#e4dccb" stroke="#2c2824"/>
      <text x="580" y="290">Rear</text>
      <text x="560" y="308">60×80 lift</text>
      <text x="560" y="326">CREDIBLE</text>
      <text x="48" y="460">Slide wall UNKNOWN — not drawn.</text>

      <text x="820" y="140" font-weight="700">Proposed zones — washer still OPEN</text>
      <rect x="820" y="160" width="700" height="280" fill="#efe8dc" stroke="#2c2824" stroke-width="2"/>
      <rect x="832" y="175" width="120" height="250" fill="#e4dccb" stroke="#2c2824"/>
      <text x="850" y="300">Cab stays</text>
      <rect x="970" y="190" width="140" height="220" fill="#e7d6d2" stroke="#8a5a12" stroke-dasharray="5 3"/>
      <text x="990" y="290">A washer</text>
      <text x="990" y="308">in the bath</text>
      <rect x="1130" y="190" width="160" height="110" fill="#d7e3ef" stroke="#2c2824"/>
      <text x="1160" y="250">Kitchen stays</text>
      <rect x="1130" y="320" width="360" height="100" fill="#cfe3d6" stroke="#2f6f4e"/>
      <text x="1160" y="360">Rear office desk — options 1–3</text>
      <text x="1160" y="378">B washer shares this zone</text>
      <text x="48" y="510">Epad: at the desk or inside the entry. Not in the battery box. Hub is underbelly.</text>
      <text x="48" y="540">Storage: cabover, dinette, and kitchen stay if the washer takes only one of bath-cabinet or rear-cavity. Desk plus washer plus garage storage in the same cavity do not all fit. See interior-layout.md.</text>
      <text x="48" y="580">Splendide envelope about 23.4 in wide × 33–34 in high × 22–22.6 in deep, 148 lb, floor 280 lb. Model vented vs ventless is OPEN.</text>
    </g>
    """
    sheet("D-07", "Interior floor plan", "NOT TO SCALE", "East to West cabover 60×80; Parris walkthrough; Splendide data sheets", body)


def d08():
    body = """
    <g font-family="ui-sans-serif,sans-serif" font-size="13" fill="#2c2824">
      <text x="48" y="104">Elevations are conceptual. Interior width and ceiling (81 in vs 7 ft) are in conflict or unpublished. No desk height is specified.</text>
      <text x="48" y="145" font-weight="700">Rear wall — desk options</text>
      <rect x="48" y="165" width="460" height="300" fill="#efe8dc" stroke="#2c2824" stroke-width="2"/>
      <rect x="70" y="330" width="180" height="80" fill="#cfe3d6" stroke="#2f6f4e"/>
      <text x="90" y="375">Desk option 2</text>
      <text x="70" y="210">Lift bed above — headroom UNKNOWN</text>
      <text x="70" y="250">Option 1: desk slides out under the bed</text>
      <text x="70" y="270">Option 3: beside the bed — width may not exist</text>
      <text x="70" y="440">Width of this wall: exterior width is TBD</text>

      <text x="560" y="145" font-weight="700">Washer option A — bath</text>
      <rect x="560" y="165" width="460" height="300" fill="#efe8dc" stroke="#2c2824" stroke-width="2"/>
      <rect x="640" y="250" width="140" height="180" fill="#e7d6d2" stroke="#8a5a12"/>
      <text x="660" y="340">23.4 in wide</text>
      <text x="660" y="358">~33 in tall</text>
      <text x="580" y="200">Standpipe top 25–34 in above machine bottom</text>
      <text x="580" y="450">Vent only if WD2100XC. WDC7100XC has no duct.</text>

      <text x="1080" y="145" font-weight="700">Washer option B — rear</text>
      <rect x="1080" y="165" width="460" height="300" fill="#efe8dc" stroke="#2c2824" stroke-width="2"/>
      <rect x="1160" y="250" width="140" height="180" fill="#f3d39a" stroke="#8a5a12"/>
      <text x="1180" y="340">Same machine</text>
      <text x="1100" y="200">Competes with the desk for the lift-bed cavity</text>
      <text x="1100" y="220">Adds 148 lb on the rear lever</text>
      <text x="1100" y="450">Splendide prefers axle or midship, not the tail.</text>

      <text x="48" y="520">Epad shown as a small wall plate near the desk. Size unpublished.</text>
      <rect x="48" y="545" width="90" height="50" fill="#d9e6f5" stroke="#2c2824"/>
      <text x="60" y="575">Epad</text>
      <text x="160" y="575">Keep it out of the spray and out of the underbody box.</text>
    </g>
    """
    sheet("D-08", "Interior elevations", "NOT TO SCALE", "Splendide installation manuals; Parris rear lift bed", body)


def d09():
    body = """
    <g font-family="ui-sans-serif,sans-serif" font-size="13" fill="#2c2824">
      <text x="48" y="104">Every bay below is a slot, not a measured compartment. Assignments move after the tape. Nothing here is a claim that the coach has six doors.</text>
      <text x="48" y="150" font-weight="700">Proposed contents — swap freely</text>
    </g>
    """
    bays = [
        ("Bay A", "UNVERIFIED door", "Sewer hoses, gloves, fittings"),
        ("Bay B", "UNVERIFIED door", "Fresh hose, pressure regulator"),
        ("Bay C", "UNVERIFIED door", "Fiat tow bar, base-plate tools"),
        ("Bay D", "UNVERIFIED door", "Supplemental brake, lighting cable"),
        ("Bay E", "UNVERIFIED door", "Leveling blocks, chocks"),
        ("Bay F", "UNVERIFIED door", "Spare parts, fuses, fluids"),
        ("Pass-through", "RV Guide says standard", "Long items — size UNKNOWN"),
        ("Step well", "Factory 12 V option", "Do not plan B4810s here"),
        ("Tail box", "New, option b", "Two B4810, maybe the hub"),
        ("Generator bay", "Location UNKNOWN", "Keep the exhaust clear"),
    ]
    blocks = []
    for i, (name, meta, use) in enumerate(bays):
        col = i % 2
        row = i // 2
        x = 48 + col * 760
        y = 180 + row * 140
        blocks.append(
            f'<rect x="{x}" y="{y}" width="700" height="120" fill="#efe8dc" stroke="#2c2824"/>'
            f'<text x="{x+16}" y="{y+32}" font-family="ui-sans-serif,sans-serif" font-size="16" font-weight="700" fill="#2c2824">{esc(name)}</text>'
            f'<text x="{x+16}" y="{y+58}" font-family="ui-sans-serif,sans-serif" font-size="13" fill="#5c564e">{esc(meta)}</text>'
            f'<text x="{x+16}" y="{y+88}" font-family="ui-sans-serif,sans-serif" font-size="15" fill="#2c2824">{esc(use)}</text>'
        )
    note = '<text x="48" y="900" font-family="ui-sans-serif,sans-serif" font-size="13" fill="#2c2824">If option f converts a bay into a battery locker, remove that bay from this list before the hoses have nowhere to go. Spare tire access stays clear unless option c relocates it off the hitch.</text>'
    sheet("D-09", "Exterior storage map", "NOT TO SCALE", "East to West rotocast compartments; RV Guide pass-through", body + "\n".join(blocks) + note)


def main():
    d01(); d02(); d03(); d04(); d05(); d06(); d07(); d08(); d09()
    print("wrote", len(list(OUT.glob("D-*.svg"))), "sheets")


if __name__ == "__main__":
    main()
