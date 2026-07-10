/* ============ The Studio — map engine ============ */
'use strict';

const SVG_NS = 'http://www.w3.org/2000/svg';
const $ = (s) => document.querySelector(s);

/* ---------- shared palette ---------- */
const INK = '#2b1d12';
const PAL = {
  K: INK,               // outline
  S: '#958b76',         // stone light
  D: '#6a6051',         // stone dark
  W: '#eee4c6',         // plaster / white wall
  N: '#7a5230',         // wood
  n: '#5c3d22',         // wood dark
  R: '#8c4a32',         // roof warm
  r: '#6d3826',         // roof warm dark
  L: '#5d6e59',         // roof slate green
  l: '#48573f',         // slate dark
  G: '#c9962e',         // gold
  g: '#a67a1e',         // gold dark
  P: '#7b5296',         // palantír purple
  p: '#a67cc4',         // palantír light
  T: '#4e6b3a',         // tree green
  t: '#3c5430',         // tree dark
  F: '#e07028',         // fire
  M: '#b9c7cc',         // mithril / silver
  C: '#8a9bb0',         // cold stone blue
  y: 'WINDOW',          // window (status-coloured)
  h: '#d8c48e',         // path/step light
};

/* ---------- sprites (rows of palette chars, '.' = empty) ---------- */
const SPRITES = {
  tower: [
    '......ppp......',
    '.....pPPPp.....',
    '.....pPPPp.....',
    '......ppp......',
    '....KKKKKKK....',
    '....KSKSKSK....',
    '....KSSDSSK....',
    '.....KSDSK.....',
    '.....KSSSK.....',
    '.....KSySK.....',
    '.....KSSSK.....',
    '.....KDSSK.....',
    '.....KSSDK.....',
    '.....KSySK.....',
    '.....KSSSK.....',
    '....KKSSDKK....',
    '...KSSSDSSSK...',
    '...KSDSSSDSK...',
    '...KSSSySSSK...',
    '..KKKKKKKKKKK..',
    '..hhhhhhhhhhh..',
  ],
  mine: [
    '.......KK..........',
    '......KDDK.....KK..',
    '.....KDSSDK...KDDK.',
    '....KDSSSSDK.KDSSDK',
    '...KDSSDSSSDKDSSDDK',
    '..KDSSSSSDSSDSSDSDK',
    '.KDSSDSSSSSSDSSSSDK',
    'KDSSSSSKKKKKSSDSSDK',
    'KDSSDSKKgGgKKSSSSDK',
    'KSSSSKKgGGGgKKDSSDK',
    'KDSSDKK.....KKSSSDK',
    'KKKKKKK..y..KKKKKKK',
    'hhhhhKK.....KKhhhhh',
  ],
  weathertop: [
    '...KK......KK......KK...',
    '..KCCK....KCCK....KCCK..',
    '..KCCK....KCCK....KCCK..',
    '..KCSCK...KCCK...KCSCK..',
    '...KCCK...KSCK...KCCK...',
    '..KCSCK....KK....KCSCK..',
    '..KCCCK..........KCCCK..',
    '.KCCKCCKK..yy..KKCCKCCK.',
    '.KTTTTTTTTTTTTTTTTTTTT.',
    'KTTtTTTTtTTTTTtTTTTtTTK',
    'KTtTTTTTTTtTTTTTTtTTTtK',
    'KKKKKKKKKKKKKKKKKKKKKKK',
  ],
  council: [
    '.........KK.........',
    '......KKKLLKKK......',
    '....KKLLLLLLLLKK....',
    '..KKLLLLLLLLLLLLKK..',
    '.KLLLLKKKKKKKKLLLLK.',
    '..KKKKKWWWWWWKKKKK..',
    '...KWKWWyWWyWWKWK...',
    '...KWKWWWWWWWWKWK...',
    '...KWKWWyKKyWWKWK...',
    '...KWKWWWKKWWWKWK...',
    '..KKKKKKKKKKKKKKKK..',
    '..hhhhhhhhhhhhhhhh..',
  ],
  forge: [
    '....KK..............',
    '...KDDK.............',
    '...KDDK....KKKKK....',
    '..KKDDKKKKKrRRRrK...',
    '.KrRRRRRRRrKRRRK....',
    'KrRRRRRRRRRrKKKKK...',
    'KKKKKKKKKKKKKSSDK...',
    '.KSSDSSSSDSKKSSSK...',
    '.KSSySSDSSSKKDSSK...',
    '.KSSSSKKKSSKKSSDK...',
    '.KDSSSKFFKSSKKKKK...',
    '.KSSDSKFFKSDSKnNK...',
    'KKKKKKKKKKKKKKKKKK..',
    'hhhhhhhhhhhhhhhhhh..',
  ],
  library: [
    '........KKK........',
    '......KKGGGKK......',
    '.....KGGgGgGGK.....',
    '....KGGGGGGGGGK....',
    '...KKKKKKKKKKKKK...',
    '...KWWWWWWWWWWWK...',
    '...KWyWWKKKWWyWK...',
    '...KWWWWKNKWWWWK...',
    '...KWyWWKNKWWyWK...',
    '...KWWWWKNKWWWWK...',
    '..KKKKKKKKKKKKKKK..',
    '..hhhhhhhhhhhhhhh..',
  ],
  hall: [
    '.........KK.........',
    '.......KKGGKK.......',
    '.....KKGGGGGGKK.....',
    '...KKGGgGGGGgGGKK...',
    '.KKGGGGGGGGGGGGGGKK.',
    'KGGKKKKKKKKKKKKKKGGK',
    '.KKKNWWNWWWWNWWNKKK.',
    '...KNWyNWKKWNyWNK...',
    '...KNWWNWKKWNWWNK...',
    '...KNWyNWKKWNyWNK...',
    '..KKKKKKKKKKKKKKKK..',
    '..hhhhhhhhhhhhhhhh..',
  ],
  pine: [
    '...K...',
    '..KTK..',
    '.KTtTK.',
    '..KTK..',
    '.KTTtK.',
    'KTtTTTK',
    '...N...',
    '...N...',
  ],
  wanderer1: [
    '..KKK..',
    '.KDDDK.',
    '.KDDDK.',
    '..KWK..',
    'K.KNK.K',
    'KNNNNNK',
    '.KNNNK.',
    '..K.K..',
    '..K..K.',
  ],
  wanderer2: [
    '..KKK..',
    '.KDDDK.',
    '.KDDDK.',
    '..KWK..',
    'K.KNK.K',
    'KNNNNNK',
    '.KNNNK.',
    '..K.K..',
    '.K..K..',
  ],
};

