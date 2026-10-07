"""Render one or more shots.

usage: python3 render.py SHOT [SHOT ...] [--preview] [--samples N]
Writes renders/<SHOT>.png and renders/<SHOT>.json (2D anchor positions for annotation).
"""
import sys
import os
import json
import math
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import bpy
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view

import lib
from lib import IN, I
import build
from specs import *

ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, 'renders')
os.makedirs(OUT, exist_ok=True)

ALL = ['Shell', 'Cab', 'Chassis', 'Roof', 'Solar', 'Power', 'Interior', 'LaundryA', 'LaundryB', 'DrawersA', 'Tow',
       'Env', 'Lights', 'Runs']


def emissions(day=True):
    k = {'LEDWarm': (18.0, 2.5), 'LEDSoft': (6.0, 1.0), 'MarkerAmber': (3.0, 0.8)}
    for n, (night, dayv) in k.items():
        m = bpy.data.materials.get(n)
        if m:
            m.node_tree.nodes['Emission'].inputs['Strength'].default_value = dayv if day else night


def ghost_mat():
    m = bpy.data.materials.new('Ghost')
    m.use_nodes = True
    nt = m.node_tree
    for n in list(nt.nodes):
        nt.nodes.remove(n)
    out = nt.nodes.new('ShaderNodeOutputMaterial')
    tr = nt.nodes.new('ShaderNodeBsdfTransparent')
    em = nt.nodes.new('ShaderNodeEmission')
    em.inputs['Color'].default_value = (0.85, 0.88, 0.95, 1)
    em.inputs['Strength'].default_value = 0.18
    lw = nt.nodes.new('ShaderNodeLayerWeight')
    lw.inputs['Blend'].default_value = 0.25
    mix = nt.nodes.new('ShaderNodeMixShader')
    nt.links.new(lw.outputs['Facing'], mix.inputs['Fac'])
    nt.links.new(tr.outputs[0], mix.inputs[1])
    nt.links.new(em.outputs[0], mix.inputs[2])
    nt.links.new(mix.outputs[0], out.inputs[0])
    return m


def set_visible(C, names):
    for n, c in C.items():
        if n == 'Cams':
            continue
        c.hide_render = n not in names
        c.hide_viewport = n not in names


def camera(name, loc, target, lens=35, ortho=None, clip_start=0.05, shift=(0, 0)):
    cd = bpy.data.cameras.new(name)
    cd.lens = lens
    cd.clip_start = clip_start
    cd.clip_end = 2000
    cd.shift_x, cd.shift_y = shift
    if ortho:
        cd.type = 'ORTHO'
        cd.ortho_scale = ortho
    o = bpy.data.objects.new(name, cd)
    bpy.context.scene.collection.objects.link(o)
    o.location = Vector(I(*loc))
    d = Vector(I(*target)) - o.location
    o.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
    bpy.context.scene.camera = o
    return o


def setup_render(samples, preview, res=(1920, 1080)):
    sc = bpy.context.scene
    sc.render.engine = 'CYCLES'
    cy = sc.cycles
    cy.device = 'CPU'
    cy.samples = samples
    cy.use_adaptive_sampling = True
    cy.adaptive_threshold = 0.02
    cy.use_denoising = True
    try:
        cy.denoiser = 'OPENIMAGEDENOISE'
    except Exception:
        pass
    cy.max_bounces = 8
    cy.diffuse_bounces = 3
    cy.glossy_bounces = 3
    cy.transmission_bounces = 6
    cy.transparent_max_bounces = 24
    cy.caustics_reflective = False
    cy.caustics_refractive = False
    cy.sample_clamp_indirect = 8.0
    sc.render.resolution_x, sc.render.resolution_y = res
    sc.render.resolution_percentage = 30 if preview else 100
    sc.render.image_settings.file_format = 'PNG'
    sc.render.threads_mode = 'AUTO'
    try:
        sc.view_settings.view_transform = 'AgX'
        sc.view_settings.look = 'AgX - Medium High Contrast'
    except Exception:
        pass
    sc.render.film_transparent = False


def project(cam, pts_in):
    sc = bpy.context.scene
    bpy.context.view_layer.update()
    W = sc.render.resolution_x
    H = sc.render.resolution_y
    out = {}
    for k, p in pts_in.items():
        v = world_to_camera_view(sc, cam, Vector(I(*p)))
        out[k] = [round(v.x * W, 1), round((1 - v.y) * H, 1), round(v.z, 3)]
    return out


def lights_on(C, on=True, strength=1.0):
    for o in C['Lights'].objects:
        o.hide_render = not on
        if on:
            o.data.energy = 55 * strength


