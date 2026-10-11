"""Voice the Primal Viking script through KIE Gemini TTS in voice C (Orus, American Gen), one call per chunk.
usage: python3 vo_tts.py [chunk numbers...] -> vo-c01.wav ... Then vo_check.py (venv python) verifies and assembles."""
import sys, json, time, re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
B = Path(__file__).resolve().parent
sys.path.insert(0, str(B.parents[3] / 'scripts'))
from run_image import load_env, post_json, get_json, download, ENV_FILE, CREATE_URL, POLL_URL
SCRIPT = (B.parents[3] / 'copy' / '2026-10-10-primal-viking-spec-57-year-old-viking.md').read_text().split('\n---\n', 2)[-1]
LINES = [l.strip() for l in SCRIPT.splitlines() if l.strip()]
SAY = [('52-year-old', 'fifty-two-year-old'), ('next 60 seconds', 'next sixty seconds'), ('5,000 km', 'five thousand kilometers'), ('minus-40', 'minus forty'), ('3pm', 'three P M'),
       ('157,579', 'one hundred and fifty-seven thousand, five hundred and seventy-nine'), ('60% off', 'sixty percent off'), ('30-day 100% money-back', 'thirty-day, one hundred percent money-back'),
       ('at 52.', 'at fifty-two.'), ('WHOLE', 'whole'), ('WANTED', 'wanted'), ('B vitamins', 'B vitamins'), ('CoQ10', 'co Q ten'), ('…', ', '), ('’', "'")]
def spoken(t):
    for a, b in SAY: t = t.replace(a, b)
    return re.sub(r'\s+', ' ', t).strip()
MAXW = 80   # voice C reads ~127 wpm raw; keep each call under ~40s so nothing gets dropped
FORCE_BREAK_AFTER = {2, 5, 8}   # line indexes: after the hook, and after the three-line promise, so the promise is voiced as ONE take
CH, cur = [], []
for i, l in enumerate(LINES):
    ends_open = cur and cur[-1].rstrip().endswith('…')          # never break a chunk after a line that trails off into the next
    if cur and not ends_open and sum(len(x.split()) for x in cur) + len(l.split()) > MAXW: CH.append(cur); cur = []
    cur.append(l)
    if i in FORCE_BREAK_AFTER: CH.append(cur); cur = []
if cur: CH.append(cur)
def join(lines):
    out = ''
    for l in lines:
        if out.rstrip().endswith('…'): l = l[0].lower() + l[1:]   # a line after an ellipsis continues the same sentence
        out += (' ' if out else '') + l
    return out
(B / 'chunks.json').write_text(json.dumps([{'n': i + 1, 'lines': c, 'spoken': spoken(join(c))} for i, c in enumerate(CH)], indent=1, ensure_ascii=False))
BRIEF = ("A male narrator in his forties or fifties tells a tall tale about Vikings with a dry sense of humour, like a man telling a story at a bar. Deep, warm, slightly gravelly, confident and unhurried but never slow. "
         "He leans on the vivid words, and drops to a deadpan for the punchlines. Not a movie-trailer voice, not a hype announcer, not an advert read. The same voice, energy and distance from the microphone from the first line to the last. ")
tok = load_env(ENV_FILE)['KIE_API_KEY']
def run(n):
    text = spoken(join(CH[n - 1]))
    note = "This passage is ONE long flowing sentence listing three things he is about to show you. Do not stop or restart between them: carry straight through the commas, and let the words why and and how continue the same breath and the same thought, building gently to the end. " if any(x.rstrip().endswith("…") for x in CH[n - 1][:-1]) else ""
    inp = {"temperature": 1, "scene": "A quiet voice-over booth. " + BRIEF + note, "sample_context": BRIEF,
           "speakers": [{"speaker_id": "Speaker 1", "voice_name": "Orus", "accent": "American (Gen)", "audio_profile": "Firm confident American man, deadpan delivery.", "style": "Vocal Smile", "pace": "Natural"}],
           "dialogue_turns": [{"speaker_id": "Speaker 1", "text": text}]}
    for attempt in range(3):
        try:
            r = post_json(CREATE_URL, {"model": 'google/gemini-3-1-flash-tts', "input": inp}, tok)
            tid = (r.get('data') or {}).get('taskId')
            if not tid: last = 'create failed ' + json.dumps(r)[:200]; continue
            t0 = time.time()
            while True:
                time.sleep(6); rec = get_json(f"{POLL_URL}?taskId={tid}", tok).get('data') or {}; st = rec.get('state')
                if st == 'success':
                    url = (json.loads(rec.get('resultJson') or '{}').get('resultUrls') or [None])[0]
                    return n, f'ok {download(url, str(B / f"vo-c{n:02d}.wav"))} bytes, {rec.get("creditsConsumed")} credits, {len(text.split())} words'
                if st in ('fail', 'failed', 'error') or time.time() - t0 > 600: last = f'failed: {rec.get("failMsg")}'; break
        except Exception as e:
            last = 'error ' + str(e)[:120]
    return n, last
todo = [int(a) for a in sys.argv[1:]] or list(range(1, len(CH) + 1))
print(len(CH), 'chunks,', sum(len(l.split()) for l in LINES), 'words', flush=True)
with ThreadPoolExecutor(4) as ex:
    for n, m in ex.map(run, todo): print('chunk', n, m, flush=True)
