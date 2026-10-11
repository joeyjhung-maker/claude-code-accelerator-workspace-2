import base64, subprocess, os, html
B="creatives/_assets/2026-10-10-primal-viking-57-year-old-viking/storyboard"
S=[
("1. Hook",[
 ("01","A 52-year-old Viking rowing for days through frigid open water,","Frame 0. The hook line sits on this shot from the first frame."),
 ("02","hauling blood-crusted axes up jagged shoreline","Out of the surf, axes dragging."),
 ("03","could easily fight hand to hand against men half his age and conquer nations.","He's winning and bored."),
 ("04","But today, that same 52-year-old modern man needs ibuprofen to get out of bed.","Same face, gone soft. First laugh."),
 ("05","The difference wasn't genetics. It was what they ate.","Side by side. Same man, two eras."),
]),
("2. The promise",[
 ("06","And in the next 60 seconds, I'll show you what ancient men ate every single day that modern men never touch…","Covered platter. Don't show what's under it yet."),
 ("07","Why your energy, your drive, your ability to stay lean, and your confidence in the bedroom all quietly stopped at the same time…","3pm at the desk. Quick cuts for the other three in the full shot list."),
 ("08","And how to get them back without prescriptions, without injections, and without another useless supplement collecting dust on your counter.","The dusty counter."),
]),
("3. The whole animal",[
 ("09","To answer this, we have to look at the life that body had to survive.","Wide. Small man, huge weather."),
 ("10","That kind of body doesn't run on chicken breast and multivitamins.","The Viking judges the plate."),
 ("11","Vikings ate the WHOLE animal, liver, heart and kidney. Nothing got thrown away, because in the Arctic you don't get to be picky… you eat what keeps you alive.","Clean, stylised cuts. Not gory."),
]),
("4. Reindeer versus cattle",[
 ("12","And the animal they ate wasn't a cow.","Dopey cow."),
 ("13","It was the reindeer.","Hero shot."),
 ("14","Cattle stand in a field, get fed, barely move, and break down young.","Feedlot."),
 ("15","Reindeer run 5,000 km a season through minus-40 cold and never quit.","The herd at full speed."),
 ("16","Vikings ate the reindeer, packed with hard nutrients. You eat the cattle, deprived of all of them.","Split screen, same pose."),
]),
("5. The food changed",[
 ("17","Now look at what happened when men stopped eating this way. Organs disappeared from the diet completely. The human body didn't change, but the food did.","Empty tray where the organs were."),
 ("18","Now you can see why your energy, your drive, and your ability to stay lean all quietly stopped at the same time… they were all running on the same fuel, and you stopped eating it.","Four gauges on empty. Pays off the promise."),
 ("19","And here's what most men do… they grab a single supplement and hope it kicks something back on.","One hopeful capsule."),
 ("20","But you can't restart a dead fire by throwing more wood on it.","Logs on cold ash."),
 ("21","Reindeer organs don't add wood, they rebuild the entire fire from the ground up.","The Viking builds it properly."),
]),
("6. Each organ, one job",[
 ("22","The liver gave that 57-year-old Viking iron and B vitamins that kept oxygen moving through his blood… so he could row from dawn until dark without fading.","He eats the reindeer liver. The glow starts in the food and runs down his arms to the oars."),
 ("23","The heart, one of the richest sources on earth for carnitine, pulled stored fat into his cells and burned it as fuel… that's how he stayed lean through an Arctic winter on almost nothing.","He holds the reindeer heart. Its carnitine flows into him and feeds the fire."),
 ("24","The kidney sent zinc and selenium that supported blood flow… which explains why half of Normandy had his jawline.","He carries the reindeer kidneys. The whole village has his face."),
 ("25","The testicle gave him the cholesterol and androgenic peptides his body needed to keep making testosterone… the reason he still WANTED to conquer and dominate at 52.","Drive, shown as conquest. No animal shown for this one, on purpose."),
 ("26","And Rhodiola, the herb they gave on wedding nights,","The herb, and the wink."),
 ("37","made sure he could keep swinging hard on the field","Mid-swing on a raid. No blood."),
 ("38","and in the bedroom.","Smug in bed with his wife. Cracked headboard."),
]),
("7. Bridge and product",[
 ("27","Now obviously you're not gonna gut a reindeer before breakfast, so we did it for you.","Butter knife versus reindeer."),
 ("28","That's Primal Viking, freeze-dried reindeer liver, heart, and kidney, with beef testicle and Arctic herbs.","The real bottle. In the final edit, composite the actual pack shot so the label is exact."),
]),
("8. What he'll notice",[
 ("29","The first thing you'll notice is that 3pm wall starts easing up… the one where you'd normally reach for another coffee just to get through the afternoon.","Same desk as frame 7, now awake."),
 ("30","And once your energy stops crashing every day, you'll actually want to train again… not because you forced yourself, but because something switched back on.","Trainers on."),
 ("31","And that's when the fat around your belly and chest that laughed at every diet you ever tried starts shifting.","One notch on the belt. A small, believable change."),
 ("32","Your wife notices before you say a word.","The double take. Strong, fully clothed."),
]),
("9. Proof, offer and close",[
 ("33","157,579 men have already made the switch.","He leads an army of ordinary men."),
 ("34","Take the free quiz… it builds a personalized routine in under two minutes, no email needed to see the result.","Placeholder. Use a capture of the real quiz."),
 ("35","And right now during the Fall Sale, you'll unlock 60% off with a 30-day 100% money-back guarantee.","The real bottle. Offer text is added in the edit."),
 ("36","The Vikings didn't guess what their body needed. They just ate the animal that survived the worst conditions on earth. You can do the same thing with two capsules and a glass of water.","Conquer your work. The two of them, level, striding through the office."),
]),
]
def b64(i):
    src=f"{B}/f{i}.png"; jpg=f"{B}/thumbs/f{i}.jpg"
    os.makedirs(f"{B}/thumbs",exist_ok=True)
    if not os.path.exists(src): return None
    subprocess.run(["ffmpeg","-y","-loglevel","error","-i",src,"-vf","scale=405:720","-q:v","5",jpg],check=True)
    return base64.b64encode(open(jpg,"rb").read()).decode()
