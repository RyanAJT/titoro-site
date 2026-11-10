// Smooth scroll, parallax and the small looping details.
gsap.registerPlugin(ScrollTrigger);
const lenis = new Lenis({ lerp: 0.09 });
lenis.on('scroll', ScrollTrigger.update);
gsap.ticker.add(t => lenis.raf(t * 1000));
gsap.ticker.lagSmoothing(0);
window.lenis = lenis;
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
const $ = (s, r = document) => [...r.querySelectorAll(s)];

// reveals (the swarm does its own reveal in build mode)
if (window.BUILD || reduce) $('.rv').forEach(e => e.classList.remove('rv'));
else $('.rv').forEach(e => gsap.to(e, { opacity: 1, y: 0, duration: 1, ease: 'expo.out', scrollTrigger: { trigger: e, start: 'top 88%' } }));

// parallax: anything with data-speed drifts against the scroll
$('[data-speed]').forEach(e => gsap.to(e, {
  yPercent: () => -parseFloat(e.dataset.speed) * 100, ease: 'none',
  scrollTrigger: { trigger: e.closest('section,header') || e, start: 'top bottom', end: 'bottom top', scrub: true }
}));

// marquee that speeds up with scroll velocity
$('.marquee .track').forEach(tr => {
  const loop = gsap.to(tr, { xPercent: -50, duration: 28, ease: 'none', repeat: -1 });
  ScrollTrigger.create({ onUpdate: s => { gsap.to(loop, { timeScale: 1 + Math.min(Math.abs(s.getVelocity()) / 400, 5), duration: .2, overwrite: true }); gsap.to(loop, { timeScale: 1, duration: 1.2, delay: .2 }); } });
});

// horizontal library: vertical scroll pans the cards (after the build, if one is playing)
function initH() {
  $('.hscroll').forEach(h => {
    const tr = h.querySelector('.htrack'), sec = h.closest('section');
    gsap.to(tr, { x: () => -(tr.scrollWidth - innerWidth + 64), ease: 'none',
      scrollTrigger: { trigger: sec, pin: true, start: 'top top', scrub: 1, end: () => '+=' + (tr.scrollWidth - innerWidth), invalidateOnRefresh: true } });
  });
  ScrollTrigger.refresh();
}
if (window.BUILD) window.afterBuild = initH; else initH();

// how-it-works: each step lights up and switches the phone scene
$('.step').forEach((s, i) => ScrollTrigger.create({
  trigger: s, start: 'top 60%', end: 'bottom 40%',
  onToggle: st => { if (!st.isActive) return; $('.step').forEach(x => x.classList.toggle('on', x === s)); $('.scene').forEach((x, k) => x.classList.toggle('on', k === i)); }
}));

// hero console: agents report what they're doing, on a loop
const jobs = [
  ['#a9e1ec', 'scout', 'Picking 4 reels worth copying this week'],
  ['#f6c177', 'scripts', 'Writing the hook for PYRAMID'],
  ['#9ed99a', 'voice', 'Recording the voiceover'],
  ['#f2a0b8', 'film', 'Rendering 1080x1920, 30fps'],
  ['#c4b5fd', 'post', 'Scheduling IG, TikTok, YouTube'],
  ['#a9e1ec', 'dms', 'Sending the guide to 12 commenters'],
  ['#f6c177', 'guides', 'Updating the CLEAR playbook'],
];
const ul = document.querySelector('.console ul');
if (ul) {
  let k = 0;
  const row = ([c, n, t], live) => `<li class="${live ? 'live' : ''}"><b style="background:${c}">${n}</b><span>${t}</span><em>${live ? 'working' : 'done'}</em></li>`;
  const draw = () => { const r = []; for (let i = 0; i < 5; i++) r.push(row(jobs[(k + i) % jobs.length], i === 4)); ul.innerHTML = r.join(''); };
  draw(); setInterval(() => { k++; gsap.to(ul, { opacity: .55, duration: .15, yoyo: true, repeat: 1, onRepeat: draw }); }, 2200);
}

// phone comment typing
$('.typed').forEach(t => { const w = t.dataset.text; let i = 0; setInterval(() => { i = (i + 1) % (w.length + 8); t.textContent = w.slice(0, Math.min(i, w.length)); }, 160); });

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
  const blobs = [['169,225,236', .55, .2, .3], ['246,193,119', .3, .75, .55], ['29,111,127', .18, .3, .85]];
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
      if (d < 170) { x.strokeStyle = `rgba(21,25,27,${(1 - d / 170) * .16})`; x.beginPath(); x.moveTo(a.x, a.sy); x.lineTo(b.x, b.sy); x.stroke(); }
    }
    x.fillStyle = 'rgba(29,111,127,.5)';
    nodes.forEach((n, i) => { x.beginPath(); x.arc(n.x, n.sy, i % 7 ? 1.6 : 3, 0, 7); x.fill(); });
    if (!reduce && !document.hidden) requestAnimationFrame(draw);
  }
  requestAnimationFrame(draw);
  document.addEventListener('visibilitychange', () => { if (!document.hidden && !reduce) requestAnimationFrame(draw); });
})();
