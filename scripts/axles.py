"""Axle load shift for the build. Writes docs/axles.json."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from specs import MASSES, WASHER, WASHER_X, axle_split, X_REAR_AXLE, WHEELBASE

out = {"rows": [], "wheelbase": WHEELBASE, "x_rear_axle": X_REAR_AXLE}
for opt in ("A", "B"):
    rows = []
    for name, w, x in MASSES + [(WASHER[0] + " (" + opt + ")", WASHER[1], WASHER_X[opt])]:
        f, r = axle_split(w, x)
        rows.append(dict(item=name, lb=w, x=x, d_from_rear_axle=round(x - X_REAR_AXLE, 1), front=round(f, 1), rear=round(r, 1)))
    tf = sum(r["front"] for r in rows); tr = sum(r["rear"] for r in rows)
    out["rows_" + opt] = rows
    out["total_" + opt] = dict(lb=round(sum(r["lb"] for r in rows), 1), front=round(tf, 1), rear=round(tr, 1))
# recheck of the earlier thread figure: 203 lb at 80 in behind the rear axle
f80, r80 = axle_split(203, X_REAR_AXLE - 80)
f64, r64 = axle_split(203, X_REAR_AXLE - 64)
out["recheck"] = dict(earlier=dict(d=80, front=round(f80, 1), rear=round(r80, 1)),
                      modelled=dict(d=64, front=round(f64, 1), rear=round(r64, 1)))
p = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "axles.json")
json.dump(out, open(p, "w"), indent=1)
print(json.dumps(out["total_A"]), json.dumps(out["total_B"]), json.dumps(out["recheck"]))
