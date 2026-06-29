# THE MORNING RUSH

*A short brief on AI in medicine — and the world it's moving through. Read it before the 8am phone lines open.*

**Wednesday 20 May 2026 · ~5 min read · Issue 022**

---

**On the line today:** NHS Shared Business Services puts £900m on the table for an eight-year national AI procurement framework — the biggest single signal yet on where the money is heading. Google uses I/O 2026 to unveil Gemini Spark, then trips immediately over its own healthcare disclaimer. NHS England quietly flips hundreds of public GitHub repos to private, naming Anthropic's mysterious "Mythos" model as the proximate worry. The RCPsych and NHSE announce joint ambient-voice guidance for mental health, learning disability and neurodivergent patients. And OpenAI ties up with Dell to put Codex on-prem — quietly answering a question the NHS has not been brave enough to ask out loud. Plus *From the Eye* — the Mythos name surfacing in policy, the public's wildly inflated mental model of GP AI use, and Azeem Azhar's compute-crunch piece.

---

## 1. NHS SBS opens £900m, eight-year AI procurement framework

**NHS Shared Business Services** has opened tenders for a new **Healthcare AI Solutions** framework worth **£900m including VAT**, running from **May 2027 to May 2035**. Published on **11 May** and entering its supplier-call phase this week, it covers **eight lots** — radiology and diagnostic imaging, early detection, virtual and robotic health, predictive analytics, research, and advisory services among them. Submission deadline is **23 June**, awards in **March 2027**. SMEs are explicitly invited; the framework is open to wider public sector use.

**Why it matters:** This is the procurement infrastructure on which actual NHS AI spending will sit for the next eight years — not a press release. It will determine who can sell into ICBs without a fresh tender, which sets defaults for years. Worth a careful read for anyone on a PCN or trust digital board; this is where the supplier shortlist for your 2028 procurement is being drawn now.

---

## 2. Google I/O — Gemini Spark launches, then warns you not to use it for medicine

At yesterday's **Google I/O**, Sundar Pichai unveiled **Gemini Spark**, an always-on agentic assistant built on the new **Gemini 3.5 Flash** model. Spark runs in the cloud and is pitched for "long-horizon tasks with minimal oversight" — monitoring credit card charges, drafting Gmail follow-ups, tracking your child's school updates. Beta for **Google AI Ultra** subscribers from next week. Tucked into the small print, Google instructs users to **"not rely on it for medical advice, legal, financial, or other professional help."**

**The view from the surgery:** The disclaimer is interesting because consumer behaviour has comprehensively ignored every previous version of it. Spark also reads Gmail by default — the first agentic system most patients will use that quietly correlates appointment letters, prescription notifications and symptom searches. Worth being aware of when discussing online health-information habits, particularly in the over-50s cohort, which is where adoption will land hardest.

---

## 3. NHS England pulls public GitHub repos behind a curtain — citing Anthropic's "Mythos"

**NHS England** has ordered all its technology teams to flip **public GitHub repositories to private by 11 May**, with exceptions requiring explicit Engineering Board approval. The reason given, in internal guidance seen by *Digital Health News*, is "**rapid advancements in AI models capable of large-scale code ingestion, inference, and reasoning (e.g. developments such as the Mythos model).**" Mythos is understood to be an unreleased Anthropic system briefed to cyber-security agencies as capable of reverse-engineering production code at scale. NHSE calls the move temporary.

**The view:** A real reversal of the long-standing "code built with public money should be reusable" policy. The point is not the policy itself — it is what NHSE has been told about the threat surface. If the assessment is that frontier models can read your code and find vulnerabilities faster than you can patch them, expect that logic to propagate well beyond GitHub when the autumn cyber assurance framework lands.

---

## 4. RCPsych and NHSE develop joint ambient-voice guidance for mental health settings

The **Royal College of Psychiatrists** and **NHS England** confirmed on **6 May** they are co-developing **dedicated guidance on ambient voice technology** for use in mental health, learning disability and neurodivergent populations, with publication by **September 2026**. The drafting group sits at RCPsych; existing NHSE scribe guidance (April 2026) does not adequately cover capacity, consent under fluctuating insight, or the privacy sensitivities of recording therapeutic dialogue.

**Why it matters:** The first college-led carve-out from the general ambient-scribe consensus, and a sensible one. The *BJPsych Bulletin* proof-of-concept work last year was promising on documentation efficiency but flagged exactly these consent and trust questions. If your practice covers safeguarding-vulnerable adults — frail elderly, dementia, learning disability — read the September document in full; the principles will travel into general practice quickly.

---

## 5. OpenAI–Dell partnership puts Codex on-prem — the NHS hosting question, answered for them

**OpenAI** and **Dell** confirmed on **19 May** that **Codex** will deploy on-premises and in hybrid environments through Dell's **AI Factory** and **AI Data Platform**. Codex has grown to over **four million weekly developer users**; the deployment lets enterprises run it inside their own data centres rather than calling OpenAI's API. OpenAI's framing is explicit: agents connect to "codebases, documentation, business systems, operational knowledge."

**The view from the surgery:** This is the deployment model the NHS has been quietly asking for in private and refusing to commit to in public — frontier AI behind the firewall, data never leaving. The BMA's data sovereignty paper last week argued precisely this case. The technical objection has now evaporated; what remains is procurement, indemnity and a willingness by NHSE to ringfence the budget. The harder questions land next.

---

### From the Eye

Three the front pages didn't run. **Item one** — that **"Mythos"** name in the NHSE GitHub directive is the first time Anthropic's internal cyber-capability evaluation work has been named in a public UK government document. Anthropic has not released a model called Mythos; the reference appears to be a non-deployed evaluation system briefed under restricted channels to NCSC and counterparts. The kind of disclosure that will be quietly tidied out of later versions of the policy. **Item two** — the **King's College London Policy Institute survey** last week contained the month's most interesting datapoint: the public **believes 39% of GPs use AI in clinical decision-making**, when the actual figure is **8%**. The gap is wider than for almost any other technology King's has surveyed, and it has implications for how patients interpret what we say in the room. **Item three** — Azeem Azhar's *Exponential View* "Prelude to an AI Supercycle" (4 May) flagged that **Nvidia B200 GPU rental prices have risen 114% in six weeks**, with the premium over the older H200 up more than sixfold. Azhar's contrarian read: the genuine risk is not that too much has been invested in AI, but that the compute is not there to deliver what has already been promised — and clinical-AI procurement timelines are downstream of that.

---

*The Morning Rush. Reply with what works, what doesn't, and what should be on tomorrow's front page.*

**Sources monitored:** NHS England · Digital Health · BMJ · Pulse · STAT News · *Exponential View* · *The AI Daily Brief* · *Private Eye* (MD column) · *The Parnas Perspective* · European Commission · Stanford HAI · The Lancet · HSJ · GPonline · King's College London · RCPsych · The Register · TechCrunch · CNBC · OpenAI · publictechnology.net
