// Agent swarm "build mode": add ?build to any page URL.
(async () => {
  if (!new URLSearchParams(location.search).has('build')) return;
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const blocks = [...document.querySelectorAll('[data-b]')];
  blocks.forEach(b => b.classList.add('b-hide'));
  const cols = ['#a9e1ec', '#5df2a4', '#ffb86b', '#ff7aa8', '#b49cff', '#7fd4ff', '#ffe066'];
  const names = ['Claude', 'layout', 'copy', 'motion', 'style', 'grid', 'type', 'links', 'assets', 'a11y', 'seo', 'qa', 'deploy', 'icons'];
  const arrow = '<svg viewBox="0 0 16 16"><path d="M1 1l13 6-6 1.5L6 15z" fill="currentColor" stroke="#041014"/></svg>';
  const curs = names.map((n, i) => {
    const el = document.createElement('div');
    el.className = 'b-cur';
    el.style.setProperty('--c', cols[i % cols.length]);
    el.style.color = cols[i % cols.length];
    el.innerHTML = arrow + `<span>${n === 'Claude' ? n : 'agent-' + String(i).padStart(2, '0') + ' · ' + n}</span>`;
    el.style.left = innerWidth / 2 + 'px'; el.style.top = scrollY + innerHeight / 2 + 'px';
    document.body.appendChild(el);
    return el;
  });
  const total = document.querySelectorAll('[data-b] *').length + blocks.length;
  let layers = 0;
  const pill = document.createElement('div');
  pill.id = 'b-pill';
  document.body.appendChild(pill);
  const setPill = (s, done) => pill.innerHTML = `<span class="dot"></span>${curs.length} agents · ${layers}/${total} layers · ${s}` + (done ? '' : '');
  setPill('building');
  const page = el => { const r = el.getBoundingClientRect(); return { x: r.left + scrollX, y: r.top + scrollY, w: r.width, h: r.height }; };
  const add = (cls, css, html = '') => { const e = document.createElement('div'); e.className = cls; for (const k in css) e.style.setProperty(k, css[k]); e.innerHTML = html; document.body.appendChild(e); return e; };

  for (const [i, b] of blocks.entries()) {
    b.scrollIntoView({ behavior: 'smooth', block: 'center' });
    await sleep(450);
    const r = page(b), c = cols[i % cols.length];
    const g1 = add('b-guide', { top: r.y + 'px', '--c': c });
    const g2 = add('b-guide', { top: r.y + r.h + 'px', '--c': c });
    const box = add('b-box', { left: r.x + 'px', top: r.y + 'px', width: r.w + 'px', height: r.h + 'px', '--c': c },
      '<i style="left:-4px;top:-4px"></i><i style="right:-4px;top:-4px"></i><i style="left:-4px;bottom:-4px"></i><i style="right:-4px;bottom:-4px"></i>' +
      `<b>${b.dataset.b} · ${Math.round(r.w)}×${Math.round(r.h)}</b>`);
    curs.forEach((cu, k) => {
      const near = k % 3 !== 0;
      cu.style.left = (near ? r.x + Math.random() * r.w : Math.random() * (innerWidth - 120)) + 'px';
      cu.style.top = (near ? r.y + Math.random() * r.h : r.y + (Math.random() - .5) * innerHeight * .8) + 'px';
    });
    await sleep(600);
    b.classList.add('b-show');
    const hs = [...b.querySelectorAll('h1,h2,h3')];
    hs.forEach(h => { h.style.clipPath = 'inset(0 100% 0 0)'; });
    for (const h of hs) {
      void h.offsetWidth; h.style.transition = 'clip-path .7s steps(18)';
      h.style.clipPath = 'inset(0 0 0 0)';
      await sleep(450);
    }
    layers += b.querySelectorAll('*').length + 1;
    setPill('building');
    await sleep(350);
    [box, g1, g2].forEach(e => e.remove());
  }
  layers = total;
  pill.innerHTML = '<span class="dot"></span>' + curs.length + ' agents · ' + total + '/' + total + ' layers · deployed ✓';
  curs.forEach(cu => { cu.style.transition = 'opacity .6s'; cu.style.opacity = 0; });
  await sleep(900);
  scrollTo({ top: 0, behavior: 'smooth' });
})();
