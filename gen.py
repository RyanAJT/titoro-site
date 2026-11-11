# Builds every page of titoro.xyz. Run: python3 gen.py
import os, re, html
from posts import POSTS

LOGO = '<svg viewBox="0 0 120 120"><g fill="currentColor"><path d="M12 50A32 32 0 0 1 44 18H59V50Z"/><path d="M61 18H108V50H92A32 32 0 0 0 61 18Z"/><path d="M44 58H76V106H60A16 16 0 0 1 44 90Z"/><circle cx="94" cy="98" r="9"/></g></svg>'
ARROW = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 8h10M9 4l4 4-4 4"/></svg>'
FOLLOW = '<a href="https://www.instagram.com/titoro.ai">Instagram</a><a href="https://www.tiktok.com/@titoro.ai">TikTok</a><a href="https://www.youtube.com/@TitoroAI">YouTube</a>'
VID = 'https://d2ol7oe51mr4n9.cloudfront.net/user_3KjFE77zHvs65uDD9jyLqGF0S7v/{}.mp4'
ADMIN_REEL = '166b5c3a-b664-4404-8b71-04e2e2bd9c23'
DOCS = {'PYRAMID': '1Ef6QVbcd9yatMF_L4QlqW9CkMAPY-QMJZa483AOyd68', 'PROJECT': '1fuW3_CexjyF42ZBLJTiBQeVFnOzJBLG_ssgaLPe7Ess', 'CLEAR': '194k4NZoPvErjl1bbSCPuCfDJNiRU0LmYSSW9XoZ0XK0', 'ASK': '1eRWCl4XQu_QbrN7VNoJBdYyM5JNXV7dBpS6UhDkUEYU', 'FLOP': '1rL3jQfQ5uYmiHyzRJet0zYNUlmZJyRoCR7ejE20JD_8', 'SETUP': '1Ko7Cnvcm3W9cbLWmEAf9tMKcU7l6NTrwKnHvk_opPhM', 'TELLS': '1ie4LhuN9KSDW1VlDtwNfLh7zzcwp9s9KGUuuzFFM1-I', 'ANIMATE': '14HjSeDhqpLTv6KUW1SCVtcequyP9VpTxrb0TzAEtSPw', 'PRICE': '1Fawi7-r5kSOz3kIQJuQ3DSdKNBxY5G38SlMxD6xOhHs', 'TRAIN': '11qCIFBkS-aRZOr_TPkLXHdxWsmcaidNcIte8FK-50oY', 'HUMAN': '1t_tbTvN4Q7QZ5YC_9DAZTF3z0RP5IjRr6TFdey7gOVA', 'COPY': '1Ng5MPJZx4gVDac2WVVBs74DVkFhztwN51bjoMzzz5RQ', 'LOGO': '1A8Zj2r0KPvhaoYEfxDWq21Y_7AZspCrU1KjTwVAfOdQ', 'PDF': '1SoEhEAl149MN39YKei-Y-PjFO9PXdHYwAlhL9NieHPU', 'INVOICE': '1wt6CL9ud7qbnwoxtHVh5ErSargrx1904fZ1Toc8-QrI', 'PRIVACY': '1Z3BaWTaVaISgxJpHBtdvW3v7wyatJ9tCqYuMoKby1L4'}
P = {p['kw']: p for p in POSTS}
CATS = {'content': 'Content', 'business': 'Business', 'basics': 'Claude basics'}

