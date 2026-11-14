// Smooth scroll, parallax, reels, search and the small details.
gsap.registerPlugin(ScrollTrigger);
const lenis = new Lenis({ lerp: 0.09 });
lenis.on('scroll', ScrollTrigger.update);
gsap.ticker.add(t => lenis.raf(t * 1000));
gsap.ticker.lagSmoothing(0);
window.lenis = lenis;
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
const desk = matchMedia('(min-width:861px)').matches;
const $ = (s, r = document) => [...r.querySelectorAll(s)];

// staggered reveals (the swarm does its own reveal in build mode)
if (!window.BUILD && !reduce) {
  const ro = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { const t = e.target; t.classList.add('in'); ro.unobserve(t); setTimeout(() => t.style.transitionDelay = '', 1300); } }), { rootMargin: '0px 0px -8% 0px' });
  $('.start,.tile,.feat,.g,.three>div,.pk,.sbox,.pain,.eng,.vsr,.orca,.faq details,.stg,.tier,.how3>div,.pains2 li,.mk,.builder').forEach((e, i) => { e.classList.add('rv'); e.style.transitionDelay = (i % 4) * 70 + 'ms'; ro.observe(e); });
}

// parallax: anything with data-speed drifts against the scroll
$('[data-speed]').forEach(e => gsap.to(e, {
  yPercent: () => -parseFloat(e.dataset.speed) * 100, ease: 'none',
  scrollTrigger: { trigger: e.closest('section,header') || e, start: 'top bottom', end: 'bottom top', scrub: true }
}));


// reels: load and play only while on screen
const io = new IntersectionObserver(es => es.forEach(({ target: v, isIntersecting: on }) => {
  if (on) { if (!v.src) v.src = v.dataset.src; v.play().catch(() => {}); } else v.pause();
}), { rootMargin: '200px' });
$('video[data-src]').forEach(v => io.observe(v));

// "Commented a keyword?" box: straight to the playbook
$('form.find').forEach(f => f.addEventListener('submit', e => {
  e.preventDefault();
  const v = f.querySelector('input').value.trim().toUpperCase(), kws = f.dataset.kw.split(',');
  if (kws.includes(v)) location.href = `/free/${v.toLowerCase()}/`;
  else if (v) location.href = `/free/?q=${encodeURIComponent(v)}`;
  else { f.classList.remove('miss'); void f.offsetWidth; f.classList.add('miss'); }
}));

// free page: search + category chips filter both the orbit and the grid
const fs = document.querySelector('.fsearch');
if (fs) {
  let cat = 'all';
  const apply = () => {
    const q = fs.value.trim().toUpperCase();
    $('.oc,.g[data-kw]').forEach(c => {
      const ok = (!q || c.dataset.kw.startsWith(q)) && (cat === 'all' || c.dataset.cat === cat);
      c.classList.toggle(c.classList.contains('oc') ? 'dim' : 'hide', !ok);
      c.classList.toggle('hit', ok && !!q);
    });
  };
  fs.value = new URLSearchParams(location.search).get('q') || '';
  fs.addEventListener('input', apply);
  fs.addEventListener('keydown', e => { const m = $('.g[data-kw]:not(.hide)'); if (e.key === 'Enter' && m.length === 1) location.href = m[0].href; });
  $('.chipf').forEach(b => b.addEventListener('click', () => { cat = b.dataset.cat; $('.chipf').forEach(x => x.classList.toggle('on', x === b)); apply(); }));
  apply();
}

// free page orbit: two rings turning opposite ways around the logo, tilting with the mouse
const orb = document.querySelector('.orbit');
if (orb && desk && !reduce) {
  const cards = $('.oc', orb), rings = [[], []];
  cards.forEach(c => rings[c.dataset.ring].push(c));
  let mx = 0, my = 0, tx = 0, ty = 0, t = 0, hover = false, last = performance.now();
  orb.addEventListener('pointermove', e => { const r = orb.getBoundingClientRect(); tx = (e.clientX - r.left) / r.width - .5; ty = (e.clientY - r.top) / r.height - .5; });
  cards.forEach(c => { c.onmouseenter = () => hover = true; c.onmouseleave = () => hover = false; });
  (function spin(now) {
    t += hover ? 0 : (now - last) / 1000; last = now;
    mx += (tx - mx) * .06; my += (ty - my) * .06;
    const W = orb.clientWidth, H = orb.clientHeight;
    rings.forEach((ring, k) => ring.forEach((c, i) => {
      const a = i / ring.length * Math.PI * 2 + (k ? -1 : 1) * t * .07 + k * .4;
      const rx = W * (k ? .42 : .26), ry = H * (k ? .41 : .27), d = (Math.sin(a) + 1) / 2;
      const x = W / 2 + Math.cos(a) * rx - 88 + mx * (k ? 60 : 30), y = H / 2 + Math.sin(a) * ry - 50 + my * (k ? 40 : 20);
      c.style.transform = `translate3d(${x}px,${y}px,0) scale(${.8 + d * .25}) rotateY(${mx * 14}deg) rotateX(${-my * 10}deg)`;
      c.style.zIndex = Math.round(d * 40) + (d > .5 ? 20 : 0);
      if (!c.classList.contains('dim')) c.style.opacity = .55 + d * .45; else c.style.opacity = '';
    }));
    requestAnimationFrame(spin);
  })(last);
}

