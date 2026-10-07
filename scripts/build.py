"""Builds the full Alita 22NFT scene. Import and call build()."""
import math
import json
import bpy
from mathutils import Vector

import lib
from lib import IN, I, box, cyl, profile_extrude, arc, coll, principled, emission
from specs import *

# ------------------------------------------------------------------ palette
def mats():
    M = {}
    M['paint'] = principled('Paint', (0.80, 0.78, 0.74), rough=0.38, coat=0.35)
    M['graphite'] = principled('Graphite', (0.03, 0.032, 0.035), rough=0.4, metal=0.15, coat=0.6)
    M['lining'] = principled('Lining', (0.075, 0.07, 0.066), rough=0.85)
    M['ceiling'] = principled('Ceiling', (0.33, 0.31, 0.29), rough=0.8)
    M['glass'] = principled('TintGlass', (0.02, 0.025, 0.03), rough=0.02, transmission=0.9, ior=1.5)
    M['glass_frost'] = principled('FrostGlass', (0.6, 0.6, 0.6), rough=0.35, transmission=0.8)
    M['black'] = principled('BlackPlastic', (0.015, 0.015, 0.016), rough=0.55)
    M['blackgloss'] = principled('BlackGloss', (0.01, 0.01, 0.012), rough=0.1, coat=1.0)
    M['rubber'] = principled('Rubber', (0.018, 0.018, 0.018), rough=0.75)
    M['rim'] = principled('Rim', (0.55, 0.56, 0.58), rough=0.25, metal=1.0)
    M['rimdark'] = principled('RimDark', (0.08, 0.085, 0.09), rough=0.3, metal=1.0)
    M['steel'] = principled('Steel', (0.35, 0.35, 0.36), rough=0.35, metal=1.0)
    M['frame'] = principled('FrameBlack', (0.03, 0.03, 0.03), rough=0.6, metal=0.3)
    M['powder'] = principled('PowderCoat', (0.025, 0.026, 0.028), rough=0.55, metal=0.2)
    M['alu'] = principled('Aluminium', (0.7, 0.71, 0.73), rough=0.3, metal=1.0)
    M['white'] = principled('WhitePlastic', (0.85, 0.85, 0.84), rough=0.4)
    M['solar'] = lib.solar_material()
    M['walnut'] = lib.wood_material('Walnut')
    M['floor'] = lib.wood_material('FloorOak', base=(0.13, 0.11, 0.09), dark=(0.06, 0.05, 0.04))
    M['fabric'] = principled('Fabric', (0.06, 0.06, 0.065), rough=0.95)
    M['fabric_light'] = principled('FabricSand', (0.42, 0.38, 0.33), rough=0.95)
    M['quartz'] = principled('Quartz', (0.06, 0.06, 0.062), rough=0.18, coat=0.4)
    M['brass'] = principled('Brass', (0.55, 0.42, 0.24), rough=0.3, metal=1.0)
    M['washer'] = principled('WasherWhite', (0.82, 0.82, 0.8), rough=0.3)
    M['led'] = emission('LEDWarm', (1.0, 0.72, 0.42), 18.0)
    M['led_soft'] = emission('LEDSoft', (1.0, 0.75, 0.48), 6.0)
    M['screen'] = emission('Screen', (0.10, 0.14, 0.2), 0.8)
    M['amber'] = emission('MarkerAmber', (1.0, 0.45, 0.05), 3.0)
    M['headlight'] = principled('HeadlightLens', (0.8, 0.82, 0.85), rough=0.05, transmission=0.6)
    M['smoked'] = principled('SmokedLens', (0.05, 0.045, 0.04), rough=0.08, coat=1.0)
    M['car'] = principled('CarGraphite', (0.03, 0.032, 0.036), rough=0.35, metal=0.0, coat=1.0)
    return M


SIDE_WINDOWS = [
    # (side, x0, x1, z0, z1) side +1 roadside, -1 curbside
    (+1, 30, 60, 60, 86),     # office roadside
    (+1, 82, 96, 78, 88),     # bath (frosted)
    (+1, 170, 214, 60, 86),   # dinette
    (-1, 34, 60, 62, 86),     # office curbside
    (-1, 90, 132, 74, 88),    # galley
    (-1, 200, 226, 62, 86),   # front curbside seat
]
REAR_WINDOW = (-18, 18, 72, 88)   # y0, y1, z0, z1
DOOR = (166, 194, 38, 112)        # curbside entry door x0, x1, z0, z1


