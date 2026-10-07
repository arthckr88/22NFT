"""Detailed Alita study: metres, +X rearward, +Y driver side. All placement coordinates ESTIMATE.
Run: blender -b -t 4 --python scripts/build_model.py -- [view number|build]
"""
import bpy, math, json, pathlib, sys
from mathutils import Vector
R=pathlib.Path(__file__).resolve().parents[1]; IN=.0254
bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete(use_global=False)
for c in list(bpy.data.collections):
 if c.name!='Collection': bpy.data.collections.remove(c)
scene=bpy.context.scene
scene.unit_settings.system='METRIC'
COL={}
for n in ['shell','power','solar','laundry_A','laundry_B','interior','chassis','tow_car','lighting','environment','diagram']:
 c=bpy.data.collections.new(n); scene.collection.children.link(c); COL[n]=c
layer='shell'
def put(o,name,material=None):
 o.name=name
 for c in list(o.users_collection): c.objects.unlink(o)
 COL[layer].objects.link(o)
 if material: o.data.materials.append(material)
 return o
def mat(name,color,metal=0,rough=.4,emission=0):
 m=bpy.data.materials.new(name); m.diffuse_color=(*color,1); m.use_nodes=True
 p=m.node_tree.nodes.get('Principled BSDF'); p.inputs['Base Color'].default_value=(*color,1); p.inputs['Metallic'].default_value=metal;p.inputs['Roughness'].default_value=rough
 if emission:p.inputs['Emission Color'].default_value=(*color,1);p.inputs['Emission Strength'].default_value=emission
 return m
bone=mat('Warm pearl fiberglass',(.72,.73,.70),.16,.26); black=mat('Charcoal satin',(.012,.017,.019),0,.52); bronze=mat('Dark bronze',(.20,.16,.09),.75,.23)
rubber=mat('Tire rubber',(.012,.015,.016),0,.65); chrome=mat('Machined alloy',(.46,.49,.51),.88,.2); glass=mat('Smoked tinted glass',(.019,.045,.060),.42,.13)
glass.node_tree.nodes['Principled BSDF'].inputs['Coat Weight'].default_value=.6
linen=mat('Charcoal woven upholstery',(.035,.041,.043),0,.85); ceiling=mat('Bone microtexture',(.57,.55,.49),0,.85)
wood=mat('Warm white oak',(.28,.19,.105),0,.45)
nt=wood.node_tree;p=nt.nodes['Principled BSDF'];tex=nt.nodes.new('ShaderNodeTexNoise');tex.inputs['Scale'].default_value=7;tex.inputs['Detail'].default_value=3
mapping=nt.nodes.new('ShaderNodeVectorMath');mapping.operation='MULTIPLY';mapping.inputs[1].default_value=(3,65,7)
coords=nt.nodes.new('ShaderNodeTexCoord');nt.links.new(coords.outputs['Generated'],mapping.inputs[0]);nt.links.new(mapping.outputs[0],tex.inputs['Vector'])
ramp=nt.nodes.new('ShaderNodeValToRGB');ramp.color_ramp.elements[0].color=(.07,.04,.015,1);ramp.color_ramp.elements[1].color=(.30,.20,.105,1);nt.links.new(tex.outputs['Fac'],ramp.inputs[0]);nt.links.new(ramp.outputs[0],p.inputs['Base Color'])
bump=nt.nodes.new('ShaderNodeBump');bump.inputs['Strength'].default_value=.13;bump.inputs['Distance'].default_value=.008;nt.links.new(tex.outputs['Fac'],bump.inputs['Height']);nt.links.new(bump.outputs[0],p.inputs['Normal'])
stone=mat('Honed black stone',(.027,.031,.033),0,.28);white=mat('Appliance enamel',(.69,.70,.66),.15,.27)
solarblue=mat('N-type silicon',(.014,.034,.050),.52,.21); solarline=mat('Cell metallization',(.28,.37,.39),.65,.28)
warm=mat('Warm 2700K light',(.95,.58,.25),0,.25,4); cool=mat('Display glow',(.30,.61,.68),0,.3,2)
routegold=mat('PV route gold',(.62,.45,.13),.3,.32);routeblue=mat('48V route blue',(.06,.34,.55),.2,.36);routegreen=mat('AC route sage',(.22,.49,.33),.2,.4);routecyan=mat('Alternator route cyan',(.1,.55,.61),.2,.4)

def box(name,loc,dim,ma,bevel=.02):
 v=[(sx*dim[0]/2,sy*dim[1]/2,sz*dim[2]/2) for sx,sy,sz in [(-1,-1,-1),(-1,-1,1),(-1,1,-1),(-1,1,1),(1,-1,-1),(1,-1,1),(1,1,-1),(1,1,1)]]
 me=bpy.data.meshes.new(name);me.from_pydata(v,[],[tuple(reversed(f)) for f in [(0,4,6,2),(1,3,7,5),(0,1,5,4),(2,6,7,3),(0,2,3,1),(4,5,7,6)]]);me.update()
 o=bpy.data.objects.new(name,me);COL[layer].objects.link(o);o.location=loc
 if ma:me.materials.append(ma)
 if bevel:
  m=o.modifiers.new('Soft manufactured edges','BEVEL');m.width=bevel;m.segments=3
  o.modifiers.new('Weighted normals','WEIGHTED_NORMAL')
 return o

