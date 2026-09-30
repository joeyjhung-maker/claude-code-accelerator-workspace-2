"""Assemble the heist picture track (no audio) to exactly 77.6s @30fps, all-intra for fast frame seeks."""
import subprocess, sys
C = 'clips/'; ORIG = '/Users/joey/Downloads/Whiskey Bottle Ad.mp4'
# (source, in, out, speed, kind)   timeline = running sum of (out-in)/speed
EDL = [
 ('c01-bottle',0,3.0,1,''),('c02-dials',.5,2.5,1,''),('c03-tower',0,2.7,1,''),('c04-seal',.3,2.2,1,''),('c05-phone',3.0,4.6,1,''),
 ('c06-archive',0,3.8,1,''),('c07-phone',0,3.4,1,''),('c08-handshake',.3,3.0,1,''),('DAN',21.1,22.0,1,'dan'),
 ('c09-cash',0,5.0,1,''),('c10-thankyou',0,4.6,1,''),('c11-drawer',0,5.65,1,''),('c12-window',0,6.0,1,''),
 ('c13-empty',0,4.35,1,''),('c06-archive',2.6,5.95,1,''),('c14-aerial',0,6.0,6.0/8.6,''),('c15-simple',0,4.8,1,''),
 ('c16-bookset',0,6.0,6.0/7.05,''),('DAN',71.4,75.55,1,'dan'),('c17-lockopen',3.0,5.05,1,'rev'),
]
inputs, parts, t = [], [], 0.0
for i,(src,a,b,sp,kind) in enumerate(EDL):
    dur=(b-a)/sp; t+=dur
    inputs += ['-i', ORIG if src=='DAN' else C+src+'.mp4']
    if kind=='dan':
        f=(f"[{i}:v]trim={a}:{b},setpts=PTS-STARTPTS,crop=1260:2240:450:0,scale=1080:1920:flags=lanczos,"
           "colorbalance=rs=-.04:gs=-.01:bs=.06:rh=.07:gh=.02:bh=-.05,eq=contrast=1.07:saturation=.88:brightness=-.02,vignette=PI/5")
    elif kind=='rev':
        f=f"[{i}:v]reverse,trim={a}:{b},setpts=PTS-STARTPTS,scale=1080:1920"
    else:
        f=f"[{i}:v]trim={a}:{b},setpts=(PTS-STARTPTS)/{sp},scale=1080:1920"
    parts.append(f+f",fps=30,setsar=1,format=yuv420p[v{i}]")
fc=';'.join(parts)+';'+''.join(f'[v{i}]' for i in range(len(EDL)))+f'concat=n={len(EDL)}:v=1:a=0,trim=0:77.6[out]'
print('timeline total', round(t,3), file=sys.stderr)
subprocess.run(['ffmpeg','-y','-loglevel','error',*inputs,'-filter_complex',fc,'-map','[out]','-c:v','libx264','-g','1','-crf','16','-preset','fast','-pix_fmt','yuv420p','build/base.mp4'],check=True)
