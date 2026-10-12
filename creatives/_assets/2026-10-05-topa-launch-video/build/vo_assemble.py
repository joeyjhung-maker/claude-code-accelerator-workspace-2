"""Trim, level (-16 LUFS static gain, peaks soft-limited to -1 dBFS) and speed each VO chunk, then join with short gaps -> ../vo.wav (48k mono)."""
import subprocess, re, sys
from pathlib import Path
import numpy as np
from scipy.io import wavfile
B = Path(__file__).resolve().parent; SR = 48000
TEMPO = 1.05; GAP = 0.26; HEAD = 0.10; TAIL = 1.9
parts = []
for src in sorted(B.glob('vo-c*.wav')):
    i = src.stem[-1]
    m = subprocess.run(['ffmpeg', '-hide_banner', '-i', str(src), '-af', 'ebur128', '-f', 'null', '-'], capture_output=True, text=True).stderr
    lufs = float(re.findall(r'I:\s+(-?[\d.]+) LUFS', m)[-1]); gain = -16 - lufs
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', str(src), '-af',
        f'silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.02,areverse,silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.04,areverse,atempo={TEMPO},volume={gain}dB',
        '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout
    a = np.frombuffer(raw, dtype=np.float32); parts.append(a); print(f'chunk {i}: {lufs} LUFS, gain {gain:+.1f} dB, {len(a)/SR:.2f}s', file=sys.stderr)
out = [np.zeros(int(HEAD * SR), np.float32)]
for i, a in enumerate(parts):
    out.append(a); out.append(np.zeros(int((GAP if i < len(parts) - 1 else TAIL) * SR), np.float32))
x = np.concatenate(out)
TH, CEIL = .7, .89                      # soft-knee the few peaks the +6 dB gain pushes over, instead of hard clipping
m = np.abs(x) > TH; x[m] = np.sign(x[m]) * (TH + (CEIL - TH) * np.tanh((np.abs(x[m]) - TH) / (CEIL - TH)))
wavfile.write(B.parent / 'vo.wav', SR, (x * 32767).astype(np.int16)); print('vo.wav', round(len(x) / SR, 2), 's')
