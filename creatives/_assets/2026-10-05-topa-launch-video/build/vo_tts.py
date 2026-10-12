"""Voice the script in ../captions.txt through KIE's Gemini TTS, one call per chunk of sections (each call caps at ~80s of audio).
usage: python vo_tts.py [chunk numbers...]   -> vo-c1.wav ... next to this file. Then run vo_assemble.py and align.py --stt."""
import sys, json, time, re
from pathlib import Path
B = Path(__file__).resolve().parent
sys.path.insert(0, str(B.parents[3] / 'scripts'))
from run_image import load_env, post_json, get_json, download, ENV_FILE, CREATE_URL, POLL_URL
VOICE = 'Zubenelgenubi'   # picked blind from voice-samples/ (I can't hear them). No accent preset: 'British (RP)' was too posh for Joey.
BRIEF = ("He is English and speaks with an ordinary, modern, neutral British accent: the everyday voice of a normal bloke from the south-east or the Midlands who runs his own business. "
         "Definitely NOT posh, not Received Pronunciation, not a newsreader, not plummy. Also not cockney, not street, not a geezer. Relaxed vowels, friendly, straight-talking, "
         "sounds like he is explaining it to a mate over a pint. He talks quickly and keeps it moving, with short pauses, and the same energy from the first line to the last.")
CHUNKS = [['HOOK', 'LEAD'], ['PROBLEM'], ['TURN', 'MECHANISM'], ['PROOF', 'HOW'], ['DATABASE'], ['OBJECTION', 'PRICE', 'CTA']]   # keep each under ~45s: long chunks drop their last lines
SAY = [('$250k to $1m+ deals', 'two hundred and fifty K to one million dollar plus deals'), (' DM ', ' D M '), ('350 million+', 'three hundred and fifty million plus'), ('10,000', 'ten thousand'),
       ('30 people', 'thirty people'), ('22 replied', 'twenty-two replied'), ('73%', 'seventy-three percent'), ('12 new', 'twelve new'), ('11 of those 12', 'eleven of those twelve'), ('92%', 'ninety-two percent'), ('350 million potential', 'three hundred and fifty million potential'), ('15 connection', 'fifteen connection'), ('20 messages', 'twenty messages'),
       ('$79 a month', 'seventy-nine dollars a month'), ('$99 for two', 'ninety-nine for two'), ('$100 a month', 'a hundred dollars a month'), ('topa.io', 'Topa dot I O'),
       ('DMs', 'D Ms'), (' IP ', ' I P '), ('AI helper', 'A I helper'), ('…', ','), ('"', '')]
sec, text = None, {}
for row in (B.parent / 'captions.txt').read_text().splitlines():
    row = row.strip()
    if not row or row.startswith('#'): continue
    if row.startswith('['): sec = row.strip('[]'); continue
    t = row.replace(' | ', ' ')
    for a, b in SAY: t = t.replace(a, b)
    text[sec] = (text.get(sec, '') + ' ' + t).strip()
tok = load_env(ENV_FILE)['KIE_API_KEY']
for n in [int(a) for a in sys.argv[1:]] or range(1, len(CHUNKS) + 1):
    inp = {"temperature": 1,
           "scene": "A small, informal voice-over booth. A down-to-earth English business owner records a fast, friendly explainer for a software launch called Topa (pronounced TOE-pah). " + BRIEF,
           "sample_context": "Fast, conversational, down-to-earth British narration. " + BRIEF,
           "speakers": [{"speaker_id": "Speaker 1", "voice_name": VOICE, "audio_profile": "Ordinary English bloke in his thirties, neutral everyday British accent, not posh, not cockney, talks fast.", "style": "Vocal Smile", "pace": "Natural"}],
           "dialogue_turns": [{"speaker_id": "Speaker 1", "text": ' '.join(text[s] for s in CHUNKS[n - 1])}]}
    r = post_json(CREATE_URL, {"model": 'google/gemini-3-1-flash-tts', "input": inp}, tok)
    tid = (r.get('data') or {}).get('taskId')
    if not tid: sys.exit('create failed: ' + json.dumps(r)[:600])
    t0 = time.time()
    while True:
        time.sleep(6); rec = get_json(f"{POLL_URL}?taskId={tid}", tok).get('data') or {}; st = rec.get('state')
        if st == 'success':
            url = (json.loads(rec.get('resultJson') or '{}').get('resultUrls') or [None])[0]
            print(f'chunk {n}:', download(url, str(B / f'vo-c{n}.wav')), 'bytes,', rec.get('creditsConsumed'), 'credits', flush=True); break
        if st in ('fail', 'failed', 'error') or time.time() - t0 > 900: sys.exit(f'chunk {n} failed: {rec.get("failMsg")}')
    time.sleep(3)
