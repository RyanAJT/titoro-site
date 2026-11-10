# Builds every page of titoro.xyz. Run: python3 gen.py
import os

LOGO = '<svg viewBox="0 0 120 120"><g fill="currentColor"><path d="M12 50A32 32 0 0 1 44 18H59V50Z"/><path d="M61 18H108V50H92A32 32 0 0 0 61 18Z"/><path d="M44 58H76V106H60A16 16 0 0 1 44 90Z"/><circle cx="94" cy="98" r="9"/></g></svg>'
ARROW = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 8h10M9 4l4 4-4 4"/></svg>'
FOLLOW = '<a href="https://www.instagram.com/titoro.ai">Instagram</a><a href="https://www.tiktok.com/@titoro.ai">TikTok</a><a href="https://www.youtube.com/@TitoroAI">YouTube</a>'

GUIDES = [
    ('PYRAMID', 'The 4-line prompt that beats 300-word prompts', '1Ef6QVbcd9yatMF_L4QlqW9CkMAPY-QMJZa483AOyd68'),
    ('PROJECT', 'Make Claude remember your business, every chat', '1fuW3_CexjyF42ZBLJTiBQeVFnOzJBLG_ssgaLPe7Ess'),
    ('CLEAR', 'Turn messy SOPs into one-action-per-step steps', '194k4NZoPvErjl1bbSCPuCfDJNiRU0LmYSSW9XoZ0XK0'),
    ('ASK', "Find 10 video ideas in someone else's comments", '1eRWCl4XQu_QbrN7VNoJBdYyM5JNXV7dBpS6UhDkUEYU'),
    ('FLOP', 'Ask Claude why your reels flopped', '1rL3jQfQ5uYmiHyzRJet0zYNUlmZJyRoCR7ejE20JD_8'),
    ('SETUP', '5 Claude settings most people skip', '1Ko7Cnvcm3W9cbLWmEAf9tMKcU7l6NTrwKnHvk_opPhM'),
    ('TELLS', '8 signs AI made your website, and the fix', '1ie4LhuN9KSDW1VlDtwNfLh7zzcwp9s9KGUuuzFFM1-I'),
    ('ANIMATE', '10 animations you can make with Claude', '14HjSeDhqpLTv6KUW1SCVtcequyP9VpTxrb0TzAEtSPw'),
    ('PRICE', 'Track competitor prices automatically', '1Fawi7-r5kSOz3kIQJuQ3DSdKNBxY5G38SlMxD6xOhHs'),
    ('TRAIN', 'Turn a staff handbook into a training game', '11qCIFBkS-aRZOr_TPkLXHdxWsmcaidNcIte8FK-50oY'),
    ('HUMAN', "Make Claude's writing sound like a person", '1t_tbTvN4Q7QZ5YC_9DAZTF3z0RP5IjRr6TFdey7gOVA'),
    ('COPY', '5 prompts that make captions sell', '1Ng5MPJZx4gVDac2WVVBs74DVkFhztwN51bjoMzzz5RQ'),
    ('LOGO', '6 real logo ideas, with the reasoning', '1A8Zj2r0KPvhaoYEfxDWq21Y_7AZspCrU1KjTwVAfOdQ'),
    ('PDF', 'Drag a PDF into Claude, get answers', '1SoEhEAl149MN39YKei-Y-PjFO9PXdHYwAlhL9NieHPU'),
    ('INVOICE', 'Make invoices with Claude', '1wt6CL9ud7qbnwoxtHVh5ErSargrx1904fZ1Toc8-QrI'),
    ('PRIVACY', 'Keep your data private in Claude', '1Z3BaWTaVaISgxJpHBtdvW3v7wyatJ9tCqYuMoKby1L4'),
]
PACKS = [
    ('Content Engine', '$19', 'Everything I use to make a reel a day.', ['Captions in your own voice', 'Hook writer: 10 hooks, under 8 words', 'Reel scripts in the Titoro format', 'Comment-to-DM guide writer', '"Why did this flop?" reviewer']),
    ('Business Ops', '$15', 'The boring admin, handled.', ['SOP rewriter', 'Quote and invoice drafter', 'Staff training game builder', 'Customer-comment miner']),
    ('Animation', '$9', 'The 10 looks from the ANIMATE reel.', ['10 ready prompts', 'The reel layout']),
    ('Everything Bundle', '$29', 'All three packs, plus every update.', []),
]
TOOLS = [
    ('Claude', 'The brain', 'Where every script, guide and skill starts.', 'https://claude.ai', False),
    ('ManyChat', 'DMs', 'Sends the guide when you comment a keyword.', '/go/manychat/', True),
    ('Buffer', 'Posting', 'Schedules every reel to IG, TikTok and YouTube.', '/go/buffer/', True),
    ('ElevenLabs', 'Voice and sound', 'Every voiceover, music bed and sound effect.', '/go/elevenlabs/', True),
    ('Higgsfield', 'Video and images', 'AI video, image and audio models, right inside Claude.', '/go/higgsfield/', True),
    ('Apify', 'Research', 'Pulls reel data for my weekly scouting.', '/go/apify/', True),
]
MAIL = '''<form class="mail" novalidate><label for="em{n}">Your email</label><div class="row"><input id="em{n}" type="email" placeholder="you@yourbusiness.com" required><button class="btn">{cta}</button></div><small>{help}</small></form>'''


