"""Install map: where every new part goes in the stock 22NFT.

Drawn to scale (inches) from the same coordinates the Blender model uses
(scripts/build.py, scripts/specs.py). x = inches forward of the rear wall,
y = inches from centreline (+ roadside / driver side), z = inches above ground.
Writes install/index.html (+ copies three reference renders).
"""
import json
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, 'install')

S = 3.0            # px per inch in every view
X0 = -12           # leftmost x drawn (hitch receiver sticks out to -6)
HALF = 45.5
F = 36.0           # floor
ROOF = 121.0
AXLES = (94, 272)

RUNS = json.load(open(os.path.join(ROOT, 'renders', '05_xray.json')))['runs_in']


def ft(key):
    return '%.0f ft' % round(RUNS[key] / 12.0)


# ---------------------------------------------------------------- svg helpers
def X(x):
    return 24 + (x - X0) * S


def Yp(y):              # plan-type views: roadside at the top
    return 46 + (HALF + 1 - y) * S


def Zs(z):              # side section
    return 40 + (140 - z) * S


W = int(X(322) + 20)
H_PLAN = int(Yp(-HALF - 1) + 60)
H_SIDE = int(Zs(-4) + 54)


def rect(x0, x1, a0, a1, fy, cls, rx=1.5, extra=''):
    ya, yb = sorted((fy(a0), fy(a1)))
    return '<rect class="%s" x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%s" %s/>' % (
        cls, X(x0), ya, X(x1) - X(x0), yb - ya, rx, extra)


def text(x, y, s, cls='lbl', anchor='start'):
    return '<text class="%s" x="%.1f" y="%.1f" text-anchor="%s">%s</text>' % (cls, x, y, anchor, s)


def poly(pts, fy, cls):
    d = ' '.join('%.1f,%.1f' % (X(p[0]), fy(p[1])) for p in pts)
    return '<polyline class="%s" points="%s"/>' % (cls, d)


def pin(n, x, a, fy, dx=0, dy=0, sys='new'):
    cx, cy = X(x), fy(a)
    px, py = cx + dx, cy + dy
    out = ''
    if dx or dy:
        out += '<line class="leader" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>' % (cx, cy, px, py)
        out += '<circle class="dot" cx="%.1f" cy="%.1f" r="2"/>' % (cx, cy)
    out += '<g class="pin %s"><circle cx="%.1f" cy="%.1f" r="10"/>%s</g>' % (
        sys, px, py, text(px, py + 4, str(n), 'pinnum', 'middle'))
    return out


def ruler(top, bottom):
    s = ''
    for x in range(0, 313, 24):
        s += '<line class="tick" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>' % (X(x), bottom - 6, X(x), bottom)
        s += text(X(x), bottom + 12, str(x), 'tick-t', 'middle')
    s += text(X(-12), bottom + 27, 'inches forward of the rear wall', 'tick-t')
    for n, ax in zip(('rear axle', 'front axle'), AXLES):
        s += '<line class="axle" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>' % (X(ax), top, X(ax), bottom - 8)
        s += text(X(ax), top - 6, '%s · x %d' % (n, ax), 'axle-t', 'middle')
    s += text(X(318), top - 6, 'FRONT →', 'dir', 'end')
    s += text(X(-10), top - 6, '← REAR', 'dir')
    return s


def svg(h, body, label):
    return ('<svg viewBox="0 0 %d %d" role="img" aria-label="%s" preserveAspectRatio="xMinYMin meet">%s</svg>'
            % (W, h, label, body))


# ---------------------------------------------------------------- shared outlines
def body_plan(fy, cab=True):
    s = rect(0, 234, -HALF, HALF, fy, 'shell', rx=4)
    if cab:
        s += ('<path class="shell" d="M%.1f %.1f L%.1f %.1f Q%.1f %.1f %.1f %.1f L%.1f %.1f Q%.1f %.1f %.1f %.1f L%.1f %.1f Z"/>'
              % (X(234), fy(40), X(300), fy(40), X(316), fy(40), X(316), fy(28), X(316), fy(-28),
                 X(316), fy(-40), X(300), fy(-40), X(234), fy(-40)))
    return s