/* ---------- rooms ---------- */
const ROOMS = {
  tower: {
    name: 'The Palantír Tower', pos: [180, 555], scale: 3.4,
    sub: 'account read & the Monday sweep — watch the market',
    plaque: 'Palantír Tower',
    count: (r) => `${r.files.length} scrolls`,
    smoke: null,
  },
  mine: {
    name: 'The Deep Mine', pos: [335, 205], scale: 3.2,
    sub: 'research — swipes, the market’s own words, VOC',
    plaque: 'The Deep Mine',
    count: (r) => `${r.files.length} veins`,
    smoke: null,
  },
  weathertop: {
    name: 'Weathertop', pos: [520, 300], scale: 3.0,
    sub: '/storm — seed the bank',
    plaque: 'Weathertop',
    count: (r) => `${r.seedsTotal || 0} seeds`,
    smoke: null,
  },
  council: {
    name: 'The Council Hall', pos: [700, 195], scale: 3.3,
    sub: '/brief — the council locks the DNA',
    plaque: 'Council Hall',
    count: (r) => `${r.briefsReady || 0} ready · ${r.briefsWritten || 0} written`,
    smoke: null,
  },
  forge: {
    name: 'The Forge', pos: [880, 305], scale: 3.3,
    sub: '/produce — mariobot hammers, the judge grades',
    plaque: 'The Forge',
    count: (r) => `${r.copyCount || 0} blades · ${r.copyThisWeek || 0} this week`,
    smoke: [4.5, 0.5], // sprite coords of chimney top
  },
  library: {
    name: 'The Library', pos: [585, 505], scale: 3.1,
    sub: 'the books — voice, hooks, the rubric, the Lock',
    plaque: 'The Library',
    count: (r) => `${r.files.length} books`,
    smoke: null,
  },
  hall: {
    name: 'The Golden Hall', pos: [1075, 215], scale: 3.3,
    sub: 'winners on the wall · losers in the barrow below',
    plaque: 'Golden Hall',
    count: (r) => `${r.winners || 0} won · ${r.losers || 0} fell`,
    smoke: null,
  },
};

