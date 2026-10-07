"""Export the model to model/22nft.glb with layer prefixes for the web viewer.

Layers (node name prefix): shell__, tow__, solar__, power__, laundryA__, laundryB__, interior__
"""
import os
import sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import bpy
import build

ROOT = os.path.dirname(HERE)
LAYER = {'Shell': 'shell', 'Cab': 'shell', 'Chassis': 'shell', 'Roof': 'shell', 'Tow': 'tow', 'Solar': 'solar',
         'Power': 'power', 'Runs': 'power', 'LaundryA': 'laundryA', 'LaundryB': 'laundryB', 'DrawersA': 'laundryB',
         'Interior': 'interior'}
FLAT = {'Solar': (0.02, 0.03, 0.05), 'Walnut': (0.13, 0.07, 0.035), 'FloorOak': (0.1, 0.085, 0.07),
        'Ground': (0.2, 0.2, 0.2)}


def flatten_materials():
    for m in bpy.data.materials:
        nt = m.node_tree
        if not nt:
            continue
        b = nt.nodes.get('Principled BSDF')
        key = m.name.split('_')[0]
        if key in FLAT and b:
            for l in list(b.inputs['Base Color'].links):
                nt.links.remove(l)
            b.inputs['Base Color'].default_value = (*FLAT[key], 1)
        em = nt.nodes.get('Emission')
        if em and not b:
            col = em.inputs['Color'].default_value[:]
            for n in list(nt.nodes):
                nt.nodes.remove(n)
            out = nt.nodes.new('ShaderNodeOutputMaterial')
            p = nt.nodes.new('ShaderNodeBsdfPrincipled')
            p.inputs['Base Color'].default_value = (0, 0, 0, 1)
            p.inputs['Emission Color'].default_value = col
            p.inputs['Emission Strength'].default_value = 1.0
            nt.links.new(p.outputs[0], out.inputs[0])
        if b and b.inputs['Transmission Weight'].default_value > 0.5:
            # glass reads better in the viewer as dark, semi-opaque
            b.inputs['Transmission Weight'].default_value = 0.0
            b.inputs['Alpha'].default_value = 0.55
            try:
                m.surface_render_method = 'BLENDED'
            except Exception:
                pass


def main():
    C, M, sky, meta = build.build('A')
    os.makedirs(os.path.join(ROOT, 'model'), exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(ROOT, 'model', '22nft.blend'))
    for n in ('Env', 'Lights', 'Cams'):
        for o in list(C[n].objects):
            bpy.data.objects.remove(o, do_unlink=True)
    flatten_materials()
    dg = bpy.context.evaluated_depsgraph_get()
    for cname, layer in LAYER.items():
        for o in list(C[cname].objects):
            if o.type == 'CURVE':
                me = bpy.data.meshes.new_from_object(o.evaluated_get(dg))
                no = bpy.data.objects.new(o.name, me)
                C[cname].objects.link(no)
                bpy.data.objects.remove(o, do_unlink=True)
                o = no
            lay = 'shell' if o.name.startswith(('Ceiling', 'CoveLED')) else layer
            o.name = '%s__%s' % (lay, o.name)
    # merge many small objects per layer+material to keep the file light
    os.makedirs(os.path.join(ROOT, 'model'), exist_ok=True)
    path = os.path.join(ROOT, 'model', '22nft.glb')
    bpy.ops.export_scene.gltf(filepath=path, export_format='GLB', export_apply=True, export_yup=True,
                              export_lights=False, export_cameras=False)
    print('GLB', os.path.getsize(path) // 1024, 'KB')


if __name__ == '__main__':
    main()