# ---------------------------------------------------------------- VIEW 1: floor plan
def view_plan():
    """Factory floorplan as the underlay, scaled to 26 ft: image px -> x = (px - 90) / 4.9 in from the rear wall,
    walls at py 50 (roadside, y +43.5) and py 520 (curbside, y -43.5)."""
    fy = Yp
    H = H_PLAN + 40
    pxin = 4.9
    sy = 470 / 87.0
    ix, iy = X(-90 / pxin), fy(43.5 + 50 / sy)
    iw, ih = 1600 / pxin * S, 584 / sy * S
    s = '<rect class="paper" x="0" y="0" width="%d" height="%d"/>' % (W, H)
    s += '<image href="img/factory-floorplan.png" x="%.1f" y="%.1f" width="%.1f" height="%.1f" preserveAspectRatio="none"/>' % (ix, iy, iw, ih)
    # ghosts: below the floor and above the ceiling
    s += rect(21, 39, -26, 26, fy, 'ghost-dc')
    s += rect(8, 13, 36, 41, fy, 'ghost-pv', rx=1)
    # the factory desk stays whole, roadside, rear wall to the shower
    s += rect(1, 72.4, 13, 43.5, fy, 'desk-out', rx=1)
    s += text(X(46), fy(9) + 4, 'factory desk stays whole, x 1–72', 'small dark', 'middle')
    # cargo door openings read off the factory floorplan (approximate)
    s += '<line class="dooropen" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>' % (X(20.4), fy(-43.5), X(53.5), fy(-43.5))
    s += '<line class="dooropen" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>' % (X(0), fy(-31.5), X(0), fy(25))
    # new hardware
    s += rect(4, 21.7, 37.15, 43.45, fy, 'n-dc')                       # RV5 in the desk base
    s += rect(48.9, 72.4, -43.5, -20.875, fy, 'n-wa')                  # washer: curbside corner, bed's forward end, against the pantry
    s += rect(48.9, 53.5, -43.5, -40, fy, 'clash', rx=0)               # overlap with the side cargo door opening
    s += rect(26.5, 28.5, 41, 43.5, fy, 'n-dc', rx=0.5)              # Epad
    s += rect(73, 79, -42, -36, fy, 'n-ac')                           # transfer switch (pantry base)
    s += rect(79.5, 84.5, -42, -36, fy, 'n-ac')                       # EMS
    s += rect(206, 223.3, -24, -16.7, fy, 'n-alt')                    # Orions under passenger seat
    s += poly([(214, -20), (200, -15.5), (60, -15.5), (40, -15.5), (37, -18)], fy, 'run alt dashed')
    s += poly([(12, 41), (12, 39), (22, 20), (24, 20)], fy, 'run dc')
    s += poly([(76, -38), (60, -38), (30, -10), (16, 36), (16, 38)], fy, 'run ac dashed')
    s += pin(1, 13, 40.3, fy, 0, 30)
    s += pin(2, 30, 0, fy, 0, 0, 'dc')
    s += pin(4, 27.5, 42.2, fy, 16, 24)
    s += pin(5, 10.5, 38.5, fy, -20, -20, 'pv')
    s += pin(10, 214.6, -20.3, fy, 0, 34, 'alt')
    s += pin(11, 76, -39, fy, -14, 30, 'ac')
    s += pin(12, 82, -39, fy, 14, 30, 'ac')
    s += pin(13, 60.65, -32.2, fy, 0, 0, 'wash')
    s += text(X(318), H - 16, 'factory floorplan, scaled to 26 ft overall · positions approximate', 'small dark', 'end')
    s += ruler(32, H - 44).replace('class="tick-t"', 'class="tick-t dark"').replace('class="axle-t"', 'class="axle-t dark"').replace('class="dir"', 'class="dir dark"')
    return svg(H, s, 'Factory floor plan with new hardware placed on it')


