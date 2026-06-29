# THE MORNING RUSH

*A short brief on AI in medicine — and the world it's moving through. Read it before the 8am phone lines open.*

**Friday 15 May 2026 · ~5 min read · Issue 017**

---

**On the line today:** NHS England quietly hands Palantir staff a new "admin" role on the Federated Data Platform with what an internal memo calls "unlimited access" to identifiable patient records — and concedes in writing that the move risks "loss of public confidence". Anthropic and the Gates Foundation put $200m into low- and middle-income country health and education programmes, with Claude credits load-bearing. STAT News lifts the bonnet on the FDA's 510(k) pathway and finds AI sepsis algorithms clearing without ever seeing a real ward. The EU's "AI Omnibus" deal hands big-tech a year of grace, and changes nothing on the medical-device track. Anthropic is locked out of the Pentagon's $200m AI procurement after a row over military guardrails. Plus *From the Eye* — NHS England goes to war on open source, Mandiant logs AI-written zero-days in the wild, and Apple delays "Health Plus".

---

## 1. Palantir staff to be handed "unlimited access" to identifiable NHS records

A leaked NHS England briefing note confirms what the **FT** first reported on Monday: staff at **Palantir**, Microsoft Azure and a handful of other vendors working on the **Federated Data Platform** will be granted a new "admin" role on the **National Data Integration Tenant** — the unpseudonymised holding area where every dataset lands before processing. The current rule requires each contractor to apply for time-limited access to a specific dataset. The new rule, the memo admits in plain English, carries "a risk of loss of public confidence" in NHS data stewardship. NHS England's public reply is that all external staff hold government security clearance and must be approved at director level.

**The view from the surgery:** This is the biggest UK data-sovereignty shift since care.data was pulled in 2014, and it has landed without a Parliamentary statement, a public consultation or a press release. Palantir's £330m FDP contract was always going to require some access; "unlimited", "identifiable" and "admin" are not the words anyone signed up for. The honest political reading is that NHSE cannot meet FDP delivery without giving contractors keys to the door, and has chosen delivery over consent. Expect a Section 251 challenge within the fortnight.

---

## 2. Anthropic puts $200m and a stack of Claude credits behind the Gates Foundation

**Anthropic** and the **Bill & Melinda Gates Foundation** yesterday announced a **$200m, four-year partnership** focused on low- and middle-income countries — biased toward global health (vaccine development; neglected diseases including polio, HPV and pre-eclampsia), education tooling, and smallholder agriculture. About half is grant funding; the rest is **Claude API credits and engineering support**. Programmes will be open-sourced as benchmarks where possible. The announcement landed the same week Anthropic was excluded from the Pentagon's $200m classified-network AI procurement (see item 5).

**Why it matters:** Strip the press-release sheen and the structural read is that frontier-AI firms are now deciding, with little democratic oversight, which diseases get accelerated and which countries get the discount API. The choice of pre-eclampsia is clinically interesting — still a leading cause of maternal death globally and a clear deployment target for low-resource ANC triage. Whether any of this lands as durable infrastructure rather than a glossy 2030 retrospective is the only question worth asking.

---

## 3. STAT News opens the FDA's 510(k) loophole, with sepsis as exhibit A

**Brittany Trang's "AI Prognosis"** column in STAT News on **13 May** dissects the **510(k) clearance pathway** — the route used for most AI medical devices, including the sepsis monitor Bayesian Health cleared last week. The "dirty secret", per Trang, is that 510(k) only requires the manufacturer to demonstrate **"substantial equivalence" to a previously cleared predicate device** — and the predicate can be a 1990s rules-based pop-up that never touched machine learning. Several AI sepsis tools, she writes, have cleared this way without being tested against the live deteriorating patient on a real ward.

