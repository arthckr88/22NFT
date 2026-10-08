"""Annotated overlays (labels, leader lines, dimensions) on the renders.

usage: python3 annotate.py [SHOT ...]   -> renders/annotated/<SHOT>.jpg
Style follows the Andrew Rose design system: bone #F3F1EC on ink, IBM Plex Mono
uppercase tracked labels, 1 px hairlines, no shadows, square scrims.
"""
import json
import math
import os
import sys

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from specs import *  # noqa

ROOT = os.path.dirname(HERE)
R = os.path.join(ROOT, 'renders')
OUT = os.path.join(R, 'annotated')
os.makedirs(OUT, exist_ok=True)
FONTS = os.environ.get('AR_FONTS', '/home/claude/fonts')
AX = json.load(open(os.path.join(ROOT, 'docs', 'axles.json')))

BONE = (243, 241, 236)
MUTE = (124, 124, 124)
INK = (0, 0, 0)
ACCENT = {'pv': (255, 170, 60), 'dc': (90, 150, 255), 'alt': (80, 220, 150), 'ac': (175, 140, 255)}


def font(kind='mono', size=22):
    if kind == 'mono':
        return ImageFont.truetype(os.path.join(FONTS, 'IBMPlexMono-Medium.ttf'), size)
    f = ImageFont.truetype(os.path.join(FONTS, 'Jost.ttf'), size)
    try:
        f.set_variation_by_axes([300])
    except Exception:
        pass
    return f


def tracked(d, xy, text, f, fill, track=0.16):
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=f, fill=fill)
        x += f.getlength(ch) + f.size * track
    return x


def text_w(text, f, track=0.16):
    return sum(f.getlength(c) + f.size * track for c in text) - f.size * track


