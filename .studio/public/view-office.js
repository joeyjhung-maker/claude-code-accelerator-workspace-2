/* ============ The Studio — the office interior view ============ */
'use strict';
(function () {
  const NS = Studio.SVG_NS;
  const PX = 2.5, TL = 12, T = PX * TL;   // tile = 30px, logical pixel = 2.5px
  const svgAdd = (svg, rows, tx, ty, pal, cls) => {
    const g = document.createElementNS(NS, 'g');
    if (cls) g.setAttribute('class', cls);
    rows.forEach((row, ry) => { [...row].forEach((ch, rx) => {
      if (ch === '.' || ch === ' ') return;
      const col = pal[ch]; if (!col) return;
      const r = document.createElementNS(NS, 'rect');
      r.setAttribute('x', tx * T + rx * PX); r.setAttribute('y', ty * T + ry * PX);
      r.setAttribute('width', PX); r.setAttribute('height', PX); r.setAttribute('fill', col);
      g.appendChild(r);
    }); });
    svg.appendChild(g); return g;
  };
  const rect = (svg, x, y, w, h, fill, cls) => {
    const r = document.createElementNS(NS, 'rect');
    r.setAttribute('x', x); r.setAttribute('y', y); r.setAttribute('width', w); r.setAttribute('height', h);
    r.setAttribute('fill', fill); if (cls) r.setAttribute('class', cls);
    svg.appendChild(r); return r;
  };

  const K = '#12100d';
  const WOOD = { K, N: '#8a5a32', n: '#6e4626', m: '#a06c3e', M: '#b87f49', W: '#f0e4c2', w: '#c4ab7c', q: '#8a7a5c' };

  /* ---------------- characters ---------------- */
  function chibi(hair, shirt, opts = {}) {
    const P = { K, H: hair[0], h: hair[1], S: '#e9c49c', s: '#d3a87e', E: '#241b12',
      T: shirt[0], t: shirt[1], u: shirt[2] || shirt[1], P: opts.pants || '#3d3630', B: '#221d17' };
    const rows = ['......KKKKKKKK......','....KKHHHHHHHHKK....','...KHHHHHHHHHHHHK...','..KHHhhHHHHHHHHHHK..','..KHhhHHHHHHHHhHHK..','..KHhHHHHHHHHHHhHK..','..KHHHHHHHHHHHHHHK..','..KHHSSSSSSSSSSHHK..','..KHSSSSSSSSSSSSHK..','...KSSEESSSSEESSK...','...KSSEESSSSEESSK...','...KSSSSSSSSSSSSK...','...KSsSSssssSSsSK...','....KSSSSSSSSSSK....','.....KSSSSSSSSK.....','....KKTTTTTTTTKK....','..KKTTTTTTTTTTTTKK..','.KTTtTTTTTTTTTTtTTK.','.KSSKTTTTuuTTTTKSSK.','.KssKTttttttttTKssK.','..KKKTTTTTTTTTTKKK..','....KPPPPPPPPPPK....','....KPPPKKKKPPPK....','....KPPPK..KPPPK....','....KBBBK..KBBBK....','....KKKKK..KKKKK....'];
    return { rows, P };
  }
  function hooded(hood, robe) {
    const P = { K, H: hood[0], h: hood[1], S: '#e9c49c', E: '#241b12', T: robe[0], t: robe[1], B: '#221d17' };
    const rows = ['......KKKKKKKK......','....KKHHHHHHHHKK....','...KHHHHHHHHHHHHK...','..KHhhHHHHHHHHHHK...','..KHhHHHHHHHHHHHK...','..KHHKKKKKKKKHHK....','..KHKSSSSSSSSKHK....','..KHKSEESSEESSKHK...','..KHKSSSSSSSSKHK....','...KKKSSSSSSKKK.....','...KTTTTTTTTTTK.....','..KTTTTTTTTTTTTK....','.KTTtTTTTTTTTtTTK...','.KTTtTTTTTTTTtTTK...','.KTTTTTTTTTTTTTTK...','.KTtTTTTTTTTTTtTK...','.KTtTTTTTTTTTTtTK...','.KTTTTTTTTTTTTTTK...','..KTTTTTTTTTTTTK....','..KTTTTTTTTTTTTK....','..KBBKKKKKKKKBBK....'];
    return { rows, P };
  }
  const seated = (c) => ({ rows: c.rows.slice(0, 21), P: c.P });

  /* ---------------- shared props ---------------- */
  const plantBig = { rows: ['....GgG.gG....','..GgGGgGGgG...','.GGgGgGGGgGG..','.gGGGgGgGGGg..','..G.gGGGg.G...','.....KNK......','....KNNNK.....','....KnnnK.....','...KnnnnnK....','...KKKKKKK....'], P: { K, N: '#a05a32', n: '#7c4526', G: '#4e6b3a', g: '#66884c' } };
  const candleWall = { rows: ['..F..','.FfF.','..W..','.KWK.','.KKK.'], P: { K, W: '#f0e4c2', F: '#ffd76a', f: '#ff9d3c' } };
  const scrollPile = { rows: ['..WWWW..','.WqqqqW.','WWWWWWWW','WqqWqqWW','WWWWWWWW'], P: { K, W: '#f0e4c2', q: '#b8a06a' } };
  const writeDesk = { rows: ['KKKKKKKKKKKKKKKKKKKKKKKKKKKK','KmmmmmmmmmmmmmmmmmmmmmmmmmmK','KNNWWWWWNNKWWWWWKNNWWWNNNNNK','KNNWqqqWNNKWqqqWKNNWqWNNiiNK','KNNWWWWWNNKKKKKKKNNWWWNNiiNK','KNNNNNNNNNNNNNNNNNNNNNNNNNNK','KnnKKKKKKKKKKKKKKKKKKKKKKnnK','KnnK....................KnnK'], P: { ...WOOD, i: '#241a10' } };
  const torchWall = { rows: ['.FfF.','FfhfF','.KfK.','.KNK.','.KNK.'], P: { K, N: '#6e4626', F: '#ff9d3c', f: '#ffd76a', h: '#fff2c0' } };

  /* ---------------- watch-room props ---------------- */
  const conspiracyBoard = { rows: ['KKKKKKKKKKKKKKKKKKKKKKKKKKKKKK','KNNNNNNNNNNNNNNNNNNNNNNNNNNNNK','KNWWWWWNrrrrWWWWWNrrNWWWWWWNNK','KNWqqqWNrWWWWqqqWNrrNWqqgqWNNK','KNWWWWWrrWNNWWWWWrrWNWWWWWWNNK','KNWgqqWNrWqqWWgqqWNrWWqqqWWNNK','KNWWWWWNrrrrWWWWWNNrrWWWWWWNNK','KNNNNNNNNNNNNNNNNNNNNNNNNNNNNK','KKKKKKKKKKKKKKKKKKKKKKKKKKKKKK'], P: { ...WOOD, r: '#a04030', g: '#c9962e' } };
  const palantirDesk = { rows: ['.....KKKKKK.....','....KppppppK....','...KpOOOOOOpK...','...KpOooOOOpK...','...KpOoOOOOpK...','...KpOOOOOOpK...','....KppppppK....','KKKKKKKKKKKKKKKK','KmmmmmmmmmmmmmmK','KNNNNNNNNNNNNNNK','KnnKKKKKKKKKKnnK','KnnK........KnnK'], P: { ...WOOD, p: '#5a3f73', O: '#a67cc4', o: '#e8d2fa' } };
  const telescope = { rows: ['........KKK.','......KKccK.','....KKccKK..','..KKccKK....','.KccKK......','.KcK........','..KNK.......','.KN.NK......','KK...KK.....'], P: { K, N: '#8a5a32', c: '#b9a06a' } };
  const globeProp = { rows: ['..KKKK..','.KccGcK.','KcGGcGcK','KcGcGGcK','.KcGGcK.','..KKKK..','...KN...','..KNNK..'], P: { K, c: '#7fa3b5', G: '#5d7548', N: '#6e4626' } };

  /* ---------------- mine props ---------------- */
  const minecart = { rows: ['.KKKKKKKKKKKKKK.','KWwWWwWWwWWwWWwK','KwWwWWwWWwWWwWWK','KNNNNNNNNNNNNNNK','KnNNNNNNNNNNNNnK','.KKKKKKKKKKKKKK.','..KfK......KfK..','.KfffK....KfffK.','..KfK......KfK..'], P: { ...WOOD, f: '#4a4a52' } };
  const supportBeam = { rows: ['KNNK......KNNK','KNNKKKKKKKKNNK','KNNNNNNNNNNNNK','KNNKKKKKKKKNNK','KNNK......KNNK','KNNK......KNNK','KNNK......KNNK'], P: WOOD };
  const lanternPost = { rows: ['.KKK.','KFfFK','KfFfK','.KKK.','..N..','..N..','.KNK.'], P: { K, N: '#6e4626', F: '#ffd76a', f: '#ff9d3c' } };
  const barrel = { rows: ['.KKKKKK.','KmNNNNmK','KNnnnnNK','KggggggK','KNnnnnNK','KmNNNNmK','.KKKKKK.'], P: { ...WOOD, g: '#8a7a5c' } };
  const crateStack = { rows: ['...KKKKKKKK.','...KNmmmmNK.','...KmWWWWmK.','...KNmmmmNK.','KKKKKKKKKKKK','KNmmmmNKNmmK','KmWWWWmKmWWK','KNmmmmNKNmmK','KKKKKKKKKKKK'], P: WOOD };

  /* ---------------- storm props ---------------- */
  const jarShelf = { rows: ['KKKKKKKKKKKKKKKKKKKKKK','KmmmmmmmmmmmmmmmmmmmmK','KcGcKcGcKcgcKcGcKcGcKK','KcGcKcgcKcGcKcGcKcgcKK','KNNNNNNNNNNNNNNNNNNNNK','KcgcKcGcKcGcKcgcKcGcKK','KcGcKcGcKcgcKcGcKcGcKK','KNNNNNNNNNNNNNNNNNNNNK'], P: { ...WOOD, c: '#b9cbd2', G: '#5d7548', g: '#8fae6a' } };
  const roundTableBig = { rows: ['......KKKKKKKK......','....KKNNNNNNNNKK....','...KNNmmmmmmmmNNK...','..KNmmNNNNNNNNmmNK..','.KNmNNWWwNNWwNNNmNK.','.KNmNWwWWNNwWWNNmNK.','KNmNNWWWwNNWWwNNNmNK','KNmNNnnnnnnnnnnNNmNK','.KNmNNWwWNNwWWNNmNK.','.KNmNNWWwNNWWwNNmNK.','..KNmmNNNNNNNNmmNK..','...KNNmmmmmmmmNNK...','....KKNNNNNNNNKK....','......KKKKKKKK......'], P: WOOD };
  const dartboard = { rows: ['.KKKKK.','KrWrWrK','KWrgrWK','KrgKgrK','KWrgrWK','KrWrWrK','.KKKKK.'], P: { K, r: '#a04030', W: '#f0e4c2', g: '#5d7548' } };
  const chestBig = { rows: ['.KKKKKKKKKKKKKK.','KNNNNNNNNNNNNNNK','KNmmmmmmmmmmmmNK','KggNNNNNNNNNNggK','KNNNNNNggNNNNNNK','KnnnnnnggnnnnnnK','KnnnnnnnnnnnnnnK','KnnnnnnnnnnnnnnK','.KKKKKKKKKKKKKK.'], P: { ...WOOD, g: '#c9962e' } };

  /* ---------------- council props ---------------- */
  const mapTableLong = { rows: ['KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK','KmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmK','KNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNNK','KNWqqWWWrrrWWWWgggWWWWWqqqWWWrrWWNNK','KNWWWqqWWWWWWggWWWWqqWWWWWWWWWWWWNNK','KNWWWWWWqqWWWWWWWqqWWWWrrrWWWggWWNNK','KNWWrrWWWWWWWqqWWWWWWWWWWWWWWWWWWNNK','KNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNNK','KNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNK','KnnKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKnnK','KnnK............................KnnK'], P: { ...WOOD, r: '#a04030', g: '#c9962e' } };
  const highChair = { rows: ['.KKKKKKKK.','KNmmmmmmNK','KNmNNNNmNK','KNmNNNNmNK','KNmNNNNmNK','KNNNNNNNNK','KKKKKKKKKK','.Kn....nK.'], P: WOOD };
  const tapestry = { rows: ['KKKKKKKKKKKK','KrrrrrrrrrrK','KrggrrrrggrK','KrrgrrrggrrK','KrrrggggrrrK','KrrgrrrrgrrK','KrrrrrrrrrrK','.KrrrrrrrrK.','..KrrrrrrK..','...KrrrrK...','....KrrK....'], P: { K, r: '#8e3b2c', g: '#c9962e' } };
  const scrollRack = { rows: ['KKKKKKKKKK','KWWKWWKWWK','KqqKqqKqqK','KKKKKKKKKK','KWWKWWKWWK','KqqKqqKqqK','KKKKKKKKKK'], P: { K, W: '#f0e4c2', q: '#b8a06a' } };

  /* ---------------- forge props ---------------- */
  const furnace = { rows: ['..KKKKKKKKKKKK..','.KffffffffffffK.','KffKKKKKKKKKKffK','KfK..........KfK','KfK.FFFFFFFF.KfK','KfK.FhhFFhFF.KfK','KfK.FFhFFFFF.KfK','KfK.FFFFhhFF.KfK','KffKKKKKKKKKKffK','KffffffffffffffK','KfffKKKKKKKKfffK','KKKKKKKKKKKKKKKK'], P: { K, f: '#4a4a52', F: '#ff9d3c', h: '#ffd76a' } };
  const anvilBig = { rows: ['.KKKKKKKKKKKKK..','KfffffffffffffK.','.KfffffffffKKK..','..KfffffffK.....','...KfffffK......','..KfffffffK.....','.KfffffffffK....','KKKKKKKKKKKKK...'], P: { K, f: '#4a4a52' } };
  const quenchBarrel = { rows: ['.KKKKKKKK.','KmNNNNNNmK','KNccccccNK','KNcCcCccNK','KggggggggK','KNnnnnnnNK','.KKKKKKKK.'], P: { ...WOOD, c: '#7fa3b5', C: '#a9c8d6', g: '#8a7a5c' } };
  const toolWall = { rows: ['KKKKKKKKKKKKKKKK','KNfNKNfNKNfNKNNK','KNfNKNfNKNfNKffK','KNfNKNfNKNfNKNNK','KKKKKKKKKKKKKKKK'], P: { K, N: '#8a5a32', f: '#4a4a52' } };
  const swordRack = { rows: ['KKKKKKKKKKKKKK','KNcNKNcNKNcNNK','KNcNKNcNKNcNNK','KNcNKNcNKNcNNK','KNgNKNgNKNgNNK','KNNNNNNNNNNNNK','KKKKKKKKKKKKKK'], P: { K, N: '#8a5a32', c: '#b9c7cc', g: '#c9962e' } };
  const judgeDesk = { rows: ['KKKKKKKKKKKKKKKKKKKK','KmmmmmmmmmmmmmmmmmmK','KNNrrNNWWWWWNNggNNNK','KNNrrNNWqqqWNNggNNNK','KNNNNNNWWWWWNNNNNNNK','KnnKKKKKKKKKKKKKKnnK'], P: { ...WOOD, r: '#a04030', g: '#5d7548' } };

  /* ---------------- library props ---------------- */
  const tallShelf = { rows: ['KKKKKKKKKKKKKKKKKKKKKKKKKKKK','KmmmmmmmmmmmmmmmmmmmmmmmmmmK','KaAbBcCdDgGaAbBrRcCgGdDaAbBK','KaAbBcCdDgGaAbBrRcCgGdDaAbBK','KaAbBcCdDgGaAbBrRcCgGdDaAbBK','KNNNNNNNNNNNNNNNNNNNNNNNNNNK','KrRgGaAbBcCdDrRaAbBcCgGdDrRK','KrRgGaAbBcCdDrRaAbBcCgGdDrRK','KrRgGaAbBcCdDrRaAbBcCgGdDrRK','KNNNNNNNNNNNNNNNNNNNNNNNNNNK','KnnnnnnnnnnnnnnnnnnnnnnnnnnK'], P: { ...WOOD, a: '#a04030', A: '#8a3628', b: '#3f6a52', B: '#35594a', c: '#3f5470', C: '#354761', d: '#c9962e', D: '#a67a1e', r: '#8e3b2c', R: '#7c3225', g: '#5d7548', G: '#52673f' } };
  const ladder = { rows: ['KNK..KNK','KNKKKKNK','KNK..KNK','KNKKKKNK','KNK..KNK','KNKKKKNK','KNK..KNK'], P: WOOD };
  const armchair = { rows: ['.KKKKKKKKKK.','KrrrrrrrrrrK','KrRRRRRRRRrK','KrRnnnnnnRrK','KrRnnnnnnRrK','KrrRRRRRRrrK','KKrrrrrrrrKK','.KK......KK.'], P: { K, r: '#8e3b2c', R: '#a34734', n: '#6d2c20' } };
  const sideTable = { rows: ['.KKKKKK.','KmNNNNmK','KNNNNNNK','.KnKKn K'], P: WOOD };
  const openBook = { rows: ['KKKKKKKKKK','KWWWWKWWWWK','KWqqWKWqqWK','KWWWWKWWWWK','KKKKKKKKKK'], P: { K, W: '#f0e4c2', q: '#8a7a5c' } };
  const cat = { rows: ['K.K.....','KKKK....','KooKK...','KKKKKKK.','.KKKKKKK','.KK.KK.K'], P: { K: '#3a332b', o: '#c9962e' } };

  /* ---------------- golden-hall props ---------------- */
  const bannerFlag = { rows: ['KKKKKKKKKK','KggggggggK','KgrrrrrrgK','KgrggggrgK','KgrgrrgrgK','KgrggggrgK','KgrrrrrrgK','.KgggggK..','..KgggK...','...KgK....'], P: { K, g: '#c9962e', r: '#8e3b2c' } };
  const bigFrame = { rows: ['GGGGGGGGGGGGGG','GgWWWWWWWWWWgG','GgWqqqWWqqWWgG','GgWWWWqWWWWWgG','GgWqqWWWqqqWgG','GgWWWWWWWWWWgG','GGGGGGGGGGGGGG'], P: { G: '#c9962e', g: '#a67a1e', W: '#f0e4c2', q: '#8a7a5c' } };
  const bigFrameEmpty = { rows: bigFrame.rows.map((r) => r.replace(/q/g, 'W')), P: { ...bigFrame.P } };
  const trophyPlinth = { rows: ['..KGGGGK..','..KgGGgK..','...KGGK...','..KGGGGK..','..KKKKKK..','..KWWWWK..','..KwWWwK..','.KWWWWWWK.','KKKKKKKKKK'], P: { K, G: '#ffd76a', g: '#c9962e', W: '#d8cba8', w: '#b8a988' } };
  const trapdoorChain = { rows: ['KKKKKKKKKKKKKK','KnnnnnnnnnnnnK','KnNNNNNNNNNNnK','KnNNKKKKKKNNnK','KnNNKffffKNNnK','KnNNKKKKKKNNnK','KnNNNNNNNNNNnK','KnnnnnnnnnnnnK','KKKKKKKKKKKKKK'], P: { ...WOOD, f: '#4a4a52' } };

  /* ---------------- hall props ---------------- */
  const questBoardBig = { rows: ['KKKKKKKKKKKKKKKKKKKKKKKKKKKK','KNNNNNNNNNNNNNNNNNNNNNNNNNNK','KNWWWWWWWWWNNWWWWWWWNNWWWWNK','KNWqqqqqqWWNNWqqqqWWNNWqqWNK','KNWWggWWWWWNNWWWWWWWNNWWWWNK','KNWqqqqWWWWNNWqqgqWWNNWgqWNK','KNWWWWWWWWWNNWWWWWWWNNWWWWNK','KNWqqgqqWWWNNWqqqqWWNNWqqWNK','KNWWWWWWWWWNNWWWWWWWNNWWWWNK','KNNNNNNNNNNNNNNNNNNNNNNNNNNK','KKKKKKKKKKKKKKKKKKKKKKKKKKKK'], P: { ...WOOD, g: '#c9962e' } };
  const bench = { rows: ['KKKKKKKKKKKKKKKK','KmmmmmmmmmmmmmmK','KNNNNNNNNNNNNNNK','.KnK........KnK.','.KnK........KnK.'], P: WOOD };
  const coatRack = { rows: ['..KNK..','.KNNNK.','KrK.KcK','KrK.KcK','KrrK.K.','..KNK..','..KNK..','.KKKKK.'], P: { K, N: '#8a5a32', r: '#8e3b2c', c: '#3f5470' } };

  /* ---------------- floors + walls ---------------- */
  function floorTiles(svg, x, y, w, h, a, b, seam, mode) {
    for (let cy = y; cy < y + h; cy++) for (let cx = x; cx < x + w; cx++) {
      rect(svg, cx * T, cy * T, T, T, ((cx + cy) % 2 ? a : b));
      if (mode === 'plank') { rect(svg, cx * T, cy * T + T - PX, T, PX, seam); if (cx % 2 === 0) rect(svg, cx * T, cy * T, PX, T, seam + '66'); }
      else if (mode === 'tile') { rect(svg, cx * T, cy * T, T, PX, seam); rect(svg, cx * T, cy * T, PX, T, seam); }
      else if (mode === 'dirt') { rect(svg, cx * T + ((cx * 7 + cy * 13) % 9) * PX, cy * T + ((cx * 5 + cy * 11) % 9) * PX, PX, PX, seam); }
      else if (mode === 'flag') { rect(svg, cx * T, cy * T, T, PX, seam); if ((cx + cy) % 2) rect(svg, cx * T, cy * T, PX, T, seam); }
    }
  }
  function carpet(svg, x, y, w, h, base, dark, light) {
    for (let cy = y; cy < y + h; cy++) for (let cx = x; cx < x + w; cx++) rect(svg, cx * T, cy * T, T, T, ((cx + cy) % 2 ? base : dark));
    rect(svg, x * T, y * T, w * T, PX, light); rect(svg, x * T, (y + h) * T - PX, w * T, PX, light);
    rect(svg, x * T, y * T, PX, h * T, light); rect(svg, (x + w) * T - PX, y * T, PX, h * T, light);
  }
  const WC = { cap: '#17100a', face: '#3b2c1f', seam: '#2b2015', base: '#5c462e' };

  /* ---------------- region → room + config ---------------- */
  const OROOMS = {
    tower:      { region: [0, 0, 11, 10],  verbs: { work: 'reading the account…', rest: 'zzz — back Mon 1pm' } },
    mine:       { region: [11, 0, 12, 10], verbs: { work: 'mining the market…', rest: 'zzz' } },
    weathertop: { region: [23, 0, 11, 10], verbs: { work: 'storming seeds…', rest: 'zzz' } },
    council:    { region: [34, 0, 12, 10], verbs: { work: 'locking DNA…', rest: 'zzz' } },
    forge:      { region: [13, 10, 33, 9] },
    library:    { region: [13, 19, 16, 9] },
    hall:       { region: [29, 19, 17, 9] },
  };
  const REF = {};

  /* label + bubble helpers (in SVG so they scale with the room) */
  function tagLabel(svg, cx, cy) {
    const t = document.createElementNS(NS, 'text');
    t.setAttribute('x', cx * T); t.setAttribute('y', cy * T);
    t.setAttribute('text-anchor', 'middle'); t.setAttribute('font-size', '15');
    t.setAttribute('fill', '#f0e2ba'); t.setAttribute('stroke', '#120c07');
    t.setAttribute('stroke-width', '3.4'); t.setAttribute('paint-order', 'stroke');
    t.setAttribute('letter-spacing', '.06em'); t.style.fontFamily = 'VT323, monospace';
    svg.appendChild(t); return t;
  }
  function bubble(svg, cx, cy) {
    const g = document.createElementNS(NS, 'g'); g.style.display = 'none';
    const box = document.createElementNS(NS, 'rect');
    box.setAttribute('rx', 4); box.setAttribute('fill', '#f6edd4'); box.setAttribute('stroke', '#241a10'); box.setAttribute('stroke-width', '1.5');
    const tail = document.createElementNS(NS, 'polygon'); tail.setAttribute('fill', '#241a10');
    const txt = document.createElementNS(NS, 'text');
    txt.setAttribute('y', cy * T - 8); txt.setAttribute('font-size', '14'); txt.setAttribute('fill', '#2b1d12');
    txt.setAttribute('text-anchor', 'middle'); txt.setAttribute('x', cx * T); txt.style.fontFamily = 'VT323, monospace';
    g.appendChild(box); g.appendChild(tail); g.appendChild(txt); svg.appendChild(g);
    return {
      set(s, zz) {
        txt.textContent = s;
        const w = s.length * 6.6 + 14, x = cx * T - w / 2, y = cy * T - 24;
        box.setAttribute('x', x); box.setAttribute('y', y); box.setAttribute('width', w); box.setAttribute('height', 20);
        tail.setAttribute('points', `${x + 12},${y + 20} ${x + 22},${y + 20} ${x + 13},${y + 27}`);
        txt.setAttribute('fill', zz ? '#8a7a5c' : '#2b1d12');
        txt.style.fontStyle = zz ? 'italic' : 'normal';
      },
      show(b) { g.style.display = b ? '' : 'none'; },
    };
  }

  function build(svg) {
    /* floors */
    floorTiles(svg, 0, 0, 11, 10, '#3c4156', '#383d50', '#2c3040', 'tile');
    floorTiles(svg, 11, 0, 12, 10, '#77603f', '#6f5939', '#57452c', 'dirt');
    floorTiles(svg, 23, 0, 11, 10, '#a3804f', '#9a7849', '#83653a', 'plank');
    floorTiles(svg, 34, 0, 12, 10, '#66482c', '#5e4227', '#4c3620', 'plank');
    floorTiles(svg, 0, 10, 13, 18, '#6f6a5e', '#676254', '#565244', 'flag');
    floorTiles(svg, 13, 10, 33, 9, '#4b4640', '#45403a', '#38342f', 'tile');
    floorTiles(svg, 13, 19, 16, 9, '#8a6a42', '#82633c', '#6b5333', 'plank');
    floorTiles(svg, 29, 19, 17, 9, '#a5813f', '#9c7939', '#87682f', 'plank');
    /* carpets */
    carpet(svg, 25.5, 3.5, 6, 4, '#42586f', '#3a4d61', '#4e6780');
    carpet(svg, 31, 22, 13, 4, '#8e3b2c', '#7c3225', '#a34734');
    carpet(svg, 14, 23.5, 4.5, 3.5, '#5d7548', '#52673f', '#6b8654');
    carpet(svg, 1.5, 11.5, 10, 1.8, '#8e3b2c', '#7c3225', '#a34734');
    carpet(svg, 4.7, 10.15, 2.6, 1.2, '#7c3225', '#6d2c20', '#8e3b2c');
    /* walls */
    const wallH = (x, y, w) => { rect(svg, x * T, y * T, w * T, T * 1.3, WC.face); for (let i = 0; i < w; i += 2) rect(svg, (x + i) * T, y * T, PX, T * 1.3, WC.seam); rect(svg, x * T, y * T, w * T, T * 0.4, WC.cap); rect(svg, x * T, y * T + T * 1.3 - PX, w * T, PX, WC.base); };
    const wallV = (x, y0, len) => rect(svg, x * T - PX * 2, y0 * T, PX * 4, len * T, WC.cap);
    wallH(0, 0, 46); wallH(0, 10, 46); wallH(13, 19, 33);
    wallV(11, 0, 10); wallV(23, 0, 10); wallV(34, 0, 10); wallV(13, 10, 18); wallV(29, 19, 9);
    const door = (x, y, w, h, f) => rect(svg, x * T, y * T, w * T, h * T, f);
    door(4.7, 10, 2.6, 1.35, '#6f6a5e'); door(16.8, 10, 2.6, 1.35, '#4b4640'); door(27, 10, 2.6, 1.35, '#4b4640');
    door(39, 10, 2.6, 1.35, '#4b4640'); door(12.8, 13.6, 1.2, 2.3, '#4b4640'); door(19, 19, 2.6, 1.35, '#8a6a42');
    door(36, 19, 2.6, 1.35, '#a5813f'); door(28.8, 23, 1.2, 2.3, '#a5813f');
    rect(svg, 0, 0, 46 * T, PX, '#000'); rect(svg, 0, 28 * T - PX, 46 * T, PX, '#000');
    rect(svg, 0, 0, PX, 28 * T, '#000'); rect(svg, 46 * T - PX, 0, PX, 28 * T, '#000');

    /* ---- WATCH ROOM ---- */
    svgAdd(svg, conspiracyBoard.rows, 2.2, 0.35, conspiracyBoard.P);
    svgAdd(svg, palantirDesk.rows, 1.2, 3.4, palantirDesk.P, 'oglow');
    svgAdd(svg, telescope.rows, 7.6, 2.6, telescope.P);
    svgAdd(svg, globeProp.rows, 9.2, 6.4, globeProp.P);
    svgAdd(svg, writeDesk.rows, 3.8, 6.2, writeDesk.P);
    svgAdd(svg, candleWall.rows, 0.5, 1.5, candleWall.P); svgAdd(svg, candleWall.rows, 10, 1.5, candleWall.P);
    const scout = chibi(['#5b4a63', '#7a6a86'], ['#4a5a78', '#3a4a63', '#5a6a88']);
    REF.tower = { chars: [svgAdd(svg, scout.rows, 5.3, 4.4, scout.P, 'ochar')], bubbles: [], seatIdx: 0 };

    /* ---- THE MINES ---- */
    svgAdd(svg, supportBeam.rows, 11.4, 1.35, supportBeam.P); svgAdd(svg, supportBeam.rows, 19.8, 1.35, supportBeam.P);
    svgAdd(svg, minecart.rows, 12, 3.2, minecart.P); svgAdd(svg, scrollPile.rows, 12.6, 2.6, scrollPile.P);
    svgAdd(svg, lanternPost.rows, 15.2, 2.2, lanternPost.P, 'oflick'); svgAdd(svg, barrel.rows, 21.4, 2.6, barrel.P);
    svgAdd(svg, crateStack.rows, 21, 4.2, crateStack.P); svgAdd(svg, scrollPile.rows, 13.2, 6.2, scrollPile.P);
    svgAdd(svg, writeDesk.rows, 15, 5.2, writeDesk.P);
    const miner = chibi(['#6e4626', '#8a5a32'], ['#7a5230', '#5c3d22', '#8a6a42']);
    REF.mine = { chars: [svgAdd(svg, seated(miner).rows, 15.9, 3.4, miner.P, 'ochar')] };
    svgAdd(svg, lanternPost.rows, 19.4, 7.6, lanternPost.P, 'oflick');

    /* ---- STORM ROOM ---- */
    svgAdd(svg, jarShelf.rows, 26.4, 0.35, jarShelf.P); svgAdd(svg, dartboard.rows, 24.2, 0.55, dartboard.P);
    svgAdd(svg, roundTableBig.rows, 26.2, 3.8, roundTableBig.P); svgAdd(svg, chestBig.rows, 23.5, 7.4, chestBig.P);
    svgAdd(svg, plantBig.rows, 23.4, 1.6, plantBig.P); svgAdd(svg, scrollPile.rows, 31.6, 7.8, scrollPile.P);
    const storm = chibi(['#3f5470', '#4e6780'], ['#42586f', '#36485c', '#4e6780']);
    REF.weathertop = { chars: [svgAdd(svg, storm.rows, 31.0, 3.9, storm.P, 'ochar')] };

    /* ---- COUNCIL ---- */
    svgAdd(svg, tapestry.rows, 34.6, 0.35, tapestry.P); svgAdd(svg, scrollRack.rows, 43.6, 0.5, scrollRack.P);
    svgAdd(svg, mapTableLong.rows, 35.2, 3.9, mapTableLong.P);
    svgAdd(svg, highChair.rows, 36.6, 7.6, highChair.P); svgAdd(svg, highChair.rows, 40.6, 7.6, highChair.P);
    svgAdd(svg, candleWall.rows, 38.5, 1.6, candleWall.P); svgAdd(svg, plantBig.rows, 44.4, 6.8, plantBig.P);
    const strategist = chibi(['#5a3f73', '#7a5a96'], ['#5a3f73', '#4a3460', '#7a5a96']);
    REF.council = { chars: [svgAdd(svg, seated(strategist).rows, 38.6, 1.9, strategist.P, 'ochar')] };

    /* ---- HALLWAY (ambient) ---- */
    svgAdd(svg, questBoardBig.rows, 1.6, 11.55, questBoardBig.P);
    svgAdd(svg, bench.rows, 8.4, 13.2, bench.P); svgAdd(svg, coatRack.rows, 0.6, 13.1, coatRack.P);
    svgAdd(svg, torchWall.rows, 3.2, 11.6, torchWall.P, 'oflick'); svgAdd(svg, torchWall.rows, 9.4, 11.6, torchWall.P, 'oflick');
    svgAdd(svg, plantBig.rows, 0.8, 25.2, plantBig.P); svgAdd(svg, plantBig.rows, 10.6, 25.2, plantBig.P);
    /* the porter walks a short corridor loop */
    const porter = chibi(['#c9962e', '#ffd76a'], ['#8a7a5c', '#6e6248', '#a89a72']);
    const pg = svgAdd(svg, porter.rows, 0, 0, porter.P, 'ochar');
    const ppath = document.createElementNS(NS, 'path');
    ppath.setAttribute('id', 'porterpath'); ppath.setAttribute('d', 'M150,420 C150,540 300,560 210,660 C150,720 240,760 210,780');
    ppath.setAttribute('fill', 'none'); svg.appendChild(ppath);
    const pm = document.createElementNS(NS, 'animateMotion');
    pm.setAttribute('dur', '46s'); pm.setAttribute('repeatCount', 'indefinite');
    pm.setAttribute('keyPoints', '0;1;0'); pm.setAttribute('keyTimes', '0;0.5;1'); pm.setAttribute('calcMode', 'linear');
    const pmp = document.createElementNS(NS, 'mpath'); pmp.setAttribute('href', '#porterpath');
    pm.appendChild(pmp); pg.appendChild(pm); pg.classList.add('typebob');

    /* ---- FORGE ---- */
    svgAdd(svg, furnace.rows, 13.6, 10.6, furnace.P, 'oflick');
    svgAdd(svg, toolWall.rows, 19.4, 11.45, toolWall.P); svgAdd(svg, swordRack.rows, 41.4, 11.45, swordRack.P);
    svgAdd(svg, writeDesk.rows, 17.6, 13.6, writeDesk.P);
    const mario = chibi(['#a04030', '#c9554a'], ['#a04030', '#7c3225', '#c9554a']);
    const mChar = svgAdd(svg, seated(mario).rows, 18.6, 11.8, mario.P, 'ochar');
    svgAdd(svg, anvilBig.rows, 24.4, 15.4, anvilBig.P); svgAdd(svg, quenchBarrel.rows, 27.6, 15.6, quenchBarrel.P);
    svgAdd(svg, judgeDesk.rows, 31.2, 14.2, judgeDesk.P);
    const judge = hooded(['#241f19', '#3a332b'], ['#241f19', '#161310']);
    const jChar = svgAdd(svg, judge.rows, 31.8, 11.9, judge.P, 'ochar');
    REF.forge = { chars: [mChar, jChar] };
    svgAdd(svg, scrollPile.rows, 35.4, 14.4, scrollPile.P); svgAdd(svg, plantBig.rows, 44.2, 12.2, plantBig.P);
    svgAdd(svg, torchWall.rows, 23, 11.6, torchWall.P, 'oflick'); svgAdd(svg, torchWall.rows, 38, 11.6, torchWall.P, 'oflick');

    /* ---- LIBRARY ---- */
    svgAdd(svg, tallShelf.rows, 13.6, 19.5, tallShelf.P); svgAdd(svg, tallShelf.rows, 20.4, 19.5, tallShelf.P);
    svgAdd(svg, ladder.rows, 19.2, 20.2, ladder.P);
    svgAdd(svg, armchair.rows, 14.6, 24, armchair.P); svgAdd(svg, armchair.rows, 17, 24, armchair.P);
    svgAdd(svg, sideTable.rows, 16.4, 25.4, sideTable.P); svgAdd(svg, candleWall.rows, 16.6, 24.9, candleWall.P);
    svgAdd(svg, openBook.rows, 24.4, 24.6, openBook.P); svgAdd(svg, writeDesk.rows, 22.4, 23.6, writeDesk.P);
    svgAdd(svg, cat.rows, 26.8, 26.4, cat.P); svgAdd(svg, plantBig.rows, 27.4, 20.9, plantBig.P);
    REF.library = { chars: [] };

    /* ---- GOLDEN HALL ---- */
    svgAdd(svg, bannerFlag.rows, 30.4, 19.35, bannerFlag.P); svgAdd(svg, bannerFlag.rows, 44.4, 19.35, bannerFlag.P);
    svgAdd(svg, bigFrame.rows, 33.4, 19.6, bigFrame.P); svgAdd(svg, bigFrame.rows, 37.4, 19.6, bigFrame.P);
    svgAdd(svg, bigFrameEmpty.rows, 41.4, 19.6, bigFrameEmpty.P);
    svgAdd(svg, torchWall.rows, 32.4, 19.7, torchWall.P, 'oflick'); svgAdd(svg, torchWall.rows, 40.6, 19.7, torchWall.P, 'oflick');
    svgAdd(svg, trophyPlinth.rows, 32.6, 22.4, trophyPlinth.P); svgAdd(svg, trophyPlinth.rows, 41.8, 22.4, trophyPlinth.P);
    svgAdd(svg, trapdoorChain.rows, 43.6, 25.2, trapdoorChain.P); svgAdd(svg, plantBig.rows, 29.8, 25.2, plantBig.P);
    REF.hall = { chars: [] };

    /* ---- dim overlays (one per room, drawn over props) ---- */
    for (const [id, cfg] of Object.entries(OROOMS)) {
      const [x, y, w, h] = cfg.region;
      const dim = rect(svg, x * T, y * T, w * T, h * T, id === 'tower' ? '#0c0e1c' : '#0a0806');
      dim.setAttribute('opacity', '0'); dim.setAttribute('pointer-events', 'none');
      REF[id].dim = dim;
    }

    /* ---- tags + bubbles (above dim) ---- */
    const TAGXY = { tower: [5.5, 8.75], mine: [17, 8.75], weathertop: [28.5, 8.75], council: [40, 8.75], forge: [29.5, 17.35], library: [21, 26.85], hall: [37.5, 26.85] };
    for (const [id, xy] of Object.entries(TAGXY)) REF[id].tag = tagLabel(svg, xy[0], xy[1]);
    REF.tower.bubbles = [bubble(svg, 5.3, 4.0)];
    REF.mine.bubbles = [bubble(svg, 17.4, 3.6)];
    REF.weathertop.bubbles = [bubble(svg, 32.2, 4.1)];
    REF.council.bubbles = [bubble(svg, 40.1, 2.1)];
    REF.forge.bubbles = [bubble(svg, 20.5, 11.9), bubble(svg, 33.6, 11.9)];

    /* ---- click regions (topmost) ---- */
    for (const [id, cfg] of Object.entries(OROOMS)) {
      const [x, y, w, h] = cfg.region;
      const c = rect(svg, x * T, y * T, w * T, h * T, 'transparent', 'oclick');
      c.style.cursor = 'pointer';
      c.addEventListener('click', () => Studio.openRoom(id));
    }
  }

  function applyChar(charGroup, status) {
    if (!charGroup) return;
    charGroup.classList.remove('working', 'idle', 'resting');
    charGroup.classList.add(status === 'hot' ? 'working' : status === 'warm' ? 'idle' : 'resting');
  }

  function update(state) {
    for (const [id, cfg] of Object.entries(OROOMS)) {
      const room = state.rooms[id]; if (!room) continue;
      const ref = REF[id]; const st = room.status;
      /* tag */
      ref.tag.textContent = `${Studio.meta[id].name.toUpperCase()} · ${Studio.meta[id].count(room)}`;
      /* dim */
      ref.dim.setAttribute('opacity', st === 'quiet' ? (id === 'tower' ? '0.5' : '0.4') : st === 'warm' ? '0.12' : '0');
      /* characters + bubbles */
      (ref.chars || []).forEach((c) => applyChar(c, st));
      if (id === 'forge') {
        const [mb, jb] = ref.bubbles;
        if (st === 'hot') { mb.set(cfg && REF ? 'hammering hooks…' : '', false); mb.show(true); jb.set('grading…', false); jb.show(true); }
        else if (st === 'quiet') { mb.set('forge banked', true); mb.show(true); jb.show(false); }
        else { mb.show(false); jb.show(false); }
      } else if (ref.bubbles && ref.bubbles.length && cfg.verbs) {
        const b = ref.bubbles[0];
        if (st === 'hot') { b.set(cfg.verbs.work, false); b.show(true); }
        else if (st === 'quiet') { b.set(cfg.verbs.rest, true); b.show(cfg.verbs.rest !== ''); }
        else { b.show(false); }
      }
    }
  }

  Studio.registerView('office', { el: '#office', wrap: '#office-wrap', build, update });
})();
