"""Pixar version sound: cartoon SFX + sneaky caper score. Writes the SFX/music bus only.
usage: python pixar_audio.py <vo_master.wav> <out_bus.wav>
Balance happens in ffmpeg afterwards (VO -16 LUFS, bus -24, master -14)."""
import sys
import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / 'build'))
import sfx as S  # noqa: E402

SR = 48000; TOTAL = 77.6; N = int(TOTAL * SR)
bus = np.zeros((N, 2))
tt = lambda d: np.arange(int(SR * d)) / SR


def put(a, t, g):
    if a.ndim == 1: a = np.stack([a, a], 1)
    o = int(t * SR); a = a[:max(0, N - o)] * 10 ** (g / 20); bus[o:o + len(a)] += a


def nm(x): return x / (np.max(np.abs(x)) or 1)
def lp(x, f): return sosfilt(butter(2, f, 'lowpass', fs=SR, output='sos'), x)


def slide_whistle(d=.6, f0=500, f1=1600):
    t = tt(d); f = f0 * (f1 / f0) ** (t / d) * (1 + .01 * np.sin(2 * np.pi * 6 * t))
    return nm(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.sin(np.pi * t / d) ** .6)
def skid():
    t = tt(.5); n = np.random.default_rng(1).standard_normal(len(t))
    sq = np.sin(2 * np.pi * np.cumsum(2200 - 900 * t) / SR) * .5
    return nm((S.filt(n, 'bandpass', [1500, 5000]) * .6 + sq) * np.exp(-t / .25))
def wobble(d=1.2):
    t = tt(d); f = 180 * (1 + .45 * np.sin(2 * np.pi * 11 * t) * np.exp(-t / .6))
    return nm(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / .5))
def snore(d=3.6):
    t = tt(d); n = lp(np.random.default_rng(3).standard_normal(len(t)), 500)
    env = np.clip(np.sin(2 * np.pi * .55 * t), 0, 1) ** 2
    whistle = np.sin(2 * np.pi * np.cumsum(900 + 300 * np.sin(2 * np.pi * .55 * t)) / SR) * np.clip(-np.sin(2 * np.pi * .55 * t), 0, 1) ** 3 * .15
    return nm(n * env + whistle)
def ring(d=1.4):
    t = tt(d); b = np.sin(2 * np.pi * 1400 * t) + np.sin(2 * np.pi * 1750 * t)
    return nm(b * (np.sin(2 * np.pi * 22 * t) > 0) * ((t % .7) < .5))
def womp():
    out = []
    for f, d in [(233, .28), (220, .28), (208, .28), (196, .9)]:
        t = tt(d); fv = f * (1 + .02 * np.sin(2 * np.pi * 5 * t) * (t > .2))
        ph = 2 * np.pi * np.cumsum(fv) / SR; s = (np.sin(ph) + .5 * np.sin(2 * ph) + .3 * np.sin(3 * ph))
        out.append(lp(s, 1800) * np.minimum(1, t / .03) * np.minimum(1, (d - t) / .06))
    return nm(np.concatenate(out))
def drumroll(d=1.7):
    t = tt(d); n = np.random.default_rng(5).standard_normal(len(t))
    hits = (np.sin(2 * np.pi * 26 * t) > .6).astype(float)
    return nm(S.filt(n, 'bandpass', [200, 5000]) * lp(hits, 300) * (.4 + .6 * t / d))
def flutter():
    out = np.zeros(int(SR * .7))
    for i in range(9):
        b = S.bubble(i, 900 + 80 * i)[:, 0] * .5; o = int(i * .07 * SR); out[o:o + len(b)] += b[:len(out) - o]
    return nm(out)
def plink(step):
    f = [523, 659, 784, 880, 1047, 1319, 1568, 1760][step % 8] * (2 if step >= 8 else 1)
    t = tt(.3); return nm((np.sin(2 * np.pi * f * t) + .3 * np.sin(4 * np.pi * f * t)) * np.exp(-t / .08))