# ------------------------------------------------------------------ shots
def shot(name, C, sky, meta):
    sc = bpy.context.scene
    vis = [v for v in ALL if v not in ('LaundryB', 'Runs')]
    emissions(day=True)
    anchors = {}
    samples = 64
    world_strength = 0.08
    lights_on(C, False)
    if name == '01_exterior':
        cam = camera('cam', (400, -400, 64), (110, 0, 58), lens=30)
        sky.sun_elevation = math.radians(24)
        sky.sun_rotation = math.radians(150)
        anchors = {'coach': (156, 0, 80)}
    elif name == '02_elevation':
        set_visible(C, vis)
        cam = camera('cam', (56, 900, 70), (56, 0, 70), ortho=560 * IN)
        sky.sun_elevation = math.radians(40)
        sky.sun_rotation = math.radians(95)
        anchors = dict(front=(316, HALF, 20), rear=(0, HALF, 20), top=(130, HALF, ROOF_Z + 14.5),
                       ground=(130, HALF, 0), fa=(X_FRONT_AXLE, HALF, 0), ra=(X_REAR_AXLE, HALF, 0),
                       roof=(130, HALF, ROOF_Z), floor=(160, HALF, FLOOR_Z), carfront=(-56, HALF, 20),
                       carrear=(meta['car_x0'], HALF, 20), box=(30, HALF, BOX['z0']))
        samples = 48
    elif name == '03_roof':
        cam = camera('cam', (152, 0, 800), (152, 0, 0), ortho=350 * IN)
        cam.rotation_euler = (0, 0, math.radians(-90))
        cam.rotation_euler = (0, 0, 0)
        nt = sc.world.node_tree
        bgn = nt.nodes['Background']
        for l in list(bgn.inputs['Color'].links):
            nt.links.remove(l)
        bgn.inputs['Color'].default_value = (0.82, 0.82, 0.83, 1)
        bgn.inputs['Strength'].default_value = 0.9
        world_strength = None
        sl = bpy.data.lights.new('plansun', 'SUN')
        sl.energy = 2.2
        sl.angle = math.radians(6)
        so = bpy.data.objects.new('plansun', sl)
        so.rotation_euler = (math.radians(35), math.radians(-20), math.radians(30))
        sc.collection.objects.link(so)
        vis = [v for v in vis if v not in ('Tow',)] + ['Runs']
        samples = 48
        px = meta['panel_xs']
        anchors = dict(ac=(AC_X, 0, ROOF_Z + 14), starlink=(AC_X, 27.5, ROOF_Z + 2), comb=(110, 0, ROOF_Z + 4),
                       rear=(0, 0, ROOF_Z), front=(303, 0, ROOF_Z), cabseam=(246, 0, ROOF_Z),
                       g1a=(px[0][0], -PANEL_L / 2, ROOF_Z + 4), g1b=(px[2][1], -PANEL_L / 2, ROOF_Z + 4),
                       g2a=(px[3][0], -PANEL_L / 2, ROOF_Z + 4), g2b=(px[5][1], -PANEL_L / 2, ROOF_Z + 4),
                       pl=(px[1][0], -PANEL_L / 2, ROOF_Z + 4), pr=(px[1][0], PANEL_L / 2, ROOF_Z + 4),
                       ey1=(px[1][0], HALF, ROOF_Z), ey0=(px[1][0], -HALF, ROOF_Z),
                       fan1=(86, 20, ROOF_Z + 2), fan2=(72, -22, ROOF_Z + 2), fan3=(226, 0, ROOF_Z + 2),
                       sky=(72, 33, ROOF_Z + 2), gland=(10.5, 38.5, ROOF_Z + 2))
    elif name == '04_underbelly':
        cam = camera('cam', (30, -118, 7), (38, 0, 17), lens=26)
        sky.sun_elevation = math.radians(30)
        sky.sun_rotation = math.radians(150)
        vis = [v for v in vis if v not in ('Tow',)]
        world_strength = 0.35
        for i, (x, y) in enumerate(((30, -40), (60, 30), (0, 0))):
            fl = bpy.data.lights.new('under%d' % i, 'AREA')
            fl.energy = 30
            fl.size = 40 * IN
            fo = bpy.data.objects.new('under%d' % i, fl)
            fo.location = I(x - 30, y - 30, 2)
            fo.rotation_euler = (math.radians(180 - 30), 0, math.radians(-40))
            sc.collection.objects.link(fo)
        anchors = dict(box=(30, -26, 15.5), spare=(SPARE_X, -13, 17), hitch=(-6, 0, 17), axle=(X_REAR_AXLE, -30, 14),
                       exhaust=(68, -44, 15), boxbot=(21, -26, BOX['z0']), groundbox=(21, -26, 0))
    elif name == '04b_tail_section':
        vis = [v for v in vis if v not in ('Tow',)]
        cam = camera('cam', (42, 900, 28), (42, 0, 28), ortho=160 * IN)
        sky.sun_elevation = math.radians(40)
        sky.sun_rotation = math.radians(95)
        samples = 40
        anchors = dict(tire=(X_REAR_AXLE, HALF, 0), boxrear=(BOX['x0'], HALF, BOX['z0']), boxfront=(BOX['x1'], HALF, BOX['z0']),
                       boxground=(BOX['x0'], HALF, 0), hitch=(-6, HALF, 16), tail=(0, HALF, 24), axle=(X_REAR_AXLE, HALF, 13.76),
                       spare=(SPARE_X, HALF, 17), floor=(40, HALF, FLOOR_Z), frame=(40, HALF, 19))
    elif name == '05_xray':
        cam = camera('cam', (300, -250, 230), (138, 0, 60), lens=28)
        gm = ghost_mat()
        for cname in ('Shell', 'Cab', 'Interior', 'Roof', 'Tow', 'LaundryA', 'DrawersA', 'Solar'):
            for o in C[cname].objects:
                if o.type in ('MESH', 'CURVE'):
                    if cname == 'Solar' and 'Cells' in o.name:
                        continue
                    o.data.materials.clear()
                    o.data.materials.append(gm)
        for o in C['Chassis'].objects:
            if o.type == 'MESH' and not o.name.startswith(('Generator', 'StarterBattery', 'Spare', 'FrameRail')):
                o.data.materials.clear()
                o.data.materials.append(gm)
        vis = [v for v in vis if v not in ('Tow', 'Env', 'LaundryA', 'DrawersA', 'Interior')] + ['Runs']
        for o in C['Runs'].objects:
            o.data.bevel_depth *= 2.4
            o.data.materials[0].node_tree.nodes['Emission'].inputs['Strength'].default_value = 4
        cols = {'B4810': (0.15, 0.45, 1.0), 'BatteryBox': (0.15, 0.45, 1.0), 'RV5': (0.15, 0.45, 1.0),
                'OrionTr': (0.2, 0.85, 0.55), 'TransferSwitch': (0.62, 0.42, 1.0), 'MainPanel': (0.62, 0.42, 1.0),
                'Combiner': (1.0, 0.62, 0.12), 'Generator': (0.62, 0.42, 1.0)}
        for o in list(C['Power'].objects) + list(C['Chassis'].objects):
            for k, col in cols.items():
                if o.type == 'MESH' and o.name.startswith(k):
                    o.data.materials.clear()
                    o.data.materials.append(lib.emission('X_' + k, col, 1.6))
        world_strength = 0.0
        sc.world.node_tree.nodes['Background'].inputs['Color'].default_value = (0.004, 0.004, 0.005, 1)
        try:
            sc.world.node_tree.links.remove(sc.world.node_tree.nodes['Background'].inputs['Color'].links[0])
        except Exception:
            pass
        sc.world.node_tree.nodes['Background'].inputs['Strength'].default_value = 1.0
        ld = bpy.data.lights.new('key', 'SUN')
        ld.energy = 2.0
        lo = bpy.data.objects.new('key', ld)
        lo.rotation_euler = (math.radians(40), 0, math.radians(30))
        sc.collection.objects.link(lo)
        samples = 64
        anchors = dict(panels=(198, 0, ROOF_Z + 4), comb=(110, 0, ROOF_Z + 4), trunk=(10.5, 38.5, 90),
                       rv5=(13, 40, FLOOR_Z + 12), batt=(30, 0, 16), orion=(267, -18, 32), starter=(263, 21, 28),
                       gen=(213, -30, 30), ts=(201, -37, FLOOR_Z + 6), alt48=(150, -15.5, 23), acin=(120, -39, FLOOR_Z + 3),
                       shore=(16, HALF, 36), panel=(154, -14, FLOOR_Z + 8))
        set_visible(C, vis)
        return cam, anchors, samples, None
    elif name in ('06_interior', '07_desk', '08_laundry_A', '09_laundry_B'):
        vis = [v for v in ALL if v not in ('Tow', 'Runs')]
        emissions(day=False)
        if name == '09_laundry_B':
            vis = [v for v in vis if v not in ('LaundryA',)]
        else:
            vis = [v for v in vis if v not in ('LaundryB', 'DrawersA')]
        lights_on(C, True, 1.0)
        sky.sun_elevation = math.radians(28)
        sky.sun_rotation = math.radians(120)
        world_strength = 0.3
        samples = 96
        if name == '06_interior':
            cam = camera('cam', (226, -6, 84), (20, 4, 64), lens=16)
        elif name == '07_desk':
            cam = camera('cam', (52, -14, 84), (6, 10, 66), lens=22)
        elif name == '08_laundry_A':
            cam = camera('cam', (152, -12, 76), (122, 34, 52), lens=18)
            anchors = dict(washer=(124.75, 20, FLOOR_Z + 18), counter=(124, 30, FLOOR_Z + 39.5),
                           vent=(124.5, HALF - 2, FLOOR_Z + 36), bath=(113, 12, FLOOR_Z + 30),
                           fridge=(148, 20, FLOOR_Z + 40), dinette=(175, 20, FLOOR_Z + 25))
        else:
            cam = camera('cam', (62, -6, 74), (12, -32, 50), lens=18)
            anchors = dict(washer=(26.5, -31.7, FLOOR_Z + 18), bed=(30, -30, 104), bedlow=(30, -30, FLOOR_Z + 38),
                           vent=(0, -31, FLOOR_Z + 24.5), desk=(14, 0, FLOOR_Z + 29.5), rv5=(13, 40, FLOOR_Z + 12),
                           hatch=(47, -HALF, 50), bl1=(2.5, -42, FLOOR_Z + 38), bl2=(40, -42, FLOOR_Z + 38),
                           bl3=(40, -10, FLOOR_Z + 38), bl4=(2.5, -10, FLOOR_Z + 38), wtop=(26, -42, FLOOR_Z + 33.7))
    elif name == '10_floorplan':
        vis = [v for v in ALL if v not in ('Tow', 'Roof', 'Solar', 'DrawersA')]
        cam = camera('cam', (150, 0, 50 + FLOOR_Z), (150, 0, 0), ortho=340 * IN, clip_start=0.02)
        cam.rotation_euler = (0, 0, 0)
        lights_on(C, True, 0.35)
        emissions(day=True)
        for o in C['Cab'].objects:
            if o.name.startswith(('Cab', 'Windshield')) and not o.name.startswith('CabDoor'):
                o.hide_render = True
        for cname in ('Shell', 'Cab', 'Interior'):
            for o in C[cname].objects:
                if o.type == 'MESH' and (cname != 'Interior' or o.name.startswith(('Ceiling', 'Bed', 'Mattress', 'Duvet', 'Bunk', 'GalleyUpper', 'DinetteUpper', 'FridgeUpper', 'Microwave', 'Puck'))):
                    o.visible_shadow = False
        sky.sun_elevation = math.radians(89)
        world_strength = 0.12
        samples = 64
        F = FLOOR_Z
        anchors = dict(desk=(14, 0, F + 30), rv5=(13, 40, F + 20), bed=(32, 0, F + 30), laundryA=(124.75, 31, F + 30),
                       laundryB=(14.8, -31.7, F + 30), bath=(88, 26, F + 10), galley=(100, -32, F + 36),
                       fridge=(148, 32, F + 40), dinette=(195, 28, F + 30), door=(180, -HALF, F + 10),
                       bench=(213, -34, F + 20), pantry=(150, -34, F + 40), batt=(30, 0, F), orion=(267, -18, F),
                       gen=(213, -30, F), ts=(201, -37, F + 8), hatch=(47, -HALF, F + 10), cab=(255, 0, F),
                       rear=(0, 0, F), front=(232, 0, F))
        set_visible(C, vis)
        return cam, anchors, samples, world_strength
    elif name == '11_axles':
        vis = ['Chassis', 'Power', 'Solar', 'LaundryA', 'Env', 'Roof', 'Shell', 'Cab']
        gl = bpy.data.materials.new('GhostLight')
        gl.use_nodes = True
        nt = gl.node_tree
        for n in list(nt.nodes):
            nt.nodes.remove(n)
        o_ = nt.nodes.new('ShaderNodeOutputMaterial')
        tr = nt.nodes.new('ShaderNodeBsdfTransparent')
        df = nt.nodes.new('ShaderNodeBsdfDiffuse')
        df.inputs['Color'].default_value = (0.2, 0.2, 0.22, 1)
        lw = nt.nodes.new('ShaderNodeLayerWeight')
        lw.inputs['Blend'].default_value = 0.08
        mx = nt.nodes.new('ShaderNodeMixShader')
        nt.links.new(lw.outputs['Facing'], mx.inputs['Fac'])
        nt.links.new(tr.outputs[0], mx.inputs[1])
        nt.links.new(df.outputs[0], mx.inputs[2])
        nt.links.new(mx.outputs[0], o_.inputs[0])
        for cname in ('Shell', 'Cab'):
            for o in C[cname].objects:
                if o.type == 'MESH':
                    o.data.materials.clear()
                    o.data.materials.append(gl)
        cam = camera('cam', (130, 900, 60), (130, 0, 60), ortho=380 * IN)
        sky.sun_elevation = math.radians(40)
        sky.sun_rotation = math.radians(95)
        samples = 40
        anchors = dict(fa=(X_FRONT_AXLE, HALF, 0), ra=(X_REAR_AXLE, HALF, 0), batt=(30, HALF, 16), rv5=(13, HALF, 46),
                       pr=(58.5, HALF, ROOF_Z + 4), pf=(198.5, HALF, ROOF_Z + 4), orion=(266, HALF, 32),
                       wa=(124, HALF, 54), wb=(14, HALF, 54), sl=(130, HALF, ROOF_Z + 3), rear=(0, HALF, 0),
                       front=(312, HALF, 0))
    elif name == '12_night':
        cam = camera('cam', (110, -440, 58), (40, 0, 62), lens=22)
        sky.sun_elevation = math.radians(-6)
        sky.sun_rotation = math.radians(250)
        world_strength = 0.9
        lights_on(C, True, 1.6)
        emissions(day=False)
        tg = bpy.data.materials['TintGlass'].node_tree.nodes['Principled BSDF']
        tg.inputs['Base Color'].default_value = (0.5, 0.47, 0.42, 1)
        ld = bpy.data.lights.new('moon', 'SUN')
        ld.energy = 0.3
        ld.color = (0.6, 0.7, 1.0)
        lo = bpy.data.objects.new('moon', ld)
        lo.rotation_euler = (math.radians(55), 0, math.radians(-140))
        sc.collection.objects.link(lo)
        pl = bpy.data.lights.new('porch', 'SPOT')
        pl.energy = 220
        pl.color = (1.0, 0.75, 0.45)
        pl.spot_size = math.radians(120)
        po = bpy.data.objects.new('porch', pl)
        po.location = I(198, -HALF - 6, 110)
        po.rotation_euler = (math.radians(20), 0, 0)
        sc.collection.objects.link(po)
        al = bpy.data.lights.new('awn', 'AREA')
        al.energy = 160
        al.color = (1.0, 0.72, 0.42)
        al.shape = 'RECTANGLE'
        al.size = 180 * IN
        al.size_y = 4 * IN
        ao = bpy.data.objects.new('awn', al)
        ao.location = I(154, -HALF - 5, 106)
        sc.collection.objects.link(ao)
        samples = 96
    set_visible(C, vis)
    return cam, anchors, samples, world_strength


