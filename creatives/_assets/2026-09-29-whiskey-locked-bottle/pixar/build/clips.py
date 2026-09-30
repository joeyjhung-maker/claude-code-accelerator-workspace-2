"""Animate every Pixar keyframe with Veo 3.1 in parallel (6s clips; 4s costs the same)."""
import subprocess, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

REPO = Path(__file__).resolve().parents[5]
P = Path(__file__).resolve().parents[1]
STYLE = "3D animated Pixar-style shot, snappy bouncy cartoon timing, exaggerated squash-and-stretch slapstick acting. Keep the characters on-model. No text, no captions."
MOTION = {
 'v01-slide': "The vault box slides fast down the glossy table straight at the camera and skids to a stop right in front of the lens with a wobble; at the far end the man throws his arms up and grins proudly.",
 'lockB-vault': "The CEO frantically cranks the big safe dial faster and faster, face going red, sweat droplets flying, hair springing loose, then he slams both fists on the vault in frustration and it bounces.",
 'v03-tower': "The camera tilts up the enormous gleaming skyscraper toward the clouds as the tiny delivery man wheels the vault trolley toward the entrance, sunlight flaring off the glass.",
 'v04-dial': "The suspicious CEO spins the rotary dial with one finger, it whirrs back, he glances at the letter and raises one eyebrow even higher, then lifts the handset to his ear.",
 'v05-answer': "The phone rings once and the man snatches it up instantly, feet still on the desk, with a huge cheeky grin and a little laugh, waving his free hand.",
 'v06-archive': "The file-folder characters snore, their little bellies rising and falling, snot bubbles inflating and popping, dust motes floating in the light beam.",
 'v07-wake': "The robot zooms in and fires glowing blue message bubbles; the folders leap into the air startled, eyes huge, dust exploding off them, papers flying everywhere.",
 'v08-shake': "The man pumps the handshake so hard the CEO's whole body wobbles like jelly, his hair flopping and cheeks jiggling, eyes spinning, both laughing.",
 'v09-moneyrain': "The folders spray fountains of green cash into the air, money rains down all over the office, and the CEO's jaw drops down onto the desk with a clunk as his eyes pop out.",
 'v10-open': "The vault door swings open with golden light pouring out; the beaming CEO slides the giant envelope across the desk and the man catches it and winks.",
 'v11-army': "The polished folder characters march into a neat line and snap a proud salute in unison, chests puffing out, sparkles twinkling.",
 'v12-bulb': "The lightbulb above the CEO's head flickers then blazes on brightly; his eyes go wide and sparkly and he throws his hands up in amazement.",
 'v13-avalanche': "More papers and folders keep tumbling down onto the buried CEO; he flails one arm and spits out a sheet of paper, overwhelmed.",
 'v14-phones': "All the desk phones ring and bounce off their cradles in the empty office while the tumbleweed rolls slowly across the carpet.",
 'v14b-pockets': "The CEO pulls his empty pockets inside out with a hopeful pleading face and a little moth flutters out and away past his nose; he blinks.",
 'v15-globe': "The robot surfs happily on top of the spinning globe as hundreds of little golden lights pop on one after another across the continents, sparkles swirling.",
 'v16-poof': "The wizard hat and robe vanish in a comic puff of purple smoke and sparkles; the man shrugs casually and holds up the glowing phone with a smirk.",
 'v17-magic': "The man reaches into his shirt pocket like a magician and golden sparkles and light burst out of it, he grins knowingly at the camera.",
 'v17b-stage': "The golden spotlight shimmers and glitter drifts slowly down through the light beam onto the empty velvet pedestal; the curtains sway gently.",
 'v19-finale': "The vault bursts open and confetti and streamers explode everywhere; the CEO dances, the robot spins happily, and the man tips his cap to the camera and winks.",
}


def run(name):
    out = P / 'clips' / f'{name}.mp4'
    if out.exists() and out.stat().st_size > 100000:
        return name, 'exists'
    cmd = ['python3', 'scripts/run_video.py', f'{MOTION[name]} {STYLE}', '--image', str(P / 'key' / f'{name}.png'), '--duration', '6', '--out', str(out)]
    r = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True)
    log = (r.stderr or '') + (r.stdout or '')
    (P / 'clips' / f'log-{name}.txt').write_text(log)
    return name, log.strip().splitlines()[-1][-90:] if log.strip() else 'no output'


if __name__ == '__main__':
    names = sys.argv[1:] or list(MOTION)
    with ThreadPoolExecutor(10) as ex:
        for name, res in ex.map(run, names):
            print(name, '->', res, flush=True)