def cyl(name,loc,r,depth,ma,axis='Z',verts=48):
 v=[(r*math.cos(i*math.tau/verts),r*math.sin(i*math.tau/verts),z) for z in [-depth/2,depth/2] for i in range(verts)]
 faces=[tuple(range(verts-1,-1,-1)),tuple(range(verts,2*verts))]+[(i,(i+1)%verts,(i+1)%verts+verts,i+verts) for i in range(verts)]
 me=bpy.data.meshes.new(name);me.from_pydata(v,[],faces);me.update();me.materials.append(ma);o=bpy.data.objects.new(name,me);COL[layer].objects.link(o);o.location=loc
 if axis=='Y':o.rotation_euler[0]=math.pi/2
 if axis=='X':o.rotation_euler[1]=math.pi/2
 for p in me.polygons:p.use_smooth=True
 m=o.modifiers.new('Machined edge','BEVEL');m.width=.005;m.segments=2
 return o

def tube(name,points,r,ma):
 c=bpy.data.curves.new(name,'CURVE');c.dimensions='3D';c.bevel_depth=r;c.bevel_resolution=3
 s=c.splines.new('POLY');s.points.add(len(points)-1)
 for p,co in zip(s.points,points):p.co=(*co,1)
 o=bpy.data.objects.new(name,c);COL[layer].objects.link(o);o.data.materials.append(ma);return o

def torus(name,loc,major,minor,ma,axis='Y'):
 n=48;k=12;v=[]
 for i in range(n):
  a=i*math.tau/n
  for j in range(k):
   b=j*math.tau/k;v.append(((major+minor*math.cos(b))*math.cos(a),(major+minor*math.cos(b))*math.sin(a),minor*math.sin(b)))
 faces=[(i*k+j,((i+1)%n)*k+j,((i+1)%n)*k+(j+1)%k,i*k+(j+1)%k) for i in range(n) for j in range(k)]
 me=bpy.data.meshes.new(name);me.from_pydata(v,[],faces);me.update();me.materials.append(ma);o=bpy.data.objects.new(name,me);COL[layer].objects.link(o);o.location=loc
 if axis=='Y':o.rotation_euler[0]=math.pi/2
 for p in me.polygons:p.use_smooth=True
 return o

def profile(name,points,width,ma,bevel=.06):
 verts=[(x,y,z) for y in [-width/2,width/2] for x,z in points];n=len(points)
 faces=[tuple(range(n-1,-1,-1)),tuple(range(n,2*n))]+[(i,(i+1)%n,(i+1)%n+n,i+n) for i in range(n)]
 me=bpy.data.meshes.new(name);me.from_pydata(verts,[],faces);me.update();o=bpy.data.objects.new(name,me);COL[layer].objects.link(o);me.materials.append(ma)
 if bevel:m=o.modifiers.new('Moulded fiberglass radii','BEVEL');m.width=bevel;m.segments=6;o.modifiers.new('Normals','WEIGHTED_NORMAL')
 return o

def cut(o,loc,dim,roundhole=False):
 bpy.context.view_layer.objects.active=o
 # Apply edge modifiers before the boolean, avoiding duplicated bevels on concave faces.
 for mod in list(o.modifiers):bpy.ops.object.modifier_apply(modifier=mod.name)
 q=cyl('temporary round cutter',loc,dim[0]/2,dim[1],black,'Y',64) if roundhole else box('temporary cutter',loc,dim,None,0)
 for mod in list(q.modifiers):q.modifiers.remove(mod)
 bpy.context.view_layer.objects.active=o
 m=o.modifiers.new('Physical opening','BOOLEAN');m.operation='DIFFERENCE';m.object=q;m.solver='EXACT';bpy.ops.object.modifier_apply(modifier=m.name)
 bpy.data.objects.remove(q,do_unlink=True)
 for poly in o.data.polygons:poly.use_smooth=False

# Frame, suspension, tires, differential, spare (reconstructed, not surveyed).
layer='chassis'
for y in [-.44,.44]:box('Frame rail ESTIMATE',(4.6,y,.60),(6.4,.09,.15),black,.013)
for x in [2.1,3.15,4.3,5.5,6.45,7.4]:box('Crossmember ESTIMATE',(x,0,.64),(.08,1.96,.1),black,.01)
for x in [.9652,5.4864]:
 cyl('Axle ESTIMATE',(x,0,.355),.065,1.75,black,'Y');cyl('Differential',(x,0,.355),.14,.27,black,'Y')
 for y in [-.93,.93]:
  torus('All-season tire',(x,y,.355),.262,.09,rubber)
  cyl('Rim barrel',(x,y,.355),.234,.175,chrome,'Y')
  side=y+(.099 if y>0 else -.099);cyl('Wheel inset',(x,side,.355),.195,.008,black,'Y');cyl('Alloy hub',(x,side+(.01 if y>0 else -.01),.355),.065,.025,chrome,'Y')
  for i in range(6):
   a=i*math.tau/6
   sp=box('Alloy spoke',(x+.12*math.cos(a),side,.355+.12*math.sin(a)),(.17,.026,.045),chrome,.01);sp.rotation_euler[1]=-a
   cyl('Lug',(x+.04*math.cos(a),side+(.025 if y>0 else -.025),.355+.04*math.sin(a)),.009,.014,chrome,'Y',16)
  for i in range(44):
   a=i*math.tau/44;tr=box('Tire shoulder tread',(x+.342*math.cos(a),y,.355+.342*math.sin(a)),(.03,.14,.012),rubber,.003);tr.rotation_euler[1]=math.pi/2-a
  box('Mud flap',(x+.42,y,.28),(.035,.31,.37),rubber,.008)
for y in [-.735,.735]:
 torus('Inner rear dual tire ESTIMATE',(5.4864,y,.355),.262,.09,rubber)
 cyl('Inner rear steel rim ESTIMATE',(5.4864,y,.355),.226,.165,black,'Y')
