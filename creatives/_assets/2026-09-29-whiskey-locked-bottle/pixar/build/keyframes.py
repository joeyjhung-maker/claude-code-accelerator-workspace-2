"""Render every Pixar-version keyframe in parallel (KIE Nano Banana 2, character sheets as references)."""
import subprocess, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

REPO = Path(__file__).resolve().parents[5]
P = Path(__file__).resolve().parents[1]
S = {k: str(P / 'sheets' / f'{k}.png') for k in ['dan', 'ceo', 'leads', 'android', 'vault']}
ST = ("High-end 3D animated feature film still (Pixar / DreamWorks quality), cinematic lighting, broad slapstick "
      "cartoon acting with big exaggerated expressions, rich colour, crisp detail, 9:16 vertical. No text, no letters, no logos, no writing.")
DAN = "the cartoon man from the Dan reference (same face, grey trucker cap, white palm-leaf shirt)"
CEO = "the stuffy cartoon CEO from the CEO reference (silver hair, moustache, navy three-piece suit, red tie)"
VAULT = "the small glass-and-steel vault box with the big round chrome safe dial and the whisky bottle inside on blue velvet, from the vault reference"
LEADS = "the cute cartoon manila file-folder characters with little faces from the Old Leads reference"
BOT = "the cute cream-and-blue robot sidekick from the android reference"
SHOTS = [
 ('v01-slide', 'dan,vault', f"Low camera at the end of an absurdly long glossy boardroom table. {DAN} stands at the far end grinning cheekily, having just shoved {VAULT} down the table; the vault box slides toward the camera in the foreground, big and sharp, with speed streaks on the polished wood. Plush boardroom, city skyline windows."),
 ('v03-tower', 'vault', "Dramatic low-angle cartoon shot of an enormous gleaming glass corporate skyscraper at golden hour, towering and intimidating, with a tiny delivery trolley carrying the vault box from the reference rolling toward its grand entrance. Stylised city, big fluffy clouds."),
 ('v04-dial', 'ceo', f"{CEO} sits at his executive desk grudgingly dialling an old-fashioned rotary desk phone with one finger, holding a cream letter with a red wax seal in his other hand, one eyebrow raised, suspicious pout. Luxury office, city skyline."),
 ('v05-answer', 'dan', f"{DAN} leans back in a comfy chair with his feet up on a desk, answering a ringing phone instantly with a huge confident grin, as if he knew it would ring. Cosy warm office with plants and a window."),
 ('v06-archive', 'leads', f"A dark, cobwebbed, forgotten archive room with towering dusty shelves; in the middle {LEADS} are piled up fast asleep, snoring with bubbles from their noses, dust drifting in a beam of light. Funny and cute."),
 ('v07-wake', 'android,leads', f"{BOT} zooms into the dusty archive on a jet of light, beaming glowing blue chat-message bubbles at {LEADS}, who jolt awake with huge startled eyes, papers flying, dust exploding off them. Energetic slapstick moment."),
 ('v08-shake', 'dan,ceo', f"{DAN} and {CEO} shake hands across a boardroom table; Dan is pumping the handshake so vigorously that the CEO's whole body is wobbling, his hair flopping and his cheeks jiggling, eyes spinning. Big comedic squash-and-stretch."),
 ('v09-moneyrain', 'ceo,leads', f"In the CEO's office, {LEADS} are spraying and spitting out huge streams of green cash like fountains; money rains down everywhere, and {CEO} stands in the middle with his jaw literally dropped down to the desk, eyes bulging out. Maximum slapstick."),
 ('v10-open', 'ceo,dan,vault', f"The door of {VAULT} swings wide open with a golden glow; {CEO}, now beaming with delight and tears of joy, slides a gigantic oversized envelope across the desk toward {DAN}, who catches it with a wink. Warm golden light."),
 ('v11-army', 'leads', f"{LEADS}, now clean and polished, stand proudly in a neat line like a little army, saluting, chests puffed out, sparkling, in a bright tidy office. Adorable and funny."),
 ('v12-bulb', 'ceo', f"{CEO} has a moment of sudden realisation: a huge glowing lightbulb has literally popped on above his head, his eyes wide and sparkling, mouth open in an amazed 'O', hands in the air. Bright office."),
 ('v13-avalanche', 'ceo', f"{CEO} is buried up to his neck in a giant avalanche of paper files and folders in his office, only his head and one flailing arm sticking out, papers still tumbling down on him, overwhelmed expression."),
 ('v14-phones', 'leads', "A cartoon open-plan office at night with every desk empty and dozens of desk phones ringing and bouncing off their cradles with motion lines, nobody there to answer them, a lonely tumbleweed rolling across the carpet. Funny and melancholy."),
 ('v14b-pockets', 'ceo', f"{CEO} turns out his empty trouser pockets with a pleading hopeful face, and a single little moth flutters out of one pocket. Office background. Classic slapstick gag."),
 ('v15-globe', 'android', f"{BOT} rides on top of a giant cartoon Earth globe floating in space like surfing it, as hundreds of little golden lights and tiny shop icons pop on all across the continents. Joyful, sparkly, epic scale."),
 ('v16-poof', 'dan', f"A pointy purple wizard hat and robe on a stand vanish in a comic puff of smoke and sparkles, while {DAN} stands beside it shrugging casually with a smirk, holding up a single glowing smartphone in one hand. Simple clean office."),
 ('v17-magic', 'dan', f"{DAN} reaches into his shirt pocket like a magician about to reveal something, a burst of golden sparkles and light shooting out of the pocket, a knowing grin on his face, dramatic spotlight on a dark stage."),
 ('v17b-stage', '', "A glamorous warm golden spotlight shining down onto an empty velvet pedestal on a dark stage, sparkles and glitter drifting through the light beam, rich red velvet curtains either side. Leave the pedestal top empty and centred for a product to be placed."),
 ('v19-finale', 'dan,ceo,android,vault', f"Big celebration finale in the office: {VAULT} bursts open with confetti and streamers exploding everywhere, {CEO} dances with joy, {BOT} does a happy spin, and {DAN} in front tips his cap to the camera with a wink. Colourful confetti, golden light."),
]


def run(shot):
    name, refs, prompt = shot
    cmd = ['python3', 'scripts/run_image.py', f'{prompt} {ST}', '--model', 'nano-banana-2', '--aspect', '9:16', '--out', str(P / 'key' / f'{name}.png')]
    if refs:
        cmd += ['--ref', ','.join(S[r] for r in refs.split(','))]
    r = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True)
    return name, (r.stdout.strip() or r.stderr.strip().splitlines()[-1])


if __name__ == '__main__':
    only = set(sys.argv[1:])
    todo = [s for s in SHOTS if not only or s[0] in only]
    with ThreadPoolExecutor(10) as ex:
        for name, res in ex.map(run, todo):
            print(name, '->', res[-80:], flush=True)
