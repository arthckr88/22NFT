"""Shared helpers for the Alita 22NFT model.

Units: authored in inches (IN converts to Blender metres).
Axes: +X forward (rear wall at x=0, front bumper at x=312),
      +Y roadside / driver side, -Y curbside / door side, +Z up, ground z=0.
"""
import math
import bpy
import bmesh
from mathutils import Vector, Matrix

IN = 0.0254


def I(*v):
    return tuple(a * IN for a in v)


# ---------------------------------------------------------------- collections
def coll(name, parent=None):
    c = bpy.data.collections.get(name)
    if c is None:
        c = bpy.data.collections.new(name)
        (parent or bpy.context.scene.collection).children.link(c)
    return c


def link(obj, c):
    for uc in list(obj.users_collection):
        uc.objects.unlink(obj)
    c.objects.link(obj)
    return obj


# ---------------------------------------------------------------- materials
_mats = {}


def principled(name, color=(0.8, 0.8, 0.8), rough=0.5, metal=0.0, coat=0.0,
               emit=None, emit_strength=0.0, transmission=0.0, alpha=1.0, ior=1.45):
    if name in _mats:
        return _mats[name]
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    b = m.node_tree.nodes['Principled BSDF']
    b.inputs['Base Color'].default_value = (*color, 1)
    b.inputs['Roughness'].default_value = rough
    b.inputs['Metallic'].default_value = metal
    b.inputs['Coat Weight'].default_value = coat
    b.inputs['Coat Roughness'].default_value = 0.05
    b.inputs['Transmission Weight'].default_value = transmission
    b.inputs['IOR'].default_value = ior
    b.inputs['Alpha'].default_value = alpha
    if emit is not None:
        b.inputs['Emission Color'].default_value = (*emit, 1)
        b.inputs['Emission Strength'].default_value = emit_strength
    m.diffuse_color = (*color, alpha)
    _mats[name] = m
    return m


def emission(name, color, strength):
    if name in _mats:
        return _mats[name]
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    for n in list(nt.nodes):
        nt.nodes.remove(n)
    out = nt.nodes.new('ShaderNodeOutputMaterial')
    em = nt.nodes.new('ShaderNodeEmission')
    em.inputs['Color'].default_value = (*color, 1)
    em.inputs['Strength'].default_value = strength
    nt.links.new(em.outputs[0], out.inputs[0])
    m.diffuse_color = (*color, 1)
    _mats[name] = m
    return m


def solar_material():
    """Dark cells on a white backsheet grid (half-cut mono look)."""
    if 'Solar' in _mats:
        return _mats['Solar']
    m = bpy.data.materials.new('Solar')
    m.use_nodes = True
    nt = m.node_tree
    b = nt.nodes['Principled BSDF']
    tc = nt.nodes.new('ShaderNodeTexCoord')
    mp = nt.nodes.new('ShaderNodeMapping')
    br = nt.nodes.new('ShaderNodeTexBrick')
    br.offset = 0.0
    br.squash = 1.0
    br.inputs['Color1'].default_value = (0.012, 0.016, 0.03, 1)
    br.inputs['Color2'].default_value = (0.016, 0.022, 0.04, 1)
    br.inputs['Mortar'].default_value = (0.3, 0.31, 0.33, 1)
    br.inputs['Scale'].default_value = 1.0
    br.inputs['Mortar Size'].default_value = 0.0018
    br.inputs['Brick Width'].default_value = 0.083   # ~3.3 in half-cut cells
    br.inputs['Row Height'].default_value = 0.083
    nt.links.new(tc.outputs['Object'], mp.inputs['Vector'])
    nt.links.new(mp.outputs['Vector'], br.inputs['Vector'])
    nt.links.new(br.outputs['Color'], b.inputs['Base Color'])
    b.inputs['Roughness'].default_value = 0.12
    b.inputs['Coat Weight'].default_value = 1.0
    b.inputs['Coat Roughness'].default_value = 0.02
    m.diffuse_color = (0.02, 0.03, 0.05, 1)
    _mats['Solar'] = m
    return m