# Spare offset driver-side next to enclosure, not an asserted factory coordinate.
torus('Spare tire ESTIMATE',(7.34,.69,.45),.26,.09,rubber,'Z');cyl('Spare steel rim',(7.34,.69,.45),.21,.12,black)
box('Spare carrier ESTIMATE',(7.34,.69,.57),(.7,.65,.035),chrome,.01)
for y in [-.43,.43]:tube('Rear leaf spring',[(5.05,y,.46),(5.49,y,.52),(5.94,y,.46)],.023,black)
box('Tow receiver',(7.89,0,.47),(.35,.09,.09),black,.015)

# Shell with real side-wall apertures and rounded cap.
layer='shell'
floor=box('Coach insulated floor',(4.91,0,.845),(5.93,2.31,.12),black,.05)
roof=box('Rounded roof',(4.82,0,3.00),(6.21,2.31,.12),bone,.07)
wallplus=box('Driver fiberglass wall',(4.91,1.125,1.92),(5.93,.075,2.08),bone,.04)
wallminus=box('Passenger fiberglass wall',(4.91,-1.125,1.92),(5.93,.075,2.08),bone,.04)
windows=[(2.78,1,2.08,1.05,.58),(6.74,1,2.15,1.32,.58),(3.99,-1,2.13,.91,.50),(6.84,-1,2.16,1.04,.56)]
for x,side,z,w,h in windows:
 wall=wallplus if side>0 else wallminus
 cut(wall,(x,side*1.125,z),(w,.3,h))
 box('Window black frame',(x,side*1.133,z),(w+.07,.055,h+.07),black,.04)
 box('Tinted window glazing',(x,side*1.171,z),(w-.025,.012,h-.025),glass,.026)
 box('Sliding glazing mullion',(x+.10,side*1.182,z),(.015,.014,h-.035),black,.003)
cut(wallminus,(2.70,-1.125,1.78),(.69,.3,1.74))
box('Entry door weather frame',(2.70,-1.157,1.78),(.735,.043,1.80),black,.05)
box('Entry door',(2.70,-1.184,1.78),(.675,.026,1.74),bone,.04)
box('Entry glass',(2.70,-1.205,2.18),(.46,.012,.55),glass,.035);box('Entry latch',(2.93,-1.224,1.69),(.06,.02,.13),black,.012)
for z in [.64,.45]:box('Retracting entry step',(2.7,-1.34,z),(.72,.44,.035),chrome,.025)
# Rounded rear cap, rear cargo hatch, bumper
rear=box('Moulded rear cap',(7.88,0,1.93),(.13,2.31,2.13),bone,.085)
box('Rear cargo access frame',(7.96,0,1.30),(.045,1.70,.74),black,.06)
box('Rear cargo hatch',(7.992,0,1.30),(.018,1.63,.67),bone,.035)
for y in [-.61,.61]:box('Rear hatch latch',(8.008,y,1.24),(.014,.09,.06),black,.01)
box('Rear lower bumper',(7.99,0,.64),(.14,2.24,.17),black,.03)
for y in [-.97,.97]:
 box('Tail lamp housing',(7.97,y,1.80),(.04,.15,.29),black,.02)
 box('Neutral smoked tail lens',(7.998,y,1.80),(.015,.11,.23),glass,.014)
# Cab sculpted side profile: no logos
cab=profile('Transit cab sculpted envelope',[(.03,.63),(.02,1.07),(.24,1.22),(.75,1.32),(1.17,2.07),(1.40,2.28),(2.07,2.28),(2.23,1.91),(2.25,.68)],2.02,bone,.09)
for side in [-1,1]:
 cut(cab,(.9652,side*.96,.355),(.82,.46,.82),True)
 # side glazing with angled front edge
 pane=profile('Cab side glass',[(1.03,1.41),(1.36,2.02),(1.96,2.03),(2.07,1.47)],.024,glass,.026);pane.location.y=side*1.017
 tube('Cab door seam',[(1.01,side*1.02,1.32),(1.12,side*1.024,.78),(2.11,side*1.025,.79),(2.12,side*1.03,2.10)],.007,black)
 box('Cab door pull',(1.98,side*1.043,1.36),(.13,.025,.027),black,.01)
 tube('Mirror arm',[(1.23,side*1.01,1.52),(1.20,side*1.23,1.54)],.024,black)
 box('Mirror',(1.21,side*1.29,1.64),(.20,.09,.29),black,.045)
wind=box('Sloped windshield',(.945,0,1.675),(.035,1.66,.76),glass,.045);wind.rotation_euler[1]=.50
for y in [-.4,.4]:tube('Wiper',[(.93,y,1.40),(1.03,y+.26,1.57)],.007,black)
box('Front bumper',(.039,0,.74),(.15,1.99,.20),black,.045)
box('Grille recess',(.012,0,1.01),(.03,.93,.23),black,.04)
for z in [.94,1.00,1.06]:box('Grille bar',(-.01,0,z),(.01,.89,.012),chrome,.002)
for y in [-.74,.74]:
 box('Headlamp shell',(.11,y,1.12),(.10,.35,.16),black,.035)
 box('Headlamp lens',(.048,y,1.135),(.014,.29,.09),white,.025)
# Class C cab-over nose, softly rounded, separate from vertical living walls
cap=profile('Rounded cab-over fiberglass',[(.40,2.38),(.34,2.74),(.48,2.97),(.70,3.07),(2.24,3.07),(2.30,2.41)],2.31,bone,.10)
box('Cab-over underside',(1.40,0,2.40),(1.83,2.15,.065),black,.04)
for side in [-1,1]:
 box('Cab-over accent',(1.43,side*1.159,2.72),(1.34,.012,.13),black,.03)
 # coach lower skirts, seams, compartments
 box('Lower charcoal skirt',(5.03,side*1.145,1.00),(5.52,.02,.20),black,.012)
 for x,w in [(3.64,1.05),(5.05,.82),(6.06,.66)]:
  box('Compartment door gasket',(x,side*1.159,1.10),(w,.02,.40),black,.025)
  box('Compartment door',(x,side*1.174,1.10),(w-.035,.013,.366),bone,.018)
  box('Compartment latch',(x,side*1.185,1.22),(.065,.015,.036),black,.01)
 tube('Roof perimeter seam',[(2.25,side*1.135,2.94),(7.75,side*1.135,2.94)],.009,black)
