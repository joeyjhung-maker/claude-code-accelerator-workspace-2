/* ============ The Studio — the coverage board (strategy map, live) ============ */
'use strict';
(function () {
  const AW_LABEL = { unaware: 'Unaware', problem: 'Problem', solution: 'Solution', product: 'Product', 'most-aware': 'Most-aware' };
  const stateOf = (c) => c.written ? 'writ' : c.brief ? 'brief' : c.seeds ? 'seed' : 'gap';
  const STATE_WORD = { writ: 'written', brief: 'briefed', seed: 'seeded', gap: 'gap' };

  function build(el) {
    el.innerHTML = '<div class="warframe"><div class="warhead"></div><div class="warbody"></div></div>';
  }

  function update(state) {
    const cov = state.coverage;
    const el = document.getElementById('board');
    if (!cov) { el.querySelector('.warbody').innerHTML = '<p class="warempty">No strategy map to read yet.</p>'; return; }
    const { segments, awareness, cells, tally } = cov;

    el.querySelector('.warhead').innerHTML = `
      <h2>The War Table</h2>
      <p>where the pipeline covers the strategy map — segment &times; awareness, read live from seed tags &amp; brief DNA</p>`;

    // grid
    let grid = '<table class="wargrid"><thead><tr><th class="corner"></th>';
    for (const a of awareness) grid += `<th>${AW_LABEL[a] || a}</th>`;
    grid += '</tr></thead><tbody>';
    for (const s of segments) {
      grid += `<tr><th class="segname">${s.name}</th>`;
      for (const a of awareness) {
        const c = cells[s.id][a];
        const st = stateOf(c);
        const label = c.seeds ? `${c.seeds}` : (st === 'writ' ? '★' : st === 'brief' ? '◆' : '');
        const title = `${s.name} × ${AW_LABEL[a] || a} — ${STATE_WORD[st]}` +
          (c.seeds ? `, ${c.seeds} seed${c.seeds > 1 ? 's' : ''}` : '') +
          (c.written ? ' (copy shipped)' : c.brief ? ' (brief locked)' : '');
        grid += `<td class="cell c-${st}" title="${title}"><span class="cellmark">${label}</span></td>`;
      }
      grid += '</tr>';
    }
    grid += '</tbody></table>';

    const legend = `<div class="warlegend">
      <span><i class="sw c-gap"></i> gap — nothing yet</span>
      <span><i class="sw c-seed"></i> seeded — ideas banked (number = count)</span>
      <span><i class="sw c-brief"></i> briefed — DNA locked</span>
      <span><i class="sw c-writ"></i> written — copy shipped</span>
    </div>`;

    const tallyRow = `<div class="wartally">
      <span class="t-writ"><b>${tally.written}</b> written</span>
      <span class="t-brief"><b>${tally.briefed}</b> briefed</span>
      <span class="t-seed"><b>${tally.seeded}</b> seeded</span>
      <span class="t-gap"><b>${tally.gaps}</b> open gaps</span>
      <span class="tallyhint">of ${segments.length * awareness.length} cells</span>
    </div>`;

    // read the empty columns/rows as plain-English gaps
    const emptyCols = awareness.filter((a) => segments.every((s) => stateOf(cells[s.id][a]) === 'gap'));
    const notes = emptyCols.length
      ? `<p class="warnote">&#9888; No coverage anywhere at: <b>${emptyCols.map((a) => AW_LABEL[a]).join(', ')}</b>. Whole awareness bands untouched — the biggest open territory.</p>`
      : '';

    el.querySelector('.warbody').innerHTML = grid + legend + tallyRow + notes;
  }

  Studio.registerView('board', { el: '#board', wrap: '#board-wrap', build, update });
})();
