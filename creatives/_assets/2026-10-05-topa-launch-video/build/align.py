"""Whisper word times -> caption-token times. Captions (../captions.txt) are the source of truth for the words;
Whisper only supplies timing. Fails if too many caption words can't be matched. Writes ../timing.js + words.json."""
import sys, json, re, subprocess, difflib
from pathlib import Path
import numpy as np
B = Path(__file__).resolve().parent; A = B.parent
norm = lambda w: re.sub(r'[^a-z0-9]', '', w.lower())
if '--stt' in sys.argv or not (B / 'words-raw.json').exists():
    from faster_whisper import WhisperModel
    pcm = np.frombuffer(subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', str(A / 'vo.wav'), '-ac', '1', '-ar', '16000', '-f', 'f32le', '-'], capture_output=True).stdout, dtype=np.float32)
    segs, _ = WhisperModel('small.en', compute_type='int8').transcribe(pcm, word_timestamps=True)
    json.dump([{'w': w.word.strip(), 's': round(w.start, 3), 'e': round(w.end, 3)} for s in segs for w in s.words], open(B / 'words-raw.json', 'w'))
raw = [w for w in json.load(open(B / 'words-raw.json')) if norm(w['w'])]
lines, toks, sec = [], [], ''
for row in (A / 'captions.txt').read_text().splitlines():
    row = row.strip()
    if not row or row.startswith('#'): continue
    if row.startswith('['): sec = row.strip('[]'); continue
    li = len(lines); lines.append({'sec': sec, 'text': row.replace(' | ', ' '), 'words': []})
    for pi, page in enumerate(row.split(' | ')):
        for w in page.split():
            toks.append({'w': w, 'line': li, 'page': pi})
a = [norm(t['w']) for t in toks]; b = [norm(w['w']) for w in raw]
sm = difflib.SequenceMatcher(None, a, b, autojunk=False); hit = 0
for i, j, n in sm.get_matching_blocks():
    for k in range(n): toks[i + k]['s'], toks[i + k]['e'] = raw[j + k]['s'], raw[j + k]['e']; toks[i + k]['j'] = j + k; hit += 1
miss = [t['w'] for t in toks if 's' not in t]
print(f'{hit}/{len(toks)} caption words matched; interpolating: {miss}', file=sys.stderr)
if len(miss) > 0.12 * len(toks): sys.exit('too many unmatched caption words - check the VO against captions.txt')
run = best = 0
for tk in toks:
    run = 0 if 's' in tk else run + 1; best = max(best, run)
if best > 5: sys.exit(f'{best} caption words in a row have no audio - the voice-over dropped or garbled a line, re-voice that chunk')
i = 0
while i < len(toks):                      # spread unmatched runs across the gap between matched neighbours
    if 's' in toks[i]: i += 1; continue
    j = i
    while j < len(toks) and 's' not in toks[j]: j += 1
    t0 = toks[i - 1]['e'] if i else 0.0
    t1 = toks[j]['s'] if j < len(toks) else raw[-1]['e']
    j0 = toks[i - 1]['j'] + 1 if i else 0; j1 = toks[j]['j'] if j < len(toks) else len(raw)
    if j1 > j0: t0, t1 = raw[j0]['s'], raw[j1 - 1]['e']       # the real audio span of the unmatched words
    wts = [max(len(norm(t['w'])), 2) for t in toks[i:j]]; c = 0
    for t, wt in zip(toks[i:j], wts):
        t['s'] = round(t0 + (t1 - t0) * c / sum(wts), 3); c += wt; t['e'] = round(t0 + (t1 - t0) * c / sum(wts), 3)
    i = j
for t in toks: lines[t['line']]['words'].append({'w': t['w'], 's': t['s'], 'e': t['e'], 'p': t['page']})
for l in lines: l['s'], l['e'] = l['words'][0]['s'], l['words'][-1]['e']
dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(A / 'vo.wav')], capture_output=True, text=True).stdout)
(A / 'timing.js').write_text('window.TIMING=' + json.dumps({'dur': round(dur, 3), 'lines': lines}) + ';\n')
json.dump(lines, open(B / 'words.json', 'w'), indent=0)
for n, l in enumerate(lines): print(f"{n:2d} {l['s']:7.2f} {l['e']:7.2f}  [{l['sec']}] {l['text'][:70]}")
print('dur', dur)
