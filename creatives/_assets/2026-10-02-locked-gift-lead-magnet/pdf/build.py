#!/usr/bin/env python3
"""Build the designed Locked Gift Strategy PDF from the Google Doc export.

Input:  export/*.html + export/images/  (Google Docs: File > Download > Web page)
Output: locked-gift-guide.html  (then printed to PDF with headless Chrome)

The wording comes straight from the export. This script only decides how each
block LOOKS (section header, step tag, pull line, framed photo, caption...).
Pagination happens in the browser (see the script at the bottom of the page).
"""
import glob
import html
import re
from html.parser import HTMLParser
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = glob.glob(str(HERE / "export" / "*.html"))[0]
OUT = HERE / "locked-gift-guide.html"

# Our own graphics: shown full width with no frame (they carry their own style).
GRAPHICS = {"image15", "image5", "image12", "image9", "image4", "image11", "image10"}
# Photo/screenshot display widths in px (content column is 688px wide).
WIDTHS = {
    "image7": 400, "image20": 480, "image1": 250, "image19": 280, "image3": 300,
    "image17": 688, "image16": 688, "image21": 380, "image6": 470, "image2": 500,
    "image8": 330, "image18": 290, "image14": 470,
}
PAIR = ("image6", "image2")  # the two proof screenshots sit side by side
TILT = {"image19": 2, "image3": -2, "image6": -1.5, "image2": 1.5, "image21": -1.5}

SECTION_STARTS = (
    "EVERYONE’S FIGHTING", "HERE’S HOW IT ALL STARTED", "SO WE TESTED IT",
    "“OKAY DAN", "SO… HOW DO YOU", "WANT ME TO HELP",
)
PAGE_BREAK_BEFORE = ("HERE’S HOW IT ALL STARTED", "SO… HOW DO YOU")
STEP_BREAKS = (3,)  # start these steps on a fresh page so each spread holds whole steps
RED_PULLS = ("WE CLOSED AND ONBOARDED", "IT'S FREE", "IT’S FREE", "THEY'RE NOW CURIOUS", "THEY’RE NOW CURIOUS")
STAMPS = ("LOCK IT.", "“YES.”")


class DocParser(HTMLParser):
    """Flatten the export into blocks: h, p, li, img, hr."""

    def __init__(self, css):
        super().__init__(convert_charrefs=True)
        self.css = css
        self.blocks = []
        self.cur = None
        self.fmt = []

    def _style(self, attrs):
        a = dict(attrs)
        style = a.get("style", "")
        for c in (a.get("class") or "").split():
            style += ";" + self.css.get(c, "")
        return style

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("h1", "h2", "h3", "p", "li"):
            self.cur = {"t": "h" if tag.startswith("h") else tag, "html": "", "imgs": []}
        elif tag == "hr":
            self.blocks.append({"t": "hr"})
        elif self.cur is None:
            return
        elif tag == "span":
            st = self._style(attrs)
            opens = ""
            closes = ""
            if re.search(r"font-weight:\s*700", st):
                opens += "<b>"; closes = "</b>" + closes
            if re.search(r"font-style:\s*italic", st):
                opens += "<i>"; closes = "</i>" + closes
            self.cur["html"] += opens
            self.fmt.append(closes)
        elif tag == "a" and a.get("href"):
            href = a["href"]
            m = re.search(r"[?&]q=([^&]+)", href)
            if "google.com/url" in href and m:
                from urllib.parse import unquote
                href = unquote(m.group(1))
            self.cur["html"] += f'<a href="{html.escape(href)}">'
            self.fmt.append("</a>")
        elif tag == "br":
            self.cur["html"] += "<br>"
        elif tag == "img":
            name = Path(a.get("src", "")).stem
            self.cur["imgs"].append(name)

    def handle_endtag(self, tag):
        if self.cur is None:
            return
        if tag in ("span", "a") and self.fmt:
            self.cur["html"] += self.fmt.pop()
        elif tag in ("h1", "h2", "h3", "p", "li"):
            b = self.cur
            self.cur = None
            self.fmt = []
            text = re.sub(r"<[^>]+>", "", b["html"]).replace("\xa0", " ").strip()
            b["text"] = text
            b["html"] = re.sub(r"^(<br>|\s)+|(<br>|\s)+$", "", b["html"].replace("\xa0", " "))
            b["html"] = re.sub(r"<(b|i)>\s*</\1>", "", b["html"])
            if text or b["imgs"]:
                self.blocks.append(b)

    def handle_data(self, data):
        if self.cur is not None:
            self.cur["html"] += html.escape(data, quote=False)


