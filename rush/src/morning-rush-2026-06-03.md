# THE MORNING RUSH

*A short brief on AI in medicine — and the world it's moving through. Read it before the 8am phone lines open.*

**Wednesday 3 June 2026 · ~5 min read · Issue 036**

---

**On the line today:** **Intermountain Health** publishes the **iCARE** results at ATS 2026 — AI-augmented remote monitoring of COPD and adult asthma cuts total cost of care 57%, halves hospital admissions and trims A&E visits by a fifth across 1,200 patients over two years. The **Nuffield Trust** GP AI survey is now sitting on the desks of practice managers everywhere: 28% of GPs using AI, but only 13% on practice-provided tools, with 11% running their own ChatGPT-on-the-side workflow. **NHS England** has quietly gone private-by-default on its GitHub repos, blaming AI-assisted reconnaissance — and the **Free Software Foundation Europe** is furious. The **EU AI Omnibus** deal pushes the high-risk obligations back to **December 2027** and the medical-device limb to **August 2028**, resetting the regulatory calendar the UK is downstream of. And **NHS Shared Business Services**'s **£900m Healthcare AI Solutions Framework** tender closes **23 June** — the procurement door that AI suppliers will spend the next decade walking through. Plus *From the Eye* — partner numbers in freefall, Anthropic's Mythos lands inside critical national infrastructure, and California's synthetic-content labelling rule clicks on.

---

## 1. Intermountain's iCARE study: AI-driven respiratory monitoring halves admissions

**Intermountain Health** presented full results of the **Intermountain COPD and Adult Asthma Remote Evaluation (iCARE)** trial at the **American Thoracic Society 2026** meeting in Orlando, with the headline release landing yesterday. Across **1,200 patients** at five Utah hospitals over two years, an app pulling daily readings from Bluetooth pulse oximeters, smart inhalers and fitness trackers — with an AI layer triaging the data and escalating to pulmonary navigators — cut **total cost of care by 57%**, **hospital admissions by 50%** and **emergency-department visits by 20%**. The technology partner is **CareCentra**, with **Adherium's Smartinhaler** providing inhaler adherence data.

**The view from the surgery:** Strip out the press-release adjectives and what is left is the most clinically credible large-scale AI-monitoring result this year, in the two conditions that fill the most NHS winter beds. The model is unmistakably the one general practice will end up running — not least because the COPD QOF domain has been creaking for a decade. The interesting question for ICBs is whether commissioning catches up before the private respiratory monitoring market does it first.

---

## 2. Nuffield Trust GP survey: 11% are running their own AI on the side

The **Nuffield Trust** large-scale GP AI survey, now circulating through LMCs in its full form, makes uncomfortable reading at the centre: of **2,108 GPs**, **28% use AI in clinical practice** — but **only 13%** use a tool provided by the practice. **11% use one they obtained themselves**, with another **4% running both**. Self-obtained tools cluster among the under-35s. Documentation is the dominant use case (57%). The headline concern across all three groups is **medico-legal risk** — flagged by **89%** of non-users, **80%** of those on practice-provided tools, and **80%** of those running their own. Lack of regulation comes second. Use is meaningfully lower in deprived areas.

**Why it matters:** The eleven per cent figure is the interesting one. It says that a large minority of UK GPs have decided their personal calculation of professional risk versus workload relief tilts towards loading the morning surgery into ChatGPT — and the central system has neither stopped them nor properly enabled them. That is the precise gap that the NHSE supplier registry was built to close, and which **Alec Price-Forbes**'s circular asking trusts to stop using non-approved tools has been trying to translate to primary care. It is also the indemnity question your **MDU** subscription is increasingly being priced against.

---

## 3. NHS England goes private-by-default on GitHub — citing AI hacking risk

From **11 May**, **NHS England's** engineering guidance now requires that **all source-code repositories be private by default**. Public access requires explicit, exceptional sign-off from the Engineering Board. The trigger named in the guidance: large frontier models — specifically those of **Anthropic's Mythos** class — that can ingest a public repo at scale, reason about architectural decisions and configuration, and generate plausible exploitation paths. NHSE has framed the move as temporary while it shores up cyber posture. The **Free Software Foundation Europe** has responded with an open letter, calling the policy a betrayal of open-source principles, signed initially by 74 supporters; **The Register**, **Computing** and **OECD.AI** have all run it as a story.

