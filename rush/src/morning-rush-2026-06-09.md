# THE MORNING RUSH

*A short brief on AI in medicine — and the world it's moving through. Read it before the 8am phone lines open.*

**Tuesday 9 June 2026 · ~5 min read · Issue 042**

---

**On the line today:** NHS England has signed off the biggest single AI deployment in any health system on earth — **Microsoft 365 Copilot for 505,000 staff** — on the strength of a "43 minutes saved a day" trial. On the very same week, a **21-model study from Mass General Brigham** quietly reminds us that even GPT-5 and Grok still flunk the differential-diagnosis stage of clinical reasoning four times out of five. A new legal teardown of **scribe contracts** finds vendors quietly reserving the right to train on patient audio, with the indemnity left deliberately vague. On the broader beat, **Google I/O** ushered in the "agentic era" with Gemini 3.5, and a plague of **deepfake doctors** is now selling miracle cures in the likeness of real, named physicians. Plus *From the Eye* — the GP "wild west", a watermark everyone suddenly wants, and Anthropic quietly passing OpenAI.

---

## 1. NHS England puts Copilot on half a million desktops

NHS England confirmed this week that it will roll out **Microsoft 365 Copilot to roughly 505,000 clinicians and support staff** from July — onboarding 200,000 in the first six months. It is, by a distance, the largest deployment of generative AI in any national health service. The business case rests on a 2025 trial across University Hospitals Birmingham, Guy's and St Thomas', and Manchester that measured **43 minutes of admin saved per person per day**. Data is pinned to UK Azure regions, with contractual promises that NHS material won't be used to train Microsoft's models.

**The view from the surgery:** Forty-three minutes is a real number and admin is a real misery, so I won't sneer. But "saved per day per clinician" is the sort of figure that survives a press release and rarely survives a year of frontline use — measured against curated tasks, in motivated pilot sites, before scale exposed every edge case. The governance terms are the right ones to have insisted on. The open question is the one no rollout answers: who checks that 505,000 people actually use it safely, and who notices when they don't.

---

## 2. Twenty-one models, and not one ready to reason unsupervised

Researchers at Mass General Brigham's MESH Incubator ran 21 general-purpose models — the latest ChatGPT, Claude, Gemini, DeepSeek and Grok — through 29 published clinical cases. Given the full picture, all landed the **correct final diagnosis over 90%** of the time. But at the earlier, harder step — building an appropriate **differential** from incomplete information — **every single model failed more than 80%** of the time. Their new PrIME-LLM score, which grades the whole reasoning arc rather than just the endpoint, topped out at 78% (Grok 4 and GPT-5). Corresponding author Marc Succi's verdict: "not ready for unsupervised clinical-grade deployment."

**Why it matters:** Hold this beside item one. We're handing AItools to half a million staff in the same month a careful study shows the best models can ace the exam answer while fumbling the actual thinking that gets you there. That's not an argument against the tools — it's the precise shape of their danger. They're strongest exactly where we're tempted to trust them (tidy final answers) and weakest where medicine actually lives (the messy front end, deciding what to worry about). Keep the human firmly in the loop, especially the junior one still learning to reason.

---

## 3. The scribe contract you didn't read reserves the right to keep your audio

A legal analysis of real ambient-scribe vendor contracts (Foley & Lardner) found a recurring set of problems hiding in the small print: **missing data-processing terms, deliberately vague indemnity clauses, and provisions letting the vendor train its AI on patient audio and transcripts.** The medico-legal sting is subtler. Once a consultation is recorded, that recording becomes "proof of all that was or was not said" — and the moment the transcript and the signed note diverge, you have manufactured your own contradiction for any future complaint.

**The view:** Every GP eyeing a scribe should ask three blunt questions before signing: does the recording get destroyed, who is liable when the note is wrong, and can the supplier mine my patients' voices to improve its product. If the salesperson waffles on any of them, that's your answer. The time saved is genuine; the liability is being quietly transferred to the clinician who signs the note, and the contract is where that transfer happens.

---

## 4. Google declares the "agentic era" — Gemini stops assisting and starts acting

At I/O this week Google unveiled **Gemini 3.5 Flash** and **Gemini Omni**, framing 2026 as the year AI shifts "from assistants to agents" — software that navigates whole workflows on its own rather than answering one prompt at a time. The Flash model claims flagship-level intelligence at budget speed and beats last quarter's Pro on coding and agentic benchmarks. Google also upgraded its agent-building platform, Antigravity, for orchestrating fleets of these things.

**Why it matters:** "Agentic" is the word to watch this year, and it should make health IT nervous in a useful way. An assistant that drafts a letter you check is one risk profile; an agent that books the test, orders the drug and updates the record on its own is another entirely. The clinical-AI tools heading for the NHS sit downstream of exactly this design shift. Before any of it touches a patient pathway, the question is no longer "is the answer right" but "what did it do while I wasn't looking, and can I undo it".

---

## 5. Deepfake doctors are now a public-health problem in their own right

Investigators have catalogued **dozens of accounts and 100-plus AI-generated videos** on TikTok and Instagram in which fabricated "doctors" — and, increasingly, the cloned faces of real, named physicians — flog weight-loss and wellness scams to audiences in the millions. One US doctor, Joel Bervell, found himself deepfaked last week promoting products he'd never heard of. The American Medical Association is now pressing legislators to modernise identity protections and force platforms to pull impersonations faster.

**The view from the surgery:** This is the consumer-facing edge of the same technology we're welcoming through the back door, and it lands squarely in our waiting rooms. The patient who arrives convinced by a confident "GP" on their phone is now arriving convinced by a synthetic one wearing a borrowed face. Worth a gentle word in consultations: a doctor in a 30-second reel selling a supplement is, almost by definition, not your doctor.

---

### From the Eye

Three the front pages didn't run. **Item one** — the RCGP's own data shows **more than one in four GPs (28%)** already using AI at work, with no consistent national guidance and no formal training — a "wild west" of clinical-note, referral and triage tools, with the promised regulatory framework still somewhere over the horizon. The deployment headlines are all top-down; the actual adoption is bottom-up and unsupervised, which is the opposite order from how you'd want safety to arrive. **Item two** — quietly, **OpenAI, Kakao and ElevenLabs have all adopted Google's SynthID watermark** for AI-generated content. A shared provenance standard across rival labs is the kind of plumbing that matters more than any model launch — it's the difference between a future where you can tell what a machine made and one where you can't, and it's being built with almost no fanfare. **Item three** — lost under the I/O noise, **Anthropic has passed OpenAI** as the world's most valuable AI firm, raising at a **$965bn** valuation on a reported **$47bn run-rate**. Remember that the clinical tools the NHS is buying ride on these platforms — and when the people who set the token prices are valued near a trillion dollars before they've turned a profit, "efficiency savings" is a phrase worth reading twice.

---

*The Morning Rush. Reply with what works, what doesn't, and what should be on tomorrow's front page.*

**Sources monitored:** NHS England · Digital Health · BMJ · Pulse · STAT News · *Exponential View* · *The AI Daily Brief* · *Private Eye* (MD column) · *The Parnas Perspective* · European Commission · Stanford HAI · The Lancet · HSJ · RCGP · Mass General Brigham