def plain(h):
    """Heading text: drop bold/italic, keep line breaks and links."""
    h = re.sub(r"</?(b|i)>", "", h)
    return re.sub(r"\s*<br>\s*", "<br>", h).strip()


def figure(name, caption=""):
    src = f"img/{name}.png" if name in GRAPHICS and name != "image4" else f"img/{name}.jpg"
    if name in GRAPHICS:
        return f'<figure class="gfx"><img src="{src}" alt=""></figure>'
    w = WIDTHS.get(name, 420)
    tilt = TILT.get(name, 0)
    style = f"width:{w}px;" + (f"transform:rotate({tilt}deg);" if tilt else "")
    cap = f'<figcaption class="hand">{caption}</figcaption>' if caption else ""
    side = " side" if caption and w <= 420 else ""
    return f'<figure class="photo{side}"><img class="frame" style="{style}" src="{src}" alt="">{cap}</figure>'


def render(blocks):
    out = []
    i = 0
    n = len(blocks)
    step_no = 0
    # --- cover: first two headings + first image are laid out by hand ---
    while i < n and not blocks[i].get("text", "").startswith("Yo yo"):
        i += 1
    lis = []
    pair_hold = []

    def flush_list():
        if lis:
            tick = '<i class="tick"><svg viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5"/></svg></i>'
            clean = [re.sub(r"</?(b|i)>|[*]", "", x).strip() for x in lis]
            items = "".join(f"<div>{tick}<span>{x}</span></div>" for x in clean)
            out.append(f'<div class="tried">{items}</div>')
            lis.clear()

    while i < n:
        b = blocks[i]
        t = b["t"]
        text = b.get("text", "")
        if t != "li":
            flush_list()
        if t == "hr":
            i += 1
            continue  # step tags and section headers do the dividing
        if t == "li":
            lis.append(b["html"])
            i += 1
            continue

        # paragraphs / headings that carry images
        if b["imgs"]:
            cap = b["html"] if text else ""
            cap = re.sub(r"</?(b|i)>", "", cap)
            # a short bold/italic line straight after a photo is its caption
            if not cap and i + 1 < n and blocks[i + 1]["t"] == "p" and not blocks[i + 1]["imgs"]:
                nxt = blocks[i + 1]
                if nxt["text"] in ("Here’s one ad account we’re running.", "\"The bugger got me.\"", "“The bugger got me.”"):
                    cap = nxt["text"]
                    i += 1
            for k, name in enumerate(b["imgs"]):
                if name in PAIR:
                    pair_hold.append(name)
                    if len(pair_hold) == len(PAIR):
                        cells = "".join(f'<img class="frame" src="img/{x}.jpg" style="transform:rotate({TILT.get(x, 0)}deg)" alt="">' for x in pair_hold)
                        out.append(f'<div class="pair">{cells}</div>')
                    continue
                out.append(figure(name, cap if k == len(b["imgs"]) - 1 else ""))
            i += 1
            continue

        if t == "h":
            h = plain(b["html"])
            up = text.upper()
            if up.startswith("STEP ") and ":" in text:
                step_no += 1
                title = text.split(":", 1)[1].strip()
                brk = ' data-break="1"' if step_no in STEP_BREAKS else ""
                out.append(f'<div class="step keep"{brk}><span class="mono">Step {step_no:02d}</span><b>{html.escape(title)}</b></div>')
            elif re.match(r"^\d\.", text):
                num, rest = h.split(".", 1)
                keep = "" if num.strip() == "5" else " keep"
                out.append(f'<div class="act{keep}"><span class="n">{num}</span><span>{rest.strip()}</span></div>')
            elif text.startswith("→"):
                rows = [r.strip(" →") for r in re.split(r"<br>", h) if r.strip()]
                out.append('<div class="chain">' + "".join(f"<div><em>→</em>{r}</div>" for r in rows) + "</div>")
            elif text.startswith("STOP FIGHTING"):
                a, bb = (h.split("<br>") + [""])[:2]
                out.append(f'<div class="closer">{a}<br><span class="red">{bb}</span></div>')
            elif text in STAMPS:
                out.append(f'<div class="stamp keep-prev">{h}</div>')
            elif text.startswith(SECTION_STARTS):
                brk = ' data-break="1"' if text.startswith(PAGE_BREAK_BEFORE) else ""
                out.append(f'<h2 class="sec keep"{brk}>{h}</h2>')
            else:
                red = " red" if text.startswith(RED_PULLS) else ""
                out.append(f'<div class="pull keep{red}">{h}</div>')
            i += 1
            continue

        # plain paragraphs
        if text.startswith("Yo yo"):
            out.append(f'<div class="hand yo">{b["html"]}</div>')
        elif text.startswith("We're getting more clients") or text.startswith("We’re getting more clients"):
            out.append('<div class="pull big">WE’RE GETTING MORE <span class="red">CLIENTS</span> THAN MOST GET REPLIES.</div>')
        elif text in ("They all worked!",):
            out.append('<div class="pull big">THEY ALL <span class="red">WORKED!</span></div>')
        elif "COFFEE DATES" in text and text.startswith("And booked"):
            out.append('<p class="keep">And booked…</p>')
            out.append('<div class="pull">4 COFFEE DATES.</div>')
        elif text == "Dan":
            out.append('<div class="hand sign">Dan</div>')
        else:
            keep = " keep" if text.endswith(("…", ":")) and len(text) < 60 else ""
            brk = ""
            out.append(f'<p class="{keep.strip()}"{brk}>{b["html"]}</p>')
        i += 1
    flush_list()
    return "\n".join(out)