# ---------------------------------------------------------------- VIEW 2: side section
def view_side():
    fz = Zs
    s = '<line class="ground" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>' % (X(-12), fz(0), X(322), fz(0))
    # body section
    s += ('<path class="shell" d="M%.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f Z"/>'
          % (X(0), fz(30), X(0), fz(ROOF), X(300), fz(ROOF), X(304), fz(98), X(284), fz(82),
             X(312), fz(52), X(316), fz(20), X(234), fz(24)))
    s += rect(2, 232, F - 1.5, F, fz, 'floor', rx=0)
    s += text(X(150), fz(F) + 14, 'floor', 'small', 'middle')
    for ax in AXLES:
        s += '<circle class="wheel" cx="%.1f" cy="%.1f" r="%.1f"/>' % (X(ax), fz(14), 14 * S)
    s += rect(-2, 292, 19, 25, fz, 'frame', rx=0)
    s += text(X(170), fz(19) + 12, 'frame rails', 'small', 'middle')
    # stock underbody
    for x0, x1, z0, z1, lab in ((66, 96, 15, 26, 'black'), (98, 118, 15, 26, 'grey'), (120, 156, 15, 26, 'fresh'),
                                (200, 226, 23, 36, 'generator'), (236, 262, 13, 23, 'fuel')):
        s += rect(x0, x1, z0, z1, fz, 'stock')
        s += text(X((x0 + x1) / 2), fz(z0) + 12, lab, 'small', 'middle')
    s += rect(45, 75, 17.5, 21.5, fz, 'stock')
    s += text(X(60), fz(17.5) + 12, 'spare', 'small', 'middle')
    s += rect(-6, 22, 16, 18.5, fz, 'frame', rx=0)
    s += text(X(4), fz(16) + 12, 'hitch', 'small', 'middle')
    # stock cabin
    s += rect(1, 72, 104, 113.5, fz, 'bedover')
    s += text(X(32), fz(113.5) - 4, 'lift bed (raised)', 'small', 'middle')
    s += rect(2, 26, 64.25, 65.5, fz, 'stock', rx=0)
    s += text(X(44), fz(65.5) + 4, 'desk top 29.5 in', 'small')
    s += rect(84.7, 114, F, 100, fz, 'stock')
    s += text(X(99.3), fz(60), 'fridge (curbside)', 'small', 'middle')
    s += rect(204, 228, 26, 45, fz, 'stock')
    # new: battery box, RV5, washers, roof
    s += rect(21, 39, 12, 19.5, fz, 'n-dc')
    s += rect(4, 21.7, F + 1.5, F + 21.2, fz, 'n-dc')
    s += rect(48.9, 72.4, F + 0.6, F + 0.6 + 33.125, fz, 'n-wa')
    s += '<line class="bedline" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>' % (X(1), fz(F + 38), X(72.4), fz(F + 38))
    s += text(X(2), fz(F + 38) - 5, 'lowered bed underside 38 in (modelled) · washer top 33.7 in', 'small')
    s += rect(73, 84.5, F + 2, F + 10, fz, 'n-ac')
    s += rect(206, 223.3, 30, 33.2, fz, 'n-alt')
    for gx in (12, 152):
        s += rect(gx, gx + 92.9, ROOF + 2.5, ROOF + 3.9, fz, 'n-pv', rx=0)
    s += rect(115.5, 144.5, ROOF, ROOF + 14.5, fz, 'n-ac', rx=4)
    s += rect(123.5, 136.5, ROOF + 14.5, ROOF + 15.9, fz, 'n-dc', rx=1)
    s += rect(106.5, 113, ROOF, ROOF + 4, fz, 'n-pv', rx=1)
    # runs (x,z)
    z = ROOF + 0.8
    s += poly([(108, z + 1), (60, z), (10.5, z), (10.5, 117), (8, F + 25), (8, F + 21)], fz, 'run pv')
    s += poly([(12, F + 3), (12, F - 3), (22, 26), (24, 18.5)], fz, 'run dc')
    s += poly([(214, 30), (200, 23), (60, 23), (40, 21), (37, 17.5)], fz, 'run alt')
    s += poly([(76, F + 3), (76, F - 4), (16, F - 4), (16, F + 4)], fz, 'run ac')
    # pins
    s += pin(1, 13, F + 11, fz, 0, -30)
    s += pin(2, 30, 15.75, fz, 0, 36, 'dc')
    s += pin(6, 69, ROOF + 3, fz, 0, -24, 'pv')
    s += pin(7, 109.75, ROOF + 2, fz, -8, -40, 'pv')
    s += pin(8, 130, ROOF + 7, fz, 26, -30, 'ac')
    s += pin(9, 130, ROOF + 15.2, fz, -26, -26, 'dc')
    s += pin(10, 214.6, 31.6, fz, 0, -34, 'alt')
    s += pin(11, 78.7, F + 6, fz, 0, -34, 'ac')
    s += pin(13, 60.65, F + 17, fz, 0, 0, 'wash')
    s += ruler(28, H_SIDE - 34)
    return svg(H_SIDE, s, 'Side section showing heights')


