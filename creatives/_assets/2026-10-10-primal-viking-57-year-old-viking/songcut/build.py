"""Song cut: storyboard frames (animated clips where they exist, stills otherwise) cut to the beat of the chosen song, with 2-3 word captions.
usage: <venv python> build.py <out.mp4>"""
import sys, json, re, subprocess, difflib, shutil
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont
B = Path(__file__).resolve().parent; A = B.parent; SB = A / 'storyboard'; C = A / 'clips'; W, H, FPS = 1080, 1920, 30
SONG = A / 'song' / 'song-FULL-A-sea-shanty-1-hookv2.mp3'; WORDS = A / 'song' / 'song-FULL-A-sea-shanty-1-hookv2-words.json'   # v4: Joey's new hook (take 2) spliced onto the original song at 28.85s
run = lambda c: subprocess.run(c, check=True)
FR = [
 ('01', "A 52-year-old Viking rowing for days through frigid open water,"), ('02', "hauling blood-crusted axes up jagged shoreline"), ('03', "could take out men half his age and conquer nations."),
 ('04', "But today, that same 52-year-old man needs ibuprofen to get out of bed."), ('05', "The difference? It’s not genetics. It was what they ate."),
 ('06', "And in the next 60 seconds, I’ll show you what ancient men ate every single day that modern men never touch…"),
 ('07', "Why your energy. Your drive. Your ability to stay lean. And your confidence in the bedroom, all quietly stopped at the same time."),
 ('08', "And how to get them back without prescriptions. Without injections. And without another useless supplement collecting dust on your counter."),
 ('09', "To answer this, we have to look at the life that body had to survive."), ('10', "That kind of body doesn’t run on chicken breast and multivitamins."),
 ('11', "Vikings ate the WHOLE animal, liver, heart and kidney. Nothing got thrown away. Because in the Arctic you don’t get to be picky. You eat what keeps you alive."),
 ('12', "And the animal they ate wasn’t a cow."), ('13', "It was the reindeer."), ('14', "Cattle stand in a field, get fed, barely move, and break down young."),
 ('15', "Reindeer run 5,000 km a season through minus-40 cold and never quit."), ('16', "Vikings ate the reindeer, packed with hard nutrients. You eat the cattle, deprived of all of them."),
 ('17', "Now look at what happened when men stopped eating this way. Organs disappeared from the diet completely."), ('18', "The human body didn’t change, but the food did."),
 ('19', "And here’s what most men try to do about it: They grab a single supplement and hope it kicks something back on."),
 ('20', "But you can’t restart a dead fire by throwing more wood on it."), ('21', "Reindeer organs don’t add wood, they rebuild the entire fire from the ground up."),
 ('22', "The liver gave that 52-year-old Viking iron and B vitamins that kept oxygen moving through his blood. So he could row from dawn until dark without fading."),
 ('23', "The heart, one of the richest sources on earth for carnitine, pulled stored fat into his cells and burned it as fuel. That’s how he stayed lean through an Arctic winter on almost nothing."),
 ('24', "The kidney sent zinc and selenium that supported blood flow. Which explains why half of Normandy had his jawline."),
 ('25', "The testicle gave him the cholesterol and androgenic peptides his body needed to keep making testosterone. That’s the reason he still WANTED to conquer and dominate at 52."),
 ('26', "And Rhodiola, the herb they gave on wedding nights,"), ('37', "made sure he could keep swinging hard on the field"), ('38', "and in the bedroom."),
 ('27', "Now obviously you’re not gonna gut a reindeer before breakfast, so we did it for you."),
 ('28', "That’s Primal Viking, freeze-dried reindeer liver, heart, and kidney, with beef testicle and Arctic herbs."),
 ('29', "The first thing you’ll notice is that 3pm wall starts easing up. The one where you’d normally reach for another coffee just to get through the afternoon."),
 ('30', "And once your energy stops crashing every day, you’ll actually want to train again. Not because you forced yourself, but because something switched back on."),
 ('31', "And that’s when the fat around your belly and chest that laughed at every diet you ever tried starts shifting."), ('32', "Your wife notices before you say a word."),
 ('33', "157,579 men have already made the switch."), ('34', "Take the free quiz. It builds a personalized routine in under two minutes, no email needed to see the result."),
 ('35', "And right now during the Fall Sale, you’ll unlock 60% off with a 30-day 100% money-back guarantee."),
 ('36', "The Vikings didn’t guess what their body needed. They just ate the animal that survived the worst conditions on earth. You can do the same thing with two capsules and a glass of water."),
 ('28', "Tap the button below to get started."),
]
dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(SONG)], capture_output=True, text=True).stdout)
# ---------- beat grid: fine tempo + phase by comb-scoring the onset envelope ----------
pcm = np.frombuffer(subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', str(SONG), '-ac', '1', '-ar', '22050', '-f', 'f32le', '-'], capture_output=True).stdout, dtype=np.float32)
hop = 256; n = len(pcm) // hop; env = np.sqrt(np.mean(pcm[:n * hop].reshape(n, hop) ** 2, axis=1)); on = np.maximum(np.diff(np.log1p(50 * env)), 0); efps = 22050 / hop
best = (-1, 0, 0)
for bpm in np.arange(117, 129, 0.02):
    bt = 60 / bpm
    for ph in np.linspace(0, bt, 24, endpoint=False):
        idx = (np.arange(ph, dur - 1, bt) * efps).astype(int); idx = idx[idx < len(on)]
        s = on[idx].mean()
        if s > best[0]: best = (s, bpm, ph)
_, BPM, PH = best; BEAT = 60 / BPM
beats = np.arange(PH, dur, BEAT)
snap = lambda t, div=1: PH + round((t - PH) / (BEAT / div)) * (BEAT / div)
# ---------- word timings: script tokens -> sung words ----------
RAW = json.loads(WORDS.read_text()); nz = lambda t: re.sub(r"[^a-z0-9]", '', t.lower())
toks = [{'t': t, 'f': fi} for fi, (_, line) in enumerate(FR) for t in line.split()]
a = [nz(t['t']) for t in toks]; b = [nz(w['w']) for w in RAW]; sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == 'equal':
        for k in range(i2 - i1): toks[i1 + k]['s'], toks[i1 + k]['e'] = RAW[j1 + k]['s'], RAW[j1 + k]['e']
    elif tag == 'replace' and j2 > j1:
        s0, e0 = RAW[j1]['s'], RAW[j2 - 1]['e']; m = i2 - i1
        for k in range(m): toks[i1 + k]['s'], toks[i1 + k]['e'] = s0 + (e0 - s0) * k / m, s0 + (e0 - s0) * (k + 1) / m
miss = [i for i, t in enumerate(toks) if 's' not in t]
for i in miss:
    p = next((toks[j]['e'] for j in range(i - 1, -1, -1) if 'e' in toks[j]), 0.0); q = next((toks[j]['s'] for j in range(i + 1, len(toks)) if 's' in toks[j]), dur)
    toks[i]['s'], toks[i]['e'] = p, min(q, p + .3)
runs = np.split(miss, np.where(np.diff(miss) != 1)[0] + 1) if miss else []
print(f'tempo {BPM:.2f} bpm | {len(toks)} script words, {len(RAW)} heard, {len(miss)} unmatched, longest run {max((len(r) for r in runs), default=0)}')
for i in range(1, len(toks)): toks[i]['s'] = max(toks[i]['s'], toks[i - 1]['s'] + 0.02)
# ---------- shots: each frame runs from its first word to the next frame's first word, snapped to the beat, then split every 4 beats ----------
fstart = [0.0] + [min(t['s'] for t in toks if t['f'] == fi) for fi in range(1, len(FR))]
fstart = [0.0] + [snap(x - 0.06, 2) for x in fstart[1:]]
for i in range(1, len(fstart)): fstart[i] = max(fstart[i], fstart[i - 1] + BEAT)
fstart.append(dur)
shots = []                                   # (frame index, start, end, variant)
for fi in range(len(FR)):
    s, e = fstart[fi], fstart[fi + 1]; cuts = [s]
    while e - cuts[-1] > 6 * BEAT: cuts.append(cuts[-1] + 4 * BEAT)
    if e - cuts[-1] > 4.6 * BEAT: cuts.append(cuts[-1] + round((e - cuts[-1]) / BEAT / 2) * BEAT)
    cuts.append(e)
    for k in range(len(cuts) - 1): shots.append((fi, cuts[k], cuts[k + 1], k))
L = np.array([e - s for _, s, e, _ in shots])
# ---------- picture ----------
seg = B / 'seg'; shutil.rmtree(seg, ignore_errors=True); seg.mkdir(); tmp = B / 'tmp'; shutil.rmtree(tmp, ignore_errors=True); tmp.mkdir(); lst = []
CROP = [(1.0, .5, .5), (1.30, .5, .36), (1.14, .5, .46), (1.42, .5, .34)]       # (zoom, centre x, centre y): wide, punch-in on the face, medium, tight
fitted = {}
def frame_n(t): return int(round(t * FPS))
for si, (fi, s, e, k) in enumerate(shots):
    fid = FR[fi][0]; nfr = max(frame_n(e) - frame_n(s), 1); out = seg / f's{si:03d}.mp4'; z, cx, cy = CROP[k % len(CROP)]
    clip = C / f'c{fid}.mp4'
    if clip.exists():
        key = (fi,)
        if key not in fitted:                 # stretch the clip over the frame's whole span once (slow up to 1.5x, then hold the last frame)
            span = fstart[fi + 1] - fstart[fi]; d = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(clip)], capture_output=True, text=True).stdout) - 0.1
            kf = min(max(span / d, 1.0), 1.5); f = tmp / f'fit{fi:02d}.mp4'
            run(['ffmpeg', '-y', '-loglevel', 'error', '-i', str(clip), '-an', '-vf', f"setpts={kf:.4f}*PTS,fps={FPS},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},tpad=stop_mode=clone:stop_duration=12,format=yuv420p",
                 '-t', f'{span + 0.2:.3f}', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '16', str(f)]); fitted[key] = f
        off = s - fstart[fi]; cw, chh = W / z, H / z; x0 = max(0, min(W - cw, cx * W - cw / 2)); y0 = max(0, min(H - chh, cy * H - chh / 2))
        run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', f'{off:.3f}', '-i', str(fitted[key]), '-vf', f"crop={cw:.0f}:{chh:.0f}:{x0:.0f}:{y0:.0f},scale={W}:{H},format=yuv420p",
             '-frames:v', str(nfr), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', str(out)])
    else:
        z1 = z + (0.07 if k % 2 == 0 else -0.05) if z > 1.05 else 1.09; z0 = z if z > 1.05 else 1.0
        zexp = f"{z0}+({z1}-{z0})*on/{nfr}"
        run(['ffmpeg', '-y', '-loglevel', 'error', '-i', str(SB / f'f{fid}.png'), '-vf',
             f"scale=2160:3840:force_original_aspect_ratio=increase,crop=2160:3840,zoompan=z='{zexp}':x='iw*{cx}-(iw/zoom/2)':y='ih*{cy}-(ih/zoom/2)':d={nfr}:s={W}x{H}:fps={FPS},format=yuv420p",
             '-frames:v', str(nfr), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', str(out)])
    lst.append(f"file 'seg/{out.name}'")
(B / 'seg.txt').write_text('\n'.join(lst))
# ---------- captions: 3-4 words at a time, one line, no word highlight. Size and position matched to the RYZE mummy ad
#            (cap height about 2.7% of frame height, centred about 63% down). Font: style 6 "Poster", picked by Joey 2026-10-11 ----------
def _face(path, want, size):
    for i in range(12):
        try: f = ImageFont.truetype(path, size, index=i)
        except Exception: break
        if all(w in ' '.join(f.getname()).lower() for w in want): return f
    return ImageFont.truetype(path, size)
PH_FONT = '/System/Library/Fonts/Supplemental/Phosphate.ttc'; size = 60
while True:                                     # grow the font until a capital H is about 51px tall (2.66% of 1920)
    FONT = _face(PH_FONT, ['solid'], size); bb = FONT.getbbox('H')
    if bb[3] - bb[1] >= 51 or size > 140: break
    size += 1
pages, cur = [], []
_w = lambda idx: FONT.getlength(' '.join(toks[j]['t'].upper().strip('…') for j in idx))
for i, t in enumerate(toks):
    if cur and _w(cur + [i]) > W - 130: pages.append(cur); cur = []          # every page must fit on ONE line
    cur.append(i); end = t['t'].rstrip('”"').endswith(('.', '…', '?', '!', ',', ':')); nxt = i + 1 < len(toks) and toks[i + 1]['f'] != t['f']
    if len(cur) >= 4 or (end and len(cur) >= 2) or (nxt and len(cur) >= 2) or t['t'].endswith(('.', '…', '?', '!')): pages.append(cur); cur = []
if cur: pages.append(cur)
CREAM, BROWN = (247, 236, 211, 255), (40, 22, 10, 255); CAP_H = 300; CAP_Y = 1217 - CAP_H // 2
cap = B / 'cap'; shutil.rmtree(cap, ignore_errors=True); cap.mkdir(); ct = ["ffconcat version 1.0"]; n = 0; widths = []
def draw(page):
    im = Image.new('RGBA', (W, CAP_H), (0, 0, 0, 0)); d = ImageDraw.Draw(im); words = [toks[i]['t'].upper().strip('…') for i in page]; rows, row = [], []
    for wd in words:
        if row and d.textlength(' '.join(row + [wd]), font=FONT) > W - 110: rows.append(row); row = []
        row.append(wd)
    rows.append(row); lh = int(size * 1.15); y = CAP_H // 2 - len(rows) * lh // 2 - bb[1] // 2
    for r in rows:
        line = ' '.join(r); tw = d.textlength(line, font=FONT); x = (W - tw) / 2; widths.append(tw / W)
        d.text((x + 5, y + 6), line, font=FONT, fill=(0, 0, 0, 150), stroke_width=7, stroke_fill=(0, 0, 0, 150))
        d.text((x, y), line, font=FONT, fill=CREAM, stroke_width=7, stroke_fill=BROWN); y += lh
    return im
for pi, page in enumerate(pages):
    s = 0.0 if pi == 0 else toks[page[0]]['s']; e = toks[pages[pi + 1][0]]['s'] if pi + 1 < len(pages) else dur
    f = cap / f'c{n:04d}.png'; draw(page).save(f); ct += [f"file 'cap/{f.name}'", f"duration {max(e - s, 0.05):.3f}"]; n += 1
ct.append(f"file 'cap/c{n - 1:04d}.png'"); (B / 'cap.txt').write_text('\n'.join(ct))
print(f'caption font size {size}, cap height {bb[3] - bb[1]}px, median line width {100 * float(np.median(widths)):.0f}% of frame, pages {len(pages)}')
# ---------- sound: the song is the whole soundtrack, mastered to -14 LUFS ----------
m = subprocess.run(['ffmpeg', '-hide_banner', '-i', str(SONG), '-af', 'ebur128', '-f', 'null', '-'], capture_output=True, text=True).stderr; lufs = float(re.findall(r'I:\s+(-?[\d.]+) LUFS', m)[-1])
run(['ffmpeg', '-y', '-loglevel', 'error', '-i', str(SONG), '-af', f"volume={-14 - lufs:.2f}dB,alimiter=limit=0.89:attack=5:release=60:level=false,afade=t=out:st={dur - 1.2:.2f}:d=1.2", '-ar', '48000', str(B / 'mix.wav')])
out = str(Path(sys.argv[1]).resolve())
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', 'seg.txt', '-f', 'concat', '-safe', '0', '-i', 'cap.txt', '-i', 'mix.wav', '-filter_complex',
                f'[1:v]fps=30,format=rgba[c];[0:v][c]overlay=0:{CAP_Y}:eof_action=repeat,format=yuv420p[v]', '-map', '[v]', '-map', '2:a', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '21', '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', out], check=True, cwd=B)
anim = sum(1 for fi, *_ in shots if (C / f'c{FR[fi][0]}.mp4').exists())
json.dump({'bpm': BPM, 'phase': PH, 'shots': [{'frame': FR[fi][0], 's': round(s, 2), 'len': round(e - s, 2)} for fi, s, e, k in shots], 'frame_starts': [round(x, 2) for x in fstart]}, open(B / 'timing.json', 'w'), indent=1)
print(f'shots {len(shots)} (animated {anim}, stills {len(shots) - anim}) | mean {L.mean():.2f}s median {np.median(L):.2f}s max {L.max():.2f}s | under 2s {100 * (L < 2).mean():.0f}% | caption pages {len(pages)} | song {lufs} LUFS')