def march(n=6, gap=.33):
    out = np.zeros(int(SR * (n * gap + .3)))
    for i in range(n):
        th = S.thump(i, 150, .05)[:, 0]; o = int(i * gap * SR); out[o:o + len(th)] += th
    return nm(out)


C = [
 (0.15, slide_whistle(.9, 300, 1200), -16), (0.3, S.whoosh(1.4, 1, 200, 2600, .5, (-.2, .2)), -16), (2.45, skid(), -12), (2.75, wobble(.8), -16),
 (3.0, S.dial(2.0, 2, 22), -12), (4.3, S.thump(3, 90, .1), -8), (4.35, S.boing(4), -14),
 (5.0, slide_whistle(.8, 400, 1900), -20), (5.2, S.shimmer(.8, 5), -24),
 (7.8, S.dial(1.3, 6, 11), -14), (8.9, S.pop(7, 300), -18),
 (9.6, ring(.9), -14), (10.1, S.pop(8, 500), -14),
 (11.2, snore(3.8), -12),
 (15.0, S.zip_(9), -12), (15.2, S.blips(10), -14), (15.45, S.bubble(11, 600), -14), (15.6, S.bubble(12, 800), -15), (15.75, S.boing(13), -12), (15.8, S.clatter(14), -14), (16.0, S.paper(15, .6), -18),
 (18.45, wobble(1.8), -13), (19.2, S.boing(16), -16),
 (22.0, S.riser(1.0, 17), -18), (22.3, S.cash(3.0, 18), -14), (23.2, S.coin(19), -20), (24.0, S.coin(20), -20),
 (25.3, S.impact(21, soft=1), -12), (25.32, S.kaching(22), -12), (25.5, S.thump(23, 70, .2), -12), (25.55, S.boing(24), -14),
 (27.0, S.squeak(25), -16), (27.1, S.shimmer(1.2, 26), -20), (28.0, S.slap(27), -14), (28.6, S.pop(28, 700), -18),
 (30.05, S.riser(.4, 29), -18), (30.1, S.kaching(30), -11), (30.12, S.impact(31, soft=1), -14),
 (31.7, march(6, .33), -14), (33.3, S.pop(32, 600), -14), (33.35, S.sparkle(.5, 33), -20),
 (37.5, S.click(34), -12), (37.6, S.shimmer(1.0, 35), -16), (38.4, S.boing(36), -16), (42.3, S.pop(37, 450), -14),
 (43.3, S.paper(38, .8), -12), (43.6, S.paper(39, .8), -14), (44.2, S.thump(40, 110, .08), -14), (45.0, S.paper(41, .6), -16),
 (46.3, ring(2.4), -16), (47.0, S.whoosh(1.2, 42, 100, 700, .5, (-.8, .8)), -22),
 (48.9, S.squeak(43), -14), (49.3, flutter(), -16), (49.9, womp(), -12),
 (51.0, S.whoosh(1.0, 44, 200, 2000, .6, (-.5, .5)), -18),
 (59.85, S.puff(45), -10), (59.9, S.sparkle(.8, 46), -14), (61.8, S.scribble(.3, 47), -14), (61.82, S.buzz if hasattr(S, 'buzz') else S.thump(48, 110, .1), -16),
 (63.0, S.pop(49, 520), -14), (63.05, S.sparkle(.6, 50), -18),
 (64.5, drumroll(1.7), -14), (66.25, S.impact(51, soft=1), -12), (66.27, S.shimmer(1.6, 52), -14), (67.0, S.ding(53, 1568), -22), (69.9, S.ding(54, 2093), -18),
 (74.6, S.clack(55), -12), (74.7, S.pop(56, 400), -12), (74.72, S.sparkle(.8, 57), -14), (74.9, S.swell(2.6, 58), -14), (75.0, S.kaching(59), -18),
]
for i in range(22):
    C.append((54.6 + i * .1, plink(i), -22))
