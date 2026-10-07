"""Render one numbered view, preserving the source blend and exporting annotation anchors."""
import bpy,sys,pathlib,json,math
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view
R=pathlib.Path(__file__).resolve().parents[1]
args=sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else ['01']
v=args[0].zfill(2);preview='preview' in args
bpy.ops.wm.open_mainfile(filepath=str(R/'model/Alita-22NFT.blend'))
s=bpy.context.scene
for c in bpy.data.collections:c.hide_viewport=False;c.hide_render=False
for o in bpy.data.objects:o.hide_render=False
for name in ['laundry_A','laundry_B']:bpy.data.collections[name].hide_render=True
bpy.data.collections['laundry_A' if v=='08' else 'laundry_B'].hide_render=False
cams=[o for o in bpy.data.objects if o.type=='CAMERA' and o.name.startswith(v+' ')]
s.camera=cams[0]
# The layers are all retained in the GLB. Cutaways remove whole shell parts for clear access.
if v in ['05','10','11']:
 bpy.data.collections['shell'].hide_render=True
 bpy.data.collections['tow_car'].hide_render=True
 if v=='05':
  for name in ['Tail weather enclosure ESTIMATE','Removable gasketed enclosure lid ESTIMATE']:bpy.data.objects[name].hide_render=True
  for o in bpy.data.collections['interior'].objects:
   o.hide_render=True
  # Ghosted floor plane and wall perimeter imply the original coach envelope.
  ghost=bpy.data.materials.new('Ghost shell concept');ghost.diffuse_color=(.25,.28,.29,1);ghost.use_nodes=True
  p=ghost.node_tree.nodes.get('Principled BSDF');p.inputs['Base Color'].default_value=(.55,.58,.56,1)
  nt=ghost.node_tree;out=nt.nodes.get('Material Output');tr=nt.nodes.new('ShaderNodeBsdfTransparent');mix=nt.nodes.new('ShaderNodeMixShader');mix.inputs[0].default_value=.65;nt.links.new(tr.outputs[0],mix.inputs[1]);nt.links.new(p.outputs[0],mix.inputs[2]);nt.links.new(mix.outputs[0],out.inputs['Surface'])
  outlines=[]
  for z in [.845,3.0]:outlines.append([(1.95,-1.155,z),(7.925,-1.155,z),(7.925,1.155,z),(1.95,1.155,z),(1.95,-1.155,z)])
  for x in [1.95,7.925]:
   for y in [-1.155,1.155]:outlines.append([(x,y,.845),(x,y,3.0)])
  for y in [-1.155,1.155]:outlines.append([(.42,y,2.42),(.42,y,2.96),(.70,y,3.07),(2.22,y,3.07)])
  for idx,points in enumerate(outlines):
   cu=bpy.data.curves.new('Ghost silhouette','CURVE');cu.dimensions='3D';cu.bevel_depth=.004;cu.bevel_resolution=2;sp=cu.splines.new('POLY');sp.points.add(len(points)-1)
   for pt,co in zip(sp.points,points):pt.co=(*co,1)
   ob=bpy.data.objects.new('Ghost outline '+str(idx),cu);bpy.data.collections['diagram'].objects.link(ob);cu.materials.append(ghost)
  bpy.data.collections['laundry_A'].hide_render=True;bpy.data.collections['laundry_B'].hide_render=True
 elif v=='10':
  s.camera.location.x=3.98;s.camera.data.ortho_scale=9.2
  s.camera.rotation_euler=(Vector((3.98,0,0))-s.camera.location).to_track_quat('-Z','Y').to_euler()
  bpy.data.collections['solar'].hide_render=True
  for o in bpy.data.collections['power'].objects:
   if '18K' in o.name or 'AC ' in o.name or 'condenser' in o.name or 'shroud' in o.name:o.hide_render=True
  for o in bpy.data.collections['interior'].objects:
   if any(t in o.name for t in ['Ceiling','ceiling','Lift bed platform','Queen mattress','Bed pillow','Overhead galley','Galley upper','Recessed','Ducted HVAC','Return grille']):o.hide_render=True
  # Shortened partitions retain floorplan relationships without hiding fixtures.
  for o in bpy.data.collections['interior'].objects:
   if o.name.startswith('Bath ') and any(t in o.name for t in ['wall','slider']):o.scale.z=.45;o.location.z=1.37
 elif v=='11':
  bpy.data.collections['interior'].hide_render=True;bpy.data.collections['tow_car'].hide_render=True