# Awning cassette, light strip
box('16 foot awning cassette',(4.80,-1.22,2.76),(4.8768,.145,.17),black,.04)
box('Awning LED strip',(4.8,-1.275,2.685),(4.65,.02,.014),warm,.002)

# Interior, preserving factory relationships. All furniture coordinate envelopes estimated.
layer='interior'
box('White oak finished floor',(4.91,0,.915),(5.78,2.14,.04),wood,.01)
for x in [2.22+i*.18 for i in range(31)]:tube('Floor plank seam',[(x,-1.055,.938),(x,1.055,.938)],.0016,black)
box('Ceiling liner',(4.91,0,2.915),(5.80,2.15,.025),ceiling,.01)
# Rear bed 80in across /60in longitudinal, raised only.
box('Lift bed platform RAISED',(6.81,0,2.58),(1.524,2.032,.075),black,.035)
box('Queen mattress 60x80',(6.81,0,2.71),(1.484,1.992,.20),linen,.09)
for y in [-.67,.67]:box('Bed pillow',(7.28,y,2.855),(.43,.54,.11),ceiling,.07)
for x in [6.10,7.53]:
 for y in [-1.04,1.04]:box('Lift bed track ESTIMATE',(x,y,1.94),(.035,.05,1.82),chrome,.012)
# Cab-over sleeping surface
box('Cab-over mattress',(1.36,0,2.57),(1.70,1.98,.18),linen,.07)
for y in [-.48,.48]:
 box('Cab captain seat',(1.84,y,1.07),(.46,.47,.16),linen,.06)
 box('Cab seat back',(2.02,y,1.42),(.14,.47,.60),linen,.05)
 box('Cab headrest',(2.04,y,1.78),(.14,.26,.18),linen,.04)
box('Cab instrument deck',(1.00,0,1.20),(.35,1.73,.15),black,.04)
torus('Steering wheel',(1.45,.48,1.36),.16,.014,black,'Y')
# Front couch driver side with articulated cushions and welting
box('Forward couch oak plinth',(2.92,.76,1.04),(1.34,.63,.25),wood,.02)
for x in [2.59,3.26]:
 box('Couch seat cushion',(x,.70,1.24),(.64,.69,.20),linen,.055)
 box('Couch back',(x,1.01,1.59),(.64,.16,.57),linen,.055)
 for z in [1.33,1.84]:tube('Couch piping',[(x-.30,.90,z),(x+.30,.90,z)],.003,bronze)
for x in [2.22,3.61]:box('Couch arm',(x,.70,1.43),(.12,.71,.52),linen,.035)
# Kitchen on passenger side
box('Kitchen carcass',(3.99,-.79,1.28),(1.20,.59,.69),black,.018)
box('Stone kitchen worktop',(3.99,-.78,1.655),(1.26,.66,.05),stone,.018)
for x,w in [(3.58,.34),(3.99,.38),(4.39,.30)]:
 for z,h in [(1.12,.29),(1.44,.23)]:
  box('Kitchen oak drawer',(x,-.477,z),(w,.022,h),wood,.008);box('Bronze recessed pull',(x,-.458,z+.07),(.15,.016,.012),bronze,.003)
sink=box('Sink rim',(3.66,-.82,1.69),(.39,.38,.015),chrome,.03)
box('Sink dark bowl',(3.66,-.82,1.703),(.34,.33,.009),black,.06)
tube('Kitchen faucet',[(3.67,-1.01,1.68),(3.67,-1.01,1.96),(3.67,-.86,1.98),(3.67,-.81,1.91)],.013,chrome)
box('Induction cooktop',(4.28,-.79,1.692),(.44,.41,.019),black,.02)
for x in [4.17,4.39]:torus('Induction zone',(x,-.79,1.704),.085,.002,chrome,'Z')
box('Kitchen backsplash',(4.02,-1.078,1.89),(1.30,.015,.38),stone,.005)
for x in [3.58,4.04,4.48]:
 box('Overhead galley cabinet',(x,-.83,2.60),(.42,.49,.47),wood,.018)
 box('Galley upper door',(x,-.571,2.6),(.39,.02,.44),black,.005)
box('Galley task light',(4,-.60,2.345),(1.19,.03,.014),warm,.002)
# Fridge/pantry immediately aft galley
box('Refrigerator tower',(5.03,-.80,1.82),(.70,.61,1.78),wood,.024)
for z,h in [(1.43,.95),(2.32,.73)]:
 box('Fridge matte door',(5.03,-.475,z),(.65,.035,h),black,.025)
 box('Fridge vertical handle',(5.30,-.446,z),(.024,.035,h*.54),bronze,.008)