def svg(vb, d): return f'<svg viewBox="{vb}"><path fill="currentColor" d="{d}"/></svg>'
# key: name, job, one line, offer, url, live affiliate?, brand colour, logo
TOOLS = {
    'higgsfield': ('Higgsfield', 'Video and images', 'Every video and image model, inside Claude.', 'Free 72-hour trial', '/go/higgsfield/', True, '#15191b',
                   svg('0 0 20 20', 'M18.35 9.84l-.02-.18c-.15-1.72-1.24-4.96-4.25-4.96-2.24 0-3.93 2.28-5.42 4.29-1.19 1.6-2.22 2.98-3.36 2.98-.3-.03-.69-.19-.93-.54-.21-.32-.27-.73-.16-1.22.17-.78 1.17-1.5 2.23-2.26.58-.41 1.17-.84 1.59-1.26 1.19-1.18 1.79-2.04 1.79-3.42S9.09 1.21 8.47.91C7.24.32 5.42.67 4.26 1.7l-.51.47C2.59 3.23 1.8 3.96 0 3.4v2.24c2.39 1.09 4.4-.99 5.16-1.94.59-.63 1.2-1 1.66-1h.02c.21.01.38.09.51.24.21.25.29.53.25.85-.09.67-.76 1.45-2 2.31C4.15 7.1 1.72 8.78 1.53 10.9c-.14 1.52.62 3.04 1.81 3.62 2.78 1.36 4.47-.98 6.26-3.45 1.37-1.9 2.67-3.7 4.48-3.7 1.63 0 2.23 1.39 2.23 2.26v.17l-.16.03c-3.94.72-6.09 4.52-6.09 6.28s1.44 3.26 3.22 3.26c2.08 0 4.65-1.83 5.06-6.97l.02-.19H20V9.84h-1.65zm-2.15 2.63c-.32 3.08-1.85 4.52-2.78 4.52-.42 0-1.01-.36-1.01-1.03 0-.75 1.09-3.03 3.53-3.71l.29-.07-.03.29z')),
    'claude': ('Claude', 'The brain', 'Where every script, guide and skill starts.', 'Free plan', 'https://claude.ai', False, '#D97757',
               svg('0 0 24 24', 'm4.7144 15.9555 4.7174-2.6471.079-.2307-.079-.1275h-.2307l-.7893-.0486-2.6956-.0729-2.3375-.0971-2.2646-.1214-.5707-.1215-.5343-.7042.0546-.3522.4797-.3218.686.0608 1.5179.1032 2.2767.1578 1.6514.0972 2.4468.255h.3886l.0546-.1579-.1336-.0971-.1032-.0972L6.973 9.8356l-2.55-1.6879-1.3356-.9714-.7225-.4918-.3643-.4614-.1578-1.0078.6557-.7225.8803.0607.2246.0607.8925.686 1.9064 1.4754 2.4893 1.8336.3643.3035.1457-.1032.0182-.0728-.164-.2733-1.3539-2.4467-1.445-2.4893-.6435-1.032-.17-.6194c-.0607-.255-.1032-.4674-.1032-.7285L6.287.1335 6.6997 0l.9957.1336.419.3642.6192 1.4147 1.0018 2.2282 1.5543 3.0296.4553.8985.2429.8318.091.255h.1579v-.1457l.1275-1.706.2368-2.0947.2307-2.6957.0789-.7589.3764-.9107.7468-.4918.5828.2793.4797.686-.0668.4433-.2853 1.8517-.5586 2.9021-.3643 1.9429h.2125l.2429-.2429.9835-1.3053 1.6514-2.0643.7286-.8196.85-.9046.5464-.4311h1.0321l.759 1.1293-.34 1.1657-1.0625 1.3478-.8804 1.1414-1.2628 1.7-.7893 1.36.0729.1093.1882-.0183 2.8535-.607 1.5421-.2794 1.8396-.3157.8318.3886.091.3946-.3278.8075-1.967.4857-2.3072.4614-3.4364.8136-.0425.0304.0486.0607 1.5482.1457.6618.0364h1.621l3.0175.2247.7892.522.4736.6376-.079.4857-1.2142.6193-1.6393-.3886-3.825-.9107-1.3113-.3279h-.1822v.1093l1.0929 1.0686 2.0035 1.8092 2.5075 2.3314.1275.5768-.3218.4554-.34-.0486-2.2039-1.6575-.85-.7468-1.9246-1.621h-.1275v.17l.4432.6496 2.3436 3.5214.1214 1.0807-.17.3521-.6071.2125-.6679-.1214-1.3721-1.9246L14.38 17.959l-1.1414-1.9428-.1397.079-.674 7.2552-.3156.3703-.7286.2793-.6071-.4614-.3218-.7468.3218-1.4753.3886-1.9246.3157-1.53.2853-1.9004.17-.6314-.0121-.0425-.1397.0182-1.4328 1.9672-2.1796 2.9446-1.7243 1.8456-.4128.164-.7164-.3704.0667-.6618.4008-.5889 2.386-3.0357 1.4389-1.882.929-1.0868-.0062-.1579h-.0546l-6.3385 4.1164-1.1293.1457-.4857-.4554.0608-.7467.2307-.2429 1.9064-1.3114Z')),
    'elevenlabs': ('ElevenLabs', 'Voice and sound', 'Voiceovers, music and sound effects.', 'Free plan', '/go/elevenlabs/', False, '#15191b', svg('0 0 24 24', 'M4.6035 0v24h4.9317V0zm9.8613 0v24h4.9317V0z')),
    'manychat': ('ManyChat', 'DMs', 'Sends the guide when someone comments a keyword.', 'Free plan', '/go/manychat/', False, '#2a7cf6', '<b>M</b>'),
    'buffer': ('Buffer', 'Posting', 'Schedules posts to IG, TikTok and YouTube.', 'Free plan', '/go/buffer/', False, '#231F20',
               svg('0 0 24 24', 'M1.371 5.476L11.943 0l10.686 5.476-10.686 5.495zm3.36 4.81l7.212 3.547 7.288-3.547 3.398 1.655-10.686 5.202L1.371 11.94zm0 6.171l7.212 3.911 7.288-3.91 3.398 1.815L11.943 24 1.371 18.273z')),
    'apify': ('Apify', 'Research', 'Ready-made scrapers for comments, prices and more.', 'Free plan', '/go/apify/', False, '#1d6f7f', '<b>A</b>'),
}
PACKS = [
    ('Content Engine', '$19', 'Write a week of content in one sitting, in your own voice.', ['Captions in your voice', 'Hook writer: 10 hooks, under 8 words', 'Reel script writer: hook, 3 steps, flip, CTA'], 'Bonus: the 10 animation prompts'),
    ('Business Ops', '$15', 'The boring admin, handled.', ['SOP rewriter: one action per step', 'Quote and invoice drafter', 'Staff training game builder'], ''),
    ('Both packs', '$25', 'Everything above, plus every future update.', [], ''),
]
MAIL = '''<form class="mail" novalidate><label for="em{n}">Your email</label><div class="row"><input id="em{n}" type="email" placeholder="you@yourbusiness.com" required><button class="btn">{cta}</button></div><small>{help}</small></form>'''
KWS = ','.join(P)
FIND = f'<form class="find" data-kw="{KWS}"><input placeholder="Commented a keyword? Type it here" aria-label="Find a playbook by keyword" autocapitalize="characters"><button class="btn" aria-label="Find">{ARROW}</button></form>'