const ROAD = 'M180,565 C205,470 250,262 335,215 C425,172 445,270 520,303 C598,333 628,203 700,201 C782,198 802,273 880,315 C958,348 1000,240 1075,226';
const SPUR = 'M523,303 C543,384 562,440 585,512';

/* ---------- sprite renderer ---------- */
function drawSprite(rows, scale, palOverride) {
  const g = document.createElementNS(SVG_NS, 'g');
  g.setAttribute('class', 'sprite');
  const w = rows[0].length, h = rows.length;
  rows.forEach((row, ry) => {
    for (let rx = 0; rx < row.length; rx++) {
      const ch = row[rx];
      if (ch === '.') continue;
      const col = (palOverride && palOverride[ch]) || PAL[ch];
      if (!col) continue;
      const rect = document.createElementNS(SVG_NS, 'rect');
      rect.setAttribute('x', rx * scale);
      rect.setAttribute('y', ry * scale);
      rect.setAttribute('width', scale);
      rect.setAttribute('height', scale);
      if (col === 'WINDOW') {
        rect.setAttribute('class', 'win');
        rect.setAttribute('fill', '#4a5a78');
      } else {
        rect.setAttribute('fill', col);
      }
      g.appendChild(rect);
    }
  });
  g.dataset.w = w * scale;
  g.dataset.h = h * scale;
  return g;
}

