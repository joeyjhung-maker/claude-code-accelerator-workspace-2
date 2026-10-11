"""Transcribe each VO chunk with Whisper and compare against the script, then (if --assemble) trim, speed, level and join -> ../vo.wav."""
import sys, json, re, subprocess, difflib
from pathlib import Path
import numpy as np
B = Path(__file__).resolve().parent; SR = 48000; TEMPO = 1.25; GAP = 0.22; HEAD = 0.08; TAIL = 1.2
CH = json.loads((B / 'chunks.json').read_text())
norm = lambda t: re.sub(r"[^a-z0-9' ]", ' ', t.lower().replace('-', ' ')).split()
from faster_whisper import WhisperModel
M = WhisperModel('medium.en', compute_type='int8')
bad = []
for c in CH:
    src = B / f"vo-c{c['n']:02d}.wav"
    pcm = np.frombuffer(subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', str(src), '-ac', '1', '-ar', '16000', '-f', 'f32le', '-'], capture_output=True).stdout, dtype=np.float32)
    segs, _ = M.transcribe(pcm, word_timestamps=True)
    heard = ' '.join(s.text for s in segs)
    a, b = norm(c['spoken']), norm(heard)
    sm = difflib.SequenceMatcher(None, a, b); ratio = sm.ratio()
    miss = [' '.join(a[i1:i2]) for tag, i1, i2, j1, j2 in sm.get_opcodes() if tag in ('delete', 'replace') and i2 - i1 >= 3]
    tail_ok = a[-3:] == b[-3:] or ' '.join(a[-2:]) in ' '.join(b[-6:])
    flag = '' if ratio > .93 and tail_ok and not miss else '  <-- CHECK'
    if flag: bad.append(c['n'])
    print(f"chunk {c['n']}: {len(pcm)/16000:.1f}s raw, match {ratio:.2f}, last words heard: '{' '.join(b[-5:])}'{flag}")
    for m in miss: print('     missing/changed:', m)
print('chunks to redo:', bad or 'none')
if '--assemble' in sys.argv and (not bad or '--force' in sys.argv):
    from scipy.io import wavfile
    parts = []
    for c in CH:
        src = B / f"vo-c{c['n']:02d}.wav"
        m = subprocess.run(['ffmpeg', '-hide_banner', '-i', str(src), '-af', 'ebur128', '-f', 'null', '-'], capture_output=True, text=True).stderr
        lufs = float(re.findall(r'I:\s+(-?[\d.]+) LUFS', m)[-1]); gain = -16 - lufs
        raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', str(src), '-af',
            f'silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.02,areverse,silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.04,areverse,atempo={TEMPO},volume={gain}dB',
            '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout
        x = np.frombuffer(raw, dtype=np.float32); parts.append(x); print(f"  c{c['n']}: {lufs} LUFS, gain {gain:+.1f} dB, {len(x)/SR:.2f}s")
    out = [np.zeros(int(HEAD * SR), np.float32)]
    for i, x in enumerate(parts):
        out.append(x); out.append(np.zeros(int((GAP if i < len(parts) - 1 else TAIL) * SR), np.float32))
    x = np.concatenate(out).copy(); TH, CEIL = .7, .89
    m = np.abs(x) > TH; x[m] = np.sign(x[m]) * (TH + (CEIL - TH) * np.tanh((np.abs(x[m]) - TH) / (CEIL - TH)))
    wavfile.write(B.parent / 'vo.wav', SR, (x * 32767).astype(np.int16)); print('vo.wav', round(len(x) / SR, 2), 's')
