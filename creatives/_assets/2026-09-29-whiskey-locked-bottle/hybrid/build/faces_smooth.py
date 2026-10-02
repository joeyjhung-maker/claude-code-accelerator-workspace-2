"""faces.csv (25fps, Vision boxes, normalized) -> faces.js: per-output-frame (30fps) [cx, cy, h] in 1080x1920 px.
Smoothing never crosses a cut in Dan's original edit, so the Dan-cam bubble snaps with the cut instead of sliding."""
import csv, json
import numpy as np
CUTS = [3.64, 4.0, 4.88, 6.72, 7.72, 11.44, 18.44, 20.96, 22.08, 27.0, 31.28, 34.12, 37.2, 39.84, 46.04, 50.96, 59.72, 64.36, 65.96, 68.88, 71.52]
rows = list(csv.DictReader(open('faces.csv')))
t = np.array([float(r['t']) for r in rows])
ok = np.array([r['n'] != '0' for r in rows])
v = np.array([[float(r['x'] or 0) * 1080, float(r['y'] or 0) * 1920, float(r['h'] or 0) * 1920] for r in rows])
seg = np.searchsorted(CUTS, t + 1e-6)
out = np.zeros_like(v)
K = 4
for i in range(len(t)):
    m = (seg == seg[i]) & ok & (np.abs(np.arange(len(t)) - i) <= K)
    if m.any():
        out[i] = v[m].mean(0)
    else:  # nearest detected frame in the same segment, else anywhere
        c = np.nonzero((seg == seg[i]) & ok)[0]
        if not len(c): c = np.nonzero(ok)[0]
        out[i] = v[c[np.argmin(np.abs(c - i))]]
NF = 2267
res = []
for n in range(NF):
    i = min(len(t) - 1, int(round(n / 30 * 25)))
    res.append([round(float(x), 1) for x in out[i]])
open('faces.js', 'w').write('window.FACES=' + json.dumps(res, separators=(',', ':')) + ';\n')
print('frames', len(res))
