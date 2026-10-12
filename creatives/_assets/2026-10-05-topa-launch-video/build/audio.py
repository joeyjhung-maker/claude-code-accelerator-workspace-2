"""Sound for the Topa launch video: SFX stem (from the cue list the page registers) + a soft synth music bed.
usage: python audio.py   -> writes sfx.wav + music.wav next to this file. Balance happens in build.sh
(VO -16 LUFS, SFX about 9 LU under, music about 14 LU under, master -14)."""
import json, sys
import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt
from pathlib import Path
import sfx as S

B = Path(__file__).resolve().parent; SR = 48000
data = json.load(open(B / 'cues.json')); DUR = data['dur']; N = int(DUR * SR)
tt = lambda d: np.arange(int(SR * d)) / SR
lp = lambda x, f: sosfilt(butter(2, f, 'lowpass', fs=SR, output='sos'), x, axis=0)
hp = lambda x, f: sosfilt(butter(2, f, 'highpass', fs=SR, output='sos'), x, axis=0)


def ring(**_):                       # soft double phone ring
    t = tt(1.0); b = (np.sin(2 * np.pi * 400 * t) + np.sin(2 * np.pi * 450 * t)) * .5
    gate = ((t < .4) | ((t > .6) & (t < 1.0))).astype(float)
    return S.stereo(S.norm(lp(b * gate, 2500) * np.minimum(1, t / .01)))
def buzz(**_):                       # short low error buzz
    t = tt(.28); y = np.sign(np.sin(2 * np.pi * 105 * t)) * np.exp(-t / .2)
    return S.stereo(S.norm(lp(y, 900)))
CUSTOM = {'ring': ring, 'buzz': buzz}

# ---------- SFX stem ----------
sfx = np.zeros((N, 2)); last = {}; kept = 0
for i, c in enumerate(data['cues']):
    if c['t'] - last.get(c['name'], -9) < .26: continue      # thin rapid bursts: one sound per flurry, not a machine gun
    last[c['name']] = c['t']; kept += 1
    fn = CUSTOM.get(c['name']) or getattr(S, c['name'])
    kw = {k: v for k, v in c.items() if k not in ('t', 'name', 'gain')}; kw.setdefault('seed', i)
    a = fn(**kw); o = int(c['t'] * SR)
    if o < 0 or o >= N: continue
    a = a[:N - o] * 10 ** (c['gain'] / 20); sfx[o:o + len(a)] += a
wavfile.write(B / 'sfx.wav', SR, (np.clip(sfx, -1, 1) * 32767).astype(np.int16))

# ---------- music bed (C major, 100 bpm) ----------
SEC = data.get('sections') or {}
BEAT = .6; BAR = 4 * BEAT
t0 = SEC.get('logo', 34.5) % BAR - BAR            # a downbeat lands on the logo hit
CH = [[130.81, 164.81, 196.00, 246.94], [110.00, 130.81, 164.81, 196.00], [87.31, 130.81, 174.61, 220.00], [98.00, 146.83, 196.00, 246.94]]  # Cmaj7 Am7 Fmaj7 G
env = lambda pts: np.interp(np.arange(N) / SR, [p[0] for p in pts], [p[1] for p in pts])
s2, s3, s4, s5, s6, s7, s8, s9 = (SEC.get(k, v) for k, v in [('s2', 5.8), ('s3', 14.2), ('s4', 33.1), ('s5', 49.2), ('s6', 59.4), ('s7', 94.3), ('s8', 116.7), ('s9', 132.2)])
lg = SEC.get('logo', 34.5); end = SEC.get('end', DUR - 2)
pad_e = env([(0, .0), (1.2, .8), (s3, .8), (s3 + 1, .6), (lg - .3, .55), (lg, 1), (s7, 1), (s7 + 1, .6), (s8, .7), (s8 + 1, 1), (DUR - 1.6, 1), (DUR, 0)])
arp_e = env([(0, 0), (.4, .55), (s3, .55), (s3 + .8, 0), (lg - .2, 0), (lg, .9), (s7 - .5, .9), (s7 + .5, 0), (s8 - .2, 0), (s8 + .6, .8), (end, 1), (end + .3, 0)])
kick_e = env([(0, 0), (lg - .1, 0), (lg, 1), (s7 - .3, 1), (s7, 0), (s8, 0), (s8 + .1, .9), (end, .9), (end + .1, 0)])
dark_e = env([(0, 0), (s3, 0), (s3 + 1.5, 1), (lg - .4, 1), (lg, 0), (s7, 0), (s7 + 1, .8), (s8 - .5, .8), (s8, 0), (DUR, 0)])
music = np.zeros((N, 2)); rng = np.random.default_rng(4)
def put(buf, a, t, g=1.0, pan=0.0):
    o = int(t * SR)
    if o >= N or o + len(a) <= 0: return
    if o < 0: a = a[-o:]; o = 0
    a = a[:N - o]; l, r = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
    buf[o:o + len(a), 0] += a * g * l; buf[o:o + len(a), 1] += a * g * r
pad = np.zeros((N, 2)); arp = np.zeros((N, 2)); kick = np.zeros((N, 2)); bass = np.zeros((N, 2))
nb = int((DUR - t0) / (2 * BAR)) + 1
for b in range(nb):
    ch = CH[b % 4]; ts = t0 + b * 2 * BAR; d = 2 * BAR + 1.2; t = tt(d)
    e = np.minimum(1, t / 1.1) * np.minimum(1, (d - t) / 1.2)
    for k, f in enumerate(ch + [ch[0] * 2, ch[2] * 2]):
        for det, pn in ((-.004, -.5), (.004, .5)):
            w = np.sin(2 * np.pi * f * (1 + det) * t + rng.random() * 6) + .35 * np.sin(4 * np.pi * f * (1 + det) * t)
            put(pad, w * e, ts, .09 if k < 4 else .05, pn)
    put(bass, np.sin(2 * np.pi * ch[0] / 2 * t) * e, ts, .34)
    notes = [ch[0] * 4, ch[2] * 4, ch[1] * 4, ch[3] * 4, ch[2] * 4, ch[0] * 8, ch[3] * 4, ch[1] * 4]
    for q in range(16):
        f = notes[q % 8]; tn = tt(.5)
        w = (np.sin(2 * np.pi * f * tn) + .3 * np.sin(4 * np.pi * f * tn)) * np.exp(-tn / .13) * np.minimum(1, tn / .004)
        put(arp, w, ts + q * BEAT / 2, .16 if q % 2 == 0 else .1, .45 if q % 2 else -.45)
    for q in range(8):
        tk = tt(.3); f = 52 + 60 * np.exp(-tk / .03)
        put(kick, np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tk / .11), ts + q * BEAT, .5 if q % 2 == 0 else .28)
bright = lp(pad, 1700); dull = lp(pad, 520)
pad = bright * (1 - dark_e[:, None]) + dull * dark_e[:, None]
music = pad * pad_e[:, None] + lp(arp, 3800) * arp_e[:, None] + kick * kick_e[:, None] + bass * (pad_e * (.5 + .5 * kick_e))[:, None]
music = hp(music, 38); music /= np.max(np.abs(music)) * 1.15
wavfile.write(B / 'music.wav', SR, (music * 32767).astype(np.int16))
print('sfx cues', kept, 'of', len(data['cues']), '| music', round(DUR, 2), 's')
