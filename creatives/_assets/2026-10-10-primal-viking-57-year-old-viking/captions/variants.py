import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
B = Path(__file__).resolve().parent; S = '/System/Library/Fonts/Supplemental/'; SY = '/System/Library/Fonts/'
def face(path, want, size):
    for i in range(12):
        try: f = ImageFont.truetype(path, size, index=i)
        except Exception: break
        if all(w.lower() in ' '.join(f.getname()).lower() for w in want): return f
    return ImageFont.truetype(path, size)
ORANGE = (232, 106, 36); CREAM = (247, 236, 211); YELLOW = (255, 214, 10); BROWN = (48, 26, 12); WHITE = (255, 255, 255); BLACK = (0, 0, 0)
V = [
 ("1  Current", lambda s: ImageFont.truetype(S + 'Arial Black.ttf', s), 96, dict(fill=WHITE, hi=YELLOW, stroke=11, sc=BLACK)),
 ("2  Impact", lambda s: ImageFont.truetype(S + 'Impact.ttf', s), 122, dict(fill=WHITE, hi=ORANGE, stroke=10, sc=BLACK, shadow=10)),
 ("3  Carved", lambda s: ImageFont.truetype(S + 'Herculanum.ttf', s), 112, dict(fill=CREAM, hi=ORANGE, stroke=10, sc=BROWN, shadow=8)),
 ("4  Storybook", lambda s: ImageFont.truetype(S + 'Trattatello.ttf', s), 138, dict(fill=CREAM, hi=YELLOW, stroke=9, sc=BROWN, shadow=8, upper=False)),
 ("5  Slab", lambda s: face(S + 'Rockwell.ttc', ['bold'], s), 104, dict(fill=CREAM, hi=ORANGE, stroke=10, sc=BROWN, shadow=10)),
 ("6  Poster", lambda s: face(S + 'Phosphate.ttc', ['solid'], s), 118, dict(fill=CREAM, hi=ORANGE, stroke=9, sc=BROWN, shadow=8)),
 ("7  Saga", lambda s: ImageFont.truetype(S + 'Luminari.ttf', s), 104, dict(fill=CREAM, hi=YELLOW, stroke=9, sc=BROWN, shadow=8)),
 ("8  Block", lambda s: face(S + 'Futura.ttc', ['condensed', 'extrabold'], s), 124, dict(fill=WHITE, hi=WHITE, stroke=9, sc=BLACK, box=ORANGE)),
]
def render(base, words, hi, name):
    tiles = []
    for label, mk, size, o in V:
        im = Image.open(base).convert('RGBA'); W, H = im.size; f = mk(size); d = ImageDraw.Draw(im)
        ws = [w.upper() if o.get('upper', True) else w for w in words]; rows, row = [], []
        for w in ws:
            if row and d.textlength(' '.join(row + [w]), font=f) > W - 130: rows.append(row); row = []
            row.append(w)
        rows.append(row); lh = int(size * 1.22); y = 1390 - len(rows) * lh // 2; k = 0
        layer = Image.new('RGBA', im.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(layer); sh = Image.new('RGBA', im.size, (0, 0, 0, 0)); ds = ImageDraw.Draw(sh)
        for r in rows:
            x = (W - d.textlength(' '.join(r), font=f)) / 2
            for w in r:
                tw = d.textlength(w, font=f)
                if k == hi and o.get('box'):
                    bb = dl.textbbox((x, y), w, font=f); dl.rounded_rectangle((bb[0] - 18, bb[1] - 14, bb[2] + 18, bb[3] + 14), 16, fill=o['box'] + (255,))
                if o.get('shadow'): ds.text((x + o['shadow'], y + o['shadow']), w, font=f, fill=(0, 0, 0, 150), stroke_width=o['stroke'], stroke_fill=(0, 0, 0, 150))
                dl.text((x, y), w, font=f, fill=(o['hi'] if k == hi else o['fill']) + (255,), stroke_width=0 if (k == hi and o.get('box')) else o['stroke'], stroke_fill=o['sc'] + (255,))
                x += d.textlength(w + ' ', font=f); k += 1
            y += lh
        im = Image.alpha_composite(Image.alpha_composite(im, sh.filter(ImageFilter.GaussianBlur(3))), layer); d = ImageDraw.Draw(im)
        lf = ImageFont.truetype(S + 'Arial Black.ttf', 54); d.rectangle((0, 0, W, 96), fill=(0, 0, 0, 215)); d.text((28, 12), label, font=lf, fill=WHITE)
        tiles.append(im.convert('RGB').resize((540, 960)))
    sheet = Image.new('RGB', (540 * 4, 960 * 2))
    for i, t in enumerate(tiles): sheet.paste(t, ((i % 4) * 540, (i // 4) * 960))
    sheet.save(B / name, quality=88)
render(B / 'base-viking.png', ['A', '52-year-old', 'Viking'], 2, 'caption-options-viking.jpg')
render(B / 'base-modern.png', ['needs', 'ibuprofen'], 1, 'caption-options-modern.jpg')
