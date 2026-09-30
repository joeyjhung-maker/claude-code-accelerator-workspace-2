"""Procedural SFX synth + mixer for the Locked Whiskey Bottle animation.
usage: python sfx.py cues.json vo.wav out.wav [duration_s]
Every sound is synthesized here (no samples), then laid onto Dan's VO at the cue times
exported from anim.html, so audio and animation share one timeline.
"""
import json, sys
import numpy as np
from scipy.signal import butter, sosfilt, lfilter
from scipy.io import wavfile

SR = 48000


def R(seed):
    return np.random.default_rng(int(abs(seed) * 1000) % (2**32))


def tt(d):
    return np.arange(int(SR * d)) / SR


def filt(x, kind, f, order=2):
    f = np.atleast_1d(f)
    f = np.clip(f, 20, SR / 2 - 200)
    sos = butter(order, f if kind == 'bandpass' else f[0], kind, fs=SR, output='sos')
    return sosfilt(sos, x)


def sweep_bp(x, fc, q=1.4, block=256):
    """time-varying bandpass (RBJ biquad, coefficients per block)."""
    out = np.zeros_like(x)
    zi = np.zeros(2)
    for i in range(0, len(x), block):
        f = float(np.clip(fc[min(i, len(fc) - 1)], 40, SR / 2 - 500))
        w = 2 * np.pi * f / SR
        al = np.sin(w) / (2 * q)
        b = np.array([al, 0, -al]); a = np.array([1 + al, -2 * np.cos(w), 1 - al])
        seg, zi = lfilter(b / a[0], a / a[0], x[i:i + block], zi=zi)
        out[i:i + block] = seg
    return out


def env_exp(n, dec, att=0.002):
    t = np.arange(n) / SR
    return np.minimum(1, t / att) * np.exp(-t / dec)


def sine_sweep(d, f0, f1, curve='exp'):
    t = tt(d)
    if curve == 'exp':
        f = f0 * (f1 / f0) ** (t / d)
    else:
        f = f0 + (f1 - f0) * t / d
    return np.sin(2 * np.pi * np.cumsum(f) / SR), f


def stereo(m, pan=0.0):
    pan = np.broadcast_to(np.asarray(pan, dtype=float), m.shape)
    l = np.cos((pan + 1) * np.pi / 4); r = np.sin((pan + 1) * np.pi / 4)
    return np.stack([m * l, m * r], 1)


def norm(x):
    p = np.max(np.abs(x)) or 1
    return x / p


# ---------------- instruments ----------------
def whoosh(dur=.6, seed=0, lo=180, hi=2600, peak=.55, pan=(-.7, .7), **_):
    n = int(SR * dur); u = np.linspace(0, 1, n)
    shape = np.where(u < peak, (u / peak) ** 2, ((1 - u) / (1 - peak)) ** 1.6)
    x = R(seed).standard_normal(n)
    y = sweep_bp(x, lo + (hi - lo) * shape, q=1.1) + .5 * filt(x, 'lowpass', 300) * shape
    y *= shape
    return stereo(norm(y), np.linspace(pan[0], pan[1], n))


def whip(dur=.34, seed=0, **k):
    return whoosh(dur, seed, 500, 6500, .6, (-.9, .9))


def swish(dur=.24, seed=0, **k):
    return whoosh(dur, seed, 900, 7000, .45, (-.3, .5))


def zoomwhoosh(dur=.7, seed=0, **k):
    a = whoosh(dur, seed, 150, 4200, .82, (0, 0))
    s, _ = sine_sweep(dur, 90, 420); s *= np.linspace(0, 1, len(s)) ** 2 * .35
    return norm(a + stereo(s))


def pop(seed=0, f0=520, **_):
    d = .14; s, _ = sine_sweep(d, f0 * 1.6, f0 * .45)
    y = s * env_exp(len(s), .045)
    y[:90] += R(seed).standard_normal(90) * np.linspace(.6, 0, 90)
    return stereo(norm(y), (R(seed).random() - .5) * .5)


