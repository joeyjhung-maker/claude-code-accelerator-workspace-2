/* ============ The Studio — shared core ============ */
/* view-agnostic: state, room meta, the scroll panel, markdown, the quest log,
   and a tiny view registry so the map and the office can share all of it. */
'use strict';

const SVG_NS = 'http://www.w3.org/2000/svg';
const $ = (s) => document.querySelector(s);

/* ---------- room meta (shared by every view) ---------- */
const META = {
  tower:      { name: 'The Watch Room',   sub: 'account read & the Monday sweep — watch the market',
                count: (r) => `${r.files.length} scrolls` },
  mine:       { name: 'The Mines',        sub: 'research — swipes, the market’s own words, VOC',
                count: (r) => `${r.files.length} veins` },
  weathertop: { name: 'The Storm Room',   sub: '/storm — seed the bank',
                count: (r) => `${r.seedsTotal || 0} seeds` },
  council:    { name: 'The Council Hall', sub: '/brief — the council locks the DNA',
                count: (r) => `${r.briefsReady || 0} ready · ${r.briefsWritten || 0} written` },
  forge:      { name: 'The Forge',        sub: '/produce — mariobot hammers, the judge grades',
                count: (r) => `${r.copyCount || 0} blades · ${r.copyThisWeek || 0} this week` },
  library:    { name: 'The Library',      sub: 'the books — voice, hooks, the rubric, the Lock',
                count: (r) => `${r.files.length} books` },
  hall:       { name: 'The Golden Hall',  sub: 'winners on the wall · losers in the barrow below',
                count: (r) => `${r.winners || 0} won · ${r.losers || 0} fell` },
};

/* the slash command each stage-room hands you (read-only — copies to clipboard) */
const ROOM_CMD = {
  tower: '/account-read', weathertop: '/storm', council: '/brief',
  forge: '/produce', hall: '/reflect',
};

const EMPTY_HINT = {
  tower: 'No scrolls yet. <b>/account-read</b> writes the first quest scroll; the Monday sweep fills the leaderboard.',
  weathertop: 'The seed bank is empty. <b>/storm</b> fills it.',
  council: 'No briefs yet. Pick seeds by number and <b>/brief</b> them.',
  forge: 'Nothing forged yet. A locked brief + <b>/produce</b> makes the first blade.',
  hall: 'No trophies yet — they arrive via <b>/reflect</b> when a winner is promoted.',
};

/* ---------- state + views ---------- */
let STATE = null;
const VIEWS = {};
let current = null;

function registerView(name, def) { VIEWS[name] = def; def._built = false; }

function setView(name) {
  if (!VIEWS[name]) return;
  current = name;
  for (const [n, v] of Object.entries(VIEWS)) {
    const wrap = $(v.wrap);
    if (wrap) wrap.hidden = (n !== name);
  }
  document.body.classList.toggle('view-office', name === 'office');
  document.body.classList.toggle('view-map', name === 'map');
  document.body.classList.toggle('view-board', name === 'board');
  document.querySelectorAll('.viewbtn').forEach((b) =>
    b.classList.toggle('on', b.dataset.view === name));
  const v = VIEWS[name];
  if (!v._built) { v.build($(v.el)); v._built = true; }
  if (STATE) v.update(STATE);
  try { localStorage.setItem('studio-view', name); } catch (e) {}
}

async function refresh() {
  try {
    const res = await fetch('/api/state');
    STATE = await res.json();
  } catch (e) { return; }
  if (current && VIEWS[current]) VIEWS[current].update(STATE);
  renderQuest();
}

/* ---------- quest log ---------- */
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
    .map(([k, v]) => `<li><span>${k}</span><span class="v">${v}</span></li>`).join('');
  let next, cmd;
  if (!q.latestRead) { next = '&#9888; No quest scroll yet — <b>/account-read</b> starts the week.'; cmd = '/account-read'; }
  else if (q.briefsReady > 0) { next = `&#9876; ${q.briefsReady} brief${q.briefsReady > 1 ? 's' : ''} await the Forge — <b>/produce</b>.`; cmd = '/produce'; }
  else if (q.seedsTotal > 0) { next = `&#10022; ${q.seedsTotal} seeds wait at the Council — pick numbers, <b>/brief</b>.`; cmd = '/brief'; }
  else { next = '&#10022; The bank is empty — <b>/storm</b> for seeds.'; cmd = '/storm'; }
  $('#quest-next').innerHTML = `${next}<button class="cmdchip" data-cmd="${cmd}" title="copy to clipboard">&#9106; ${cmd}</button>`;
}

