"""Animate the storyboard stills with Veo 3.1 (image-to-video). usage: python3 clips.py 01 02 ...   (no args = all). Skips clips that already exist."""
import subprocess, sys, json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
REPO = Path(__file__).resolve().parents[4]; A = Path(__file__).resolve().parents[1]; C = A / 'clips'
STYLE = "3D animated Pixar-style shot, smooth expressive character animation with snappy comic timing. Keep the characters exactly on-model: the Viking is always bare-headed with long grey hair, he never wears a helmet or horns. No text, no captions, no subtitles, no logos, no speech."
T = {f['frame']: f['len'] for f in json.loads((A / 'animatic' / 'timing.json').read_text())['frames']}
MOTION = {
 '01': "The Viking rows hard and steadily, hauling the oars in a strong rhythm as the longship crashes through heavy grey waves, spray bursting over the bow, the crew rowing in time behind him, camera pushing in on his unbothered face.",
 '02': "The Viking strides out of the surf up the black rocks dragging the two heavy axes, water streaming off him, breath steaming, the camera tracking backwards in front of him.",
 '03': "A playful cartoon tussle: the big Viking calmly holds the young warrior at arm's length with one hand on his forehead while the young man swings his arms and cannot reach him; the Viking looks bored, yawns, and glances at the camera.",
 '04': "The modern man winces and rubs his lower back, slowly reaches for the pill bottle on the nightstand, shakes it, and sighs with his shoulders slumping.",
 '05': "The two men stand side by side; the Viking looks the modern man up and down and slowly shakes his head, the modern man shrugs sheepishly and takes a sip from his can.",
 '06': "The Viking slowly begins to lift the lid of the glowing platter, golden light spilling out and flickering across his face, he glances at the camera with a knowing raised eyebrow, then lowers the lid again.",
 '07': "The modern man sleeps face down on the desk, his back rising and falling as he snores, a coffee cup wobbles, the second hand of the wall clock ticks, he jolts slightly and settles again.",
 '08': "The modern man blows dust off one of the supplement bottles, a cloud of dust puffs up, he coughs and waves it away, a spider scuttles across the bottles, he sighs.",
 '09': "The Viking leans into the rope and drags the longship up the icy beach step by step, snow blasting sideways across the frame, his cloak whipping in the wind.",
 '10': "The Viking leans closer to the plate, sniffs the pale chicken breast, recoils in disgust and glares; the modern man lowers his fork and looks away, embarrassed.",
 '11': "The Viking proudly lifts the wooden board of meat toward the camera, firelight flickering, steam rising from the cuts, sparks drifting up from the campfire, he nods with satisfaction.",
 '12': "The cow chews slowly with half-closed eyes, blinks, flicks an ear at a fly and keeps chewing.",
 '13': "The reindeer lifts its head proudly, breath steaming, the aurora rippling across the sky behind it, wind ruffling its fur.",
 '14': "The cow eats lazily from the trough without moving its body, the cows behind stand motionless, one slowly blinks.",
 '15': "The reindeer herd charges straight at the camera through the blizzard, snow exploding under their hooves, the lead bull pounding forward with antlers lowered.",
 '16': "On the left the Viking tears a big bite from the meat and chews with gusto as the fire crackles; on the right the modern man takes a slow sad bite of the floppy burger.",
 '17': "The modern man looks down at his empty basket, then at the empty tray in the chilled counter, scratches his head, and shrugs.",
 '18': "The modern man sits deadpan in sunglasses, the can rising and falling on his stomach as he breathes; above him the gauge needles twitch and drop to empty and the red warning lights blink.",
 '19': "The modern man holds the single capsule up to the light, squints at it hopefully, crosses his fingers tighter, and gives a nervous little smile.",
 '20': "The modern man tosses a log onto a completely dead, cold campfire. The fire never lights: there are no flames, no glow, no embers and no sparks at any point, only thin grey smoke and a puff of grey ash that rises and drifts away. He waits, leans in, and frowns at the cold grey ash.",
 '21': "The Viking places one more piece of wood and the fire roars up brightly, sparks swirling into the night, warm light growing across his satisfied face.",
 '22': "The Viking bites the slice of liver and chews; glowing red-gold particles flow from the meat down through him and race along his arms as he grips the oar and pulls with fresh strength, the spirit reindeer shimmering behind.",
 '23': "The Viking holds the roasted heart high; golden particles stream from it into his body and the flames in his belly flare brighter, the spirit reindeer behind him tosses its antlers, snow drifting.",
 '24': "The Viking strolls forward whistling innocently, swinging the skewer; the bearded villagers all turn their identical faces to watch him pass, a bearded baby waves.",
 '25': "The Viking thrusts his sword toward the distant coast, cloak billowing, the longship surging forward through the water, the ships behind following, he roars.",
 '26': "The Viking holds up the glowing golden-root plant, it pulses with light, he turns it in his fingers, then looks at the camera and gives a slow wink.",
 '37': "The Viking brings the axe down in a huge swing, the wooden shield bursts into flying splinters, the two enemy warriors tumble away in a panic, snow spraying.",
 '38': "The Viking leans back with a smug grin and wiggles his eyebrows at the camera; his wife fans herself faster and giggles, the candle flames flicker.",
 '27': "The modern man looks from his tiny butter knife to the enormous reindeer on the counter and back again, gulps, and the toaster pops.",
 '29': "The modern man types fast and energetically, pushes the coffee cup away with one hand, glances at the wall clock and grins; the colleagues behind stay slumped asleep.",
 '30': "The modern man grips the barbell and deadlifts it off the floor with a determined roar, holds it at the top, chalk dust drifting, then sets it down with a nod.",
 '31': "The modern man pulls his belt one notch tighter, looks down at his stomach, looks up at the mirror with raised eyebrows, and breaks into a pleased grin.",
 '32': "The modern man strolls through the kitchen sipping his water, chest out; his wife's eyes go wide, she does a double take and nearly spills her coffee, he walks on without noticing.",
 '33': "The modern man pumps his raised fist and roars; behind him the huge crowd of men raise their fists and cheer in a wave.",
 '36': "The Viking and the modern man stride confidently toward the camera in step, the office workers' heads turning to follow them, papers fluttering in their wake, both grinning.",
}
def run(n):
    out = C / f'c{n}.mp4'
    if out.exists() and out.stat().st_size > 100000: return n, 'exists'
    dur = 8   # same price as 6s, and the song cut stretches each clip over a longer span
    last = ''
    for d in ([dur, 6] if dur == 8 else [6]):
        cmd = ['python3', 'scripts/run_video.py', f'{MOTION[n]} {STYLE}', '--image', str(A / 'storyboard' / f'f{n}.png'), '--duration', str(d), '--out', str(out)]
        r = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True)
        log = (r.stderr or '') + (r.stdout or ''); (C / f'log-{n}.txt').write_text(log)
        last = log.strip().splitlines()[-2][-110:] if len(log.strip().splitlines()) > 1 else log[-200:]
        if out.exists() and out.stat().st_size > 100000: return n, f'{d}s ' + last
    return n, 'FAILED ' + last
if __name__ == '__main__':
    names = sys.argv[1:] or list(MOTION)
    with ThreadPoolExecutor(6) as ex:
        for n, m in ex.map(run, names): print(n, m, flush=True)