def bubble(seed=0, f0=500, **_):
    d = .11; s, _ = sine_sweep(d, f0, f0 * 2.3)
    y = (s + .3 * np.sin(2 * np.arcsin(np.clip(s, -1, 1)))) * env_exp(len(s), .05, .004)
    return stereo(norm(y), .3)


def tik(seed=0, **_):
    d = .03; f = 2300 * (.85 + .3 * R(seed).random())
    t = tt(d); y = np.sin(2 * np.pi * f * t) * env_exp(len(t), .008)
    y += filt(R(seed + 1).standard_normal(len(t)), 'highpass', 4000) * env_exp(len(t), .003) * .5
    return stereo(norm(y), (R(seed + 2).random() - .5) * .6)


def scratch(dur=.8, seed=0, **_):
    n = int(SR * dur); r = R(seed)
    x = filt(r.standard_normal(n), 'bandpass', [1800, 7500])
    strokes = np.abs(np.sin(np.pi * np.cumsum(7 + 5 * r.random(n) * 0 + 3 * np.sin(np.arange(n) / SR * 2)) / SR))
    grain = filt(r.standard_normal(n), 'lowpass', 40); grain = .6 + .4 * grain / (np.max(np.abs(grain)) + 1e-9)
    e = np.minimum(1, np.arange(n) / (SR * .04)) * np.minimum(1, (n - np.arange(n)) / (SR * .08))
    return stereo(norm(x * strokes ** .6 * grain * e), (r.random() - .5) * .4)


def scribble(dur=.4, seed=0, **k):
    n = int(SR * dur); r = R(seed)
    x = filt(r.standard_normal(n), 'bandpass', [1200, 6000])
    am = .5 + .5 * np.sin(2 * np.pi * 14 * np.arange(n) / SR)
    e = np.minimum(1, np.arange(n) / (SR * .02)) * np.minimum(1, (n - np.arange(n)) / (SR * .05))
    return stereo(norm(x * am * e))


def marker(seed=0, **_):
    n = int(SR * .32); r = R(seed)
    x = sweep_bp(r.standard_normal(n), np.linspace(900, 2400, n), q=2)
    e = np.sin(np.linspace(0, np.pi, n)) ** .7
    return stereo(norm(x * e), np.linspace(-.4, .4, n))


def thump(seed=0, f0=95, dec=.22, **_):
    d = dec * 3; s, _ = sine_sweep(d, f0, f0 * .45)
    y = s * env_exp(len(s), dec, .003)
    nb = filt(R(seed).standard_normal(len(s)), 'lowpass', 1400) * env_exp(len(s), .025)
    return stereo(norm(y + .6 * nb))


def impact(seed=0, soft=0, **_):
    d = 1.4; s, _ = sine_sweep(d, 72, 34)
    boom = s * env_exp(len(s), .45 if not soft else .25, .003)
    crack = filt(R(seed).standard_normal(len(s)), 'highpass', 2500) * env_exp(len(s), .03)
    body = filt(R(seed + 1).standard_normal(len(s)), 'lowpass', 900) * env_exp(len(s), .12)
    y = boom + (.35 if soft else .7) * crack + .5 * body
    return stereo(norm(y))


def stamp(seed=0, **_):
    a = thump(seed, 110, .12)[:, 0]
    n = len(a); t = np.arange(n) / SR
    knock = np.sin(2 * np.pi * 240 * t) * env_exp(n, .05)
    paper = filt(R(seed).standard_normal(n), 'bandpass', [500, 3000]) * env_exp(n, .06)
    return stereo(norm(a + .6 * knock + .7 * paper))


def bell(f=1320, d=1.4, seed=0):
    t = tt(d); y = np.zeros_like(t)
    for m, a, dec in [(1, 1, .9), (2.0, .35, .6), (2.76, .5, .45), (5.4, .2, .2), (8.9, .08, .1)]:
        y += a * np.sin(2 * np.pi * f * m * t) * np.exp(-t / dec)
    return y * np.minimum(1, t / .002)


