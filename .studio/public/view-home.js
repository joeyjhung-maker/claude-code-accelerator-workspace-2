/* ============ The Studio — The Gatehouse (projects + machine sync) ============ */
'use strict';
(function () {
  const dot = (a) => `<i class="pdot ${a || 'quiet'}"></i>`;

  function build(el) {
    el.innerHTML = '<div class="gateframe"><div class="gatehead"></div><div class="gatebody"></div></div>';
  }

  function jvCard(j) {
    const facts = `
      <span class="jfact"><b>${j.research}</b> research</span>
      <span class="jfact"><b>${j.sellTheir}</b> their-offer</span>
      <span class="jfact"><b>${j.sellOur}</b> our-offer</span>`;
    const tags = [];
    if (j.hasCampaignPlan) tags.push('<span class="jtag">campaign plan</span>');
    if (j.hasOnePager) tags.push('<span class="jtag">one-pager</span>');
    const open = j.partnerFile ? ` data-p="${encodeURIComponent(j.partnerFile)}"` : '';
    return `<div class="jvcard"${open} title="${j.partnerFile ? 'open partner brief' : ''}">
      <div class="jvtop">${dot(j.activity)}<span class="jvname">${j.name}</span>
        <span class="jage">${j.lastActivity ? Studio.ago(j.lastActivity) : '—'}</span></div>
      <div class="jfacts">${facts}</div>
      ${tags.length ? `<div class="jtags">${tags.join('')}</div>` : ''}
    </div>`;
  }

  function clientCard(c) {
    const s = c.stats;
    const statChips = s ? `<div class="cstats">
      <span class="cstat"><b>${s.seeds}</b> seeds</span>
      <span class="cstat"><b>${s.briefsReady}</b> briefs ready</span>
      <span class="cstat"><b>${s.briefsWritten}</b> written</span>
      <span class="cstat"><b>${s.copyThisWeek}</b> forged/wk</span>
      <span class="cstat"><b>${s.winners}</b> winners</span></div>` : '';
    const jvs = (c.jvs && c.jvs.length)
      ? `<div class="jvwrap"><div class="jvlabel">&#9096; JV deals (${c.jvs.length})</div>
         <div class="jvgrid">${c.jvs.map(jvCard).join('')}</div></div>`
      : '';
    const openC = c.clientFile ? ` data-p="${encodeURIComponent(c.clientFile)}"` : '';
    return `<div class="clientCard">
      <div class="ctop">${dot(c.activity)}<span class="cname"${openC}>${c.name}</span>
        <span class="ckind">client</span>
        <span class="cage">${c.lastActivity ? Studio.ago(c.lastActivity) : '—'}</span></div>
      ${statChips}${jvs}</div>`;
  }

  function syncPanel(sync) {
    if (!sync) return '';
    const facts = [];
    if (typeof sync.dirty === 'number') facts.push(`<span><b>${sync.dirty}</b> unsaved file${sync.dirty === 1 ? '' : 's'}</span>`);
    if (typeof sync.ahead === 'number') facts.push(`<span><b>${sync.ahead}</b> ahead</span>`);
    if (typeof sync.behind === 'number') facts.push(`<span><b>${sync.behind}</b> behind</span>`);
    if (sync.lastCommitAt) facts.push(`<span>last save ${Studio.ago(sync.lastCommitAt)}</span>`);
    const fetched = sync.fetchedAt ? `checked GitHub ${Studio.ago(sync.fetchedAt)}` : 'not checked yet';
    return `<div class="syncPanel tone-${sync.tone}">
      <div class="synchead">&#9906; Machine sync</div>
      <div class="syncverdict">${sync.message}</div>
      <div class="syncfacts">${facts.join('')}</div>
      <div class="syncactions">
        <span class="syncfetch-age">${fetched}</span>
        <button class="syncfetch">&#8635; check GitHub now</button>
      </div>
      <div class="syncnote">This panel only reports. The buttons stay on the double-click files:
        <b>Start Work</b> when you sit down, <b>Finish Work</b> when you get up.</div>
    </div>`;
  }

  function wire(el, state) {
    el.querySelectorAll('[data-p]').forEach((n) => {
      n.addEventListener('click', (e) => {
        e.stopPropagation();
        Studio.openDoc(decodeURIComponent(n.dataset.p));
      });
    });
    const fb = el.querySelector('.syncfetch');
    if (fb) fb.addEventListener('click', async () => {
      fb.disabled = true; fb.textContent = 'checking…';
      try {
        const res = await fetch('/api/sync/refresh');
        state.sync = await res.json();
        update(state);
      } catch (e) {
        fb.disabled = false; fb.textContent = '&#8635; check failed — retry';
      }
    });
  }

  function update(state) {
    const el = document.getElementById('home');
    el.querySelector('.gatehead').innerHTML = `
      <h2>The Gatehouse</h2>
      <p>everything running &mdash; and whether it's safe to switch machines &mdash; read live from the vault</p>`;
    const clients = (state.projects && state.projects.clients) || [];
    const cards = clients.length ? clients.map(clientCard).join('') : '<p class="gateempty">No clients yet.</p>';
    el.querySelector('.gatebody').innerHTML =
      `<div class="projlabel">&#9733; Projects</div>${cards}${syncPanel(state.sync)}`;
    wire(el, state);
  }

  Studio.registerView('home', { el: '#home', wrap: '#home-wrap', build, update });
})();