def wood_material(name='Walnut', base=(0.16, 0.085, 0.045), dark=(0.07, 0.035, 0.018), axis='X'):
    """Grain runs along the given axis; box() picks the axis from the part's longest side."""
    key = name if axis == 'X' else name + '_' + axis
    if key in _mats:
        return _mats[key]
    m = bpy.data.materials.new(key)
    m['wood'] = [name, list(base), list(dark)]
    m.use_nodes = True
    nt = m.node_tree
    b = nt.nodes['Principled BSDF']
    tc = nt.nodes.new('ShaderNodeTexCoord')
    mp = nt.nodes.new('ShaderNodeMapping')
    mp.inputs['Scale'].default_value = {'X': (1.2, 40.0, 40.0), 'Y': (40.0, 1.2, 40.0), 'Z': (40.0, 40.0, 1.2)}[axis]
    nz = nt.nodes.new('ShaderNodeTexNoise')
    nz.inputs['Scale'].default_value = 2.5
    nz.inputs['Detail'].default_value = 10.0
    nz.inputs['Roughness'].default_value = 0.62
    nz.inputs['Distortion'].default_value = 0.6
    ramp = nt.nodes.new('ShaderNodeValToRGB')
    ramp.color_ramp.elements[0].position = 0.35
    ramp.color_ramp.elements[1].position = 0.7
    ramp.color_ramp.elements[0].color = (*dark, 1)
    ramp.color_ramp.elements[1].color = (*base, 1)
    nt.links.new(tc.outputs['Object'], mp.inputs['Vector'])
    nt.links.new(mp.outputs['Vector'], nz.inputs['Vector'])
    nt.links.new(nz.outputs['Fac'], ramp.inputs['Fac'])
    nt.links.new(ramp.outputs['Color'], b.inputs['Base Color'])
    b.inputs['Roughness'].default_value = 0.42
    b.inputs['Coat Weight'].default_value = 0.2
    m.diffuse_color = (*base, 1)
    _mats[key] = m
    return m


def ground_material():
    if 'Ground' in _mats:
        return _mats['Ground']
    m = bpy.data.materials.new('Ground')
    m.use_nodes = True
    nt = m.node_tree
    b = nt.nodes['Principled BSDF']
    nz = nt.nodes.new('ShaderNodeTexNoise')
    nz.inputs['Scale'].default_value = 60.0
    nz.inputs['Detail'].default_value = 8.0
    ramp = nt.nodes.new('ShaderNodeValToRGB')
    ramp.color_ramp.elements[0].color = (0.11, 0.105, 0.1, 1)
    ramp.color_ramp.elements[1].color = (0.24, 0.225, 0.21, 1)
    nt.links.new(nz.outputs['Fac'], ramp.inputs['Fac'])
    nt.links.new(ramp.outputs['Color'], b.inputs['Base Color'])
    b.inputs['Roughness'].default_value = 0.85
    m.diffuse_color = (0.18, 0.17, 0.16, 1)
    _mats['Ground'] = m
    return m


# ---------------------------------------------------------------- geometry
def _new_obj(name, mesh, c):
    o = bpy.data.objects.new(name, mesh)
    c.objects.link(o)
    return o


def box(name, x0, x1, y0, y1, z0, z1, mat, c, bevel=0.0, seg=3):
    """Axis-aligned box from inch bounds. bevel in inches."""
    me = bpy.data.meshes.new(name)
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    bm.to_mesh(me)
    bm.free()
    o = _new_obj(name, me, c)
    o.scale = ((x1 - x0) * IN, (y1 - y0) * IN, (z1 - z0) * IN)
    o.location = ((x0 + x1) / 2 * IN, (y0 + y1) / 2 * IN, (z0 + z1) / 2 * IN)
    if mat is not None and 'wood' in mat.keys():
        dims = [x1 - x0, y1 - y0, z1 - z0]
        ax = 'XYZ'[dims.index(max(dims))]
        nm, b_, d_ = mat['wood']
        mat = wood_material(nm, tuple(b_), tuple(d_), ax)
    if mat:
        me.materials.append(mat)
    apply_scale(o)
    if bevel > 0:
        m = o.modifiers.new('bevel', 'BEVEL')
        m.width = bevel * IN
        m.segments = seg
        m.limit_method = 'ANGLE'
        m.harden_normals = False
    shade_smooth(o, 35)
    return o


def cyl(name, x, y, z, r, depth, mat, c, axis='Z', verts=48, bevel=0.0, seg=3):
    me = bpy.data.meshes.new(name)
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=False, segments=verts,
                          radius1=r * IN, radius2=r * IN, depth=depth * IN)
    bm.to_mesh(me)
    bm.free()
    o = _new_obj(name, me, c)
    if axis == 'X':
        o.rotation_euler = (0, math.radians(90), 0)
    elif axis == 'Y':
        o.rotation_euler = (math.radians(90), 0, 0)
    o.location = (x * IN, y * IN, z * IN)
    if mat:
        me.materials.append(mat)
    if bevel > 0:
        m = o.modifiers.new('bevel', 'BEVEL')
        m.width = bevel * IN
        m.segments = seg
        m.limit_method = 'ANGLE'
    shade_smooth(o, 40)
    return o