def ding(seed=0, f=1568, **_):
    return stereo(norm(bell(f)), .2)


def metal(seed=0, base=900, d=.18, dec=.05):
    t = tt(d); r = R(seed); y = np.zeros_like(t)
    for m in [1, 2.3, 3.7, 5.2, 7.1]:
        y += np.sin(2 * np.pi * base * m * (.97 + .06 * r.random()) * t) * np.exp(-t / (dec * (1.2 - m / 10)))
    return y * np.minimum(1, t / .001)


def clack(seed=0, **_):
    m = metal(seed, 820, .3, .06)
    th = thump(seed, 130, .06)[:, 0][:len(m)]
    out = np.zeros(len(m)); out[:len(th)] += th * .8
    m2 = metal(seed + 3, 1150, .2, .04); off = int(.05 * SR); out[off:off + len(m2)] += m2[:len(out) - off] * .7
    return stereo(norm(m + out))


def coin(seed=0, **_):
    r = R(seed + 11); d = .35; t = tt(d); y = np.zeros_like(t)
    for f in [3100, 4350, 5650, 7300]:
        y += (.4 + .6 * r.random()) * np.sin(2 * np.pi * f * (.93 + .14 * r.random()) * t) * np.exp(-t / (.06 + .12 * r.random()))
    return stereo(norm(y * np.minimum(1, t / .0008)), (r.random() - .5) * .8)


def kaching(seed=0, **_):
    out = np.zeros(int(SR * 1.8))
    d = metal(seed, 560, .25, .07); out[:len(d)] += d * .8
    for off, f in [(.07, 2093), (.15, 2637)]:
        b = bell(f, 1.5); o = int(off * SR); out[o:o + len(b)] += b[:len(out) - o] * .8
    for i in range(10):
        c = coin(seed + i)[:, 0]; o = int((.1 + .05 * i + .02 * R(seed + i).random()) * SR); out[o:o + len(c)] += c[:len(out) - o] * .25
    return stereo(norm(out))


def glug(seed=0, **_):
    out = np.zeros(int(SR * 1.05)); r = R(seed)
    for i in range(6):
        d = .085; s, _ = sine_sweep(d, 150 + 30 * r.random(), 330 + 60 * r.random())
        y = s * np.sin(np.linspace(0, np.pi, len(s))) ** 1.5
        o = int((i * .16 + .02 * r.random()) * SR); out[o:o + len(y)] += y[:len(out) - o] * (1 - i * .08)
    out = filt(out, 'lowpass', 1200)
    return stereo(norm(out))


def dial(dur=1.1, seed=0, rate=14, **_):
    out = np.zeros(int(SR * dur)); n = int(dur * rate)
    for i in range(n):
        c = tik(seed + i)[:, 0] * .6 + metal(seed + i, 1300, .03, .006) * .5
        o = int(i / rate * SR); out[o:o + len(c)] += c[:len(out) - o]
    return stereo(norm(out), .15)


def paper(seed=0, dur=.45, **_):
    n = int(SR * dur); r = R(seed)
    x = sweep_bp(r.standard_normal(n), np.linspace(700, 2600, n), q=.9)
    flutter = .7 + .3 * np.sin(2 * np.pi * 23 * np.arange(n) / SR)
    e = np.sin(np.linspace(0, np.pi, n)) ** 1.2
    return stereo(norm(x * flutter * e), np.linspace(-.6, .2, n))


def slap(seed=0, **_):
    n = int(SR * .25)
    x = filt(R(seed).standard_normal(n), 'bandpass', [400, 4000]) * env_exp(n, .03)
    th = thump(seed, 150, .05)[:n, 0]; x[:len(th)] += .5 * th
    return stereo(norm(x))