// how it works: highlight the stage on screen in the side list
const snav = $('.snav li');
if (snav.length) { const so = new IntersectionObserver(es => es.forEach(e => e.isIntersecting && snav.forEach(l => l.classList.toggle('on', l.dataset.i === e.target.dataset.i))), { rootMargin: '-45% 0px -45% 0px' }); $('.stg').forEach(s => so.observe(s)); snav[0].classList.add('on'); }

// motion kit: count-up when on screen
$('.num[data-to]').forEach(n => new IntersectionObserver(([e], o) => {
  if (!e.isIntersecting) return; o.disconnect();
  const to = +n.dataset.to, t0 = performance.now();
  (function tick(t) { const p = Math.min(1, (t - t0) / 1600); n.textContent = Math.round(to * (1 - Math.pow(1 - p, 3))); if (p < 1) requestAnimationFrame(tick); })(t0);
}).observe(n));

// reel carousel: arrows + "1 / N" counter
const rt = document.querySelector('.rctrack');
if (rt) {
  const step = () => rt.querySelector('.rc').offsetWidth + 18, cnt = document.querySelector('.rcc'), n = rt.children.length;
  $('.rcb').forEach(b => b.onclick = () => rt.scrollBy({ left: b.dataset.d * step(), behavior: 'smooth' }));
  rt.addEventListener('scroll', () => cnt.textContent = `${Math.min(n, Math.round(rt.scrollLeft / step()) + 1)} / ${n}`);
}

// copy buttons
$('.copy').forEach(b => b.addEventListener('click', () => {
  navigator.clipboard.writeText(b.dataset.copy || b.parentNode.querySelector('pre,p').textContent);
  const o = b.textContent; b.textContent = 'Copied ✓'; b.classList.add('ok');
  setTimeout(() => { b.textContent = o; b.classList.remove('ok'); }, 1500);
}));

// email forms: no backend yet, so be honest about it
$('form.mail').forEach(f => f.addEventListener('submit', e => {
  e.preventDefault();
  const v = f.querySelector('input').value;
  f.innerHTML = /.+@.+\..+/.test(v) ? '<p class="lead">Thanks. Sign-ups open this week. Follow @titoro.ai for now so you don\'t miss it.</p>' : f.innerHTML;
}));

// replay button
$('[data-replay]').forEach(b => b.addEventListener('click', () => { location.href = location.pathname + '?build'; }));

// ambient background: drifting colour fields + a slow agent network, behind everything
(() => {
  const c = document.createElement('canvas'), x = c.getContext('2d');
  c.id = 'amb'; document.body.prepend(c);
  const dpr = Math.min(devicePixelRatio || 1, 1.5);
  let W, H, mx = -999, my = -999;
  const size = () => { W = innerWidth; H = innerHeight; c.width = W * dpr; c.height = H * dpr; x.setTransform(dpr, 0, 0, dpr, 0, 0); };
  size(); addEventListener('resize', size);
  addEventListener('pointermove', e => { mx = e.clientX; my = e.clientY; });
  const blobs = [['169,225,236', .16, .2, .3], ['29,111,127', .3, .75, .55], ['246,193,119', .06, .3, .85]];
  const N = innerWidth < 700 ? 18 : 34;
  const nodes = Array.from({ length: N }, () => ({ x: Math.random() * innerWidth, y: Math.random() * innerHeight, vx: (Math.random() - .5) * .25, vy: (Math.random() - .5) * .25 }));
  let sy = 0;
  function draw(t) {
    sy += ((window.lenis ? lenis.scroll : scrollY) - sy) * .08;
    x.clearRect(0, 0, W, H);
    blobs.forEach(([rgb, a, bx, by], i) => {
      const px = W * (bx + Math.sin(t / 9000 + i * 2) * .12), py = H * (by + Math.cos(t / 11000 + i) * .1 + Math.sin(sy / 1400 + i * 1.7) * .18);
      const r = Math.max(W, H) * .55, g = x.createRadialGradient(px, py, 0, px, py, r);
      g.addColorStop(0, `rgba(${rgb},${a * .55})`); g.addColorStop(1, `rgba(${rgb},0)`);
      x.fillStyle = g; x.fillRect(0, 0, W, H);
    });
    const off = (sy * .15) % H;
    for (const n of nodes) {
      n.x += n.vx; n.y += n.vy;
      const dx = n.x - mx, dy = (((n.y - off) % H) + H) % H - my, d = Math.hypot(dx, dy);
      if (d < 120) { n.x += dx / d * .8; n.y += dy / d * .8; }
      if (n.x < -20) n.x = W + 20; if (n.x > W + 20) n.x = -20;
      if (n.y < -20) n.y = H + 20; if (n.y > H + 20) n.y = -20;
    }
    nodes.forEach(n => n.sy = (((n.y - off) % H) + H) % H);
    x.lineWidth = 1;
    for (let i = 0; i < N; i++) for (let j = i + 1; j < N; j++) {
      const a = nodes[i], b = nodes[j], d = Math.hypot(a.x - b.x, a.sy - b.sy);
      if (d < 170) { x.strokeStyle = `rgba(169,225,236,${(1 - d / 170) * .12})`; x.beginPath(); x.moveTo(a.x, a.sy); x.lineTo(b.x, b.sy); x.stroke(); }
    }
    x.fillStyle = 'rgba(169,225,236,.35)';
    nodes.forEach((n, i) => { x.beginPath(); x.arc(n.x, n.sy, i % 7 ? 1.6 : 3, 0, 7); x.fill(); });
    if (!reduce && !document.hidden) requestAnimationFrame(draw);
  }
  requestAnimationFrame(draw);
  document.addEventListener('visibilitychange', () => { if (!document.hidden && !reduce) requestAnimationFrame(draw); });
})();
