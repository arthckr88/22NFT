"""Assemble the build book (book/index.html + img/ + model/) from renders and data."""
import html
import json
import os
import shutil
import sys

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from specs import SPECS, MASSES, X_REAR_AXLE, WHEELBASE  # noqa
from book_data import DECISIONS, COMPONENTS, LAUNDRY, WALKTHROUGH  # noqa

ROOT = os.path.dirname(HERE)
R = os.path.join(ROOT, 'renders')
B = os.path.join(ROOT, 'book')
os.makedirs(os.path.join(B, 'img'), exist_ok=True)
os.makedirs(os.path.join(B, 'model'), exist_ok=True)
AX = json.load(open(os.path.join(ROOT, 'docs', 'axles.json')))
E = html.escape

SHOTS = [
    ('01_exterior', 'Exterior', 'Three-quarter front, curbside. Abarth flat-towed behind.', None),
    ('02_elevation', 'Driver-side elevation', 'Dimensioned. Front to the left.', '02_elevation'),
    ('03_roof', 'Roof plan', 'Six panels, Chill Cube, Starlink Mini, vents, clearances.', '03_roof'),
    ('04_underbelly', 'Underbelly', 'Battery enclosure at the tail, from below and behind.', '04_underbelly'),
    ('04b_tail_section', 'Tail section', 'Ground clearance and departure angle.', '04b_tail_section'),
    ('05_xray', 'Power system', 'Ghosted coach, color-coded runs with approximate lengths.', '05_xray'),
    ('06_interior', 'Interior', 'From the cab looking to the rear office.', None),
    ('07_desk', 'Rear office', 'Desk at 29.5 in, kneehole open, RV5 in the pedestal.', None),
    ('08_laundry_A', 'Laundry A', 'Bath side, in place of the drawer stack.', '08_laundry_A'),
    ('09_laundry_B', 'Laundry B', 'Rear garage, curbside corner under the lift bed.', '09_laundry_B'),
    ('10_floorplan', 'Floorplan', 'Cut at 50 in. Both laundry options shown.', '10_floorplan'),
    ('11_axles', 'Weight on the chassis', 'Component masses and axle load shift.', '11_axles'),
    ('12_night', 'Night', 'Lights on, awning strip lit, Abarth attached.', None),
]


def jpg(src, dst, q=84, w=1920):
    im = Image.open(src).convert('RGB')
    if im.size[0] > w:
        im = im.resize((w, int(im.size[1] * w / im.size[0])), Image.LANCZOS)
    im.save(dst, quality=q, optimize=True, progressive=True)
    tw = 720
    im.resize((tw, int(im.size[1] * tw / im.size[0])), Image.LANCZOS).save(dst.replace('.jpg', '_t.jpg'), quality=80)


def status_pill(s):
    t = {'C': 'Confirmed', 'R': 'Credible', 'E': 'Estimate'}[s]
    return '<span class="pill pill-%s">%s</span>' % (s.lower(), t)


