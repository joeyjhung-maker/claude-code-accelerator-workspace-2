// HYBRID LAYER — Dan's real footage living inside the doodle world.
// The doodle (anim.html) still renders underneath, untouched. On top of it:
//   #dan (canvas): Dan's original footage, clipped to whatever shape the current beat wants
//                  (full frame, a live "Dan-cam" bubble, or a hole/tear/card opening onto the doodle)
//   #hy  (svg):    ink rims, paper-tape captions, and the doodle gags drawn over his footage
// Every frame is a pure function of t, same as the doodle, so the sound cues come from the same timeline.
(function () {
const FPS = 30, NF = FACES.length, VO_END = (NF - 1) / FPS;
const qs = new URLSearchParams(location.search);
const FR = qs.get('frames') || 'frames/';
const doodleSeek = window.seek, doodleCues = window.collectCues;
const cv = document.getElementById('dan'), cx = cv.getContext('2d'), hy = document.getElementById('hy');

// ---------- the beat map ----------
// full = Dan full screen · bubble = live Dan-cam over the doodle · doodle = doodle only
// hole/tear/card = full -> doodle (or doodle -> full) openings · up/down = bubble <-> full morph
const BUB = {x: 190, y: 1722, r: 146}, END = {x: 255, y: 1495, r: 190};
const TL = [
  ['full', 0, 3.0],
  ['hole', 3.0, 3.42, {x: 520, y: 1010}],            // ink circle on his REAL lock opens onto the drawn one
  ['doodle', 3.42, 7.55],
  ['tear', 7.55, 7.98],                               // zoom into the tower... the paper rips, it's Dan
  ['full', 7.98, 10.95],
  ['card', 10.95, 11.45],                             // "one single offer" card grows into the offer card
  ['doodle', 11.45, 11.85],
  ['bin', 11.85, 12.2],
  ['bubble', 12.2, 21.0],
  ['up', 21.0, 21.45],                                // "and that's the whole pitch"
  ['full', 21.45, 26.95],
  ['down', 26.95, 27.4],
  ['bubble', 27.4, 37.2],
  ['up', 37.2, 37.6],                                 // "ridiculously easy to sell"
  ['full', 37.6, 39.3],
  ['down', 39.3, 39.8],
  ['bubble', 39.8, 50.6],
  ['bout', 50.6, 50.92],
  ['doodle', 50.92, 59.72],
  ['tear', 59.72, 60.1],                              // "plus you don't have to be a tech guru"
  ['full', 60.1, 62.2],
  ['down', 62.2, 62.65],
  ['bubble', 62.65, 64.15],
  ['up', 64.15, 64.55],                               // "I'm so pumped about this offer"
  ['full', 64.55, 65.55],
  ['hole', 65.55, 65.95, {x: 540, y: 1120}],
  ['doodle', 65.95, 69.1],
  ['bin', 69.1, 69.45],
  ['bubble', 69.45, 71.5],
  ['up', 71.5, 71.95],                                // "if you don't love it... refund"
  ['full', 71.95, 74.4],
  ['down', 74.4, 74.95, {end: 1}],                    // "take care" — he lands in the end card
  ['bubble', 74.95, 99, {end: 1}],
];
function beat(t) {for (const b of TL) if (t >= b[1] && t < b[2]) return {k: b[0], q: P(t, b[1], b[2] - b[1]), o: b[3] || {}, t0: b[1], t1: b[2]}; return {k: 'doodle', q: 0, o: {}}}
// how much of the doodle is on screen (drives which doodle sound cues survive)
window.doodleVis = function (t) {const b = beat(t);
  return ({full: 0, doodle: 1, bubble: 1, bin: 1, bout: 1, up: 1 - b.q, down: b.q, hole: b.q, card: b.q, tear: 1 - b.q})[b.k]};

// ---------- captions (Dan's words, verbatim) — paper tape laid over his burned-in captions ----------
// {word|style}: a amber, b blue, g green, r red, h yellow marker
const CAPS = [
  [0, 2.33, 'I sent this bottle of {whiskey|a}'],
  [2.33, 3.64, 'with this little {combination code|b} and a letter'],
  [7.5, 9.5, 'and when they dial a number in that letter'],
  [9.5, 11.5, 'I put {one single offer|h} in front of them'],
  [20.9, 22.1, "and that's the whole pitch"],
  [22.1, 23.3, "we've just done this for a client"],
  [23.3, 26.98, 'and generated an extra {$1.2m|g} from this offer'],
  [26.98, 27.5, 'and as a thank you…'],
  [37.1, 39.84, 'and this offer is {ridiculously easy|h} to sell'],
  [59.6, 61.5, "plus you don't have to be a {tech guru|r}"],
  [61.5, 62.3, 'to be able to build this'],
  [62.3, 64.25, 'the AI behind it is {very, very simple|g}'],
  [64.25, 65.72, "I'm so {pumped|a} about this offer"],
  [65.72, 66.0, 'I wrote a book on it'],
  [71.4, 72.35, "if you don't love it"],
  [72.35, 74.72, "you can {keep it|g} and I'll {refund|g} you your money"],
  [74.72, 99, 'take care'],
];
const COL = {a: AMBER, b: BLUE, g: GREEN, r: RED};
const mc = document.createElement('canvas').getContext('2d');
function capLines(src, px) {
  const toks = []; src.replace(/\{([^|}]+)\|(\w)\}|([^{\s]+)/g, (m, w, st, plain) => {(w ? w.split(' ') : [plain]).forEach(x => toks.push([x, st || '']))});
  mc.font = `800 ${px}px Poppins`; const sp = mc.measureText(' ').width, lines = [[]]; let w = 0;
  for (const [x, st] of toks) {const ww = mc.measureText(x).width; if (w + ww > 860 && lines[lines.length - 1].length) {lines.push([]); w = 0}
    lines[lines.length - 1].push([x, st, ww]); w += ww + sp;}
  return lines.map(l => ({ws: l, w: l.reduce((a, [, , ww]) => a + ww, 0) + sp * (l.length - 1), sp}));
}
function tape(t) {
  const c = CAPS.find(([a, b]) => t >= a && t < b); if (!c) return '';
  const px = 54, lines = capLines(c[2], px), two = lines.length > 1, cy = two ? 1255 : 1256, hh = two ? 184 : 124;
  const q = P(t, c[0], .22), s = c[0] > 0 ? bk(q) * .06 + .94 : 1, rot = -1.2 + (1 - q) * 1.6;
  const x0 = 58, x1 = 1022, y0 = cy - hh / 2, y1 = cy + hh / 2;
  let edge = (x, sgn, up) => {let d = ''; for (let j = 0; j <= 8; j++) {const i = up ? 8 - j : j, y = y0 + (y1 - y0) * i / 8; d += `L${(x + sgn * (i % 2 ? 9 : -3)).toFixed(1)} ${y.toFixed(1)} `} return d};
  const shape = `M${x0} ${y0} L${x1} ${y0} ${edge(x1, 1, 0)}L${x0} ${y1} ${edge(x0, -1, 1)}Z`;
  let body = `<path d="${shape}" fill="${INK}" opacity=".35" transform="translate(7 9)"/><path d="${shape}" fill="${PAPER}" stroke="${INK}" stroke-width="3"/>`;
  lines.forEach((l, li) => {let x = 540 - l.w / 2; const y = cy + (two ? (li ? 58 : -8) : 25) - (two ? 12 : 0);
    for (const [w, st, ww] of l.ws) {
      if (st === 'h') body += `<rect x="${(x - 8).toFixed(1)}" y="${y - px * .78}" width="${(ww + 16).toFixed(1)}" height="${px * .98}" rx="8" fill="#FFE066" opacity=".9" transform="rotate(-1.5 ${x} ${y})"/>`;
      body += `<text x="${x.toFixed(1)}" y="${y}" class="t" font-size="${px}" font-weight="800" fill="${COL[st] || INK}">${w.replace(/&/g, '&amp;')}</text>`;
      x += ww + l.sp;}});
  return `<g transform="translate(540 ${cy}) rotate(${rot.toFixed(2)}) scale(${s.toFixed(4)}) translate(-540 ${-cy})">${body}</g>`;
}

// ---------- the doodle gags that live on Dan's footage (source-frame coords) ----------
function hat(f, t) {           // the TECH GURU wizard hat, tracked onto his head, then flicked off
  const hq = P(t, 60.5, .35), e = eio(P(t, 61.55, .55)); if (hq <= 0 || e >= 1) return '';
  const k = f[2] / 440 * 1.08, hx = f[0], hy = f[1] - f[2] * .66;
  const strike = `<path d="M430 915 L655 905" stroke="${RED}" stroke-width="14" stroke-linecap="round" ${rf()} ${dv(P(t, 61.2, .25))}/>`;
  const art = `<g ${rf()} stroke="${INK}" stroke-width="7" stroke-linejoin="round"><path d="M410 1000 L540 640 L670 1000 Z" fill="#2B2A4A"/><ellipse cx="540" cy="1000" rx="210" ry="42" fill="#2B2A4A"/><path d="M510 760 l8 16 l18 2 l-13 12 l4 18 l-17 -9 l-17 9 l4 -18 l-13 -12 l18 -2z" fill="#FFD447" stroke-width="3"/></g><text x="540" y="930" class="t" font-size="36" font-weight="900" text-anchor="middle" fill="#fff">TECH GURU</text>${strike}`;
  const inner = pop(hq, 540, 1000, art, -12);
  return `<g transform="translate(${L(0, 900, e)} ${L(0, -700, e)}) rotate(${L(0, 80, e)} ${hx} ${hy})"><g transform="translate(${hx} ${hy}) rotate(-7) scale(${k.toFixed(4)}) translate(-540 -1000)">${mblur(inner, Math.sin(e * Math.PI) * 30, Math.sin(e * Math.PI) * 10)}</g></g>`;
}
function sticker(q, x, y, w, h, rot, inner) {
  if (q <= 0) return '';
  return pop(q, x + w / 2, y + h / 2, `<g transform="rotate(${rot} ${x + w / 2} ${y + h / 2})"><rect x="${x + 10}" y="${y + 12}" width="${w}" height="${h}" rx="18" fill="${INK}"/><rect x="${x}" y="${y}" width="${w}" height="${h}" rx="18" fill="${PAPER}" stroke="${INK}" stroke-width="7" ${rf()}/>${inner}</g>`);
}
function gags(t, f) {
  let s = '';
  // hook: red ink circle round the real combination lock he's pointing at
  if (t < 3.5) {const q = P(t, 2.45, .45); s += scrib(518, 1000, 118, 132, q, PAPER, 17) + scrib(518, 1000, 118, 132, q, RED, 9);
    s += burst(t, 2.8, 518, 1000, {n: 14, life: 1.0, type: 'spark', v: 700, g: 0});}
  // "one single offer": an index card slides in (it becomes the offer card on the cut)
  if (t >= 9.7 && t < 10.95) {const q = eo(P(t, 9.72, .4));
    s += `<g transform="translate(${L(700, 0, q)} 0) rotate(${L(12, -3, q)} 800 1520)">${card(0)}</g>`;}
  // $1.2M lands on Dan: sticker, cash burst, flash, shake
  if (t >= 23.9 && t < 27.5) {
    s += sticker(P(t, 24.15, .35), 200, 120, 330, 100, -6, T('an extra', 365, 190, {h: 1, s: 66, a: 'middle'}));
    s += sticker(P(t, 25.28, .4), 170, 215, 740, 250, -3, T('$1.2M', 540, 395, {s: 200, w: 900, a: 'middle', f: GREEN}));
    s += burst(t, 25.3, 540, 340, {n: 30, life: 1.8, type: 'cash'}) + burst(t, 25.36, 540, 340, {n: 26, life: 1.4, type: 'star', size: 26});
  }
  // "ridiculously easy": sparkle ticks round his head
  if (t >= 38.2 && t < 40) {const q = P(t, 38.4, .3);
    [[-1, -.2], [1, -.3], [-1.1, .35], [1.08, .3]].forEach(([a, b], i) => {const px = f[0] + a * f[2] * .78, py = f[1] + b * f[2];
      s += pop(P(t, 38.4 + i * .07, .3), px, py, `<path d="M${px} ${py - 34} L${px + 9} ${py - 9} L${px + 34} ${py} L${px + 9} ${py + 9} L${px} ${py + 34} L${px - 9} ${py + 9} L${px - 34} ${py} L${px - 9} ${py - 9}Z" fill="#FFD447" stroke="${INK}" stroke-width="5"/>`)});
    void q;}
  // tech guru hat
  if (t >= 60 && t < 62.3) s += hat(f, t);
  // "so pumped": energy dashes + amber bolts round his head
  if (t >= 64.4 && t < 65.9) {
    for (let i = 0; i < 10; i++) {const a = -Math.PI * .95 + i / 9 * Math.PI * .9 - .05, q = P(t, 64.6 + i * .025, .25), r0 = f[2] * .95, r1 = f[2] * 1.22;
      const x0 = f[0] + Math.cos(a) * r0, y0 = f[1] - f[2] * .1 + Math.sin(a) * r0, x1 = f[0] + Math.cos(a) * r1, y1 = f[1] - f[2] * .1 + Math.sin(a) * r1;
      const dd = `d="M${x0.toFixed(1)} ${y0.toFixed(1)} L${x1.toFixed(1)} ${y1.toFixed(1)}" stroke-linecap="round" ${dv(q)}`;
      s += `<path ${dd} stroke="${INK}" stroke-width="20"/><path ${dd} stroke="${PAPER}" stroke-width="10"/>`;}
    [[-1, 1], [1, -1]].forEach(([sd, r], i) => {const bx = f[0] + sd * f[2] * .95, by = f[1] + f[2] * .15;
      s += pop(P(t, 64.75 + i * .1, .3), bx, by, `<path d="M${bx + 10} ${by - 70} L${bx - 28} ${by + 6} L${bx + 2} ${by + 6} L${bx - 12} ${by + 70} L${bx + 32} ${by - 12} L${bx + 2} ${by - 12}Z" fill="${AMBER}" stroke="${INK}" stroke-width="6" stroke-linejoin="round"/>`, r * 20)});
  }
  // "keep it" sticker
  if (t >= 72.8 && t < 74.95) s += sticker(P(t, 72.95, .35), 600, 150, 400, 150, 4, T('keep it ✓', 800, 250, {s: 76, w: 900, a: 'middle', f: GREEN}));
  return s;
}
function card(fillOnly) {
  return `<rect x="610" y="1420" width="400" height="220" rx="14" fill="${INK}" transform="translate(9 11)"/><rect x="610" y="1420" width="400" height="220" rx="14" fill="#fff" stroke="${INK}" stroke-width="7" ${rf()}/>` +
    (fillOnly ? '' : `<rect x="650" y="1498" width="320" height="58" rx="8" fill="#FFE066" opacity=".9"/>` + T('one single offer', 810, 1545, {h: 1, s: 64, a: 'middle', f: INK}));
}

// ---------- geometry ----------
function rough(x, y, r, seed, n = 56) {let d = ''; for (let i = 0; i <= n; i++) {const a = i / n * Math.PI * 2, j = 1 + .018 * Math.sin(a * 5 + seed) + .012 * Math.sin(a * 11 + seed * 2.3);
  d += (i ? 'L' : 'M') + (x + r * j * Math.cos(a)).toFixed(1) + ' ' + (y + r * j * Math.sin(a)).toFixed(1) + ' ';} return d + 'Z'}
const FULL = 'M-60 -60 H1140 V1980 H-60 Z';
function faceAt(t) {return FACES[Math.max(0, Math.min(NF - 1, Math.round(t * FPS)))]}
function bubXf(f, B, t) {       // transform that puts Dan's face in the middle of bubble B
  const zoom = (t >= 39.84 && t < 50.96) ? 1.55 : 1.18;   // split-screen section: tighter, keeps his old captions out
  const s = zoom * B.r / f[2];
  return {s, tx: B.x - f[0] * s, ty: B.y + B.r * .1 - f[1] * s};
}
const SH = [[25.3, 22], [60.6, 6], [61.6, 7], [64.7, 8], [72.95, 5], [3.3, 8]];
function shake(t) {let x = 0, y = 0; for (const [t0, a] of SH) {const g = t - t0; if (g < 0 || g > .7) continue; const d = a * Math.exp(-g * 8); x += d * Math.sin(g * 83 + t0); y += d * Math.cos(g * 71 + t0 * 2);} return [x, y]}

// ---------- per-frame composite ----------
let IMG = null, IMG_N = -1;
function state(t) {
  const b = beat(t), f = faceAt(t), rs = Math.floor(t * 8) % 3;
  const B = b.o.end ? END : BUB;
  let xf = {s: 1, tx: 0, ty: 0}, clip = null, rim = '', extra = '', bubble = null;
  const [sx, sy] = shake(t);
  if (b.k === 'full') clip = FULL;
  else if (b.k === 'bubble' || b.k === 'bin' || b.k === 'bout') {
    const k = b.k === 'bin' ? bk(b.q) : b.k === 'bout' ? 1 - eio(b.q) : 1;
    if (k > .01) {const r = B.r * k; xf = bubXf(f, B, t); if (k < 1) {xf.s *= k; xf.tx = B.x - (B.x - xf.tx) * k; xf.ty = B.y - (B.y - xf.ty) * k;}
      clip = rough(B.x, B.y, r, rs); bubble = {x: B.x, y: B.y, r, k};}
  } else if (b.k === 'up' || b.k === 'down') {
    const u = eio(b.k === 'up' ? b.q : 1 - b.q), bx = bubXf(f, B, t);
    const s = Math.exp(L(Math.log(bx.s), 0, u));
    const fx = L(B.x, f[0], u), fy = L(B.y + B.r * .1, f[1], u);           // where the face sits on screen
    xf = {s, tx: fx - f[0] * s, ty: fy - f[1] * s};
    const r = L(B.r, 1200, u * u), ccx = L(B.x, 540, u), ccy = L(B.y, 960, u);
    clip = rough(ccx, ccy, r, rs); bubble = {x: ccx, y: ccy, r, k: 1, fade: 1 - P(u, .6, .4)};
  } else if (b.k === 'hole') {
    const e = eio(b.q), r = L(0, 1250, e * e * .6 + e * .4);
    clip = FULL + ' ' + rough(b.o.x, b.o.y, Math.max(r, 1), rs);
    rim = `<path d="${rough(b.o.x, b.o.y, Math.max(r, 1), rs)}" fill="none" stroke="${PAPER}" stroke-width="22"/><path d="${rough(b.o.x, b.o.y, Math.max(r, 1), rs)}" fill="none" stroke="${INK}" stroke-width="9"/>`;
  } else if (b.k === 'tear') {
    const Y = L(2080, -160, eio(b.q)); let d = '', pts = [];
    for (let i = 0; i <= 24; i++) {const x = -40 + i * 1160 / 24, y = Y + (x - 540) * -.12 + (i % 2 ? 26 : -18) + 14 * Math.sin(i * 1.7 + 2);
      pts.push([x, y]);}
    d = 'M' + pts.map(p => p.map(v => v.toFixed(1)).join(' ')).join(' L') + ' L1140 2000 L-60 2000 Z';
    clip = d;
    const line = 'M' + pts.map(p => p.map(v => v.toFixed(1)).join(' ')).join(' L');
    rim = `<path d="${line}" transform="translate(0 16)" fill="none" stroke="${INK}" stroke-width="26" opacity=".28"/><path d="${line}" fill="none" stroke="#FFFBF2" stroke-width="20"/><path d="${line}" transform="translate(0 -9)" fill="none" stroke="${INK}" stroke-width="4" opacity=".55"/>`;
  } else if (b.k === 'card') {
    const e = eio(b.q), x0 = L(610, -80, e), y0 = L(1420, -80, e), x1 = L(1010, 1160, e), y1 = L(1640, 2000, e);
    const cardP = `M${x0} ${y0} H${x1} V${y1} H${x0} Z`;
    clip = FULL + ' ' + cardP;
    rim = `<path d="${cardP}" fill="#fff" opacity="${(1 - P(e, 0, .45)).toFixed(3)}"/>` +
      `<g opacity="${(1 - P(e, 0, .3)).toFixed(3)}"><rect x="650" y="1498" width="320" height="58" rx="8" fill="#FFE066" opacity=".9"/>${T('one single offer', 810, 1545, {h: 1, s: 64, a: 'middle', f: INK})}</g>` +
      `<path d="${cardP}" fill="none" stroke="${INK}" stroke-width="${L(7, 14, e)}" ${rf()}/>`;
  }
  xf.tx += sx; xf.ty += sy;
  return {b, f, xf, clip, rim, bubble};
}
function render(t) {
  const st = state(t), {xf, clip, rim, bubble, f} = st;
  cx.clearRect(0, 0, 1080, 1920);
  let svg = '';
  if (clip) {
    const p = new Path2D(clip);
    if (bubble) {cx.save(); cx.globalAlpha = bubble.fade ?? 1; cx.fillStyle = INK; cx.translate(9, 11); cx.fill(p); cx.restore();}  // hard ink shadow, like the doodle badge
    cx.save(); cx.clip(p, 'evenodd');
    if (IMG) cx.drawImage(IMG, xf.tx, xf.ty, 1080 * xf.s, 1920 * xf.s);
    cx.restore();
    const inner = tape(t) + gags(t, f);
    svg += `<clipPath id="dc"><path d="${clip}" clip-rule="evenodd"/></clipPath><g clip-path="url(#dc)"><g transform="matrix(${xf.s.toFixed(5)} 0 0 ${xf.s.toFixed(5)} ${xf.tx.toFixed(2)} ${xf.ty.toFixed(2)})">${inner}</g></g>`;
    if (bubble) {
      const a = bubble.fade ?? 1;
      svg += `<path d="${clip}" fill="none" stroke="${INK}" stroke-width="8" opacity="${a.toFixed(3)}" ${rf()}/>`;
      const lk = st.b.o.end ? 1 : bubble.k;
      if (a > .05 && lk > .05 && bubble.r < 400) svg += `<g opacity="${(a * cl(lk)).toFixed(3)}">${T('Dan', bubble.x + bubble.r + 22, bubble.y + 22 + (st.b.o.end ? 8 : 0), {h: 1, s: st.b.o.end ? 88 : 66, rot: -5})}</g>`;
    }
    svg += rim;
  }
  // $1.2M flash lands on Dan's footage too
  const fl = t >= 25.3 && t < 25.6 ? .55 * (1 - (t - 25.3) / .3) : 0;
  if (fl > 0) svg += `<rect width="1080" height="1920" fill="#fff" opacity="${fl.toFixed(3)}"/>`;
  hy.innerHTML = svg;
}
window.seek = function (t) {doodleSeek(t); render(t)};
function frameUrl(n) {return FR + 'd' + String(n).padStart(5, '0') + '.jpg'}
window.renderAt = async function (t) {
  const n = Math.max(0, Math.min(NF - 1, Math.round(t * FPS)));
  if (n !== IMG_N) {const im = new Image(); im.src = frameUrl(n); await im.decode(); IMG = im; IMG_N = n;}
  window.seek(t);
  await document.fonts.ready;
  return true;
};

// ---------- sound: doodle cues only where the doodle is on screen, plus the hybrid's own ----------
const MINE = [
  // hook
  [2.45, 'scribble', -14, {dur: .45}], [2.8, 'sparkle', -18], [3.0, 'zoomwhoosh', -8, {dur: .5}], [3.02, 'scratch', -20, {dur: .4}],
  // tear into Dan
  [7.55, 'zip', -8], [7.58, 'paper', -10], [7.62, 'whoosh', -14, {dur: .4, hi: 3000}],
  // index card, then it becomes the offer card
  [9.72, 'swish', -12], [10.1, 'thump', -14], [10.95, 'zoomwhoosh', -8, {dur: .55}],
  // bubble in / out / morphs
  [11.85, 'pop', -11, {f0: 420}], [11.9, 'sparkle', -20],
  [21.0, 'zoomwhoosh', -10, {dur: .45}], [26.95, 'whoosh', -11, {dur: .45, hi: 4000}], [27.35, 'pop', -16],
  [37.2, 'zoomwhoosh', -10, {dur: .4}], [38.4, 'sparkle', -14], [38.45, 'pop', -16, {f0: 520}],
  [39.3, 'whoosh', -12, {dur: .45, hi: 4000}], [39.75, 'pop', -16],
  [50.6, 'whoosh', -14, {dur: .3, hi: 3500}],
  // $1.2M on Dan
  [24.1, 'scratch', -24, {dur: .5}], [23.9, 'riser', -14, {dur: 1.4}], [25.3, 'impact', -4], [25.33, 'kaching', -8], [25.36, 'sparkle', -14, {dur: 1.4}], [25.4, 'cash', -16, {dur: 1.4}],
  // tech guru hat
  [59.72, 'zip', -8], [59.75, 'paper', -10], [60.5, 'boing', -10], [60.52, 'pop', -12, {f0: 300}], [61.2, 'scribble', -12, {dur: .3}], [61.55, 'whoosh', -8, {dur: .55, hi: 4500}],
  [62.2, 'whoosh', -12, {dur: .45, hi: 4000}], [62.6, 'pop', -16],
  // pumped
  [64.15, 'zoomwhoosh', -10, {dur: .4}], [64.6, 'scribble', -18, {dur: .35}], [64.75, 'pop', -12, {f0: 600}], [64.85, 'pop', -12, {f0: 700}], [64.9, 'sparkle', -16],
  [65.55, 'zoomwhoosh', -8, {dur: .45}],
  // CTA + close
  [69.1, 'pop', -12, {f0: 420}], [71.5, 'zoomwhoosh', -10, {dur: .45}], [72.95, 'pop', -11], [73.0, 'ding', -14],
  [74.4, 'whoosh', -11, {dur: .5, hi: 4000}], [74.92, 'pop', -13],
];
window.collectCues = function () {
  const all = doodleCues();
  const kept = all.filter(c => doodleVis(c.t) >= .5 && !(c.t >= 23.8 && c.t < 25.6));
  const mine = MINE.map(([t, type, g, x]) => ({t, type, g, ...(x || {})}));
  window.seek(0);
  return [...kept, ...mine].sort((a, b) => a.t - b.t);
};
})();