/* ---------- map assembly ---------- */
function buildMap() {
  const svg = $('#map');

  // backdrop mountains (NE corner) + vignette
  const deco = document.createElementNS(SVG_NS, 'g');
  deco.innerHTML = `
    <path d="M900,90 L950,38 L1000,90 Z" fill="#b7a476" stroke="${INK}" stroke-width="2"/>
    <path d="M955,95 L1020,26 L1085,95 Z" fill="#c3b183" stroke="${INK}" stroke-width="2"/>
    <path d="M1008,40 L1020,26 L1032,40 L1020,52 Z" fill="#efe8d2"/>
    <path d="M1060,100 L1105,55 L1150,100 Z" fill="#b7a476" stroke="${INK}" stroke-width="2"/>
    <text x="1023" y="122" text-anchor="middle" font-size="17" fill="#6b543a" font-style="italic">the misty mountains</text>
  `;
  svg.appendChild(deco);

  // roads
  for (const [d, dash] of [[ROAD, '2 9'], [SPUR, '2 9']]) {
    const p = document.createElementNS(SVG_NS, 'path');
    p.setAttribute('d', d);
    p.setAttribute('fill', 'none');
    p.setAttribute('stroke', '#6b543a');
    p.setAttribute('stroke-width', '3.5');
    p.setAttribute('stroke-dasharray', dash);
    p.setAttribute('stroke-linecap', 'round');
    if (d === ROAD) p.id = 'roadpath';
    svg.appendChild(p);
  }

  // scattered pines
  [[225, 300, 2.6], [415, 145, 2.2], [640, 420, 2.4], [520, 460, 2.2], [960, 140, 2.2], [770, 380, 2.6], [190, 150, 2.2], [1120, 330, 2.6]]
    .forEach(([x, y, s]) => {
      const t = drawSprite(SPRITES.pine, s);
      t.setAttribute('transform', `translate(${x - (7 * s) / 2}, ${y - 8 * s})`);
      svg.appendChild(t);
    });

  // rooms
  for (const [id, cfg] of Object.entries(ROOMS)) {
    const group = document.createElementNS(SVG_NS, 'g');
    group.setAttribute('class', 'room quiet');
    group.id = `room-${id}`;
    group.setAttribute('tabindex', '0');
    group.setAttribute('role', 'button');
    group.setAttribute('aria-label', cfg.name);

    const sprite = drawSprite(SPRITES[id], cfg.scale);
    const w = +sprite.dataset.w, h = +sprite.dataset.h;
    const ox = cfg.pos[0] - w / 2, oy = cfg.pos[1] - h;

    // halo behind the building
    const halo = document.createElementNS(SVG_NS, 'ellipse');
    halo.setAttribute('class', 'halo');
    halo.setAttribute('cx', cfg.pos[0]);
    halo.setAttribute('cy', cfg.pos[1] - h / 2.2);
    halo.setAttribute('rx', w * 0.75);
    halo.setAttribute('ry', h * 0.62);
    halo.setAttribute('fill', '#ffd76a');
    halo.setAttribute('opacity', '0');
    group.appendChild(halo);

    sprite.setAttribute('transform', `translate(${ox}, ${oy})`);
    group.appendChild(sprite);

    // smoke (forge chimney or generic rooftop)
    const sm = document.createElementNS(SVG_NS, 'g');
    sm.setAttribute('class', 'smoke');
    const [scx, scy] = cfg.smoke
      ? [ox + cfg.smoke[0] * cfg.scale, oy + cfg.smoke[1] * cfg.scale]
      : [cfg.pos[0], oy - 2];
    for (let i = 0; i < 3; i++) {
      const c = document.createElementNS(SVG_NS, 'circle');
      c.setAttribute('cx', scx); c.setAttribute('cy', scy); c.setAttribute('r', 4);
      sm.appendChild(c);
    }
    group.appendChild(sm);

    // plaque
    const plaque = document.createElementNS(SVG_NS, 'g');
    plaque.setAttribute('class', 'plaque');
    const t1 = document.createElementNS(SVG_NS, 'text');
    t1.setAttribute('x', cfg.pos[0]);
    t1.setAttribute('y', cfg.pos[1] + 22);
    t1.setAttribute('text-anchor', 'middle');
    t1.setAttribute('font-size', '21');
    t1.setAttribute('fill', INK);
    t1.textContent = cfg.plaque;
    const t2 = document.createElementNS(SVG_NS, 'text');
    t2.setAttribute('x', cfg.pos[0]);
    t2.setAttribute('y', cfg.pos[1] + 41);
    t2.setAttribute('text-anchor', 'middle');
    t2.setAttribute('font-size', '17');
    t2.setAttribute('fill', '#6b543a');
    t2.setAttribute('class', 'countline');
    t2.textContent = '…';
    plaque.appendChild(t1); plaque.appendChild(t2);
    group.appendChild(plaque);

    group.addEventListener('click', () => openRoom(id));
    group.addEventListener('keydown', (e) => { if (e.key === 'Enter') openRoom(id); });
    svg.appendChild(group);
  }

  // the wanderer walks the road
  const wg = document.createElementNS(SVG_NS, 'g');
  wg.id = 'wanderer';
  const f1 = drawSprite(SPRITES.wanderer1, 2.6);
  f1.setAttribute('class', 'sprite frame1');
  f1.setAttribute('transform', 'translate(-9,-22)');
  const f2 = drawSprite(SPRITES.wanderer2, 2.6);
  f2.setAttribute('class', 'sprite frame2');
  f2.setAttribute('transform', 'translate(-9,-22)');
  wg.appendChild(f1); wg.appendChild(f2);
  const motion = document.createElementNS(SVG_NS, 'animateMotion');
  motion.setAttribute('dur', '150s');
  motion.setAttribute('repeatCount', 'indefinite');
  motion.setAttribute('keyPoints', '0;1;0');
  motion.setAttribute('keyTimes', '0;0.5;1');
  motion.setAttribute('calcMode', 'linear');
  const mpath = document.createElementNS(SVG_NS, 'mpath');
  mpath.setAttribute('href', '#roadpath');
  motion.appendChild(mpath);
  wg.appendChild(motion);
  svg.appendChild(wg);
  setInterval(() => wg.classList.toggle('step'), 320);

  // vignette on top
  const vg = document.createElementNS(SVG_NS, 'rect');
  vg.setAttribute('x', 0); vg.setAttribute('y', 0);
  vg.setAttribute('width', 1200); vg.setAttribute('height', 700);
  vg.setAttribute('fill', 'url(#vignette)');
  vg.setAttribute('pointer-events', 'none');
  svg.appendChild(vg);
}

