"""Heist sound design: dark pulse score + designed SFX + clean Veo foley, balanced VO-first.
usage: python heist_audio.py <vo_master.wav> <out_bus.wav>
Writes the SFX+music bus only (48k stereo float). The VO/bus balance and loudness pass happen in ffmpeg
(see BUILD note): VO -16 LUFS, bus -24 LUFS, master -14 LUFS.
"""
import sys, subprocess
import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / 'build'))   # the doodle-version synth library
import sfx as S  # noqa: E402

SR = 48000; TOTAL = 77.6; N = int(TOTAL * SR)
bus = np.zeros((N, 2))


def put(a, t, g):
    o = int(t * SR); a = a[:max(0, N - o)] * 10 ** (g / 20); bus[o:o + len(a)] += a


def lp(x, f): return sosfilt(butter(2, f, 'lowpass', fs=SR, output='sos'), x)
def hp(x, f): return sosfilt(butter(2, f, 'highpass', fs=SR, output='sos'), x)


# ---- 1. clean Veo foley (only the clips Gemini flagged as speech/music-free) ----
def veo(clip, src_in, src_out, t, g, speed=1.0):
    p = HERE.parent / 'clips' / f'{clip}.mp4'
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-ss', str(src_in), '-to', str(src_out), '-i', str(p),
                          '-ac', '2', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True, check=True).stdout
    a = np.frombuffer(raw, dtype=np.float32).reshape(-1, 2).astype(np.float64)
    a /= (np.max(np.abs(a)) or 1); f = int(.08 * SR)
    a[:f] *= np.linspace(0, 1, f)[:, None]; a[-f:] *= np.linspace(1, 0, f)[:, None]
    put(a, t, g)


veo('c02-dials', .5, 2.5, 3.0, -14)       # dial clicks
veo('c09-cash', 0, 5.0, 22.0, -15)        # money counter
veo('c13-empty', 0, 4.35, 43.25, -16)     # unanswered phone ringing

# ---- 2. designed SFX (reusing the doodle synth instruments) ----
CUTS = [3.0, 5.0, 7.7, 9.6, 11.2, 15.0, 18.4, 21.1, 22.0, 27.0, 31.6, 37.25, 43.25, 47.6, 50.95, 59.55, 64.35, 71.4, 75.55]
for i, c in enumerate(CUTS):
    put(S.whoosh(.55, i, 120, 1800, .75, (-.4, .4)), c - .4, -24)          # soft air on every cut
cues = [
    (0.0, S.riser(2.6, 1), -26), (0.35, S.thump(1, 70, .5), -16),          # cold open sub hit
    (2.95, S.clack(2), -12),                                                # lock detail
    (4.3, S.paper(3, .45), -18),                                            # the letter
    (5.2, S.impact(4, soft=1), -14),                                        # $10 million
    (7.95, S.stamp(5), -20),                                                # wax seal crack
    (9.6, S.dial(1.0, 6, 11), -18),                                         # rotary dial
    (9.65, S.thump(6, 60, .6), -16),                                        # "one single offer" beat
    (15.6, S.thump(7, 80, .3), -16), (15.9, S.bubble(8, 700), -20),         # sales? / SMS
    (18.45, S.impact(9, soft=1), -16),                                      # if you don't get paid
    (21.05, S.whump(10), -18),                                              # cut to Dan
    (23.8, S.riser(1.5, 11), -16), (25.3, S.impact(12), -8), (25.32, S.kaching(13), -20),   # $1.2M
    (28.0, S.slap(14), -18),                                                # envelope slides
    (28.4, S.riser(1.45, 15), -17), (30.1, S.impact(16), -9), (30.12, S.coin(17), -22),      # $225,000
    (31.6, S.drawer(18), -12),                                              # the filing drawer
    (33.2, S.thump(19, 90, .25), -18),
    (42.3, S.thump(20, 70, .5), -15),                                       # "immediately"
    (43.4, S.tick(21), -24), (44.8, S.tick(22), -24), (46.3, S.tick(23), -24), (48.9, S.tick(24), -23),
    (51.0, S.whoosh(1.2, 25, 100, 900, .6, (-.6, .6)), -18),                # aerial sweep
    (58.3, S.impact(26, soft=1), -16),
    (61.8, S.scribble(.3, 27), -18), (61.8, S.thump(27, 110, .12), -18),    # tech guru struck
    (63.0, S.thump(28, 65, .5), -15),
    (66.05, S.riser(1.2, 29), -18), (66.2, S.impact(30, soft=1), -12), (66.25, S.shimmer(1.4, 31), -26),  # book reveal
    (69.9, S.ding(32, 1319), -26),
    (75.45, S.riser(.5, 33), -18), (75.6, S.clack(34), -8), (75.62, S.impact(35, soft=1), -14), (75.7, S.swell(2.4, 36), -16),
]
for t, a, g in cues:
    put(a, t, g)