# ------------------------------------------------------------------ shell
def build_shell(M, C):
    z0 = 24.0
    R = ROOF_Z
    pts = [(0.0, z0 + 4), (0.0, R - 12)]
    pts += arc(12, R - 12, 12, 180, 90, 8)[1:]
    pts += [(246.0, R)]
    # cabover nose
    pts += [(260, R - 0.6), (273, R - 3), (285, R - 8), (295, R - 15), (301, R - 23),
            (302.5, R - 29), (300, R - 34), (292, R - 36.5), (278, R - 37)]
    pts += [(238.0, 84.0), (234.0, 82.0), (232.0, 78.0), (232.0, z0), (3.0, z0)]
    shell = profile_extrude('Shell', pts, -HALF, HALF, M['paint'], C['Shell'], bevel=3.5, seg=6)
    shell.data.materials.append(M['lining'])
    lib.apply_mods(shell)
    sol = shell.modifiers.new('solid', 'SOLIDIFY')
    sol.thickness = 2.0 * IN
    sol.offset = -1.0
    sol.material_offset = 1
    sol.use_even_offset = True
    lib.apply_mods(shell)

    cutters = []
    for side, x0, x1, za, zb in SIDE_WINDOWS:
        y = side * HALF
        cutters.append(box('cut', x0, x1, y - 4, y + 4, za, zb, None, C['Shell'], bevel=3, seg=4))
    y0, y1, za, zb = REAR_WINDOW
    cutters.append(box('cut', -4, 4, y0, y1, za, zb, None, C['Shell'], bevel=3, seg=4))
    # rear wheel well
    cutters.append(cyl('cut', X_REAR_AXLE, 0, 14, 17.5, 100, None, C['Shell'], axis='Y', verts=64))
    for cu in cutters:
        lib.apply_mods(cu)
    lib.boolean_diff(shell, cutters)
    shell.data.set_sharp_from_angle(angle=math.radians(40))

    # ceiling lining with cove
    box('Ceiling', 3, 231, -HALF + 2.2, HALF - 2.2, CEIL_Z, CEIL_Z + 1, M['ceiling'], C['Interior'])
    for side in (-1, 1):
        box('CoveLED', 6, 228, side * (HALF - 3.2) - 0.25, side * (HALF - 3.2) + 0.25,
            CEIL_Z - 0.3, CEIL_Z, M['led_soft'], C['Interior'])

    # glass, frameless and flush, rounded
    for side, x0, x1, za, zb in SIDE_WINDOWS:
        y = side * (HALF + 0.15)
        g = box('Window', x0 - 1.2, x1 + 1.2, y - 0.3, y + 0.3, za - 1.2, zb + 1.2,
                M['glass_frost'] if (x0 == 82) else M['glass'], C['Shell'], bevel=3.5, seg=5)
    y0, y1, za, zb = REAR_WINDOW
    box('RearWindow', -0.75, -0.15, y0 - 1.2, y1 + 1.2, za - 1.2, zb + 1.2, M['glass'], C['Shell'], bevel=3.5, seg=5)

    # graphite lower sweep, both sides
    for side in (-1, 1):
        sweep = [(1.5, z0 + 0.5), (1.5, 46), (120, 46), (175, 50), (231, 56), (231, z0 + 0.5)]
        y = side * HALF
        profile_extrude('Sweep', sweep, y - 0.12 if side > 0 else y - 0.35,
                        y + 0.35 if side > 0 else y + 0.12, M['graphite'], C['Shell'], bevel=0.3, seg=2)
        # beltline pinstripe
        box('Belt', 2, 231, y - 0.2, y + 0.2, 52.5, 53.0, M['graphite'], C['Shell'])
    # rear cap graphite band and lights
    box('RearBand', -0.4, 0.6, -HALF + 3, HALF - 3, z0 + 0.5, 46, M['graphite'], C['Shell'], bevel=0.5)
    for side in (-1, 1):
        box('TailLamp', -0.8, 0.6, side * 40 - 2.5, side * 40 + 2.5, 50, 72, M['smoked'], C['Shell'], bevel=1.2)
    box('RearMarkerBar', -0.7, 0.2, -16, 16, R - 6, R - 4.5, M['amber'], C['Shell'], bevel=0.3)
    # cabover marker lights and light bar
    box('CaboverLightBar', 296, 301, -30, 30, R - 21, R - 19.5, M['led_soft'], C['Shell'], bevel=0.4)
    for y in (-12, 0, 12):
        box('Marker', 300.5, 302.6, y - 1.5, y + 1.5, R - 28, R - 27, M['amber'], C['Shell'], bevel=0.3)
    # roof edge gutters
    for side in (-1, 1):
        box('Gutter', 8, 246, side * (HALF - 1.2) - 0.6, side * (HALF - 1.2) + 0.6, R - 0.2, R + 1.2,
            M['white'], C['Shell'], bevel=0.4)

    # entry door (curbside) with gap ring and window
    x0, x1, za, zb = DOOR
    y = -HALF
    box('DoorGap', x0 - 0.3, x1 + 0.3, y - 0.2, y + 0.05, za - 0.3, zb + 0.3, M['black'], C['Shell'], bevel=2.2)
    box('Door', x0, x1, y - 0.55, y + 0.0, za, zb, M['paint'], C['Shell'], bevel=2, seg=4)
    box('DoorWindow', x0 + 4, x1 - 4, y - 0.75, y - 0.45, 80, 104, M['glass'], C['Shell'], bevel=2.5)
    box('DoorHandle', x0 + 2, x0 + 3.5, y - 1.3, y - 0.5, 70, 76, M['steel'], C['Shell'], bevel=0.4)
    box('Step', x0 + 1, x1 - 1, y - 12, y - 1, 20, 21.5, M['steel'], C['Shell'], bevel=0.3)
    box('PorchLight', x1 + 3, x1 + 9, y - 1.0, y - 0.2, zb - 3, zb - 1, M['led'], C['Shell'], bevel=0.3)

    # compartment doors on the skirt (and the garage load hatch)
    comps = [(-1, 200, 226, 26, 44, 'Gen'), (-1, 140, 162, 26, 44, ''), (+1, 180, 206, 26, 44, 'LP'),
             (+1, 140, 166, 26, 44, ''), (-1, 34, 60, 40, 58, 'Hatch'), (+1, 8, 24, 28, 44, 'Shore')]
    for side, x0, x1, za, zb, tag in comps:
        y = side * HALF
        o = side * 0.55
        box('CompGap', x0 - 0.25, x1 + 0.25, y - 0.1, y + 0.1, za - 0.25, zb + 0.25, M['black'], C['Shell'], bevel=1.2)
        box('CompDoor' + tag, x0, x1, min(y, y + o), max(y, y + o), za, zb, M['graphite'], C['Shell'], bevel=1.0)
        for xx in ((x0 + 3,) if (x1 - x0) < 20 else (x0 + 3, x1 - 3)):
            box('Lock', xx - 0.6, xx + 0.6, min(y + o, y + 2 * o), max(y + o, y + 2 * o), zb - 4, zb - 2.8,
                M['steel'], C['Shell'], bevel=0.2)
    if True:  # generator exhaust louvres
        for k in range(5):
            box('Louvre', 204, 222, -HALF - 0.9, -HALF - 0.6, 29 + k * 3, 30 + k * 3, M['black'], C['Shell'])

    # awning cassette curbside, 16 ft
    box('Awning', 58, 250, -HALF - 4.5, -HALF - 0.3, 108, 115, M['black'], C['Shell'], bevel=1.6, seg=4)
    box('AwningLED', 60, 248, -HALF - 4.6, -HALF - 3.6, 107.6, 108.0, M['led'], C['Shell'])
    return shell


