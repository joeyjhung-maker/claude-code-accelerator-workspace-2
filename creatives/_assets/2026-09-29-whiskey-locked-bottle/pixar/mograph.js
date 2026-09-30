// Motion-graphics layer for the Pixar version. Glossy, chunky, outlined shapes that match the 3D cartoon look.
// Everything is a pure function of t. Positions were mapped from gridded stills of build/base.mp4 (1080x1920).
const MG = (() => {
  const INK = '#1b1b24';
  const rnd = i => { const v = Math.sin(i * 127.1 + 311.7) * 43758.5453; return v - Math.floor(v); };
  const P = (t, s, d) => Math.max(0, Math.min(1, (t - s) / d));
  const eo = v => 1 - Math.pow(1 - v, 3);
  const bk = v => { if (v <= 0) return 0; if (v >= 1) return 1; const c1 = 2.2, c3 = c1 + 1; return 1 + c3 * Math.pow(v - 1, 3) + c1 * Math.pow(v - 1, 2); };
  const vis = (t, t0, t1, fin = .25, fout = .2) => Math.min(P(t, t0, fin), 1 - P(t, t1 - fout, fout));
  let x;

  function glossy(col, y0, y1) { const g = x.createLinearGradient(0, y0, 0, y1); g.addColorStop(0, shade(col, 40)); g.addColorStop(.55, col); g.addColorStop(1, shade(col, -35)); return g; }
  function shade(hex, p) { const n = parseInt(hex.slice(1), 16); let r = n >> 16, g = (n >> 8) & 255, b = n & 255; const f = v => Math.max(0, Math.min(255, Math.round(v + (p > 0 ? (255 - v) * p / 100 : v * p / 100)))); return `rgb(${f(r)},${f(g)},${f(b)})`; }
  function outlined(path, fill, lw = 10) { x.lineJoin = 'round'; x.lineCap = 'round'; x.save(); x.shadowColor = 'rgba(0,0,0,.35)'; x.shadowOffsetY = 10; x.fillStyle = INK; x.lineWidth = lw * 2; x.strokeStyle = INK; path(); x.stroke(); x.restore(); path(); x.fillStyle = fill; x.fill(); }

  // pill label
  function pill(txt, cx, cy, col, t, t0, t1, size = 66) {
    const q = vis(t, t0, t1); if (q <= 0) return; const s = bk(P(t, t0, .3)) * (1 - P(t, t1 - .15, .15));
    x.save(); x.translate(cx, cy + Math.sin(t * 5) * 4); x.rotate(Math.sin(t * 3) * .03); x.scale(s, s);
    x.font = `${size}px "Luckiest Guy"`; const w = x.measureText(txt).width + size * 1.1, h = size * 1.5;
    outlined(() => { x.beginPath(); x.roundRect(-w / 2, -h / 2, w, h, h / 2); }, glossy(col, -h / 2, h / 2), 7);
    x.fillStyle = 'rgba(255,255,255,.35)'; x.beginPath(); x.roundRect(-w / 2 + 10, -h / 2 + 6, w - 20, h * .3, h * .15); x.fill();
    x.fillStyle = '#fff'; x.textAlign = 'center'; x.textBaseline = 'middle'; x.lineWidth = size * .16; x.strokeStyle = INK; x.strokeText(txt, 0, 4); x.fillText(txt, 0, 4);
    x.restore();
  }
  // fat curved arrow drawn on from (ax,ay) to (bx,by), tip bobs at the target
  function arrow(ax, ay, bx, by, bend, col, t, t0, t1) {
    const q = vis(t, t0, t1); if (q <= 0) return; const d = eo(P(t, t0, .45)), bob = Math.sin((t - t0) * 9) * 10 * (d >= 1 ? 1 : 0);
    const mx = (ax + bx) / 2 + bend * (by - ay) * .35, my = (ay + by) / 2 - bend * (bx - ax) * .35;
    const pt = u => [(1 - u) * (1 - u) * ax + 2 * (1 - u) * u * mx + u * u * bx, (1 - u) * (1 - u) * ay + 2 * (1 - u) * u * my + u * u * by];
    const end = Math.max(.02, d * .88); const N = 30; const pts = []; for (let i = 0; i <= N; i++) pts.push(pt(end * i / N));
    const [ex, ey] = pts[N], [px, py] = pts[N - 2]; const ang = Math.atan2(ey - py, ex - px); const off = [Math.cos(ang) * bob, Math.sin(ang) * bob];
    x.save(); x.globalAlpha = q; x.translate(off[0], off[1]);
    x.lineCap = 'round'; x.lineJoin = 'round';
    const line = w => { x.beginPath(); pts.forEach(([u, v], i) => i ? x.lineTo(u, v) : x.moveTo(u, v)); x.lineWidth = w; x.stroke(); };
    x.save(); x.shadowColor = 'rgba(0,0,0,.35)'; x.shadowOffsetY = 10; x.strokeStyle = INK; line(46); x.restore();
    x.strokeStyle = col; line(28); x.strokeStyle = 'rgba(255,255,255,.35)'; x.lineWidth = 8; line(8);
    x.translate(ex, ey); x.rotate(ang);
    outlined(() => { x.beginPath(); x.moveTo(52, 0); x.lineTo(-18, -44); x.lineTo(-6, 0); x.lineTo(-18, 44); x.closePath(); }, glossy(col, -44, 44), 8);
    x.restore();
  }
  // pulsing target ring
  function ring(cx, cy, r, col, t, t0, t1) {
    const q = vis(t, t0, t1); if (q <= 0) return;
    for (let k = 0; k < 2; k++) { const ph = ((t - t0) * 1.2 + k * .5) % 1; x.save(); x.globalAlpha = q * (1 - ph) * .85; x.lineWidth = 12 * (1 - ph) + 3; x.strokeStyle = col; x.beginPath(); x.arc(cx, cy, r * (1 + ph * .45), 0, Math.PI * 2); x.stroke(); x.restore(); }
    x.save(); x.globalAlpha = q; x.setLineDash([26, 18]); x.lineDashOffset = -t * 90; x.lineWidth = 10; x.strokeStyle = INK; x.beginPath(); x.arc(cx, cy, r * bk(P(t, t0, .35)), 0, Math.PI * 2); x.stroke();
    x.lineWidth = 6; x.strokeStyle = col; x.stroke(); x.restore();
  }
  // comic speed lines converging on a point
  function speed(cx, cy, t, t0, t1, col = 'rgba(255,255,255,.75)') {
    const q = vis(t, t0, t1, .15, .25); if (q <= 0) return; x.save(); x.globalAlpha = q * .8; x.fillStyle = col;
    for (let i = 0; i < 46; i++) { const a = rnd(i * 3.3) * Math.PI * 2, r0 = 380 + rnd(i * 7.1 + Math.floor(t * 12)) * 260, r1 = 1500, w = 6 + rnd(i) * 16;
      x.beginPath(); x.moveTo(cx + Math.cos(a) * r0, cy + Math.sin(a) * r0); x.lineTo(cx + Math.cos(a + w / r1) * r1, cy + Math.sin(a + w / r1) * r1); x.lineTo(cx + Math.cos(a - w / r1) * r1, cy + Math.sin(a - w / r1) * r1); x.closePath(); x.fill(); }
    x.restore();
  }
  // starburst impact with an onomatopoeia word
  function impact(cx, cy, word, col, t, t0, dur = .7, r = 190) {
    const a = t - t0; if (a < 0 || a > dur) return; const s = bk(P(t, t0, .18)) * (1 - P(t, t0 + dur - .15, .15));
    x.save(); x.translate(cx, cy); x.rotate(-.12 + a * .3); x.scale(s, s);
    outlined(() => { x.beginPath(); for (let i = 0; i < 24; i++) { const ang = i / 24 * Math.PI * 2, rr = i % 2 ? r * .58 : r * (0.9 + rnd(i) * .2); x.lineTo(Math.cos(ang) * rr, Math.sin(ang) * rr); } x.closePath(); }, glossy(col, -r, r), 9);
    if (word) { x.rotate(.12); x.font = `${r * .42}px "Luckiest Guy"`; x.textAlign = 'center'; x.textBaseline = 'middle'; x.lineWidth = r * .08; x.strokeStyle = INK; x.strokeText(word, 0, 6); x.fillStyle = '#fff'; x.fillText(word, 0, 6); }
    x.restore();
  }
  // shockwave ring
  function shock(cx, cy, t, t0, col = '#ffffff', maxR = 520) { const a = P(t, t0, .45); if (a <= 0 || a >= 1) return; x.save(); x.globalAlpha = (1 - a) * .9; x.lineWidth = 26 * (1 - a) + 2; x.strokeStyle = col; x.beginPath(); x.arc(cx, cy, maxR * eo(a), 0, Math.PI * 2); x.stroke(); x.restore(); }
  // glossy 4-point sparkle stars
  function sparkles(cx, cy, spread, n, t, t0, t1, col = '#FFF3B0') {
    const q = vis(t, t0, t1, .2, .3); if (q <= 0) return;
    for (let i = 0; i < n; i++) { const ph = ((t - t0) * (0.9 + rnd(i) * .8) + rnd(i * 5)) % 1, s = Math.sin(ph * Math.PI) * (16 + rnd(i * 3) * 26);
      const px = cx + (rnd(i * 2.1) - .5) * spread * 2, py = cy + (rnd(i * 4.7) - .5) * spread * 2 - ph * 40;
      x.save(); x.globalAlpha = q; x.translate(px, py); x.rotate(ph * 1.5); x.fillStyle = col; x.shadowColor = col; x.shadowBlur = 18;
      x.beginPath(); x.moveTo(0, -s); x.quadraticCurveTo(0, 0, s, 0); x.quadraticCurveTo(0, 0, 0, s); x.quadraticCurveTo(0, 0, -s, 0); x.quadraticCurveTo(0, 0, 0, -s); x.fill(); x.restore(); }
  }
  // glossy gold coin
  function coin(px, py, r, spin) { x.save(); x.translate(px, py); x.scale(Math.max(.12, Math.abs(Math.cos(spin))), 1);
    outlined(() => { x.beginPath(); x.arc(0, 0, r, 0, Math.PI * 2); }, glossy('#F5B82E', -r, r), 5);
    x.strokeStyle = 'rgba(160,100,10,.8)'; x.lineWidth = r * .12; x.beginPath(); x.arc(0, 0, r * .7, 0, Math.PI * 2); x.stroke();
    x.fillStyle = '#FFF7C9'; x.font = `${r * 1.1}px "Luckiest Guy"`; x.textAlign = 'center'; x.textBaseline = 'middle'; x.fillText('$', 0, r * .08); x.restore(); }
  function coinRain(t, t0, t1, n = 34) { const q = vis(t, t0, t1, .1, .4); if (q <= 0) return; x.save(); x.globalAlpha = q;
    for (let i = 0; i < n; i++) { const sp = 700 + rnd(i) * 700, ph = ((t - t0) * sp / 2300 + rnd(i * 9)) % 1; coin(60 + rnd(i * 3.7) * 960, -80 + ph * 2100, 26 + rnd(i * 5) * 22, t * 6 + i); } x.restore(); }
  function coinBurst(cx, cy, t, t0, n = 26, dur = 1.4) { const a = t - t0; if (a < 0 || a > dur) return;
    for (let i = 0; i < n; i++) { const ang = -Math.PI / 2 + (rnd(i * 3.1 + t0) - .5) * 3.2, v = 900 + rnd(i * 7 + t0) * 900;
      x.save(); x.globalAlpha = 1 - P(a, dur * .7, dur * .3); coin(cx + Math.cos(ang) * v * a, cy + Math.sin(ang) * v * a + 1500 * a * a, 30 + rnd(i) * 16, a * 12 + i); x.restore(); } }
  // emote bubbles
  function bang(cx, cy, t, t0, t1, ch = '!', col = '#FF4D4D') { const q = vis(t, t0, t1); if (q <= 0) return; const s = bk(P(t, t0, .25));
    x.save(); x.translate(cx, cy + Math.sin((t - t0) * 12) * 6); x.rotate(Math.sin((t - t0) * 8) * .12); x.scale(s, s);
    x.font = '150px "Luckiest Guy"'; x.textAlign = 'center'; x.textBaseline = 'middle'; x.lineWidth = 22; x.strokeStyle = INK; x.strokeText(ch, 0, 0); x.fillStyle = glossy(col, -70, 70); x.fillText(ch, 0, 0); x.restore(); }
  function vein(cx, cy, t, t0, t1) { const q = vis(t, t0, t1); if (q <= 0) return; const s = bk(P(t, t0, .2)) * (1 + .12 * Math.sin((t - t0) * 20));
    x.save(); x.translate(cx, cy); x.scale(s, s); x.strokeStyle = '#E3261B'; x.lineWidth = 16; x.lineCap = 'round';
    for (let k = 0; k < 4; k++) { x.save(); x.rotate(k * Math.PI / 2 + .6); x.beginPath(); x.moveTo(14, 8); x.quadraticCurveTo(34, 10, 38, 34); x.stroke(); x.restore(); } x.restore(); }
  function sweat(cx, cy, t, t0, t1) { const q = vis(t, t0, t1); if (q <= 0) return;
    for (let i = 0; i < 3; i++) { const ph = ((t - t0) * 1.6 + i / 3) % 1, dir = i - 1; const px = cx + dir * 70 * ph, py = cy - 40 * Math.sin(ph * Math.PI) + ph * 60;
      x.save(); x.globalAlpha = q * (1 - ph * .6); x.translate(px, py); x.rotate(dir * .5);
      outlined(() => { x.beginPath(); x.moveTo(0, -30); x.quadraticCurveTo(22, 4, 0, 18); x.quadraticCurveTo(-22, 4, 0, -30); }, glossy('#7CC8FF', -30, 18), 4); x.restore(); } }
  function zzz(cx, cy, t, t0, t1) { const q = vis(t, t0, t1); if (q <= 0) return;
    for (let i = 0; i < 5; i++) { const ph = ((t - t0) * .45 + i / 5) % 1, sz = 50 + ph * 70;
      x.save(); x.globalAlpha = q * Math.sin(ph * Math.PI); x.translate(cx + Math.sin(ph * 6 + i) * 60 + ph * 120, cy - ph * 520); x.rotate(-.2 + Math.sin(ph * 5) * .2);
      x.font = `${sz}px "Luckiest Guy"`; x.textAlign = 'center'; x.lineWidth = sz * .18; x.strokeStyle = INK; x.strokeText('Z', 0, 0); x.fillStyle = glossy('#9FD4FF', -sz, 0); x.fillText('Z', 0, 0); x.restore(); } }
  function wobbleLines(cx, cy, r, t, t0, t1) { const q = vis(t, t0, t1); if (q <= 0) return; x.save(); x.globalAlpha = q; x.strokeStyle = '#fff'; x.lineWidth = 10; x.lineCap = 'round';
    for (let s = -1; s <= 1; s += 2) for (let k = 0; k < 3; k++) { const rr = r + k * 34 + Math.sin(t * 25 + k) * 8; x.beginPath(); x.arc(cx, cy, rr, s > 0 ? -.45 : Math.PI - .45, s > 0 ? .45 : Math.PI + .45); x.stroke(); } x.restore(); }
  function check(cx, cy, r, t, t0, t1) { const q = vis(t, t0, t1); if (q <= 0) return; const s = L2(2.2, 1, eo(P(t, t0, .22)));
    x.save(); x.globalAlpha = q * Math.min(1, P(t, t0, .1) * 3); x.translate(cx, cy); x.rotate(-.15); x.scale(s, s);
    outlined(() => { x.beginPath(); x.arc(0, 0, r, 0, Math.PI * 2); }, glossy('#3FCF6B', -r, r), 6);
    x.strokeStyle = '#fff'; x.lineWidth = r * .24; x.lineCap = 'round'; x.lineJoin = 'round'; x.beginPath(); x.moveTo(-r * .45, 0); x.lineTo(-r * .1, r * .35); x.lineTo(r * .5, -r * .38); x.stroke(); x.restore(); shock(cx, cy, t, t0, '#3FCF6B', r * 2.6); }
  const L2 = (a, b, v) => a + (b - a) * v;
  function pin(px, py, t, t0, t1 = 1e9) { const a = P(t, t0, .35); if (a <= 0 || t >= t1) return; const drop = (1 - bk(a)) * -160;
    x.save(); x.translate(px, py + drop); outlined(() => { x.beginPath(); x.moveTo(0, 0); x.bezierCurveTo(-26, -34, -26, -62, 0, -64); x.bezierCurveTo(26, -62, 26, -34, 0, 0); }, glossy('#FF4D4D', -64, 0), 5);
    x.fillStyle = '#fff'; x.beginPath(); x.arc(0, -40, 9, 0, Math.PI * 2); x.fill(); x.restore(); if (a >= 1) shock(px, py, t, t0 + .35, '#FFD447', 70); }
  function rays(cx, cy, r, col, t, t0, t1, n = 16) { const q = vis(t, t0, t1, .35, .3); if (q <= 0) return; x.save(); x.translate(cx, cy); x.rotate(t * .5); x.globalAlpha = q * .28; x.fillStyle = col;
    for (let i = 0; i < n; i++) { x.rotate(Math.PI * 2 / n); x.beginPath(); x.moveTo(0, 0); x.lineTo(r, -r * .1); x.lineTo(r, r * .1); x.fill(); } x.restore(); }
  function ribbons(t, t0, cols, dir = 1) { const a = P(t, t0 - .18, .45); if (a <= 0 || a >= 1) return;
    cols.forEach((c, i) => { const k = eo(Math.max(0, Math.min(1, a * 1.25 - i * .12))); if (k <= 0 || k >= 1) return; const off = L2(-1700, 1700, k) * dir;
      x.save(); x.translate(540 + off, 960 + (i - 1) * 260); x.rotate(-.35 * dir);
      outlined(() => { x.beginPath(); x.moveTo(-1200, -60); x.quadraticCurveTo(0, -150, 1200, -60); x.lineTo(1200, 60); x.quadraticCurveTo(0, -30, -1200, 60); x.closePath(); }, glossy(c, -120, 60), 8); x.restore(); }); }
  function vibe(cx, cy, t, t0, t1) { const q = vis(t, t0, t1); if (q <= 0) return; x.save(); x.globalAlpha = q; x.strokeStyle = '#FFD447'; x.lineCap = 'round';
    for (let s = -1; s <= 1; s += 2) for (let k = 0; k < 3; k++) { const on = Math.floor(t * 10 + k) % 2; if (!on) continue; x.lineWidth = 12; x.beginPath(); x.arc(cx, cy, 70 + k * 36, s > 0 ? -.6 : Math.PI - .6, s > 0 ? .6 : Math.PI + .6); x.stroke(); } x.restore(); }
  function confetti(t, t0, t1, n = 90) { const q = vis(t, t0, t1, .05, .4); if (q <= 0) return; const cols = ['#FFD447', '#4BE37E', '#6FB6FF', '#FF6B9A', '#FF8A3D', '#B47CFF'];
    for (let i = 0; i < n; i++) { const sp = 380 + rnd(i) * 520, ph = ((t - t0) * sp / 2100 + rnd(i * 3)) % 1; x.save(); x.globalAlpha = q; x.translate(rnd(i * 2.3) * 1080 + Math.sin(t * 3 + i) * 40, -40 + ph * 2000); x.rotate(t * 4 + i); x.scale(1, Math.cos(t * 7 + i));
      x.fillStyle = cols[i % cols.length]; x.strokeStyle = INK; x.lineWidth = 3; x.fillRect(-14, -8, 28, 16); x.strokeRect(-14, -8, 28, 16); x.restore(); } }
  function coinArc(ax, ay, bx, by, t, t0, dur = .8) { const a = P(t, t0, dur); if (a <= 0 || a >= 1) return; const e = eo(a); coin(L2(ax, bx, e), L2(ay, by, e) - Math.sin(e * Math.PI) * 260, 44, a * 16); }

  // camera punch: returns [scale, dx, dy]
  const HITS = [[2.0, .07], [4.3, .06], [18.5, .05], [25.3, .09], [30.1, .08], [42.3, .05], [59.9, .06], [66.25, .06], [74.7, .08]];
  function camera(t) { let s = 1, dx = 0, dy = 0; for (const [t0, a] of HITS) { const g = t - t0; if (g < 0 || g > .6) continue; const d = a * Math.exp(-g * 7) * Math.cos(g * 30);
    s += Math.max(0, a * Math.exp(-g * 6)); dx += d * 260 * Math.sin(g * 71); dy += d * 200 * Math.cos(g * 53); } return [s, dx, dy]; }

  // ---------------- timeline (drawn under the words) ----------------
  function draw(ctx, t) {
    x = ctx;
    // scene-change ribbon swooshes
    ribbons(t, 5.0, ['#FFD447', '#6FB6FF', '#FF6B9A'], 1); ribbons(t, 11.2, ['#6FB6FF', '#FFD447'], -1); ribbons(t, 22.0, ['#4BE37E', '#FFD447', '#4BE37E'], 1);
    ribbons(t, 31.6, ['#FFD447', '#FF8A3D'], -1); ribbons(t, 37.25, ['#6FB6FF', '#B47CFF'], 1); ribbons(t, 50.95, ['#B47CFF', '#6FB6FF', '#4BE37E'], -1);
    ribbons(t, 59.55, ['#FF6B9A', '#FFD447'], 1); ribbons(t, 66.2, ['#FFD447', '#FF8A3D', '#FFD447'], -1); ribbons(t, 74.65, ['#4BE37E', '#FF6B9A', '#6FB6FF'], 1);
    // 0-3: vault slides at camera
    speed(540, 920, t, .2, 2.4); shock(540, 920, t, 2.45); sparkles(540, 900, 260, 10, t, 2.45, 3.0);
    arrow(940, 1560, 700, 1150, -1, '#FFD447', t, 1.2, 3.0); pill('LOCKED!', 820, 1640, '#FF6B3D', t, 1.4, 3.0);
    // 3-5: the dial
    ring(540, 440, 170, '#FFD447', t, 3.05, 4.95); arrow(130, 1250, 330, 960, 1, '#FFD447', t, 3.2, 4.95); sparkles(540, 1050, 300, 10, t, 3.1, 4.95); 
    vein(640, 120, t, 3.1, 4.95); sweat(420, 150, t, 3.1, 4.95); impact(820, 440, 'BAM!', '#FF6B3D', t, 4.3, .7, 160);
    // 5-7.7: the tower
    speed(540, 200, t, 5.0, 6.0, 'rgba(255,255,255,.5)'); pin(540, 180, t, 5.4, 7.7); ring(540, 150, 90, '#FF4D4D', t, 5.7, 7.6); sparkles(540, 200, 200, 8, t, 5.6, 7.6);
    // 7.7-9.6: CEO + letter
    bang(705, 250, t, 8.0, 9.55, '?', '#6FB6FF'); ring(810, 1190, 110, '#FFD447', t, 7.85, 9.55); arrow(960, 1560, 860, 1290, -1, '#FFD447', t, 7.95, 9.55); pill('THE LETTER', 820, 1010, '#FF6B3D', t, 8.1, 9.55, 60);
    // 9.6-11.2: Dan answers instantly
    vibe(560, 810, t, 9.6, 10.2); bang(820, 560, t, 9.9, 11.15, '!', '#FFD447'); sparkles(620, 820, 220, 8, t, 9.8, 11.1);
    // 11.2-15: sleepy old leads
    zzz(640, 900, t, 11.3, 15.0); arrow(900, 420, 650, 900, 1, '#FFD447', t, 11.5, 14.9); pill('OLD LEADS', 780, 360, '#B47CFF', t, 11.6, 14.9);
    // 15-18.4: robot wakes them up
    for (let k = 0; k < 4; k++) shock(351, 379, t, 15.2 + k * .3, '#6FB6FF', 420);
    bang(380, 1230, t, 15.6, 18.3, '!', '#FF4D4D'); bang(560, 1170, t, 15.7, 18.3, '!', '#FFD447'); bang(730, 1240, t, 15.8, 18.3, '!', '#FF4D4D');
    // 18.4-22: jelly handshake
    impact(459, 1028, 'DEAL!', '#FFD447', t, 18.5, .8, 170); wobbleLines(700, 700, 240, t, 18.7, 21.0); sparkles(460, 1030, 200, 8, t, 19.0, 21.9);
    // 22-27: money rain
    coinRain(t, 22.3, 27.0); rays(540, 1080, 1100, '#FFE68A', t, 25.25, 27.0); coinBurst(540, 1080, t, 25.3, 30); bang(760, 880, t, 25.5, 26.9, '!', '#FF4D4D');
    // 27-31.6: the vault opens, thank-you envelope
    rays(540, 900, 1000, '#FFE68A', t, 27.05, 29.2, 20); sparkles(540, 900, 300, 16, t, 27.05, 29.2); rays(432, 487, 700, '#FFE68A', t, 29.2, 31.5); arrow(150, 1250, 380, 960, 1, '#4BE37E', t, 27.3, 29.15); 
    coinBurst(756, 1244, t, 30.1, 30); shock(756, 1244, t, 30.1, '#FFD447', 600);
    // 31.6-37.25: proud old leads, paid for
    [150, 320, 490, 660, 840].forEach((cx, i) => check(cx, 1080, 56, t, 33.3 + i * .12, 37.2));
    for (let i = 0; i < 10; i++) coinArc(150 + (i % 5) * 170, 1150, 940, 200, t, 35.0 + i * .18, .9);
    // 37.25-43.25: lightbulb moment
    rays(540, 270, 900, '#FFF3A0', t, 37.4, 43.2, 20); ring(540, 270, 170, '#FFD447', t, 37.6, 43.2); sparkles(540, 300, 320, 14, t, 37.6, 43.2); impact(820, 760, 'DING!', '#FFD447', t, 42.3, .7, 150);
    // 43.25-50.95: the pain
    sweat(560, 800, t, 43.4, 46.2); wobbleLines(620, 893, 170, t, 43.4, 46.2);
    vibe(180, 1150, t, 46.3, 48.8); vibe(900, 1100, t, 46.5, 48.8); vibe(540, 1250, t, 46.7, 48.8);
    bang(700, 300, t, 49.0, 50.9, '?', '#6FB6FF'); sweat(430, 330, t, 49.2, 50.9);
    // 50.95-59.55: the globe lights up
    x.save(); x.globalAlpha = vis(t, 51.0, 59.5); x.setLineDash([30, 20]); x.lineDashOffset = -t * 120; x.strokeStyle = '#FFD447'; x.lineWidth = 8; x.beginPath(); x.ellipse(540, 1163, 520, 150, -.25, 0, Math.PI * 2); x.stroke(); x.restore();
    for (let i = 0; i < 22; i++) { const a = rnd(i * 5.1) * Math.PI * 2, r = 330 * Math.sqrt(rnd(i * 3.3)); pin(540 + Math.cos(a) * r, 1163 + Math.sin(a) * r * .95, t, 54.6 + i * .1, 59.55); }
    sparkles(540, 1163, 520, 16, t, 51.2, 59.5);
    // 59.55-64.35: no tech guru, very simple
    impact(380, 560, 'POOF!', '#B47CFF', t, 59.9, .9, 200); ring(470, 560, 120, '#4BE37E', t, 62.3, 64.3); check(640, 420, 60, t, 63.1, 64.3);
    // 64.35-66.2: the magic pocket
    sparkles(560, 900, 260, 18, t, 64.4, 66.2, '#FFE68A'); speed(560, 900, t, 65.4, 66.2, 'rgba(255,240,180,.6)');
    // 66.2-71.55: the book
    rays(540, 1284, 1000, '#FFE68A', t, 66.25, 71.5, 22); sparkles(540, 1284, 380, 20, t, 66.3, 71.5); shock(540, 1284, t, 66.25, '#FFD447', 700);
    arrow(150, 1760, 300, 1450, 1, '#4BE37E', t, 69.0, 71.5); arrow(930, 1760, 780, 1450, -1, '#4BE37E', t, 69.1, 71.5);
    // 71.55-74.65: refund
    coinArc(540, 1500, 675, 780, t, 73.4, .9); sparkles(675, 780, 220, 10, t, 72.4, 74.6); check(880, 560, 62, t, 72.55, 74.6);
    // 74.65-77.6: finale
    confetti(t, 74.7, 77.6); shock(540, 540, t, 74.7, '#FFD447', 900); rays(540, 540, 1100, '#FFE68A', t, 74.7, 77.6); sparkles(540, 540, 300, 14, t, 74.8, 77.6); sparkles(594, 1515, 300, 12, t, 74.9, 77.6);
  }
  return { draw, camera };
})();