def page(path, title, desc, body, on=''):
    nav = ''.join(f'<a class="l{" on" if on == k else ""}" href="/{k}/">{v}</a>' for k, v in [('free', 'Free playbooks'), ('packs', 'Skill Packs'), ('tools', 'Tools')])
    out = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<link rel="icon" href="/favicon.svg"><link rel="stylesheet" href="/style.css">
<script src="/build.js"></script></head>
<body>
<nav class="top"><a class="logo" href="/">{LOGO}titoro</a>{nav}<a class="cta" href="/free/">Get the free stuff</a></nav>
{body}
<div class="wrap"><footer data-b="footer">
<div><b style="color:var(--ink)">titoro</b><br>Free AI playbooks for people who run a business.<br><br><span class="small">Not affiliated with Anthropic. Claude is a trademark of Anthropic, PBC. Some links are affiliate links: I may earn a commission at no cost to you.</span>
<p class="built"><span class="mono">This site was built by 12 AI agents.</span> <button class="lnk" data-replay>Watch them build it {ARROW}</button></p></div>
<div class="fl"><span class="mono">Site</span><a href="/free/">Free playbooks</a><a href="/packs/">Skill Packs</a><a href="/tools/">Tools</a><a href="/disclosure/">Disclosure</a></div>
<div class="fl"><span class="mono">Follow</span>{FOLLOW}<span>created by orca.agentics</span></div>
<div class="big">titoro.</div>
</footer></div>
<script src="/vendor/gsap.min.js"></script><script src="/vendor/ScrollTrigger.min.js"></script><script src="/vendor/lenis.min.js"></script><script src="/site.js"></script>
</body></html>
'''
    os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
    open(path, 'w').write(out)


def phone(reel, cls='', speed=None):
    sp = f' data-speed="{speed}"' if speed is not None else ''
    return f'<div class="ph {cls}"{sp}><video muted loop playsinline preload="none" data-src="{VID.format(reel)}"></video><span class="phlogo">{LOGO}</span></div>'


def tile(k, small=False):
    n, job, line, offer, url, aff, col, lg = TOOLS[k]
    ext = '' if url.startswith('/') else ' target="_blank" rel="noopener"'
    return (f'<a class="tile{" sm" if small else ""}" href="{url}"{ext}><span class="lg" style="--c:{col}">{lg}</span>'
            f'<span class="tt"><b>{n}</b><span class="mono">{job}</span></span><p>{line}</p>'
            f'<span class="go">{offer} · Try it {ARROW}</span>' + ('<span class="aff mono">affiliate</span>' if aff else '') + '</a>')


def feat():
    lg = TOOLS['higgsfield'][7]
    return f'''<div class="feat"><span class="lg big" style="--c:#fff;color:#15191b">{lg}</span>