# ---------------------------------------------------------------- VIEW 3: underbody
def view_under():
    fy = Yp
    s = body_plan(fy)
    for ax in AXLES:
        for side in (-1, 1):
            s += rect(ax - 14, ax + 14, side * 46.5, side * 39, fy, 'wheel', rx=3)
    s += rect(-2, 292, 14, 17, fy, 'frame', rx=0) + rect(-2, 292, -17, -14, fy, 'frame', rx=0)
    for x0, x1, y0, y1, lab in ((66, 96, -13, 13, 'black'), (98, 118, -13, 13, 'grey'), (120, 156, -13, 13, 'fresh'),
                                (236, 262, 18, 34, 'fuel'), (200, 226, -40, -20, 'generator'),
                                (258, 268, 16, 26, '')):
        s += rect(x0, x1, y0, y1, fy, 'stock')
        if lab:
            s += text(X((x0 + x1) / 2), fy((y0 + y1) / 2) + 4, lab, 'small', 'middle')
    s += text(X(263), fy(16) + 12, 'start batt.', 'small', 'middle')
    for k in range(2):
        s += '<circle class="stock" cx="%.1f" cy="%.1f" r="%.1f"/>' % (X(186 + k * 11), fy(32), 5.2 * S)
    s += text(X(191.5), fy(41), 'LP', 'small', 'middle')
    s += '<circle class="stock" cx="%.1f" cy="%.1f" r="%.1f"/>' % (X(60), fy(0), 15 * S)
    s += text(X(60), fy(0) + 4, 'spare', 'small', 'middle')
    s += rect(-6, 22, -1.25, 1.25, fy, 'frame', rx=0) + rect(6, 10, -17, 17, fy, 'frame', rx=0)
    s += text(X(2), fy(-20), 'hitch', 'small', 'middle')
    # new
    s += rect(21, 39, -26, 26, fy, 'n-dc')
    for y0 in (-24.5, 0.6):
        s += rect(22.5, 37.5, y0, y0 + 23.9, fy, 'pack', rx=1)
    s += rect(206, 223.3, -24, -16.7, fy, 'n-alt')
    # runs
    s += poly([(214, -20), (200, -15.5), (60, -15.5), (40, -15.5), (37, -18)], fy, 'run alt')
    s += poly([(212, -30), (150, -38), (76, -39)], fy, 'run ac dashed')
    s += poly([(76, -39), (60, -38), (30, -10), (16, 36), (16, 38)], fy, 'run ac')
    s += poly([(16, 44.5), (20, 30), (60, 30), (70, -30), (76, -36)], fy, 'run ac dashed')
    s += '<circle class="riser dc" cx="%.1f" cy="%.1f" r="5"/>' % (X(12), fy(40))
    s += pin(2, 30, 13, fy, 0, -60, 'dc')
    s += pin(10, 214.6, -20.3, fy, 0, 30, 'alt')
    s += pin(3, 12, 40, fy, -20, 16, 'dc')
    s += text(X(150), fy(-15.5) - 10, 'alternator 48 V run along the curbside rail · about 16 ft', 'small run-t alt-t', 'middle')
    s += text(X(60), fy(-38) + 14, 'transfer switch → RV5 · about 9 ft', 'small run-t ac-t', 'middle')
    s += text(X(110), fy(30) - 6, 'shore inlet → transfer switch (inlet spot unverified)', 'small run-t ac-t', 'middle')
    s += ruler(32, H_PLAN - 44)
    return svg(H_PLAN, s, 'Underbody plan, looking down through the floor')


