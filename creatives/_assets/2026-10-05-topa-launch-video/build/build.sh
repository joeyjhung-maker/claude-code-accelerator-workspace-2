#!/bin/zsh
# Full build: cues -> audio stems -> parallel frame render -> mux. usage: build/build.sh <out.mp4>   (AUDIO_ONLY=1 re-mixes the sound onto an existing render)  (needs NODE_PATH with puppeteer-core, PY with numpy/scipy)
set -e; setopt nullglob
B=${0:A:h}; OUT=${1:?out.mp4}; PY=${PY:-python3}; J=${JOBS:-4}
cd $B
node render.js cues cues.json
$PY - <<PYEOF
import json
d = json.load(open('cues.json')); L = json.load(open('words.json'))
first = lambda sec, k=0: L[[i for i, l in enumerate(L) if l['sec'] == sec][0] + k]
logo = [w['s'] for w in first('MECHANISM')['words'] if 'Topa' in w['w']][0] - .12
d['sections'] = {'s2': first('LEAD', 1)['s'], 's3': first('PROBLEM')['s'], 's4': first('MECHANISM')['s'] - .5, 'logo': logo, 's5': first('PROOF')['s'], 's6': first('HOW')['s'], 's7': first('OBJECTION')['s'], 's8': first('PRICE')['s'], 's9': first('CTA')['s'], 'end': L[-1]['e']}
json.dump(d, open('cues.json', 'w'))
PYEOF
$PY audio.py
lufs() { ffmpeg -hide_banner -i $1 -af ebur128 -f null - 2>&1 | grep -E "^\s+I:" | tail -1 | awk '{print $2}'; }
gv=$(printf "%.2f" $(( -16.0 - $(lufs ../vo.wav) ))); gs=$(printf "%.2f" $(( -25.0 - $(lufs sfx.wav) ))); gm=$(printf "%.2f" $(( -30.0 - $(lufs music.wav) )))
ffmpeg -y -loglevel error -i ../vo.wav -i sfx.wav -i music.wav -filter_complex "[0:a]volume=${gv}dB,pan=stereo|c0=c0|c1=c0[v];[1:a]volume=${gs}dB[s];[2:a]volume=${gm}dB[m];[v][s][m]amix=inputs=3:normalize=0[x]" -map "[x]" -ar 48000 mix-pre.wav
gx=$(printf "%.2f" $(( -14.0 - $(lufs mix-pre.wav) )))
ffmpeg -y -loglevel error -i mix-pre.wav -af "volume=${gx}dB,alimiter=limit=0.84:attack=5:release=60:level=false" -ar 48000 mix.wav
echo "gains: vo ${gv} sfx ${gs} music ${gm} master ${gx} -> $(lufs mix.wav) LUFS"
if [[ -n "$AUDIO_ONLY" ]]; then   # picture unchanged: swap the soundtrack on the existing file
  ffmpeg -y -loglevel error -i $OUT -i mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 256k -shortest -movflags +faststart ${OUT:r}.tmp.mp4 && mv ${OUT:r}.tmp.mp4 $OUT; echo "audio swapped on $OUT"; exit 0
fi
N=$($PY -c "import json;print(round(json.load(open('cues.json'))['dur']*30))"); per=$(( (N + J - 1) / J )); rm -f seg-*.mp4 segs.txt
for i in $(seq 0 $((J-1))); do node render.js video $((i*per)) $(( (i+1)*per )) seg-$i.mp4 & done; wait
for i in $(seq 0 $((J-1))); do echo "file 'seg-$i.mp4'" >> segs.txt; done
ffmpeg -y -loglevel error -f concat -safe 0 -i segs.txt -i mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 256k -shortest -movflags +faststart $OUT
rm -f seg-*.mp4 segs.txt; echo "done $OUT"
