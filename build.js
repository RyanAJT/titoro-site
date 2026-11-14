// Agent swarm build: plays on a visitor's first home-page visit, or any page with ?build.
// Never scrolls the page: agents build what's on screen, the rest builds as the visitor scrolls to it.
(() => {
  const q = new URLSearchParams(location.search);
  const home = location.pathname === '/' || location.pathname === '/index.html';
  let seen = false; try { seen = sessionStorage.getItem('titoroBuilt') === '1'; } catch (e) {}
  const AUTO = location.pathname.startsWith('/build'); // recording mode: always plays and scrolls itself
  window.BUILD = AUTO || !q.has('nobuild') && q.has('build') || (!q.has('nobuild') && home && !seen && !matchMedia('(prefers-reduced-motion: reduce)').matches);
  if (!window.BUILD) return;
  document.documentElement.classList.add('building');

  const ATOM = 'h1,h2,h3,h4,p,.btn,.mono,.g,.pk,.pain,.eng,.vsr,.orca,details,.stg,.scr,.start,.tile,.feat,.ph,.chip,.find,form,li,.bigT,.prompt,.oc,.core,.get,.sbox,.kwcard,.endc';
  const BOX = '.g,.pk,.pain,.eng,.vsr,.orca,details,.stg,.scr,.start,.tile,.feat,.ph,.chip,.find,form,.prompt,.oc,.core,.get,.sbox,.kwcard,.endc';
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const rnd = (a, b) => a + Math.random() * (b - a);
  const cols = ['#7cc7d6', '#f6c177', '#9ed99a', '#f2a0b8', '#c4b5fd', '#8fb8ff', '#f4d35e', '#ff9e7a'];
  const names = ['Claude', 'layout', 'copy', 'motion', 'type', 'grid', 'color', 'links', 'assets', 'a11y', 'seo', 'qa'];
  const verbs = ['writing', 'aligning', 'kerning', 'placing', 'styling', 'spacing', 'linking', 'checking', 'tuning', 'snapping'];
  const arrow = c => `<svg viewBox="0 0 16 16"><path d="M1.5 1.5l12.5 6-6 1.6-2.2 5.7z" fill="${c}" stroke="#0b1113" stroke-width="1.2" stroke-linejoin="round"/></svg>`;

  addEventListener('DOMContentLoaded', run);

  async function run() {
    const atoms = [];
    document.querySelectorAll('[data-b]').forEach(b => {
      let list = [...b.querySelectorAll(ATOM)].filter(a => !a.parentElement.closest(BOX));
      if (!list.length) list = [b];
      list.forEach(a => a.classList.add('bx-hide'));
      atoms.push(...list);
    });
    const total = atoms.length, queue = atoms.slice(), working = new Set();
    const crew = names.slice(0, innerWidth < 700 ? 6 : 12);
    let done = 0, skipped = false, live = true;

    const layer = document.createElement('div');
    layer.id = 'swarm';
    document.body.appendChild(layer);
    const pill = document.createElement('div');
    pill.id = 'pill';
    document.body.appendChild(pill);
    const setPill = s => pill.innerHTML = `<span class="dot"></span><span>${crew.length} agents · ${done}/${total} · ${s}</span>` + (s !== 'deployed ✓' ? '<button>Skip</button>' : '');
    setPill('building');
    pill.addEventListener('click', e => { if (e.target.tagName === 'BUTTON') skipped = true; });

    const add = (cls, css, html = '') => { const e = document.createElement('div'); e.className = cls; e.style.cssText = css; e.innerHTML = html; layer.appendChild(e); return e; };
    const rect = el => { const r = el.getBoundingClientRect(); return { x: r.left + scrollX, y: r.top + scrollY, w: r.width, h: r.height }; };
    const reveal = el => { el.classList.remove('bx-hide'); el.classList.add('bx-in'); done++; setPill('building'); };

    // agents: smooth spring toward a target; goTo resolves inside the frame loop, not on a timer
    const ags = crew.map((n, i) => {
      const c = cols[i % cols.length];
      const el = add('ag', '', arrow(c) + `<span class="tag" style="background:${c}">${n === 'Claude' ? 'Claude' : 'agent-' + String(i).padStart(2, '0') + ' · ' + n}</span><span class="act"></span>`);
      const x = innerWidth / 2 + rnd(-160, 160), y = scrollY + innerHeight / 2 + rnd(-80, 80);
      return { el, c, x, y, vx: 0, vy: 0, tx: x, ty: y, ph: rnd(0, 9), arrive: null };
    });
    const goTo = (a, x, y) => new Promise(res => { a.tx = x; a.ty = y; a.arrive = res; });

    let last = performance.now();
    (function tick(now) {
      const dt = Math.min((now - last) / 16.67, 3); last = now;
      for (const a of ags) {
        const wx = Math.sin(now / 900 + a.ph) * 4, wy = Math.cos(now / 1100 + a.ph) * 4;
        a.vx = (a.vx + (a.tx + wx - a.x) * .028 * dt) * Math.pow(.86, dt);
        a.vy = (a.vy + (a.ty + wy - a.y) * .028 * dt) * Math.pow(.86, dt);
        a.x += a.vx * dt; a.y += a.vy * dt;
        a.el.style.transform = `translate3d(${a.x}px,${a.y}px,0)`;
        if (a.arrive && Math.hypot(a.tx - a.x, a.ty - a.y) < 14) { const r = a.arrive; a.arrive = null; r(); }
      }
      if (live) requestAnimationFrame(tick);
    })(last);
    const act = (a, txt) => { a.el.classList.toggle('busy', !!txt); a.el.querySelector('.act').textContent = txt || ''; };

    // one agent builds one element at a steady pace: fly over, select, sweep, reveal
    async function work(a, el) {
      working.add(el);
      const r = rect(el);
      await goTo(a, r.x + rnd(0, Math.min(r.w, 240)), r.y + rnd(0, Math.min(r.h, 60)));
      const tagName = el.matches(BOX) ? (el.className.split(' ')[0] || 'box') : el.tagName.toLowerCase();
      const sel = add('sel', `left:${r.x}px;top:${r.y}px;width:${r.w}px;height:${r.h}px;--c:${a.c};opacity:0`,
        '<i style="left:-4px;top:-4px"></i><i style="right:-4px;top:-4px"></i><i style="left:-4px;bottom:-4px"></i><i style="right:-4px;bottom:-4px"></i>' +
        `<b>${tagName} · ${Math.round(r.w)}×${Math.round(r.h)}</b>`);
      requestAnimationFrame(() => sel.style.opacity = 1);
      act(a, verbs[(Math.random() * verbs.length) | 0] + '…');
      await Promise.race([goTo(a, r.x + r.w * rnd(.45, .9), r.y + r.h * rnd(.35, .9)), sleep(900)]);
      await sleep(rnd(140, 260));
      reveal(el); working.delete(el); act(a, '');
      sel.style.opacity = 0; setTimeout(() => sel.remove(), 320);
    }

    // next element on screen; anything the visitor already scrolled past (or off to the side) just appears
    function next() {
      for (let i = 0; i < queue.length; i++) {
        const el = queue[i], r = rect(el);
        if (r.w === 0 || r.x > innerWidth - 40 || r.y + r.h < scrollY) { queue.splice(i--, 1); reveal(el); continue; }
        if (r.y < scrollY + innerHeight * .92) { queue.splice(i, 1); return el; }
        return null; // queue is in page order, so the rest is below the fold
      }
      return null;
    }
    async function agent(a, i) {
      await sleep(i * 90);
      while (!skipped && (queue.length || working.size)) {
        const el = next();
        if (el) {
          if (a.parked) { a.parked = false; a.x = rnd(innerWidth * .1, innerWidth * .9); a.y = scrollY + innerHeight + 30; a.vx = a.vy = 0; a.el.style.opacity = 1; } // fly in from below
          await work(a, el); continue;
        }
        if (AUTO) { await goTo(a, rnd(innerWidth * .15, innerWidth * .85), scrollY + innerHeight * rnd(.55, .85)); continue; } // stay on screen while the camera moves
        // nothing on screen left to build: rest out of sight until the visitor scrolls
        if (!a.parked) { a.parked = true; a.el.style.opacity = 0; }
        if (!working.size && queue.length) setPill('scroll ↓');
        await sleep(250);
      }
    }
    // recording mode camera: once the screen is built, glide down to the next part
    if (AUTO) (async () => {
      await sleep(1500);
      while (!skipped && queue.length) {
        const r = rect(queue[0]);
        if (!working.size && r.y > scrollY + innerHeight * .92) { lenis.scrollTo(Math.min(r.y - innerHeight * .25, document.documentElement.scrollHeight), { duration: 1.6, force: true }); await sleep(1900); }
        else await sleep(200);
      }
    })();
    await Promise.all(ags.map(agent));

    // finish
    document.querySelectorAll('.bx-hide').forEach(e => { e.classList.remove('bx-hide'); e.classList.add('bx-in'); });
    done = total; setPill('deployed ✓');
    try { sessionStorage.setItem('titoroBuilt', '1'); } catch (e) {}
    queue.length = 0; working.clear();
    ags.forEach(a => { a.tx = a.x + rnd(-800, 800); a.ty = a.y - rnd(600, 1000); a.el.style.transition = 'opacity .9s'; a.el.style.opacity = 0; });
    // un-wrapping the library changes the page height, so hold the visitor's spot instead of jumping
    const anchor = [...document.querySelectorAll('[data-b]')].find(b => b.getBoundingClientRect().bottom > 0);
    const off = anchor && anchor.getBoundingClientRect().top;
    document.documentElement.classList.remove('building');
    window.afterBuild && window.afterBuild();
    if (anchor) { const y = scrollY + anchor.getBoundingClientRect().top - off; window.lenis ? lenis.scrollTo(y, { immediate: true, force: true }) : scrollTo(0, y); }
    await sleep(1400);
    live = false; layer.remove();
    await sleep(1600);
    pill.style.transition = 'opacity .6s'; pill.style.opacity = 0;
    setTimeout(() => pill.remove(), 700);
  }
})();