def profile_extrude(name, pts_xz, y0, y1, mat, c, bevel=0.0, seg=6):
    """Polygon in the XZ plane (inches), extruded from y0 to y1."""
    me = bpy.data.meshes.new(name)
    bm = bmesh.new()
    vs = [bm.verts.new((x * IN, y0 * IN, z * IN)) for x, z in pts_xz]
    f = bm.faces.new(vs)
    res = bmesh.ops.extrude_face_region(bm, geom=[f])
    nv = [e for e in res['geom'] if isinstance(e, bmesh.types.BMVert)]
    bmesh.ops.translate(bm, vec=Vector((0, (y1 - y0) * IN, 0)), verts=nv)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.to_mesh(me)
    bm.free()
    o = _new_obj(name, me, c)
    if mat:
        me.materials.append(mat)
    if bevel > 0:
        m = o.modifiers.new('bevel', 'BEVEL')
        m.width = bevel * IN
        m.segments = seg
        m.limit_method = 'ANGLE'
        m.angle_limit = math.radians(25)
    shade_smooth(o, 32)
    return o


def arc(cx, cz, r, a0, a1, n=10):
    """Points (x,z) on a circle, degrees, inclusive."""
    out = []
    for i in range(n + 1):
        a = math.radians(a0 + (a1 - a0) * i / n)
        out.append((cx + r * math.cos(a), cz + r * math.sin(a)))
    return out


def shade_smooth(o, angle_deg=35):
    me = o.data
    for p in me.polygons:
        p.use_smooth = True
    try:
        o.modifiers.new('autosmooth', 'SMOOTH_BY_ANGLE')
        o.modifiers['autosmooth']['Input_1'] = math.radians(angle_deg)
    except Exception:
        pass


def apply_scale(o):
    me = o.data
    me.transform(Matrix.Diagonal((*o.scale, 1.0)))
    o.scale = (1, 1, 1)


def apply_mods(o):
    dg = bpy.context.evaluated_depsgraph_get()
    ev = o.evaluated_get(dg)
    me = bpy.data.meshes.new_from_object(ev)
    old = o.data
    o.modifiers.clear()
    o.data = me
    if old.users == 0:
        bpy.data.meshes.remove(old)


def join(objs, name):
    ctx = bpy.context
    for ob in ctx.view_layer.objects:
        ob.select_set(False)
    for ob in objs:
        ob.select_set(True)
    ctx.view_layer.objects.active = objs[0]
    bpy.ops.object.join()
    objs[0].name = name
    return objs[0]


def boolean_diff(target, cutters, solver='EXACT'):
    cut = join(cutters, target.name + '_cutters') if len(cutters) > 1 else cutters[0]
    m = target.modifiers.new('cut', 'BOOLEAN')
    m.operation = 'DIFFERENCE'
    m.object = cut
    m.solver = solver
    apply_mods(target)
    bpy.data.objects.remove(cut, do_unlink=True)
    # boolean leaves an empty material slot for the cut faces: give them a real material
    me = target.data
    empty = [i for i, mm in enumerate(me.materials) if mm is None]
    if empty:
        fill = 1 if len(me.materials) > 2 else 0
        for p in me.polygons:
            if p.material_index in empty:
                p.material_index = fill
        for i in reversed(empty):
            me.materials.pop(index=i)


def curve_path(name, pts_in, radius, mat, c):
    """Tube through points (inches)."""
    cu = bpy.data.curves.new(name, 'CURVE')
    cu.dimensions = '3D'
    cu.bevel_depth = radius * IN
    cu.bevel_resolution = 3
    sp = cu.splines.new('POLY')
    sp.points.add(len(pts_in) - 1)
    for p, (x, y, z) in zip(sp.points, pts_in):
        p.co = (x * IN, y * IN, z * IN, 1)
    o = bpy.data.objects.new(name, cu)
    c.objects.link(o)
    if mat:
        cu.materials.append(mat)
    return o


def path_len(pts):
    return sum((Vector(a) - Vector(b)).length for a, b in zip(pts, pts[1:]))
