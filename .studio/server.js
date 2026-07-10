#!/usr/bin/env node
/**
 * The Studio — a tiny read-only window on the creative-strategy vault.
 * Zero dependencies. Serves the pixel map + live JSON of the vault state.
 * It NEVER writes to the vault.
 */
const http = require('http');
const fs = require('fs');
const path = require('path');

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

  return { generatedAt: Date.now(), vault: VAULT, rooms, quest };
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

// ---------- http ----------
const MIME = {
  '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript',
  '.woff2': 'font/woff2', '.svg': 'image/svg+xml', '.png': 'image/png', '.json': 'application/json',
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
    if (url.pathname === '/api/file') {
      const p = url.searchParams.get('p') || '';
      try { return send(200, JSON.stringify(readVaultFile(p))); }
      catch (e) { return send(403, JSON.stringify({ error: e.message })); }
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
