"""Cut the animated clips to the voice-over timing (stills where a clip doesn't exist yet), add captions + mix. usage: python3 assemble.py out.mp4 [end_seconds]"""
import json, subprocess, sys, shutil
from pathlib import Path
B = Path(__file__).resolve().parent; A = B.parent; AN = A / 'animatic'; C = A / 'clips'; W, H, FPS = 1080, 1920, 30
T = json.loads((AN / 'timing.json').read_text())['frames']
seg = B / 'seg'; shutil.rmtree(seg, ignore_errors=True); seg.mkdir(); lst = []; used = []
for i, f in enumerate(T):
    n0, n1 = int(round(f['start'] * FPS)), int(round((f['start'] + f['len']) * FPS)); nfr = max(n1 - n0, 1); need = nfr / FPS
    out = seg / f's{i:02d}.mp4'; clip = C / f"c{f['frame']}.mp4"
    if clip.exists():
        d = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(clip)], capture_output=True, text=True).stdout)
        k = max(need / (d - 0.1), 1.0)          # only ever slow a clip down, never speed it up; short shots just use the start of the clip
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', str(clip), '-an', '-vf', f"setpts={k:.4f}*PTS,scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},format=yuv420p",
                        '-frames:v', str(nfr), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', str(out)], check=True)
        used.append((f['frame'], round(need, 1), round(k, 2)))
    else:
        shutil.copy(AN / 'seg' / f's{i:02d}.mp4', out)
    lst.append(f"file 'seg/{out.name}'")
(B / 'seg.txt').write_text('\n'.join(lst))
out = sys.argv[1]; end = sys.argv[2] if len(sys.argv) > 2 else None
cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', str(B / 'seg.txt'), '-f', 'concat', '-safe', '0', '-i', 'cap.txt', '-i', 'mix.wav',
       '-filter_complex', '[1:v]fps=30,format=rgba[c];[0:v][c]overlay=0:1150:eof_action=repeat,format=yuv420p[v]', '-map', '[v]', '-map', '2:a']
if end: cmd += ['-t', end]
cmd += ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '21', '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', str(Path(out).resolve())]
subprocess.run(cmd, check=True, cwd=AN)
print('animated shots:', len(used), '| slowed:', [(a, c) for a, b, c in used if c > 1.02])