/* ---------- state ---------- */
let STATE = null;

async function refresh() {
  try {
    const res = await fetch('/api/state');
    STATE = await res.json();
  } catch {
    return; // server hiccup; keep last state
  }
  for (const [id, cfg] of Object.entries(ROOMS)) {
    const room = STATE.rooms[id];
    if (!room) continue;
    const g = $(`#room-${id}`);
    g.classList.remove('hot', 'warm', 'quiet');
    g.classList.add(room.status);
    g.querySelector('.countline').textContent = cfg.count(room);
  }
  renderQuest();
}

function renderQuest() {
  const q = STATE.quest;
  const rows = [
    ['Seeds banked', q.seedsTotal],
    ['Briefs ready', q.briefsReady],
    ['Briefs written', q.briefsWritten],
    ['Forged this week', q.copyThisWeek],
    ['Winners', q.winners],
  ];
  $('#quest-stats').innerHTML = rows
    .map(([k, v]) => `<li><span>${k}</span><span class="v">${v}</span></li>`)
    .join('');
  let next;
  if (!q.latestRead) next = '&#9888; No quest scroll yet — <b>/account-read</b> starts the week.';
  else if (q.briefsReady > 0) next = `&#9876; ${q.briefsReady} brief${q.briefsReady > 1 ? 's' : ''} await the Forge — <b>/produce</b>.`;
  else if (q.seedsTotal > 0) next = `&#10022; ${q.seedsTotal} seeds wait at the Council — pick numbers, <b>/brief</b>.`;
  else next = '&#10022; The bank is empty — <b>/storm</b> for seeds.';
  $('#quest-next').innerHTML = next;
}

/* ---------- the scroll (room panel) ---------- */
const overlay = $('#overlay');
let currentRoom = null;

function ago(mtime) {
  const s = (Date.now() - mtime) / 1000;
  if (s < 90) return 'just now';
  if (s < 3600) return `${Math.round(s / 60)}m ago`;
  if (s < 86400) return `${Math.round(s / 3600)}h ago`;
  return `${Math.round(s / 86400)}d ago`;
}

function cleanName(name) {
  return name.replace(/\.md$|\.txt$/i, '').replace(/[-_]/g, ' ');
}

const FICON = `<svg class="ficon" viewBox="0 0 7 8"><rect width="7" height="8" fill="#efe4c0"/><path d="M0,0 h7 v8 h-7 z" fill="none" stroke="${INK}" stroke-width="1.6"/><rect x="1.5" y="2" width="4" height="1" fill="#6b543a"/><rect x="1.5" y="4" width="4" height="1" fill="#6b543a"/></svg>`;

function fileRow(f) {
  const badges = [];
  if (f.status) badges.push(`<span class="badge ${f.status}">${f.status}</span>`);
  if (typeof f.seeds === 'number') badges.push(`<span class="badge seedcount">${f.seeds} seeds</span>`);
  if (f.extra) badges.push(`<span class="badge outside">outside vault</span>`);
  if (Date.now() - f.mtime < 86400000) badges.push(`<span class="badge new">new</span>`);
  return `<li data-p="${encodeURIComponent(f.path)}" data-n="${encodeURIComponent(f.name)}">
    ${FICON}<span class="fname">${cleanName(f.name)}</span>${badges.join('')}
    <span class="fage">${ago(f.mtime)}</span></li>`;
}

