// Frame-accurate renderer for the code-animated ads (doodle anim.html, game.html, heist.html, pixar.html).
// Setup once:  mkdir -p /tmp/r && cd /tmp/r && npm i puppeteer-core && cp <repo>/scripts/render_frames.js .
// usage: HTML=<page> AUDIO=<wav> OUT=<mp4> [WAIT=load] node render_frames.js video 30
//        HTML=<page> PFX=x node render_frames.js stills 1.5,3.8   |  HTML=<page> CUES=<json> node render_frames.js cues
// Pages whose picture is a <video> (heist, pixar) need WAIT=load. Wrap long renders in `caffeinate -i`.
const puppeteer = require('puppeteer-core');
const { spawn } = require('child_process');
const path = require('path');
const DIR = '/Users/joey/Documents/claude-code-accelerator-workspace/creatives/_assets/2026-09-29-whiskey-locked-bottle';
const HTML = 'file://' + (process.env.HTML || (DIR + '/build/anim.html'));
const AUDIO = process.env.AUDIO || (DIR + '/dan-whiskey-vo.wav');
const OUT = process.env.OUT || '/Users/joey/Documents/claude-code-accelerator-workspace/creatives/2026-09-29-flexxable-iaa-whiskey-locked-bottle-animated-v1.mp4';
const SP = __dirname;
const DUR = 77.6;

(async () => {
  const [mode, arg] = process.argv.slice(2);
  const b = await puppeteer.launch({
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    headless: 'new', args: ['--allow-file-access-from-files', '--hide-scrollbars'],
  });
  const p = await b.newPage();
  p.on('pageerror', e => console.error('PAGEERR', e.message));
  await p.setViewport({ width: 1080, height: 1920, deviceScaleFactor: 1 });
  await p.goto(HTML, { waitUntil: process.env.WAIT || 'networkidle0', timeout: 120000 });
  await p.evaluate(async () => { if (window.ready) await window.ready; await Promise.all(['600 60px Poppins','800 60px Poppins','900 60px Poppins','600 60px Caveat','700 60px Caveat'].map(f => document.fonts.load(f, 'A$1✓'))); await document.fonts.ready; });
  const shoot = async (t, type = 'jpeg') => {
    await p.evaluate(t => window.seek(t), t);
    await p.evaluate(() => Promise.all([...document.images].map(i => i.complete ? 0 : new Promise(r => i.onload = r))));
    return p.screenshot(type === 'png' ? { type: 'png' } : { type: 'jpeg', quality: 92 });
  };
  if (mode === 'cues') {
    const cues = await p.evaluate(() => window.collectCues());
    require('fs').writeFileSync(process.env.CUES || (DIR + '/build/cues.json'), JSON.stringify(cues, null, 0));
    console.log('cues', cues.length);
  } else if (mode === 'stills') {
    for (const t of arg.split(',').map(Number)) {
      require('fs').writeFileSync(path.join(SP, `${process.env.PFX||'still'}-${t.toFixed(2)}.png`), await shoot(t, 'png'));
    }
  } else {
    const FPS = Number(arg || 30), N = Math.round(FPS * DUR);
    const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-',
      '-i', AUDIO, '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-preset', 'medium',
      '-c:a', 'aac', '-b:a', '192k', '-af', 'apad', '-shortest', '-movflags', '+faststart', OUT], { stdio: ['pipe', 'inherit', 'inherit'] });
    const t0 = Date.now();
    for (let i = 0; i < N; i++) {
      const buf = await shoot(i / FPS);
      if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
      if (i % 150 === 0) console.log(`frame ${i}/${N}  ${((Date.now() - t0) / 1000).toFixed(0)}s`);
    }
    ff.stdin.end();
    await new Promise(r => ff.on('close', r));
    console.log('done', OUT);
  }
  await b.close();
})();