/* copy a slash command to the clipboard (never runs it — the Studio is read-only) */
function legacyCopy(text) {
  try {
    const ta = document.createElement('textarea');
    ta.value = text; ta.setAttribute('readonly', '');
    ta.style.cssText = 'position:fixed;top:0;left:0;opacity:0';
    document.body.appendChild(ta); ta.focus(); ta.select();
    const ok = document.execCommand('copy'); ta.remove(); return ok;
  } catch (e) { return false; }
}
function flashCopied(chip) {
  const old = chip.innerHTML;
  chip.classList.add('copied');
  chip.innerHTML = '&#10003; copied — paste into Claude Code';
  setTimeout(() => { chip.innerHTML = old; chip.classList.remove('copied'); }, 1400);
}
function copyCmd(chip) {
  const cmd = chip.dataset.cmd;
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(cmd)
      .then(() => flashCopied(chip))
      .catch(() => { if (legacyCopy(cmd)) flashCopied(chip); else chip.innerHTML = '&#9888; copy blocked'; });
  } else if (legacyCopy(cmd)) {
    flashCopied(chip);
  } else {
    chip.innerHTML = '&#9888; copy blocked';
  }
}

/* ---------- the scroll (room panel) ---------- */
let currentRoom = null;
const overlay = () => $('#overlay');

function ago(mtime) {
  const s = (Date.now() - mtime) / 1000;
  if (s < 90) return 'just now';
  if (s < 3600) return `${Math.round(s / 60)}m ago`;
  if (s < 86400) return `${Math.round(s / 3600)}h ago`;
  return `${Math.round(s / 86400)}d ago`;
}
const cleanName = (n) => n.replace(/\.md$|\.txt$/i, '').replace(/[-_]/g, ' ');

const FICON = `<svg class="ficon" viewBox="0 0 7 8"><rect width="7" height="8" fill="#efe4c0"/><path d="M0,0 h7 v8 h-7 z" fill="none" stroke="#2b1d12" stroke-width="1.6"/><rect x="1.5" y="2" width="4" height="1" fill="#6b543a"/><rect x="1.5" y="4" width="4" height="1" fill="#6b543a"/></svg>`;

function fileRow(f, id) {
  const badges = [];
  if (f.status) badges.push(`<span class="badge ${f.status}">${f.status}</span>`);
  if (typeof f.seeds === 'number') badges.push(`<span class="badge seedcount">${f.seeds} seeds</span>`);
  if (f.extra) badges.push(`<span class="badge outside">outside vault</span>`);
  if (Date.now() - f.mtime < 86400000) badges.push(`<span class="badge new">new</span>`);
  // a ready brief is a loaded gun for /produce — hand over the exact command
  if (id === 'council' && f.status === 'ready') {
    const target = f.name.replace(/\.md$/i, '');
    badges.push(`<button class="cmdchip mini" data-cmd="/produce ${target}" title="copy /produce for this brief">&#9106; /produce</button>`);
  }
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
  const meta = META[id];
  const room = STATE && STATE.rooms[id];
  $('#scroll-title').textContent = meta.name;
  $('#scroll-sub').textContent = meta.sub;
  const body = $('#scroll-body');
  const cmdRow = ROOM_CMD[id]
    ? `<div class="cmdrow"><button class="cmdchip" data-cmd="${ROOM_CMD[id]}" title="copy to clipboard">&#9106; ${ROOM_CMD[id]}</button><span class="cmdhint">copy, then paste into Claude Code</span></div>`
    : '';

  if (!room || room.files.length === 0) {
    body.innerHTML = cmdRow + `<div class="empty">${EMPTY_HINT[id] || 'Nothing here yet.'}</div>`;
  } else {
    let stats = `<div class="statrow"><span class="stat"><b>${room.files.length}</b> files</span>`;
    if (id === 'weathertop') stats += `<span class="stat"><b>${room.seedsTotal}</b> seeds</span>`;
    if (id === 'council') stats += `<span class="stat"><b>${room.briefsReady}</b> ready</span><span class="stat"><b>${room.briefsWritten}</b> written</span>`;
    if (id === 'forge') stats += `<span class="stat"><b>${room.copyThisWeek}</b> this week</span>`;
    if (id === 'hall') stats += `<span class="stat"><b>${room.winners}</b> winners</span><span class="stat"><b>${room.losers}</b> losers</span>`;
    stats += `<span class="stat">last work <b>${ago(room.lastActivity)}</b></span></div>`;

    const groups = new Map();
    for (const f of room.files) {
      const g = groupFor(id, f);
      if (!groups.has(g)) groups.set(g, []);
      groups.get(g).push(f);
    }
    let html = cmdRow + stats;
    for (const [g, files] of groups) {
      if (g) html += `<div class="groupHead">${g}</div>`;
      html += `<ul class="filelist">${files.map((f) => fileRow(f, id)).join('')}</ul>`;
    }
    body.innerHTML = html;
    body.querySelectorAll('.filelist li').forEach((li) => {
      li.addEventListener('click', (e) => {
        if (e.target.closest('.cmdchip')) return; // let the copy chip handle its own click
        openFile(decodeURIComponent(li.dataset.p), decodeURIComponent(li.dataset.n));
      });
    });
  }
  overlay().hidden = false;
}