function groupFor(id, f) {
  if (id === 'hall') return f.path.startsWith('losers') ? 'The Barrow (what fell, and why)' : 'The Hall (what won, and why)';
  if (id === 'mine') {
    if (f.extra) return 'Scrolls from beyond the vault (VOC)';
    if (f.path.includes('swipe-bank/organic')) return 'Organic finds';
    if (f.path.includes('swipe-bank')) return 'The swipe bank';
    if (f.path.startsWith('swipes')) return 'House swipes';
    return 'Pattern readings';
  }
  if (id === 'forge') return f.path.startsWith('creatives') ? 'Creatives' : 'Copy';
  if (id === 'library') {
    if (f.path.startsWith('brand')) return 'Brand shelf';
    if (f.path.startsWith('concepts')) return 'Concept shelf';
    if (f.path.startsWith('rubrics')) return 'The judge’s shelf';
    return 'The Script & maps';
  }
  return null;
}

function openRoom(id) {
  currentRoom = id;
  const cfg = ROOMS[id];
  const room = STATE && STATE.rooms[id];
  $('#scroll-title').textContent = cfg.name;
  $('#scroll-sub').textContent = cfg.sub;
  const body = $('#scroll-body');

  if (!room || room.files.length === 0) {
    const hints = {
      tower: 'No scrolls yet. <b>/account-read</b> writes the first quest scroll; the Monday sweep fills the leaderboard.',
      weathertop: 'The seed bank is empty. <b>/storm</b> fills it.',
      council: 'No briefs yet. Pick seeds by number and <b>/brief</b> them.',
      forge: 'Nothing forged yet. A locked brief + <b>/produce</b> makes the first blade.',
      hall: 'No trophies yet — they arrive via <b>/reflect</b> when a winner is promoted.',
    };
    body.innerHTML = `<div class="empty">${hints[id] || 'Nothing here yet.'}</div>`;
  } else {
    // stats row
    let stats = `<div class="statrow"><span class="stat"><b>${room.files.length}</b> files</span>`;
    if (id === 'weathertop') stats += `<span class="stat"><b>${room.seedsTotal}</b> seeds</span>`;
    if (id === 'council') stats += `<span class="stat"><b>${room.briefsReady}</b> ready</span><span class="stat"><b>${room.briefsWritten}</b> written</span>`;
    if (id === 'forge') stats += `<span class="stat"><b>${room.copyThisWeek}</b> this week</span>`;
    if (id === 'hall') stats += `<span class="stat"><b>${room.winners}</b> winners</span><span class="stat"><b>${room.losers}</b> losers</span>`;
    stats += `<span class="stat">last work <b>${ago(room.lastActivity)}</b></span></div>`;

    // grouped file list
    const groups = new Map();
    for (const f of room.files) {
      const gname = groupFor(id, f);
      if (!groups.has(gname)) groups.set(gname, []);
      groups.get(gname).push(f);
    }
    let html = stats;
    for (const [gname, files] of groups) {
      if (gname) html += `<div class="groupHead">${gname}</div>`;
      html += `<ul class="filelist">${files.map(fileRow).join('')}</ul>`;
    }
    body.innerHTML = html;
    body.querySelectorAll('.filelist li').forEach((li) => {
      li.addEventListener('click', () => openFile(decodeURIComponent(li.dataset.p), decodeURIComponent(li.dataset.n)));
    });
  }
  overlay.hidden = false;
}

async function openFile(p, name) {
  const body = $('#scroll-body');
  body.innerHTML = `<div class="empty">unrolling…</div>`;
  let data;
  try {
    const res = await fetch(`/api/file?p=${encodeURIComponent(p)}`);
    data = await res.json();
    if (data.error) throw new Error(data.error);
  } catch (e) {
    body.innerHTML = `<div class="empty">Could not read this scroll: ${e.message}</div>`;
    return;
  }
  body.innerHTML = `
    <div class="backbar"><button id="backbtn">&larr; back to the room</button></div>
    <div class="doc">${renderMarkdown(data.content)}</div>`;
  $('#backbtn').addEventListener('click', () => openRoom(currentRoom));
  body.scrollTop = 0;
}

function closeScroll() { overlay.hidden = true; }
$('#scroll-close').addEventListener('click', closeScroll);
overlay.addEventListener('click', (e) => { if (e.target === overlay) closeScroll(); });
document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeScroll(); });