def riser(dur=1.4, seed=0, **_):
    n = int(SR * dur); u = np.linspace(0, 1, n)
    x = sweep_bp(R(seed).standard_normal(n), 400 + 7000 * u ** 2, q=2.5)
    s, _ = sine_sweep(dur, 180, 1400)
    y = (x + .3 * s) * u ** 2.2
    return stereo(norm(y))


def shimmer(dur=1.2, seed=0, **_):
    out = np.zeros(int(SR * (dur + .4))); r = R(seed)
    notes = [1568, 1760, 2093, 2349, 2637, 3136, 3520, 4186]
    for i in range(int(18 * dur)):
        f = notes[r.integers(len(notes))]; b = bell(f, .5) * .5
        o = int(r.random() * dur * .8 * SR); out[o:o + len(b)] += b[:len(out) - o] * (.4 + .6 * r.random())
    return stereo(norm(out), 0)


def sparkle(dur=.6, seed=0, **k):
    return shimmer(dur, seed + 5)


def boing(seed=0, **_):
    d = .55; t = tt(d)
    f = 220 * (1 + .35 * np.sin(2 * np.pi * 16 * t) * np.exp(-t / .15))
    y = np.sin(2 * np.pi * np.cumsum(f) / SR) * env_exp(len(t), .18)
    return stereo(norm(y))


def bounce(seed=0, **_):
    out = np.zeros(int(SR * .6))
    for i, o in enumerate([0, .18, .32]):
        p = pop(seed + i, 700 - i * 60)[:, 0] * (1 - i * .3); s = int(o * SR); out[s:s + len(p)] += p[:len(out) - s]
    return stereo(norm(out))


def zip_(seed=0, **_):
    n = int(SR * .28); u = np.linspace(0, 1, n)
    x = sweep_bp(R(seed).standard_normal(n), 5000 - 4200 * u, q=3)
    s, _ = sine_sweep(.28, 1600, 300)
    return stereo(norm((x + .4 * s) * (1 - u) ** .5 * np.minimum(1, u * 40)))


def squeak(seed=0, **_):
    d = .3; t = tt(d); f = 1250 + 180 * np.sin(2 * np.pi * 26 * t) + 500 * t
    ph = 2 * np.pi * np.cumsum(f) / SR
    y = (np.sin(ph) + .4 * np.sin(2 * ph) + .2 * np.sin(3 * ph)) * np.sin(np.pi * t / d) ** .8
    return stereo(norm(filt(y, 'bandpass', [800, 5000])), .4)


def click(seed=0, **_):
    n = int(SR * .08); t = np.arange(n) / SR
    y = filt(R(seed).standard_normal(n), 'highpass', 3000) * env_exp(n, .004) + np.sin(2 * np.pi * 3400 * t) * env_exp(n, .01)
    hum = np.sin(2 * np.pi * 120 * tt(.5)) * .08 * np.exp(-tt(.5) / .2)
    out = np.zeros(int(SR * .5)); out[:n] += y; out += hum
    return stereo(norm(out))


def blips(seed=0, **_):
    out = np.zeros(int(SR * .32))
    for i, f in enumerate([880, 1320, 1175]):
        t = tt(.065); sq = np.sign(np.sin(2 * np.pi * f * t)) * .5 + np.sin(2 * np.pi * f * t) * .5
        y = filt(sq, 'lowpass', 4000) * np.minimum(1, (len(t) - np.arange(len(t))) / 200)
        o = int(i * .09 * SR); out[o:o + len(y)] += y
    return stereo(norm(out), .4)


def plink(seed=0, step=0, **_):
    scale = [523, 587, 659, 784, 880, 1047, 1175, 1319, 1568, 1760, 2093]
    f = scale[step % len(scale)] * (2 if step >= len(scale) else 1)
    t = tt(.35); y = (np.sin(2 * np.pi * f * t) + .25 * np.sin(4 * np.pi * f * t)) * env_exp(len(t), .08)
    return stereo(norm(y), (step % 5 - 2) * .3)