def run(name, preview=False, samples_override=None, project_only=False):
    t0 = time.time()
    laundry = 'B' if name == '09_laundry_B' else 'A'
    C, M, sky, meta = build.build(laundry)
    cam, anchors, samples, ws = shot(name, C, sky, meta)
    sc = bpy.context.scene
    if ws is not None and sc.world.node_tree.nodes['Background'].inputs['Color'].is_linked:
        sc.world.node_tree.nodes['Background'].inputs['Strength'].default_value = ws
    setup_render(samples_override or samples, preview)
    proj = project(cam, anchors) if anchors else {}
    path = os.path.join(OUT, name + ('_preview' if preview else '') + '.png')
    sc.render.filepath = path
    if not project_only:
        bpy.ops.render.render(write_still=True)
    info = dict(shot=name, anchors=proj, res=[sc.render.resolution_x * sc.render.resolution_percentage // 100,
                                               sc.render.resolution_y * sc.render.resolution_percentage // 100],
                ortho_scale_in=(cam.data.ortho_scale / IN if cam.data.type == 'ORTHO' else None),
                runs_in=meta['runs_in'], seconds=round(time.time() - t0))
    with open(os.path.join(OUT, name + ('_preview' if preview else '') + '.json'), 'w') as f:
        json.dump(info, f, indent=1)
    print('DONE', name, info['seconds'], 's')


if __name__ == '__main__':
    args = sys.argv[1:]
    prev = '--preview' in args
    so = None
    if '--samples' in args:
        so = int(args[args.index('--samples') + 1])
    shots = [a for a in args if not a.startswith('--') and not a.isdigit()]
    for s in shots:
        run(s, prev, so, project_only='--project-only' in args)
