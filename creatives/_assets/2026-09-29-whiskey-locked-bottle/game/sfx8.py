"""8-bit / chiptune SFX + music bed for the 16-bit game version.
usage: python sfx8.py cues.json vo.wav out.wav [duration_s] [--no-music]
Square / triangle / noise voices only, like an SNES/NES sound chip. Every cue time comes from game.html.
"""
import json, sys
import numpy as np
from scipy.signal import butter, sosfilt
from scipy.io import wavfile

SR = 48000


def tt(d):
    return np.arange(int(SR * d)) / SR


def sq(f, d, duty=.5, vol=1.0):
    t = tt(d); ph = (np.cumsum(np.broadcast_to(f, t.shape)) / SR) % 1.0
    return np.where(ph < duty, 1.0, -1.0) * vol


def tri(f, d):
    t = tt(d); ph = (np.cumsum(np.broadcast_to(f, t.shape)) / SR) % 1.0
    return 4 * np.abs(ph - .5) - 1


def noise(d, seed=0, period=1):
    r = np.random.default_rng(seed); n = int(SR * d)
    x = np.sign(r.standard_normal(n // period + 1)); return np.repeat(x, period)[:n]


def env(n, a=.002, dcy=None, sus=1.0, rel=.01):
    t = np.arange(n) / SR; e = np.minimum(1, t / max(a, 1e-4))
    if dcy: e = e * np.exp(-t / dcy)
    r = int(rel * SR)
    if r and n > r: e[-r:] *= np.linspace(1, 0, r)
    return e * sus


def lp(x, f):
    return sosfilt(butter(2, f, 'lowpass', fs=SR, output='sos'), x)


def seq(notes, step, duty=.5, dcy=.09, voice='sq'):
    """notes: list of freqs (0 = rest); returns mono."""
    out = []
    for f in notes:
        if f <= 0: out.append(np.zeros(int(SR * step))); continue
        s = sq(f, step, duty) if voice == 'sq' else tri(f, step)
        out.append(s * env(len(s), dcy=dcy, rel=.004))
    return np.concatenate(out)


def N(name):
    names = {'C': -9, 'C#': -8, 'D': -7, 'D#': -6, 'E': -5, 'F': -4, 'F#': -3, 'G': -2, 'G#': -1, 'A': 0, 'A#': 1, 'B': 2}
    if not name: return 0
    n, o = name[:-1], int(name[-1]); return 440 * 2 ** ((names[n] + 12 * (o - 4)) / 12)


def st(m, pan=0.0):
    l = np.cos((pan + 1) * np.pi / 4); r = np.sin((pan + 1) * np.pi / 4)
    return np.stack([m * l, m * r], 1)


def nm(x):
    p = np.max(np.abs(x)) or 1; return x / p


# ---------------- instruments ----------------
def blip(seed=0, **_):
    f = [880, 988, 1047, 932][seed % 4]; s = sq(f, .028, .25); return st(nm(s * env(len(s), dcy=.012)), ((seed % 5) - 2) * .1)
def cursor(**_):
    s = sq(1568, .04, .25); return st(nm(s * env(len(s), dcy=.02)))
def confirm(**_):
    return st(nm(seq([N('E6'), N('B6')], .06, .5, .05)))
def window(**_):
    s = sq(np.linspace(500, 1400, int(SR * .09)), .09, .25); return st(nm(s * env(len(s), dcy=.05)))
def close(**_):
    s = sq(np.linspace(1400, 400, int(SR * .1)), .1, .25); return st(nm(s * env(len(s), dcy=.06)))
def coin(**_):
    a = sq(N('B5'), .07, .5); b = sq(N('E6'), .38, .5) * env(int(SR * .38), dcy=.12)
    return st(nm(np.concatenate([a * env(len(a)), b])))
def coinrain(dur=1.5, seed=0, **_):
    out = np.zeros(int(SR * (dur + .5))); r = np.random.default_rng(seed)
    for i in range(int(dur * 10)):
        c = coin()[:, 0] * (.5 + .5 * r.random()) * (1 - i / (dur * 12)); o = int((i * .1 + .03 * r.random()) * SR)
        out[o:o + len(c)] += c[:len(out) - o]
    return st(nm(out), .2)
def itemget(**_):
    a = seq([N('G5'), N('A5'), N('B5'), N('D6')], .09, .5, .2)
    held = (sq(N('G6'), .7, .5) * .6 + sq(N('D6'), .7, .25) * .4) * env(int(SR * .7), dcy=.4)
    b = tri(N('G3'), 1.06) * env(int(SR * 1.06), dcy=.6) * .6
    m = np.concatenate([a, held]); m[:len(b)] += b[:len(m)]
    return st(nm(m))
def itemsmall(**_):
    return st(nm(seq([N('C6'), N('E6'), N('G6'), N('C7')], .06, .5, .12)))
def start(**_):
    return st(nm(seq([N('C5'), N('G5'), N('C6')], .07, .5, .1)))
def powerup(**_):
    fs = [N(x) for x in ['C5', 'E5', 'G5', 'C6', 'E6', 'G6', 'C7', 'E7']]
    return st(nm(seq(fs, .045, .25, .08)))
def oneup(**_):
    return st(nm(seq([N(x) for x in ['E6', 'G6', 'E7', 'C7', 'D7', 'G7']], .08, .5, .12)))
def join(**_):
    return st(nm(seq([N(x) for x in ['G5', 'C6', 'E6', 'G6']], .07, .25, .15)), .3)
def ring(dur=1.1, **_):
    t = tt(dur); f = np.where((t * 25) % 1 < .5, 1300, 1000); s = sq(f, dur, .5)
    gate = ((t % .5) < .4).astype(float); return st(nm(s * gate * env(len(s), rel=.02)))
def alert(**_):
    a = sq(N('A6'), .07, .5); b = sq(N('A6'), .22, .5) * env(int(SR * .22), dcy=.12)
    n = noise(.1, 3, 8) * env(int(SR * .1), dcy=.03) * .5
    m = np.concatenate([a, np.zeros(int(SR * .03)), b]); m[:len(n)] += n
    return st(nm(m))
def drop8(**_):
    s = sq(np.linspace(1600, 300, int(SR * .18)), .18, .5); return st(nm(s * env(len(s), dcy=.1)))
def clunk8(**_):
    n = noise(.12, 4, 12) * env(int(SR * .12), dcy=.03); s = sq(110, .12, .5) * env(int(SR * .12), dcy=.04)
    return st(nm(n + s))
def sparkle8(**_):
    return st(nm(seq([N(x) for x in ['E7', 'B6', 'G7', 'D7', 'B7']], .035, .125, .03)))
def steps(dur=.9, **_):
    out = np.zeros(int(SR * dur))
    for i in range(int(dur / .12)):
        n = noise(.03, i, 20) * env(int(SR * .03), dcy=.008); o = int(i * .12 * SR); out[o:o + len(n)] += n * (.7 + .3 * (i % 2))
    return st(nm(out))
def iris(**_):
    s = sq(np.geomspace(1200, 150, int(SR * .45)), .45, .5); return st(nm(s * env(len(s), dcy=.3)))
def battle(**_):
    n = noise(.6, 9, 3) * np.linspace(1, 0, int(SR * .6))
    s = seq([N(x) for x in ['C7', 'B6', 'A#6', 'A6', 'G#6', 'G6', 'F#6', 'F6', 'E6', 'D#6']], .05, .5, .04)
    m = np.zeros(max(len(n), len(s))); m[:len(n)] += n * .5; m[:len(s)] += s
    return st(nm(m))
def mosaic(**_):
    s = sq(np.geomspace(300, 2400, int(SR * .35)), .35, .125); return st(nm(s * np.linspace(.2, 1, len(s)) * env(len(s), rel=.05)))
def whiteout(**_):
    s = sq(np.geomspace(400, 3200, int(SR * .4)), .4, .25); n = noise(.4, 1, 2) * np.linspace(0, .6, int(SR * .4))
    return st(nm(s * .6 + n))
def jump8(**_):
    s = sq(np.geomspace(300, 1400, int(SR * .15)), .15, .25); return st(nm(s * env(len(s), dcy=.08)))
def sms8(seed=0, **_):
    return st(nm(seq([N('A6'), N('E7')], .035, .25, .03)), ((seed % 3) - 1) * .3)
def hit8(**_):
    n = noise(.35, 5, 6) * env(int(SR * .35), dcy=.1); s = sq(np.geomspace(220, 55, int(SR * .35)), .35, .5) * env(int(SR * .35), dcy=.12)
    return st(nm(n + s))
def heal(**_):
    fs = [N(x) for x in ['C6', 'G6', 'E6', 'C7', 'G6', 'E7', 'C7', 'G7']]
    a = seq(fs, .05, .25, .1); b = seq(fs[::-1], .05, .125, .1) * .5
    m = np.zeros(len(a) + int(SR * .2)); m[:len(a)] += a; m[int(SR * .1):int(SR * .1) + len(b)] += b
    return st(nm(m))
def fall8(**_):
    s = sq(np.geomspace(1800, 400, int(SR * .5)), .5, .5); return st(nm(s * env(len(s), rel=.05)))
def land8(**_):
    n = noise(.15, 7, 16) * env(int(SR * .15), dcy=.04); s = tri(np.geomspace(160, 60, int(SR * .15)), .15) * env(int(SR * .15), dcy=.06)
    return st(nm(n + s * 1.2))
def chest(**_):
    a = seq([N(x) for x in ['G5', 'G#5', 'A5', 'A#5', 'B5', 'C6']], .06, .5, .08)
    b = (sq(N('C7'), .6, .25) * .5 + sq(N('G6'), .6, .5) * .5) * env(int(SR * .6), dcy=.3)
    return st(nm(np.concatenate([a, b])))
def fanfare1(**_):
    return st(nm(seq([N(x) for x in ['C6', 'C6', 'C6', 'G6', 0, 'E6', 'G6']], .09, .5, .1)))
def stampseq(n=8, gap=.08, **_):
    out = np.zeros(int(SR * (n * gap + .2)))
    for i in range(n):
        s = sq(220, .05, .5) * env(int(SR * .05), dcy=.02) + noise(.05, i, 10) * env(int(SR * .05), dcy=.015) * .6
        o = int(i * gap * SR); out[o:o + len(s)] += s
    return st(nm(out))
def blipseq(n=8, gap=.07, **_):
    out = np.zeros(int(SR * (n * gap + .1)))
    for i in range(n):
        s = sq(N('C6') * 2 ** (i / 12), .04, .25) * env(int(SR * .04), dcy=.02); o = int(i * gap * SR); out[o:o + len(s)] += s
    return st(nm(out))
def check8(p=1.0, **_):
    return st(nm(seq([N('C6') * p, N('G6') * p], .06, .5, .1)))
def plink8(step=0, **_):
    scale = [N(x) for x in ['C5', 'D5', 'E5', 'G5', 'A5', 'C6', 'D6', 'E6', 'G6', 'A6', 'C7']]
    f = scale[step % 11] * (2 if step >= 11 else 1); s = sq(f, .12, .125) * env(int(SR * .12), dcy=.05)
    return st(nm(s), ((step % 5) - 2) * .3)
def buzz(**_):
    s = sq(110, .35, .5) + sq(116, .35, .5); return st(nm(s * env(len(s), rel=.03)))
def node(p=1.0, **_):
    return st(nm(seq([N('E5') * p, N('A5') * p, N('E6') * p], .05, .25, .08)))
def legendary(**_):
    a = seq([N(x) for x in ['C5', 'E5', 'G5', 'C6', 'E6', 'G6']], .08, .5, .2)
    held = (sq(N('C6'), 1.2, .25) * .4 + sq(N('E6'), 1.2, .5) * .3 + tri(N('G4'), 1.2) * .5) * env(int(SR * 1.2), dcy=.6)
    return st(nm(np.concatenate([a, held])))
def coinback(**_):
    return st(nm(seq([N('E6'), N('B5')], .08, .5, .1)))
def dialspin(dur=.6, **_):
    out = np.zeros(int(SR * dur))
    for i in range(int(dur * 24)):
        s = sq(1800, .012, .5) * env(int(SR * .012), dcy=.004); o = int(i / 24 * SR); out[o:o + len(s)] += s
    return st(nm(out))
def unlock(**_):
    c = noise(.05, 2, 4) * env(int(SR * .05), dcy=.01); a = seq([N(x) for x in ['G5', 'C6', 'E6', 'G6', 'C7']], .05, .5, .1)
    return st(nm(np.concatenate([c, a])))
def fireworks(dur=1.6, **_):
    out = np.zeros(int(SR * (dur + .6))); r = np.random.default_rng(4)
    for i in range(6):
        n = noise(.4, i, 2 + i % 3) * env(int(SR * .4), dcy=.1) * .7; o = int((i * .27 + .05 * r.random()) * SR); out[o:o + len(n)] += n
    return st(nm(out), 0)
def clearfanfare(**_):
    mel = [N(x) if x else 0 for x in ['G5', 'C6', 'E6', 'G6', 'C7', 'E7', 'G7', 0, 'E7', 0, 'C7', 'D7', 'G7']]
    m = seq(mel, .11, .5, .14)
    bass = seq([N(x) for x in ['C3', 'C3', 'G3', 'G3', 'C4', 'C4', 'E3', 'E3', 'G3', 'G3', 'C3', 'G3', 'C4']], .11, .5, .2, 'tri')
    out = m * .8 + bass[:len(m)] * .7
    tail = (sq(N('C7'), .8, .5) * .4 + sq(N('G6'), .8, .25) * .3 + tri(N('C4'), .8) * .6) * env(int(SR * .8), dcy=.35)
    return st(nm(np.concatenate([out, tail])))


INSTR = {k: v for k, v in globals().items() if callable(v) and k not in ('tt', 'sq', 'tri', 'noise', 'env', 'lp', 'seq', 'N', 'st', 'nm', 'main', 'music', 'butter', 'sosfilt')}


# ---------------- chiptune music bed ----------------
def music(total, stop_at=74.6, boss=(22.0, 31.6)):
    bpm = 150; beat = 60 / bpm; step = beat / 4
    prog = [('C', 'E', 'G'), ('A', 'C', 'E'), ('F', 'A', 'C'), ('G', 'B', 'D')]
    prog_boss = [('A', 'C', 'E'), ('F', 'A', 'C'), ('E', 'G#', 'B'), ('A', 'C', 'E')]
    base = {'C': 'C', 'A': 'A', 'F': 'F', 'G': 'G', 'E': 'E'}
    n = int(total * SR); out = np.zeros(n)
    t = 0.0; bar = 0
    while t < stop_at:
        in_boss = boss[0] <= t < boss[1]
        ch = (prog_boss if in_boss else prog)[bar % 4]
        root = N(ch[0] + '2'); arp = [N(c + '5') for c in ch] + [N(ch[0] + '6')]
        for s16 in range(16):
            tt0 = t + s16 * step
            if tt0 >= stop_at: break
            o = int(tt0 * SR)
            # arpeggio (12.5% square)
            a = sq(arp[s16 % 4], step, .125) * env(int(SR * step), dcy=.06) * .22
            # bass: triangle 8ths (16ths in the boss section)
            if in_boss or s16 % 2 == 0:
                b = tri(root * (2 if (s16 // 2) % 2 else 1), step * (1 if in_boss else 2)) * env(int(SR * step * (1 if in_boss else 2)), rel=.01) * .5
                out[o:o + len(b)] += b[:n - o]
            # drums: kick 1&3, snare 2&4, hats on 8ths
            if s16 in (0, 8):
                k = tri(np.geomspace(150, 45, int(SR * .12)), .12) * env(int(SR * .12), dcy=.05) * .8; out[o:o + len(k)] += k[:n - o]
            if s16 in (4, 12):
                sn = noise(.1, bar * 16 + s16, 3) * env(int(SR * .1), dcy=.035) * .35; out[o:o + len(sn)] += sn[:n - o]
            if s16 % 2 == 0:
                h = noise(.03, s16 + bar, 1) * env(int(SR * .03), dcy=.008) * .15; out[o:o + len(h)] += h[:n - o]
            out[o:o + len(a)] += a[:n - o]
        t += beat * 4; bar += 1
    fade = int(.6 * SR); e = int(stop_at * SR); out[max(0, e - fade):e] *= np.linspace(1, 0, min(fade, e))
    out = lp(out, 7000)
    return np.stack([out, out], 1)


def main():
    cues = json.load(open(sys.argv[1]))
    sr, vo = wavfile.read(sys.argv[2]); assert sr == SR
    vo = vo.astype(np.float64)
    if np.max(np.abs(vo)) > 2: vo /= 32768.0
    if vo.ndim == 1: vo = np.stack([vo, vo], 1)
    total = float(sys.argv[4]) if len(sys.argv) > 4 and not sys.argv[4].startswith('--') else 77.6
    Nn = int(total * SR)
    v = np.zeros((Nn, 2)); v[:min(Nn, len(vo))] = vo[:Nn]
    bus = np.zeros((Nn, 2)); missing = set()
    for i, c in enumerate(cues):
        fn = INSTR.get(c['type'])
        if not fn: missing.add(c['type']); continue
        kw = {k: x for k, x in c.items() if k not in ('t', 'type', 'g')}; kw.setdefault('seed', i)
        a = fn(**kw) * 10 ** (c.get('g', -12) / 20); o = int(c['t'] * SR)
        if o >= Nn: continue
        a = a[:Nn - o]; bus[o:o + len(a)] += a
    # speech envelope for ducking
    envv = np.abs(v[:, 0]); k = int(.06 * SR); envv = np.convolve(envv, np.ones(k) / k, 'same'); envv /= envv.max() or 1
    speech = np.clip(envv * 4, 0, 1)
    bus *= (1 - .3 * speech)[:, None]
    if '--no-music' not in sys.argv:
        m = music(total) * 10 ** (-17 / 20)
        m *= (1 - .6 * speech)[:, None]      # music drops well under Dan
        bus += m
    bus = np.tanh(bus * 1.2) / np.tanh(1.2) * .9
    vv = v / (np.max(np.abs(v)) or 1) * .9
    if '--stems' in sys.argv:
        wavfile.write('stem-vo.wav', SR, vv.astype(np.float32)); wavfile.write('stem-bus.wav', SR, bus.astype(np.float32))
    out = vv + bus
    out = out / np.max(np.abs(out)) * 10 ** (-1 / 20)
    wavfile.write(sys.argv[3], SR, out.astype(np.float32))
    print('cues', len(cues), 'missing', missing)


if __name__ == '__main__':
    main()
