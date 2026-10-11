"""Transcribe each full song and compare with the lyrics sent. Sung vocals transcribe less reliably than speech, so treat the match as a guide."""
import sys, json, re, subprocess, difflib
from pathlib import Path
import numpy as np
from faster_whisper import WhisperModel
B = Path(__file__).resolve().parent
norm = lambda t: re.sub(r"[^a-z0-9' ]", ' ', t.lower().replace('-', ' ')).split()
lyr = re.sub(r'\[.*?\]', ' ', (B / 'tab2-lyrics.txt').read_text()); a = norm(lyr)
M = WhisperModel('medium.en', compute_type='int8'); res = {}
for f in sorted(B.glob('song-FULL-*.mp3')):
    pcm = np.frombuffer(subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', str(f), '-ac', '1', '-ar', '16000', '-f', 'f32le', '-'], capture_output=True).stdout, dtype=np.float32)
    segs, _ = M.transcribe(pcm, word_timestamps=True, vad_filter=False); words = [w for s in segs for w in s.words]
    b = norm(' '.join(w.word for w in words)); sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    miss = [' '.join(a[i1:i2]) for tag, i1, i2, j1, j2 in sm.get_opcodes() if tag in ('delete', 'replace') and i2 - i1 >= 5]
    extra = [' '.join(b[j1:j2]) for tag, i1, i2, j1, j2 in sm.get_opcodes() if tag == 'insert' and j2 - j1 >= 5]
    p2 = np.frombuffer(subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', str(f), '-ac', '1', '-ar', '22050', '-f', 'f32le', '-'], capture_output=True).stdout, dtype=np.float32)
    hop = 512; n = len(p2) // hop; env = np.sqrt(np.mean(p2[:n * hop].reshape(n, hop) ** 2, axis=1)); on = np.maximum(np.diff(np.log1p(50 * env)), 0); on -= on.mean()
    ac = np.correlate(on, on, 'full')[len(on) - 1:]; fps = 22050 / hop; lags = np.arange(len(ac)); bpm = np.where(lags > 0, 60 * fps / np.maximum(lags, 1), 0); m = (bpm >= 70) & (bpm <= 180)
    tempo = 60 * fps / lags[m][np.argmax(ac[m])]; dur = len(pcm) / 16000
    covered = sum(i2 - i1 for tag, i1, i2, j1, j2 in sm.get_opcodes() if tag == 'equal') / len(a)
    res[f.name] = {'dur': round(dur, 1), 'tempo': round(float(tempo), 1), 'heard_words': len(b), 'script_words': len(a), 'script_covered_pct': round(covered * 100),
                   'first_word': round(words[0].start, 1) if words else None, 'last_word': round(words[-1].end, 1) if words else None,
                   'last_heard': ' '.join(b[-6:]), 'missing_runs': len(miss), 'missing_words': sum(len(x.split()) for x in miss), 'extra_runs': len(extra), 'missing': [x[:70] for x in miss[:8]], 'extra': [x[:60] for x in extra[:4]]}
    json.dump([{'w': w.word.strip(), 's': round(w.start, 3), 'e': round(w.end, 3)} for w in words], open(B / (f.stem + '-words.json'), 'w'))
    print(f.name, json.dumps(res[f.name], indent=0)[:1100], flush=True)
json.dump(res, open(B / 'song-check.json', 'w'), indent=1)
