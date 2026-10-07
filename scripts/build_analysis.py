import json,math,pathlib
R=pathlib.Path(__file__).resolve().parents[1];wb=178;front=.9652;rear=5.4864
components=[
('B4810 pair',202.8,7.18,'tail / power'),('RV5 hub',30.86,7.727,'tail / power'),('Tail enclosure + mounts',40,7.42,'ESTIMATE'),('Tail cables / protection',15,7.42,'ESTIMATE'),
('Callsun six panels',393.9,sum([2.543032,3.334496,4.12596,5.692124,6.483588,7.275052])/6,'published mass, verify net'),('Roof mounting hardware',30,4.91,'ESTIMATE'),('Furrion 18K gross',77.16,4.909042,'removed factory A/C mass UNKNOWN'),('Starlink system + mount',12.98,4.909042,'mount 2 lb ESTIMATE'),('Orion pair',7.94,2.575,'selected model provisional'),('Other electrical / interior wiring',25,4.6,'ESTIMATE'),('Laundry A',148,5.51,'exclusive option A'),('Laundry B',148,6.61,'exclusive option B'),('Laundry support / lines',15,5.51,'ESTIMATE; B center 6.61 instead')]
rows=[]
for name,m,x,note in components:
 inch=(x-front)/.0254;dr=m*inch/wb;df=m-dr
 rows.append(dict(item=name,mass_lb=m,x_from_front_axle_in=round(inch,2),front_lb=round(df,2),rear_lb=round(dr,2),note=note))
tail=rows[:4];ta={k:round(sum(r[k] for r in tail),2) for k in ['mass_lb','front_lb','rear_lb']}
# Choose each laundry independently, never add both.
base=rows[:10]
totals={}
for op,x in [('A',5.51),('B',6.61)]:
 df=163*(rear-x)/(rear-front);dr=163-df
 totals[op]=dict(gross_addition_lb=round(sum(r['mass_lb'] for r in base)+163,2),front_lb=round(sum(r['front_lb'] for r in base)+df,2),rear_lb=round(sum(r['rear_lb'] for r in base)+dr,2),removed_mass='UNKNOWN: subtract removed stock A/C, replaced cabinets and existing solar after measurement')
base_loads=dict(editing_5h=0.70,fridge=0.8,cameras_laptop=0.4,lights=0.2,starlink_8h=.68,pumps_fans=.20)
energy={
'battery_nominal_kwh':10.24,'soc_operating_window':.8,'inverter_efficiency':.9,'usable_ac_kwh':7.3728,'base_daily_kwh':sum(base_loads.values()),'base_loads':base_loads,
'roof_solar_moderate_kwh':1.65*5.5*.75,'roof_solar_hot_kwh':1.65*6*.70,
'harvest_input_condition':'Full-nameplate harvest assumes an approved input arrangement accepts 1,650 W; the requested parallel connection is not yet verified.',
'parallel_single_input_ceiling_kw':50*21.29/1000,
'moderate':dict(hvac_avg_kw=.55,hours=8,total_kwh=sum(base_loads.values())+.55*8,solar_kwh=1.65*5.5*.75),
'hot_100F':dict(hvac_avg_kw=1.2,hours=24,total_kwh=sum(base_loads.values())+1.2*24,solar_kwh=1.65*6*.70),
'laundry_cycle_kwh_range':[2,4],'laundry_cycle_water_gal_range':[12,20],
'generator_ac_working_kw':3.2,'generator_energy_delivery_efficiency':.9,'generator_net_battery_recharge_kw':2.3,
'quiet_night':dict(moderate_8h_kwh=8*.55+.6,hot_8h_kwh=8*1.2+.6,hot_estimated_hours=(7.3728-.6)/1.2),
'NOTE':'ALL energy, water, climate and generator performance values are scenarios/ESTIMATES, not measured Furrion or Splendide duty cycles. No cooling-load calculation proves 18K capacity at 100F.'}
for s in ['moderate','hot_100F']:
 v=energy[s];v['daily_deficit_kwh']=v['total_kwh']-v['solar_kwh'];v['generator_hours_est']=max(0,v['daily_deficit_kwh'])/(3.2*.9)
analysis={'wheelbase_in':178,'tail':ta,'gross_totals':totals,'components':rows,'battery_only_old':{'mass_lb':202.8,'tail_lever_in':80,'front_lb':-202.8*80/178,'rear_lb':202.8*(1+80/178)},'departure':{'enclosure_ground_in':.2589/.0254,'rear_lever_in':(7.99785-rear)/.0254,'angle_deg':math.degrees(math.atan(.2589/(7.99785-rear)))},'solar':{'nameplate_w':1650,'imp_A':77.52,'isc_A':82.14,'bare_array_in':6*30.16,'array_with_5_gaps_in':6*30.16+5,'model_array_plus_ac_band_in':(7.275052+.383032-2.16)/.0254,'roof_estimate_in':220,'edge_to_panel_in':(91-68.35)/2},'energy':energy}
(R/'docs/analysis.json').write_text(json.dumps(analysis,indent=2))
(R/'docs/AXLE-AND-ENERGY.md').write_text('# Axle and energy scenarios\n\nAll longitudinal centers, mounting allowances and daily energy values are ESTIMATE. Actual empty and loaded scale tickets supersede this model.\n\nStatic point-mass formula: Δrear = m × x / 178; Δfront = m − Δrear. x is inches rearward of the front axle. Negative front values unload the steering axle. These are incremental loads, not remaining carrying capacity.\n\n| Component | Added lb | CG aft front axle, in | Δ front, lb | Δ rear, lb | Qualification |\n|---|---:|---:|---:|---:|---|\n'+'\n'.join(f'| {r["item"]} | {r["mass_lb"]:.2f} | {r["x_from_front_axle_in"]:.2f} | {r["front_lb"]:+.2f} | {r["rear_lb"]:+.2f} | {r["note"]} |' for r in rows)+'\n\nTail assembly: '+str(ta)+'\n\nGross additions by mutually exclusive laundry option: '+str(totals)+'\n\nEarlier +294 / −91 is reproduced by battery pair alone at ~80 in behind rear axle. It does not hold for the complete tail assembly.\n\n'+json.dumps(energy,indent=2))
print(json.dumps({'tail':ta,'totals':totals,'departure':analysis['departure'],'roof_band_in':analysis['solar']['model_array_plus_ac_band_in']},indent=2))
