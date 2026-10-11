"""Animatic: storyboard stills cut to vo.wav with word-highlight captions and the music bed. usage: <venv python> build.py [--stt]"""
import sys, json, re, subprocess, difflib, shutil
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont
B = Path(__file__).resolve().parent; A = B.parent; SB = A / 'storyboard'; W, H, FPS = 1080, 1920, 30
run = lambda c, **k: subprocess.run(c, check=True, **k)
# ---- storyboard frames + their voice-over text (single source: storyboard/build_board.py) ----
src = (SB / 'build_board.py').read_text(); ns = {}
exec(src[src.index('S=['):src.index('def b64')], ns)
FR = [(i, line) for _, frames in ns['S'] for i, line, _ in frames]
# ---- word timings from the master audio ----
dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(A / 'vo.wav')], capture_output=True, text=True).stdout)
if '--stt' in sys.argv or not (B / 'words-raw.json').exists():
    from faster_whisper import WhisperModel
    pcm = np.frombuffer(subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', str(A / 'vo.wav'), '-ac', '1', '-ar', '16000', '-f', 'f32le', '-'], capture_output=True).stdout, dtype=np.float32)
    segs, _ = WhisperModel('medium.en', compute_type='int8').transcribe(pcm, word_timestamps=True)
    (B / 'words-raw.json').write_text(json.dumps([{'w': w.word.strip(), 's': round(w.start, 3), 'e': round(w.end, 3)} for s in segs for w in s.words]))
RAW = json.loads((B / 'words-raw.json').read_text())
nz = lambda t: re.sub(r"[^a-z0-9]", '', t.lower().replace('’', "'"))
NUM = {'52yearold': ['52', 'year', 'old'], '60': ['60'], '5000': ['5000'], 'minus40': ['minus', '40'], '3pm': ['3', 'pm'], '157579': ['157579'], '60%': ['60'], '30day': ['30', 'day'], '100%': ['100']}
toks = []                                   # display tokens, in order, tagged with their storyboard frame
for fi, (fid, line) in enumerate(FR):
    for t in line.split(): toks.append({'t': t, 'f': fi})
a = [nz(t['t']) for t in toks]; b = [nz(w['w']) for w in RAW]
sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == 'equal':
        for k in range(i2 - i1): toks[i1 + k]['s'], toks[i1 + k]['e'] = RAW[j1 + k]['s'], RAW[j1 + k]['e']
    elif tag == 'replace' and j2 > j1:      # e.g. "52-year-old" vs "52 year old": spread the heard span over the script tokens
        s0, e0 = RAW[j1]['s'], RAW[j2 - 1]['e']; n = i2 - i1
        for k in range(n): toks[i1 + k]['s'], toks[i1 + k]['e'] = s0 + (e0 - s0) * k / n, s0 + (e0 - s0) * (k + 1) / n
miss = [i for i, t in enumerate(toks) if 's' not in t]
for i in miss:                              # anything unheard: sit between its neighbours
    p = next((toks[j]['e'] for j in range(i - 1, -1, -1) if 'e' in toks[j]), 0.0); q = next((toks[j]['s'] for j in range(i + 1, len(toks)) if 's' in toks[j]), dur)
    toks[i]['s'], toks[i]['e'] = p, min(q, p + .25)
run_miss = max((len(list(g)) for g in np.split(miss, np.where(np.diff(miss) != 1)[0] + 1)), default=0) if miss else 0
print(f'{len(toks)} script words, {len(RAW)} heard, {len(miss)} unmatched (longest run {run_miss})')
assert run_miss < 6, 'captions and audio have drifted apart'
# ---- caption pages: 4-5 words, break on punctuation ----
pages, cur = [], []
for i, t in enumerate(toks):
    cur.append(i); end = t['t'].rstrip('”"').endswith(('.', '…', '?', '!', ','))
    nxt_frame = i + 1 < len(toks) and toks[i + 1]['f'] != t['f']
    if len(cur) >= 5 or (end and len(cur) >= 3) or (nxt_frame and len(cur) >= 2) or t['t'].endswith(('.', '…')): pages.append(cur); cur = []
if cur: pages.append(cur)
FONT = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Black.ttf', 74)
cap = B / 'cap'; shutil.rmtree(cap, ignore_errors=True); cap.mkdir()
lines_txt = ["ffconcat version 1.0"]; t_prev = 0.0; n = 0
def draw(page, hi):
    im = Image.new('RGBA', (W, 520), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    words = [toks[i]['t'].upper() for i in page]; rows, row = [], []
    for wd in words:
        if row and d.textlength(' '.join(row + [wd]), font=FONT) > W - 140: rows.append(row); row = []
        row.append(wd)
    rows.append(row); y = 260 - len(rows) * 50; k = 0
    for r in rows:
        x = (W - d.textlength(' '.join(r), font=FONT)) / 2
        for wd in r:
            d.text((x, y), wd, font=FONT, fill=(255, 214, 10, 255) if k == hi else (255, 255, 255, 255), stroke_width=9, stroke_fill=(0, 0, 0, 255))
            x += d.textlength(wd + ' ', font=FONT); k += 1
        y += 100
    return im
for pi, page in enumerate(pages):
    for k, i in enumerate(page):
        s = 0.0 if n == 0 else toks[i]['s']                      # first caption is on screen from frame 0
        e = toks[page[k + 1]]['s'] if k + 1 < len(page) else (toks[pages[pi + 1][0]]['s'] if pi + 1 < len(pages) else dur)
        f = cap / f'c{n:04d}.png'; draw(page, k).save(f)
        lines_txt += [f"file 'cap/{f.name}'", f"duration {max(e - s, 0.04):.3f}"]; n += 1
lines_txt.append(f"file 'cap/c{n - 1:04d}.png'")
(B / 'cap.txt').write_text('\n'.join(lines_txt))
# ---- picture: each still held for its lines, slow push in or out ----
starts = [0.0] + [next(t['s'] for t in toks if t['f'] == fi) for fi in range(1, len(FR))] + [dur]
seg = B / 'seg'; shutil.rmtree(seg, ignore_errors=True); seg.mkdir(); cl = []
for fi, (fid, _) in enumerate(FR):
    d = starts[fi + 1] - starts[fi]; nfr = max(int(round(starts[fi + 1] * FPS)) - int(round(starts[fi] * FPS)), 1)
    z = f"zoom='1+0.10*on/{nfr}'" if fi % 2 == 0 else f"zoom='1.10-0.10*on/{nfr}'"
    out = seg / f's{fi:02d}.mp4'
    run(['ffmpeg', '-y', '-loglevel', 'error', '-i', str(SB / f'f{fid}.png'), '-vf',
         f"scale=2160:3840:force_original_aspect_ratio=increase,crop=2160:3840,zoompan={z}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={nfr}:s={W}x{H}:fps={FPS},format=yuv420p",
         '-frames:v', str(nfr), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', str(out)])
    cl.append(f"file 'seg/{out.name}'")
(B / 'seg.txt').write_text('\n'.join(cl))
(B / 'timing.json').write_text(json.dumps({'frames': [{'frame': fid, 'start': round(starts[i], 2), 'len': round(starts[i + 1] - starts[i], 2)} for i, (fid, _) in enumerate(FR)], 'pages': len(pages), 'dur': dur}, indent=1))
print('frames', len(FR), '| caption pages', len(pages), '| caption states', n, '| dur', round(dur, 2))
print('longest holds:', sorted([(round(starts[i + 1] - starts[i], 1), FR[i][0]) for i in range(len(FR))], reverse=True)[:8])