# ------------------------------------------------------------------ cab
def build_cab(M, C):
    W = 40.4
    pts = [(232, 22), (232, 83), (256, 83.5), (261, 82.5), (284, 52), (300, 47), (309, 43),
           (313, 36), (314, 24), (311, 16), (300, 12), (232, 12)]
    cab = profile_extrude('Cab', pts, -W, W, M['paint'], C['Cab'], bevel=4.0, seg=6)
    lib.apply_mods(cab)
    cut = [cyl('cut', X_FRONT_AXLE, 0, 14, 16.5, 100, None, C['Cab'], axis='Y', verts=64)]
    lib.boolean_diff(cab, cut)
    cab.data.set_sharp_from_angle(angle=math.radians(40))
    # windshield: slab lying on the slope (cab outer surface sits ~0 in from profile)
    ang = math.atan2(82.5 - 52, 284 - 261)          # slope angle above horizontal, going forward/down
    cx, cz = (261 + 284) / 2, (82.5 + 52) / 2
    L = math.hypot(284 - 261, 82.5 - 52) - 5
    ws = box('Windshield', -L / 2, L / 2, -33.5, 33.5, -0.25, 0.25, M['glass'], C['Cab'], bevel=3)
    nx, nz = math.sin(ang), math.cos(ang)            # outward normal of the slope
    ws.location = ((cx + 0.35 * nx) * IN, 0, (cz + 0.35 * nz) * IN)
    ws.rotation_euler = (0, ang, 0)

    def span(a, b):
        return min(a, b), max(a, b)
    for side in (-1, 1):
        y = side * (W + 0.1)
        box('CabWindow', 238, 262, y - 0.3, y + 0.3, 56, 79, M['glass'], C['Cab'], bevel=3)
        box('CabDoorSeam', 236, 236.4, y - 0.35, y + 0.35, 20, 82, M['black'], C['Cab'])
        box('CabDoorSeam', 263, 263.4, y - 0.35, y + 0.35, 20, 60, M['black'], C['Cab'])
        ya, yb = span(y, y + side * 0.8)
        box('Handle', 240, 245, ya, yb, 52, 53.5, M['black'], C['Cab'], bevel=0.3)
        ya, yb = span(side * (W + 0.5), side * (W + 8))
        box('MirrorArm', 262, 264, ya, yb, 60, 61.5, M['black'], C['Cab'])
        ya, yb = span(side * (W + 6), side * (W + 13))
        box('Mirror', 260, 264, ya, yb, 56, 72, M['black'], C['Cab'], bevel=1.2)
        ya, yb = span(side * 25, side * 37)
        box('Headlight', 302, 311.5, ya, yb, 39, 45, M['headlight'], C['Cab'], bevel=1.5)
    box('Grille', 310, 314.2, -22, 22, 28, 42, M['black'], C['Cab'], bevel=1.5)
    for k in range(4):
        box('GrilleBar', 313.9, 314.5, -21, 21, 30 + k * 3.2, 30.8 + k * 3.2, M['rimdark'], C['Cab'])
    box('Bumper', 306, 316, -38, 38, 14, 26, M['black'], C['Cab'], bevel=2.5)
    # cab interior essentials
    for side in (-1, 1):
        box('SeatBase', 240, 256, side * 18 - 9, side * 18 + 9, 26, 40, M['black'], C['Cab'], bevel=2)
        box('SeatCushion', 240, 258, side * 18 - 10, side * 18 + 10, 40, 45, M['fabric'], C['Cab'], bevel=2.5)
        box('SeatBack', 236, 241, side * 18 - 10, side * 18 + 10, 44, 74, M['fabric'], C['Cab'], bevel=2.5)
    box('Dash', 268, 284, -38, 38, 54, 64, M['black'], C['Cab'], bevel=3)
    cyl('Wheel', 262, 18, 62, 7.5, 1.2, M['black'], C['Cab'], axis='X')
    # cabover bunk
    box('BunkDeck', 236, 296, -42, 42, 86, 88, M['walnut'], C['Interior'])
    box('BunkMattress', 238, 294, -40, 40, 88, 94, M['fabric_light'], C['Interior'], bevel=2.5, seg=4)
    return cab


# ------------------------------------------------------------------ wheels
def wheel(name, x, y, z, r, width, M, c, outward=1, dual_inner=False, dark=False, rim_ratio=0.6):
    t = cyl(name + 'Tire', x, y, z, r, width, M['rubber'], c, axis='Y', verts=64, bevel=2.3, seg=6)
    rim_r = r * rim_ratio
    dish = width * 0.5 - 0.6
    rim = cyl(name + 'Rim', x, y + outward * (dish - 0.4), z, rim_r, 0.8,
              M['rimdark'] if dark else M['rim'], c, axis='Y', verts=64, bevel=0.35)
    cyl(name + 'Barrel', x, y, z, rim_r - 0.2, width - 1.2, M['rimdark'], c, axis='Y', verts=48)
    cyl(name + 'Hub', x, y + outward * (dish + 0.2), z, rim_r * 0.32, 1.2, M['steel'], c, axis='Y', verts=32, bevel=0.3)
    for k in range(8):
        a = math.radians(k * 45 + 22.5)
        cyl(name + 'Lug', x + math.cos(a) * rim_r * 0.5, y + outward * (dish + 0.4),
            z + math.sin(a) * rim_r * 0.5, 0.55, 1.2, M['steel'], c, axis='Y', verts=12)
        # vent holes read as dark ovals
        cyl(name + 'Vent', x + math.cos(a + 0.39) * rim_r * 0.78, y + outward * (dish + 0.02),
            z + math.sin(a + 0.39) * rim_r * 0.78, 1.25, 0.5, M['black'], c, axis='Y', verts=16)
    return t