def cash(dur=1.5, seed=0, **_):
    n = int(SR * dur); r = R(seed)
    x = filt(r.standard_normal(n), 'bandpass', [1500, 8000])
    grains = (filt(r.standard_normal(n), 'lowpass', 30) > .002).astype(float)
    grains = filt(grains, 'lowpass', 200)
    e = np.minimum(1, np.arange(n) / (SR * .1)) * np.minimum(1, (n - np.arange(n)) / (SR * .3))
    return stereo(norm(x * (.3 + grains) * e), np.sin(np.linspace(0, 6, n)) * .5)


def puff(seed=0, **_):
    n = int(SR * .4); x = filt(R(seed).standard_normal(n), 'bandpass', [250, 1600])
    return stereo(norm(x * np.sin(np.linspace(0, np.pi, n)) ** 2))


def whump(seed=0, **_):
    n = int(SR * .6); u = np.linspace(0, 1, n)
    x = filt(R(seed).standard_normal(n), 'lowpass', 380) * np.sin(np.pi * u) ** 1.5
    s = np.sin(2 * np.pi * 52 * tt(.6)) * np.sin(np.pi * u) * .7
    return stereo(norm(x + s))


def drawer(seed=0, **_):
    n = int(SR * .45); x = sweep_bp(R(seed).standard_normal(n), np.linspace(300, 1100, n), q=2) * np.linspace(.3, 1, n)
    out = np.zeros(int(SR * .7)); out[:n] += x
    th = thump(seed, 140, .07)[:, 0]; o = n - 400; out[o:o + len(th)] += th[:len(out) - o] * 1.2
    return stereo(norm(out))


def clatter(seed=0, **_):
    out = np.zeros(int(SR * .5))
    for i in range(4):
        th = thump(seed + i, 160 + 40 * i, .04)[:, 0] * (1 - i * .2); o = int(i * .06 * SR); out[o:o + len(th)] += th[:len(out) - o]
    out += filt(R(seed).standard_normal(len(out)), 'bandpass', [300, 2500]) * env_exp(len(out), .05) * .5
    return stereo(norm(out))


def tick(seed=0, f0=1.0, **_):
    sc = scratch(.12, seed)[:, 0]
    p = pop(seed, 700 * f0)[:, 0]
    out = np.zeros(max(len(sc), len(p)) + int(.1 * SR)); out[:len(sc)] += sc * .7
    o = int(.09 * SR); out[o:o + len(p)] += p
    b = bell(1760 * f0, .5) * .25; out[o:o + len(b)] += b[:len(out) - o]
    return stereo(norm(out))


def typing(dur=1.5, seed=0, **_):
    out = np.zeros(int(SR * dur)); r = R(seed); t = 0.0; i = 0
    while t < dur - .05:
        c = tik(seed + i)[:, 0]; o = int(t * SR); out[o:o + len(c)] += c[:len(out) - o] * (.5 + .5 * r.random())
        t += .07 + .09 * r.random(); i += 1
    return stereo(norm(out))


def patter(dur=.45, seed=0, **_):
    out = np.zeros(int(SR * (dur + .1)))
    for i in range(15):
        c = pop(seed + i, 900 + 40 * i)[:, 0] * .6; o = int(i * .025 * SR); out[o:o + len(c)] += c[:len(out) - o]
    return stereo(norm(out))


def fold(seed=0, **_):
    p = paper(seed, .3)[:, 0]; th = thump(seed, 120, .08)[:, 0]
    out = np.zeros(len(p) + len(th)); out[:len(p)] += p; out[len(p) - 800:len(p) - 800 + len(th)] += th
    return stereo(norm(out))


def pour(dur=2.0, seed=0, **_):
    n = int(SR * dur); r = R(seed)
    x = filt(r.standard_normal(n), 'bandpass', [2000, 7000]) * .15
    e = np.minimum(1, np.arange(n) / (SR * .2)) * np.minimum(1, (n - np.arange(n)) / (SR * .3))
    return stereo(norm(x * e), .5)


