"""Voice samples for the Primal Viking VO. usage: python3 samples.py  -> sample-*.wav next to this file."""
import sys, json, time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
B = Path(__file__).resolve().parent
sys.path.insert(0, str(B.parents[3] / 'scripts'))
from run_image import load_env, post_json, get_json, download, ENV_FILE, CREATE_URL, POLL_URL
TEXT = ("A fifty-two-year-old Viking rowing for days through frigid open water, hauling blood-crusted axes up jagged shoreline, could easily fight hand to hand against men half his age and conquer nations. "
        "But today, that same fifty-two-year-old modern man needs ibuprofen to get out of bed. "
        "The difference wasn't genetics. It was what they ate.")
BRIEF = ("A male narrator in his forties or fifties tells a tall tale about Vikings with a dry sense of humour, like a man telling a story at a bar. Deep, warm, slightly gravelly, confident and unhurried but never slow. "
         "He leans on the vivid words, and drops to a deadpan for the punchline about ibuprofen. Not a movie-trailer voice, not a hype announcer, not an advert read. ")
BRIEF = ("A male narrator in his fifties tells a tall tale about Vikings with a dry sense of humour, like a man telling a story at a bar. Deep, firm, confident, deadpan. "
         "He talks briskly and keeps the story moving at a quick conversational clip, short pauses only, never dragging. He drops to a deadpan for the punchline about ibuprofen. "
         "Not a movie-trailer voice, not a hype announcer. ")
S = [("C-brisk-take", "Orus", "American (Gen)", "Firm confident American man, deadpan, talks briskly.", "Natural"),
     ("C-rapid-take", "Orus", "American (Gen)", "Firm confident American man, deadpan, talks fast.", "Rapid Fire")]
tok = load_env(ENV_FILE)['KIE_API_KEY']
def run(s):
    name, voice, accent, prof, pace = s
    sp = {"speaker_id": "Speaker 1", "voice_name": voice, "audio_profile": prof, "style": "Vocal Smile", "pace": pace}
    if accent: sp["accent"] = accent
    scene = "A quiet voice-over booth. " + BRIEF + ("" if accent else "He is English with an everyday neutral British accent, not posh, not cockney.")
    inp = {"temperature": 1, "scene": scene, "sample_context": BRIEF, "speakers": [sp], "dialogue_turns": [{"speaker_id": "Speaker 1", "text": TEXT}]}
    r = post_json(CREATE_URL, {"model": 'google/gemini-3-1-flash-tts', "input": inp}, tok)
    tid = (r.get('data') or {}).get('taskId')
    if not tid: return name, 'create failed: ' + json.dumps(r)[:300]
    t0 = time.time()
    while True:
        time.sleep(6); rec = get_json(f"{POLL_URL}?taskId={tid}", tok).get('data') or {}; st = rec.get('state')
        if st == 'success':
            url = (json.loads(rec.get('resultJson') or '{}').get('resultUrls') or [None])[0]
            n = download(url, str(B / f'sample-{name}.wav')); return name, f'ok {n} bytes, {rec.get("creditsConsumed")} credits'
        if st in ('fail', 'failed', 'error') or time.time() - t0 > 600: return name, f'failed: {rec.get("failMsg")}'
S = [s for s in S if not (B / f"sample-{s[0]}.wav").exists()]
with ThreadPoolExecutor(5) as ex:
    for n, m in ex.map(run, S): print(n, m, flush=True)