def build_running_gear(M, C):
    R = 13.76
    c = C['Chassis']
    for side in (-1, 1):
        wheel('FW', X_FRONT_AXLE, side * 34.0, R, R, 7.7, M, c, outward=side)
        wheel('RWo', X_REAR_AXLE, side * 38.6, R, R, 7.7, M, c, outward=side)
        wheel('RWi', X_REAR_AXLE, side * 29.6, R, R, 7.7, M, c, outward=side)
    # frame rails and cross members
    box('FrameRail', -2, 292, 14, 17, 19, 25, M['frame'], c)
    box('FrameRail', -2, 292, -17, -14, 19, 25, M['frame'], c)
    for x in (2, 44, 80, 130, 180, 225):
        box('CrossMember', x, x + 3, -17, 17, 20, 24, M['frame'], c)
        box('Outrigger', x, x + 3, -HALF + 2, -17, 26, 30, M['frame'], c)
        box('Outrigger', x, x + 3, 17, HALF - 2, 26, 30, M['frame'], c)
    cyl('RearAxle', X_REAR_AXLE, 0, R, 2.6, 60, M['frame'], c, axis='Y')
    diff = cyl('Diff', X_REAR_AXLE, 0, R, 6, 9, M['frame'], c, axis='X', bevel=2)
    cyl('FrontAxle', X_FRONT_AXLE, 0, R, 2.2, 56, M['frame'], c, axis='Y')
    cyl('Driveshaft', (X_REAR_AXLE + 250) / 2, 0, 17, 1.6, 250 - X_REAR_AXLE, M['steel'], c, axis='X')
    for side in (-1, 1):
        box('LeafSpring', X_REAR_AXLE - 26, X_REAR_AXLE + 26, side * 15 - 1.2, side * 15 + 1.2, 16, 19, M['frame'], c)
        box('Shock', X_REAR_AXLE - 4, X_REAR_AXLE - 2, side * 20 - 1, side * 20 + 1, 12, 24, M['steel'], c)
    # exhaust, curbside, exits ahead of the battery box
    lib.curve_path('Exhaust', [(250, -8, 16), (150, -21, 16), (78, -21, 16), (70, -30, 16), (68, -44, 15)],
                   1.2, M['steel'], c)
    # tanks (between the rails) and other underfloor items
    box('FreshTank', 120, 156, -13, 13, 15, 26, M['black'], c, bevel=1.5)
    box('GreyTank', 98, 118, -13, 13, 15, 26, M['black'], c, bevel=1.5)
    box('BlackTank', 66, 96, -13, 13, 15, 26, M['black'], c, bevel=1.5)
    box('FuelTank', 236, 262, 18, 34, 13, 23, M['black'], c, bevel=2)
    box('Generator', 200, 226, -40, -20, 23, 36, M['powder'], c, bevel=1.5)
    for k in range(2):
        cyl('LPTank', 186 + k * 11, 32, 34, 5.2, 18, M['white'], c, axis='Y', bevel=2)
    box('StarterBattery', 258, 268, 16, 26, 24, 32, M['black'], c, bevel=0.6)
    # spare tire, horizontal under the tail
    wheel('Spare', SPARE_X, 0, 17.0, R, 7.7, M, c, outward=1, dark=True)
    sp = [o for o in c.objects if o.name.startswith('Spare')]
    for o in sp:
        # rotate the spare to lie flat about its own centre
        o.rotation_euler = (0, 0, 0)
        loc = Vector(o.location)
        rel = loc - Vector(I(SPARE_X, 0, 17.0))
        o.location = Vector(I(SPARE_X, 0, 17.0)) + Vector((rel.x, -rel.z, rel.y))
    box('SpareCarrier', SPARE_X - 15, SPARE_X + 15, -1, 1, 20.5, 21.5, M['frame'], c)
    # hitch receiver
    box('Receiver', -6, 22, -1.25, 1.25, 16, 18.5, M['powder'], c, bevel=0.2)
    box('HitchCross', 6, 10, -17, 17, 17, 20, M['powder'], c, bevel=0.2)


# ------------------------------------------------------------------ roof
def build_roof(M, C):
    c = C['Solar']
    z0 = ROOF_Z + 2.5
    panel_xs = []
    for gx0 in (PANELS_REAR_X0, PANELS_FRONT_X0):
        for k in range(3):
            x0 = gx0 + k * (PANEL_W + PANEL_GAP)
            x1 = x0 + PANEL_W
            panel_xs.append((x0, x1))
            box('PanelFrame', x0, x1, -PANEL_L / 2, PANEL_L / 2, z0, z0 + 1.38, M['alu'], c, bevel=0.15)
            box('PanelCells', x0 + 0.6, x1 - 0.6, -PANEL_L / 2 + 0.6, PANEL_L / 2 - 0.6, z0 + 1.38, z0 + 1.42,
                M['solar'], c)
            for xx in (x0 + 3, x1 - 4):
                for yy in (-PANEL_L / 2 + 6, PANEL_L / 2 - 8):
                    box('ZBracket', xx, xx + 1, yy, yy + 2, ROOF_Z, z0, M['alu'], c)
    # combiner box between rear group and AC
    box('Combiner', 106.5, 113, -5, 5, ROOF_Z, ROOF_Z + 4, M['white'], C['Power'], bevel=0.6)
    box('RoofGland', 8, 13, 36, 41, ROOF_Z, ROOF_Z + 2.2, M['white'], C['Power'], bevel=0.5)

    ac = C['Roof']
    ax = AC_X
    box('ACCurb', ax - 14.5, ax + 14.5, -14.75, 14.75, ROOF_Z, ROOF_Z + 1, M['black'], ac, bevel=0.5)
    box('ChillCube', ax - 14.5, ax + 14.5, -14.75, 14.75, ROOF_Z + 1, ROOF_Z + 14.5, M['black'], ac,
        bevel=3.5, seg=6)
    for k in range(5):
        box('ACTopVent', ax - 10 + k * 4.6, ax - 8 + k * 4.6, -10, 10, ROOF_Z + 14.3, ROOF_Z + 14.8, M['rimdark'], ac, bevel=0.3)
    for k in range(6):
        box('ACGrille', ax - 12 + k * 4.4, ax - 10.2 + k * 4.4, -15.0, 15.0, ROOF_Z + 4, ROOF_Z + 10,
            M['black'], ac, bevel=0.3)
    # Starlink Mini on a flat mount beside the AC (roadside margin)
    box('StarlinkMount', ax - 6.5, ax + 6.5, 22, 33, ROOF_Z, ROOF_Z + 1.0, M['alu'], ac, bevel=0.3)
    box('StarlinkMini', ax - 5.7, ax + 5.7, 22.6, 32.4, ROOF_Z + 1.0, ROOF_Z + 2.4, M['white'], ac, bevel=0.6)
    # existing fans / skylight (under the panels; low-profile)
    for (x, y) in ((86, 20), (72, -22), (226, 0)):
        box('FanBase', x - 8, x + 8, y - 8, y + 8, ROOF_Z, ROOF_Z + 0.8, M['white'], ac, bevel=0.5)
        box('FanDome', x - 6.5, x + 6.5, y - 6.5, y + 6.5, ROOF_Z + 0.8, ROOF_Z + 2.0, M['white'], ac, bevel=1.0)
    box('Skylight', 64, 80, 26, 40, ROOF_Z, ROOF_Z + 1.6, M['glass_frost'], ac, bevel=0.8)
    return panel_xs


