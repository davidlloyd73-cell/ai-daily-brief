# THE MORNING RUSH

*A short brief on AI in medicine — and the world it's moving through. Read it before the 8am phone lines open.*

**Friday 4 September 2026 · ~5 min read · Issue 124**

---

**On the line today:** a medical AI company releases three models to clinicians and deliberately holds back its best one; the FDA quietly starts letting generative AI devices reach patients before they are authorised; ChatGPT plugs into the chart of 325 million patients, read-only, for now; OpenAI declares its newest model genuinely dangerous in the cyber domain and ships it anyway; and Meta stops scoring its staff on how much AI they use, two months after being sued over it. From the Eye: the complaints letters nobody wrote, the police report written by machine about a search made by machine, and Uber discovering the virtues of organised labour.

---

## 1. The model too good to release

OpenEvidence, the clinical search tool a great many doctors now use in preference to a textbook, published a family of four models on Wednesday. Three went straight to verified clinicians free: Osler, the fast default at around five seconds an answer; Sackett, a slower search for questions that turn on the weight of evidence; and Snow, which takes about five minutes and produces something closer to a literature review. The fourth, Darwin, is available only by application to researchers. The company's stated reason is dual-use risk in virology and genetics — and on its own reported figures Darwin is the strongest medical model yet built, including a perfect score on MedQA.

**The view from the surgery:** the tiering is the interesting part, not the benchmarks. A company has looked at its own best product and concluded that the thing which makes it excellent at answering a clinical question also makes it excellent at answering a question nobody should ask. That is a judgement about capability, made voluntarily, by a vendor. Note also what the three released models really are: not better answers, but a choice of how long you are willing to wait for one. Five seconds in a ten-minute appointment; five minutes for the letter you write at seven in the evening.

---

## 2. The regulator decides to learn by watching

STAT reported yesterday that four products, including Cadence's hypertension management software and Limbic's AI-delivered CBT, have been accepted into the FDA's TEMPO pilot — a route that lets digital health companies put generative AI products in front of patients without marketing authorisation. The stated purpose is partly to stock the Medicare ACCESS model, which pays providers on whether patients improve rather than on activity, and partly to give regulators hands-on experience of these devices in the real world rather than on paper.

**Why it matters:** this is the same instinct behind the MHRA's AI Airlock, and it is defensible — you cannot write rules for a technology you have only read about. But "provisional access while we learn" is a phrase with history in this country, and the learning has to actually happen. Limbic's product is telephone CBT delivered by a voice agent to Medicare patients with depression or anxiety, supervised by clinicians. Whether that supervision is real or nominal is the whole question, and a pilot is precisely where it gets decided.

---

## 3. Read-only, for now

OpenAI announced on Tuesday that ChatGPT for Healthcare now connects to Epic, the record system covering more than 325 million patients. Authorised clinicians can pull notes, labs, medications and specialist correspondence into a chat, or work with ChatGPT inside supported Epic workflows. Access is gated behind organisational accounts with a business-associate agreement, launch partners include UCSF, Cedars-Sinai and Memorial Sloan Kettering, and — the load-bearing detail — it cannot write back to the record.

**The view:** read-only is doing a lot of work in that sentence, and it will not last. The direction of travel is obvious to anyone who has watched a scribe go from suggesting text to inserting it. What strikes me is the layering: many of these hospitals already have an ambient scribe and Epic's own AI in the chart. That is three models with opinions about the same patient, none of which knows what the others said. We spent thirty years trying to get one version of the truth into the record. We may be about to acquire several.

---

## 4. OpenAI says its model is dangerous, then releases it

OpenAI announced on Monday that Astra is the first model to cross the "Critical" cybersecurity threshold in its Preparedness Framework — meaning, on the company's own assessment, that it can find novel vulnerabilities and build working exploits against hardened targets without being led by the hand. In testing it discovered and chained two zero-days, now being disclosed to maintainers. The model is going out broadly to paying users; the strongest cyber capabilities are being fenced off to a vetted group under the name Daybreak, with chain-of-thought monitoring and containment-escape testing bolted on.

**The view from the surgery:** every NHS trust reading this should understand what has changed. The capability that took out our pathology services in 2024 required a competent criminal group. It now requires a subscription and a way past someone's access controls. The gating may well hold. But the model is out, and the defensive side of that arms race is currently staffed, in most trusts, by about four people and a spreadsheet.

---

## 5. Meta stops counting tokens

Meta has removed "usage of AI" from its performance review criteria, replacing labels such as "AI Native" and "AI First" with the limper formulation that results "may be supported by AI or other means". This follows a July lawsuit from around two dozen former employees who argue the metric was used in May's layoffs and unfairly penalised staff on health or family leave, who consumed fewer tokens for entirely obvious reasons. Meta is simultaneously pushing Hatch, a new internal agent that acts on a computer rather than just chatting, across the company.

**Why it matters:** measuring AI adoption by consumption is exactly the error the NHS has made with every activity metric it has ever loved, and it fails the same way — the number rewards the person with the most time, not the best work. Anyone in an ICB currently drafting a "digital maturity" indicator for AI use in general practice should read this and put the pen down. Meta got there in a year and a lawsuit. We usually take a decade.

---

### From the Eye

**The letters nobody wrote** — HSJ reports that trust complaints teams are being buried in AI-generated complaint letters running to dozens of pages, complete with confident legal argument that is wrong and case references that do not exist. Complaints handling is already the least-resourced corner of most trusts, and the asymmetry is total: thirty seconds to generate, half a day to answer. The patient with a real grievance, writing a page in their own words, now waits behind a stack of machine prose. **The report about the search, written by the searcher's software** — 404 Media noted that a Texas sheriff's report on trawling more than 80,000 number-plate cameras for a woman who had self-administered an abortion was itself drafted using Axon's Draft One, which turns body-camera audio into police reports. One system found her, another wrote the official account of finding her, and the disclosure only exists because the tool leaves a footprint. **Uber discovers the union movement** — the FT reports that Uber, having spent a decade fighting organised labour, is now lobbying alongside driver unions for rules keeping humans in the network, including an 85 per cent human-driver quota in New Jersey. Uber's own figure is that one autonomous vehicle displaces roughly four drivers. There is no principle here whatsoever, which is what makes it such a clean illustration of how quickly the automation argument changes sides when it arrives at your own door.

---

*The Morning Rush. Reply with what works, what doesn't, and what should be on tomorrow's front page.*

**Sources monitored:** NHS England · Digital Health · BMJ · Pulse · STAT News · *Exponential View* · *The AI Daily Brief* · *Private Eye* (MD column) · *The Parnas Perspective* · European Commission · Stanford HAI · The Lancet · HSJ