**The view:** This is the first concrete sign of a UK public-sector institution treating frontier-AI code-reading capability as a *threat model* rather than a productivity story. Whether NHSE is over-reading the risk is genuinely arguable — but you cannot dismiss it as panic. The same Mythos-class capability is the reason the Illinois bill and the EU AI Act's systemic-risk threshold exist. Watch whether DHSC, the MOD and HMRC follow within the quarter.

---

## 4. EU AI Omnibus: high-risk rules pushed to 2027, medical devices to 2028

The **Council of the EU and the European Parliament** reached provisional political agreement on the **Digital Omnibus on AI** on **7 May**. The substantive effect, now being formalised: the **Annex III high-risk obligations** — hiring, credit, biometrics, education, essential services — slip from **2 August 2026** to **2 December 2027**. The **Annex I limb** — AI embedded in regulated products including **medical devices**, machinery and vehicles — slips further to **2 August 2028**. The cited rationale is to give time for standards, conformity-assessment infrastructure and guidance to catch up.

**Why it matters:** The European medical-device limb shifting by a clear two years is the bit the UK clinical-AI buyer should mark. **MHRA**'s own AI-as-medical-device framework, due later this year, has been calibrated to the Brussels calendar — when that calendar moves, ours wobbles with it. The practical risk is the wrong one: a slower European backstop tempts UK vendors to ship sooner with thinner evidence, leaning on the MHRA AI Airlock sandbox as a substitute for proper conformity. The slowdown is not a regulatory holiday — but it will be sold as one.

---

## 5. NHS SBS £900m AI procurement framework — tender closes 23 June

The **NHS Shared Business Services Healthcare AI Solutions Framework**, published **11 May**, is the single biggest pre-procurement event in NHS AI to date — a national route worth **£900m including VAT**, running **12 May 2027 to 11 May 2035**. Eight lots: medical imaging, laboratory diagnostics, preventative care, virtual and robotic health, data-driven forecasting, research and innovation, service-efficiency systems, and end-to-end packages. **Tender submissions close 23 June 2026**, contract awards in **March 2027**.

**The view from the surgery:** Practice-level relevance is medium-direct: an SBS framework is not a buy-list, but it does set the field of suppliers ICBs can call off against without re-tendering. Three things are worth watching as the lots are awarded. First, whether a serious **primary-care ambient scribe** lot emerges — the framework's scope as currently drawn does not name it clearly. Second, whether the eventual supplier list overlaps cleanly with the **NHSE AVT supplier registry**. Third, the lot 3 "preventative care" wording — that is where remote-monitoring vendors of the iCARE shape will land.

---

### From the Eye

Three the front pages didn't run. **Item one** — the **GP partnership numbers** are now in the kind of freefall that gets its own column in *Pulse*. **FTE partners** have fallen from **15,544 in April 2025** to **15,120 in April 2026** — 424 lost in a single year — and Pulse's latest survey finds **40% of remaining partners are actively considering going salaried**, with more than a quarter having recently considered handing the contract back. The AI story sits inside this story: practices most exposed to the partner exodus are the same ones least able to fund either the ambient scribe or the IT lead the new **GP IT Operating Model v6** now requires them to nominate. **Item two** — **TechCrunch** reported yesterday that **Anthropic** is scaling **Claude Mythos** into critical national infrastructure across **15+ countries**. The same model class that NHS England just cited as a hacking risk is being sold, in parallel, as the answer to defending critical systems against precisely that risk. The contradiction is not a bug — it is the entire commercial logic of frontier safety, and worth keeping in view when the next press release lands. **Item three** — California's **synthetic-content labelling rule** comes into force on **2 August 2026**, requiring AI-generated content to be machine-readably marked and deployers to disclose at first interaction. It is the first major regulator to make AI-generated medical *advertising* a labelling question — and the **AMA** has been openly lobbying for exactly this since the deepfake-doctor stories of February. Worth noting before your next patient brings in a printed "Dr Smith recommends" supplement leaflet.

---

*The Morning Rush. Reply with what works, what doesn't, and what should be on tomorrow's front page.*

**Sources monitored:** NHS England · Digital Health · HTN Health Tech News · BMJ · Pulse · STAT News · *Exponential View* · *The AI Daily Brief* · *Private Eye* (MD column) · *The Parnas Perspective* · European Commission · Stanford HAI · The Lancet · HSJ · Nuffield Trust · ATS · MHRA · NHS SBS