# ------------------------------------------------------------------ interior helpers
def cabinet(name, x0, x1, y0, y1, z0, z1, face, ndoors, rows, M, c, carcass='walnut', front='walnut',
            pull=True):
    """Carcass + door/drawer fronts with 1/8 in reveals on one face."""
    box(name, x0, x1, y0, y1, z0, z1, M[carcass], c, bevel=0.2)
    g = 0.125
    t = 0.75
    if face in ('y+', 'y-'):
        a0, a1 = x0, x1
    else:
        a0, a1 = y0, y1
    da = (a1 - a0) / ndoors
    zs = [z0]
    tot = sum(rows)
    acc = z0
    for r in rows:
        acc += (z1 - z0) * r / tot
        zs.append(acc)
    for i in range(ndoors):
        for j in range(len(rows)):
            u0, u1 = a0 + i * da + g, a0 + (i + 1) * da - g
            v0, v1 = zs[j] + g, zs[j + 1] - g
            if face == 'y+':
                box(name + 'Front', u0, u1, y1, y1 + t, v0, v1, M[front], c, bevel=0.12, seg=2)
                if pull:
                    box('Pull', (u0 + u1) / 2 - 3, (u0 + u1) / 2 + 3, y1 + t, y1 + t + 0.5, v1 - 1.6, v1 - 1.1,
                        M['brass'], c)
            elif face == 'y-':
                box(name + 'Front', u0, u1, y0 - t, y0, v0, v1, M[front], c, bevel=0.12, seg=2)
                if pull:
                    box('Pull', (u0 + u1) / 2 - 3, (u0 + u1) / 2 + 3, y0 - t - 0.5, y0 - t, v0 + 1.1, v0 + 1.6,
                        M['brass'], c)
            elif face == 'x+':
                box(name + 'Front', x1, x1 + t, u0, u1, v0, v1, M[front], c, bevel=0.12, seg=2)
                if pull:
                    box('Pull', x1 + t, x1 + t + 0.5, (u0 + u1) / 2 - 3, (u0 + u1) / 2 + 3, v1 - 1.6, v1 - 1.1,
                        M['brass'], c)


def puck(x, y, M, c):
    cyl('Puck', x, y, CEIL_Z - 0.15, 1.6, 0.3, M['led'], c, verts=24)
    cyl('PuckRing', x, y, CEIL_Z - 0.05, 2.0, 0.2, M['brass'], c, verts=24)


# ------------------------------------------------------------------ interior
def build_interior(M, C):
    c = C['Interior']
    F = FLOOR_Z
    box('Floor', 2, 232, -HALF + 2, HALF - 2, F - 1.5, F, M['floor'], c)
    # rear office: desk across the rear wall, RV5 pedestal roadside
    dz = F + 29.5
    box('DeskTop', 2, 26, -20, HALF - 2, dz - 1.25, dz, M['walnut'], c, bevel=0.2)
    box('DeskEdgeLED', 25.6, 26.0, -19, HALF - 3, dz - 1.3, dz - 1.15, M['led_soft'], c)
    cabinet('DeskPedestal', 2, 24, 25.5, HALF - 2, F, dz - 1.25, 'x+', 1, [1, 1, 1], M, c)
    box('DeskLeg', 2, 24, -20, -18.75, F, dz - 1.25, M['walnut'], c)
    box('Monitor', 7, 8, -10, 18, dz + 6, dz + 22, M['black'], c, bevel=0.3)
    box('MonitorScreen', 8.0, 8.1, -9.4, 17.4, dz + 6.6, dz + 21.4, M['screen'], c)
    box('MonitorArm', 4, 7, 3, 5, dz, dz + 12, M['black'], c)
    box('Keyboard', 14, 19, -2, 12, dz, dz + 0.6, M['black'], c, bevel=0.2)
    cyl('DeskLamp', 8, -14, dz + 8, 0.4, 16, M['brass'], c)
    cyl('DeskLampShade', 10, -14, dz + 16, 2.2, 1.4, M['brass'], c, axis='Z')
    # office chair
    cyl('ChairBase', 38, 4, F + 1, 11, 1, M['black'], c)
    cyl('ChairPost', 38, 4, F + 8, 1.2, 14, M['steel'], c)
    box('ChairSeat', 30, 47, -4.5, 12.5, F + 16, F + 19.5, M['fabric'], c, bevel=1.6, seg=4)
    box('ChairBack', 44.5, 47.5, -4, 12, F + 21, F + 40, M['fabric'], c, bevel=1.4, seg=4)
    # lift bed (raised, office mode)
    bz = 104.0
    box('BedPlatform', 2, 62, -42, 42, bz, bz + 2, M['walnut'], c, bevel=0.3)
    box('BedLED', 2.5, 61.5, -41.5, 41.5, bz - 0.25, bz, M['led_soft'], c)
    box('Mattress', 3, 61, -40, 40, bz + 2, bz + 9.5, M['fabric_light'], c, bevel=2.2, seg=4)
    box('Duvet', 3, 46, -40.5, 40.5, bz + 8, bz + 10.2, M['fabric'], c, bevel=2.5, seg=4)
    for side in (-1, 1):
        box('BedTrack', 1.5, 3, side * 43 - 0.6, side * 43 + 0.6, F, CEIL_Z, M['black'], c)
        box('BedTrack', 61, 62.5, side * 43 - 0.6, side * 43 + 0.6, F, CEIL_Z, M['black'], c)
    # bath (roadside) partition with sliding door
    box('BathWallRear', 63, 64, 7, HALF - 2, F, CEIL_Z, M['lining'], c)
    box('BathWallFront', 112, 113, 7, HALF - 2, F, CEIL_Z, M['lining'], c)
    box('BathWallAisle', 64, 76, 7, 8, F, CEIL_Z, M['lining'], c)
    box('BathWallAisle', 100, 112, 7, 8, F, CEIL_Z, M['lining'], c)
    box('BathHeader', 76, 100, 7, 8, F + 78, CEIL_Z, M['lining'], c)
    box('BathDoor', 74, 101, 5.6, 6.6, F + 1, F + 78, M['walnut'], c, bevel=0.2)
    box('BathDoorPull', 76, 77, 5.0, 5.6, F + 34, F + 46, M['brass'], c)
    # galley (curbside)
    cz = F + 35
    cabinet('Galley', 64, 140, -HALF + 2, -20.5, F + 4, cz, 'y+', 4, [1, 1, 1.4], M, c)
    box('GalleyToe', 64, 140, -HALF + 2, -21.5, F, F + 4, M['black'], c)
    box('Counter', 63, 141, -HALF + 2, -19.5, cz, cz + 1.5, M['quartz'], c, bevel=0.25)
    cyl('Sink', 122, -32, cz + 1.0, 7.5, 1.2, M['steel'], c, verts=48)
    cyl('SinkBowl', 122, -32, cz + 1.4, 6.8, 0.4, M['black'], c, verts=48)
    cyl('Faucet', 122, -40.5, cz + 7, 0.5, 12, M['black'], c)
    box('FaucetSpout', 117, 122.5, -41, -40, cz + 12.5, cz + 13.3, M['black'], c)
    box('Induction', 80, 100, -40, -24, cz + 1.5, cz + 1.75, M['blackgloss'], c, bevel=0.3)
    cabinet('GalleyUpper', 64, 140, -HALF + 2, -HALF + 15, 92, 112, 'y+', 4, [1], M, c)
    box('Microwave', 84, 104, -HALF + 2.5, -HALF + 15.4, 92.2, 103, M['blackgloss'], c, bevel=0.3)
    box('UpperLED', 64, 140, -HALF + 13, -HALF + 14, 91.5, 91.8, M['led'], c)
    cabinet('Pantry', 141, 160, -HALF + 2, -20.5, F, 112, 'y+', 1, [1, 1], M, c)
    # front curbside bench
    cabinet('Bench', 196, 230, -HALF + 2, -22, F, F + 15, 'y+', 2, [1], M, c)
    box('BenchCushion', 196, 230, -HALF + 2.5, -22.5, F + 15, F + 19, M['fabric'], c, bevel=1.8, seg=4)
    box('BenchBack', 196, 230, -HALF + 2.5, -HALF + 7, F + 19, F + 38, M['fabric'], c, bevel=1.8, seg=4)
    # fridge (roadside) - position depends on laundry option (A uses x112-136)
    box('Fridge', 137, 160, 20, HALF - 2, F, F + 64, M['blackgloss'], c, bevel=0.6)
    box('FridgeHandle', 158, 158.8, 18.8, 20, F + 30, F + 52, M['steel'], c)
    cabinet('FridgeUpper', 137, 160, 30, HALF - 2, F + 64.5, 112, 'y-', 1, [1], M, c)
    # dinette (roadside), two facing seats + table
    for x0, x1, back in ((164, 182, 164), (208, 230, 230)):
        box('DinetteBase', x0, x1, 10, HALF - 2, F, F + 14, M['walnut'], c, bevel=0.2)
        box('DinetteCushion', x0, x1, 10.5, HALF - 2.5, F + 14, F + 18.5, M['fabric'], c, bevel=2.0, seg=4)
        bx0 = back - 4 if back == 182 or back == 164 else back - 4
        if back == 164:
            box('DinetteBack', 164, 168, 10.5, HALF - 2.5, F + 18.5, F + 40, M['fabric'], c, bevel=1.8, seg=4)
        else:
            box('DinetteBack', 226, 230, 10.5, HALF - 2.5, F + 18.5, F + 40, M['fabric'], c, bevel=1.8, seg=4)
    box('Table', 183, 207, 11, HALF - 3, F + 27.5, F + 28.75, M['walnut'], c, bevel=0.4)
    cyl('TablePost', 195, 28, F + 14, 1.2, 27, M['black'], c)
    cabinet('DinetteUpper', 164, 230, HALF - 15, HALF - 2, 92, 112, 'y-', 3, [1], M, c)
    box('UpperLED', 164, 230, HALF - 14, HALF - 13, 91.5, 91.8, M['led'], c)
    # bath fixtures
    box('Shower', 64, 88, 20, HALF - 2, F, F + 6, M['white'], c, bevel=1.0)
    box('Vanity', 98, 112, 26, HALF - 2, F, F + 32, M['walnut'], c, bevel=0.2)
    cyl('Toilet', 92, 32, F + 8, 7, 16, M['white'], c, bevel=2)
    # pucks + cove
    for x in (12, 40, 76, 106, 136, 166, 196, 222):
        puck(x, 0, M, c)
    # interior area lights (warm) for interior / night shots
    for i, x in enumerate((20, 70, 125, 185, 220)):
        ld = bpy.data.lights.new('IntLight%d' % i, 'AREA')
        ld.energy = 55
        ld.color = (1.0, 0.78, 0.55)
        ld.size = 18 * IN
        lo = bpy.data.objects.new('IntLight%d' % i, ld)
        lo.location = I(x, 0, CEIL_Z - 3)
        C['Lights'].objects.link(lo)


