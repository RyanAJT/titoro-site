// Agent swarm build: plays on a visitor's first home-page visit, or any page with ?build.
// One frame loop drives everything: agents ease toward targets, the camera glides to the build frontier.
(() => {
  const q = new URLSearchParams(location.search);
  const home = location.pathname === '/' || location.pathname === '/index.html';
  let seen = false; try { seen = localStorage.getItem('titoroBuilt') === '1'; } catch (e) {}
  window.BUILD = !q.has('nobuild') && q.has('build') || (!q.has('nobuild') && home && !seen && !matchMedia('(prefers-reduced-motion: reduce)').matches);
  if (!window.BUILD) return;
  document.documentElement.classList.add('building');

  const ATOM = 'h1,h2,h3,h4,p,.btn,.mono,.g,.pk,.bt,.console,.phone,form,.marquee,li,.bigT,td';
  const BOX = '.g,.pk,.bt,.console,.phone,form,.marquee';
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
    let done = 0, skipped = false, live = true;

    const layer = document.createElement('div');
    layer.id = 'swarm';
    document.body.appendChild(layer);
    const pill = document.createElement('div');
    pill.id = 'pill';
    document.body.appendChild(pill);
    const setPill = s => pill.innerHTML = `<span class="dot"></span><span>${names.length} agents · ${done}/${total} layers · ${s}</span>` + (s === 'building' ? '<button>Skip</button>' : '');
    setPill('building');
    pill.addEventListener('click', e => { if (e.target.tagName === 'BUTTON') skipped = true; });

    const add = (cls, css, html = '') => { const e = document.createElement('div'); e.className = cls; e.style.cssText = css; e.innerHTML = html; layer.appendChild(e); return e; };
    const rect = el => { const r = el.getBoundingClientRect(); return { x: r.left + scrollX, y: r.top + scrollY, w: r.width, h: r.height }; };
    const reveal = el => { el.classList.remove('bx-hide'); el.classList.add('bx-in'); done++; setPill('building'); };

    // agents: smooth spring toward a target; goTo resolves inside the frame loop, not on a timer
    const ags = names.map((n, i) => {
      const c = cols[i % cols.length];
      const el = add('ag', '', arrow(c) + `<span class="tag" style="background:${c}">${n === 'Claude' ? 'Claude' : 'agent-' + String(i).padStart(2, '0') + ' · ' + n}</span><span class="act"></span>`);
      const x = innerWidth / 2 + rnd(-160, 160), y = scrollY + innerHeight / 2 + rnd(-80, 80);
      return { el, c, x, y, vx: 0, vy: 0, tx: x, ty: y, ph: rnd(0, 9), arrive: null };
    });
    const goTo = (a, x, y) => new Promise(res => { a.tx = x; a.ty = y; a.arrive = res; });

    // camera: glide toward the topmost unfinished element, never jump
    let cam = scrollY, cv = 0, goal = 0;
    const frontier = () => {
      let y = Infinity;
      working.forEach(el => { y = Math.min(y, rect(el).y); });
      if (queue[0]) y = Math.min(y, rect(queue[0]).y);
      return y;
    };
    let last = performance.now();
    (function tick(now) {
      const dt = Math.min((now - last) / 16.67, 3); last = now;
      const f = frontier();
      if (f < Infinity) {
        const max = document.documentElement.scrollHeight - innerHeight;
        goal = Math.max(goal, Math.min(max, f - innerHeight * .3)); // only ever moves down
        cv = (cv + (goal - cam) * .01 * dt) * Math.pow(.86, dt);
        cv = Math.max(-9, Math.min(9, cv));
        cam += cv * dt;
        window.lenis ? lenis.scrollTo(cam, { immediate: true, force: true }) : scrollTo(0, cam);
      }
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

    // agents pull from one shared queue; anything far below or off to the side waits for the camera
    async function agent(a, i) {
      await sleep(i * 90);
      while (!skipped && (queue.length || working.size)) {
        const el = queue[0];
        if (!el) { await goTo(a, a.x + rnd(-60, 60), a.y + rnd(-40, 40)); await sleep(rnd(150, 350)); continue; }
        const r = rect(el);
        if (r.w === 0 || r.x > innerWidth - 40) { queue.shift(); reveal(el); continue; }
        const atBottom = scrollY >= document.documentElement.scrollHeight - innerHeight - 4;
        if (r.y + Math.min(r.h, 120) > scrollY + innerHeight * .95 && !atBottom) {
          // drift down with the camera instead of standing still
          await goTo(a, rnd(innerWidth * .15, innerWidth * .85), scrollY + innerHeight * rnd(.55, .8));
          continue;
        }
        queue.shift();
        await work(a, el);
      }
    }
    await Promise.all(ags.map(agent));

    // finish
    document.querySelectorAll('.bx-hide').forEach(e => { e.classList.remove('bx-hide'); e.classList.add('bx-in'); });
    done = total; setPill('deployed ✓');
    try { localStorage.setItem('titoroBuilt', '1'); } catch (e) {}
    queue.length = 0; working.clear();
    ags.forEach(a => { a.tx = a.x + rnd(-800, 800); a.ty = a.y - rnd(600, 1000); a.el.style.transition = 'opacity .9s'; a.el.style.opacity = 0; });
    document.documentElement.classList.remove('building');
    window.afterBuild && window.afterBuild();
    window.lenis ? lenis.scrollTo(0, { duration: 1.6, force: true }) : scrollTo({ top: 0, behavior: 'smooth' });
    await sleep(1400);
    live = false; layer.remove();
    await sleep(1600);
    pill.style.transition = 'opacity .6s'; pill.style.opacity = 0;
    setTimeout(() => pill.remove(), 700);
  }
})();
