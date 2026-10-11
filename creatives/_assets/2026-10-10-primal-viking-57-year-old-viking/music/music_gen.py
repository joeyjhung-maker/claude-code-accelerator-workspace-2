"""Instrumental music options through KIE's Suno route. usage: python3 music_gen.py  -> music-<name>-1.mp3 / -2.mp3"""
import sys, json, time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
B = Path(__file__).resolve().parent
sys.path.insert(0, str(B.parents[3] / 'scripts'))
from run_image import load_env, post_json, get_json, download, ENV_FILE
tok = load_env(ENV_FILE)['KIE_API_KEY']
GEN = "https://api.kie.ai/api/v1/generate"; REC = "https://api.kie.ai/api/v1/generate/record-info"
OPTS = [
 ("A-nordic-swagger", "Nordic Folk Swagger", "instrumental, cinematic Nordic folk, deep frame drums and war drums at a steady mid-tempo march, low tagelharpa and bowed lyre drone, distant horn calls, sparse and spacious, dry confident swagger with a wink, no vocals, no choir, leaves room for a deep male narrator, slow build to a triumphant finish"),
 ("B-tall-tale", "Tall Tale", "instrumental, playful adventurous storytelling score, plucked strings and hand percussion with a light Viking folk flavour, bouncy mid-tempo, mischievous and warm, small drums and a low drone, occasional horn stab, no vocals, understated underscore for a narrator, grows bigger and heroic in the final third"),
 ("C-epic-understated", "Quiet Conqueror", "instrumental, restrained epic underscore, slow heavy drum pulse like oars, deep sub drone, low brass swells, sparse metallic hits, serious and cinematic but minimal, no melody fighting a voice-over, no vocals, no choir, steady build across four minutes to a big heroic ending"),
]
def run(o):
    name, title, style = o
    body = {"prompt": "", "customMode": True, "instrumental": True, "model": "V4_5", "style": style, "title": title, "callBackUrl": "https://example.com/none"}
    try:
        r = post_json(GEN, body, tok)
    except Exception as e:
        return name, 'create error ' + str(e)[:200]
    tid = (r.get('data') or {}).get('taskId')
    if not tid: return name, 'create failed ' + json.dumps(r)[:300]
    t0 = time.time()
    while time.time() - t0 < 540:
        time.sleep(10)
        try: d = get_json(f"{REC}?taskId={tid}", tok).get('data') or {}
        except Exception as e: continue
        st = d.get('status')
        if st in ('SUCCESS', 'FIRST_SUCCESS') and st == 'SUCCESS':
            tracks = ((d.get('response') or {}).get('sunoData')) or []
            out = []
            for i, t in enumerate(tracks, 1):
                u = t.get('audioUrl') or t.get('audio_url') or t.get('sourceAudioUrl')
                if u: download(u, str(B / f'music-{name}-{i}.mp3')); out.append(f"{t.get('duration')}s")
            return name, 'ok ' + ', '.join(out)
        if st and ('FAIL' in st or 'ERROR' in st): return name, f'failed {st}: {d.get("errorMessage")}'
    return name, 'timeout, task ' + tid
with ThreadPoolExecutor(3) as ex:
    for n, m in ex.map(run, OPTS): print(n, m, flush=True)