# ------------------------------------------------------------------ laundry
def build_laundry(M, C):
    F = FLOOR_Z
    out = {}
    # Option A: bath side, between bath wall (x113) and fridge (x137)
    c = C['LaundryA']
    box('A_CabSideRear', 113, 114, 19, HALF - 2, F, F + 38, M['walnut'], c)
    box('A_CabSideFront', 135.5, 136.5, 19, HALF - 2, F, F + 38, M['walnut'], c)
    box('A_Plinth', 114, 135.5, 20, HALF - 2, F, F + 0.6, M['black'], c)
    w = box('A_Washer', 114.25, 135.25, 20.4, 43.0, F + 0.6, F + 0.6 + 33.1, M['washer'], c, bevel=0.6)
    cyl('A_Door', 124.75, 20.0, F + 15, 7.2, 0.8, M['steel'], c, axis='Y', bevel=0.3)
    cyl('A_DoorGlass', 124.75, 19.4, F + 15, 5.6, 0.4, M['glass'], c, axis='Y')
    box('A_Panel', 114.6, 134.9, 20.0, 20.5, F + 27, F + 32.5, M['blackgloss'], c)
    box('A_Counter', 112.5, 137, 18.5, HALF - 2, F + 38, F + 39.5, M['quartz'], c, bevel=0.25)
    box('A_ChargePad', 122, 128, 24, 32, F + 39.5, F + 39.7, M['black'], c, bevel=0.2)
    box('A_VentDuct', 122, 127, 43.0, HALF - 1.8, F + 22, F + 27, M['alu'], c)
    box('A_ExtVent', 120.5, 128.5, HALF - 0.2, HALF + 0.7, F + 20.5, F + 28.5, M['white'], C['LaundryA'], bevel=0.6)
    lib.curve_path('A_Hot', [(113.5, 40, F + 6), (118, 40, F + 6)], 0.3, M['brass'], c)
    lib.curve_path('A_Drain', [(118, 42, F + 2), (118, 42, F - 8), (116, 0, 24)], 0.6, M['black'], c)
    out['A'] = dict(x=124.75, y=31.7, z=F + 17)

    # Drawer stack that stays if laundry goes to the garage (Option B)
    cd = C['DrawersA']
    cabinet('DrawerStack', 113, 136.5, 19, HALF - 2, F, F + 35, 'y-', 1, [1, 1, 1, 1], M, cd)
    box('DrawerCounter', 112.5, 137, 18.5, HALF - 2, F + 35, F + 36.5, M['quartz'], cd, bevel=0.25)

    # Option B: rear garage, curbside rear corner under the lift bed
    c = C['LaundryB']
    box('B_Plinth', 3, 27, -HALF + 2.5, -20, F, F + 0.6, M['black'], c)
    box('B_Washer', 3.5, 26.1, -HALF + 2.6, -20.4, F + 0.6, F + 33.7, M['washer'], c, bevel=0.6)
    cyl('B_Door', 26.5, -31.7, F + 15, 7.2, 0.8, M['steel'], c, axis='X', bevel=0.3)
    cyl('B_DoorGlass', 27.1, -31.7, F + 15, 5.6, 0.4, M['glass'], c, axis='X')
    box('B_Panel', 26.0, 26.5, -42.5, -21, F + 27, F + 32.5, M['blackgloss'], c)
    box('B_Surround', 2.5, 27.5, -20.4, -19.5, F, F + 36, M['walnut'], c)
    box('B_VentDuct', 1.2, 3.5, -34, -29, F + 22, F + 27, M['alu'], c)
    box('B_ExtVent', -0.9, 0.0, -35.5, -27.5, F + 20.5, F + 28.5, M['white'], c, bevel=0.6)
    lib.curve_path('B_Supply', [(113, 40, F + 3), (64, 40, F + 3), (64, -10, F - 3), (20, -30, F - 3), (12, -30, F + 6)],
                   0.3, M['brass'], c)
    lib.curve_path('B_Drain', [(10, -36, F + 2), (10, -36, F - 8), (98, -10, 24)], 0.6, M['black'], c)
    out['B'] = dict(x=14.8, y=-31.7, z=F + 17)
    return out