def main():
    raw = Path(SRC).read_text(encoding="utf-8")
    css = dict(re.findall(r"\.(c\d+)\{([^}]*)\}", raw))
    p = DocParser(css)
    p.feed(raw[raw.find("<body"):])
    flow = render(p.blocks)
    page = TEMPLATE.replace("{{FLOW}}", flow)
    OUT.write_text(page, encoding="utf-8")
    print(f"blocks: {len(p.blocks)}  ->  {OUT.name}")


TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>The Locked Gift Strategy</title>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Caveat:wght@700&family=IBM+Plex+Mono:wght@500;600&family=Libre+Franklin:ital,wght@0,400;0,700;0,800;1,400;1,700&display=swap" rel="stylesheet">
<style>
  :root { --ink:#1C1A17; --red:#C23B22; --paper:#FFFFFF; --label:#FBF8F1; --tint:#F3EBDD; --kraft:#CDAA7D; --mute:#5A534A; }
  @page { size: 8.5in 11in; margin: 0; }
  * { box-sizing:border-box; -webkit-print-color-adjust:exact; print-color-adjust:exact; }
  html, body { margin:0; background:var(--paper); color:var(--ink); }
  #flow { display:none; }
  @media screen { body.sheet { display:grid; grid-template-columns:repeat(4, 8.5in); background:#888; gap:6px; } }

  /* ---------- page frame ---------- */
  .page { width:8.5in; height:11in; padding:0.46in 0.67in 0.4in; display:flex; flex-direction:column; position:relative; overflow:hidden; page-break-after:always; background:var(--paper); }
  .page:last-child { page-break-after:auto; }
  .mono { font-family:'IBM Plex Mono', monospace; font-weight:600; letter-spacing:.14em; text-transform:uppercase; }
  .hdr { display:flex; justify-content:space-between; font-size:9.5px; padding-bottom:9px; border-bottom:2px dashed var(--ink); margin-bottom:24px; flex-shrink:0; }
  .ftr { padding-top:12px; display:flex; justify-content:space-between; align-items:center; font-size:9.5px; flex-shrink:0; }
  .ftr .pg { background:var(--ink); color:#fff; padding:5px 9px; letter-spacing:.1em; }
  .ftr .lock { display:flex; align-items:center; gap:7px; }
  .ftr svg { width:12px; height:12px; fill:none; stroke:var(--red); stroke-width:2.6; stroke-linecap:round; stroke-linejoin:round; }
  .body { flex:1 1 0; min-height:0; overflow:hidden; }
  .body > :first-child { margin-top:0; }

  /* ---------- type ---------- */
  .body p { font-family:'Libre Franklin', sans-serif; font-size:15px; line-height:1.43; margin:0 0 7.5px; }
  .tight p { margin-bottom:5px; line-height:1.36; }
  .tight figure { margin:10px 0 16px; }
  .tight .step { margin:16px 0 12px; }
  .tight .pull { margin:8px 0 10px; }
  .tight .sec { margin:18px 0 14px; }
  .body p b { font-weight:800; }
  .body a { color:var(--red); text-decoration:underline; text-underline-offset:2px; }
  .red { color:var(--red); }
  .hand { font-family:Caveat, cursive; font-weight:700; line-height:1.05; }
  .yo { font-size:50px; margin:0 0 16px; transform:rotate(-2deg); transform-origin:left; }
  .sign { font-size:54px; margin:6px 0 18px; transform:rotate(-3deg); transform-origin:left; }
  .sec { font-family:Anton, sans-serif; font-weight:400; font-size:50px; line-height:1; margin:26px 0 20px; padding-top:16px; border-top:6px solid var(--ink); }
  .pull { font-family:Anton, sans-serif; font-weight:400; font-size:36px; line-height:1.04; margin:12px 0 14px; }
  .pull.big { font-size:45px; margin:10px 0 16px; }
  .stamp { display:inline-block; margin:8px 0 18px 4px; border:5px solid var(--red); color:var(--red); font-family:Anton, sans-serif; font-size:38px; line-height:1; padding:8px 18px 11px; transform:rotate(-3deg); }
  .closer { font-family:Anton, sans-serif; font-size:49px; line-height:1; margin:26px 0 22px; padding-top:18px; border-top:6px solid var(--ink); }

  /* ---------- components ---------- */
  .frame { border:3px solid var(--ink); box-shadow:9px 9px 0 var(--ink); display:block; }
  figure { margin:14px 0 26px; }
  figure.gfx img { width:100%; display:block; }
  .pair { display:flex; gap:30px; align-items:center; margin:18px 0 28px; }
  .pair img { flex:1 1 0; min-width:0; width:50%; }
  .body > figure.photo:first-child, .body > .pair:first-child { margin-top:14px; }
  figure.photo { display:flex; flex-direction:column; align-items:flex-start; gap:16px; }
  figure.photo.side { flex-direction:row; align-items:center; gap:26px; }
  figcaption.hand { font-size:29px; max-width:300px; transform:rotate(-3deg); }
  figure.photo:not(.side) figcaption.hand { max-width:none; transform:rotate(-1.5deg); }
  .step { display:inline-flex; align-items:center; gap:16px; margin:24px 0 18px; background:var(--label); border:3px solid var(--ink); box-shadow:7px 7px 0 var(--ink); padding:11px 20px 12px 16px; transform:rotate(-1deg); }
  .step .mono { background:var(--red); color:#fff; font-size:11px; padding:6px 9px; }
  .step b { font-family:Anton, sans-serif; font-weight:400; font-size:34px; line-height:1; }
  .tried { display:grid; grid-template-columns:1fr 1fr; gap:7px 18px; margin:8px 0 18px; }
  .tried div { display:flex; align-items:center; gap:10px; font-family:'IBM Plex Mono', monospace; font-weight:500; font-size:11px; line-height:1.3; background:var(--tint); border:2px solid var(--ink); padding:6px 9px; }
  .tick { width:15px; height:15px; flex-shrink:0; background:var(--ink); display:flex; align-items:center; justify-content:center; }
  .tick svg { width:10px; height:10px; fill:none; stroke:#fff; stroke-width:3.4; stroke-linecap:round; stroke-linejoin:round; }
  .chain { margin:16px 0 18px; border:3px solid var(--ink); background:var(--label); box-shadow:9px 9px 0 var(--ink); }
  .chain div { font-family:Anton, sans-serif; font-size:33px; line-height:1; padding:14px 18px; border-bottom:2px dashed var(--ink); display:flex; gap:14px; }
  .chain div:last-child { border-bottom:none; }
  .chain em { font-style:normal; color:var(--red); }
  .act { display:flex; align-items:flex-start; gap:14px; margin:0 0 10px; background:var(--label); border:3px solid var(--ink); padding:12px 16px; font-family:Anton, sans-serif; font-size:25px; line-height:1.12; }
  .act .n { width:38px; height:38px; flex-shrink:0; border-radius:50%; background:var(--ink); color:#fff; display:flex; align-items:center; justify-content:center; font-size:20px; margin-top:-2px; }

  /* ---------- cover ---------- */
  .kicker { font-size:11px; color:var(--red); margin-bottom:12px; }
  h1 { font-family:Anton, sans-serif; font-weight:400; font-size:61px; line-height:1.12; margin:0; letter-spacing:.005em; }
  h1 .ul { text-decoration:underline; text-decoration-thickness:6px; text-underline-offset:5px; text-decoration-skip-ink:none; }
  .cover .stamp { align-self:flex-start; margin:20px 0 26px 4px; }
  .hero { display:flex; gap:26px; align-items:flex-end; }
  .hero img { width:500px; }
  .tag { flex-grow:1; background:var(--label); border:3px solid var(--ink); display:flex; flex-direction:column; transform:rotate(2deg); margin-bottom:14px; }
  .tag .row { padding:10px 12px; border-bottom:2px solid var(--ink); }
  .tag .lbl { font-size:8.5px; display:block; margin-bottom:3px; }
  .tag .big { font-family:Anton, sans-serif; font-size:23px; line-height:1.05; }
  .tag .sm { font-family:'Libre Franklin', sans-serif; font-size:12px; }
  .bars { height:40px; margin:12px 12px 8px; background:repeating-linear-gradient(90deg, var(--ink) 0 2px, transparent 2px 4px, var(--ink) 4px 5px, transparent 5px 8px, var(--ink) 8px 11px, transparent 11px 13px); }
  .tag .code { font-size:7.5px; text-align:center; padding-bottom:10px; }
</style>
</head>
<body>

<section class="page cover">
  <div class="hdr mono"><span>Priority · Handle with curiosity</span><span>Free guide · Dan Wardrope</span></div>
  <div class="kicker mono">The Locked Gift Strategy</div>
  <h1>HOW WE’RE GETTING CEOs OF $20M-$80M COMPANIES TO CALL <span class="ul">US</span>… <span class="red">FOR JUST $40 BUCKS…</span></h1>
  <div class="stamp">…USING “LOCKED GIFTS”!</div>
  <div class="hero">
    <img class="frame" src="img/image13.jpg" alt="Dan holding a locked bottle of whisky and the letter">
    <div class="tag">
      <div class="row"><span class="lbl mono">From</span><div class="big">DAN WARDROPE</div><div class="sm">B2B Leads Lab</div></div>
      <div class="row"><span class="lbl mono">To</span><div class="big">YOUR DREAM 100</div></div>
      <div class="bars"></div>
      <div class="code mono">LG · Desk not screen</div>
    </div>
  </div>
  <div style="flex:1"></div>
  <div class="ftr mono"><span class="pg">01</span><span class="lock"><svg viewBox="0 0 24 24"><rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>Get on their desk</span></div>
</section>

<div id="flow">
{{FLOW}}
</div>

<script>
// Pour the blocks in #flow into fixed-size pages, one block at a time.
(async function paginate() {
  await document.fonts.ready;
  await Promise.all([...document.images].map(im => im.complete ? 0 : new Promise(r => { im.onload = im.onerror = r; })));
  const flow = document.getElementById('flow');
  const blocks = [...flow.children];
  flow.remove();
  let pageNo = 1, body;
  const lock = '<svg viewBox="0 0 24 24"><rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>';
  function newPage() {
    pageNo++;
    const s = document.createElement('section');
    s.className = 'page';
    s.innerHTML = '<div class="hdr mono"><span>The Locked Gift Strategy</span><span>Dan Wardrope · B2B Leads Lab</span></div>'
      + '<div class="body"></div>'
      + '<div class="ftr mono"><span class="pg">' + String(pageNo).padStart(2, '0') + '</span><span class="lock">' + lock + 'Get on their desk</span></div>';
    document.body.appendChild(s);
    body = s.querySelector('.body');
  }
  const over = () => body.scrollHeight > body.clientHeight + 1;
  // If a page would hold only a few stray lines, squeeze them onto the page before it.
  function rescue() {
    const pages = document.querySelectorAll('.page');
    if (pages.length < 3) return;
    const prevBody = pages[pages.length - 2].querySelector('.body');
    if (!prevBody || !body.children.length || body.children.length > 4) return;
    const cur = body, moved = [...cur.children];
    prevBody.classList.add('tight');
    moved.forEach(c => prevBody.appendChild(c));
    if (prevBody.scrollHeight > prevBody.clientHeight + 1) {
      moved.forEach(c => cur.appendChild(c));
      prevBody.classList.remove('tight');
      return;
    }
    cur.closest('.page').remove();
    pageNo--;
    body = prevBody;
  }
  newPage();
  for (const el of blocks) {
    if (el.dataset.break && body.children.length) { rescue(); newPage(); }
    body.appendChild(el);
    if (over() && body.children.length > 1) {
      // carry any trailing "keep with next" blocks over to the new page too
      const carry = [el];
      let prev = el.previousElementSibling;
      while (prev && prev.classList.contains('keep') && body.children.length > carry.length + 1) {
        carry.unshift(prev);
        prev = prev.previousElementSibling;
      }
      newPage();
      carry.forEach(c => body.appendChild(c));
    }
  }
  rescue();
  document.title = 'The Locked Gift Strategy';
  document.body.dataset.pages = pageNo;
  if (location.search.includes('sheet')) document.body.classList.add('sheet');
  const row = new URLSearchParams(location.search).get('row');
  if (row !== null) [...document.querySelectorAll('.page')].forEach((pg, i) => { if (Math.floor(i / 8) !== Number(row)) pg.style.display = 'none'; });
})();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