# Dry bath driver side: solid walls, shower, toilet, sliding doorway
box('Bath outer rear wall',(5.06,.72,1.89),(.05,.73,1.88),black,.012)
box('Bath forward wall',(3.71,.72,1.89),(.05,.73,1.88),black,.012)
box('Bath corridor wall',(4.39,.342,1.89),(1.40,.04,1.88),black,.013)
cut(bpy.data.objects['Bath corridor wall'],(4.17,.342,1.78),(.56,.15,1.64))
box('Bath slider parked',(4.74,.302,1.80),(.52,.035,1.71),wood,.015)
box('Shower tray',(4.59,.79,.978),(.74,.56,.075),white,.04)
box('Shower glass partition',(4.36,.79,1.83),(.012,.58,1.56),glass,.008)
tube('Shower mixer/rail',[(4.91,1.03,1.34),(4.91,1.03,2.38),(4.84,1.03,2.42)],.011,chrome)
box('Toilet pedestal',(3.96,.79,1.10),(.33,.43,.32),white,.07);box('Toilet lid',(3.96,.75,1.28),(.36,.44,.08),white,.065)
# Rear desk + preserved drawers driver side
box('Factory desk warm oak top',(6.78,.82,1.59),(1.81,.56,.055),wood,.025)
box('Factory storage pedestal',(7.41,.82,1.25),(.48,.51,.63),black,.012)
for z in [1.055,1.25,1.445]:
 box('Factory desk drawer',(7.41,.548,z),(.44,.022,.173),wood,.008)
 box('Desk drawer finger pull',(7.41,.531,z+.055),(.20,.012,.012),bronze,.002)
box('Desk leg',(6.02,.82,1.26),(.045,.49,.61),black,.008)
box('Editing monitor',(6.66,.945,1.99),(.79,.035,.43),black,.016)
box('Monitor subtle landscape',(6.66,.922,1.99),(.73,.003,.37),glass,.008)
box('Monitor stand',(6.66,.92,1.71),(.045,.06,.17),chrome,.01);box('Monitor base',(6.66,.87,1.627),(.30,.17,.018),black,.012)
box('Keyboard',(6.64,.69,1.634),(.40,.14,.018),black,.011)
for i in range(15):
 for j in range(4):box('Keyboard key',(6.46+i*.024,.635+j*.029,1.647),(.017,.018,.004),ceiling,.001)
box('Editing laptop',(6.13,.82,1.625),(.32,.23,.019),black,.012)
box('Desk task light stem',(7.15,1.0,1.89),(.018,.018,.5),bronze,.005);box('Desk task light',(7.15,.91,2.15),(.27,.19,.018),warm,.005)
# Small studio chair and camera gear in rear garage
box('Studio chair seat',(6.65,.07,1.22),(.47,.45,.12),linen,.06)
box('Studio chair back',(6.65,-.14,1.51),(.46,.08,.52),linen,.045)
cyl('Chair pedestal',(6.65,.07,1.05),.032,.24,chrome)
for a in range(5):
 q=a*math.tau/5;tube('Chair base spoke',[(6.65,.07,.962),(6.65+.29*math.cos(q),.07+.29*math.sin(q),.962)],.013,black)
for x in [7.26,7.68]:
 box('Camera hard case',(x,-.71,1.095),(.33,.54,.31),black,.035)
 for y in [-.95,-.49]:box('Case clasp',(x,y,1.17),(.08,.012,.03),chrome,.003)
 box('Case handle',(x,-.71,1.265),(.17,.045,.025),rubber,.008)
box('Ribbed luggage',(6.05,-.83,1.30),(.35,.32,.69),black,.06)
for x in [5.93+i*.031 for i in range(9)]:box('Luggage rib',(x,-1.005,1.3),(.006,.012,.54),chrome,.002)
for x in [7.56,7.69,7.79]:tube('Folded light stand',[(x,-1.0,.99),(x,-1.0,2.04)],.014,black)
# Decorative acoustic slat strip and concealed LEDs
for x in [5.85+i*.047 for i in range(43)]:box('Desk acoustic oak slat',(x,1.076,2.02),(.020,.014,.76),wood,.005)
for y in [-1.015,1.015]:box('Warm concealed ceiling LED',(4.8,y,2.888),(5.5,.012,.014),warm,.002)
for x in [2.52,3.55,5.44]:
 cyl('Recessed ceiling fixture',(x,0,2.895),.065,.018,bronze);cyl('Recessed LED diffuser',(x,0,2.881),.050,.006,warm)
# HVAC return and actual duct visualization below roof unit
box('Ducted HVAC return grille',(4.957,0,2.885),(.53,.47,.028),black,.025)
for x in [4.74+i*.026 for i in range(17)]:box('Return grille louvre',(x,0,2.861),(.008,.41,.008),ceiling,.002)
for x in [2.65,3.45,5.45,6.1]:
 for y in [-.62,.62]:box('Existing duct register ESTIMATE',(x,y,2.888),(.18,.10,.012),black,.012)