# ------------------------------------------------------------------ power
def build_power(M, C, panel_xs):
    c = C['Power']
    cr = C['Runs']
    F = FLOOR_Z
    b = BOX
    # battery box + two packs
    box('BatteryBox', b['x0'], b['x1'], b['y0'], b['y1'], b['z0'], b['z1'], M['powder'], c, bevel=0.6)
    box('BoxStoneGuard', b['x1'], b['x1'] + 1.5, b['y0'], b['y1'], b['z0'], b['z0'] + 4, M['powder'], c, bevel=0.3)
    for y0 in (-24.5, 0.6):
        box('B4810', 22.5, 37.5, y0, y0 + 23.9, b['z0'] + 0.8, b['z0'] + 6.5, principled('BluettiGrey', (0.11, 0.115, 0.12), rough=0.4), c, bevel=0.4)
    for y in (-20, 20):
        box('BoxHanger', 24, 36, y - 1, y + 1, b['z1'], 25, M['frame'], c)
    box('Disconnect', 24, 28, 22, 25, b['z1'] - 2, b['z1'], M['amber'], c)
    # RV5 inside the desk pedestal, on the roadside wall
    box('RV5', 4.0, 21.7, HALF - 2 - 6.3, HALF - 2.05, F + 1.5, F + 1.5 + 19.7,
        principled('RV5Body', (0.13, 0.135, 0.14), rough=0.35), c, bevel=0.8)
    box('RV5Display', 6, 11, HALF - 8.4, HALF - 8.25, F + 15, F + 19, M['screen'], c)
    # Orions under the passenger seat
    for k in range(2):
        box('OrionTr', 262 + k * 6, 267.3 + k * 6, -22, -14.7, 30, 33.2, principled('VictronBlue', (0.02, 0.12, 0.35), rough=0.4), c, bevel=0.3)
    box('TransferSwitch', 198, 204, -40, -34, F + 2, F + 10, M['white'], c, bevel=0.3)
    box('MainPanel', 150, 158, -HALF + 3, -HALF + 6, F + 2, F + 14, M['white'], c, bevel=0.3)

    runs = {}
    pv = emission('RunPV', (1.0, 0.62, 0.12), 3.0)
    dc = emission('Run48V', (0.15, 0.45, 1.0), 3.0)
    alt = emission('RunAlt', (0.2, 0.85, 0.55), 3.0)
    ac = emission('RunAC', (0.62, 0.42, 1.0), 3.0)
    z = ROOF_Z + 0.8
    for i, (x0, x1) in enumerate(panel_xs):
        xm = (x0 + x1) / 2
        pts = [(xm, 30, z), (xm, 6 if xm < 110 else 3, z), (110, 0, z + 1.5)]
        nm = 'PV_panel%d' % (i + 1)
        lib.curve_path(nm, pts, 0.35, pv, cr)
        runs[nm] = lib.path_len(pts)
    trunk = [(108, 4, z + 1), (60, 38, z), (10.5, 38.5, z), (10.5, 38.5, CEIL_Z), (8, 40, F + 25), (8, 40, F + 21)]
    lib.curve_path('PV_trunk', trunk, 0.6, pv, cr)
    runs['PV trunk, combiner to RV5 (x2 runs)'] = lib.path_len(trunk)
    bat = [(12, 41, F + 3), (12, 39, F - 3), (22, 20, 26), (24, 20, b['z1'] - 1)]
    lib.curve_path('DC48', bat, 0.75, dc, cr)
    runs['48V, RV5 to batteries'] = lib.path_len(bat)
    alt12 = [(262, 21, 28), (262, 0, 30), (264, -18, 31)]
    lib.curve_path('ALT12', alt12, 0.6, alt, cr)
    runs['12V, starter battery to Orions'] = lib.path_len(alt12)
    alt48 = [(270, -18, 30), (250, -15.5, 23), (60, -15.5, 23), (40, -15.5, 21), (37, -18, b['z1'] - 2)]
    lib.curve_path('ALT48', alt48, 0.45, alt, cr)
    runs['48V, Orions to batteries'] = lib.path_len(alt48)
    gen = [(212, -30, 34), (201, -37, F + 6)]
    lib.curve_path('GEN', gen, 0.5, ac, cr)
    runs['120V, generator to transfer switch'] = lib.path_len(gen)
    acin = [(198, -37, F + 3), (198, -38, F - 4), (60, -38, F - 4), (30, -10, F - 4), (16, 36, F - 4), (16, 38, F + 4)]
    lib.curve_path('ACIN', acin, 0.5, ac, cr)
    runs['120V, transfer switch to RV5 AC in'] = lib.path_len(acin)
    shore = [(16, HALF - 1, 32), (20, 30, F - 5), (60, 30, F - 5), (180, -30, F - 5), (198, -36, F - 3), (198, -37, F + 3)]
    lib.curve_path('SHORE', shore, 0.45, ac, cr)
    runs['120V, shore inlet to transfer switch'] = lib.path_len(shore)
    acout = [(14, 37, F + 4), (14, 34, F - 3), (60, 34, F - 3), (150, -36, F - 3), (154, -38, F + 6)]
    lib.curve_path('ACOUT', acout, 0.45, ac, cr)
    runs['120V, RV5 AC out to main panel'] = lib.path_len(acout)
    return runs