total=sum(len(l.split()) for _,fr in S for _,l,_ in fr)
out=["""<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Viking Storyboard</title>
<style>
:root{--bg:#f6f3ee;--ink:#1c1a17;--mute:#6b655c;--card:#fff;--line:#e1dbd0;--acc:#b4531a}
@media (prefers-color-scheme:dark){:root{--bg:#161412;--ink:#f0ebe3;--mute:#a59d90;--card:#211e1a;--line:#35302a;--acc:#e8843f}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.45 -apple-system,Segoe UI,Helvetica,Arial,sans-serif}
main{max-width:1180px;margin:0 auto;padding:24px 16px 60px}
h1{font-size:26px;margin:0 0 4px}.sub{color:var(--mute);margin:0 0 20px}
h2{font-size:17px;margin:34px 0 12px;padding-bottom:6px;border-bottom:2px solid var(--acc)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:14px}
.f{background:var(--card);border:1px solid var(--line);border-radius:10px;overflow:hidden}
.f img{display:block;width:100%;aspect-ratio:9/16;object-fit:cover;background:#000}
.f .n{font-weight:700;color:var(--acc);font-size:13px;padding:8px 10px 0}
.f .vo{padding:4px 10px 6px;font-size:13.5px}
.f .d{padding:0 10px 10px;color:var(--mute);font-size:12.5px}
.miss{aspect-ratio:9/16;display:flex;align-items:center;justify-content:center;color:var(--mute);background:var(--line)}
</style></head><body><main>
<h1>Primal Viking: "The 52-year-old Viking"</h1>
<p class="sub">Storyboard, 38 key frames. Third-party voice-over. Each card shows the frame, the voice-over line it covers, and a note. Captions, the product label and offer text are not on these frames; they're added in the edit.</p>"""]
t=0.0
for title,frames in S:
    out.append(f"<h2>{html.escape(title)}</h2><div class='grid'>")
    for i,line,note in frames:
        w=len(line.split()); start=t; t+=w/185*60
        ts=f"{int(start//60)}:{int(start%60):02d}"
        d=b64(i)
        img=f"<img alt='Frame {i}' src='data:image/jpeg;base64,{d}'>" if d else "<div class='miss'>not rendered</div>"
        out.append(f"<div class='f'>{img}<div class='n'>Frame {int(i)} · about {ts}</div><div class='vo'>{html.escape(line)}</div><div class='d'>{html.escape(note)}</div></div>")
    out.append("</div>")
out.append(f"<p class='sub' style='margin-top:30px'>Timings are estimates at 185 words a minute. Total runtime about {int(t//60)}:{int(t%60):02d}.</p></main></body></html>")
open(f"{B}/storyboard.html","w").write("\n".join(out))
print("words",total,"runtime",t)