/* ---------- tiny markdown renderer ---------- */
function esc(s) {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function inline(s) {
  return s
    .replace(/\[\[([^\]]+)\]\]/g, '<mark>$1</mark>')
    .replace(/!\[[^\]]*\]\([^)]*\)/g, '')
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>')
    .replace(/\*\*([^*]+)\*\*/g, '<b>$1</b>')
    .replace(/(^|\W)\*([^*\n]+)\*(?=\W|$)/g, '$1<i>$2</i>')
    .replace(/`([^`]+)`/g, '<code>$1</code>');
}

function renderMarkdown(src) {
  let text = src.replace(/\r\n/g, '\n');
  let out = '';

  // frontmatter → DNA plate
  if (text.startsWith('---')) {
    const end = text.indexOf('\n---', 3);
    if (end !== -1) {
      const fm = text.slice(3, end).trim();
      text = text.slice(end + 4);
      const items = fm.split('\n').map((l) => {
        const m = l.match(/^([\w-]+):\s*(.*)$/);
        return m ? `<dt>${esc(m[1])}</dt><dd>${inline(esc(m[2]))}</dd>` : '';
      }).join('');
      if (items) out += `<dl class="dna">${items}</dl>`;
    }
  }

  const lines = text.split('\n');
  let i = 0, para = [], list = null;

  const flushPara = () => {
    if (para.length) { out += `<p>${para.map((l) => inline(esc(l))).join('<br>')}</p>`; para = []; }
  };
  const flushList = () => {
    if (list) { out += `<${list.tag}>${list.items.map((x) => `<li>${x}</li>`).join('')}</${list.tag}>`; list = null; }
  };

  while (i < lines.length) {
    const line = lines[i];

    if (line.startsWith('```')) {
      flushPara(); flushList();
      const buf = [];
      i++;
      while (i < lines.length && !lines[i].startsWith('```')) { buf.push(lines[i]); i++; }
      out += `<pre>${esc(buf.join('\n'))}</pre>`;
      i++; continue;
    }
    if (/^\|.*\|\s*$/.test(line)) {
      flushPara(); flushList();
      const rows = [];
      while (i < lines.length && /^\|.*\|\s*$/.test(lines[i])) { rows.push(lines[i]); i++; }
      const cells = (r) => r.replace(/^\||\|$/g, '').split('|').map((c) => inline(esc(c.trim())));
      let table = '<table>';
      rows.forEach((r, idx) => {
        if (/^\|[\s:|-]+\|$/.test(r)) return; // separator row
        const tag = idx === 0 ? 'th' : 'td';
        table += `<tr>${cells(r).map((c) => `<${tag}>${c}</${tag}>`).join('')}</tr>`;
      });
      out += table + '</table>';
      continue;
    }
    const h = line.match(/^(#{1,4})\s+(.*)$/);
    if (h) {
      flushPara(); flushList();
      const lvl = Math.min(h[1].length, 3);
      out += `<h${lvl}>${inline(esc(h[2]))}</h${lvl}>`;
      i++; continue;
    }
    if (/^(---+|\*\*\*+)\s*$/.test(line)) { flushPara(); flushList(); out += '<hr>'; i++; continue; }
    if (/^>\s?/.test(line)) {
      flushPara(); flushList();
      const buf = [];
      while (i < lines.length && /^>\s?/.test(lines[i])) { buf.push(lines[i].replace(/^>\s?/, '')); i++; }
      out += `<blockquote>${buf.map((l) => inline(esc(l))).join('<br>')}</blockquote>`;
      continue;
    }
    const ul = line.match(/^\s*[-*]\s+(.*)$/);
    const ol = line.match(/^\s*\d+\.\s+(.*)$/);
    if (ul || ol) {
      flushPara();
      const tag = ul ? 'ul' : 'ol';
      if (!list || list.tag !== tag) { flushList(); list = { tag, items: [] }; }
      list.items.push(inline(esc((ul || ol)[1])));
      i++; continue;
    }
    if (line.trim() === '') { flushPara(); flushList(); i++; continue; }
    para.push(line);
    i++;
  }
  flushPara(); flushList();
  return out;
}

/* ---------- boot ---------- */
buildMap();
refresh();
setInterval(refresh, 30000);
window.addEventListener('focus', refresh);