def page(path, title, desc, body, on=''):
    nav = ''.join(f'<a class="l{" on" if on == k else ""}" href="/{k}/">{v}</a>' for k, v in [('free', 'Free playbooks'), ('packs', 'Skill Packs'), ('tools', 'My stack')])
    html = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<link rel="icon" href="/favicon.svg"><link rel="stylesheet" href="/style.css">
<script src="/build.js"></script></head>
<body>
<nav class="top"><a class="logo" href="/">{LOGO}titoro</a>{nav}<a class="cta" href="/free/">Get the free stuff</a></nav>
{body}
<div class="wrap"><footer data-b="footer">
<div><b style="color:var(--ink)">titoro</b><br>Claude tutorials, free playbooks and ready-made skills, for people who run a business or a page.<br><br><span class="small">Not affiliated with Anthropic. Claude is a trademark of Anthropic, PBC. Some links are affiliate links.</span></div>
<div class="fl"><span class="mono">Site</span><a href="/free/">Free playbooks</a><a href="/packs/">Skill Packs</a><a href="/tools/">My stack</a><a href="/disclosure/">Disclosure</a></div>
<div class="fl"><span class="mono">Follow</span>{FOLLOW}<span>created by orca.agentics</span></div>
<div class="big">titoro.</div>
</footer></div>
<script src="/vendor/gsap.min.js"></script><script src="/vendor/ScrollTrigger.min.js"></script><script src="/vendor/lenis.min.js"></script><script src="/site.js"></script>
</body></html>
'''
    os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
    open(path, 'w').write(html)


def gcard(k, t, d, dark=False):
    return f'<a class="g{" dark" if dark else ""}" href="https://docs.google.com/document/d/{d}/view"><span class="mono">Comment {k}</span><div class="kw">{k}</div><p>{t}</p></a>'


# ---------- home ----------
kw = ''.join(f'<span>{k}</span>' for k, _, _ in GUIDES[:10])
lib = ''.join(gcard(k, t, d, i % 3 == 1) for i, (k, t, d) in enumerate(GUIDES[:8]))
main_pack = PACKS[0]
side = ''.join(f'<div class="pk rv"><span class="mono">Pack</span><h3>{n}</h3><p>{d}</p><div class="price">{p}</div></div>' for n, p, d, _ in PACKS[1:3])
bento = f'''
<a class="bt w4 rv" href="https://claude.ai"><span class="mono">The brain</span><div class="sched" style="margin-top:18px"><span>scripts.md<em>writing</em></span><span>guides/PYRAMID<em>done</em></span><span class="go">skill: captions-in-my-voice<em>live</em></span></div><h4>Claude</h4><p>Where every script, guide and skill starts.</p></a>
<a class="bt w2 rv" href="/go/manychat/"><span class="mono aff">affiliate</span><span class="mono">DMs</span><div class="dm me" style="margin-top:18px;max-width:none">PYRAMID</div><div class="dm" style="color:var(--ink);background:var(--paper2);max-width:none">Here's your guide</div><h4>ManyChat</h4></a>
<a class="bt w2 rv" href="/go/elevenlabs/"><span class="mono aff">affiliate</span><span class="mono">Voice</span><div class="wave" style="margin-top:20px">{''.join(f'<i style="animation-delay:-{i*.13:.2f}s"></i>' for i in range(22))}</div><h4>ElevenLabs</h4></a>
<a class="bt w2 rv" href="/go/buffer/"><span class="mono aff">affiliate</span><span class="mono">Posting</span><div class="sched" style="margin-top:18px"><span>IG<em>6:47pm</em></span><span class="go">TikTok<em>9:41pm</em></span></div><h4>Buffer</h4></a>
<a class="bt w2 rv" href="/go/higgsfield/"><span class="mono aff">affiliate</span><span class="mono">Video</span><div class="frames"><i></i><i></i><i></i><i></i></div><h4>Higgsfield</h4><p>AI video and images.</p></a>'''

home = f'''
<header class="wrap hero" data-b="hero">
  <svg class="bigT" data-speed="-.25" viewBox="0 0 120 120"><g fill="currentColor"><path d="M12 50A32 32 0 0 1 44 18H59V50Z"/><path d="M61 18H108V50H92A32 32 0 0 0 61 18Z"/><path d="M44 58H76V106H60A16 16 0 0 1 44 90Z"/><circle cx="94" cy="98" r="9"/></g></svg>
  <div>
    <p class="mono eyebrow"><b>titoro.xyz</b> Claude, but actually useful</p>
    <h1>I let AI agents run my page. <span class="serif">Steal</span> the <span class="hl">playbooks</span>.</h1>
    <p class="sub">Every reel I post becomes a free guide. The ones I use daily become Skill Packs you install once. Built for people who run a business or a page.</p>
    <div class="ctas"><a class="btn" href="/free/">Get the free playbooks {ARROW}</a><button class="btn alt" data-replay>Watch the agents build this</button></div>
    <p class="mono note">16 free playbooks · new ones every week</p>
  </div>
  <div class="console" data-speed=".12">
    <div class="bar"><i></i><i></i><i></i><span class="mono">titoro HQ · agents</span></div>
    <ul></ul>
    <div class="chip"><span class="dot"></span>Today's reel goes out at 6:47pm</div>
  </div>
