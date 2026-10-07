# Axle and energy scenarios

All longitudinal centers, mounting allowances and daily energy values are ESTIMATE. Actual empty and loaded scale tickets supersede this model.

Static point-mass formula: Δrear = m × x / 178; Δfront = m − Δrear. x is inches rearward of the front axle. Negative front values unload the steering axle. These are incremental loads, not remaining carrying capacity.

| Component | Added lb | CG aft front axle, in | Δ front, lb | Δ rear, lb | Qualification |
|---|---:|---:|---:|---:|---|
| B4810 pair | 202.80 | 244.68 | -75.97 | +278.77 | tail / power |
| RV5 hub | 30.86 | 266.21 | -15.29 | +46.15 | tail / power |
| Tail enclosure + mounts | 40.00 | 254.13 | -17.11 | +57.11 | ESTIMATE |
| Tail cables / protection | 15.00 | 254.13 | -6.42 | +21.42 | ESTIMATE |
| Callsun six panels | 393.90 | 155.27 | +50.30 | +343.60 | published mass, verify net |
| Roof mounting hardware | 30.00 | 155.31 | +3.82 | +26.18 | ESTIMATE |
| Furrion 18K gross | 77.16 | 155.27 | +9.85 | +67.31 | removed factory A/C mass UNKNOWN |
| Starlink system + mount | 12.98 | 155.27 | +1.66 | +11.32 | mount 2 lb ESTIMATE |
| Orion pair | 7.94 | 63.38 | +5.11 | +2.83 | selected model provisional |
| Other electrical / interior wiring | 25.00 | 143.10 | +4.90 | +20.10 | ESTIMATE |
| Laundry A | 148.00 | 178.93 | -0.77 | +148.77 | exclusive option A |
| Laundry B | 148.00 | 222.24 | -36.78 | +184.78 | exclusive option B |
| Laundry support / lines | 15.00 | 178.93 | -0.08 | +15.08 | ESTIMATE; B center 6.61 instead |

Tail assembly: {'mass_lb': 288.66, 'front_lb': -114.79, 'rear_lb': 403.45}

Gross additions by mutually exclusive laundry option: {'A': {'gross_addition_lb': 998.64, 'front_lb': -40.0, 'rear_lb': 1038.64, 'removed_mass': 'UNKNOWN: subtract removed stock A/C, replaced cabinets and existing solar after measurement'}, 'B': {'gross_addition_lb': 998.64, 'front_lb': -79.66, 'rear_lb': 1078.3, 'removed_mass': 'UNKNOWN: subtract removed stock A/C, replaced cabinets and existing solar after measurement'}}

Earlier +294 / −91 is reproduced by battery pair alone at ~80 in behind rear axle. It does not hold for the complete tail assembly.

{
  "battery_nominal_kwh": 10.24,
  "soc_operating_window": 0.8,
  "inverter_efficiency": 0.9,
  "usable_ac_kwh": 7.3728,
  "base_daily_kwh": 2.98,
  "base_loads": {
    "editing_5h": 0.7,
    "fridge": 0.8,
    "cameras_laptop": 0.4,
    "lights": 0.2,
    "starlink_8h": 0.68,
    "pumps_fans": 0.2
  },
  "roof_solar_moderate_kwh": 6.8062499999999995,
  "roof_solar_hot_kwh": 6.929999999999999,
  "harvest_input_condition": "Full-nameplate harvest assumes an approved input arrangement accepts 1,650 W; the requested parallel connection is not yet verified.",
  "parallel_single_input_ceiling_kw": 1.0645,
  "moderate": {
    "hvac_avg_kw": 0.55,
    "hours": 8,
    "total_kwh": 7.380000000000001,
    "solar_kwh": 6.8062499999999995,
    "daily_deficit_kwh": 0.5737500000000013,
    "generator_hours_est": 0.19921875000000044
  },
  "hot_100F": {
    "hvac_avg_kw": 1.2,
    "hours": 24,
    "total_kwh": 31.779999999999998,
    "solar_kwh": 6.929999999999999,
    "daily_deficit_kwh": 24.849999999999998,
    "generator_hours_est": 8.62847222222222
  },
  "laundry_cycle_kwh_range": [
    2,
    4
  ],
  "laundry_cycle_water_gal_range": [
    12,
    20
  ],
  "generator_ac_working_kw": 3.2,
  "generator_energy_delivery_efficiency": 0.9,
  "generator_net_battery_recharge_kw": 2.3,
  "quiet_night": {
    "moderate_8h_kwh": 5.0,
    "hot_8h_kwh": 10.2,
    "hot_estimated_hours": 5.644
  },
  "NOTE": "ALL energy, water, climate and generator performance values are scenarios/ESTIMATES, not measured Furrion or Splendide duty cycles. No cooling-load calculation proves 18K capacity at 100F."
}