<div><span class="mono" style="color:var(--mist)">Partner offer · Higgsfield</span><h3>Every video model, inside Claude.</h3>
<p>Higgsfield's connector puts the top video, image and audio models right in your Claude chat. New users get a free 72-hour trial.</p></div>
<div class="fa"><a class="btn" href="/go/higgsfield/">Start the free trial {ARROW}</a><a class="lnk" href="/fable/">How to set it up</a><span class="mono small">affiliate link · card needed, cancel before day 3</span></div></div>'''


def gcard(k, i=0):
    p = P[k]
    return f'<a class="g{" dark" if i % 5 == 2 else ""}" href="/free/{k.lower()}/" data-kw="{k}" data-cat="{p["cat"]}"><span class="mono">Comment {k}</span><div class="kw">{k}</div><p>{p["title"]}</p></a>'


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    t = re.sub(r'(?<!\*)\*(?!\s)(.+?)\*', r'<i>\1</i>', t)
    return re.sub(r'`(.+?)`', r'<code>\1</code>', t)


def md(src):
    out, lst, code = [], None, None
    for ln in src.split('\n'):
        if code is not None:
            if ln.strip() == '```':
                out.append(f'<div class="prompt"><span class="mono">Copy-paste prompt</span><pre>{html.escape(chr(10).join(code), quote=False)}</pre><button class="copy">Copy prompt</button></div>'); code = None
            else: code.append(ln)
            continue
        m = re.match(r'(\d+)\. (.*)', ln) or re.match(r'(-) (.*)', ln)
        kind = ('ol' if m.group(1) != '-' else 'ul') if m else None
        if lst and kind != lst: out.append(f'</{lst}>'); lst = None
        if ln.strip() == '```': code = []
        elif ln.startswith('## '): out.append(f'<h2>{inline(ln[3:])}</h2>')
        elif m:
            if not lst: out.append(f'<{kind}>'); lst = kind
            out.append(f'<li>{inline(m.group(2))}</li>')
        elif ln.strip(): out.append(f'<p>{inline(ln)}</p>')
    if lst: out.append(f'</{lst}>')
    return '\n'.join(out)


# ---------- home ----------
start = ''.join(f'''<a class="start" href="/free/{k.lower()}/" data-speed="{s}">{phone(P[k]["reel"], "mini")}<div><span class="mono">Comment {k}</span><h3>{P[k]["title"]}</h3><p>{P[k]["desc"]}</p><span class="lnk">Read the playbook {ARROW}</span></div></a>''' for k, s in [('PYRAMID', .04), ('PROJECT', -.04), ('HUMAN', .04)])
home = f'''
<header class="wrap hero" data-b="hero">
  <svg class="bigT" data-speed="-.3" viewBox="0 0 120 120"><g fill="currentColor"><path d="M12 50A32 32 0 0 1 44 18H59V50Z"/><path d="M61 18H108V50H92A32 32 0 0 0 61 18Z"/><path d="M44 58H76V106H60A16 16 0 0 1 44 90Z"/><circle cx="94" cy="98" r="9"/></g></svg>
  <div>
    <p class="mono eyebrow"><b>titoro.xyz</b> From the @titoro.ai reels</p>
    <h1>Free AI playbooks for people who <span class="serif">run a business</span>.</h1>
    <p class="sub">Step-by-step guides from my reels. Copy the prompt, follow the steps, done.</p>
    {FIND}
    <div class="ctas"><a class="btn" href="/free/">Browse free playbooks {ARROW}</a><a class="btn alt" href="/packs/">See Skill Packs</a></div>
    <p class="mono note">{len(POSTS)} playbooks · new ones every week</p>
  </div>
  <div class="stage">
    {phone(P["PYRAMID"]["reel"], "p1", -.18)}{phone(P["HUMAN"]["reel"], "p2", .1)}{phone(P["PROJECT"]["reel"], "p3", -.06)}
    <span class="chip c1" data-speed="-.35">Comment <b>PYRAMID</b></span><span class="chip c2" data-speed=".25">Guide sent ✓</span>
  </div>