class Canvas:
    def __init__(self, shot, src=None):
        self.shot = shot
        self.im = Image.open(os.path.join(R, (src or shot) + '.png')).convert('RGB')
        meta = json.load(open(os.path.join(R, shot + '.json')))
        self.a = {k: (v[0], v[1]) for k, v in meta['anchors'].items()}
        self.meta = meta
        self.ov = Image.new('RGBA', self.im.size, (0, 0, 0, 0))
        self.d = ImageDraw.Draw(self.ov)
        self.f = font('mono', 21)
        self.fs = font('mono', 17)

    def P(self, k):
        return self.a[k]

    def label(self, k_or_xy, text, dx, dy, sub=None, color=BONE, dot=True, left_edge=None):
        x, y = self.P(k_or_xy) if isinstance(k_or_xy, str) else k_or_xy
        tx, ty = x + dx, y + dy
        lines = [text.upper()] + ([sub.upper()] if sub else [])
        w = max(text_w(lines[0], self.f), text_w(lines[1], self.fs) if sub else 0) + 24
        h = 36 + (26 if sub else 0)
        left = tx - w if dx < 0 else tx
        if left_edge is not None:
            left = left_edge
            dx = -1 if (left + w / 2) < x else 1
        W, H = self.im.size
        left = min(max(left, 8), W - w - 8)
        ty = min(max(ty, h / 2 + 8), H - 100 - h / 2)
        top = ty - h / 2
        # leader: elbow from anchor to the label edge
        ex = left + w if dx < 0 else left
        self.d.line([(x, y), (ex - (12 if dx < 0 else -12) * 0, ty)], fill=color + (230,), width=2)
        if dot:
            self.d.ellipse([x - 5, y - 5, x + 5, y + 5], fill=color + (255,))
        self.d.rectangle([left, top, left + w, top + h], fill=(0, 0, 0, 205), outline=(243, 241, 236, 60), width=1)
        tracked(self.d, (left + 12, top + 7), lines[0], self.f, color + (255,))
        if sub:
            tracked(self.d, (left + 12, top + 36), lines[1], self.fs, MUTE + (255,))

    def dim(self, p1, p2, text, off=0, side=1, color=BONE, ext=True):
        """Dimension line between two points (pixels), offset perpendicular by off."""
        (x1, y1), (x2, y2) = (self.P(p1) if isinstance(p1, str) else p1), (self.P(p2) if isinstance(p2, str) else p2)
        dx, dy = x2 - x1, y2 - y1
        L = math.hypot(dx, dy) or 1
        nx, ny = -dy / L * off, dx / L * off
        a1, a2 = (x1 + nx, y1 + ny), (x2 + nx, y2 + ny)
        if ext and off:
            self.d.line([(x1, y1), a1], fill=color + (120,), width=1)
            self.d.line([(x2, y2), a2], fill=color + (120,), width=1)
        self.d.line([a1, a2], fill=color + (240,), width=2)
        for (px, py), s in ((a1, 1), (a2, -1)):
            ux, uy = dx / L * s, dy / L * s
            self.d.line([(px, py), (px + ux * 14 - uy * 6, py + uy * 14 + ux * 6)], fill=color + (240,), width=2)
            self.d.line([(px, py), (px + ux * 14 + uy * 6, py + uy * 14 - ux * 6)], fill=color + (240,), width=2)
        mx, my = (a1[0] + a2[0]) / 2, (a1[1] + a2[1]) / 2
        w = text_w(text.upper(), self.fs) + 16
        W, H = self.im.size
        mx = min(max(mx, w / 2 + 8), W - w / 2 - 8)
        self.d.rectangle([mx - w / 2, my - 15, mx + w / 2, my + 15], fill=(0, 0, 0, 225))
        tracked(self.d, (mx - w / 2 + 8, my - 11), text.upper(), self.fs, color + (255,))

    def at(self, k, text, tx, ty, sub=None, color=BONE):
        """Label whose box starts at left edge tx, centred on row ty, with a leader to anchor k."""
        x, y = self.P(k) if isinstance(k, str) else k
        self.label((x, y), text, 1, ty - y, sub, color, left_edge=tx)

    def dimh(self, xa, xb, y, text, ref=None):
        """Horizontal dimension at pixel row y between pixel columns xa, xb; ref = rows the witness lines start from."""
        if ref:
            for x, yr in ((xa, ref[0]), (xb, ref[1])):
                self.d.line([(x, yr), (x, y)], fill=BONE + (110,), width=1)
        self.dim((xa, y), (xb, y), text, off=0, ext=False)

    def dimv(self, x, ya, yb, text, ref=None):
        if ref:
            for y, xr in ((ya, ref[0]), (yb, ref[1])):
                self.d.line([(xr, y), (x, y)], fill=BONE + (110,), width=1)
        self.dim((x, ya), (x, yb), text, off=0, ext=False)

    def title(self, idx, name, sub):
        W, H = self.im.size
        self.d.rectangle([0, H - 92, W, H], fill=(0, 0, 0, 215))
        self.d.line([(0, H - 92), (W, H - 92)], fill=(243, 241, 236, 40), width=1)
        tracked(self.d, (40, H - 78), (idx + ' / ' + name).upper(), self.fs, MUTE + (255,), 0.24)
        tracked(self.d, (40, H - 50), sub.upper(), self.f, BONE + (255,), 0.12)

    def save(self, name=None):
        out = Image.alpha_composite(self.im.convert('RGBA'), self.ov).convert('RGB')
        p = os.path.join(OUT, (name or self.shot) + '.jpg')
        out.save(p, quality=90)
        return p

    def px_per_in(self):
        """For ortho shots: pixels per inch."""
        return self.im.size[0] / self.meta['ortho_scale_in']


def ann_02():
    c = Canvas('02_elevation')
    fx, gy = c.P('front')[0], c.P('ground')[1]
    rx = c.P('rear')[0]
    top = c.P('top')[1]
    c.dimh(fx, rx, top - 40, 'Coach 26 ft 0 in (312 in) · confirmed', ref=(c.P('front')[1], c.P('rear')[1]))
    c.dimh(c.P('fa')[0], c.P('ra')[0], gy + 60, 'Wheelbase 178 in · confirmed', ref=(gy, gy))
    c.dimv(fx - 30, gy, top, 'Height 137 in', ref=(fx, c.P('top')[0]))
    c.dimv(rx + 45, gy, c.P('floor')[1], 'Floor 36 in · est', ref=(rx, rx))
    c.dimh(c.P('carfront')[0], c.P('carrear')[0], gy - 230, 'Abarth 144.4 in')
    c.label('box', 'Batteries + box', 120, 150, 'Tail, by the spare · bottom 12 in · est')
    c.title('02', 'Elevation', 'Driver side · front left · Abarth flat-towed')
    return c.save()


