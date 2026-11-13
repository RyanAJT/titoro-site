# The 16 playbook posts. Body uses mini-markdown: ## heading, 1. / - lists, ``` prompt blocks, **bold**, *italic*, `code`.
# Facts come from the matching Google Doc guide. Tools only appear where they do a real step.

POSTS = [
dict(kw='BUILD', cat='content', mins=6, plan='Claude Pro (Fable 5.2 until 16 Nov)', reel=None,
  title='3 things to build with Claude Fable 5.2 before Monday',
  desc='A brand mini-game, a rebuilt website and a month of content. Nine copy-paste Claude prompts, three for each build.',
  get=['A playable mini-game that collects emails', 'A rebuilt homepage you can publish', '30 days of content and a week of scripts'],
  tools=['claude'], related='PROMPTS', pack='Content Engine',
  body='''Claude Fable 5.2 is on the Pro plan until Monday 16 November. Don't waste it on random chats. Here are three things worth building this weekend, with three copy-paste prompts each. Run each build in its own chat so Claude remembers your details.

## Build 1: A mini-game for your brand
A game people actually play keeps them on your page way longer than any post.
```
My business: [what you sell, who it's for, your vibe].
Suggest 5 simple browser mini-games that fit my brand and that someone could finish in under 60 seconds. For each: the name, how it plays in one line, how it shows off my product, and why people would share it. Then pick the best one and explain why.
```
```
Build the game you picked as one single HTML file I can open in a browser. Rules:
- Works on phone and desktop (tap and click)
- Uses my brand colours: [hex codes] and my logo text: [name]
- Start screen, game, end screen with the score
- No external libraries or images, draw everything with code
Give me the full file in one code block.
```
```
Update the game:
- On the end screen, show the score and a box: "Enter your email to get [your offer, e.g. 10% off]"
- Save the email and score to the browser's local storage and show a thank-you message
- Add a "Play again" and a "Share my score" button that copies a text like "I scored [X] on [game name], beat me at [your link]"
Give me the full updated file.
```

## Build 2: Rebuild your website
Most small business sites are a logo and a phone number. Audit, rewrite, build.
```
Here's the text from my current homepage: [paste it, or paste the URL if Claude can browse].
My customer: [who]. What I want visitors to do: [book / buy / message].
Act like a conversion copywriter. List the 10 biggest problems losing me customers, worst first. For each: what's wrong, why it costs me, and the fix in one line.
```
```
Rewrite my homepage using your fixes. Sections:
1. Hero: headline under 10 words, a one-line subhead, the button text
2. The problem my customer has
3. How I solve it: 3 benefits
4. Proof: [paste reviews or results]
5. FAQ: the 5 objections people have before buying
6. Final call to action
Keep it in plain words a 12-year-old would understand.
```
```
Turn that copy into one single HTML page I can publish. Modern, clean, mobile-first, brand colours [hex codes], font [name or "clean sans-serif"]. Add smooth scroll, a sticky button, and leave image placeholders labelled with what photo to put there. Give me the full file in one code block.
```

## Build 3: A month of content in your voice
Paste five posts, get thirty days planned and a week of scripts ready to film.
```
Here are 5 of my best posts or captions: [paste them].
Study how I write: tone, sentence length, words I use, words I'd never use, how I open and how I end. Write it up as a "brand voice guide" with 10 rules and 3 example sentences. Use this guide for everything else we write in this chat.
```
```
Using my voice guide, plan 30 days of short-form video for [business]. Mix: 40% tips, 30% behind the scenes, 20% customer stories, 10% offers.
Make it a table: day | format (talking head / B-roll / carousel) | hook (first line) | the one point | CTA.
```
```
Write full scripts for days 1 to 7. Each one:
- A hook in the first 2 seconds
- 30 to 45 seconds when spoken
- On-screen text suggestions in [brackets]
- A caption with 3 hashtags
All in my brand voice. Make them ready to film.
```

## Tips
- Fill in every [bracket]. The more specific you are, the better the result.
- After Monday these prompts still work on other Claude models, just with simpler results.'''),

dict(kw='PROMPTS', cat='content', mins=5, plan='Free Claude plan', reel=None,
  title='5 Claude prompts that replace a marketing agency',
  desc='Hooks, competitor research, a 30-day plan, welcome emails and a landing page. Five copy-paste prompts for small businesses.',
  get=['10 hooks in your brand voice', "Your competitors' weak spots", 'A 30-day plan, emails and a landing page'],
  tools=['claude'], related='PYRAMID', pack='Content Engine',
  body='''Agencies charge thousands a month for the work these five prompts do in one chat. Fill in the [brackets] and run them in one chat so Claude remembers your brand.

## 1. Hooks that sound like you, not an ad
```
You're my social media manager.
My brand: [name], [what you sell], [who it's for], [your tone, e.g. small-batch, slightly cheeky].
Write 10 Instagram hooks that sound like us, not like an ad.
Each under 12 words. No hashtags, no emojis.
```

## 2. Spy on your competitors
```
Here are reviews of 3 competitors: [paste Google / Shopee / Amazon reviews].
1. Group the complaints by theme and count how often each comes up.
2. For each of the top 5, tell me how my business could win on it.
Put it in a table: complaint | count | how I win.
My business: [what you sell].
```

## 3. A month of content in 30 seconds
```
Plan 30 days of Instagram posts for [business].
Mix: 40% tips, 30% behind-the-scenes, 20% social proof, 10% offers.
One line per day, grouped by week, with the format (reel / carousel / story).
```

## 4. Emails that actually sell
```
Write a 3-email welcome sequence for new subscribers of [business].
Goal: first order within 7 days.
Email 1 (day 0): welcome + small hook. Email 2 (day 3): our story / why we're different. Email 3 (day 6): offer with a deadline.
Give subject lines, preview text and the full body. Keep each under 120 words.
```

## 5. A landing page that converts
```
Write the hero section for my product page.
Product: [what it is]. Customer: [who]. Biggest objection: [e.g. price, freshness, trust].
Give me: a headline under 10 words, a one-line subhead, 3 benefit bullets that answer the objection, and the button text.
Then give 2 alternative headlines to A/B test.
```

## Tips
- The more specific your [brackets], the less generic the output.
- Works on the free Claude plan.'''),

dict(kw='PYRAMID', cat='content', mins=3, plan='Free Claude plan', reel='e69212b2-e741-4092-b689-9d2bd4772c1e',
  title='The 4-line prompt that beats a 300-word prompt',
  desc='Stop writing long prompts. The 4-line prompt pyramid gets better results from Claude. Free copy-paste template.',
  get=['A 4-line prompt you can reuse for anything', 'Answers that sound like you, not a robot', 'Fewer rewrites: fix results in one line'],
  tools=['claude'], related='PROJECT', pack='Content Engine',
  body='''Most people try to get better AI results by writing longer prompts. With the newest models that usually backfires. A long script boxes the AI in. A clear goal, plus room to think, gets you something better.

## Why it works
New models are good at planning. When you give them a goal, let them research and let them ask you questions, they fill the gaps with your real details instead of guessing.

## The 4 layers
1. **Goal.** What you want and who it's for. *"A reel about our free Claude guide, for small business owners."*
2. **Let it research.** *"Look at what's working for pages like mine first."* Works best with web search turned on.
3. **Let it interview you.** *"Ask me 5 questions before you write anything."*
4. **One good example.** Paste one past post that actually worked.

## Copy-paste template
```
Goal: [what you want] for [who it's for].
First, look at what's working for [pages / businesses like mine].
Ask me 5 questions before you write anything.
Here's one past post that worked: [paste it]
```

## Tips
- Answer its questions honestly and briefly. That's where your own voice comes from.
- Don't like the result? Say what's wrong in one line ("too formal", "shorter") instead of rewriting the prompt.
- Works on the free Claude plan, and in most other AI chats.'''),

dict(kw='PROJECT', cat='basics', mins=5, plan='Free Claude plan', reel='127f4330-ca8f-4636-b5d7-4d70c96f8692',
  title='Make Claude remember your business in every chat',
  desc='Stop starting every Claude chat from zero. Set up a Claude Project with your files and a copy-paste instructions template.',
  get=['A Claude Project set up in about 5 minutes', 'A fill-in instructions template', 'Real prices and tone in every chat, without pasting them again'],
  tools=['claude'], related='HUMAN', pack='Content Engine',
  body='''Every new Claude chat starts blank, so you re-upload the same price list and re-explain your business every time. A **Project** fixes that: add your files and instructions once, and every chat inside the Project uses them. It works on the free plan too.

## What you get on each plan
- **Free:** up to 5 Projects, with files and instructions.
- **Paid plans:** when your files get big, Claude switches on a search mode (RAG) so the Project can hold much more.
- Chats in the same Project don't read each other's history. Only the files and instructions carry over, so anything important belongs in a file.

## Set it up in 3 steps
1. **Create the Project.** Click **Projects** in the left sidebar, then **New project**. Name it after your business.
2. **Upload your files once.** On the Project page, click **Add** next to **Context** (on some accounts it's called **Project knowledge**). Start with your price list or menu, a one-page brand guide, and 3 to 10 posts that worked.
3. **Paste your instructions.** Click **Add** next to **Instructions**, paste the template below with your details, and save.

## The instructions template
```
You are the marketing assistant for [BUSINESS NAME], a [what you are] in [area].
Read the files in this project before you write anything:
- [price list file]: the only prices and promos you may use
- [brand guide file]: who reads our posts and how we sound
- [best posts file]: copy this style, not the words
About us: what we sell [products, price range]; who buys [one real customer]; why us [1 to 3 honest reasons].
How we sound: [tone], [length], [language].
Never: use the words elevate, unlock, unleash, delve, game-changer, seamless, journey. Never invent prices, promos, results or reviews. If something is missing, ask me.
Always: use prices exactly as written. End promos with [your call to action]. Give me 3 clearly different options. If my request is unclear, ask 1 or 2 questions first.
```

## Check it works
Open a new chat inside the Project and try:
1. "Write this week's promo post." It should use your real prices without you pasting anything.
2. "What's our cheapest item?" It should answer from your price list.
3. "Reply to a customer asking if we deliver." If your files don't say, it should ask you instead of making something up.

## Keep it sharp
- One Project per business or client. Don't mix brands.
- Update the files, not the chats. Price change? Replace the file and every chat gets it.
- Found a caption style you love? Add it to your best-posts file.'''),

dict(kw='HUMAN', cat='content', mins=4, plan='Free Claude plan', reel='1d14c567-4e82-47ae-b94e-a9bcaffdb6a5',
  title="Make AI writing sound like you, not a robot",
  desc='The 3-exhibit prompt and 40 banned AI words that make Claude write captions that sound like a real person.',
  get=['The 3-exhibit prompt', '40 AI words to ban', '3 caption versions every time: funny, straight, very short'],
  tools=['claude'], related='COPY', pack='Content Engine',
  body='''Claude sounds like a robot because it doesn't know you, so it fills the gaps with the safest, most average words it can find. Give it three pieces of evidence and the captions change completely.

## The 3 exhibits
1. **Exhibit A: posts that worked.** Paste 3 real posts that got good reactions. Examples beat adjectives.
2. **Exhibit B: who's reading.** One specific person. "Office workers, half asleep in the lift at 7:45am" writes a completely different caption from "young professionals".
3. **Exhibit C: banned words.** The words that make you sound like an ad.

## The prompt
```
Write [what you need] for [business], about [the offer or news].
Exhibit A: posts that worked for us. Copy the style, not the words:
1. [paste post]
2. [paste post]
3. [paste post]
Exhibit B: who's reading: [one real person: who, where, what time, how they feel]. Write only for them.
Exhibit C: never use these words or phrases: [paste the banned list]. No hashtags inside the text.
Rules: under [number] words. Put the price or key fact in the first line. Sound like a person talking, not an ad. Give me 3 versions: one funny, one straight, one very short.
```

## The banned list
elevate, unlock, unleash, delve, embark, journey, realm, tapestry, landscape, game-changer, revolutionise, seamless, cutting-edge, robust, leverage, harness, empower, transformative, navigate, foster, synergy, testament, vibrant, bustling, nestled, pivotal, meticulous, curated, ever-evolving, indulge, "in today's fast-paced world", "more than just a…", "look no further", "it's not just X, it's Y", "whether you're a… or a…", "take it to the next level", "let's dive in", "the power of", "a symphony of", "we've got you covered".

Add your own: any word Claude uses three times in a row is a candidate.

## Before and after (demo shop)
**Before:** "In today's fast-paced world, coffee is more than just a drink. Elevate your mornings!"

**After, with the 3 exhibits:** "Kopi Ais. RM4.90. Eyes open in one sip."

## Make it permanent
- Put the exhibits in a Claude Project so every chat starts with them. See the **PROJECT** playbook.
- Still too stiff? Reply "too polished, make it sound like a text to a friend".'''),

dict(kw='COPY', cat='content', mins=3, plan='Free Claude plan', reel=None,
  title='5 caption prompts that actually sell',
  desc='Five copy-paste prompts that turn flat captions into posts people act on. Works in Claude, ChatGPT or Gemini.',
  get=['5 caption prompts you can paste today', 'A WhatsApp broadcast version of any post', 'Captions that answer objections before they come up'],
  tools=['claude', 'buffer'], related='HUMAN', pack='Content Engine',
  body='''## Step 0: teach it your voice
Paste 3 of your own best posts first and say: *"This is how I write. Match this voice in everything below."*

## The 5 prompts
1. **Rewrite to sell:** "Rewrite this caption to make someone want it today. No hype words (no 'elevate', 'unlock', 'game-changer'). Keep it under 60 words: [paste caption]"
2. **Hook ×10:** "Give me 10 opening hooks for this post, each under 8 words. Mix curiosity, a number, and a bold claim I can back up."
3. **Objection killer:** "List the 3 objections a customer will have about this offer (price, trust, timing) and rewrite the caption so it answers them without sounding defensive."
4. **WhatsApp version:** "Turn this into a WhatsApp broadcast under 60 words, friendly, one clear next step, no hashtags."
5. **Make it shorter:** "Cut this in half. Keep the offer, the price and the call to action."

## Before and after (demo bakery)
**Before:** New cake available. Order now.

**After:** Pandan gula melaka cake, baked fresh this morning. Soft, not too sweet. 12 slices left today. WhatsApp us to keep one 🍰

## Why these work
Anthropic's prompting guide boils down to: be clear and direct, give context (who it's for, where it's posted), and show examples (your own posts).

## Post them on autopilot
Once you have a week of captions, schedule them all in one sitting with Buffer instead of posting by hand every day.'''),

dict(kw='ASK', cat='content', mins=4, plan='Free Claude plan', reel='8bb31b77-9632-44da-a05a-b2612f45b22b',
  title="Find your next 10 video ideas in someone else's comments",
  desc="Your customers already told you what they want, in other creators' comment sections. Two prompts turn those comments into 10 video ideas.",
  get=['The top 10 complaints your customers have', 'Real quotes to use as hooks', 'A 40-second script for each one'],
  tools=['claude', 'apify'], related='FLOP', pack='Content Engine',
  body='''## Step 1: find 10 creators your customers follow
Look for accounts in your niche with roughly 5K to 50K followers. Smaller creators have more honest comment sections.

## Step 2: get the comments into Claude
Open their 3 most popular posts and copy the comments. Faster: pull them with Apify's Instagram comment scraper and download the file. Then paste into Claude with:
```
These are comments from posts my customers watch.
1. Group them by the problem or complaint people mention.
2. Rank the top 10 complaints by how often they come up.
3. For each one, quote 2 real comments word for word.
My business: [what you sell, who it's for].
```

## Step 3: one video per complaint
```
For complaint #[number], write a 40-second reel script.
- Line 1: say the complaint the way customers say it.
- Show the quick fix in 3 steps.
- My product is the fix, but give real value even without buying.
- End with: Comment [KEYWORD] and I'll send you [freebie].
```

## Tips
- Use the customers' own words in your hook. That's what makes people stop scrolling.
- Don't copy the creator's video. You're using the comments to learn what people want.'''),

dict(kw='FLOP', cat='content', mins=4, plan='Free Claude plan', reel=None,
  title='Ask Claude why your reels flopped',
  desc='Screenshot your Instagram Insights and let Claude tell you why your worst reels flopped. 5 prompts and a 10-point flop checklist.',
  get=['A diagnosis of your worst reels', '5 new hooks for each flop', 'A 7-day plan built only on what already works for you'],
  tools=['claude'], related='ASK', pack='Content Engine',
  body='''No new apps or logins: just screenshots from Instagram Insights.

## What to screenshot
Instagram app → your reel → View insights: views, accounts reached, average watch time, skip rate (if shown), saves and shares. Do it for your 3 best and 3 worst reels.

## The 5 prompts
1. **Flop diagnosis:** "Here are Insights for my 3 best and 3 worst reels. Why did the worst ones flop? Be specific about the first 3 seconds."
2. **Compare:** "What do my best 3 have in common that my worst 3 don't? Hook, length, format, topic."
3. **Hook rewrite ×5:** "Rewrite the opening line of [worst reel] 5 ways, each under 8 words, result first."
4. **First-3-seconds fix:** "Describe exactly what should be on screen in seconds 0 to 3 for this reel."
5. **7-day plan:** "Make me a 7-day posting plan using only the patterns from my best reels. No guessing."

## The flop checklist: 10 ways reels die in 3 seconds
1. Logo or intro before the point
2. Result shown at the end instead of the start
3. Two lines of text fighting each other
4. Hook says "tips" instead of a specific outcome
5. Talking before anything moves on screen
6. Small text that's hard to read on a phone
7. Slow first cut (more than 2 seconds)
8. No reason to watch to the end
9. Topic too broad ("AI for business")
10. CTA before any value

Claude reads images (JPG, PNG, WebP) and CSV files, so screenshots are enough.'''),

dict(kw='ANIMATE', cat='content', mins=5, plan='Free Claude plan', reel=None,
  title='10 animations you can make with Claude for your reels',
  desc='Ten copy-paste prompts that make Claude build animated graphics you can screen-record for reels. Works on the free plan.',
  get=['10 ready animation prompts', 'Graphics you can drop into any reel', 'How to add sound and video on top'],
  tools=['claude', 'higgsfield', 'elevenlabs'], related='TELLS', pack='Content Engine',
  body='''Paste any prompt into Claude. It builds the animation as an artifact you can watch, tweak and screen-record. Works on the free plan.

**How to use:** swap the words in [brackets] for your business, then add "make it loop smoothly and fill a 9:16 vertical frame". Play it full screen and screen-record.

## 3 prompts to start with
```
Build a dark dashboard card animation: the label '[Monthly revenue]', a big number counting up from 0 to [RM 48,200], a green '▲ [312]%' badge, and a glowing line chart drawing left to right with a soft gradient fill and a white dot at the tip.
```
```
Build an isometric flow diagram: 4 blocks rise up in sequence, labelled [Comment → DM → Follow → Guide]. Glowing particles flow from block to block in a loop. Ice-blue and teal blocks, last block white, dark background.
```
```
Build a rotating wireframe globe on a near-black background. From [Kuala Lumpur], glowing arcs fly out one by one to [Singapore, Tokyo, London, Sydney]. Caption '[Kuala Lumpur → 7 markets]'. Slow rotation, cyan glow.
```

## The other 7 ideas
1. **Map route:** a glowing route drawing across a dark city map, with a delivery-time card.
2. **Headline:** a newspaper front page whose headline types itself in.
3. **Teardown:** an exploded view of a product, layers separating with labels.
4. **Agent swarm:** a grid of little robot tiles passing glowing work between them.
5. **Paper desk:** paper sheets landing on a desk, a red pen circling a line.
6. **Ink wash:** a Japanese ink landscape brushing itself in.
7. **Hologram:** a wireframe object rotating inside a projector beam.

All 10 full prompts are in the Google Doc guide (button below).

## Tips
- Say "slower", "more glow" or "use my brand colours [#hex]" to adjust.
- Ask for "a version with a transparent background" to put it over your own video.

## Make it a full reel
- **Sound:** add a music bed and whooshes with ElevenLabs. Sound is what makes motion graphics feel finished.
- **Real footage:** need actual video clips around the animation? Higgsfield's connector lets Claude generate them in the same chat.'''),

dict(kw='TELLS', cat='basics', mins=3, plan='Free Claude plan', reel='959fa53e-5b74-40cb-b62c-9a342b87468f',
  title='8 signs customers can tell AI made your website',
  desc='The 8 giveaways that make a website look AI-made, and one prompt that finds and fixes them.',
  get=['An 8-point checklist to run on your site', 'One prompt that finds every giveaway', 'A rewritten homepage in plain words'],
  tools=['claude'], related='ANIMATE', pack=None,
  body='''## The checklist
1. A purple or pink gradient everywhere
2. A stock photo of people laughing at a laptop
3. Emojis in every button (🚀 ✨ 💡)
4. Words like unlock, elevate, seamless, next-level, cutting-edge
5. Every card the same size with the same icon
6. The price buried three clicks deep
7. No WhatsApp or "message us" button
8. It breaks on a phone (text cut off, sideways scrolling)

## The fix prompt
```
Here is my website: [link or paste the text].
Find every sign it was made by AI (generic gradients, stock-photo feel, emoji buttons, buzzwords like unlock/elevate/seamless, identical cards, hidden prices, no WhatsApp button, mobile problems).
List each one with the exact place it appears.
Then rewrite the homepage for a real local business: plain words a customer would actually say, the price visible, one clear WhatsApp button, and real photos suggested instead of stock.
```

## Tips
- Open your site on your own phone before and after. Most customers will see it there.
- Replace stock photos with real ones of your counter, your team or your product, even phone photos.'''),

dict(kw='SETUP', cat='basics', mins=4, plan='Some steps need a paid plan', reel=None,
  title='5 Claude settings to switch on today',
  desc='Skills, plugins, Claude in Chrome, scheduled tasks and artifacts: the 5 Claude settings most people skip, and which plan each needs.',
  get=['The 5 settings in the right order', 'Which plan each one needs', '3 prompts to try straight away'],
  tools=['claude'], related='PROJECT', pack=None,
  body='''Do them in this order.

## 1. Skills (all plans, Free included)
Teach Claude a job once and it does it your way every time. Path: Customize → Skills. Needs code execution on (Settings → Capabilities). Starter ideas: quote writer, caption writer, reply-in-my-voice.

## 2. Plugins (paid plans)
One click adds a bundle of skills and app connections for a type of work. Path: Customize → Plugins → Discover → Add.

## 3. Claude in Chrome (paid plans, Chrome only)
Sits beside the page you're on: fills forms, updates sheets, compares prices. Don't let it handle payments or logins you aren't watching.

## 4. Scheduled tasks (paid plans)
"Every weekday at 8, send me today's orders and enquiries." Runs in the cloud, laptop shut.

## 5. Artifacts (all plans; public link sharing on paid plans)
Ask for a price calculator, stock tracker, booking form or quote builder and Claude builds a working tool next to the chat.

## Prompts to try
```
Build me a price calculator for [product] with box sizes and delivery.
```
```
Make a skill that writes my quotes in this format: [paste one].
```
```
Every Monday at 9, summarise last week's enquiries from [source].
```

Plans and features change. Check Anthropic's help pages for the latest.'''),

dict(kw='PRIVACY', cat='basics', mins=3, plan='Any Claude plan', reel=None,
  title='Claude privacy checklist: lock down shared chats in 2 minutes',
  desc='Some shared Claude chats showed up in Google. Here is the 2-minute fix and the full privacy checklist.',
  get=['A 2-minute fix to do today', 'A 9-point monthly checklist', 'What to do if something is already public'],
  tools=['claude'], related='SETUP', pack=None,
  body='''In July 2026, some Claude chats showed up in Google search results. Every one of them was a chat someone had shared with a public link. Chats that were never shared were not exposed.

## What that means
- Sharing a chat creates a **public link**. Anyone with the link can open it.
- A shared link stays live until you turn it off. Turning it off kills the link, but it can't delete copies or screenshots people already made.

## The 2-minute fix
1. **Turn off shares from the chat.** Open any chat you've shared, tap **Share**, set it back to **Private**.
2. **Check everything you've ever shared.** Settings → Privacy → Shared chats. Turn off anything you don't need public.
3. **Keep sensitive details out of shareable chats.** No passwords, IC numbers, bank details, phone numbers or client information.

## The full checklist
1. Review your shared chats once a month.
2. Check your published artifacts too, and unpublish the ones you don't need.
3. Share a clean copy, not the original working chat.
4. Re-read the whole chat before you hit Share, uploaded files included.
5. Never paste passwords or API keys into any chat. If you already did, change them now.
6. Use an incognito chat for one-off sensitive questions.
7. In Settings → Privacy, set how your chats are used the way you want.
8. Search for yourself: Google *site:claude.ai/share "your business name"*.
9. Client work? Strip names and details first, or get their OK.

## If something is already out there
- Turn the share off first.
- Change any password, key or code that appeared in the chat.
- Once the link is dead, ask Google to refresh the result with its "Remove outdated content" tool.'''),

dict(kw='CLEAR', cat='business', mins=2, plan='Free Claude plan', reel='a1b4e0cf-c9ea-4935-9a47-da1d97116402',
  title='Write SOPs nobody can misread (the aircraft-manual trick)',
  desc='Aircraft manuals use Simplified Technical English so nobody misreads a step. One prompt rewrites your SOPs the same way.',
  get=['One prompt that rewrites any SOP', 'One action per step, numbered', 'Instructions a new hire can follow on day one'],
  tools=['claude'], related='TRAIN', pack='Ops Engine',
  body='''Aircraft maintenance manuals are written in **Simplified Technical English** (the standard is called ASD-STE100): short sentences, one action per step, and words that each have only one meaning. Andrej Karpathy suggested telling AI to write this way.

## The prompt
```
Rewrite this SOP following ASD-STE100 (Simplified Technical English), about 80% of the way.
- One action per step, numbered.
- Short sentences. Use the active voice.
- Use one word for one meaning, every time.
- Put warnings before the step they apply to.
Keep every step that matters. Do not add new steps.

[paste your SOP here]
```

## Tips
- Works for opening and closing checklists, posting routines, packing orders, refunds, or anything a new staff member does.
- Print the result and let a new hire try it. Every question they ask shows you a step to fix.
- "80% of the way" keeps it readable. 100% strict can sound robotic.'''),

dict(kw='TRAIN', cat='business', mins=4, plan='Free plan to build, paid to share by link', reel=None,
  title='Turn your staff handbook into a training game',
  desc='Photograph your staff handbook and Claude turns it into a phone game with flashcards, order-building and a checklist quiz.',
  get=['A training game that works on a phone', 'Flashcards, order-building and a checklist quiz', 'A results screen showing what staff miss most'],
  tools=['claude'], related='CLEAR', pack='Ops Engine',
  body='''Takes about 10 minutes.

## 1. Photograph your pages
Pick 3 to 5 pages new staff must learn: menu and prices, recipes, the opening or closing checklist. Shoot them flat, in daylight, no glare. Claude reads JPEG, PNG and PDF, up to 20 files per chat.

## 2. Paste this prompt with the photos
```
These are pages from our staff handbook. Turn them into a training game for new staff that works on a phone. Include: (1) flashcards for every product and price, (2) a 'build the order' game for the recipes, (3) a quiz on the checklist. Any wrong answer comes back later until they get it right. Give stars for each round. At the end, show a results screen listing the questions they missed most. Keep it simple, big buttons, our shop name at the top.
```

## 3. Game types that work for any shop
- **Flashcards:** products, prices, stock codes, service menu.
- **Build the order:** recipes, packing steps, a service routine.
- **Checklist quiz:** opening, closing, hygiene and safety steps.

## 4. Sharing it with staff
- Claude builds the game as an artifact. Artifacts are on every plan, including Free.
- Sharing by link with "anyone" needs a paid Claude plan. Check what staff see when they open it; they may need to sign in.
- Results show within one play session. Saving scores across days needs a paid plan.'''),

dict(kw='PRICE', cat='business', mins=5, plan='Claude Code (paid) or no-code', reel='ad4a1e74-3115-40ed-b687-482ff7449c2a',
  title='Track competitor prices automatically with Claude',
  desc='Get a weekly message when a competitor changes prices. Two routes: Claude Code with a free tool, or a no-code scraper.',
  get=["Every item and price from a competitor's public page", 'A weekly message showing only what changed', 'A setup you do once and forget'],
  tools=['claude', 'apify'], related='ASK', pack='Ops Engine',
  body='''In our demo, the shop next door cut its kopi ais from RM6.50 to RM4.90, and the owner found out 21 days later. A weekly check would have flagged it within a week. *(Demo shop, not a real one.)*

## Route A: Claude Code (techy, free tool)
You need Claude Code (paid Claude plan) and **Reverse API Engineer**, free and open source (MIT licence) on GitHub: kalil0321/reverse-api-engineer.
1. Install it: `uv tool install reverse-api-engineer` (follow its README if your setup differs).
2. Open the competitor's **public** price page and let the tool watch how the page loads its prices.
3. Ask Claude Code: *"Turn this into a small script that fetches every item name and price from this page and saves them to prices.csv."*
4. Run it once and check the prices match the page.
5. Make it weekly with the prompt below.
```
Every Monday at 9am, run the script, compare with last week, and tell me any item that changed price, with the % change.
```

## Route B: no code with Apify
1. Create a free Apify account and pick a ready-made scraper for the kind of site (online store, delivery app listing and so on).
2. Paste the competitor's public page, run it once and download the results.
3. Set a weekly schedule in Apify.
4. Upload this week's and last week's file to Claude and paste the prompt below.
```
Compare these two price lists. Show only the items that changed, with the old price, new price and % change.
```

## Play it fair
- Only public pages anyone can see without logging in.
- Respect each site's terms of use. Once a week is plenty.
- Never collect personal data or anything behind a login.'''),

dict(kw='INVOICE', cat='business', mins=5, plan='Paid Claude plan', reel=None,
  title='Let Claude chase your unpaid invoices every morning',
  desc='A scheduled Claude task checks your invoice sheet and drafts polite payment reminders in Gmail. Nothing sends without you.',
  get=['A daily list of overdue invoices', 'Reminder drafts in your tone, ready in Gmail', 'Nothing sent without your OK'],
  tools=['claude'], related='CLEAR', pack='Ops Engine',
  body='''Every morning Claude checks your invoice sheet, finds anything overdue and drafts a polite reminder for each customer. You read the drafts and hit send. Setup takes about 10 minutes.

## What you need
- A paid Claude plan (scheduled tasks are on all paid plans).
- The Google Drive and Gmail connectors turned on (Settings → Connectors).
- One Google Sheet called **Invoices** with the columns: Invoice no · Customer · Email · Amount · Issued · Due date · Paid? (Yes/No).

## Step 1: test the prompt once by hand
```
Open my Google Sheet called "Invoices". Find every row where Paid? is "No" and the due date is before today. For each one, work out how many days overdue it is.
1 to 7 days late: a short, friendly nudge. Assume they forgot.
8 to 13 days late: polite but clear. Mention the invoice number, amount and due date.
14+ days late: firmer. Restate the amount and due date and ask them to reply with a payment date.
Write like me: [YOUR TONE]. Sign off as [YOUR NAME, BUSINESS]. Payment details: [BANK / PAYMENT LINK].
Before drafting, check my Gmail Sent folder and skip anyone I've already emailed about that invoice in the last 3 days.
Create each reminder as a Gmail DRAFT addressed to the customer, subject "Reminder: Invoice [no]". Do not send anything. Then give me a short summary: who is overdue, by how many days, the total outstanding, and which drafts are ready.
```

## Step 2: put it on a schedule
1. In Claude, click **Scheduled** in the left sidebar, then **New task**.
2. Name it "Invoice reminders", paste your final prompt, choose **Daily** or **Weekdays**, and save.

Shortcut: in a chat where the prompt already worked, type **/schedule**.

## Watch out for
- It runs in the cloud, even when your computer is off.
- Keep the sheet up to date. A paid invoice still marked "No" gets a draft, which you'll catch because it's only a draft.
- Keep it as drafts. Don't let any AI send money emails without you reading them first.'''),

dict(kw='PDF', cat='business', mins=4, plan='Free tool, Python needed', reel=None,
  title='Stop dragging PDFs into Claude: save tokens with MarkItDown',
  desc='Claude reads every PDF page as text and as an image. Convert to Markdown first with Microsoft MarkItDown and use far fewer tokens.',
  get=['Lighter files that stretch your usage limit', 'A one-line convert command', 'When to keep the PDF instead'],
  tools=['claude'], related='PROJECT', pack=None,
  body='''When you drop a PDF into Claude, it reads every page as text and as a picture. Great when the layout matters, wasteful when you only need the words. Claude's docs put each PDF page at roughly 1,500 to 3,000 tokens of text, plus the image.

## Option 1: convert it yourself
**MarkItDown** is a free, open-source tool from Microsoft that turns PDF, Word, PowerPoint and Excel files into clean Markdown.
1. Install it (Python 3.10 or newer): `pip install 'markitdown[all]'`
2. Convert: `markitdown report.pdf -o report.md`
3. Attach report.md to Claude instead of the PDF.

## Option 2: let Claude convert files itself
In Claude Code:
```
pip install markitdown-mcp
claude mcp add markitdown -- markitdown-mcp
```
Then ask: *"Convert ~/Downloads/report.pdf to Markdown and give me the 5 key points."*

## When to keep the PDF
- Charts, tables and diagrams where the picture carries the meaning.
- Designed documents where layout matters.
- Scanned PDFs (photos of paper) have no text layer, so there's nothing to convert.

## More token savers
- Send only the pages you need.
- Convert once and keep the .md file in a Claude Project.
- Ask for a 1-page summary file and reuse that next time.'''),

dict(kw='LOGO', cat='business', mins=5, plan='Claude Code (paid plan)', reel=None,
  title='Get 6 real logo ideas from Claude, not a coffee cup',
  desc='A free Claude Code skill that gives 6 different logo directions as editable SVGs, with the reasoning behind each.',
  get=['6 logo directions as editable SVG files', 'A one-line reason for each', 'A brief that avoids the obvious icon'],
  tools=['claude', 'higgsfield'], related='TELLS', pack=None,
  body='''Ask most AI tools for a logo and you get the obvious icon: a cup for a café, a tooth for a dentist. **Logo Generator** is a free, open-source Claude Code skill by op7418 (MIT licence) that asks about your business first, then gives you 6 directions as editable SVGs, PNG exports and a showcase page to compare them.

## What you need
- Claude Code (included with Claude Pro and above) and Python 3.8 or newer.
- Optional, for mockup images only: a Gemini API key from Google AI Studio.

## Install it (5 minutes)
```
npx skills add https://github.com/op7418/logo-generator-skill.git
cd ~/.claude/skills/logo-generator
pip install -r requirements.txt
```
Restart Claude Code and type `/logo-generator` to check it's there. Keep any API key in the .env file, never in a chat.

## The brief
```
Create a logo for [NAME], a [WHAT YOU DO] in [CITY]. My customers are [WHO]. The one feeling I want people to get is [FEELING]. Style: [MINIMAL or BOLD], [WARM or COOL] colours. Avoid the obvious icons for my industry, like [CLICHÉ]. Give me 6 genuinely different directions with one line of reasoning each. It must still read clearly at small sizes, like a profile picture.
```

## Pick and polish
1. Open the showcase page and shortlist 2. Look at them tiny and big.
2. Ask for changes in plain words: "Make option 3 thicker so it works at 32px."
3. Export: "Export the logo as PNG at 2048x2048, with and without background." Keep the SVG as your master.

## Mockups without a Gemini key
Want to see the logo on a shopfront, cup or tote bag? Higgsfield's connector can generate mockup images inside Claude.

## Watch out for
- Check it's not too close to an existing brand. In Malaysia, search MyIPO before you print anything.
- Treat the 6 ideas as round one, then refine.'''),
]