# ---- 3. score: dark heist pulse in A minor, 96 bpm ----
def score():
    out = np.zeros(N); bpm = 96; beat = 60 / bpm; e8 = beat / 2
    chords = [(55.0, [220.0, 261.63, 329.63]), (43.65, [174.61, 220.0, 261.63]), (36.71, [146.83, 174.61, 220.0]), (41.2, [164.81, 207.65, 246.94])]
    t = 0.0; bar = 0
    while t < 75.4:
        root, pad = chords[bar % 4]; bar_len = beat * 4
        # pad (detuned saw-ish, filtered) for the whole bar
        n = int(bar_len * SR); tt = np.arange(n) / SR; p = np.zeros(n)
        for f in pad:
            for d in (-.4, .4):
                ph = 2 * np.pi * (f + d) * tt; p += (np.sin(ph) + .3 * np.sin(2 * ph) + .15 * np.sin(3 * ph))
        p = lp(p / 12, 900) * np.minimum(1, tt / .4) * np.minimum(1, (bar_len - tt) / .4)
        o = int(t * SR); out[o:o + n] += p[:N - o] * .5
        # sub pulse on 8ths + ticking clock
        for k in range(8):
            tk = t + k * e8; ok = int(tk * SR)
            if ok >= N: break
            m = int(e8 * SR); s = np.sin(2 * np.pi * root * np.arange(m) / SR) * np.exp(-np.arange(m) / SR / .12)
            out[ok:ok + m] += s[:N - ok] * (.9 if k % 2 == 0 else .55)
            cl = hp(np.random.default_rng(k + bar * 8).standard_normal(int(.02 * SR)), 3000) * np.exp(-np.arange(int(.02 * SR)) / SR / .004)
            out[ok:ok + len(cl)] += cl[:N - ok] * (.35 if k % 2 == 0 else .18)
        t += bar_len; bar += 1
    # lift the energy for the money section, drop out under the book reveal, fade before the end
    tt = np.arange(N) / SR
    env = 1 + .35 * ((tt > 22) & (tt < 31.6)) - .5 * ((tt > 64.35) & (tt < 66.2))
    env *= np.clip((75.4 - tt) / 1.2, 0, 1)
    return np.stack([out * env, out * env], 1)


bus += score() * 10 ** (-19 / 20)

# duck the whole bus under Dan's speech
_, vo = wavfile.read(sys.argv[1]); vo = vo.astype(np.float64)
if np.max(np.abs(vo)) > 2: vo /= 32768.0
vm = np.abs(vo[:, 0] if vo.ndim > 1 else vo)[:N]; vm = np.pad(vm, (0, N - len(vm)))
k = int(.06 * SR); e = np.convolve(vm, np.ones(k) / k, 'same'); e /= e.max() or 1
bus *= (1 - .4 * np.clip(e * 4, 0, 1))[:, None]
bus = np.tanh(bus * 1.2) / np.tanh(1.2)
wavfile.write(sys.argv[2], SR, bus.astype(np.float32))
print('bus written', sys.argv[2])