async function openFile(p) {
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
  body.querySelectorAll('.imglink').forEach((el) =>
    el.addEventListener('click', () => openImage(el.dataset.img)));
  body.scrollTop = 0;
}

/* ---------- image lightbox ---------- */
function openImage(name) {
  const src = `/api/asset?name=${encodeURIComponent(name)}`;
  const box = document.createElement('div');
  box.className = 'imgbox';
  box.innerHTML = `
    <div class="imgframe">
      <div class="imgbar">
        <span class="imgname">${name}</span>
        <a class="imgdl" href="${src}&dl=1" download="${name}">&#8681; download</a>
        <button class="imgclose" title="Close (Esc)">&times;</button>
      </div>
      <div class="imgstage"><img src="${src}" alt="${name}"></div>
    </div>`;
  document.body.appendChild(box);
  const remove = () => { box.remove(); document.removeEventListener('keydown', onEsc); };
  const onEsc = (e) => { if (e.key === 'Escape') remove(); };
  box.addEventListener('click', (e) => { if (e.target === box) remove(); });
  box.querySelector('.imgclose').addEventListener('click', remove);
  box.querySelector('img').addEventListener('error', () => {
    box.querySelector('.imgstage').innerHTML = `<div class="imgmiss">Couldn’t find <b>${name}</b> in the vault. It may not be rendered yet.</div>`;
  });
  document.addEventListener('keydown', onEsc);
}

function closeScroll() { overlay().hidden = true; }