</header>

<div class="marquee" data-b="keywords"><div class="track"><span class="serif">Comment</span>{kw}<span class="serif">Comment</span>{kw}</div></div>

<section class="blk wrap" data-b="how">
  <p class="mono eyebrow"><b>01</b> How it works</p>
  <h2>From a 40-second reel to a tool you <span class="serif">keep</span>.</h2>
  <div class="how">
    <div class="steps">
      <div class="step on"><span class="n">STEP 1</span><h3>Watch a reel.</h3><p>One idea, one result, under a minute. Real screens, nothing staged.</p></div>
      <div class="step"><span class="n">STEP 2</span><h3>Comment the keyword.</h3><p>Every reel ends with a word, like PYRAMID or CLEAR. Comment it.</p></div>
      <div class="step"><span class="n">STEP 3</span><h3>Get the playbook in your DMs.</h3><p>The full step-by-step guide lands in seconds. Free, always.</p></div>
      <div class="step"><span class="n">STEP 4</span><h3>Want it done for you? Install the pack.</h3><p>Skill Packs turn the playbooks into skills Claude runs for you, every day.</p></div>
    </div>
    <div class="phoneWrap"><div class="phone"><div class="screen">
      <div class="scene reel on"><span class="mono">@titoro.ai</span><div class="bars"><i style="height:40%"></i><i style="height:65%;animation-delay:-.4s"></i><i style="height:85%;animation-delay:-.8s"></i><i style="height:100%;animation-delay:-1.2s"></i></div><div class="rt">Stop writing 300-word prompts.</div></div>
      <div class="scene"><span class="mono" style="color:#8a979b">Comments</span><div class="cmt"><b>@yourbusiness</b><span class="typed" data-text="PYRAMID"></span></div></div>
      <div class="scene"><span class="mono" style="color:#8a979b">titoro.ai</span><div class="dm">Thanks for your comment! Drop a follow so the guide reaches you.</div><div class="dm me">Followed</div><div class="dm">Here's your guide<span class="open">Open the playbook</span></div></div>
      <div class="scene pack"><span class="mono">Skill Pack installed</span><h3 style="margin:14px 0 6px;letter-spacing:-.02em">Content Engine</h3><div class="file"><i></i>captions-in-my-voice</div><div class="file"><i></i>hook-writer</div><div class="file"><i></i>reel-script</div><div class="file"><i></i>flop-reviewer</div><p style="margin-top:auto;font-size:14px;color:var(--ink2)">Claude now writes like you, every time.</p></div>
    </div></div></div>
  </div>
