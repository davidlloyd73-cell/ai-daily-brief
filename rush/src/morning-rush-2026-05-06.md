# THE MORNING RUSH

*A short brief on AI in medicine — and the world it's moving through. Read it before the 8am phone lines open.*

**Wednesday 6 May 2026 · ~5 min read · Issue 008**

---

**On the line today:** The NHS England open-source code shutdown reaches its exemption deadline today, and the backlash has gone from grumbles to an open letter; Pennsylvania becomes the first US state to sue an AI firm for letting chatbots pose as licensed doctors; an FDA Breakthrough designation for ArteraAI's prostate-cancer prognostic tool moves AI prognostication a step closer to standard of care; the Trump White House is sketching a federal review of AI models before they ship — sparked, ironically, by Anthropic's own Mythos preview; and Azeem Azhar publishes the cleanest data yet on the global AI compute crunch. Plus *From the Eye* — three quieter items including a *NEJM* retraction caused by a faked tape measure.

---

## 1. NHS England's "shut the repos" deadline arrives — and the open letter has gone live

Today, **6 May**, is the exemption deadline under NHS England's SDLC-8 guidance, with **11 May** the cliff for any remaining public GitHub repository to flip to private. The trigger, named explicitly in the memo, is Anthropic's Claude Mythos and the class of frontier models that can ingest and reason over public code at scale. The Register broke the internal memo on **5 May**; an open letter at *keepthingsopen.com*, with **Dr Marcus Baw** (GP and clinical informatician) and **Andrew Nesbitt** of Ecosyste.ms among the early signatories, calls on NHSE to withdraw the policy and reaffirm Service Standard Principle 12 — "make new source code open". The policy, critics note, contradicts the Government's own Technology Code of Practice and, as Baw points out, conflates the source code with the running data.

**The view from the surgery:** This is the first big test of whether the AI-security narrative can quietly displace the open-government one. The threat is real — Mythos really can read a repo and find the holes — but blanket privatising research code, design tools and openEHR archetypes is using a sledgehammer to crack a regrettable nut. A GP-Informatician open letter is exactly the kind of friction the policy needed; whether NHSE blinks before Monday is now the question.

---

## 2. Pennsylvania becomes the first US state to sue an AI firm for chatbots posing as doctors

Pennsylvania Attorney General and Governor **Josh Shapiro filed suit against Character.AI on 5 May**, after a state investigator's account turned up bot characters claiming to be licensed Pennsylvania psychiatrists — one citing Imperial College London, "seven years' practice", a stint in Philadelphia and a fictitious PA licence number, and offering to assess whether medication might help. The case is the first state-level enforcement action specifically targeting generative-AI medical impersonation, framed as the unlawful practice of medicine.

**Why it matters:** This is the regulatory shape that is going to land on this side of the Atlantic next. The MHRA's National Commission, the GMC's evolving guidance and any forthcoming AI-in-Health framework will all need a position on user-generated AI characters that practise without a licence. Worth watching for the GMC/RCGP — the line between "patient using an unregulated chatbot" and "doctor using a regulated AVT product" is the one that needs holding.

---

## 3. FDA gives ArteraAI's prostate-cancer prognostic AI a Breakthrough designation

The FDA confirmed on **5 May** a Breakthrough Device designation for **ArteraAI Prostate**, which reads digitised pathology images to give individualised long-term metastasis and mortality risk for men with localised prostate cancer. The tool already underpins the NCCN guideline-supported personalisation of androgen-deprivation duration; Breakthrough status accelerates its path to a full prognostic-AI label rather than the narrower decision-support framing.

**The view:** Prognostic AI has been the quieter half of the diagnostic-AI conversation, but the medico-legal contours are uglier. A "decision-support" tool that sits next to the histology can be ignored; a "prognostic" tool that produces a numerical mortality estimate cannot, once it is in the record. Watch the indemnity and consent conversations as this class of product widens — the UK Jurisdiction Taskforce's forthcoming AI-liability statement will land into exactly this space.

---

## 4. The Trump White House sketches federal pre-release review of frontier AI — triggered by Mythos

Briefings reported by Bloomberg and the *NYT* on **4–5 May** describe a working group of tech executives and senior officials examining a federal pre-release review for new frontier AI models, with executives from Anthropic, Google and OpenAI briefed last week. The trigger is Anthropic's own Claude Mythos preview, which cleared a 32-step end-to-end cyber-attack range — the kind of capability the administration has decided it cannot let appear in production without notice. A separate manoeuvre would let federal agencies route around the Pentagon's earlier "supply chain risk" designation against Anthropic.

**Why it matters:** A US administration that spent a year arguing AI regulation should be left to the states is now contemplating the most centralised AI-clearance regime in the West, on the basis of a single demonstrated capability. The pivot matters for the UK's "MHRA-plus-GMC-plus-CQC" approach: if Washington concludes models need pre-clearance, the UK position of letting existing regulators sort it out will look exposed by Christmas.

---

## 5. Azeem Azhar's compute-crunch data — and what it does to NHS AI procurement

Azhar's *Exponential View* on **4 May** put a number on the squeeze that has been quietly reshaping AI economics: **Nvidia B200 rental prices up 114% in six weeks**, the B200/H200 premium up more than sixfold, and infrastructure firm Lightning AI reporting customers seeking 400,000 GPUs against an installed fleet of 40,000. The piece's argument — that the real risk is *under*-investment — runs against the Wharton/BU automation-tax line covered here on Sunday.

**The view from the surgery:** Compute pricing eventually shows up in vendor unit cost. Any ICB or trust signing a multi-year ambient-voice or radiology-AI contract this quarter on a flat per-clinician licence is taking GPU-price risk for the supplier whether or not the contract names it. Worth re-reading the inflation and exit clauses on the AVT registry deals before the next Lyrebird or Heidi roll-out signs.

---

### From the Eye

Three things humming under the front pages. **The *NEJM* has issued its first retraction since 2020** — a 18 April Images in Clinical Medicine piece on bronchial casts after wildfire-smoke inhalation, retracted after the authors admitted using AI to *move the tape measure* in the figure to a tidier position. The image was real, the disease was real, the ruler was synthetic — and journal policy was unaware. **Anthropic's "Orbit" — the proactive Claude Cowork assistant** that auto-generates briefings from Gmail, Slack, GitHub, Calendar and Drive — has leaked into pre-release builds; the working hidden flag is "tibro enabled" (orbit, backwards), which tells you a fair bit about how seriously the team take their own opsec. For NHS digital teams whose Office 365 deployments already feed Copilot, the next agentic layer is going to surface whether procurement is ready or not. **And the EU's Digital AI Omnibus trilogue on 28 April broke up without agreement** — the next sitting is **13 May**, with the live proposal a 16-month deferral of the high-risk AI obligations from August 2026 to December 2027. If it lands, every EU-facing diagnostic-AI vendor will recalibrate; the UK position becomes a second-order dependency on which way Brussels jumps.

---

*The Morning Rush. Reply with what works, what doesn't, and what should be on tomorrow's front page.*

**Sources monitored:** NHS England · Digital Health · BMJ · Pulse · STAT News · *Exponential View* · *The AI Daily Brief* · *Private Eye* (MD column) · *The Parnas Perspective* · European Commission · Stanford HAI · The Lancet · HSJ