/* ---------- tiny markdown renderer ---------- */
function esc(s) { return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }
function inline(s) {
  return s
    .replace(/\[\[([^\]]+)\]\]/g, '<mark>$1</mark>')
    .replace(/!\[[^\]]*\]\([^)]*\)/g, '')
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>')
    // backtick'd image filenames become clickable chips (before generic code)
    .replace(/`([\w./-]+\.(?:png|jpe?g|gif|webp))`/gi, '<span class="imglink" data-img="$1" title="click to view">$1</span>')
    .replace(/\*\*([^*]+)\*\*/g, '<b>$1</b>')
    .replace(/(^|\W)\*([^*\n]+)\*(?=\W|$)/g, '$1<i>$2</i>')
    .replace(/`([^`]+)`/g, '<code>$1</code>');
}
function renderMarkdown(src) {
  let text = src.replace(/\r\n/g, '\n');
  let out = '';
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
  const flushPara = () => { if (para.length) { out += `<p>${para.map((l) => inline(esc(l))).join('<br>')}</p>`; para = []; } };
  const flushList = () => { if (list) { out += `<${list.tag}>${list.items.map((x) => `<li>${x}</li>`).join('')}</${list.tag}>`; list = null; } };
  while (i < lines.length) {
    const line = lines[i];
    if (line.startsWith('```')) {
      flushPara(); flushList();
      const buf = []; i++;
      while (i < lines.length && !lines[i].startsWith('```')) { buf.push(lines[i]); i++; }
      out += `<pre>${esc(buf.join('\n'))}</pre>`; i++; continue;
    }
    if (/^\|.*\|\s*$/.test(line)) {
      flushPara(); flushList();
      const rows = [];
      while (i < lines.length && /^\|.*\|\s*$/.test(lines[i])) { rows.push(lines[i]); i++; }
      const cells = (r) => r.replace(/^\||\|$/g, '').split('|').map((c) => inline(esc(c.trim())));
      let table = '<table>';
      rows.forEach((r, idx) => {
        if (/^\|[\s:|-]+\|$/.test(r)) return;
        const tag = idx === 0 ? 'th' : 'td';
        table += `<tr>${cells(r).map((c) => `<${tag}>${c}</${tag}>`).join('')}</tr>`;
      });
      out += table + '</table>'; continue;
    }
    const h = line.match(/^(#{1,4})\s+(.*)$/);
    if (h) { flushPara(); flushList(); const lvl = Math.min(h[1].length, 3); out += `<h${lvl}>${inline(esc(h[2]))}</h${lvl}>`; i++; continue; }
    if (/^(---+|\*\*\*+)\s*$/.test(line)) { flushPara(); flushList(); out += '<hr>'; i++; continue; }
    if (/^>\s?/.test(line)) {
      flushPara(); flushList();
      const buf = [];
      while (i < lines.length && /^>\s?/.test(lines[i])) { buf.push(lines[i].replace(/^>\s?/, '')); i++; }
      out += `<blockquote>${buf.map((l) => inline(esc(l))).join('<br>')}</blockquote>`; continue;
    }
    const ul = line.match(/^\s*[-*]\s+(.*)$/);
    const ol = line.match(/^\s*\d+\.\s+(.*)$/);
    if (ul || ol) {
      flushPara();
      const tag = ul ? 'ul' : 'ol';
      if (!list || list.tag !== tag) { flushList(); list = { tag, items: [] }; }
      list.items.push(inline(esc((ul || ol)[1]))); i++; continue;
    }
    if (line.trim() === '') { flushPara(); flushList(); i++; continue; }
    para.push(line); i++;
  }
  flushPara(); flushList();
  return out;
}

/* ---------- boot ---------- */
function start() {
  if (location.protocol === 'file:') {
    document.body.innerHTML = `
      <div style="max-width:560px;margin:14vh auto;padding:26px 30px;
        background:linear-gradient(178deg,#f2e4bc,#e2cf9c);border:3px solid #2b1d12;
        box-shadow:0 8px 0 rgba(43,29,18,.35);text-align:center;font-family:VT323,monospace;color:#2b1d12;">
        <h1 style="font-family:'Uncial Antiqua',serif;font-size:30px;margin-bottom:12px;">
          You shall not pass&hellip; this way</h1>
        <p style="font-size:21px;line-height:1.5;">This is only the blank parchment. The living map needs the studio server, which reads the vault.</p>
        <p style="font-size:21px;line-height:1.5;margin-top:12px;">Double-click <b>&ldquo;Open The Studio.command&rdquo;</b> in the vault folder &mdash; it lights the beacons and opens <b>localhost:4173</b> for you.</p>
      </div>`;
    return;
  }
  $('#scroll-close').addEventListener('click', closeScroll);
  overlay().addEventListener('click', (e) => { if (e.target === overlay()) closeScroll(); });
  document.addEventListener('click', (e) => {
    const chip = e.target.closest('.cmdchip');
    if (chip) { e.stopPropagation(); copyCmd(chip); }
  });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeScroll(); });
  document.querySelectorAll('.viewbtn').forEach((b) =>
    b.addEventListener('click', () => setView(b.dataset.view)));

  let want = 'office';
  try { want = localStorage.getItem('studio-view') || 'office'; } catch (e) {}
  if (!VIEWS[want]) want = Object.keys(VIEWS)[0];

  refresh().then(() => {
    setView(want);
    setInterval(refresh, 30000);
    window.addEventListener('focus', refresh);
  });
}

window.Studio = { registerView, setView, openRoom, meta: META, ago, state: () => STATE, start, SVG_NS };
