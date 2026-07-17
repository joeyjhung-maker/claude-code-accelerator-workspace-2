#!/usr/bin/env node
/**
 * The Studio — a tiny read-only window on the creative-strategy vault.
 * Zero dependencies. Serves the pixel map + live JSON of the vault state.
 * It NEVER writes to the vault.
 */
const http = require('http');
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const PORT = process.env.STUDIO_PORT || 4173;
const VAULT = path.resolve(__dirname, '..');
const PUBLIC = path.join(__dirname, 'public');

// Files outside the vault the studio may read (explicit whitelist only).
const EXTRA_FILES = {
  'voc:voice-of-customer': '/Users/joey/Documents/Projects/market-research/copy-bank/voice-of-customer.md',
  'voc:trends-log': '/Users/joey/Documents/Projects/market-research/trends-log.md',
};

// ---------- helpers ----------
const exists = (p) => { try { fs.accessSync(p); return true; } catch { return false; } };

function listDir(rel, { recursive = false } = {}) {
  const abs = path.join(VAULT, rel);
  if (!exists(abs)) return [];
  const out = [];
  const walk = (dir, base) => {
    let entries;
    try { entries = fs.readdirSync(dir, { withFileTypes: true }); } catch { return; }
    for (const e of entries) {
      if (e.name.startsWith('.')) continue;
      const full = path.join(dir, e.name);
      const relPath = path.join(base, e.name);
      if (e.isDirectory()) { if (recursive) walk(full, relPath); continue; }
      if (!/\.(md|txt)$/i.test(e.name)) continue;
      let st; try { st = fs.statSync(full); } catch { continue; }
      out.push({ name: e.name, path: relPath, mtime: st.mtimeMs, size: st.size });
    }
  };
  walk(abs, rel);
  out.sort((a, b) => b.mtime - a.mtime);
  return out;
}

function fileEntry(rel) {
  const abs = path.join(VAULT, rel);
  if (!exists(abs)) return null;
  let st; try { st = fs.statSync(abs); } catch { return null; }
  if (!st.isFile()) return null;
  return { name: path.basename(rel), path: rel, mtime: st.mtimeMs, size: st.size };
}

function extraEntry(key) {
  const abs = EXTRA_FILES[key];
  if (!abs || !exists(abs)) return null;
  let st; try { st = fs.statSync(abs); } catch { return null; }
  return { name: path.basename(abs), path: key, mtime: st.mtimeMs, size: st.size, extra: true };
}

function readFrontmatter(abs) {
  let text; try { text = fs.readFileSync(abs, 'utf8'); } catch { return {}; }
  if (!text.startsWith('---')) return {};
  const end = text.indexOf('\n---', 3);
  if (end === -1) return {};
  const fm = {};
  for (const line of text.slice(3, end).split('\n')) {
    const m = line.match(/^([\w-]+):\s*(.*)$/);
    if (m) fm[m[1]] = m[2].trim();
  }
  return fm;
}

