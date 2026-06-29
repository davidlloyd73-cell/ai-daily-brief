# THE MORNING RUSH

*A short brief on AI in medicine — and the world it's moving through. Read it before the 8am phone lines open.*

**Tuesday 2 June 2026 · ~5 min read · Issue 035**

---

**On the line today:** The **CQC** confirms it is building a regulatory model and assessment framework specifically for AI in health and social care — with the consultation on the draft sector-specific frameworks closing on **12 June**. The **WHO** publishes a discussion paper repositioning AI as a force on the *evidence base for policy*, not just the consulting room. **ASCO 2026** in Chicago wraps with AI as the standing brand of the meeting, with Mayo Clinic showing AI personalising treatment for newly-diagnosed myeloma and a multimodal prostate-cancer biomarker validated across three management pathways. A **Penn State** study finds consumer chatbots answer general health queries at **76% accuracy** — but with the worst performance and the highest "harm score" in internal medicine, neurology and dermatology. And **Illinois** becomes the first US state to require third-party audits of frontier-model safety protocols, the same week **OpenAI** quietly aligns its internal governance with the EU AI Act. Plus *From the Eye* — Karpathy lands at Anthropic, HHS sets AI on the audit trail, and the NHS GP IT Operating Model gets its first refresh in five years.

---

## 1. CQC builds an AI assessment framework — consultation closes 12 June

The **Care Quality Commission** confirmed yesterday, via a regulatory update covered in **HTN**, that the **draft sector-specific assessment frameworks** open for consultation since **24 March** are now being explicitly extended to cover AI in regulated services. The drafts span adult social care, mental health, primary care and community services, and hospitals — they replace the **Single Assessment Framework**. Consultation closes at **5pm on 12 June**, with pilots running through the summer, a final framework by the end of the summer, and full implementation by the end of 2026. The CQC has been explicit that it does not regulate AI tools — it regulates the providers using them, scrutinising AI under the **Well-Led** domain and against the core fundamental standards of safety and consent.

**The view from the surgery:** This is the bit of the UK regulatory landscape that actually bites at practice level. The CQC does not need primary legislation to put AI into a Well-Led inspection — it can do it now. For any practice running an ambient scribe, a triage tool or a clinical-letters drafter, the post-12 June period is when "we use AI in the practice" becomes an inspectable answer. If your IT lead has not yet read the draft primary care framework, that is the small job for this week.

---

## 2. WHO puts AI in evidence-informed policy on the table

The **World Health Organization** today published *Artificial intelligence and evidence-informed policy — emerging challenges and opportunities*, a discussion paper that pointedly redirects attention from clinical care to the *upstream* end of health policy: how problems are framed, how options are designed, how impact is assessed. It maps where existing evidence-informed policy-making tools already converge with AI governance — transparency, participatory engagement, rights protection, risk-based oversight — and where they do not. The paper is unusually direct about the risks: bias, opacity, equity gaps, and a regulatory hole around how AI shapes the *evidence base* on which Member States make decisions.

**Why it matters:** WHO discussion papers do not bind anyone, but they do set the rhetorical perimeter inside which finance ministries and chief medical officers eventually move. The interesting framing is that AI risk is no longer being staged only as a clinical-safety issue. It is being staged as an epistemic risk to the policymaking process itself. For the UK that maps onto the ongoing **National Commission into the Regulation of AI in Healthcare** — and gives our own regulators useful international cover for a slower, more sceptical line.

---

## 3. ASCO 2026 wraps — AI now its own standing brand at the meeting

**ASCO 2026** finishes today at McCormick Place, and the centre of gravity has shifted. ASCO and Conexiant used the meeting to launch **ASCO AI in Oncology**, a year-round digital destination rather than a one-off session track — a tacit admission that AI in cancer care now needs its own editorial spine. The headline science from the weekend: a **Mayo Clinic** team showed an AI model picking up immune signals on routine bone-marrow slides that predict which newly-diagnosed **multiple myeloma** patients gain most from immunotherapy and stem-cell transplant, and a separate group presented a **multimodal AI digital-pathology biomarker** for **prostate cancer** validated for risk stratification across active surveillance, surgery and radiotherapy management strategies.

