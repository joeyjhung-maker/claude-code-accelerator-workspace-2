# Export Claude Design canvas artboards (.dc.html) to clean static HTML + full-page PNGs.
# Usage: python scripts/design_canvas_export.py <folder with .dc.html files> <out folder> <assets folder>
# Needs Pillow and Google Chrome. Edit JOBS (artboards + tweak values) and BLOBS (asset id -> file in <assets folder>).
# HTML lands in <out>/handoff/ with images in handoff/img/; PNGs land in <out>/.
# Workflow: workflows/2026-10-14-design-mockup-to-png.md
import re, sys, os, shutil, subprocess
from PIL import Image

src_dir, out_dir, assets = sys.argv[1], sys.argv[2], sys.argv[3]
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

JOBS = [
    ("Main.dc.html", "variant-a-dark", "locked-gifts-optin-A-dark.png", "Locked Gifts — Variant A (dark)", {"accent": "#FFD43B"}),
    ("Receipt.dc.html", "variant-b-light", "locked-gifts-optin-B-light.png", "Locked Gifts — Variant B (light)", {"accent": "#1D4ED8", "highlight": "#FFE14D"}),
]
BLOBS = {
    "44590c2471fabed4ac97e7fa870737c0": "dan-its-locked.jpg",
    "b2689cf5824763ed1b1aca3018aeaf92": "gift-wine.png",
    "e8fdf61b26977fb0ff0013a10e1102fb": "gift-yeti.png",
    "edf8cfdd178eefd198df4ec04a842864": "gift-airtag.jpg",
    "6c7cb15ff0af90aa2c356de2871834b0": "gift-jbl.jpg",
}

hand = os.path.join(out_dir, "handoff")
os.makedirs(os.path.join(hand, "img"), exist_ok=True)
for fn in BLOBS.values():
    shutil.copy(os.path.join(assets, fn), os.path.join(hand, "img", fn))

for name, stem, png, title, props in JOBS:
    html = open(os.path.join(src_dir, name), encoding="utf-8").read()
    html = html.replace('<script src="./support.js"></script>', '<meta name="viewport" content="width=device-width, initial-scale=1">')
    html = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", html, flags=re.S)
    html = re.sub(r"\s*<script type=\"text/x-dc\".*?</script>", "", html, flags=re.S)
    m = re.search(r"<helmet>(.*?)</helmet>", html, flags=re.S)
    html = re.sub(r"\s*<helmet>.*?</helmet>", "", html, flags=re.S)
    html = html.replace("</head>", (m.group(1).strip() if m else "") + "\n</head>", 1)
    for t in ("<x-dc>", "</x-dc>"):
        html = html.replace(t, "")
    for k, v in props.items():
        html = re.sub(r"\{\{\s*" + k + r"\s*\}\}", v, html)
    for bid, fn in BLOBS.items():
        html = html.replace("/_blob/" + bid, "img/" + fn)
    html = re.sub(r"\n{3,}", "\n\n", html)
    assert "{{" not in html and "/_blob/" not in html, f"unfilled hole or unknown image in {name}"
    page = os.path.join(hand, stem + ".html")
    open(page, "w", encoding="utf-8").write(html)

    raw = os.path.join(out_dir, "_raw.png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=2",
                    "--window-size=1440,2600", "--virtual-time-budget=8000", f"--screenshot={raw}", "file://" + page],
                   check=True, capture_output=True)
    im = Image.open(raw).convert("RGB"); px = im.load(); bg = px[5, im.height - 5]; bottom = im.height
    for y in range(im.height - 1, 0, -1):
        if any(px[x, y] != bg for x in range(0, im.width, 4)):
            bottom = min(im.height, y + 1 + 96); break
    im.crop((0, 0, im.width, bottom)).save(os.path.join(out_dir, png))
    shutil.copy(os.path.join(out_dir, png), os.path.join(hand, "preview-" + stem.split("-", 1)[1] + ".png"))
    os.remove(raw)
    print(stem, bottom)