</section>

<section class="libsec" data-b="library">
  <div class="wrap"><p class="mono eyebrow"><b>02</b> Free playbooks</p><h2>Every guide from the reels. <span class="serif">Free</span>.</h2><p class="lead">No sign-up wall. Pick one, open it, use it today.</p></div>
  <div class="hscroll"><div class="htrack">{lib}<a class="g dark" href="/free/"><span class="mono">And 8 more</span><div class="kw">See all</div><p>Browse the full library</p></a></div></div>
</section>

<section class="blk wrap" data-b="packs">
  <p class="mono eyebrow"><b>03</b> Skill Packs</p>
  <h2>Guides teach you how. Packs just <span class="serif">do it</span>.</h2>
  <p class="lead">Each pack is a set of skills I use myself, tested, with a two-minute setup video. Launching one at a time.</p>
  <div class="packs">
    <div class="pk main rv" data-speed=".05"><span class="mono">Most useful</span><h3 style="font-size:44px">{main_pack[0]}</h3><p>{main_pack[2]}</p><ul>{''.join(f'<li>{x}</li>' for x in main_pack[3])}</ul>
      <div class="bottom"><div class="price">{main_pack[1]}</div><a class="btn" style="background:var(--mist);color:var(--ink)" href="/packs/">Join the waitlist {ARROW}</a></div></div>
    {side}
  </div>
</section>

<section class="blk wrap" data-b="stack">
  <p class="mono eyebrow"><b>04</b> My stack</p>
  <h2>The exact tools behind <span class="serif">every</span> reel.</h2>
  <p class="lead">Some links are affiliate links. I only list what I actually use.</p>
  <div class="bento">{bento}</div>
  <p style="margin-top:24px"><a class="btn alt" href="/tools/">See the full stack {ARROW}</a></p>
</section>

<section class="wrap" data-b="replay" style="padding-bottom:140px">
  <div class="replay"><div><p class="mono" style="color:var(--mist)">Behind the scenes</p><h2 style="margin-top:16px">This site was built by <span class="serif">12 agents</span>.</h2><p class="lead">Watch them do it again, one element at a time.</p></div>
  <div><button class="btn" data-replay>Replay the build {ARROW}</button>{MAIL.format(n=1, cta='Weekly tips', help='One useful AI trick a week. No spam.').replace('class="mail"', 'class="mail" style="color:var(--paper)"')}</div></div>
