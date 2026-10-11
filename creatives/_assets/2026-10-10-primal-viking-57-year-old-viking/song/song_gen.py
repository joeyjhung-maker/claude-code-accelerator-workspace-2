"""Sung versions through KIE's Suno route (vocals + lyrics). usage: python3 song_gen.py  -> song-<name>-1.mp3 / -2.mp3"""
import sys, json, time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
B = Path(__file__).resolve().parent
sys.path.insert(0, str(B.parents[3] / 'scripts'))
from run_image import load_env, post_json, get_json, download, ENV_FILE
tok = load_env(ENV_FILE)['KIE_API_KEY']
GEN = "https://api.kie.ai/api/v1/generate"; REC = "https://api.kie.ai/api/v1/generate/record-info"; CREDIT = "https://api.kie.ai/api/v1/chat/credit"
LYRICS = (B / 'tab2-lyrics.txt').read_text()
NOREP = " Sing the lyrics exactly once, straight through, in order, with no chorus, no repeated lines, no added words and no long instrumental breaks."
OPTS = [
 ("FULL-A-sea-shanty", "Viking Shanty", "rowdy sea shanty drinking song, stomping and clapping on every beat, gruff older male lead vocal in his fifties, deep and gravelly, group of men shouting the ends of lines, fiddle and bodhran, 120 bpm, every word clearly sung and easy to understand, storytelling, humorous." + NOREP),
 ("FULL-C-trap-talk", "Viking Bars", "hard-hitting hip-hop beat with heavy 808s and war drums, deep older male voice rapping in a clear confident talk-rap flow, low Nordic choir hits and horn stabs, 128 bpm, punchy, every word clearly enunciated, swagger and humor." + NOREP),
]
def run(o):
    name, title, style = o
    body = {"prompt": LYRICS, "customMode": True, "instrumental": False, "model": "V4_5", "style": style, "title": title, "callBackUrl": "https://example.com/none"}
    try: r = post_json(GEN, body, tok)
    except Exception as e: return name, 'create error ' + str(e)[:200]
    tid = (r.get('data') or {}).get('taskId')
    if not tid: return name, 'create failed ' + json.dumps(r)[:300]
    t0 = time.time()
    while time.time() - t0 < 560:
        time.sleep(10)
        try: d = get_json(f"{REC}?taskId={tid}", tok).get('data') or {}
        except Exception: continue
        st = d.get('status')
        if st == 'SUCCESS':
            out = []
            for i, t in enumerate(((d.get('response') or {}).get('sunoData')) or [], 1):
                u = t.get('audioUrl') or t.get('audio_url') or t.get('sourceAudioUrl')
                if u: download(u, str(B / f'song-{name}-{i}.mp3')); out.append(f"{t.get('duration')}s")
            return name, 'ok ' + ', '.join(out)
        if st and ('FAIL' in st or 'ERROR' in st or 'SENSITIVE' in st): return name, f'failed {st}: {d.get("errorMessage")}'
    return name, 'timeout, task ' + tid
if __name__ == '__main__':
    print('credits before:', get_json(CREDIT, tok).get('data'), flush=True)
    with ThreadPoolExecutor(3) as ex:
        for n, m in ex.map(run, OPTS): print(n, m, flush=True)
    print('credits after:', get_json(CREDIT, tok).get('data'))