def ann_03():
    c = Canvas('03_roof')
    y_top = c.P('ey1')[1]
    y_bot = c.P('ey0')[1]
    pb = c.P('pl')[1]
    c.dimh(c.P('g1a')[0], c.P('g1b')[0], pb + 26, 'Rear group 92.9 in')
    c.dimh(c.P('g2a')[0], c.P('g2b')[0], pb + 26, 'Front group 92.9 in')
    c.dimv(c.P('g2b')[0] + 30, c.P('pl')[1], c.P('pr')[1], 'Panel 68.35 in')
    c.dimv(c.P('rear')[0] - 40, y_bot, y_top, 'Width 91 in · est', ref=(c.P('rear')[0], c.P('rear')[0]))
    c.dimh(c.P('rear')[0], c.P('cabseam')[0], y_bot + 60, 'Flat roof 234 in · est', ref=(y_bot, y_bot))
    c.at('gland', 'Roof entry', 40, 60, 'Rear chase down to the RV5')
    c.at('ac', 'Chill Cube 18K', 880, 60, '29.5 × 29 in · existing 14×14 opening')
    c.at('comb', 'Combiner', 420, 150, '6 × 25A fuses · PV1 / PV2')
    c.at('starlink', 'Starlink Mini', 1180, 150, 'Flat mount · 11.4 × 9.8 in')
    c.at('fan1', 'Bath fan', 40, 235, 'Under panel · low-profile cover')
    c.at('fan2', 'Galley fan', c.P('fan2')[0] - 60, y_bot + 140, 'Under panel · low-profile cover')
    c.at('fan3', 'Cabover fan', c.P('fan3')[0] + 40, y_bot + 140, 'Under panel')
    c.title('03', 'Roof', '6 × Callsun 275W in parallel · 1,650 W · rear left, cab right · roadside at top')
    return c.save()


def ann_04():
    c = Canvas('04_underbelly')
    W, H = c.im.size
    c.at('box', 'Battery box', c.P('box')[0] - 260, H - 260, '2 × B4810 · 52 × 18 × 7.5 in · about 227 lb')
    c.at('spare', 'Spare tire', c.P('spare')[0] + 120, 140, 'Stays in place, ahead of the box')
    c.at('hitch', 'Hitch receiver', 120, 160, 'Lowest point at the tail')
    c.at('exhaust', 'Exhaust exit', c.P('exhaust')[0] + 60, H - 260, 'Turns out ahead of the box')
    c.at('axle', 'Rear axle', c.P('axle')[0] + 80, 260)
    c.title('04', 'Underbelly', 'Curbside, under the skirt · battery box between the spare and the hitch')
    return c.save()