</section>
'''
page('index.html', 'titoro · I let AI agents run my page. Steal the playbooks.', 'Free Claude playbooks from every reel, ready-made Skill Packs, and the exact AI stack behind @titoro.ai.', home)

# ---------- free ----------
cards = ''.join(gcard(k, t, d, i % 5 == 2) for i, (k, t, d) in enumerate(GUIDES))
page('free/index.html', 'Free playbooks · titoro', 'Every guide from the @titoro.ai reels, free.', f'''
<header class="wrap phead" data-b="header"><p class="mono eyebrow"><b>Free</b> {len(GUIDES)} playbooks</p><h1>Free <span class="serif">playbooks</span>.</h1><p class="lead">Everything I send in DMs, in one place. Each card shows the keyword from its reel.</p></header>
<section class="wrap" data-b="library"><div class="grid2">{cards}</div></section>
<section class="wrap" data-b="nudge" style="padding-bottom:120px"><div class="replay"><div><h2>Want the ready-made version?</h2><p class="lead">Skill Packs turn these playbooks into skills Claude runs for you.</p></div><div><a class="btn" href="/packs/">See the packs {ARROW}</a></div></div></section>
''', 'free')

# ---------- packs ----------
pcs = ''
for i, (n, p, d, items) in enumerate(PACKS):
    cls = 'pk main' if i == 0 else 'pk'
    pcs += f'<div class="{cls}"><span class="mono soon">Coming soon</span><h3>{n}</h3><p>{d}</p>' + (f'<ul>{"".join(f"<li>{x}</li>" for x in items)}</ul>' if items else '') + f'<div class="price">{p}</div></div>'
page('packs/index.html', 'Skill Packs · titoro', 'Ready-made Claude skills, tested, with a short setup video.', f'''
<header class="wrap phead" data-b="header"><p class="mono eyebrow"><b>Packs</b> works with Claude</p><h1>Skill <span class="serif">Packs</span>.</h1><p class="lead">Guides teach you how. Packs just do it. Every skill is one I use myself, tested before it goes on sale.</p></header>
<section class="wrap" data-b="packs"><div class="packs" style="margin-top:20px">{pcs}</div></section>
<section class="wrap blk" data-b="waitlist"><h2>Get first access.</h2><p class="lead">Packs launch one at a time. Join the list and you hear first.</p>{MAIL.format(n=2, cta='Join the waitlist', help='One email when a pack launches. Nothing else.')}</section>
<section class="wrap" data-b="faq" style="padding-bottom:120px"><div class="prose" style="margin:0">
<p><b>Do I need to code?</b><br>No. You upload the files in Claude's settings once.</p>
<p><b>Which Claude plan?</b><br>Skills run on paid Claude plans and in Claude Code. Each pack says exactly what it needs.</p>
<p><b>Is this official?</b><br>No. These are my own skills, not affiliated with or endorsed by Anthropic.</p>
<p><b>Refunds?</b><br>If a pack doesn't work for you within 14 days, email me and I'll refund you.</p></div></section>
''', 'packs')

# ---------- tools ----------
rows = ''.join(f'<tr><td class="mono">{g}</td><td><b>{n}</b></td><td class="d">{d}</td><td style="text-align:right"><a class="btn alt" href="{u}">Open{" · affiliate" if a else ""}</a></td></tr>' for n, g, d, u, a in TOOLS)
page('tools/index.html', 'My stack · titoro', 'The exact AI tools behind the @titoro.ai reels.', f'''
<header class="wrap phead" data-b="header"><p class="mono eyebrow"><b>Stack</b> {len(TOOLS)} tools</p><h1>My <span class="serif">stack</span>.</h1><p class="lead">The exact tools behind every reel and automation. Some links are affiliate links: if you sign up, I may earn a small commission at no extra cost to you. I only list what I actually use.</p></header>
<section class="wrap" data-b="stack"><table class="tools">{rows}</table></section>
''', 'tools')

# ---------- disclosure ----------
page('disclosure/index.html', 'Disclosure · titoro', 'Affiliate disclosure, refunds and privacy.', '''
<header class="wrap phead" data-b="header"><h1>The small <span class="serif">print</span>.</h1></header>
<section class="wrap" data-b="text"><div class="prose">
<p><b>Affiliate links.</b> Some links on this site and in my posts and DMs earn me a commission at no cost to you. They are marked "affiliate".</p>
<p><b>Not affiliated with Anthropic.</b> Claude is a trademark of Anthropic, PBC. Skill Packs are my own work.</p>
<p><b>Refunds.</b> If a pack doesn't work for you within 14 days, email me and I'll refund you.</p>
<p><b>Privacy.</b> Your email is only used for what you signed up for. Unsubscribe any time.</p>
<p><b>Results.</b> Examples in my videos show what worked for me, not a promise.</p></div></section>
''')


# ---------- fable (launch guide) ----------
REF = 'https://higgsfield.ai?fpr=jing-45bb72'
MCP = 'https://higgsfield.ai/mcp?fpr=jing-45bb72'
PROMPTS = [
    ('Cinematic trailer', 'Make me a 10-second cinematic trailer shot: a lone rider crossing a salt flat at golden hour, low drone angle, dust trailing behind. Vertical 9:16. Use Higgsfield.'),
    ('Anime scene', 'Create an anime-style scene: a girl running through red torii gates at night, lanterns glowing, petals in the wind. 9:16, 8 seconds.'),
    ('Product ad', 'Turn this product photo into a 6-second ad: slow orbit around the product on a marble table, soft morning light, then a clean end card.'),
    ('Talking explainer', 'Write a 20-second script about my business, then generate a voiceover and a matching video with captions.'),
    ('3D from video', 'Here is a 360 video of an object. Build a 3D model of it and render a turntable shot.'),
]
steps = f'''
<div class="fstep"><span class="mono">Step 1 · 1 minute</span><h3>Create your Higgsfield account</h3><p>Sign up free with this link. It's the account the trial attaches to.</p><a class="btn" href="{REF}" target="_blank" rel="noopener">Sign up on Higgsfield {ARROW}</a><small class="mono">affiliate link · I may earn a commission at no cost to you</small></div>
<div class="fstep"><span class="mono">Step 2 · 30 seconds</span><h3>Start the free 3-day trial</h3><p>On the Higgsfield MCP page, start the 72-hour trial. It's $0 today and unlocks unlimited use of the top video, image and audio models inside Claude.</p><a class="btn alt" href="{MCP}" target="_blank" rel="noopener">Open higgsfield.ai/mcp {ARROW}</a><div class="warn"><b>Read this first.</b> A card is needed to start. After 72 hours the trial renews into Higgsfield Ultra (40% off the first month) unless you cancel. Set a reminder for day 3 if you only want the free part. Offer for new users, limited time, Higgsfield's terms apply.</div></div>
<div class="fstep"><span class="mono">Step 3 · 1 minute</span><h3>Connect it to Claude</h3><ol><li>Open Claude, go to <b>Settings → Connectors</b>.</li><li>Click <b>Add custom connector</b>, name it <b>Higgsfield</b>.</li><li>Paste this URL: <code>https://mcp.higgsfield.ai/mcp</code> <button class="copy" data-copy="https://mcp.higgsfield.ai/mcp">Copy</button></li><li>Click <b>Connect</b> and sign in to Higgsfield.</li></ol></div>
<div class="fstep"><span class="mono">Step 4</span><h3>Pick Fable 5.2 and ask for anything</h3><p>Choose Claude Fable 5.2 in the model menu (paid Claude plans), start a new chat and paste one of these:</p>
''' + ''.join(f'<div class="prompt"><span class="mono">{t}</span><p>{p}</p><button class="copy" data-copy="{p}">Copy prompt</button></div>' for t, p in PROMPTS) + '</div>'
page('fable/index.html', 'Fable 5.2 + Higgsfield: free 3-day setup · titoro', 'Connect Higgsfield to Claude Fable 5.2 and make AI videos free for 3 days. Step-by-step setup.', f'''
<header class="wrap phead" data-b="header"><p class="mono eyebrow"><b>New</b> Claude Fable 5.2 × Higgsfield</p><h1>Every video model, inside Claude. <span class="serif">Free</span> for 3 days.</h1><p class="lead">Anthropic just released Claude Fable 5.2, and Higgsfield opened a free 72-hour trial of its connector for new users. Here's the full setup. It takes about 3 minutes.</p></header>
<section class="wrap fsteps" data-b="steps">{steps}</section>
<section class="wrap" data-b="more" style="padding:80px 0 120px"><div class="replay"><div><h2>Want more like this?</h2><p class="lead">Every reel I post becomes a free playbook.</p></div><div><a class="btn" href="/free/">See the free playbooks {ARROW}</a></div></div></section>
<script>document.querySelectorAll('.copy').forEach(b=>b.onclick=()=>{{navigator.clipboard.writeText(b.dataset.copy);b.textContent='Copied';setTimeout(()=>b.textContent=b.dataset.copy.startsWith('http')?'Copy':'Copy prompt',1500)}})</script>
''')

# ---------- short links ----------
for k, u in {'manychat': 'https://manychat.com', 'buffer': 'https://buffer.com', 'elevenlabs': 'https://elevenlabs.io', 'higgsfield': 'https://higgsfield.ai?fpr=jing-45bb72', 'apify': 'https://apify.com'}.items():
    os.makedirs(f'go/{k}', exist_ok=True)
    open(f'go/{k}/index.html', 'w').write(f'<!DOCTYPE html><meta charset="utf-8"><title>Redirecting</title><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0;url={u}"><a href="{u}">Continue to {k}</a>')
os.makedirs('freeskills', exist_ok=True)
open('freeskills/index.html', 'w').write('<!DOCTYPE html><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=/free/"><a href="/free/">Free playbooks</a>')
open('favicon.svg', 'w').write(LOGO.replace('currentColor', '#15191b').replace('<svg ', '<svg xmlns="http://www.w3.org/2000/svg" '))
open('404.html', 'w').write(open('index.html').read())
