# THE MORNING RUSH

*A short brief on AI in medicine — and the world it's moving through. Read it before the 8am phone lines open.*

**Sunday 17 May 2026 · ~5 min read · Issue 019**

---

**On the line today:** A King's College London survey lands the most quotable UK number of the spring — one in seven adults have now used an AI chatbot instead of contacting a GP, and a fifth of those say the bot actively talked them out of seeing one. *NEJM AI* publishes the first hard randomised number for automation bias: physicians given erroneous LLM suggestions drop fourteen percentage points on diagnostic accuracy, with AI-literacy training making no measurable difference. Rotherham NHS Foundation Trust quietly proves the unglamorous AI use case works — 28% off the IT helpdesk in three months. Microsoft's MDASH, a hundred-agent harness pointed at its own source code, finds sixteen new Windows vulnerabilities including four critical RCEs. And Trump publicly reverses himself on federal AI regulation, citing Anthropic's Mythos by name. Plus *From the Eye* — Sweden's fake-disease sting on the chatbots, Aaron Parnas builds his counter-misinformation engine, and Eli Lilly switches on the first pharmaceutical AI supercomputer.

---

## 1. King's College London puts a number on the GP-to-GPT switch

A nationally representative poll of **2,000 UK adults** published last week by **King's College London's Policy Institute** with Ipsos finds **one in seven (15%)** have used an AI chatbot **instead of contacting a doctor or NHS service**, and **one in ten** have done the same for mental health support. Of those who consulted an AI, **20% say the chatbot did not encourage them to seek a professional opinion** and **21% actively decided against** seeing a clinician on the back of what the bot told them. The accidental punchline: the public estimate that **39% of UK GPs already use AI in clinical decision-making**. The actual figure, per the RCGP's own member survey, is **8%**.

**The view from the surgery:** This is the most useful UK data point on AI-in-primary-care to land all year, and it changes the conversation in a quiet way. The argument has been about whether to allow AI into the consulting room; the data says it has already entered the patient's home, with consent from no one and oversight from nothing. The 21% who declined to seek care are not a hypothetical — they are people we won't see, with conditions we won't diagnose. The right answer is not a leaflet about ChatGPT's limitations. It is to acknowledge that we are now the second-opinion service and to position ourselves accordingly.

---

## 2. *NEJM AI* lands the first hard number on automation bias

A randomised trial published in **NEJM AI** by Akshay Bhuller and colleagues at Beth Israel Deaconess put **44 physicians**, all formally AI-literacy-trained, through **264 diagnostic cases** with optional LLM consultation. The control arm averaged **84.9% accuracy**. The arm exposed to **deliberately erroneous LLM suggestions** dropped to **73.3%** — an adjusted **14-percentage-point fall**. The drop held even when the doctor had explicitly questioned the AI's reasoning before deferring to it. The authors' bottom line, in plain English: voluntary use and prior training did not protect against automation bias.

**Why it matters:** This is the first peer-reviewed clinical RCT to quantify what every GP suspects happens in the five-minute consult — that once the screen has produced a plausible answer, the brain quietly stops looking for the missing piece. The number is large enough to matter regulatorily. If the MHRA's incoming Software-as-a-Medical-Device pathway leans on "human in the loop" as a safety claim, this paper is the inconvenient evidence that the loop closes the wrong way under time pressure. Expect citations in the next BMA briefing on AI scribe contracts.

---

## 3. Rotherham proves the boring AI case works

**Rotherham NHS Foundation Trust** reported on **15 May** that the AI voice agent it deployed on Netcall's Liberty Converse platform has **cut IT helpdesk call volumes by 28%** since launch, with **41% of queries now self-served**. The trust has costed avoided downtime separately and is preparing a phase-two rollout to out-of-hours support for clinical-system password resets and printer faults — the unromantic 3am calls that pull a duty technician away from a real incident.

**The view:** The healthcare-AI conversation is dominated by ambient scribes, diagnostic models and chatbot triage — high-stakes, high-headline. The bigger near-term efficiency is sitting on every trust's internal helpdesk and switchboard. Rotherham's 28% is not a moonshot; it is a procurement decision and a six-week training cycle. The contrast with the trusts spending eighteen months piloting a £1m AI radiology tool that delivers a 4% gain is becoming embarrassing. Worth showing this to your CCG/ICB analytics lead this week.