</header>

<section class="blk wrap" data-b="offers">
  <p class="mono eyebrow"><b>01</b> What you get</p>
  <h2>Three ways to get AI <span class="serif">working</span> for you.</h2>
  <div class="offers">
    <a class="offer" href="/free/" data-speed=".03"><span class="mono">Free</span><div class="num">{len(POSTS)}</div><h3>Free playbooks</h3><p>Step-by-step guides. Copy, paste, done.</p><div class="kws">{"".join(f"<i>{k}</i>" for k in list(P)[:6])}</div><span class="lnk">Browse free {ARROW}</span></a>
    <a class="offer dark" href="/packs/" data-speed="-.04"><span class="mono">Paid</span><div class="num">$15<small>+</small></div><h3>Skill Packs</h3><p>The playbooks I use most, turned into skills Claude runs for you.</p><div class="kws"><i>Content Engine</i><i>Business Ops</i></div><span class="lnk">See packs {ARROW}</span></a>
    <a class="offer" href="/tools/" data-speed=".05"><span class="mono">Free trials</span><div class="logos">{"".join(f'<span class="lg" style="--c:{TOOLS[k][6]}">{TOOLS[k][7]}</span>' for k in TOOLS)}</div><h3>Tools I use</h3><p>The exact stack behind my reels, with free plans and trials.</p><span class="lnk">See tools {ARROW}</span></a>
  </div>
</section>

<section class="blk wrap" data-b="how">
  <p class="mono eyebrow"><b>02</b> How it works</p>
  <h2>Get any playbook in <span class="serif">3 steps</span>.</h2>
  <div class="how">
    <div class="steps">
      <div class="step on"><span class="n">01</span><h3>Watch a reel.</h3><p>One idea, under a minute.</p></div>
      <div class="step"><span class="n">02</span><h3>Comment the keyword.</h3><p>It's at the end of every reel, like PYRAMID or CLEAR.</p></div>
      <div class="step"><span class="n">03</span><h3>Get the guide in your DMs.</h3><p>Or grab it right here, no comment needed.</p><a class="btn" href="/free/" style="margin-top:22px">Browse free playbooks {ARROW}</a></div>
    </div>
    <div class="phoneWrap">{phone(ADMIN_REEL, "how")}</div>
  </div>
</section>

<section class="blk wrap" data-b="start">
  <p class="mono eyebrow"><b>03</b> Start here</p>
  <h2>New here? Start with <span class="serif">these 3</span>.</h2>
  <div class="starts">{start}</div>
  <p style="margin-top:28px"><a class="btn alt" href="/free/">See all {len(POSTS)} playbooks {ARROW}</a></p>
</section>

<section class="blk wrap" data-b="tools">
  <p class="mono eyebrow"><b>04</b> Tools I use</p>
  <h2>The tools behind <span class="serif">every</span> reel.</h2>
  {feat()}
  <div class="tiles">{"".join(tile(k) for k in ["claude", "elevenlabs", "manychat", "buffer", "apify"])}</div>
  <p class="small" style="margin-top:18px">Some links are affiliate links. I only list what I use.</p>
</section>

<section class="wrap" data-b="email" style="padding-bottom:120px">
  <div class="endc"><div><p class="mono" style="color:var(--mist)">Weekly</p><h2>One useful AI trick a week.</h2><p class="lead">Short, practical, free. Unsubscribe any time.</p></div>
  <div>{MAIL.format(n=1, cta='Send it to me', help='No spam. Just the trick.')}</div></div>