def main():
    have = []
    for key, title, cap, ann in SHOTS:
        src = os.path.join(R, key + '.png')
        if not os.path.exists(src):
            print('missing render', key)
            continue
        jpg(src, os.path.join(B, 'img', key + '.jpg'))
        a = None
        if ann and os.path.exists(os.path.join(R, 'annotated', ann + '.jpg')):
            jpg(os.path.join(R, 'annotated', ann + '.jpg'), os.path.join(B, 'img', key + '_ann.jpg'))
            a = 'img/%s_ann.jpg' % key
        have.append((key, title, cap, a))
    shutil.copy(os.path.join(ROOT, 'model', '22nft.gltf.json'), os.path.join(B, 'model', '22nft.gltf.json'))

    runs = json.load(open(os.path.join(R, '05_xray.json')))['runs_in'] if os.path.exists(os.path.join(R, '05_xray.json')) else {}

    tiles = []
    for i, (key, title, cap, a) in enumerate(have):
        tiles.append(
            '<figure class="tile"><button class="tile-btn" type="button" data-i="%d" aria-label="Open %s">'
            '<img src="img/%s_t.jpg" alt="%s" loading="lazy" width="720" height="405"></button>'
            '<figcaption><span class="mono">%s%s</span><span class="cap">%s</span></figcaption></figure>'
            % (i, E(title), key, E(title + '. ' + cap), E(key.split('_')[0]), ' / ANNOTATED' if a else '', E(title)))
    shots_js = json.dumps([dict(src='img/%s.jpg' % k, ann=a, title=t, cap=c, idx=k.split('_')[0]) for k, t, c, a in have])

    spec_rows = ''.join('<tr><td>%s</td><td>%s</td><td>%s</td><td class="src">%s</td></tr>' % (
        E(i), E(v), status_pill(s), ('<a href="%s" target="_blank" rel="noopener">%s</a>' % (E(src), E(src.split('/')[2])) if src.startswith('http') else E(src)))
        for i, v, src, s in SPECS)

    comp = ''.join(
        '<article class="comp"><h3>%s</h3><dl>%s</dl></article>' % (
            E(c['name']), ''.join('<div><dt>%s</dt><dd>%s</dd></div>' % (E(k), E(c[f])) for k, f in (
                ('Location', 'where'), ('Why there', 'why'), ('Dimensions', 'dims'), ('Clearances', 'clear'),
                ('Weight', 'weight'), ('Service access', 'service'), ('Risks', 'risk'))))
        for c in COMPONENTS)

    laundry = ''.join('<tr><th scope="row">%s</th><td>%s</td><td>%s</td></tr>' % (E(a), E(b), E(c)) for a, b, c in LAUNDRY)

    def axrows(rows):
        return ''.join('<tr><td>%s</td><td class="n">%.0f</td><td class="n">%.0f</td><td class="n">%+.0f</td><td class="n">%+.0f</td></tr>' % (
            E(r['item']), r['lb'], r['x'], r['front'], r['rear']) for r in rows)
    ta, tb = AX['total_A'], AX['total_B']
    rc = AX['recheck']

    run_rows = ''
    if runs:
        pv = sum(v for k, v in runs.items() if k.startswith('PV_panel'))
        items = [('Panel leads to combiner (6)', pv, 'pv')] + [(k, v, ('pv' if k.startswith('PV') else 'dc' if k.startswith('48V, RV5') else 'alt' if ('Orion' in k) else 'ac')) for k, v in runs.items() if not k.startswith('PV_panel')]
        run_rows = ''.join('<tr><td><span class="swatch sw-%s" aria-hidden="true"></span>%s</td><td class="n">%.0f ft</td></tr>' % (c, E(k), v / 12) for k, v, c in items)

    dec = ''.join('<div class="dec"><dt>%s</dt><dd>%s</dd></div>' % (E(a), E(b)) for a, b in DECISIONS)
    tier = {1: 'Measure first', 2: 'Measure', 3: 'Check'}
    walk = ''.join('<li class="walk t%d"><span class="pill pill-w%d">%s</span><div><strong>%s</strong><p>%s</p></div></li>' % (
        t, t, tier[t], E(a), E(b)) for a, b, t in WALKTHROUGH)

    page = TEMPLATE
    for k, v in dict(TILES=''.join(tiles), SHOTS_JS=shots_js, SPEC_ROWS=spec_rows, COMPONENTS=comp, LAUNDRY=laundry,
                     AXROWS_A=axrows(AX['rows_A']), AXROWS_B=axrows(AX['rows_B']),
                     TA_LB='%.0f' % ta['lb'], TA_F='%+.0f' % ta['front'], TA_R='%+.0f' % ta['rear'],
                     TB_F='%+.0f' % tb['front'], TB_R='%+.0f' % tb['rear'],
                     RC_EF='%+.0f' % rc['earlier']['front'], RC_ER='%+.0f' % rc['earlier']['rear'],
                     RC_MF='%+.0f' % rc['modelled']['front'], RC_MR='%+.0f' % rc['modelled']['rear'],
                     RUN_ROWS=run_rows, DECISIONS=dec, WALK=walk).items():
        page = page.replace('{{%s}}' % k, v)
    open(os.path.join(B, 'index.html'), 'w').write(page)
    print('book written', len(page) // 1024, 'KB,', len(have), 'renders')


TEMPLATE = open(os.path.join(HERE, 'book_template.html')).read()

if __name__ == '__main__':
    main()


def write_markdown():
    """Plain-text companion for the repo: docs/BUILD_BOOK.md"""
    L = ['# Alita 22NFT build book, model R1', '',
         'Renders in `renders/`, annotated views in `renders/annotated/`, model in `model/`.', '',
         '## Specs', '', '| Item | Value | Status | Source |', '| --- | --- | --- | --- |']
    st = {'C': 'Confirmed', 'R': 'Credible', 'E': 'ESTIMATE'}
    L += ['| %s | %s | %s | %s |' % (i, v, st[s], src) for i, v, src, s in SPECS]
    L += ['', '## Components', '']
    for c in COMPONENTS:
        L += ['### ' + c['name'], ''] + ['- **%s:** %s' % (k, c[f]) for k, f in (
            ('Location', 'where'), ('Why there', 'why'), ('Dimensions', 'dims'), ('Clearances', 'clear'),
            ('Weight', 'weight'), ('Service access', 'service'), ('Risks', 'risk'))] + ['']
    L += ['## Laundry A vs B', '', '| | A, bath side | B, rear garage |', '| --- | --- | --- |']
    L += ['| %s | %s | %s |' % r for r in LAUNDRY]
    L += ['', '## Axle math', '', 'Front share = weight x (x - 94) / 178, x in inches from the rear wall.', '',
          '| Item | lb | x in | Front | Rear |', '| --- | --- | --- | --- | --- |']
    L += ['| %s | %.0f | %.0f | %+.0f | %+.0f |' % (r['item'], r['lb'], r['x'], r['front'], r['rear']) for r in AX['rows_A']]
    ta, tb, rc = AX['total_A'], AX['total_B'], AX['recheck']
    L += ['| **Total (A)** | %.0f | | %+.0f | %+.0f |' % (ta['lb'], ta['front'], ta['rear']), '',
          'With laundry B: front %+.0f lb, rear %+.0f lb.' % (tb['front'], tb['rear']), '',
          'Recheck of the earlier figure: 203 lb at 80 in behind the axle gives %+.0f rear / %+.0f front (holds as arithmetic). '
          'The modelled box sits 64 in behind the axle: %+.0f rear / %+.0f front.' % (
              rc['earlier']['rear'], rc['earlier']['front'], rc['modelled']['rear'], rc['modelled']['front']), '',
          '## Decisions', '']
    L += ['- **%s:** %s' % d for d in DECISIONS]
    L += ['', '## Verify at walkthrough', '']
    tier = {1: 'Measure first', 2: 'Measure', 3: 'Check'}
    L += ['- [ ] **%s** (%s): %s' % (a, tier[t], b) for a, b, t in WALKTHROUGH]
    open(os.path.join(ROOT, 'docs', 'BUILD_BOOK.md'), 'w').write('\n'.join(L) + '\n')


if __name__ == '__main__':
    write_markdown()
