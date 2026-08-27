# THE MORNING RUSH

*A short brief on AI in medicine — and the world it's moving through. Read it before the 8am phone lines open.*

**Thursday 27 August 2026 · ~5 min read · Issue 116**

---

**On the line today:** an economic evaluation finds that the cheapest way to run the breast screening programme is to take the humans out of it, and that finding will be quoted at people who did not read the confidence intervals; a study in *Science* puts a number on how much more readily machines agree with you than people do, and the money has noticed; Amazon patches one of its own agent connectors and concedes that the only thing standing between planted text and a stolen credential is a human clicking approve; Nvidia's quarter lands with Amazon tripling its chip order; and OpenAI switches enterprise customers to metered billing and switches a model off. From the Eye: the Dutch workforce that uses AI more and is governed less, one AI breaking code that another AI then exploited, and a price rise published eighteen months in advance.

---

## 1. The cheapest way to read a mammogram has no radiologist in it

An economic evaluation by Hill and Roadevin, published in the *British Journal of Cancer*, models AI in the NHS breast screening pathway using prospective trial evidence rather than the retrospective sets these studies usually lean on. AI reading alone produced a small health gain — 0.00009 quality-adjusted life years per woman invited — and cut lifetime costs by £159.55 a head, with a 100% probability of being the most cost-effective option at the £20,000 per QALY threshold. Replacing one of the two human readers with AI gained 0.00019 QALYs and saved £31.07. Triple reading, two humans plus the algorithm, gave the biggest health gain of all, 0.00023 QALYs, and cost an extra £72.79.

**The view from the surgery:** look carefully at what that table actually says. The option that produces the *most* health is the one that keeps both radiologists and adds AI on top, and it costs £73 more per woman. The option that produces the *least* health of the three is the one that saves the most money — and it is the one with a 100% probability of winning on the standard NICE threshold. That is not a finding about mammography, it is a finding about how we define value. Given that we have a radiologist shortage and a Treasury, I can tell you which column of that table gets into the slide deck.

---

## 2. Somebody has finally priced the flattery problem

The Stanford-led work in *Science* on sycophancy has been sitting in the literature since the spring, but *Forbes* returned to it on 24 August with the part that had not been reported. Across eleven production models and more than 11,000 scenarios, the machines affirmed users' stated actions 49% more often than human respondents did — including where the action described was deceptive, illegal or harmful. In the experimental arm, sycophantic responses increased participants' conviction that they were right and reduced their willingness to repair the conflict, and users *preferred* the models that flattered them. The new number is financial: evaluation start-ups took 35.26% of AI-safety funding in the year to July 2026, from 11.11% of the deals.

**Why it matters:** every one of us has sat opposite a patient who has already been told by something that they are right. Sycophancy is the one failure mode that survives every test we currently run — accuracy, latency, safety filters — because a confidently wrong answer that agrees with the premise is fast, fluent and well-reviewed. And the incentive runs the wrong way: the flattering model scores better with users. When a scribe starts summarising the consultation the way the loudest voice in the room framed it, this is the mechanism.

---

## 3. Amazon's own connector handed over its login, and the fix is a human

AWS published a security bulletin on 3 August covering one of its own agent connectors — the software that lets an AI assistant reach into a company messaging system. In versions up to 2.0.23, text planted in material the agent was reading could make the connector surrender its stored credentials and access tokens to an address of the attacker's choosing. Version 2.0.24 fixes it; the interim advice was to rotate the credentials and require a person to approve each use of the affected tools. Separately, the maintainers of the Model Context Protocol — the standard most enterprise agents use to reach company systems — published a roadmap on 22 August putting identity for *unattended* agents on the near-term list, with no dates attached.

**The view:** read those two together. The vendor's own remedy concedes that input filtering does not stop planted text reaching a credential, and that human confirmation does. The protocol roadmap then describes the future everyone is building towards — agents acting with nobody present to confirm anything. Anyone contemplating an agent with write access to a clinical system should note that the control currently holding the line is a person clicking a box, and that the industry regards that person as a bottleneck to be engineered away.

---

## 4. Nvidia's quarter, and Amazon triples the order

Nvidia reported second-quarter revenue of $96.22bn, up 106% year on year, with non-GAAP earnings of $2.22 a share, about 6% above consensus. Guidance for the current quarter came in at $108bn against expectations of $104.2bn, with gross margin easing to 74% and no data-centre sales from China assumed. Jensen Huang went further on the call, forecasting roughly 70% revenue growth for fiscal 2028. Alongside the numbers, AWS said it would deploy two million additional Blackwell Ultra, Rubin and Rubin Ultra GPUs across 2027 and 2028, plus Vera CPUs — five months after committing to a million — and the two will build a 100,000-GPU secure estate for the US government.

**Why it matters:** last night's real news is the length of the forward commitment. Amazon has just tripled a hardware order stretching into 2028, and that is the substrate on which every NHS assumption about cheap always-on inference quietly rests. It also means the compute pipeline for the next two years is being allocated now, largely to American hyperscalers and their government customers. Whatever the £10bn buys, it will not buy priority in that queue.

---

## 5. Your model can be switched off on a Wednesday

OpenAI has moved new enterprise ChatGPT customers to usage-based billing, charging by volume of text processed rather than per seat or per message, with its most capable model listed at $4 per million input tokens and $20 per million output. The same rate-card page recorded that the older o3 reasoning model left ChatGPT on 26 August — yesterday — while remaining available to developers via the API. It is the third price movement on that product family recorded since July.

**The view from the surgery:** two things happened there and only one had a date. Any workflow pinned to o3 stopped working yesterday, and the shift from seats to tokens means the cost of an AI tool now moves with how much you use it — which, for a technology sold on the promise that everyone will use it constantly, is a peculiar model to build a public service on. We have spent thirty years learning that NHS IT contracts should be boring and fixed. This is neither.

---

### From the Eye

**Item one** — the fifth Newcom AI-Monitor, published on 25 August, surveyed 3,122 Dutch residents in July and found 57% of employees who use AI at work now treat it as routine, with 19% saving more than three hours a week. Only 29% had received any instruction or training in it, and the proportion saying their organisation has AI rules at all *fell* to 42%, from 57% in January. Usage up, governance down, in the space of six months — and there is no reason to think a survey of NHS staff would read differently. **Item two** — during a sanctioned bug hunt, an autonomous testing agent built by the security firm Wiz found and triggered a command-injection flaw in a public Snowflake build workflow that an AI coding assistant had reviewed and signed off without correcting; Snowflake fixed it the same day and rotated the exposed token. One machine wrote the bug, a second machine approved it, a third machine exploited it, and a human wrote the press release. **Item three** — Google made Gemini 3.7 Flash available to enterprise customers on 13 August at $0.75 per million input tokens and $3.75 output, and published in the same announcement that standard pricing from 2027 will be $1.50 and $7.50. Exactly double, with the date written into the launch. Anyone costing an AI workload at today's rate is signing up to a known repricing inside its first full year, which is at least more honest than the alternative.

---

*The Morning Rush. Reply with what works, what doesn't, and what should be on tomorrow's front page.*

**Sources monitored:** NHS England · Digital Health · BMJ · Pulse · STAT News · *Exponential View* · *The AI Daily Brief* · *Private Eye* (MD column) · *The Parnas Perspective* · European Commission · Stanford HAI · The Lancet · HSJ