**The view:** The interesting structural story is the editorial one. ASCO has effectively conceded that "AI" is no longer a sub-strand of imaging or pathology or supportive care — it is its own continuous content stream. Pathologists in particular should note: two of the strongest abstracts this week point at AI on the **routine** slide, not specialist immunohistochemistry, doing the prognostic work. That is closer to the NHS histopathology bench than most US oncology AI tends to be.

---

## 4. Penn State: chatbots 76% accurate — and worst exactly where it matters

A **Penn State** team led by **Lin Lin** and to be presented at **FAccT 2026** in Montreal on **25–28 June** put **212 prompts** to consumer AI chatbots — written from both patient and clinician perspectives — and found overall accuracy of **~76%**. The "headline-friendly" number conceals the clinically dangerous one: validity scores were lowest, and *harm scores* highest, in **internal medicine**, **neurology** and **dermatology**. The authors are blunt that consumer chatbots may be most useful in the hands of trained clinicians — not patients — which is exactly the population using them.

**Why it matters:** Pair this with the **King's College London** poll from a fortnight ago — 15% of UK adults already using chatbots instead of a GP, 20% talked out of seeing one. The Penn State result tells us which clinical areas are most exposed. Neurology and dermatology are also the two areas where my patients are most likely to over- or under-react to a chatbot answer, because both lean heavily on visual and historical pattern recognition. Worth keeping the abstract URL to hand for the next patient with a printed differential.

---

## 5. Illinois first to require frontier-model audits — OpenAI aligns to EU rules

**Illinois Governor JB Pritzker** confirmed last week he will sign **SB 315** — the **Artificial Intelligence Safety Measures Act** — the first US state law to require **third-party audits** of frontier-model safety protocols. The bill cleared on **27 May**, with the governor's signature expected this week. On **28 May** **OpenAI** published its **Frontier Governance Framework**, explicitly aligning its internal Preparedness Framework with the **EU AI Act's Code of Practice for General-Purpose AI** and **California's Transparency in Frontier AI Act**. The optics are unmistakable: OpenAI is preparing for August's EU deadline and is setting an implicit baseline for Anthropic, Google and xAI to match.

**The view from the surgery:** The federal framework Trump pushed in December was supposed to pre-empt this kind of state law — Illinois is the first concrete sign that it has not. For UK clinical-AI buyers, the medium-term significance is straightforward. The serious safety-audit pressure on frontier labs is now coming through the EU, California and Illinois in parallel, all on roughly the same calendar. When MHRA finalises its **AI-as-medical-device** framework later in 2026, it will be slotting into a denser global oversight stack than it would have done a quarter ago.

---

### From the Eye

Three the front pages didn't run. **Item one** — on **19 May**, **Andrej Karpathy** — OpenAI co-founder, ex-Tesla AI lead — joined **Anthropic** to launch a team using **Claude itself to accelerate pre-training research**. The same week **Claude Opus 4.8** shipped with effort-control in claude.ai and a cheaper fast mode. The tactical read is that the model your AVT-registry scribe runs on is now being trained partly *by* the previous version of itself — a recursive loop that the **UK AISI** report flagged last week as eroding the value of pre-deployment benchmarks. **Item two** — on **21 May** the US Department of Health and Human Services launched **AERO**, an AI initiative to review the **annual audit history** of federally-funded health programmes across all 50 states, going back at least five years, to identify waste, fraud and abuse. It is the cleanest example yet of regulators pointing AI at the audit trail rather than at the consulting room. Worth watching whether **NHS Counter Fraud Authority** or the **DHSC's** equivalent takes the same posture. **Item three** — **NHS England** quietly updated the **GP IT Operating Model** to **v6** on **27 May**, the first refresh in five years. The change that matters: practices must now formally identify an individual responsible for IT including data and cyber security, and complete an annual training-needs analysis for digital services. For single-handed practices and small partnerships this is the bit that will land in the next CQC visit — the framework above (Item 1) gives the inspector somewhere to point.

---

*The Morning Rush. Reply with what works, what doesn't, and what should be on tomorrow's front page.*

**Sources monitored:** NHS England · Digital Health · HTN Health Tech News · BMJ · Pulse · STAT News · *Exponential View* · *The AI Daily Brief* · *Private Eye* (MD column) · *The Parnas Perspective* · WHO · European Commission · Stanford HAI · The Lancet · HSJ · CQC · MHRA · ASCO
