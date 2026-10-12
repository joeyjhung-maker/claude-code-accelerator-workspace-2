"""Sung version of a replacement hook only, same shanty style as the full song, through KIE's Suno route.
usage: python3 hook_gen.py  -> hook-v2-sea-shanty-1.mp3 / -2.mp3 (+ hook-v2-task.json, kept so the take can be extended later)"""
import sys, json, time
from pathlib import Path
B = Path(__file__).resolve().parent
sys.path.insert(0, str(B.parents[3] / 'scripts'))
from run_image import load_env, post_json, get_json, download, ENV_FILE
tok = load_env(ENV_FILE)['KIE_API_KEY']
GEN = "https://api.kie.ai/api/v1/generate"; REC = "https://api.kie.ai/api/v1/generate/record-info"; CREDIT = "https://api.kie.ai/api/v1/chat/credit"
LYRICS = (B / 'hook-v2-lyrics.txt').read_text()
NOREP = " Sing the lyrics exactly once, straight through, in order, with no chorus, no repeated lines, no added words and no long instrumental breaks."
STYLE = "rowdy sea shanty drinking song, stomping and clapping on every beat, gruff older male lead vocal in his fifties, deep and gravelly, group of men shouting the ends of lines, fiddle and bodhran, 120 bpm, every word clearly sung and easy to understand, storytelling, humorous." + NOREP
if __name__ == '__main__':
    print('credits before:', get_json(CREDIT, tok).get('data'), flush=True)
    body = {"prompt": LYRICS, "customMode": True, "instrumental": False, "model": "V4_5", "style": STYLE, "title": "Viking Shanty", "callBackUrl": "https://example.com/none"}
    r = post_json(GEN, body, tok); tid = (r.get('data') or {}).get('taskId')
    if not tid: sys.exit('create failed ' + json.dumps(r)[:300])
    print('task', tid, flush=True); t0 = time.time()
    while time.time() - t0 < 560:
        time.sleep(10)
        try: d = get_json(f"{REC}?taskId={tid}", tok).get('data') or {}
        except Exception: continue
        st = d.get('status')
        if st == 'SUCCESS':
            tracks = ((d.get('response') or {}).get('sunoData')) or []
            (B / 'hook-v2-task.json').write_text(json.dumps({'taskId': tid, 'tracks': [{'id': t.get('id'), 'duration': t.get('duration')} for t in tracks]}, indent=1))
            for i, t in enumerate(tracks, 1):
                u = t.get('audioUrl') or t.get('audio_url') or t.get('sourceAudioUrl')
                if u: download(u, str(B / f'hook-v2-sea-shanty-{i}.mp3')); print(f'take {i}: {t.get("duration")}s', flush=True)
            break
        if st and ('FAIL' in st or 'ERROR' in st or 'SENSITIVE' in st): sys.exit(f'failed {st}: {d.get("errorMessage")}')
    else: sys.exit('timeout, task ' + tid)
    print('credits after:', get_json(CREDIT, tok).get('data'))
