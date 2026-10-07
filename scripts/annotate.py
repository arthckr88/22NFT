"""Pillow technical overlays: factual component sizes; placement/clearance labels explicitly ESTIMATE."""
from PIL import Image,ImageDraw,ImageFont
import pathlib,json,math
R=pathlib.Path(__file__).resolve().parents[1];W,H=1920,1080
font=R/'book/vendor/Jost.ttf';mono=R/'book/vendor/IBMPlexMono.ttf'
def F(n,m=False):return ImageFont.truetype(str(mono if m else font),n)
GOLD='#cdb96a';BONE='#f3f1ec';BG='#151918';MUTED='#b9bcb4';BLUE='#79b5d1';GREEN='#89b89b';CYAN='#78c7c9'
TITLES={'02':'DRIVER ELEVATION','03':'ROOF / PARALLEL SOLAR','04':'TAIL / PROTECTED POWER','05':'POWER / CONNECTION GATES','08':'LAUNDRY A / BATH SIDE','09':'LAUNDRY B / REAR GARAGE','10':'FLOORPLAN / PRESERVED WORKSPACE','11':'AXLE / INCREMENTAL LOADS'}

def annotate(v):
 im=Image.open(R/f'renders/{v}.png').convert('RGBA');overlay=Image.new('RGBA',im.size,(0,0,0,0));d=ImageDraw.Draw(overlay);A=json.loads((R/f'renders/{v}-anchors.json').read_text())
 d.rectangle((0,0,W,105),fill=(12,15,14,242));d.text((48,20),f'{v}   {TITLES[v]}',font=F(33),fill=BONE);d.text((48,68),'COMPONENT ENVELOPES: SOURCED  /  ALL POSITIONS, ROUTES & CLEARANCES: ESTIMATE',font=F(17,True),fill=GOLD)
 d.rectangle((0,H-63,W,H),fill=(12,15,14,242));d.text((48,H-45),'ANDREW ROSE   /   ALITA 22NFT   /   DESIGN VISUALIZATION — VERIFY AT WALKTHROUGH',font=F(17,True),fill=MUTED)
 def call(anchor,x,y,head,body,color=GOLD,width=385):
  p=A.get(anchor);lines=body.split('\n');h=58+len(lines)*24
  d.rounded_rectangle((x,y,x+width,y+h),radius=3,fill=(17,22,21,232),outline=color,width=1)
  d.text((x+15,y+9),head,font=F(23),fill=BONE)
  for i,line in enumerate(lines):d.text((x+15,y+43+i*24),line,font=F(17,True),fill=color)
  if p and 0<p[0]<W and 105<p[1]<H-65:
   start=(x+width/2,y+h/2);end=(p[0],p[1]);d.line((start,end),fill=color,width=2);d.ellipse((end[0]-5,end[1]-5,end[0]+5,end[1]+5),fill=color)
 def dim(p1,p2,text,offset=0,color=GOLD):
  x1,y1=p1;x2,y2=p2;y1+=offset;y2+=offset;d.line((x1,y1,x2,y2),fill=color,width=3)
  dx=x2-x1;dy=y2-y1;ln=max(1,math.hypot(dx,dy));nx=-dy/ln*10;ny=dx/ln*10
  for x,y in [(x1,y1),(x2,y2)]:d.line((x-nx,y-ny,x+nx,y+ny),fill=color,width=3)
  b=d.textbbox((0,0),text,font=F(21,True));tw=b[2];tx=(x1+x2)/2-tw/2;ty=(y1+y2)/2-33
  d.rectangle((tx-8,ty-3,tx+tw+8,ty+29),fill=(17,22,21,240));d.text((tx,ty),text,font=F(21,True),fill=BONE)
 if v=='02':
  dim(A['front'][:2],A['rear'][:2],'26 ft exterior / OEM 2027',940-A['front'][1])
  dim(A['front_axle'][:2],A['rear_axle'][:2],'178 in wheelbase / OEM',995-A['front_axle'][1])
  call('ac',610,125,'Height reference','11 ft 5 in OEM; modeled roof\npositions ESTIMATE',width=500)
 if v=='03':
  call('ac',55,133,'Ducted 18K heat pump','29.5 × 29 × 14.5 in\nService clearance UNVERIFIED')
  call('starlink',55,765,'Starlink Standard 4X','23.4 × 15.07 in footprint\nVariant / fixed mount ESTIMATE')
  call('vent',1455,133,'Existing vent band','Vent positions ESTIMATE\nNo relocation approved')
  call('combiner',1455,753,'Six panels / parallel','1,650 W · 77.52 A Imp\n82.14 A Isc · input conflict')
  dim(A['roof_start'][:2],A['roof_end'][:2],'216.46 in modeled array + A/C band',385)
  d.rounded_rectangle((650,120,1290,205),radius=3,fill=(17,22,21,235),outline=GOLD);d.text((674,131),'EACH PANEL 68.35 × 30.16 × 1.38 in',font=F(21,True),fill=BONE);d.text((674,164),'1 in modeled row gaps · 11.33 in side margins',font=F(17,True),fill=GOLD)
  d.text((596,970),'220 in usable roof is ESTIMATE; remaining length ≈3.54 in total.',font=F(19,True),fill=BG)
 if v=='04':
  call('battery',52,138,'2 × B4810 / 10.24 kWh','23.94 × 14.96 × 5.71 in each\n101.4 lb each · mounting pending')
  call('rv5',1450,138,'RV5 protected hub','17.72 × 19.69 × 6.30 in\n30.86 lb · dry cooling required')
  call('spare',1450,750,'Spare + service access','Factory position / carrier unknown\nRemoval path must remain usable')
  call('tailbottom',52,750,'45.5 × 37 × 9.5 in enclosure','10.2 in ground clearance ESTIMATE\n5.9° departure angle ESTIMATE')
  d.rounded_rectangle((585,729,1375,1005),radius=3,fill=(17,22,21,243),outline=GOLD)
  d.text((607,740),'SIDE SECTION / RIDE HEIGHT & FRAME ESTIMATE',font=F(18,True),fill=BONE)
  gx,gy=780,962;sc=4.2;tailx=gx+98.875984*sc;bot=gy-10.192913*sc;top=bot-9.5*sc
  d.line((620,gy,1346,gy),fill=MUTED,width=2)
  d.ellipse((gx-58,gy-116,gx+58,gy),outline=MUTED,width=2)
  d.line((660,top-19,tailx,top-19),fill=MUTED,width=8)
  d.rectangle((tailx-45.5*sc,top,tailx,bot),outline=BLUE,width=2)
  d.line((gx,gy,tailx,bot),fill=GOLD,width=2)
  d.line((tailx+18,bot,tailx+18,gy),fill=GOLD,width=2)
  for yy in [bot,gy]:d.line((tailx+8,yy,tailx+28,yy),fill=GOLD,width=2)
  d.text((tailx-178,top-32),'45.5 in enclosure',font=F(16,True),fill=BLUE)
  d.text((tailx+34,bot+8),'10.2 in',font=F(16,True),fill=GOLD)
  d.text((920,gy-30),'5.9° departure',font=F(17,True),fill=GOLD)
  d.text((603,790),'Lid/walls removed in main cutaway. Service & cooling\nclearances are not established.',font=F(16,True),fill=MUTED)
 if v=='05':
  call('combiner',52,137,'PV → combiner → RV5','≈5.9 m home run ESTIMATE\nSix parallel exceeds 50 A input',GOLD)
  call('orion',52,760,'Alternator → Orion ×2','12/48-8 provisional · 720 W\n≈2.2 m in / ≈5.6 m out',CYAN)
  call('rv5',1450,137,'RV5 ↔ 48 V batteries','≈0.7 m per battery ESTIMATE\nOrion/BMS tie pending approval',BLUE)
  call('generator',1450,752,'Generator AC / AGS','≈5.0 m AC run ESTIMATE\nStart interface + SOC gate open',GREEN)
  d.rounded_rectangle((605,874,1315,1000),radius=3,fill=(17,22,21,240),outline=GOLD);d.text((627,889),'SOLAR → HOUSE BATTERY → GENERATOR BACKUP',font=F(21),fill=BONE);d.text((627,924),'No stationary chassis engine auto-start.',font=F(18,True),fill=MUTED);d.text((627,953),'Colored runs are topology, not conductor sizing.',font=F(18,True),fill=MUTED)
 if v in ['08','09']:
  key='laundryA' if v=='08' else 'laundryB'
  call(key,52,132,'Splendide WDV2200XCD','23.5 W × 22.625 D × 33.375 H in\n148 lb · 120 V / 11 A',width=480)
  call(key,1350,132,'Service + door sweep','1 in front/back case minimum\n≈40.5 in open depth; measure',width=515)
  call(key,52,758,'Plumbing proposal','Hot/cold kitchen supply tees\nDedicated trap / air-break drain',width=480)
  call(key,1350,758,'Vent + support','4 in dedicated exterior metal vent\n≥280 lb floor support; anchor',width=515)
  d.rounded_rectangle((607,890,1313,994),radius=3,fill=(17,22,21,240),outline=GOLD);d.text((630,906),'DESK / DRAWERS PRESERVED · BED SHOWN RAISED',font=F(21),fill=BONE);d.text((630,948),'Loading aisle + bed-down swept volume UNVERIFIED',font=F(18,True),fill=GOLD)
 if v=='10':
  cx,cy=A['laundryA'][:2];hx=.5969/9.2*1920/2;hy=.574675/9.2*1920/2
  for x1,y1,x2,y2 in [(cx-hx,cy-hy,cx+hx,cy-hy),(cx-hx,cy+hy,cx+hx,cy+hy),(cx-hx,cy-hy,cx-hx,cy+hy),(cx+hx,cy-hy,cx+hx,cy+hy)]:
   length=math.hypot(x2-x1,y2-y1);n=max(1,int(length/14))
   for j in range(n):
    t=j/n;t2=min(1,t+.45/n);d.line((x1+(x2-x1)*t,y1+(y2-y1)*t,x1+(x2-x1)*t2,y1+(y2-y1)*t2),fill=GOLD,width=2)
  d.rectangle((cx-hx-5,cy-hy-28,cx-hx+172,cy-hy-3),fill=(17,22,21,242));d.text((cx-hx,cy-hy-25),'A / alternate bay',font=F(16,True),fill=GOLD)
  for key,x,y,head,body in [('couch',52,135,'Forward couch','Factory relationship retained'),('bath',52,325,'Dry bath','A bay adjacent; survey required'),('desk',52,730,'Rear editing desk','Desk + drawer pedestal retained'),('orion',52,530,'Orion-Tr Smart ×2','Forward dry bay / driving charge'),('kitchen',1450,135,'Kitchen + fridge','Factory relationship retained'),('generator',1450,280,'Generator connection','Existing unit / AC tie + AGS gate'),('laundryB',1450,440,'Laundry B shown','A is a mutually exclusive option'),('battery',1450,752,'Tail power below floor','Hub + packs beside spare')]:call(key,x,y,head,body)
  d.text((575,917),'ROOF: 6×275 W / 18K HP / Starlink / combiners',font=F(17,True),fill=BG)
  d.text((575,946),'BELOW: RV5 / B4810×2 / Orion×2 / existing generator',font=F(17,True),fill=BG)
  d.text((575,975),'Lift bed raised / omitted. Desk + drawers retained.',font=F(17,True),fill=BG)
 if v=='11':
  call('ac',565,137,'Roof component masses','Solar 393.9 lb* + mounts 30 lb EST\nHeat pump 77.16 gross / Starlink 12.98\n*Published mass basis needs net check',width=790)
  call('orion',595,753,'Forward charging / rear appliance','Orions 7.94 lb / laundry 148 lb\nSupport + plumbing 15 lb EST',width=730)
  a=json.loads((R/'docs/analysis.json').read_text());t=a['tail']
  call('front_axle',52,136,'Front axle / steering load',f'Tail assembly Δ {t["front_lb"]:+.1f} lb\nGAWR 4,630 lb; actual load unknown',width=460)
  call('rear_axle',1380,136,'Rear axle',f'Tail assembly Δ {t["rear_lb"]:+.1f} lb\nGAWR 7,275 lb; actual load unknown',width=485)
  call('battery',52,754,'Complete tail assembly','288.66 lb incl. hub + allowances\nCG ≈70.8 in behind rear axle',width=460)
  call('laundryB',1380,754,'Gross build / no removals','≈999 lb added; choose A OR B\nNet payload remains UNKNOWN',width=485)
  dim(A['front_axle'][:2],A['rear_axle'][:2],'178 in / Δrear = mass × CG distance ÷ wheelbase',100)
 out=Image.alpha_composite(im,overlay).convert('RGB');out.save(R/f'renders/{v}-annotated.png')
 return out
if __name__=='__main__':
 for v in TITLES:
  if (R/f'renders/{v}.png').exists():annotate(v)
 for p in (R/'renders').glob('*.png'):
  if 'preview' not in p.name:Image.open(p).convert('RGB').save(p.with_suffix('.jpg'),quality=93,optimize=True)
