# Export Claude Design canvas artboards (.dc.html) to full-page PNGs with headless Chrome.
# Usage: python scripts/design_canvas_to_png.py <folder with the .dc.html files> <hero image> <out folder>
# Needs Pillow (a scratch venv is fine). Edit `jobs` below: one row per artboard, with its
# output name and the tweak values ({{accent}} etc.) to bake in. Every /_blob/ image becomes <hero image>.
# Workflow: workflows/2026-10-14-design-mockup-to-png.md
import re, sys, subprocess, shutil, os
from PIL import Image

src_dir, img_path, out_dir = sys.argv[1], sys.argv[2], sys.argv[3]
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
work = os.path.join(out_dir, "_render")
os.makedirs(work, exist_ok=True)
shutil.copy(img_path, os.path.join(work, "dan.jpg"))

jobs = [
    ("Main.dc.html", "locked-gifts-optin-A-dark.png", {"accent": "#FFD43B"}),
    ("Receipt.dc.html", "locked-gifts-optin-B-light.png", {"accent": "#1D4ED8", "highlight": "#FFE14D"}),
]
SCALE = 2
W, H = 1440, 2200

for name, out_name, props in jobs:
    html = open(os.path.join(src_dir, name), encoding="utf-8").read()
    html = html.replace('<script src="./support.js"></script>', "")
    html = re.sub(r"<script type=\"text/x-dc\".*?</script>", "", html, flags=re.S)
    for tag in ("<x-dc>", "</x-dc>", "<helmet>", "</helmet>"):
        html = html.replace(tag, "")
    for k, v in props.items():
        html = re.sub(r"\{\{\s*" + k + r"\s*\}\}", v, html)
    html = re.sub(r"/_blob/[0-9a-f]{32}", "dan.jpg", html)
    page = os.path.join(work, name.replace(".dc.html", ".html"))
    open(page, "w", encoding="utf-8").write(html)

    raw = os.path.join(work, out_name)
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    f"--force-device-scale-factor={SCALE}", f"--window-size={W},{H}",
                    "--virtual-time-budget=8000", f"--screenshot={raw}", "file://" + page],
                   check=True, capture_output=True)

    # Trim the empty background below the footer
    im = Image.open(raw).convert("RGB")
    bg = im.getpixel((5, im.height - 5))
    px = im.load()
    bottom = im.height
    for y in range(im.height - 1, 0, -1):
        if any(px[x, y] != bg for x in range(0, im.width, 4)):
            bottom = min(im.height, y + 1 + 48 * SCALE)
            break
    im.crop((0, 0, im.width, bottom)).save(os.path.join(out_dir, out_name))
    print(out_name, im.width, bottom)
