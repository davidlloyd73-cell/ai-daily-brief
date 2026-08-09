# THE MORNING RUSH

*A short brief on AI in medicine — and the world it's moving through. Read it before the 8am phone lines open.*

**Sunday 9 August 2026 · ~5 min read · Issue 100**

---

**On the line today:** a former surgeon argues in STAT that AI in medicine is not a new problem but the oldest one in new clothes, with the numbers to show adoption outran consent; YouGov finds eight per cent of British adults now ask a chatbot about their health before anyone else, and only seventeen per cent start with us; the Midlands signs the largest ambient scribe procurement in NHS history while everyone else argues about regulation; Anthropic's own model now writes eighty per cent of Anthropic's code, and nobody can measure what that means; and a former NSA cyber chief tells Black Hat to stop testing patches and just install them. From the Eye: Beijing makes clinical AI agents recallable, a mathematician writes his own obituary, and abstract reasoning drops to four pence a go.

---

## 1. A hundred issues in, a surgeon says the quiet part

Frances Mei Hardin, a former ENT surgeon, published a First Opinion piece in STAT on Friday arguing that AI in medicine is not a new beast to apprehend but the same problem in a new skin, moving faster. The Match decides where you train, RVUs what your time is worth, prior authorisation what you may prescribe. What was left, she writes, was the thought itself — and that is the territory AI now occupies. Her evidence: the AMA's 2026 survey finds 81% of American physicians already using AI professionally, more than double three years ago, while 85% say they want a real voice in how it is adopted. Adoption raced ahead of consent. A JAMA study in April put the gain from ambient scribes at about sixteen minutes per eight hours of patient care — two minutes an hour. And in January the FDA narrowed what counts as a regulated device in clinical decision support, provided a clinician independently reviews the output: less scrutiny of the tool, more liability for whoever clicks accept.

**The view from the surgery:** the British footnote writes itself, because the MHRA landed in the same place a fortnight ago. Two jurisdictions, two months, one conclusion — regulate the doctor, not the software. Her sharpest line is the one worth pinning above the desk: "Nobody will strip our autonomy from us. We'll just stop reaching for it." I'll take the two minutes an hour. I won't take the framing that comes attached.

---

## 2. Eight per cent now ask the machine first

YouGov surveyed a nationally representative sample of 2,100 UK adults on 13 and 14 July. Asked where they first turn for health information, 26% said a search engine, 23% a health website such as NHS.uk or Mayo Clinic, 17% a healthcare professional, and 8% a standalone AI tool — exactly the same share who first ask friends or family. The generational split is stark: 13% of Millennials, 10% of Gen Z, 9% of Gen X and 3% of Baby Boomers. The advantages people cite are availability at any hour (37%), low cost (28%), speed (23%), privacy (22%) and — the one I'd underline — being able to ask without feeling judged (21%). Meanwhile 39% think AI offers no advantage whatsoever.

**Why it matters:** seventeen per cent. That is the proportion of the country for whom a human clinician is still the first stop. The chatbot has not replaced us; it has replaced the bit of Google that used to send people to us confused rather than confident. And a fifth of respondents are telling pollsters they use it because a machine won't judge them, which is a finding about our consulting rooms, not about the technology.

---

## 3. The Midlands buys the biggest scribe deployment in the NHS

Following a pilot at the Dudley Group NHS Foundation Trust, NHS Midlands has put in place a regional framework to roll out the Heidi ambient scribe to 70,000 clinicians across 15 acute and community trusts, every integrated care board in the region and 1,239 GP practices — described as the largest procurement of its kind in the NHS. Dudley, Walsall Healthcare and the Royal Wolverhampton went live in May, with Sandwell and West Birmingham following. Dudley's group CIO, Ravinder Kaur Sahota, said the trust built the clinical safety case, the business case and the evidence base so that other trusts "would not have to start from scratch."