# sounds for the motion-graphics layer (mograph.js)
for i, t0 in enumerate([5.0, 11.2, 22.0, 31.6, 37.25, 50.95, 59.55, 66.2, 74.65]):      # ribbon swooshes
    C.append((t0 - .25, S.whoosh(.55, 100 + i, 300, 4200, .55, (-.9, .9) if i % 2 == 0 else (.9, -.9)), -17))
for i, t0 in enumerate([1.2, 3.2, 7.95, 11.5, 27.4, 69.0]):                             # arrows drawing on
    C.append((t0, S.swish(.24, 120 + i), -21))
for i in range(5): C.append((33.3 + i * .12, S.pop(140 + i, 600 + 60 * i), -15))       # check stamps
for t0 in (63.1, 72.55): C.append((t0, S.pop(150, 820), -15))
for i in range(10): C.append((35.0 + i * .18 + .85, S.coin(160 + i), -24))              # coins flying out of the folders
C += [(18.5, S.thump(170, 120, .09), -12), (42.3, S.ding(171, 1760), -18), (1.4, S.pop(172, 500), -18), (8.1, S.pop(173, 520), -18), (11.6, S.pop(174, 540), -18)]
for t, a, g in C:
    if callable(a): a = a(0)
    put(a, t, g)


def score():
    """Sneaky caper: plucked walking bass + finger snaps + xylophone motif, 112 bpm swing, C minor -> major on the money."""
    out = np.zeros(N); beat = 60 / 112; t = 0.0; bar = 0
    minor = [65.41, 77.78, 98.0, 103.83, 98.0, 77.78, 73.42, 61.74]
    major = [65.41, 82.41, 98.0, 110.0, 98.0, 82.41, 73.42, 61.74]
    motif = [523.25, 0, 622.25, 587.33, 0, 523.25, 466.16, 0]
    while t < 74.5:
        money = (22 <= t < 31.6) or (62.3 <= t < 74.5)
        line = major if money else minor
        for k in range(8):
            tk = t + k * beat / 2 + (beat * .08 if k % 2 else 0)
            o = int(tk * SR)
            if o >= N: break
            m = int(beat * .5 * SR); tb = np.arange(m) / SR
            pl = np.sin(2 * np.pi * line[k] * tb) * np.exp(-tb / .18) + .3 * np.sin(4 * np.pi * line[k] * tb) * np.exp(-tb / .08)
            out[o:o + m] += pl[:N - o] * .9
            if k in (2, 6):
                sn = S.filt(np.random.default_rng(bar * 8 + k).standard_normal(int(.05 * SR)), 'bandpass', [1500, 6000]) * np.exp(-np.arange(int(.05 * SR)) / SR / .012)
                out[o:o + len(sn)] += sn[:N - o] * .5
            f = motif[k] * (1.1225 if money and motif[k] in (622.25,) else 1)
            if f and bar % 2 == 0:
                x = np.sin(2 * np.pi * f * tb) * np.exp(-tb / .12) * .35 + np.sin(2 * np.pi * f * 3 * tb) * np.exp(-tb / .04) * .1
                out[o:o + m] += x[:N - o]
        t += beat * 4; bar += 1
    tl = np.arange(N) / SR
    env = np.clip((74.6 - tl) / .6, 0, 1) * (1 - .5 * ((tl > 11.2) & (tl < 15.0))) * (1 - .6 * ((tl > 64.5) & (tl < 66.3)))
    s = lp(out * env, 5000)
    return np.stack([s, s], 1)


bus += score() * 10 ** (-17 / 20)
_, vo = wavfile.read(sys.argv[1]); vo = vo.astype(np.float64)
if np.max(np.abs(vo)) > 2: vo /= 32768.0
vm = np.abs(vo[:, 0] if vo.ndim > 1 else vo)[:N]; vm = np.pad(vm, (0, N - len(vm)))
k = int(.06 * SR); e = np.convolve(vm, np.ones(k) / k, 'same'); e /= e.max() or 1
bus *= (1 - .35 * np.clip(e * 4, 0, 1))[:, None]
bus = np.tanh(bus * 1.2) / np.tanh(1.2)
wavfile.write(sys.argv[2], SR, bus.astype(np.float32))
print('bus written')