# Washer alternatives accurately scaled, front faces into aisle, no under-desk placement.
def washer(prefix,x,y,side):
 global layer
 layer='laundry_'+prefix
 # front faces -Y for driver side, +Y for passenger side
 front=-side;d=.55245;w=.5969;h=.847725;base=.94
 box(prefix+' dedicated level floor support ESTIMATE',(x,y,base-.025),(w+.08,d+.08,.05),black,.01)
 box(prefix+' washer cabinet',(x,y,base+h/2),(w,d,h),white,.016)
 fy=y+front*(d/2+.002)
 box(prefix+' charcoal fascia',(x,fy,base+h-.077),(w-.04,.013,.12),black,.006)
 cyl(prefix+' control dial',(x+w*.25,fy+front*.007,base+h-.075),.028,.010,chrome,'Y')
 for i in range(5):cyl(prefix+' control button',(x-.15+i*.044,fy+front*.010,base+h-.075),.005,.004,cool,'Y',12)
 cyl(prefix+' door bezel',(x,fy+front*.004,base+.39),.229,.018,chrome,'Y')
 cyl(prefix+' door black rim',(x,fy+front*.012,base+.39),.204,.008,black,'Y')
 cyl(prefix+' tinted washer glass',(x,fy+front*.015,base+.39),.169,.006,glass,'Y')
 box(prefix+' door handle',(x+.17,fy+front*.015,base+.39),(.025,.010,.14),white,.008)
 for xx in [x-w*.35,x+w*.35]:
  for yy in [y-d*.34,y+d*.34]:cyl(prefix+' vibration isolator',(xx,yy,base-.01),.025,.025,rubber)
 # 4 in dedicated metal duct, supply and independent standpipe; illustrative topology.
 backy=y-front*(d/2+.028)
 tube(prefix+' 4 inch metal exhaust ESTIMATE',[(x+.20,backy,base+.17),(x+.20,side*1.07,base+.17)],.0508,chrome)
 box(prefix+' exterior vent hood ESTIMATE',(x+.20,side*1.178,base+.17),(.16,.03,.17),black,.013)
 for xx,ma in [(x-.19,routeblue),(x-.15,routegold)]:tube(prefix+' hot cold routing ESTIMATE',[(xx,backy,base+.59),(xx,backy,.80),(4.02,-1.035,.80),(4.02,-1.035,1.30)],.008,ma)
 tube(prefix+' trapped washer standpipe ESTIMATE',[(x-.23,backy,base+.74),(x-.23,backy,base+.06),(x-.16,backy,base+.06),(x-.16,backy,.80),(4.1,-1.04,.80)],.019,black)
washer('A',5.51,.74,1);washer('B',6.61,-.75,-1)

# Roof: six landscape panels separated by center equipment band.
layer='solar';panelcenters=[];cursor=2.16
for i in range(6):
 if i==3:cursor+=.7493+.0254
 x=cursor+.766064/2;panelcenters.append(x);cursor+=.766064+.0254
 box(f'Panel {i+1} 275W aluminum frame',(x,0,3.142),( .766064,1.73609,.035052),chrome,.008)
 box(f'Panel {i+1} cell laminate',(x,0,3.162),(.733,1.704,.003),solarblue,.003)
 for a in range(6):
  for b in range(12):
   cx=x-.36+(a+.5)*.12;cy=-.84+(b+.5)*.14
   box(f'P{i+1} split cell',(cx,cy,3.165),(.115,.134,.001),solarblue,.002)
 for a in range(7):box('Cell grid seam',(x-.36+a*.12,0,3.167),(.002,1.68,.001),solarline,0)
 for b in range(13):box('Cell grid seam',(x,-.84+b*.14,3.167),(.72,.0015,.001),solarline,0)
 for xx in [x-.28,x+.28]:
  for yy in [-.90,.90]:box('Solar foot bracket ESTIMATE',(xx,yy,3.087),(.075,.11,.07),black,.006)
 for yy in [-.955,.955]:tube(f'P{i+1} PV drop',[(x,yy,3.134),(x,yy,3.085),(4.79,yy,3.085)],.004,black)
# AC in intervening band
layer='power';acx=(panelcenters[2]+.383032+.0254)+.7493/2
box('18K heat pump shroud',(acx,0,3.244),(.7493,.7366,.3683),black,.075)
for yy in [-.364,.364]:
 for x in [acx-.30+j*.029 for j in range(21)]:box('AC condenser louvre',(x,yy,3.235),(.009,.012,.20),chrome,.002)
for xx in [acx-.2,acx+.2]:box('AC shroud seam',(xx,0,3.429),(.01,.60,.004),black,.002)
# equipment band vents and antenna alongside AC: service clearances NOT claimed
layer='solar'
box('Starlink Standard 4X ESTIMATE mount',(acx,-.75,3.12),(.14,.14,.10),black,.02)
box('Starlink Standard antenna',(acx,-.75,3.192),(.594,.383,.0397),white,.036)
box('Bath roof vent ESTIMATE',(acx,.72,3.105),(.3556,.3556,.10),black,.025)
box('Bath vent translucent lid',(acx,.72,3.164),(.33,.33,.014),glass,.025)
cyl('Plumbing vent ESTIMATE',(5.45,.91,3.10),.032,.09,white)
box('Roof cable gland ESTIMATE',(4.8,-1.01,3.095),(.13,.09,.06),black,.014)
box('PV combiner bank 1 ESTIMATE',(4.65,-1.0,3.09),(.19,.11,.06),black,.012)
box('PV combiner bank 2 ESTIMATE',(5.09,-1.0,3.09),(.19,.11,.06),black,.012)

# Protected tail power compartment: shell and equipment separate for viewer toggles.
layer='power'
enc=box('Tail weather enclosure ESTIMATE',(7.42,-.46,.3783), (1.1557,.9398,.2388),black,.025)
# remove front/top face notion for view via removable service panel object; equipment kept inside
cut(enc,(7.42,-.46,.400),(1.1497,.9338,.276))
box('Removable gasketed enclosure lid ESTIMATE',(7.42,-.46,.49895),(1.1557,.9398,.0025),black,.015)
# Two horizontal packs side by side, both below the reconstructed frame rail.
for i,y in enumerate([-.705,-.225]):
 box('B4810 5.12kWh pack '+str(i+1),(7.18,y,.380),(.608,.38,.145),black,.018)
 for yy in [y-.1775,y+.1775]:box('Battery lifting handle',(7.18,yy,.438),(.24,.015,.012),chrome,.003)
 for xx in [6.97,7.39]:box('Battery restraint strap',(xx,y,.458),(.025,.40,.010),bronze,.003)