function countSeeds(abs) {
  let text; try { text = fs.readFileSync(abs, 'utf8'); } catch { return 0; }
  return (text.match(/^## /gm) || []).length;
}

const notTemplate = (f) => !f.name.startsWith('_');
const newest = (files) => files.reduce((m, f) => Math.max(m, f.mtime), 0);

function activity(lastMtime) {
  if (!lastMtime) return 'quiet';
  const age = Date.now() - lastMtime;
  if (age < 30 * 60 * 1000) return 'hot';
  if (age < 24 * 60 * 60 * 1000) return 'warm';
  return 'quiet';
}

// ---------- strategy-map coverage grid ----------
const AWARE = ['unaware', 'problem', 'solution', 'product', 'most-aware'];
const SEGS = [
  { id: 's1', name: 'Burned-Out Agency Owner' },
  { id: 's2', name: '9-5 Escapee / Aspiring' },
  { id: 's3', name: 'Proof-Chaser' },
  { id: 's4', name: 'Opportunity Seeker' },
  { id: 'niche', name: 'Niche / vertical cuts' },
];
function mapAware(text) {
  if (!text) return null;
  const t = text.toLowerCase().split('/')[0].split('→')[0];
  if (t.includes('unaware')) return 'unaware';
  if (t.includes('problem')) return 'problem';
  if (t.includes('solution')) return 'solution';
  if (t.includes('product')) return 'product';
  if (t.includes('most')) return 'most-aware';
  return null;
}
function mapSegs(text) {
  if (!text) return [];
  const t = text.toLowerCase();
  const nums = [...t.matchAll(/segment\s*(\d)/g)].map((m) => 's' + m[1]).filter((s) => ['s1', 's2', 's3', 's4'].includes(s));
  if (nums.length) return [...new Set(nums)];
  if (t.includes('vertical')) return ['niche'];
  if (t.includes('opportunit')) return ['s4'];
  if (t.includes('proof')) return ['s3'];
  if (t.includes('escap') || t.includes('9-5') || t.includes('9 to 5')) return ['s2'];
  if (t.includes('agency')) return ['s1'];
  return [];
}
function computeCoverage() {
  const client = 'clients/flexxable';
  const cells = {};
  for (const s of SEGS) { cells[s.id] = {}; for (const a of AWARE) cells[s.id][a] = { seeds: 0, brief: false, written: false }; }
  // seeds — explicit [segment]/[awareness] tags
  for (const f of listDir(`${client}/seeds`)) {
    let text; try { text = fs.readFileSync(path.join(VAULT, f.path), 'utf8'); } catch { continue; }
    for (const b of text.split(/^## /m).slice(1)) {
      const aw = mapAware((b.match(/\[awareness:\s*([^\]]+)\]/i) || [])[1]);
      const segs = mapSegs((b.match(/\[segment:\s*([^\]]+)\]/i) || [])[1]);
      if (!aw || !segs.length) continue;
      for (const sg of segs) if (cells[sg]) cells[sg][aw].seeds++;
    }
  }
  // briefs — DNA Segment/Awareness lines + frontmatter status
  for (const f of listDir(`${client}/briefs`)) {
    let text; try { text = fs.readFileSync(path.join(VAULT, f.path), 'utf8'); } catch { continue; }
    const status = (text.match(/^status:\s*(\w+)/m) || [])[1] || '';
    const aw = mapAware((text.match(/\*\*Awareness:\*\*\s*(.+)/i) || [])[1]);
    const segs = mapSegs((text.match(/\*\*Segment:\*\*\s*(.+)/i) || [])[1]);
    if (!aw || !segs.length) continue;
    for (const sg of segs) if (cells[sg]) { cells[sg][aw].brief = true; if (status === 'written') cells[sg][aw].written = true; }
  }
  // tallies
  let gaps = 0, seeded = 0, briefed = 0, written = 0;
  for (const s of SEGS) for (const a of AWARE) {
    const c = cells[s.id][a];
    if (c.written) written++; else if (c.brief) briefed++; else if (c.seeds) seeded++; else gaps++;
  }
  return { segments: SEGS, awareness: AWARE, cells, tally: { gaps, seeded, briefed, written } };
}

// ---------- trophies (Golden Hall) + trigger words (Watch Room) ----------
function firstMatch(text, re) { const m = text.match(re); return m ? m[1].trim() : ''; }
function parseTrophy(relPath) {
  let text; try { text = fs.readFileSync(path.join(VAULT, relPath), 'utf8'); } catch { return null; }
  const title = firstMatch(text, /^#\s+(.+)$/m).replace(/^Winner\s*\([^)]*\):\s*/i, '').replace(/^Loser\s*\([^)]*\):\s*/i, '').replace(/^["“]|["”]$/g, '');
  const hook = firstMatch(text, /^[-*]\s*\*{0,2}Hook\*{0,2}:\s*["“]?(.+?)["”]?\s*$/mi);
  const why = firstMatch(text, /^[-*]\s*\*{0,2}(?:Why[^:]*|Cause of death|Why it died)\*{0,2}:\s*(.+)$/mi);
  return { path: relPath, title, hook, why };
}
function parseTriggerWords() {
  const rel = 'clients/flexxable/trigger-words.md';
  if (!exists(path.join(VAULT, rel))) return null;
  let text; try { text = fs.readFileSync(path.join(VAULT, rel), 'utf8'); } catch { return null; }
  const spend = new Set(), conv = new Set();
  for (const line of text.split('\n')) {
    const m = line.match(/^\s*[-*]?\s*([A-Za-z][\w '"/-]*?)\s*[·|]\s*source:\s*([\w-]+)/i);
    if (!m) continue;
    const word = m[1].trim().toLowerCase(), src = m[2].toLowerCase();
    if (src.includes('sweep') || src.includes('competitor')) spend.add(word);
    else conv.add(word);
  }
  const both = [...spend].filter((w) => conv.has(w));
  return { spend: [...spend], conversion: [...conv], both, path: rel };
}

// ---------- projects (clients + JV deals) ----------
const prettyFolder = (name) => name.replace(/[-_]/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase());

function listSubdirs(rel) {
  const abs = path.join(VAULT, rel);
  if (!exists(abs)) return [];
  let entries; try { entries = fs.readdirSync(abs, { withFileTypes: true }); } catch { return []; }
  return entries
    .filter((e) => e.isDirectory() && !e.name.startsWith('_') && !e.name.startsWith('.'))
    .map((e) => e.name);
}

function partnerName(base) {
  try {
    const text = fs.readFileSync(path.join(VAULT, base, 'partner.md'), 'utf8');
    const m = text.match(/^#\s+(.+)$/m);
    if (m) return m[1].replace(/^JV\s*Partner:\s*/i, '').trim();
  } catch {}
  return null;
}

function buildJV(folder) {
  const base = `jv/partners/${folder}`;
  const research = listDir(`${base}/research`).filter(notTemplate);
  const sellTheir = listDir(`${base}/copy/sell-their-offer`, { recursive: true }).filter(notTemplate);
  const sellOur = listDir(`${base}/copy/sell-our-offer`, { recursive: true }).filter(notTemplate);
  const last = newest(listDir(base, { recursive: true }));
  return {
    id: folder,
    name: partnerName(base) || prettyFolder(folder),
    partnerFile: exists(path.join(VAULT, base, 'partner.md')) ? `${base}/partner.md` : null,
    research: research.length,
    sellTheir: sellTheir.length,
    sellOur: sellOur.length,
    hasCampaignPlan: exists(path.join(VAULT, base, 'campaign-plan.md')),
    hasOnePager: exists(path.join(VAULT, base, 'offer-one-pager.md')),
    lastActivity: last,
    activity: activity(last),
  };
}

function buildProjects(quest) {
  const jvs = listSubdirs('jv/partners').map(buildJV).sort((a, b) => b.lastActivity - a.lastActivity);
  const clients = listSubdirs('clients').map((name) => {
    const base = `clients/${name}`;
    const isFlex = name === 'flexxable';
    const last = newest(listDir(base, { recursive: true }));
    return {
      id: name,
      name: prettyFolder(name),
      clientFile: exists(path.join(VAULT, base, 'client.md')) ? `${base}/client.md` : null,
      stats: isFlex ? {
        seeds: quest.seedsTotal, briefsReady: quest.briefsReady,
        briefsWritten: quest.briefsWritten, copyThisWeek: quest.copyThisWeek, winners: quest.winners,
      } : null,
      jvs: isFlex ? jvs : [],   // the JV layer is Flexxable's
      lastActivity: last,
      activity: activity(last),
    };
  });
  return { clients };
}

// ---------- machine sync status (reports only — never mutates) ----------
function git(args) {
  try { return execFileSync('git', args, { cwd: VAULT, encoding: 'utf8', timeout: 8000 }).trim(); }
  catch { return null; }
}

function buildSyncStatus() {
  const dirtyOut = git(['status', '--porcelain']);
  const dirty = dirtyOut == null ? null : (dirtyOut ? dirtyOut.split('\n').filter(Boolean).length : 0);
  let ahead = null, behind = null;
  const counts = git(['rev-list', '--left-right', '--count', 'HEAD...@{u}']); // no fetch — uses last-known refs
  if (counts) { const m = counts.split(/\s+/); ahead = +m[0]; behind = +m[1]; }
  const lastCommit = git(['log', '-1', '--format=%s']);
  const lastCommitAt = git(['log', '-1', '--format=%ct']);
  let fetchedAt = null;
  try { fetchedAt = fs.statSync(path.join(VAULT, '.git', 'FETCH_HEAD')).mtimeMs; } catch {}

  let verdict, tone, message;
  if (ahead == null || behind == null) {
    verdict = 'unknown'; tone = 'quiet';
    message = 'No GitHub link yet. Double-click “Start Work” to connect and sync.';
  } else if (ahead > 0 && behind > 0) {
    verdict = 'diverged'; tone = 'bad';
    message = 'Both machines changed since the last sync. Open Claude Code and say: “my repo diverged, help me merge.”';
  } else if (behind > 0 && dirty) {
    verdict = 'behind-dirty'; tone = 'bad';
    message = 'GitHub has newer work AND you have unsaved changes here. Double-click “Finish Work” first, then ask Claude if it warns.';
  } else if (behind > 0) {
    verdict = 'behind'; tone = 'warn';
    message = 'The other machine pushed newer work. Double-click “Start Work” to pull it in.';
  } else if (ahead > 0 || dirty) {
    verdict = 'ahead'; tone = 'warn';
    message = 'You have work here that isn’t on GitHub yet. Double-click “Finish Work” before switching machines.';
  } else {
    verdict = 'synced'; tone = 'good';
    message = 'In sync with GitHub — safe to switch machines.';
  }
  return {
    dirty, ahead, behind, lastCommit,
    lastCommitAt: lastCommitAt ? +lastCommitAt * 1000 : null,
    fetchedAt, verdict, tone, message,
  };
}

// ---------- rooms ----------
function buildState() {
  const client = 'clients/flexxable';

  // Palantír Tower — account read + competitor intel
  const towerFiles = [
    fileEntry('swipes/market-leaderboard.md'),
    fileEntry(`${client}/trigger-words.md`),
    fileEntry(`${client}/strategy-map.md`),
    fileEntry(`${client}/hypotheses.md`),
    fileEntry(`${client}/analysis-config.md`),
    ...listDir(`${client}/account-reads`),
  ].filter(Boolean);

  // The Deep Mine — research
  const mineFiles = [
    ...listDir(`${client}/swipe-bank`, { recursive: true }),
    fileEntry(`${client}/parsed-hooks-bodies-headlines.md`),
    fileEntry(`${client}/internal-vectors.md`),
    extraEntry('voc:voice-of-customer'),
    extraEntry('voc:trends-log'),
    ...listDir('swipes').filter((f) => f.name !== 'market-leaderboard.md'),
  ].filter(Boolean);

  // Weathertop — seeds
  const seedFiles = listDir(`${client}/seeds`).map((f) => ({
    ...f, seeds: countSeeds(path.join(VAULT, f.path)),
  }));
  const seedsTotal = seedFiles.reduce((n, f) => n + f.seeds, 0);

  // Council Hall — briefs
  const briefFiles = listDir(`${client}/briefs`).map((f) => {
    const fm = readFrontmatter(path.join(VAULT, f.path));
    return { ...f, status: fm.status || 'unknown', date: fm.date || '', copy: fm.copy || '' };
  });
  const briefsReady = briefFiles.filter((b) => b.status === 'ready').length;
  const briefsWritten = briefFiles.filter((b) => b.status === 'written').length;

  // The Forge — produced work
  const copyFiles = listDir('copy').filter(notTemplate);
  const creativeFiles = listDir('creatives', { recursive: true }).filter(notTemplate);
  const weekAgo = Date.now() - 7 * 24 * 60 * 60 * 1000;
  const copyThisWeek = copyFiles.filter((f) => f.mtime > weekAgo).length;

  // The Library — reference books
  const libraryFiles = [
    ...listDir('brand'), ...listDir('concepts'), ...listDir('rubrics'),
    fileEntry('the-data-dictionary.md'), fileEntry('memory-map.md'), fileEntry('CLAUDE.md'),
  ].filter(Boolean);

  // Golden Hall — winners + the barrow (losers)
  const winnerFiles = listDir('winners').filter(notTemplate);
  const loserFiles = listDir('losers').filter(notTemplate);

  const mk = (files, extras = {}) => ({
    files, lastActivity: newest(files), status: activity(newest(files)), ...extras,
  });

  const rooms = {
    tower: mk(towerFiles),
    mine: mk(mineFiles),
    weathertop: mk(seedFiles, { seedsTotal }),
    council: mk(briefFiles, { briefsReady, briefsWritten }),
    forge: mk([...copyFiles, ...creativeFiles], { copyCount: copyFiles.length, copyThisWeek }),
    library: mk(libraryFiles),
    hall: mk([...winnerFiles, ...loserFiles], { winners: winnerFiles.length, losers: loserFiles.length }),
  };

  // Quest log — the week at a glance
  const accountReads = listDir(`${client}/account-reads`);
  const quest = {
    seedsTotal,
    seedsLatest: seedFiles[0] ? seedFiles[0].name.replace('.md', '') : null,
    briefsReady, briefsWritten,
    copyThisWeek,
    winners: winnerFiles.length,
    latestRead: accountReads[0] ? accountReads[0].name.replace('.md', '') : null,
  };

  const trophies = {
    winners: winnerFiles.map((f) => parseTrophy(f.path)).filter(Boolean),
    losers: loserFiles.map((f) => parseTrophy(f.path)).filter(Boolean),
    shipped: copyFiles.length,
  };

  return {
    generatedAt: Date.now(), vault: VAULT, rooms, quest,
    coverage: computeCoverage(), trophies, triggerWords: parseTriggerWords(),
    projects: buildProjects(quest), sync: buildSyncStatus(),
  };
}

// ---------- file reads (sandboxed) ----------
function readVaultFile(p) {
  if (EXTRA_FILES[p]) {
    return { path: p, content: fs.readFileSync(EXTRA_FILES[p], 'utf8') };
  }
  const abs = path.resolve(VAULT, p);
  if (!abs.startsWith(VAULT + path.sep)) throw new Error('outside vault');
  if (path.basename(abs).startsWith('.')) throw new Error('hidden file');
  if (!/\.(md|txt)$/i.test(abs)) throw new Error('not a text file');
  return { path: p, content: fs.readFileSync(abs, 'utf8') };
}

// ---------- image assets (sandboxed, found by basename) ----------
const IMG_EXT = /\.(png|jpe?g|gif|webp)$/i;
const SKIP_DIRS = new Set(['node_modules', '.git', '.studio', '.obsidian', '.claude']);
let assetIndex = null;

function buildAssetIndex() {
  const map = new Map();
  const walk = (dir) => {
    let entries; try { entries = fs.readdirSync(dir, { withFileTypes: true }); } catch { return; }
    for (const e of entries) {
      if (e.name.startsWith('.') || SKIP_DIRS.has(e.name)) continue;
      const full = path.join(dir, e.name);
      if (e.isDirectory()) walk(full);
      else if (IMG_EXT.test(e.name) && !map.has(e.name)) map.set(e.name, full);
    }
  };
  walk(VAULT);
  assetIndex = map;
  return map;
}

// name may be a bare basename ("foo.png") or a vault-relative path ("creatives/foo.png")
function resolveAsset(name) {
  if (!IMG_EXT.test(name)) throw new Error('not an image');
  if (name.includes('/')) {
    const abs = path.resolve(VAULT, name);
    if (!abs.startsWith(VAULT + path.sep)) throw new Error('outside vault');
    if (exists(abs)) return abs;
    name = path.basename(name);
  }
  if (!assetIndex) buildAssetIndex();
  if (!assetIndex.has(name)) buildAssetIndex(); // maybe newly rendered — rebuild once
  const hit = assetIndex.get(name);
  if (!hit) throw new Error('not found in vault');
  return hit;
}

// ---------- http ----------
const MIME = {
  '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript',
  '.woff2': 'font/woff2', '.svg': 'image/svg+xml', '.png': 'image/png', '.json': 'application/json',
  '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.gif': 'image/gif', '.webp': 'image/webp',
};

const server = http.createServer((req, res) => {
  const url = new URL(req.url, `http://localhost:${PORT}`);
  const send = (code, body, type = 'application/json') => {
    res.writeHead(code, { 'Content-Type': type, 'Cache-Control': 'no-store' });
    res.end(body);
  };
  try {
    if (url.pathname === '/api/state') {
      return send(200, JSON.stringify(buildState()));
    }
    if (url.pathname === '/api/sync/refresh') {
      // user-triggered "check GitHub now" — git fetch touches .git only, never the vault/working tree
      git(['fetch', 'origin', '--quiet']);
      return send(200, JSON.stringify(buildSyncStatus()));
    }
    if (url.pathname === '/api/file') {
      const p = url.searchParams.get('p') || '';
      try { return send(200, JSON.stringify(readVaultFile(p))); }
      catch (e) { return send(403, JSON.stringify({ error: e.message })); }
    }
    if (url.pathname === '/api/asset') {
      const name = url.searchParams.get('name') || '';
      try {
        const abs = resolveAsset(name);
        const body = fs.readFileSync(abs);
        const dl = url.searchParams.get('dl');
        res.writeHead(200, {
          'Content-Type': MIME[path.extname(abs).toLowerCase()] || 'application/octet-stream',
          'Cache-Control': 'no-store',
          ...(dl ? { 'Content-Disposition': `attachment; filename="${path.basename(abs)}"` } : {}),
        });
        return res.end(body);
      } catch (e) { return send(404, JSON.stringify({ error: e.message })); }
    }
    // static
    let rel = url.pathname === '/' ? '/index.html' : url.pathname;
    const abs = path.resolve(PUBLIC, '.' + rel);
    if (!abs.startsWith(PUBLIC + path.sep) || !exists(abs)) return send(404, '{"error":"not found"}');
    return send(200, fs.readFileSync(abs), MIME[path.extname(abs)] || 'application/octet-stream');
  } catch (e) {
    return send(500, JSON.stringify({ error: e.message }));
  }
});

server.listen(PORT, '127.0.0.1', () => {
  console.log(`The Studio is open → http://localhost:${PORT}  (vault: ${VAULT})`);
});