def ann_04b():
    c = Canvas('04b_tail_section')
    W, H = c.im.size
    tx, ty = c.P('tire')
    rows = [('hitch', (200, 200, 200), 'Hitch receiver 9.1°'), ('boxrear', (255, 170, 60), 'Battery box 9.3°'),
            ('tail', (200, 200, 200), 'Rear skirt 14.3°')]
    for i, (k, col, txt) in enumerate(rows):
        x, y = c.P(k)
        dx, dy = x - tx, y - ty
        ext = ((W - 30) - tx) / dx if dx > 0 else (30 - tx) / dx
        ex, ey = tx + dx * ext, ty + dy * ext
        c.d.line([(tx, ty), (ex, ey)], fill=col + (235,), width=3 if k == 'boxrear' else 2)
        c.d.ellipse([x - 6, y - 6, x + 6, y + 6], fill=col + (255,))
        c.label((x, y), txt, 1, [700, 770, 840][i] - y, None, col, dot=False, left_edge=W - 430)
    gy = c.P('boxground')[1]
    bx0, by = c.P('boxrear')
    bx1, _ = c.P('boxfront')
    c.dimv(bx0 - 30, gy, by, 'Clearance 12 in · est', ref=(bx0, bx0))
    c.dimh(bx0, bx1, by + 40, 'Box 18 in')
    c.dimh(bx0, tx, gy + 40, 'Box to tire contact 73 in', ref=(gy, gy))
    c.at('frame', 'Frame bottom 19 in · est', c.P('frame')[0] + 260, 120)
    c.at('floor', 'Floor 36 in · est', c.P('floor')[0] + 520, 200)
    c.at('spare', 'Spare tire', c.P('spare')[0] + 180, H - 220)
    c.title('04B', 'Tail section', 'Departure angle · the hitch receiver limits first; the box clears it by 0.2°')
    return c.save()


def ann_05():
    c = Canvas('05_xray')
    W, H = c.im.size
    runs = c.meta['runs_in']

    def ft(k):
        return '%.0f ft' % (runs[k] / 12 + 0.49)
    pv_panels = sum(v for k, v in runs.items() if k.startswith('PV_panel')) / 12
    c.at('panels', 'Panels to combiner', 1380, 110, '6 leads · %.0f ft in all' % pv_panels, ACCENT['pv'])
    c.at('comb', 'Combiner', 620, 80, '25A fuse per panel', ACCENT['pv'])
    c.at('trunk', 'PV trunk', 70, 190, '2 runs · about ' + ft('PV trunk, combiner to RV5 (x2 runs)') + ' each', ACCENT['pv'])
    c.at('shore', 'Shore inlet', 70, 310, ft('120V, shore inlet to transfer switch') + ' to the transfer switch', ACCENT['ac'])
    c.at('rv5', 'RV5 hub', 70, 430, 'Desk pedestal · ' + ft('48V, RV5 to batteries') + ' of 48V to the packs', ACCENT['dc'])
    c.at('batt', 'B4810 × 2', 70, 640, '10.24 kWh · under the tail', ACCENT['dc'])
    c.at('acin', 'AC in to RV5', 420, 930, ft('120V, transfer switch to RV5 AC in') + ' under the floor', ACCENT['ac'])
    c.at('alt48', 'Alternator, 48V run', 860, 930, ft('48V, Orions to batteries') + ' along the curbside rail', ACCENT['alt'])
    c.at('gen', 'Generator 4,000 W', 1280, 800, ft('120V, generator to transfer switch') + ' to the transfer switch', ACCENT['ac'])
    c.at('orion', 'Orion-Tr × 2', 1500, 930, '12V lead ' + ft('12V, starter battery to Orions') + ' · under the passenger seat', ACCENT['alt'])
    c.title('05', 'Power system', 'Amber solar · blue 48V · green alternator · violet 120V · lengths approximate')
    return c.save()


def ann_08():
    c = Canvas('08_laundry_A')
    c.at('washer', 'WDV2200XCD', 1100, 640, 'Vented · 23.5 × 33.1 × 22.6 in · 148 lb')
    c.at('counter', 'Raised counter', 1150, 60, '38 in · fold and charge')
    c.at('vent', 'Wall vent', 1280, 330, 'Roadside wall behind the dryer · about 1 ft of duct')
    c.at('bath', 'Bath wall', 60, 260, 'Hot and cold from the bath manifold, about 2 ft')
    c.at('fridge', 'Fridge', 1640, 140)
    c.title('08', 'Laundry A', 'Bath side · replaces the drawer stack · raised counter above')
    return c.save()


