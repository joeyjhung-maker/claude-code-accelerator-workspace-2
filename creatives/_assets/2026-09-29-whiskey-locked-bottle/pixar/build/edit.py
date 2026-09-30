"""Cut the Pixar picture track to exactly 77.6s @30fps (all-intra for frame-accurate seeks).
Uses the lip-sync clip for Dan's refund line if it exists, otherwise falls back to the finale clip."""
import subprocess, sys
from pathlib import Path

P = Path(__file__).resolve().parents[1]; C = P / 'clips'
LIP = C / 'g20-lipsync.mp4'
# (clip, src_in, src_out, speed)
EDL = [
 ('h01-hero-slide', 0, 3.0, 1), ('h02-hero-dial', 0, 1.95, .975), ('v03-tower', 0, 2.7, 1), ('v04-dial', .5, 2.4, 1), ('v05-answer', .8, 2.4, 1),
 ('v06-archive', 0, 3.8, 1), ('v07-wake', 0, 3.4, 1), ('v08-shake', 0, 3.6, 1), ('v09-moneyrain', 0, 5.0, 1), ('h03-hero-reveal', 0, 2.2, 1), ('v10-open', 1.8, 4.2, 1),
 ('v11-army', 0, 5.65, 1), ('v12-bulb', 0, 6.0, 1), ('v13-avalanche', 0, 3.05, 1), ('v14-phones', 0, 2.6, 1), ('v14b-pockets', 1.0, 3.05, 1),
 ('v15-globe', 0, 6.0, 6.0 / 8.6), ('v16-poof', 0, 4.8, 1), ('v17-magic', 1.0, 2.85, 1), ('v17b-stage', 0, 5.35, 1),
 ('g20-lipsync', 0, 3.1, 1) if LIP.exists() else ('v05-answer', 2.5, 5.6, 1),
 ('h04-hero-finale', 0, 2.95, 1),
]
if not LIP.exists():
    print('!! lip-sync clip missing, using Dan-on-the-phone for the refund line', file=sys.stderr)
inputs, parts, t = [], [], 0.0
for i, (src, a, b, sp) in enumerate(EDL):
    t += (b - a) / sp
    inputs += ['-i', str(C / f'{src}.mp4')]
    parts.append(f"[{i}:v]trim={a}:{b},setpts=(PTS-STARTPTS)/{sp},scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1,format=yuv420p[v{i}]")
fc = ';'.join(parts) + ';' + ''.join(f'[v{i}]' for i in range(len(EDL))) + f'concat=n={len(EDL)}:v=1:a=0,trim=0:77.6[out]'
print('timeline', round(t, 3), file=sys.stderr)
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', *inputs, '-filter_complex', fc, '-map', '[out]', '-c:v', 'libx264', '-g', '1',
                '-crf', '16', '-preset', 'fast', '-pix_fmt', 'yuv420p', str(P / 'build' / 'base.mp4')], check=True)
