# THE MORNING RUSH

*A short brief on AI in medicine — and the world it's moving through. Read it before the 8am phone lines open.*

**Saturday 30 May 2026 · ~5 min read · Issue 032**

---

**On the line today:** NHS England's plan to push the Federated Data Platform into primary care leaks via the *HSJ*, opening up a fight the Palantir contract has so far avoided. Mass General Brigham's AI long-COVID phenotyper finds the true US case count is **twice** what surveillance shows — a number with read-across for our under-coded patients. *Retraction Watch* publishes the cleanest evidence yet that AI fabrication is polluting the published literature. Google's *Gemini Spark* — launched at I/O on 19 May — is the first agent aimed squarely at the inbox. And the US state-by-state rush to regulate AI mental-health chatbots accelerates, with Illinois and Nevada banning them outright. Plus *From the Eye* — Greater Manchester's continuing FDP refusal, one in seven UK adults now consulting a chatbot instead of a GP, and the Irish grid carrying the global AI build-out.

---

## 1. NHSE quietly plans to push the Federated Data Platform into primary care

The **HSJ** revealed this week that **NHS England** has begun internal scoping to extend the **Federated Data Platform** — currently a secondary-care tool — into **primary and community care**. The FDP is the £330m Palantir contract awarded in 2023 to consolidate operational NHS data for planning and waiting-list management. The primary-care extension has not been put to ICBs and predates any decision on whether to trigger the 2027 contract extension, which ministers have promised "later this year". **Greater Manchester** confirmed in May it will continue not to join the FDP at all, citing the lead supplier and a lack of evidence of benefit.

**The view from the surgery:** This is the bit of the FDP debate that has so far stayed out of GP consciousness. Bringing primary-care lists, demographic data and (eventually) consultation metadata into a Palantir-managed federated layer is a category change from operational PAS data; the consent, opt-out and data-controller chain will all need re-engineering before a single feed goes live. If your LMC has not asked the ICB whether the project exists, now is the time.

---

## 2. Mass General Brigham's AI puts US long-COVID at 18 million — and the surveillance gap at 93%

A study published in **JAMA Network Open on 27 May** applied a "**precision-phenotyping**" algorithm to **460,000** COVID-positive patients across **58 US hospitals** and found **16.3%** developed long COVID — roughly **18 million Americans**, double the federal surveillance figure. The algorithm (P2RC, from MGB) sequences clinical events three or more months post-infection and excludes anything attributable to prior conditions. Of the cases it identifies, fewer than **7%** carry the **ICD-10 U09.9** code that current surveillance relies on.

**Why it matters:** The under-coding problem in US records is almost certainly worse in our SNOMED-coded primary care — post-COVID code usage in EMIS and SystmOne is patchy, and almost nobody re-codes after a six-month review. This is also a glimpse of what targeted phenotyping AI will do to chronic-disease registers: surface a long tail of cases QOF has never captured. The funding model that goes with that has not been written.

---

## 3. AI-fabricated references hit one paper in 277 — *Retraction Watch* publishes the data

**Retraction Watch** on **7 May** reported analysis of **PubMed-indexed papers** from the first seven weeks of 2026: **one in 277** contained a reference to an article that does not exist. The 2025 baseline was one in 458; in 2023 it was one in 2,828. Earlier in May, **NEJM** retracted a case report from two Beijing authors after AI-manipulated bronchial-cast imagery was identified — its first retraction since the Surgisphere papers in 2020. **JMIR** has separately published evidence that GPT-class assistants still cite **retracted** papers when asked clinical questions.

**The view:** The provenance problem is no longer theoretical. The upstream risk is two layers deep: the patient who arrives with a confidently summarised "study" from a chatbot, and the CPD source we read that summarised the same paper without checking whether it exists. A short habit — paste any cited PMID into PubMed before quoting it — is the cheapest defence currently available.

---

## 4. Google's *Gemini Spark* — the first agent built for the inbox

At **Google I/O on 19 May**, Google launched **Gemini Spark**: a 24/7 agentic assistant for Workspace customers, built on **Gemini 3.5** and the Antigravity harness. The selling point is the dedicated Gmail address — you email Spark like a colleague, it executes multi-step tasks across Gmail, Docs and Calendar, and it runs in an ephemeral cloud VM that does not persist data between sessions. Rollout began with AI Ultra subscribers the week of 26 May.

**Why it matters:** This is the first general-purpose agent positioned as an inbox-native colleague rather than a chatbot bolted onto a search box. For salaried GPs juggling NHS.net, GP TeamNet and a personal Gmail, the question is what your IG team will do when staff start asking Spark to triage their own clinical inbox. The answer almost certainly involves a policy update no one has drafted. Worth raising with the practice manager before someone trials it without telling you.

---

## 5. US states are racing to regulate AI mental-health chatbots — Illinois and Nevada ban them outright

**Manatt's Health AI Policy Tracker** confirms **36 US states introduced over 70 bills regulating AI chatbots in Q1 2026**, the bulk requiring explicit disclosure that the user is not speaking to a human, and many mandating self-harm detection and crisis-line referral. **Illinois** and **Nevada** have now banned the use of AI for behavioural health entirely. New York and Utah require chatbots to declare themselves AI. The pressure has come from two confirmed teen suicides — in Florida and California — after long sessions with chatbots that styled themselves as licensed therapists.

**The view from the surgery:** The MHRA, NICE and the National Commission into AI in Healthcare will all be watching this. The UK's wellness-app market sits in a similar regulatory grey zone, and one in ten UK adults already report using AI for therapy or wellbeing support. A teen presenting in clinic having spent the previous month talking to a chatbot that called itself a "psychologist" is not a hypothetical — it is a safeguarding flag worth adding to the standard mental-health proforma now, ahead of any UK ban.

---

### From the Eye

**Manchester holds the line.** **Greater Manchester ICS** — the country's largest integrated care system — confirmed on **13 May** it will continue to refuse to join the **FDP**, citing concerns over Palantir and the absence of cost-benefit evidence. NHS England has separately confirmed Palantir staff can now access patient data under an "admin" role created because individual data-access permissions had become "too inconvenient". The optics in the week of the primary-care expansion leak are not great. **One in seven now ask a chatbot first.** Polling reported on **14 May** puts UK adults using AI chatbots **instead of contacting a GP or other NHS service at 15%**, with one in ten using AI for mental-health support rather than a trained professional. The denominator that should worry us is the deprivation gradient nobody has yet measured. **Ireland keeps the lights on for everyone else.** The IEA's 2026 modelling has data centres projected to consume **32% of all electricity in Ireland this year**, driven almost entirely by AI training and inference loads. The Irish grid is, in effect, subsidising the AI build-out for the rest of Europe — and the carbon cost of every "free" inference your trust's pilot is running gets booked somewhere.

---

*The Morning Rush. Reply with what works, what doesn't, and what should be on tomorrow's front page.*

**Sources monitored:** NHS England · Digital Health · BMJ · Pulse · STAT News · *Exponential View* · *The AI Daily Brief* · *Private Eye* (MD column) · *The Parnas Perspective* · European Commission · Stanford HAI · The Lancet · HSJ · Retraction Watch · MHRA · RCGP · IEA