if v in ['06','07','08','09']:
 if v=='06':
  s.camera.location.y=-.79;s.camera.rotation_euler=(Vector((6.80,.45,1.83))-s.camera.location).to_track_quat('-Z','Y').to_euler()
 bpy.data.collections['solar'].hide_render=True
 bpy.data.collections['tow_car'].hide_render=True
 # Roof remains in render for light bounce; camera is inside it.
 s.view_settings.exposure=.30
 s.cycles.samples=32
 # Clear foreground bath slider only in A closeup; dry bath footprint kept intact.
 if v=='09':
  s.camera.location=(5.15,.06,2.02);s.camera.data.lens=19;s.camera.rotation_euler=(Vector((6.80,0,1.58))-s.camera.location).to_track_quat('-Z','Y').to_euler()
  for o in bpy.data.collections['interior'].objects:
   if 'chair' in o.name.lower():o.hide_render=True
 if v=='08':
  s.camera.location=(4.40,-.43,1.86);s.camera.data.lens=26;s.camera.rotation_euler=(Vector((5.51,.59,1.37))-s.camera.location).to_track_quat('-Z','Y').to_euler()
  for o in bpy.data.collections['interior'].objects:
   if o.name.startswith('Bath corridor wall') or o.name.startswith('Bath slider'):o.hide_render=True
if v=='04':
 bpy.data.collections['laundry_A'].hide_render=True;bpy.data.collections['laundry_B'].hide_render=True
 bpy.data.collections['tow_car'].hide_render=True
 for name in ['Removable gasketed enclosure lid ESTIMATE','Tail weather enclosure ESTIMATE']:
  bpy.data.objects[name].hide_render=True
 # Layered cutaway enables view of enclosed hardware, not a road-ready uncovered arrangement.
 s.camera.location=(9.1,-3.2,.16);s.camera.rotation_euler=(Vector((7.4,-.05,.4))-s.camera.location).to_track_quat('-Z','Y').to_euler()
 bpy.data.collections['shell'].hide_render=True;bpy.data.collections['interior'].hide_render=True;bpy.data.collections['solar'].hide_render=True
 # Keep only tail subset for unambiguous enclosure and spare study.
 for o in bpy.data.collections['power'].objects:
  if o.location.x<6.5:o.hide_render=True
if v in ['02','03']:bpy.data.collections['tow_car'].hide_render=True
if v=='12':
 # A moonlit studio sky and extended floor avoid a finite-ground/horizon stripe.
 wn=s.world.node_tree
 for n in wn.nodes:
  if n.type=='BACKGROUND':
   for link in list(n.inputs['Color'].links):wn.links.remove(link)
   n.inputs['Color'].default_value=(.016,.025,.040,1)
 for o in bpy.data.collections['environment'].objects:
  if o.type=='MESH':o.scale.x*=50;o.scale.y*=50
 for n in s.world.node_tree.nodes:
  if n.type=='BACKGROUND':n.inputs['Strength'].default_value=.12
 for o in bpy.data.collections['lighting'].objects:
  if o.type=='LIGHT' and o.name.startswith('Large studio'):o.data.energy=240;o.data.color=(.55,.67,1)
  if o.type=='LIGHT' and o.name.startswith('Soft rear'):o.data.energy=180;o.data.color=(.50,.61,.85)
 for o in bpy.data.objects:
  if o.name.startswith('Tinted window glazing'):
   m=o.data.materials[0].copy();o.data.materials[0]=m;p=m.node_tree.nodes.get('Principled BSDF');p.inputs['Base Color'].default_value=(.20,.12,.05,1);p.inputs['Emission Color'].default_value=(.40,.23,.09,1);p.inputs['Emission Strength'].default_value=.75
 s.view_settings.exposure=.9;s.cycles.samples=32
s.render.resolution_percentage=50 if preview else 100
s.render.filepath=str(R/'renders'/f'{v}{"-preview" if preview else ""}.png')
# Simplification lowers CPU burden without replacing actual modeled geometry.
s.render.use_simplify=True;s.render.simplify_subdivision_render=1
s.cycles.adaptive_threshold=.07
bpy.context.view_layer.update()
anchors={'front_axle':(.9652,0,.355),'rear_axle':(5.4864,0,.355),'front':(0,0,0),'rear':(7.9248,0,0),'ac':(4.9,0,3.42),'starlink':(4.9,-.75,3.20),'vent':(4.9,.72,3.16),'combiner':(4.78,-1.0,3.1),'rv5':(7.727,-.46,.41),'battery':(7.18,-.705,.38),'spare':(7.34,.69,.45),'orion':(2.57,.81,.60),'generator':(3.81,-.61,.54),'laundryA':(5.51,.74,1.5),'laundryB':(6.61,-.75,1.5),'desk':(6.78,.82,1.59),'bath':(4.39,.74,1.3),'kitchen':(3.99,-.79,1.65),'couch':(2.92,.76,1.3),'bed':(6.81,0,2.58),'roof_start':(2.16,0,3.1),'roof_end':(7.658084,0,3.1),'tailbottom':(7.42,-.46,.2589)}
pix={}
for name,p in anchors.items():
 q=world_to_camera_view(s,s.camera,Vector(p));pix[name]=[round(q.x*1920,1),round((1-q.y)*1080,1),round(q.z,2)]
(R/'renders'/f'{v}-anchors.json').write_text(json.dumps(pix,indent=2))
print('RENDER_START',v,flush=True);bpy.ops.render.render(write_still=True);print('RENDER_COMPLETE',v,flush=True)
