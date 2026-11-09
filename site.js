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
