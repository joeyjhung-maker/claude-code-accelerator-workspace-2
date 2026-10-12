// Frame-accurate renderer for launch.html (1920x1080). Needs puppeteer-core on NODE_PATH.
//   node render.js stills 0,4.9,12 <outdir>      -> PNG stills at those seconds
//   node render.js cues <cues.json>              -> dump the SFX cue list the page registers
//   node render.js video <from> <to> <out.mp4>   -> silent H.264 segment of frames [from,to)
const puppeteer = require('puppeteer-core'); const { spawn } = require('child_process'); const fs = require('fs'); const path = require('path');
const HTML = 'file://' + path.resolve(__dirname, '..', 'launch.html'); const FPS = 30;
(async () => {
  const [mode, a, b, c] = process.argv.slice(2);
  const br = await puppeteer.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: 'new', args: ['--allow-file-access-from-files', '--hide-scrollbars', '--force-color-profile=srgb'] });
  const p = await br.newPage(); let bad = 0;
  p.on('pageerror', e => { bad++; console.error('PAGEERR', e.message); }); p.on('console', m => { if (m.type() === 'error') console.error('CONSOLE', m.text()); });
  await p.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 1 });
  await p.goto(HTML, { waitUntil: 'load', timeout: 60000 });
  await p.evaluate(async () => { await Promise.all([300, 400, 600, 700, 800, 900].map(w => document.fonts.load(`${w} 60px Inter`, 'Ag$1✓'))); await document.fonts.ready; await window.ready; });
  if (bad) { console.error('page failed to build'); process.exit(1); }
  const shoot = async (t, type) => { await p.evaluate(t => window.seek(t), t); return p.screenshot(type === 'png' ? { type: 'png' } : { type: 'jpeg', quality: 93 }); };
  if (mode === 'cues') { const cues = await p.evaluate(() => ({ dur: TIMING.dur, cues: window.collectCues() })); fs.writeFileSync(a, JSON.stringify(cues)); console.log('cues', cues.cues.length); }
  else if (mode === 'stills') { fs.mkdirSync(b, { recursive: true }); for (const t of a.split(',').map(Number)) fs.writeFileSync(path.join(b, `t${t.toFixed(2).padStart(6, '0')}.png`), await shoot(t, 'png')); }
  else {
    const dur = await p.evaluate(() => TIMING.dur); const f0 = +a, f1 = Math.min(+b, Math.round(dur * FPS));
    const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '16', '-preset', 'medium', '-g', '30', c], { stdio: ['pipe', 'inherit', 'inherit'] });
    for (let i = f0; i < f1; i++) { const buf = await shoot(i / FPS); if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r)); if ((i - f0) % 300 === 0) console.log(`${c}: frame ${i}/${f1}`); }
    ff.stdin.end(); await new Promise(r => ff.on('close', r));
  }
  await br.close();
})();