</section>
'''
page('index.html', 'titoro · Free AI playbooks for people who run a business', 'Free step-by-step AI playbooks from the @titoro.ai reels, ready-made Claude Skill Packs, and the tools I use.', home)

# ---------- free: orbit dashboard ----------
orbit = ''.join(f'<a class="oc" href="/free/{k.lower()}/" data-kw="{k}" data-cat="{p["cat"]}" data-ring="{i % 2}"><span class="mono">{CATS[p["cat"]]}</span><b>{k}</b><small>{p["title"]}</small></a>' for i, (k, p) in enumerate(P.items()))
chips = '<button class="chipf on" data-cat="all">All</button>' + ''.join(f'<button class="chipf" data-cat="{c}">{n}</button>' for c, n in CATS.items())
page('free/index.html', 'Free AI playbooks · titoro', f'{len(POSTS)} free step-by-step AI playbooks from the @titoro.ai reels. Pick one, copy the prompt, done.', f'''
<header class="wrap phead fhead" data-b="header"><p class="mono eyebrow"><b>Free</b> {len(POSTS)} playbooks</p><h1>{len(POSTS)} free <span class="serif">playbooks</span>.</h1><p class="lead">Pick one, copy the prompt, done.</p>
<div class="ftools"><input class="fsearch" placeholder="Type a keyword, e.g. PYRAMID" aria-label="Search playbooks"><div class="chips">{chips}</div></div></header>
<section class="orbit" data-b="orbit"><div class="core">{LOGO}<span class="mono">titoro.ai</span></div>{orbit}</section>
<section class="wrap" data-b="library"><p class="mono eyebrow" style="margin-top:20px"><b>All</b> The full list</p><div class="grid2">{"".join(gcard(k, i) for i, k in enumerate(P))}</div></section>
<section class="wrap" data-b="nudge" style="padding-bottom:120px"><div class="endc"><div><h2>Want them done for you?</h2><p class="lead">Skill Packs turn my most-used playbooks into skills Claude runs for you.</p></div><div><a class="btn" href="/packs/">See Skill Packs {ARROW}</a></div></div></section>
''', 'free')

# ---------- playbook posts ----------
for p in POSTS:
    k = p['kw']
    media = phone(p['reel'], 'post') if p['reel'] else f'<div class="kwcard"><span class="mono">Comment</span><b>{k}</b></div>'
    pack = next((x for x in PACKS if x[0] == p['pack']), None)
    rel = P[p['related']]
    side = f'''<div class="sbox"><span class="mono">Tools in this playbook</span>{"".join(tile(t, True) for t in p["tools"])}</div>
<a class="sbox rel" href="/free/{rel["kw"].lower()}/"><span class="mono">Next playbook</span><b>{rel["kw"]}</b><p>{rel["title"]}</p></a>''' + (f'''
<a class="sbox packbox" href="/packs/"><span class="mono">Done for you</span><b>{pack[0]} Pack</b><p>{pack[2]} {pack[1]}.</p><span class="lnk">See the pack {ARROW}</span></a>''' if pack else '')
    page(f'free/{k.lower()}/index.html', f'{p["title"]} · titoro', p['desc'], f'''
<header class="wrap posthd" data-b="header">
  <div><p class="mono crumbs"><a href="/free/">Free playbooks</a> / {k}</p>
  <p class="mono eyebrow"><b>Comment {k}</b> {p["mins"]}-minute read · {p["plan"]}</p>
  <h1>{p["title"]}</h1>
  <div class="get"><span class="mono">What you'll get</span><ul>{"".join(f"<li>{g}</li>" for g in p["get"])}</ul></div></div>
  <div class="pmedia" data-speed="-.08">{media}</div>
</header>
<section class="wrap postwrap" data-b="post">
  <article class="pbody">{md(p["body"])}
  <p class="docl"><a class="btn alt" href="https://docs.google.com/document/d/{DOCS[k]}/view" target="_blank" rel="noopener">Open the Google Doc version {ARROW}</a></p>
  <p class="small">Some links are affiliate links: I may earn a commission at no cost to you. Not affiliated with Anthropic.</p></article>
  <aside class="side">{side}</aside>