# ---------------------------------------------------------------- VIEW 4: roof
def view_roof():
    fy = Yp
    s = rect(0, 300, -HALF, HALF, fy, 'shell', rx=6)
    s += '<line class="seam" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>' % (X(234), fy(HALF), X(234), fy(-HALF))
    s += text(X(267), fy(-HALF) + 16, 'cab-over roof', 'small', 'middle')
    for gx in (12, 152):
        for k in range(3):
            x0 = gx + k * 31.3
            s += rect(x0, x0 + 30.3, -34.175, 34.175, fy, 'n-pv', rx=1)
    s += text(X(58.5), fy(-34.2) + 16, 'panels 1–3 · 68.35 in across', 'small', 'middle')
    s += text(X(198.5), fy(-34.2) + 16, 'panels 4–6', 'small', 'middle')
    s += rect(115.5, 144.5, -14.75, 14.75, fy, 'n-ac', rx=5)
    s += text(X(130), fy(0) + 4, 'AC', 'big-t', 'middle')
    s += rect(123.5, 136.5, 22, 33, fy, 'n-dc', rx=1.5)
    s += rect(106.5, 113, -5, 5, fy, 'n-pv', rx=1)
    s += rect(8, 13, 36, 41, fy, 'n-pv', rx=1)
    # existing fans / skylight under the panels
    for (x, y) in ((86, 20), (72, -22), (226, 0)):
        s += rect(x - 8, x + 8, y - 8, y + 8, fy, 'conflict', rx=2)
        s += '<path class="warn" d="M%.1f %.1f l7 12 h-14 z"/>' % (X(x), fy(y) - 7)
    s += rect(64, 80, 26, 40, fy, 'conflict', rx=2)
    for i, x in enumerate([27.15, 58.45, 89.75, 167.15, 198.45, 229.75]):
        s += poly([(x, 30), (x, 6 if x < 110 else 3), (110, 0)], fy, 'run pv thin')
    s += poly([(108, 4), (60, 38), (10.5, 38.5)], fy, 'run pv dashed')
    s += pin(6, 42.3, -20, fy, 0, 0, 'pv')
    s += pin(6, 182.3, -20, fy, 0, 0, 'pv')
    s += pin(7, 109.75, 0, fy, 0, 46, 'pv')
    s += pin(5, 10.5, 38.5, fy, -18, -18, 'pv')
    s += pin(8, 130, -9, fy, 0, 46, 'ac')
    s += pin(9, 130, 27.5, fy, 24, -20, 'dc')
    s += pin('!', 86, 20, fy, 0, -30, 'warn')
    s += ruler(32, H_PLAN - 44)
    return svg(H_PLAN, s, 'Roof plan')