box('RV5 hub 48V inverter',(7.727,-.46,.410),(.450088,.500126,.1599),black,.018)
box('RV5 service display',(7.727,-.203,.41),(.14,.008,.045),cool,.005)
for x in [7.55+i*.018 for i in range(20)]:box('RV5 vent slot',(x,-.203,.39),(.007,.01,.08),chrome,.002)
for x in [6.96,7.87]:
 box('Proposed carrier channel ESTIMATE',(x,0,.64),(.08,1.96,.06),black,.007)
 for y in [-.90,-.02]:
  box('Formed mounting web ESTIMATE',(x,y,.5875),(.003,.07,.185),chrome,.001)
  box('Mount lower flange ESTIMATE',(x+.038,y,.497),(.08,.07,.003),chrome,.001)
  box('Mount upper flange ESTIMATE',(x+.038,y,.672),(.08,.07,.003),chrome,.001)
  for z in [.497,.672]:cyl('Generic mounting bolt ESTIMATE',(x+.038,y,z+.004),.0065,.005,bronze,'Z',12)
box('Tail service disconnect ESTIMATE',(6.99,.005,.42),(.08,.05,.12),bronze,.01)
# Forward Orions dry compartment, protected runs.
for x in [2.47,2.68]:
 box('Orion 12 to48 Smart provisional',(x,.81,.60),(.186,.08,.13),routeblue,.012)
 for j in range(7):box('Orion cooling fin',(x-.07+j*.023,.755,.60),(.012,.03,.12),black,.003)
box('Existing generator ESTIMATE',(3.81,-.61,.54),(.75,.65,.40),black,.06)
box('AC distribution ESTIMATE',(3.15,-.82,.75),(.29,.10,.24),black,.013)
box('AGS controller pending',(3.41,-.82,.73),(.11,.08,.11),bronze,.01)
# Full candidate runs. Colors exclude red; pending ties noted by dashed diagram in book.
tube('PV home run approx 5.9m ESTIMATE',[(4.79,-1.01,3.1),(5.35,-1.025,3.1),(5.35,-1.025,.74),(7.41,-.92,.65),(7.41,-.06,.48)],.014,routegold)
for y in [-.705,-.225]:tube('Battery 48V lead approx 0.7m ESTIMATE',[(7.18,y,.40),(7.48,y,.43),(7.72,-.20,.45)],.014,routeblue)
tube('Vehicle12V CCP run approx 2.2m ESTIMATE',[(1.54,.64,.94),(1.95,.73,.72),(2.55,.76,.68)],.014,routecyan)
tube('Orion output candidate approx 5.6m ESTIMATE',[(2.56,.76,.68),(3.2,.9,.73),(6.92,.90,.73),(7.25,-.25,.60)],.014,routecyan)
tube('Generator AC approx 5.0m ESTIMATE',[(3.8,-.58,.74),(3.8,-.96,.75),(7.42,-.96,.74),(7.42,-.04,.52)],.014,routegreen)
tube('House AC approx 5.0m ESTIMATE',[(7.42,-.04,.50),(7.0,-.92,.75),(3.14,-.92,.75)],.014,routegreen)
# Road towcar clean hatchback, black cabin glass and detailed wheels; no badges.
layer='tow_car'
car=profile('Generic small hatchback body',[(9.12,.28),(9.17,.72),(9.70,.88),(10.06,1.35),(10.39,1.49),(11.40,1.49),(12.25,1.1),(12.65,.7),(12.63,.3)],1.64,bone,.085)
for x in [9.87,12.03]:
 for side in [-1,1]:
  cut(car,(x,side*.75,.30),(.68,.40,.68),True)
  torus('Hatch tire',(x,side*.77,.30),.216,.074,rubber)
  cyl('Hatch alloy rim',(x,side*.835,.30),.19,.022,chrome,'Y')
  cyl('Hatch black rim inset',(x,side*.85,.30),.14,.015,black,'Y')
  for a in range(5):
   q=a*math.tau/5;sp=box('Hatch spoke',(x+.102*math.cos(q),side*.861,.30+.102*math.sin(q)),(.13,.013,.028),chrome,.004);sp.rotation_euler[1]=-q
for side in [-1,1]:
 pane=profile('Hatch side glazing',[(9.97,.94),(10.24,1.34),(11.34,1.35),(11.94,1.06),(11.92,.92)],.012,glass,.025);pane.location.y=side*.83
 box('Hatch window pillar',(10.94,side*.85,1.14),(.07,.018,.39),black,.008)
 box('Hatch handle',(10.82,side*.85,.83),(.12,.015,.025),black,.005)
 box('Hatch mirror',(10.12,side*.93,1.02),(.16,.15,.10),black,.035)
w=box('Hatch windshield',(9.93,0,1.12),(.025,1.46,.52),glass,.03);w.rotation_euler[1]=.62
w=box('Hatch backlight',(11.94,0,1.22),(.025,1.44,.52),glass,.03);w.rotation_euler[1]=.76
box('Hatch front bumper',(9.135,0,.46),(.09,1.58,.15),black,.025)
for y in [-.59,.59]:box('Hatch headlamp',(9.15,y,.73),(.025,.26,.12),white,.027)
# towbar connection: conceptual only, A-frame sufficient articulation
for y in [-.53,.53]:tube('Towbar ESTIMATE',[(8.05,0,.45),(8.34,0,.45),(9.15,y,.43)],.027,black)
for y in [-.14,.14]:tube('Tow safety cable ESTIMATE',[(8.12,y,.45),(8.55,y,.35),(9.13,y*.9,.44)],.008,chrome)
# Environment architectural ground, not exported
layer='environment';ground=mat('Warm grey studio ground',(.23,.24,.23),0,.75)
box('Ground',(4,0,-.05),(200,200,.1),ground,0)
# sun/sky, large-area fill, interior practical lights
layer='lighting'
def area(name,loc,power,size,color,target):
 d=bpy.data.lights.new(name,'AREA');d.energy=power;d.shape='DISK';d.size=size;d.color=color;o=bpy.data.objects.new(name,d);COL[layer].objects.link(o);o.location=loc;o.rotation_euler=(Vector(target)-o.location).to_track_quat('-Z','Y').to_euler();return o