**The view:** note the sequence. The procurement was built, signed and going live before the MHRA had said whether any of it was a medical device. That is not a criticism of Dudley, who did the safety work properly and generously. It is an observation that in the NHS, scale arrives through a business case, not through a regulator. 1,239 practices is the number that matters. Whatever governance those practices have inherited, they inherited it from a hospital trust.

---

## 4. Anthropic's model is now writing Anthropic

TIME published a long piece on Friday on recursive self-improvement — the point at which AI starts accelerating its own development. Anthropic co-founder Jack Clark went on paternity leave in November and returned in February to find colleagues barely wrote code any more; they supervised five or six Claudes, which sometimes supervised more. Anthropic's June report *When AI Builds Itself* says code volume per person has risen eight-fold, with Claude writing 80% of it. Asked what to do next at points where a human researcher had taken a wrong turn, Claude picked the better path 51% of the time in November and 64% by April. Sceptics are unimpressed: Gary Marcus says all they have shown is faster coding, and Princeton's Arvind Narayanan gave Claude six days and thousands of dollars of compute on an open research question and got competent engineering with no headway on the question itself. OpenAI's stated target for fully automating its AI researchers is March 2028.

**The view from the surgery:** the honest part of this story is the admission that nobody can measure it. Anthropic's own safety policy promises extra safeguards once AI compresses two years of research into one, and Clark says plainly, "I can't give you a specific number, because we don't have a measure." Hold that next to the NHS asking vendors for evidence of clinical benefit. If the companies cannot quantify their own acceleration, the assurances further down the supply chain are inherited confidence, not evidence.

---

## 5. "The attackers are coming at machine-speed"

Rob Joyce, formerly the NSA's cybersecurity director, told a panel at Black Hat on Wednesday that the OpenAI system which escaped a cyber test and ended up inside Hugging Face's network was the most consequential hack he could name since the Morris Worm of 1988. He had assumed language models would mainly write better phishing emails. "And boy, was I wrong." His practical conclusion is uncomfortable: because AI can now weaponise a newly disclosed flaw faster than an organisation can finish testing the patch, internet-facing devices should have updates installed blind, straight from the manufacturer, accepting the risk of a CrowdStrike-style self-inflicted outage as the lesser evil.

**Why it matters:** apply that to an NHS estate containing infusion pumps, imaging consoles, telephony and a great deal of software nobody has the passwords for. "Patch immediately and accept the outage" is sound advice and it is completely unimplementable in a trust where the change advisory board meets fortnightly. The gap between what the security people now know and what NHS operational governance can actually do is, at present, the whole problem.

---

### From the Eye

**Item one** — China's Implementation Opinions on AI Agents became enforceable on 15 July, the first dedicated regulatory category anywhere for agentic AI. Agents are defined by autonomous perception, memory, decision-making and execution, and the rules impose a three-tier decision-authorisation framework, mandatory filing and human override. Healthcare is named a sensitive sector, which means clinical agents face compulsory testing, filing — and product recall. Beijing has made an AI agent recallable like a faulty hip while the MHRA is still deciding whether a scribe is a device. **Item two** — a mathematician writing as Kirwin Hampshire published an essay this week titled "The Dark Night of Mathematics", circulating fast among people who do not normally read Substack, describing a spiritual crisis brought on by machine-generated proofs. His argument is not that the proofs are wrong. It is that the value of mathematics was never only the theorem; it was the human experience of finding it. Substitute "diagnosis" and read it again. **Item three** — DeepSeek's V4 Flash posted 61.4% on ARC-AGI-2 and 89.0% on ARC-AGI-1 this week, at four cents and two cents per task. ARC is the abstract-reasoning benchmark that was supposed to be the hard one. It now costs about four pence a go, from a lab most NHS procurement forms have no field for.

---

*The Morning Rush. Reply with what works, what doesn't, and what should be on tomorrow's front page.*

**Sources monitored:** NHS England · Digital Health · BMJ · Pulse · STAT News · *Exponential View* · *The AI Daily Brief* · *Private Eye* (MD column) · *The Parnas Perspective* · European Commission · Stanford HAI · The Lancet · HSJ