# ------------------------------------------------------------------ tow car
def build_car(M, C):
    c = C['Tow']
    L, W = 144.4, 64.1
    front_x = -56.0
    X0 = front_x - L
    pts = [(0, 16), (0, 34), (2, 42), (6, 49), (14, 55), (26, 58.2), (42, 58.7), (58, 58.2), (72, 56.5),
           (86, 52.5), (104, 44), (118, 38.5), (130, 36), (139, 33), (143.5, 28), (144.4, 22), (143, 15),
           (137, 10), (8, 10), (2, 12)]
    pts = [(X0 + x, z) for x, z in pts]
    body = profile_extrude('Car', pts, -W / 2, W / 2, M['car'], c, bevel=8.0, seg=8)
    lib.apply_mods(body)
    wx = (X0 + 24.0, X0 + 24.0 + 90.6)
    cut = [cyl('cut', x, 0, 11.4, 13.0, 80, None, c, axis='Y', verts=48) for x in wx]
    lib.boolean_diff(body, cut)
    body.data.set_sharp_from_angle(angle=math.radians(40))
    for side in (-1, 1):
        y = side * (W / 2 + 0.05)
        box('CarGlass', X0 + 14, X0 + 52, y - 0.35, y + 0.35, 38, 53.5, M['glass'], c, bevel=3.5)
        box('CarGlass', X0 + 55, X0 + 90, y - 0.35, y + 0.35, 38, 52.5, M['glass'], c, bevel=3.5)
        box('CarRocker', X0 + 30, X0 + 104, y - 0.4 if side > 0 else y - 0.4, y + 0.4, 10, 14, M['black'], c, bevel=1)
        box('CarBelt', X0 + 10, X0 + 96, y - 0.3, y + 0.3, 36.6, 37.4, M['rimdark'], c)
        for x in wx:
            wheel('CarW', x, side * 26.5, 11.4, 11.4, 7.7, M, c, outward=side, dark=True, rim_ratio=0.72)
    # windshield and hatch glass as slabs
    for (xa, za, xb, zb) in ((X0 + 74, 56.3, X0 + 112, 40.5), (X0 + 3, 44, X0 + 16, 55.5)):
        ang = math.atan2(zb - za, xb - xa)
        Lg = math.hypot(xb - xa, zb - za) - 5
        g = box('CarScreen', -Lg / 2, Lg / 2, -26, 26, -0.3, 0.3, M['glass'], c, bevel=3)
        g.location = (((xa + xb) / 2) * IN, 0, ((za + zb) / 2 + 1.2) * IN)
        g.rotation_euler = (0, -ang, 0)
    for side in (-1, 1):
        cyl('CarLamp', X0 + 141.5, side * 21, 30, 3.2, 3, M['headlight'], c, axis='X', bevel=0.8)
        box('CarTail', X0 - 0.4, X0 + 2, side * 24 - 4, side * 24 + 4, 34, 40, M['smoked'], c, bevel=1.0)
    # tow bar, baseplate and safety cables
    hx, hz = -6.0, 17.2
    for side in (-1, 1):
        lib.curve_path('TowArm', [(hx, side * 1.0, hz), (front_x + 2, side * 15, 16.5)], 0.75, M['powder'], c)
    lib.curve_path('SafetyCable', [(hx + 2, 6, 15.5), (-30, 10, 10), (front_x + 2, 18, 14)], 0.2, M['steel'], c)
    lib.curve_path('SafetyCable', [(hx + 2, -6, 15.5), (-30, -10, 10), (front_x + 2, -18, 14)], 0.2, M['steel'], c)
    lib.curve_path('TowCord', [(hx + 1, 3, 18.5), (-30, 2, 13), (front_x + 2, 4, 19)], 0.25, M['black'], c)
    box('CarGrille', X0 + 141, X0 + 145.2, -12, 12, 17, 22, M['black'], c, bevel=1.5)
    box('CarMirror', X0 + 86, X0 + 90, -W / 2 - 3, W / 2 + 3, 43, 47, M['car'], c, bevel=1.2)
    box('Baseplate', front_x - 1, front_x + 1.5, -22, 22, 14, 19, M['powder'], c, bevel=0.3)
    return X0


# ------------------------------------------------------------------ environment
def build_env(C):
    sc = bpy.context.scene
    g = box('Ground', -6000, 6000, -6000, 6000, -2, 0, lib.ground_material(), C['Env'])
    world = bpy.data.worlds.new('Sky')
    sc.world = world
    world.use_nodes = True
    nt = world.node_tree
    bg = nt.nodes['Background']
    sky = nt.nodes.new('ShaderNodeTexSky')
    sky.sky_type = 'MULTIPLE_SCATTERING'
    sky.sun_elevation = math.radians(22)
    sky.sun_rotation = math.radians(215)
    sky.altitude = 1200
    sky.sun_size = math.radians(1.2)
    sky.sun_disc = True
    nt.links.new(sky.outputs['Color'], bg.inputs['Color'])
    bg.inputs['Strength'].default_value = 0.08
    return sky


def build(laundry='A'):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    lib._mats.clear()
    names = ['Shell', 'Cab', 'Chassis', 'Roof', 'Solar', 'Power', 'Interior', 'LaundryA', 'LaundryB',
             'DrawersA', 'Tow', 'Env', 'Lights', 'Cams', 'Runs']
    C = {n: coll(n) for n in names}
    M = mats()
    build_shell(M, C)
    build_cab(M, C)
    build_running_gear(M, C)
    panel_xs = build_roof(M, C)
    build_interior(M, C)
    pos = build_laundry(M, C)
    runs = build_power(M, C, panel_xs)
    car_x0 = build_car(M, C)
    sky = build_env(C)
    meta = dict(runs_in=runs, panel_xs=panel_xs, laundry_pos=pos, car_x0=car_x0)
    return C, M, sky, meta