def ann_09():
    c = Canvas('09_laundry_B')
    pts = [c.P(k) for k in ('bl1', 'bl2', 'bl3', 'bl4', 'bl1')]
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        n = int(math.hypot(x2 - x1, y2 - y1) // 14)
        for i in range(0, n, 2):
            a, b = i / n, min(1, (i + 1) / n)
            c.d.line([(x1 + (x2 - x1) * a, y1 + (y2 - y1) * a), (x1 + (x2 - x1) * b, y1 + (y2 - y1) * b)],
                     fill=(255, 170, 60, 235), width=3)
    c.at('bl2', 'Lift bed, lowered', 200, 120, 'Underside 38 in above the floor · estimate', (255, 170, 60))
    c.at('wtop', 'Washer top 33.7 in', 60, 330, 'About 4 in under the lowered bed')
    c.at('washer', 'WDV2200XCD', 980, 640, 'Garage, curbside rear corner')
    c.at('vent', 'Rear wall vent', 1180, 210, 'About 1 ft of duct')
    c.at('desk', 'Desk', 1560, 520, 'Washer about 2 ft from the chair')
    c.title('09', 'Laundry B', 'Rear garage · water about 13 ft from the bath manifold · load with the bed up')
    return c.save()


def ann_10():
    c = Canvas('10_floorplan')
    rows = [('rv5', 'RV5 hub', 40, 100), ('bath', 'Bath', 470, 100), ('fridge', 'Fridge', 900, 100),
            ('dinette', 'Dinette', 1240, 100), ('desk', 'Desk 29.5 in · bed lifts above', 150, 180),
            ('laundryA', 'Laundry A', 650, 180), ('laundryB', 'Laundry B', 40, 870), ('galley', 'Galley', 560, 870),
            ('pantry', 'Pantry', 860, 870), ('bench', 'Bench', 1300, 870), ('batt', 'Batteries, below floor', 40, 940),
            ('hatch', 'Load hatch', 520, 940), ('door', 'Entry door', 1000, 940), ('ts', 'Transfer switch', 1330, 940),
            ('orion', 'Orion-Tr × 2, under seat', 1500, 640), ('gen', 'Generator, below', 1500, 760)]
    for k, t, x, y in rows:
        c.at(k, t, x, y)
    y0 = c.P('rear')[1] - 290
    c.dimh(c.P('rear')[0], c.P('front')[0], 250, 'House 232 in · estimate')
    c.title('10', 'Floorplan', 'Cut at 50 in · both laundry options shown · rear left, roadside at top')
    return c.save()


def ann_11():
    c = Canvas('11_axles')
    rows = {r['item']: r for r in AX['rows_A']}
    rb = {r['item']: r for r in AX['rows_B']}

    def lab(k, item, tx, ty):
        r = rows.get(item) or rb.get(item)
        c.at(k, '%s · %.0f lb' % (item, r['lb']), tx, ty, 'Front %+.0f · rear %+.0f lb' % (r['front'], r['rear']))
    lab('pf', 'Solar, front 3 panels', 60, 60)
    lab('pr', 'Solar, rear 3 panels', 1300, 60)
    lab('wa', 'Washer-dryer (A)', 760, 170)
    lab('rv5', 'RV5 hub', 1480, 300)
    lab('orion', '2 x Orion-Tr', 60, 520)
    lab('batt', '2 x B4810 batteries', 1380, 560)
    ta, tb = AX['total_A'], AX['total_B']
    c.at('fa', 'Front axle %+.0f lb (A) · %+.0f lb (B)' % (ta['front'], tb['front']), 40, 930, 'Rated 4,630 lb')
    c.at('ra', 'Rear axle %+.0f lb (A) · %+.0f lb (B)' % (ta['rear'], tb['rear']), 1180, 930, 'Rated 7,275 lb')
    c.title('11', 'Weight', 'Build adds about %.0f lb · nearly all of it lands on the rear axle' % ta['lb'])
    return c.save()


ALLS = dict(_02=ann_02, _03=ann_03, _04=ann_04, _04b=ann_04b, _05=ann_05, _08=ann_08, _09=ann_09, _10=ann_10,
            _11=ann_11)

if __name__ == '__main__':
    want = sys.argv[1:] or list(ALLS)
    for k in want:
        try:
            print(ALLS[k if k.startswith('_') else '_' + k]())
        except FileNotFoundError as e:
            print('missing', k, e)