# ---------------------------------------------------------------- schedule
SCHED = [
    # n, sys, part, where, position, displaces, mount/access, connects
    ('1', 'dc', 'Bluetti RV5 hub', 'In the rear-end pedestal of the factory desk (“desk below”), roadside rear corner under the lift bed, on the floor against the roadside wall.',
     'x 1–22 in from rear wall · roadside wall · floor level', 'The rear-end desk pedestal’s storage. The rest of the desk is untouched.',
     'Bolted to the floor through its mounting holes. Pedestal needs a vented front panel so the RV5 keeps 7.87 in of open air at its vents. Front panel removable for service.',
     '48 V down through the floor to the packs (%s) · PV trunks from the roof gland straight above (%s each) · 120 V in from the transfer switch in the pantry base (about 9 ft) · 120 V out to the factory breaker panel (location to find) · 12 V out to the coach 12 V panel.' % (
         ft('48V, RV5 to batteries'), ft('PV trunk, combiner to RV5 (x2 runs)'))),
    ('2', 'dc', '2 × B4810 in a sealed box', 'Under the tail, across the frame rails, between the hitch crossmember and the spare tire.',
     'x 21–39 in from rear wall (about 64 in behind the rear axle) · 52 × 18 × 7.5 in box · bottom about 12 in off the ground',
     'Nothing inside. Uses empty space behind the spare. Must clear the hitch receiver tube, the exhaust tip, and the dump valves.',
     'Hangers bolted to the coach builder’s frame extension (not welded). Lockable lid, baffled vent, low drain, skid plate. Packs fused inside the box at their terminals.',
     '48 V up through the floor into the desk base (%s) · alternator 48 V run from the cab (about 16 ft).' % ft('48V, RV5 to batteries')),
    ('3', 'dc', 'Main DC disconnect, PV breakers, pack fuse', 'Disconnect and both PV breakers inside the desk base next to the RV5. The pack fuse goes in the battery box.',
     'Desk base, beside #1 · pack fuse in #2', 'Shares the desk base with the RV5.',
     'Reachable from inside the coach without crawling under. (The 3D model draws the disconnect on the box; this map moves it inside.)',
     'Sits between the packs and the RV5, and between each PV trunk and its RV5 input.'),
    ('4', 'dc', 'Bluetti Epad (control screen)', 'On the roadside wall at the desk, just above the desk base.',
     'x 26–28 in · roadside wall · eye level when seated', 'Wall space only.',
     'Surface mount. Ethernet to the RV5 directly below.', 'Data cable to #1 (under 3 ft).'),
    ('5', 'pv', 'Roof cable gland', 'Rear roadside corner of the roof, directly above the desk.',
     'x 8–13 in · 36–41 in roadside of centre', 'Nothing. New sealed penetration (or the factory solar side-port if it lands here).',
     'Sealed gland with written roof-warranty coverage. The two PV trunks drop inside the rear roadside wall into the desk base.',
     'Both PV trunks from #7 to #1.'),
    ('6', 'pv', '6 × Callsun 275 W panels', 'Roof, one crosswise row of six: panels 1–3 behind the AC, panels 4–6 ahead of it, running onto the cab-over roof.',
     'x 12–105 and 152–245 in · each 68.35 in across the roof', 'Roof space only. The existing fans and skylight sit under the panels (see fit check).',
     'Z-brackets or a low rail, about 2.5 in off the roof. Walk margin left on both sides.',
     'Panel leads to #7 (4–12 ft each, about %d ft total).' % round(sum(v for k, v in RUNS.items() if k.startswith('PV_panel')) / 12)),
    ('7', 'pv', 'Combiner box (3 + 3, 25 A per panel)', 'Roof centreline, between panels 1–3 and the AC.',
     'x 106–113 in · centreline', 'Nothing.', 'Bolted to the roof, sealed. Two groups of three, each with a 25 A fuse per panel.',
     'Panels in; two PV trunks out to #5 then #1 (%s each).' % ft('PV trunk, combiner to RV5 (x2 runs)')),
    ('8', 'ac', 'Furrion Chill Cube 18K (ducted)', 'The existing 14 × 14 in AC opening. Swaps one-for-one with the factory unit.',
     'Opening modelled at x 116–145 in (centre x 130). Real position unverified.', 'The factory AC (removed). Its ceiling assembly is replaced by the Chill Cube air distribution box, which feeds the existing ducts.',
     'Bolts through the existing opening. Confirm the air distribution box mates to the factory ducts before buying.',
     '120 V from the main panel (RV5 output).'),
    ('9', 'dc', 'Starlink Mini', 'Roof, roadside of the AC on a flat mount.',
     'x 124–137 in · 22–33 in roadside of centre', 'Roof space only.', 'Flat mount, adhesive or bolted. Cable rides the PV gland or the AC chase.',
     '12 V from the RV5 12 V output.'),
    ('10', 'alt', '2 × Victron Orion-Tr 12/48', 'Under the passenger (curbside) cab seat, close to the starter battery.',
     'x 206–223 in · curbside · under the seat base', 'Space under the passenger seat. The cab seats swivel to face the table, so the swivel base must leave room (fit check).',
     'Screwed to the seat base or the floor beside it. Ignition-switched. Fuse at the starter battery.',
     '12 V from the starter battery (about 3 ft) · 48 V back to the packs along the curbside rail (about 16 ft, about 16 A, so a small cable).'),
    ('11', 'ac', 'Transfer switch', 'In the base of the pantry, curbside, just forward of the lift bed. Candidate spot: move it next to the factory power center if that turns out to be nearby.',
     'x 73–79 in · curbside · floor of the pantry', 'The bottom shelf of the pantry.', 'Screwed to the floor. Service through the pantry door.',
     'Generator in (length depends on the generator bay, unverified) · shore in through #12 · out to the RV5 AC input (about 9 ft).'),
    ('12', 'ac', 'Surge protector / EMS (hardwired)', 'Beside the transfer switch in the pantry base.',
     'x 79–85 in · curbside', 'The bottom shelf of the pantry.', 'Screwed to the floor next to #11.',
     'Shore inlet in (inlet location unverified) · out to #11.'),
    ('13', 'wash', 'Splendide WDV2200XCD (vented)', 'Curbside corner at the forward end of the lift bed, backed against the curbside wall with its side against the pantry wall.',
     'x 48.9–72.4 in · y 20.9–43.5 in curbside of centre · footprint 23½ W × 22⅝ D × 33⅛ H in (plus about 0.6 in plinth) · centre about 33 in behind the rear axle', 'Garage floor in that corner, under the forward end of the bed.',
     'Bracket to the floor. Fits under the lowered bed only if the bed\u2019s underside sits at least 33.7 in above the floor (modelled 38 in, unpublished). Vent out the curbside wall. Its rear 4\u00bd in overlaps the forward end of the curbside cargo door opening (x 20\u201354), leaving about 29 in of the opening clear.',
     'Hot and cold cross under the aisle from the bath (shower directly opposite, about 4 ft) or come back from the galley sink. Drain to the grey tank, which the model puts under the floor just ahead of this corner. Own 15 A circuit from the main panel.'),
]