---

## 4. Microsoft turns a hundred agents on its own code — and finds sixteen new Windows holes

Microsoft Security disclosed on **12 May** that its **MDASH** ("multi-model agentic scanning harness") found **16 previously unknown vulnerabilities** in Windows networking and authentication components — **four of them critical remote-code-execution flaws** — all patched in this month's Patch Tuesday. MDASH orchestrates **more than 100 specialised AI agents** across frontier and distilled models that "discover, debate, and prove" exploitable bugs end-to-end. On Microsoft's published planted-bug test it found **21 of 21 with zero false positives**, and scored **88.45% on the CyberGym public benchmark** — about five points above the next entry. Enterprise preview opens in June.

**Why it matters:** This is the first major-vendor demonstration that agentic AI applied to defensive cyber is producing real-world findings at scale — and a useful counterweight to Anthropic's parallel offensive-Mythos warning. NHS Digital and the NCSC will be reading the technical paper carefully; the trust IT teams running unsupported Windows estates rather less carefully. The honest read is that AI is now on both sides of the cyber arms race, with the defenders briefly ahead — for the first time in a decade.

---

## 5. Trump pivots on AI regulation — and names Mythos as the reason

NPR reported on **14 May** that the White House has shifted line on federal AI regulation, with Trump telling reporters on Wednesday that "there should be regulations on AI" — a clean reversal from December's Executive Order 14365 directing the AG to sue states pushing their own. The proximate cause, per two senior officials, is **Anthropic's Mythos preview**, the cyber-offensive frontier model Dario Amodei has refused to release outside a hand-picked forty-organisation "Glasswing" cohort. CASI (the rebadged AI Safety Institute) is now being asked to draft federal evaluation standards by end-Q3.

**The view from the surgery:** The wider point for UK readers is that an American federal floor on frontier-model regulation, if it actually arrives, changes the calculus on the **MHRA's International Reliance Framework** due in the autumn. The "we'll just import US standards" shortcut becomes much more defensible if the US has standards worth importing. Until then, the Atlantic regulatory drift continues in our favour — but very slowly.

---

### From the Eye

Three the bigger papers undersold. **Sweden's bixonimania sting** — University of Gothenburg researchers uploaded two preprints describing a wholly invented eye condition ("eyelid discoloration from blue light"), authored by fictional academics at the equally fictional Asteria Horizon University; ChatGPT, Gemini, Copilot and Perplexity all proceeded to brief patients on its prevalence and recommend specialist referral, and one peer-reviewed Cureus paper cited it before retraction. The meta-finding, buried in the *Nature* write-up: LLMs are markedly more credulous when the input "looks medical" — formatted like a discharge summary or a clinical paper. **Aaron Parnas**, the *Parnas Perspective* political-news Substacker, trailed a new **AI-misinformation counter-platform** to launch next week, after his own team was repeatedly targeted by AI-generated impersonation video this spring; the architecture leans on watermark-detection plus rapid-response fact-checking, and is being pitched to local US election officials before the November midterms. Worth tracking whether the BBC Verify team picks it up. And **Eli Lilly switched on "LillyPod"** on **13 May** — billed as the world's first pharmaceutical AI supercomputer, an NVIDIA DGX SuperPOD with B300 systems, dedicated to drug-discovery, genomics and clinical-development workflows. The headline is the hardware. The buried detail is that Lilly is paying NVIDIA directly rather than via AWS or Azure — the first hyperscaler-bypass deal in big pharma. The cloud middlemen will not have missed it.

---

*The Morning Rush. Reply with what works, what doesn't, and what should be on tomorrow's front page.*

**Sources monitored:** NHS England · Digital Health · BMJ · Pulse · STAT News · *NEJM AI* · *The Lancet* · *Exponential View* · *The AI Daily Brief* · *Private Eye* (MD column) · *The Parnas Perspective* · King's College London · NPR · The Register · Microsoft Security · Nature