**The view:** This is the regulatory shape the **MHRA** is openly proposing to import in its forthcoming Software-as-a-Medical-Device pathway, via the **International Reliance Framework** due in autumn. The argument for reliance is real — UK device approvals are bottlenecked. The argument against is that we would be inheriting an evidentiary bar that is now the subject of an unfolding scandal in its country of origin. Worth a public position from the GMC and MDU before the MHRA consults, not after.

---

## 4. The EU's "AI Omnibus" arrives — three months late, a year of grace for everyone

On **7 May** the European Council and Parliament reached political agreement on the **AI Act Omnibus**: regulatory-sandbox deadline extended to **August 2027**; transparency obligations brought forward to August this year; synthetic-content watermarking grace period shortened from six to three months. New prohibitions are added against AI-generated **non-consensual intimate content** ("nudifier" apps) effective 2 December. Crucially for clinicians, the medical-device track is **unchanged** — high-risk classification still applies to any AI tool that aids diagnosis or treatment.

**Why it matters:** The political read is that Brussels has blinked, post-DeepSeek and post-Mistral, on enforcement timelines for general-purpose AI — and not on medical devices. For the UK the second half matters more: any AI-MD product sold across the Channel will still clear as high-risk, and the MHRA's reliance proposal therefore has to decide whether to mirror EU or US norms on a device-by-device basis. The "we'll just align with Brussels" shortcut is gone.

---

## 5. The Pentagon picks seven AI vendors. Anthropic is not one of them.

Announced **14 May**: the **Department of Defense** has signed Impact Level 6/7 contracts — classified networks, up to Secret — with **SpaceX, OpenAI, Google, NVIDIA, Microsoft, Amazon Web Services and Reflection**. **Anthropic is absent**, after a public row last month in which the company refused to relax its usage policies on weapons targeting and offensive cyber, and was duly labelled a "supply-chain risk". The total package is reported at roughly **$200m** — coincidentally or otherwise mirrored by Anthropic's Gates Foundation announcement the same week.

**The view from the surgery:** Each frontier lab now carries a visibly different commercial posture on the dual-use question, and the Pentagon's exclusion makes the schism explicit. The clinical angle is less obvious but real — the same usage-policy text that locks Anthropic out of DoD also locks it out of any future NHS contract requiring battlefield-medicine portability or NCSC-style assurance. The vendors who said yes to Washington will not be saying no to Whitehall.

---

### From the Eye

Three threads the wires under-played. **NHS England ordered hundreds of public GitHub repositories made private by 11 May**, in a memo citing — by name — Anthropic's forthcoming "Mythos" model and its alleged ability to ingest and reason about public NHS source code "at large scale". Privately, NHS insiders quoted in *The Register* say very few of the affected repos contain anything sensitive, and the move is more reputational than threat-intelligence-led. The irony of an open-source crackdown justified by closed-source AI is its own commentary. **Mandiant's Google Threat Intelligence Group** on **12 May** published the first public catalogue of **AI-generated zero-day exploits being used in the wild** — five confirmed, North-Korean-attributed, and written end-to-end with what the team calls "off-the-shelf coding agents". Worth knowing the next time a colleague tells you AI cybercrime is theoretical. And **Apple has quietly delayed "Apple Health Plus"** — the Apple-Intelligence-powered companion to the existing Health app — into 2027 at the earliest, with Eddy Cue's team splitting the feature set into smaller releases. The buried detail: Apple is reportedly building an option to let users default Siri to **Claude or Gemini** for medical questions rather than route through its own model. If true, the patient-facing front door to medical AI on iPhones may end up wearing somebody else's badge.

---

*The Morning Rush. Reply with what works, what doesn't, and what should be on tomorrow's front page.*

**Sources monitored:** NHS England · Digital Health · BMJ · Pulse · STAT News · The Lancet · *Exponential View* · *The AI Daily Brief* · *Private Eye* (MD column) · *The Parnas Perspective* · European Commission · Stanford HAI · HSJ · The Register · FT · Reuters