</section>
<section class="wrap" data-b="email" style="padding-block:40px 120px"><div class="endc"><div><h2>One useful AI trick a week.</h2><p class="lead">Like this one. Free, short, no spam.</p></div><div>{MAIL.format(n=1, cta='Send it to me', help='Unsubscribe any time.')}</div></div></section>
''', 'free')

# ---------- packs ----------
pcs = ''.join(f'''<div class="pk{" main" if i == 0 else ""}"><span class="mono soon">Coming soon</span><h3>{n}</h3><p>{d}</p>''' + (f'<ul>{"".join(f"<li>{x}</li>" for x in items)}</ul>' if items else '') + (f'<p class="bonus">{b}</p>' if b else '') + f'<div class="price">{pr}</div></div>' for i, (n, pr, d, items, b) in enumerate(PACKS))
page('packs/index.html', 'Skill Packs · titoro', 'Ready-made Claude skills, tested, with a short setup video.', f'''
<header class="wrap phead" data-b="header"><p class="mono eyebrow"><b>Packs</b> Works with Claude</p><h1>Guides teach you how. Packs <span class="serif">do it for you</span>.</h1><p class="lead">My most-used playbooks, turned into skills Claude runs for you. Every skill is one I use myself, tested before it goes on sale.</p></header>
<section class="wrap" data-b="packs"><div class="packs" style="margin-top:20px">{pcs}</div></section>
<section class="wrap blk" data-b="howp"><h2>How it works</h2><div class="three">
<div><span class="n mono">01</span><h3>Download</h3><p>Get the skill files and a 2-minute setup video.</p></div>
<div><span class="n mono">02</span><h3>Upload once</h3><p>In Claude, go to Customize → Skills and add the files.</p></div>
<div><span class="n mono">03</span><h3>Just ask</h3><p>"Write this week's captions." Claude uses the skill automatically.</p></div></div></section>
<section class="wrap" data-b="waitlist"><h2>Get first access.</h2><p class="lead">Packs launch one at a time. Join the list and you hear first.</p>{MAIL.format(n=2, cta='Join the waitlist', help='One email when a pack launches. Nothing else.')}</section>
<section class="wrap" data-b="faq" style="padding-block:80px 120px"><div class="prose" style="margin:0">
<p><b>Do I need to code?</b><br>No. You upload the files in Claude once.</p>
<p><b>Which Claude plan?</b><br>Each pack says exactly what it needs before you buy.</p>
<p><b>Is this official?</b><br>No. These are my own skills, not affiliated with or endorsed by Anthropic.</p>
<p><b>Refunds?</b><br>If a pack doesn't work for you within 14 days, email me and I'll refund you.</p></div></section>
''', 'packs')

# ---------- tools ----------
page('tools/index.html', 'Tools I use · titoro', 'The exact AI tools behind the @titoro.ai reels, with free plans and trials.', f'''
<header class="wrap phead" data-b="header"><p class="mono eyebrow"><b>Tools</b> {len(TOOLS)} tools</p><h1>The tools behind <span class="serif">every</span> reel.</h1><p class="lead">The exact stack I use for scripts, voice, video, DMs and posting. Some links are affiliate links: if you sign up, I may earn a commission at no extra cost to you. I only list what I use.</p></header>
<section class="wrap" data-b="tools" style="padding-bottom:120px">{feat()}<div class="tiles">{"".join(tile(k) for k in TOOLS if k != "higgsfield")}</div></section>
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
<section class="wrap" data-b="more" style="padding-block:80px 120px"><div class="replay"><div><h2>Want more like this?</h2><p class="lead">Every reel I post becomes a free playbook.</p></div><div><a class="btn" href="/free/">See the free playbooks {ARROW}</a></div></div></section>
''')

# ---------- short links ----------
for k, u in {'manychat': 'https://manychat.com', 'buffer': 'https://buffer.com', 'elevenlabs': 'https://elevenlabs.io', 'higgsfield': 'https://higgsfield.ai?fpr=jing-45bb72', 'apify': 'https://apify.com'}.items():
    os.makedirs(f'go/{k}', exist_ok=True)
    open(f'go/{k}/index.html', 'w').write(f'<!DOCTYPE html><meta charset="utf-8"><title>Redirecting</title><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0;url={u}"><a href="{u}">Continue to {k}</a>')
os.makedirs('freeskills', exist_ok=True)
open('freeskills/index.html', 'w').write('<!DOCTYPE html><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=/free/"><a href="/free/">Free playbooks</a>')
open('favicon.svg', 'w').write(LOGO.replace('currentColor', '#15191b').replace('<svg ', '<svg xmlns="http://www.w3.org/2000/svg" '))
open('404.html', 'w').write(open('index.html').read())
urls = ['', 'free/', 'packs/', 'tools/', 'fable/', 'disclosure/'] + [f'free/{k.lower()}/' for k in P]
open('sitemap.xml', 'w').write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(f'<url><loc>https://titoro.xyz/{u}</loc></url>' for u in urls) + '</urlset>')
open('robots.txt', 'w').write('User-agent: *\nAllow: /\nSitemap: https://titoro.xyz/sitemap.xml\n')