area('Large studio key',(-2,-7,10),1800,8,(1,.90,.77),(4,0,1.5));area('Soft rear fill',(9,4,7),1100,6,(.77,.86,1),(4,0,1.5))
for x in [2.8,4.0,5.7,6.85]:area('Interior warm practical',(x,0,2.84),45,.55,(1,.67,.36),(x,0,1.0))
world=bpy.data.worlds.new('HDRI-style Nishita daylight');scene.world=world;world.use_nodes=True;wn=world.node_tree;wn.nodes.clear();out=wn.nodes.new('ShaderNodeOutputWorld');bg=wn.nodes.new('ShaderNodeBackground');sky=wn.nodes.new('ShaderNodeTexSky');sky.sky_type='MULTIPLE_SCATTERING';sky.sun_elevation=.42;sky.sun_rotation=2.15;sky.altitude=0;sky.air_density=1.1;sky.sun_size=.06;bg.inputs['Strength'].default_value=.18;wn.links.new(sky.outputs[0],bg.inputs[0]);wn.links.new(bg.outputs[0],out.inputs[0])
# camera helpers and exposure
layer='diagram'
def camera(name,loc,target,lens=45,ortho=None):
 d=bpy.data.cameras.new(name);o=bpy.data.objects.new(name,d);COL[layer].objects.link(o);o.location=loc;o.rotation_euler=(Vector(target)-o.location).to_track_quat('-Z','Y').to_euler();d.lens=lens;d.clip_start=.04;d.clip_end=300
 if ortho:d.type='ORTHO';d.ortho_scale=ortho
 return o
CAMS={
'01':camera('01 Exterior front 3 quarter',(-7.8,-10.6,6.0),(5.45,0,1.35),47),
'02':camera('02 Driver elevation',(4.01,15,1.78),(4.01,0,1.78),45,9.85),
'03':camera('03 Roof survey',(4.95,0,13),(4.95,0,0),45,7.60),
'04':camera('04 Tail underbody',(10.10,-2.65,.10),(7.34,-.08,.48),44),
'05':camera('05 Power cutaway',(12.0,-11.3,7.2),(4.85,0,1.42),47),
'06':camera('06 Interior cab to rear',(2.16,-.11,2.12),(6.65,.05,1.83),19),
'07':camera('07 Rear office',(5.75,-.66,2.18),(6.89,.83,1.71),31),
'08':camera('08 Laundry A',(4.74,-.90,1.83),(5.51,.74,1.36),29),
'09':camera('09 Laundry B',(5.57,.77,1.94),(6.61,-.75,1.41),29),
'10':camera('10 Floorplan',(4.94,0,13),(4.94,0,0),45,7.3),
'11':camera('11 Axle loads',(4.2,-15,1.6),(4.2,0,1.6),45,9.6),
'12':camera('12 Night exterior',(-6.9,-10.6,4.4),(5.3,0,1.46),44)}
scene.render.engine='CYCLES';scene.cycles.device='CPU';scene.cycles.samples=24;scene.cycles.use_denoising=True;scene.cycles.max_bounces=5;scene.cycles.diffuse_bounces=3;scene.cycles.glossy_bounces=3;scene.cycles.transparent_max_bounces=4
scene.render.resolution_x=1920;scene.render.resolution_y=1080;scene.render.resolution_percentage=100;scene.render.image_settings.file_format='PNG';scene.render.image_settings.color_mode='RGB';scene.render.film_transparent=False
scene.view_settings.view_transform='AgX';scene.view_settings.exposure=.0
scene.render.threads_mode='FIXED';scene.render.threads=4
# Store projected callout locations and complete geometry for reproducibility.
meta={'units':'metres','all_placements':'ESTIMATE','roof_centers':panelcenters,'ac_center':acx,'front_axle_x':.9652,'rear_axle_x':5.4864,'tail_cg_x':(202.8*7.18+30.86*7.727+55*7.42)/288.66,'tail_ground_clearance_m':.2589,'wheelbase_m':4.5212,'coach_length_m':7.9248,'coach_width_m':2.3114}
(R/'docs/model-geometry.json').write_text(json.dumps(meta,indent=2))
scene.camera=CAMS['01'];COL['laundry_A'].hide_render=True;COL['laundry_A'].hide_viewport=True
bpy.ops.wm.save_as_mainfile(filepath=str(R/'model/Alita-22NFT.blend'),compress=True)
# Export full model including both alternatives; keep collections as named empty parents.
for n,c in COL.items():
 if n in ['environment','lighting','diagram']:continue
 c.hide_viewport=False;c.hide_render=False
 e=bpy.data.objects.new('LAYER_'+n,None);c.objects.link(e)
 for o in list(c.objects):
  if o!=e:o.parent=e
bpy.ops.object.select_all(action='DESELECT')
for n,c in COL.items():
 if n not in ['environment','lighting','diagram']:
  for o in c.objects:o.select_set(True)
bpy.ops.export_scene.gltf(filepath=str(R/'model/Alita-22NFT.glb'),export_format='GLB',use_selection=True,export_cameras=False,export_lights=False,export_apply=True,export_yup=True)
# Updated blend with model parents and selected-layer default.
COL['laundry_A'].hide_render=True;COL['laundry_A'].hide_viewport=True
bpy.ops.wm.save_as_mainfile(filepath=str(R/'model/Alita-22NFT.blend'),compress=True)
print('BUILD_COMPLETE',len(bpy.data.objects),meta,flush=True)
