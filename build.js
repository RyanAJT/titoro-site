// Agent swarm build: plays on a visitor's first home-page visit, or any page with ?build.
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
  const cols = ['#7cc7d6', '#f6c177', '#9ed99a', '#f2a0b8', '#c4b5fd', '#8fb8ff', '#f4d35e', '#ff9e7a'];
  const names = ['Claude', 'layout', 'copy', 'motion', 'type', 'grid', 'color', 'links', 'assets', 'a11y', 'seo', 'qa'];
  const verbs = ['writing', 'aligning', 'kerning', 'placing', 'styling', 'spacing', 'linking', 'checking', 'tuning', 'snapping'];
  const arrow = c => `<svg viewBox="0 0 16 16"><path d="M1.5 1.5l12.5 6-6 1.6-2.2 5.7z" fill="${c}" stroke="#0b1113" stroke-width="1.2" stroke-linejoin="round"/></svg>`;

  addEventListener('DOMContentLoaded', run);

  async function run() {
    const blocks = [...document.querySelectorAll('[data-b]')];
    const atoms = [];
    blocks.forEach(b => {
      b._atoms = [...b.querySelectorAll(ATOM)].filter(a => !a.parentElement.closest(BOX));
      if (!b._atoms.length) b._atoms = [b];
      b._atoms.forEach(a => a.classList.add('bx-hide'));
      atoms.push(...b._atoms);
    });
    const total = atoms.length;
    let done = 0, skipped = false;

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

    // agents: spring physics toward a target, always drifting a little
    const ags = names.map((n, i) => {
      const c = cols[i % cols.length];
      const el = add('ag', '', arrow(c) + `<span class="tag" style="background:${c}">${n === 'Claude' ? 'Claude' : 'agent-' + String(i).padStart(2, '0') + ' · ' + n}</span><span class="act"></span>`);
      const a = { el, c, x: innerWidth / 2 + (Math.random() - .5) * 200, y: scrollY + innerHeight / 2, vx: 0, vy: 0, tx: 0, ty: 0, ph: Math.random() * 9 };
      a.tx = a.x; a.ty = a.y;
      return a;
    });
    let live = true;
    (function tick(t) {
      for (const a of ags) {
        const wx = Math.sin(t / 700 + a.ph) * 3, wy = Math.cos(t / 900 + a.ph) * 3;
        a.vx = (a.vx + (a.tx + wx - a.x) * .06) * .78;
        a.vy = (a.vy + (a.ty + wy - a.y) * .06) * .78;
        a.x += a.vx; a.y += a.vy;
        a.el.style.transform = `translate3d(${a.x}px,${a.y}px,0)`;
      }
      if (live) requestAnimationFrame(tick);
    })(0);
    const goTo = async (a, x, y) => { a.tx = x; a.ty = y; for (let i = 0; i < 60 && Math.hypot(a.x - x, a.y - y) > 8; i++) await sleep(16); };
    const act = (a, txt) => { a.el.classList.toggle('busy', !!txt); a.el.querySelector('.act').textContent = txt || ''; };

    // one agent builds one element: fly over, select it, work, reveal
    let active = 0;
    async function work(a, el) {
      active++;
      let r = rect(el);
      if (r.y + Math.min(r.h, 200) > scrollY + innerHeight * .85 || r.y < scrollY + 80) {
        const top = Math.max(0, r.y - innerHeight * .3);
        window.lenis ? lenis.scrollTo(top, { duration: .8 }) : scrollTo({ top, behavior: 'smooth' });
        await sleep(500); r = rect(el);
      }
      await goTo(a, r.x + Math.random() * Math.min(r.w, 260), r.y + Math.random() * Math.min(r.h, 80));
      if (skipped) { active--; return; }
      const tagName = el.matches(BOX) ? (el.className.split(' ')[0] || 'box') : el.tagName.toLowerCase();
      const sel = add('sel', `left:${r.x}px;top:${r.y}px;width:${r.w}px;height:${r.h}px;--c:${a.c}`,
        '<i style="left:-4px;top:-4px"></i><i style="right:-4px;top:-4px"></i><i style="left:-4px;bottom:-4px"></i><i style="right:-4px;bottom:-4px"></i>' +
        `<b>${tagName} · ${Math.round(r.w)}×${Math.round(r.h)}</b>`);
      act(a, verbs[(Math.random() * verbs.length) | 0] + '…');
      // drag the cursor across the element while "working"
      await goTo(a, r.x + r.w * (.4 + Math.random() * .5), r.y + r.h * (.3 + Math.random() * .6));
      await sleep(120 + Math.random() * 260);
      el.classList.remove('bx-hide'); el.classList.add('bx-in');
      done++; setPill('building');
      act(a, ''); active--;
      setTimeout(() => { sel.style.opacity = 0; setTimeout(() => sel.remove(), 300); }, 250);
    }
    // idle agents measure things so nobody stands still
    async function fidget(a, b) {
      const r = rect(b);
      const x = r.x + Math.random() * r.w, y = r.y + Math.random() * Math.min(r.h, innerHeight * .8);
      await goTo(a, x, y);
      const w = 40 + Math.random() * 160, h = 20 + Math.random() * 60;
      const g = add('sel', `left:${x}px;top:${y}px;width:${w}px;height:${h}px;--c:${a.c};border-style:dashed`, `<b>${Math.round(w)}×${Math.round(h)}</b>`);
      act(a, ['measuring', 'snapping', 'checking contrast', 'testing hover'][(Math.random() * 4) | 0]);
      await goTo(a, x + w, y + h);
      await sleep(200);
      act(a, ''); g.remove();
    }

    for (const b of blocks) {
      if (skipped) break;
      const r = rect(b);
      const top = Math.max(0, r.y - 110);
      window.lenis ? lenis.scrollTo(top, { duration: 1 }) : scrollTo({ top, behavior: 'smooth' });
      await sleep(650);
      const c = cols[blocks.indexOf(b) % cols.length];
      const g1 = add('guide h', `top:${r.y}px;--c:${c}`), g2 = add('guide h', `top:${r.y + r.h}px;--c:${c}`);
      const queue = b._atoms.filter(a => a.classList.contains('bx-hide'));
      await Promise.all(ags.map(async a => {
        while (!skipped) {
          const el = queue.shift();
          if (el) await work(a, el);
          else if (active > 0) await fidget(a, b);
          else break;
        }
      }));
      g1.remove(); g2.remove();
    }

    // finish
    document.querySelectorAll('.bx-hide').forEach(e => { e.classList.remove('bx-hide'); e.classList.add('bx-in'); });
    done = total; setPill('deployed ✓');
    try { localStorage.setItem('titoroBuilt', '1'); } catch (e) {}
    ags.forEach(a => { a.tx = a.x + (Math.random() - .5) * 1600; a.ty = a.y - 600 - Math.random() * 400; a.el.style.transition = 'opacity .9s'; a.el.style.opacity = 0; });
    document.documentElement.classList.remove('building');
    window.afterBuild && window.afterBuild();
    window.lenis ? lenis.scrollTo(0, { duration: 1.6 }) : scrollTo({ top: 0, behavior: 'smooth' });
    await sleep(1400);
    live = false; layer.remove();
    await sleep(1600);
    pill.style.transition = 'opacity .6s'; pill.style.opacity = 0;
    setTimeout(() => pill.remove(), 700);
  }
})();