CHECKS = [
    ('Roof fans and skylight under the panels', 'The panels sit 2.5 in off the roof, and the model puts two roof fans and the bath skylight under them. A MaxxFan Deluxe with rain dome is 23.2 × 16.6 in and stands 5.0 in tall closed and 9.1 in with the lid open (retailer spec, overall unit height). It cannot sit under a panel on 2.5 in brackets. See the roof fallback section.'),
    ('Roof length and AC position', 'The row of six spans 233 in from the first panel edge to the last (x 12 to 245). The model treats the roof as flat from the rear cap over the cab-over to about x 300. Measure the flat roof length, whether the cab-over roof is flat and walkable, and the AC opening’s distance from the rear cap.'),
    ('Tail box vs. hitch and spare', 'In the model the box starts right where the receiver tube ends. Measure the gap from the hitch crossmember to the spare, frame-extension height and bolt points, and exhaust-tip position.'),
    ('Desk base size', 'The RV5 is 17.7 × 19.7 × 6.3 in and wants 7.87 in of air at its vents. Measure the factory desk base in the roadside rear corner to confirm it can take the RV5 with a vented front.'),
    ('Passenger seat swivel', 'The cab seats swivel to face the table. Check what’s under the passenger swivel base and whether two Orions (each about 7.3 × 5.1 × 3.1 in) fit without blocking the swivel. Fallback: the floor beside the seat base or the pantry base with the transfer switch.'),
    ('Factory power center and generator bay', 'Find the factory breaker panel and converter, and the generator bay. The transfer switch goes in the pantry base unless the power center is close by.'),
    ('Shore inlet location', 'The model guesses the inlet is at the rear roadside. If it’s forward, the shore run to the transfer switch gets shorter.'),
    ('Cargo doors', 'The factory floorplan shows large cargo doors in the rear wall and on the curbside under the bed. The curbside door swings outward, so it still opens; the washer takes about 4\u00bd in off the forward end of its roughly 33 in opening. Measure the opening.'),
    ('Washer corner', 'Measure the lift bed\u2019s underside fully lowered at the forward curbside corner (needs at least 33.7 in), the floor space from the pantry wall back (needs 23\u00bd in) and out from the curbside wall (needs 22\u215d in), where the bath and galley supply lines run, and where the grey tank inlet is.'),
]


