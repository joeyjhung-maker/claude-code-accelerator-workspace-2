/* ============ The Studio — the overworld map view ============ */
'use strict';
(function () {
  const NS = Studio.SVG_NS;
  const INK = '#2b1d12';
  const PAL = {
    K: INK, S: '#958b76', D: '#6a6051', W: '#eee4c6', N: '#7a5230', n: '#5c3d22',
    R: '#8c4a32', r: '#6d3826', L: '#5d6e59', l: '#48573f', G: '#c9962e', g: '#a67a1e',
    P: '#7b5296', p: '#a67cc4', T: '#4e6b3a', t: '#3c5430', F: '#e07028', M: '#b9c7cc',
    C: '#8a9bb0', y: 'WINDOW', h: '#d8c48e',
  };
  const SPRITES = {
    tower: ['......ppp......','.....pPPPp.....','.....pPPPp.....','......ppp......','....KKKKKKK....','....KSKSKSK....','....KSSDSSK....','.....KSDSK.....','.....KSSSK.....','.....KSySK.....','.....KSSSK.....','.....KDSSK.....','.....KSSDK.....','.....KSySK.....','.....KSSSK.....','....KKSSDKK....','...KSSSDSSSK...','...KSDSSSDSK...','...KSSSySSSK...','..KKKKKKKKKKK..','..hhhhhhhhhhh..'],
    mine: ['.......KK..........','......KDDK.....KK..','.....KDSSDK...KDDK.','....KDSSSSDK.KDSSDK','...KDSSDSSSDKDSSDDK','..KDSSSSSDSSDSSDSDK','.KDSSDSSSSSSDSSSSDK','KDSSSSSKKKKKSSDSSDK','KDSSDSKKgGgKKSSSSDK','KSSSSKKgGGGgKKDSSDK','KDSSDKK.....KKSSSDK','KKKKKKK..y..KKKKKKK','hhhhhKK.....KKhhhhh'],
    weathertop: ['...KK......KK......KK...','..KCCK....KCCK....KCCK..','..KCCK....KCCK....KCCK..','..KCSCK...KCCK...KCSCK..','...KCCK...KSCK...KCCK...','..KCSCK....KK....KCSCK..','..KCCCK..........KCCCK..','.KCCKCCKK..yy..KKCCKCCK.','.KTTTTTTTTTTTTTTTTTTTT.','KTTtTTTTtTTTTTtTTTTtTTK','KTtTTTTTTTtTTTTTTtTTTtK','KKKKKKKKKKKKKKKKKKKKKKK'],
    council: ['.........KK.........','......KKKLLKKK......','....KKLLLLLLLLKK....','..KKLLLLLLLLLLLLKK..','.KLLLLKKKKKKKKLLLLK.','..KKKKKWWWWWWKKKKK..','...KWKWWyWWyWWKWK...','...KWKWWWWWWWWKWK...','...KWKWWyKKyWWKWK...','...KWKWWWKKWWWKWK...','..KKKKKKKKKKKKKKKK..','..hhhhhhhhhhhhhhhh..'],
    forge: ['....KK..............','...KDDK.............','...KDDK....KKKKK....','..KKDDKKKKKrRRRrK...','.KrRRRRRRRrKRRRK....','KrRRRRRRRRRrKKKKK...','KKKKKKKKKKKKKSSDK...','.KSSDSSSSDSKKSSSK...','.KSSySSDSSSKKDSSK...','.KSSSSKKKSSKKSSDK...','.KDSSSKFFKSSKKKKK...','.KSSDSKFFKSDSKnNK...','KKKKKKKKKKKKKKKKKK..','hhhhhhhhhhhhhhhhhh..'],
    library: ['........KKK........','......KKGGGKK......','.....KGGgGgGGK.....','....KGGGGGGGGGK....','...KKKKKKKKKKKKK...','...KWWWWWWWWWWWK...','...KWyWWKKKWWyWK...','...KWWWWKNKWWWWK...','...KWyWWKNKWWyWK...','...KWWWWKNKWWWWK...','..KKKKKKKKKKKKKKK..','..hhhhhhhhhhhhhhh..'],
    hall: ['.........KK.........','.......KKGGKK.......','.....KKGGGGGGKK.....','...KKGGgGGGGgGGKK...','.KKGGGGGGGGGGGGGGKK.','KGGKKKKKKKKKKKKKKGGK','.KKKNWWNWWWWNWWNKKK.','...KNWyNWKKWNyWNK...','...KNWWNWKKWNWWNK...','...KNWyNWKKWNyWNK...','..KKKKKKKKKKKKKKKK..','..hhhhhhhhhhhhhhhh..'],
    pine: ['...K...','..KTK..','.KTtTK.','..KTK..','.KTTtK.','KTtTTTK','...N...','...N...'],
    wanderer1: ['..KKK..','.KDDDK.','.KDDDK.','..KWK..','K.KNK.K','KNNNNNK','.KNNNK.','..K.K..','..K..K.'],
    wanderer2: ['..KKK..','.KDDDK.','.KDDDK.','..KWK..','K.KNK.K','KNNNNNK','.KNNNK.','..K.K..','.K..K..'],
  };
  const VIS = {
    tower:      { pos: [180, 555], scale: 3.4, plaque: 'Palantír Tower', smoke: null },
    mine:       { pos: [335, 205], scale: 3.2, plaque: 'The Mines',      smoke: null },
    weathertop: { pos: [520, 300], scale: 3.0, plaque: 'Weathertop',     smoke: null },
    council:    { pos: [700, 195], scale: 3.3, plaque: 'Council Hall',   smoke: null },
    forge:      { pos: [880, 305], scale: 3.3, plaque: 'The Forge',      smoke: [4.5, 0.5] },
    library:    { pos: [585, 505], scale: 3.1, plaque: 'The Library',    smoke: null },
    hall:       { pos: [1075, 215], scale: 3.3, plaque: 'Golden Hall',   smoke: null },
  };
  const ROAD = 'M180,565 C205,470 250,262 335,215 C425,172 445,270 520,303 C598,333 628,203 700,201 C782,198 802,273 880,315 C958,348 1000,240 1075,226';
  const SPUR = 'M523,303 C543,384 562,440 585,512';

  function drawSprite(rows, scale) {
    const g = document.createElementNS(NS, 'g');
    g.setAttribute('class', 'sprite');
    rows.forEach((row, ry) => {
      for (let rx = 0; rx < row.length; rx++) {
        const ch = row[rx];
        if (ch === '.') continue;
        const col = PAL[ch]; if (!col) continue;
        const rect = document.createElementNS(NS, 'rect');
        rect.setAttribute('x', rx * scale); rect.setAttribute('y', ry * scale);
        rect.setAttribute('width', scale); rect.setAttribute('height', scale);
        if (col === 'WINDOW') { rect.setAttribute('class', 'win'); rect.setAttribute('fill', '#4a5a78'); }
        else rect.setAttribute('fill', col);
        g.appendChild(rect);
      }
    });
    g.dataset.w = rows[0].length * scale;
    g.dataset.h = rows.length * scale;
    return g;
  }

  function build(svg) {
    const deco = document.createElementNS(NS, 'g');
    deco.innerHTML = `
      <path d="M900,90 L950,38 L1000,90 Z" fill="#b7a476" stroke="${INK}" stroke-width="2"/>
      <path d="M955,95 L1020,26 L1085,95 Z" fill="#c3b183" stroke="${INK}" stroke-width="2"/>
      <path d="M1008,40 L1020,26 L1032,40 L1020,52 Z" fill="#efe8d2"/>
      <path d="M1060,100 L1105,55 L1150,100 Z" fill="#b7a476" stroke="${INK}" stroke-width="2"/>
      <text x="1023" y="122" text-anchor="middle" font-size="17" fill="#6b543a" font-style="italic">the misty mountains</text>`;
    svg.appendChild(deco);

    for (const [d] of [[ROAD], [SPUR]]) {
      const p = document.createElementNS(NS, 'path');
      p.setAttribute('d', d); p.setAttribute('fill', 'none');
      p.setAttribute('stroke', '#6b543a'); p.setAttribute('stroke-width', '3.5');
      p.setAttribute('stroke-dasharray', '2 9'); p.setAttribute('stroke-linecap', 'round');
      if (d === ROAD) p.id = 'roadpath';
      svg.appendChild(p);
    }
    [[225,300,2.6],[415,145,2.2],[640,420,2.4],[520,460,2.2],[960,140,2.2],[770,380,2.6],[190,150,2.2],[1120,330,2.6]]
      .forEach(([x, y, s]) => {
        const t = drawSprite(SPRITES.pine, s);
        t.setAttribute('transform', `translate(${x - (7 * s) / 2}, ${y - 8 * s})`);
        svg.appendChild(t);
      });

    for (const [id, cfg] of Object.entries(VIS)) {
      const group = document.createElementNS(NS, 'g');
      group.setAttribute('class', 'room quiet');
      group.id = `mroom-${id}`;
      group.setAttribute('tabindex', '0');
      group.setAttribute('role', 'button');
      group.setAttribute('aria-label', Studio.meta[id].name);
      const sprite = drawSprite(SPRITES[id], cfg.scale);
      const w = +sprite.dataset.w, h = +sprite.dataset.h;
      const ox = cfg.pos[0] - w / 2, oy = cfg.pos[1] - h;
      const halo = document.createElementNS(NS, 'ellipse');
      halo.setAttribute('class', 'halo');
      halo.setAttribute('cx', cfg.pos[0]); halo.setAttribute('cy', cfg.pos[1] - h / 2.2);
      halo.setAttribute('rx', w * 0.75); halo.setAttribute('ry', h * 0.62);
      halo.setAttribute('fill', '#ffd76a'); halo.setAttribute('opacity', '0');
      group.appendChild(halo);
      sprite.setAttribute('transform', `translate(${ox}, ${oy})`);
      group.appendChild(sprite);
      const sm = document.createElementNS(NS, 'g');
      sm.setAttribute('class', 'smoke');
      const [scx, scy] = cfg.smoke ? [ox + cfg.smoke[0] * cfg.scale, oy + cfg.smoke[1] * cfg.scale] : [cfg.pos[0], oy - 2];
      for (let i = 0; i < 3; i++) {
        const c = document.createElementNS(NS, 'circle');
        c.setAttribute('cx', scx); c.setAttribute('cy', scy); c.setAttribute('r', 4);
        sm.appendChild(c);
      }
      group.appendChild(sm);
      const plaque = document.createElementNS(NS, 'g');
      plaque.setAttribute('class', 'plaque');
      const t1 = document.createElementNS(NS, 'text');
      t1.setAttribute('x', cfg.pos[0]); t1.setAttribute('y', cfg.pos[1] + 22);
      t1.setAttribute('text-anchor', 'middle'); t1.setAttribute('font-size', '21'); t1.setAttribute('fill', INK);
      t1.textContent = cfg.plaque;
      const t2 = document.createElementNS(NS, 'text');
      t2.setAttribute('x', cfg.pos[0]); t2.setAttribute('y', cfg.pos[1] + 41);
      t2.setAttribute('text-anchor', 'middle'); t2.setAttribute('font-size', '17'); t2.setAttribute('fill', '#6b543a');
      t2.setAttribute('class', 'countline'); t2.textContent = '…';
      plaque.appendChild(t1); plaque.appendChild(t2);
      group.appendChild(plaque);
      group.addEventListener('click', () => Studio.openRoom(id));
      group.addEventListener('keydown', (e) => { if (e.key === 'Enter') Studio.openRoom(id); });
      svg.appendChild(group);
    }

    const wg = document.createElementNS(NS, 'g');
    wg.id = 'wanderer';
    const f1 = drawSprite(SPRITES.wanderer1, 2.6); f1.setAttribute('class', 'sprite frame1'); f1.setAttribute('transform', 'translate(-9,-22)');
    const f2 = drawSprite(SPRITES.wanderer2, 2.6); f2.setAttribute('class', 'sprite frame2'); f2.setAttribute('transform', 'translate(-9,-22)');
    wg.appendChild(f1); wg.appendChild(f2);
    const motion = document.createElementNS(NS, 'animateMotion');
    motion.setAttribute('dur', '150s'); motion.setAttribute('repeatCount', 'indefinite');
    motion.setAttribute('keyPoints', '0;1;0'); motion.setAttribute('keyTimes', '0;0.5;1'); motion.setAttribute('calcMode', 'linear');
    const mpath = document.createElementNS(NS, 'mpath'); mpath.setAttribute('href', '#roadpath');
    motion.appendChild(mpath); wg.appendChild(motion); svg.appendChild(wg);
    setInterval(() => wg.classList.toggle('step'), 320);
  }

  function update(state) {
    for (const id of Object.keys(VIS)) {
      const room = state.rooms[id]; if (!room) continue;
      const g = document.getElementById(`mroom-${id}`);
      g.classList.remove('hot', 'warm', 'quiet');
      g.classList.add(room.status);
      g.querySelector('.countline').textContent = Studio.meta[id].count(room);
    }
  }

  Studio.registerView('map', { el: '#map', wrap: '#map-wrap', build, update });
})();