def swell(dur=2.6, seed=0, **_):
    t = tt(dur); y = np.zeros_like(t)
    for f in [220, 277.18, 329.63, 440, 554.37, 659.25]:
        for det in (-.6, .6):
            ph = 2 * np.pi * (f + det) * t
            y += (np.sin(ph) + .3 * np.sin(2 * ph) + .12 * np.sin(3 * ph)) / 6
    e = np.minimum(1, t / .7) * np.minimum(1, (dur - t) / 1.0)
    y = filt(y * e, 'lowpass', 2200)
    return norm(np.stack([y, np.roll(y, 480)], 1))


INSTR = dict(whoosh=whoosh, whip=whip, swish=swish, zoomwhoosh=zoomwhoosh, pop=pop, bubble=bubble, tik=tik,
             scratch=scratch, scribble=scribble, marker=marker, thump=thump, impact=impact, stamp=stamp, ding=ding,
             clack=clack, coin=coin, kaching=kaching, glug=glug, dial=dial, paper=paper, slap=slap, riser=riser,
             shimmer=shimmer, sparkle=sparkle, boing=boing, bounce=bounce, zip=zip_, squeak=squeak, click=click,
             blips=blips, plink=plink, cash=cash, puff=puff, whump=whump, drawer=drawer, clatter=clatter, tick=tick,
             typing=typing, patter=patter, fold=fold, pour=pour, swell=swell)


# per-type level trims (dB). v4: bells were too loud and distracting.
TRIM = dict(ding=-6, kaching=-6, shimmer=-6, sparkle=-6, plink=-4, tick=-4)


def main():
    cues = json.load(open(sys.argv[1]))
    sr, vo = wavfile.read(sys.argv[2])
    assert sr == SR, sr
    vo = vo.astype(np.float64)
    if vo.dtype.kind == 'i' or np.max(np.abs(vo)) > 2:
        vo /= 32768.0
    if vo.ndim == 1:
        vo = np.stack([vo, vo], 1)
    total = float(sys.argv[4]) if len(sys.argv) > 4 else 77.6
    N = int(total * SR)
    mixv = np.zeros((N, 2)); mixv[:min(N, len(vo))] = vo[:N]
    bus = np.zeros((N, 2))
    missing = set()
    for i, c in enumerate(cues):
        fn = INSTR.get(c['type'])
        if not fn:
            missing.add(c['type']); continue
        kw = {k: v for k, v in c.items() if k not in ('t', 'type', 'g')}
        kw.setdefault('seed', i)
        a = fn(**kw) * 10 ** ((c.get('g', -12) + TRIM.get(c['type'], 0)) / 20)
        o = int(c['t'] * SR)
        if o >= N: continue
        a = a[:N - o]; bus[o:o + len(a)] += a
    # duck SFX a little under speech
    env = np.abs(mixv[:, 0]); k = int(.05 * SR)
    env = np.convolve(env, np.ones(k) / k, 'same'); env /= env.max() or 1
    duck = 1 - .35 * np.clip(env * 3, 0, 1)
    bus *= duck[:, None]
    vop = np.max(np.abs(mixv)) or 1
    bus = np.tanh(bus * 1.2) / np.tanh(1.2) * .9      # soft-clip the SFX bus only; the VO stays untouched
    if '--stems' in sys.argv:
        wavfile.write('stem-vo.wav', SR, (mixv / vop * .9).astype(np.float32)); wavfile.write('stem-bus.wav', SR, bus.astype(np.float32))
    out = mixv / vop * .9 + bus
    out = out / np.max(np.abs(out)) * 10 ** (-1 / 20)
    wavfile.write(sys.argv[3], SR, out.astype(np.float32))
    print('cues', len(cues), 'missing', missing, 'sfx peak', round(float(np.max(np.abs(bus))), 3))


if __name__ == '__main__':
    main()