def axle_section():
    WB = 178.0

    def sp(w, x):
        f = w * (x - 94) / WB
        return f, w - f
    build = [(202.0, 30), (25.0, 30), (30.9, 13), (89.4, 58.5), (89.4, 198.5), (60.0, 128),
             (7.9, 214.6), (40.0, 140), (6.0, 130), (148.0, 60.65)]          # washer: curbside corner at the bed's forward end
    heavy = [(107.7, 58.5), (107.7, 198.5)]
    trip = [(290.5, 138), (40, -6), (200, 250)]
    rows = ''
    for pan, extra in (('29.8 lb', []), ('65.7 lb', heavy)):
        for gname, gx in (('midship', 130), ('in the rear garage', 40)):
            items = build + extra + trip + [(350, gx)]
            f = sum(sp(w, x)[0] for w, x in items)
            r = sum(sp(w, x)[1] for w, x in items)
            rows += ('<tr><td>Panels %s each · gear %s</td><td class="mono">%+.0f lb</td><td class="mono">%+.0f lb</td>'
                     '<td class="mono"><strong>%s lb</strong></td><td class="mono">%s lb</td></tr>' % (
                         pan, gname, f, r, format(round(7275 - r), ','), format(round(4630 - f), ',')))
    return rows


def page():
    imgs = [('img/factory-floorplan.png', 'Factory 22NF floorplan (East to West)'), ('img/05_xray_ann.jpg', 'Power system X-ray (3D model, interior out of date)'),
            ('img/04b_tail_section_ann.jpg', 'Tail section (3D model)')]
    rows = ''
    for n, sys, part, where, pos, disp, mount, conn in SCHED:
        rows += ('<tr><td><span class="chip %s">%s</span></td><td><strong>%s</strong><span class="where">%s</span></td>'
                 '<td class="mono">%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (sys, n, part, where, pos, disp, mount, conn))
    checks = ''.join('<li><strong>%s.</strong> %s</li>' % c for c in CHECKS)
    refs = ''.join('<figure><img src="%s" alt="%s"><figcaption>%s</figcaption></figure>' % (p, a, a) for p, a in imgs)
    tpl = open(os.path.join(HERE, 'install_template.html')).read()
    return (tpl.replace('{{PLAN}}', view_plan()).replace('{{SIDE}}', view_side())
            .replace('{{UNDER}}', view_under()).replace('{{ROOF}}', view_roof())
            .replace('{{ROWS}}', rows).replace('{{CHECKS}}', checks).replace('{{REFS}}', refs).replace('{{AXLE}}', axle_section()))


def main():
    os.makedirs(os.path.join(OUT, 'img'), exist_ok=True)
    for f in ('05_xray_ann.jpg', '04b_tail_section_ann.jpg'):
        shutil.copy(os.path.join(ROOT, 'book', 'img', f), os.path.join(OUT, 'img', f))
    open(os.path.join(OUT, 'index.html'), 'w').write(page())
    print('install map written', W, H_PLAN, H_SIDE)


if __name__ == '__main__':
    main()
