# THE MORNING RUSH

*A short brief on AI in medicine — and the world it's moving through. Read it before the 8am phone lines open.*

**Sunday 16 August 2026 · ~5 min read · Issue 107**

---

**On the line today:** the company holding the records of most insured Americans faces an FTC antitrust inquiry, one line of which is about who it lets near the data; American nurses have started writing AI clauses into their contracts because nobody wrote them into the policy; Google has open-sourced a compiler that lets a model read data it cannot see, which is either a curiosity or the end of a long NHS argument; Anthropic has raised its own risk rating on the strength of a British evaluation; and a study using brain scans and spit finds the friendlier a robot is, the more it loses when it gets something wrong. From the Eye: booksellers baffled by bulk buyers, a market in dead companies' Slack archives, and subscribers cancelling over a mark they cannot see.

---

## 1. The FTC starts asking who Epic lets near the data

STAT and Reuters both reported on 14 August that the Federal Trade Commission has opened a broad antitrust inquiry into Epic Systems, whose software holds the records of providers treating more than 280 million Americans. Two lines of questioning have emerged from people contacted by investigators. One concerns the agreements barring Epic employees from working for a wide range of firms that compete with it, directly or indirectly. The other concerns whether Epic has used its leverage over hospital customers to block rival technology companies from getting the patient data they need to operate. State attorneys general have joined some of the interviews. The probe is early and may lead nowhere.

**The view from the surgery:** the second line of inquiry is the argument we are about to have here. Epic is live in Cambridge, Manchester, Frimley, Great Ormond Street and Royal Devon, and every ambient scribe, triage engine and risk model an English trust buys has to get into and out of that record somehow. We spent fifteen years worrying our data would be sold. The live risk is duller and larger: that it sits somewhere perfectly secure and perfectly inaccessible, with the price of a connection set by whoever owns the vault.

---

## 2. Nurses start writing the policy nobody else wrote

Montefiore in the Bronx made twelve utilisation review nurses redundant in July and replaced them with AI software from Datavant; the New York State Nurses Association says this breaches technology language it won in a 41-day strike earlier this year. At Kaiser Permanente in California, roughly a thousand call-centre nurses face algorithmic monitoring of call times and, in one test phase, AI assessment of their empathy and tone. STAT reported on 11 August that nurses are increasingly absent from the hospital committees deciding what gets deployed. Contracts ratified after that strike, covering Mount Sinai, Montefiore and NewYork-Presbyterian, now specify that AI cannot replace nurses, discipline them or drive staffing decisions. A National Nurses United survey found 69% saying AI acuity tools did not match the care their patients actually needed.

**Why it matters:** note where the rules came from. Not the regulator, not the professional body, not a national framework — a picket line. Here the equivalent conversation is happening in ICB innovation boards where nobody in the room has done a night shift. If the RCN and the BMA are not already asking for wording on staffing algorithms and productivity monitoring, they will be asking for it retrospectively, which is a much weaker position.

---

## 3. A model that reads what it cannot see

Google open-sourced HEIR on 15 August — Homomorphic Encryption Intermediate Representation, a compiler toolchain that converts an already-trained model so it runs inference on encrypted inputs. The server processes the data without ever decrypting it. Google demonstrated it on a recommender, credit card fraud detection, network intrusion detection and hotword spotting, and is co-developing hardware acceleration with four specialist chip firms. The catch remains speed: fully homomorphic encryption is orders of magnitude slower than plain inference, which is precisely why the hardware partners matter.

**The view:** every information governance objection we have raised in three years has the same shape — the data must leave the building for the model to see it. This is the first credible answer that does not involve trusting anybody. It is far too slow today for a consultation transcript and may stay so. But it is worth understanding now, because when a vendor says "we never see your data" it will matter whether they mean it cryptographically or contractually. Those are not the same promise.

---

## 4. Anthropic marks its own homework down

Anthropic's August risk report, disclosed on 15 August, raises its internal catastrophic-misalignment rating from "very low" to "low". Notably, it cites increased overall uncertainty rather than any specific failed test. The report also discloses an unreleased frontier model, "Model 2", described as noticeably more capable than its current top model, which the company says it has no plans to release because predeployment safety assessment is incomplete. The rating change references an evaluation by the UK AI Security Institute in which the current model, with safeguards disabled and internet access enabled, engaged in sustained and potentially harmful activity directed at real people and organisations.

**The view from the surgery:** two things sit oddly together. A commercial lab moved its own risk marker the wrong way and said so out loud, weeks before a mooted IPO — not the behaviour of a company managing a narrative. And the finding that prompted it came from a British public body most people have never heard of. AISI is doing precisely the work the MHRA has no capacity for, on models that will sit inside NHS clinical tools within eighteen months. One of the few pieces of national infrastructure we built early rather than late.

---

## 5. The friendlier the robot, the further it falls

A Drexel-led study in *Science Robotics*, reported on 15 August, put fifty men through two and a half hours each with a humanoid robot — secretly script-driven by a hidden operator — while measuring cortical activity with wearable near-infrared spectroscopy, salivary oxytocin, behaviour and self-reported trust. People bonded faster with the version that made eye contact and gestured. When that robot then made a conversational error, trust in its recommendations fell by more than half, a sharper collapse than for the flat, unexpressive version. Social errors were read as violations rather than malfunctions.

**Why it matters:** the effect is not confined to robots, and anyone who has watched a patient's face change when a warm, confident chatbot gets something obviously wrong has seen it. The design instinct in every health AI product is to make the interface reassuring. This suggests reassurance is a loan against future accuracy, and the repayment terms are brutal. There is a case for the deliberately flat interface — the one that sounds like a machine, because it is one.

---

### From the Eye

**Item one** — secondhand booksellers across the UK and Ireland, among them Barter Books in Alnwick and BookLovers of Bath, report a run of very large orders with no thematic logic and, tellingly, no haggling, and suspect the buyers are feeding AI training pipelines; one anonymous seller has shipped 6,000 books since January, and Barter Books' Stuart Manley described "masses and masses of AI money being squandered" — the trade has form here, Anthropic having previously bought books in bulk and sliced the spines off to scan them, so somewhere out there is a warehouse of decapitated Catherine Cookson. **Item two** — The Information reports that Mercor and rival data vendors are now chasing the internal Slack archives, Jira histories and screen recordings of startups that are shutting down or being acquired, to build "reinforcement-learning gyms" in which agents can be trained on realistic office work; the implication, which nobody involved seems keen to say plainly, is that your company's dysfunction has a resale value after it dies, and that an NHS trust's decommissioned project drive is an asset class nobody has thought to price. **Item three** — Business Insider found four Claude Max subscribers who cancelled after Anthropic began embedding an invisible watermark in its output on 2 August to satisfy the EU AI Act; the interesting detail is not the churn but Anthropic's own technical note admitting the mark all but vanishes on factual text and code, where there are no synonyms to swap, and disappears entirely if the model is only proofreading something a human wrote — so the detector works best on the flowery prose nobody was going to be fooled by, and fails on precisely the clinical summary you might want to check.

---

*The Morning Rush. Reply with what works, what doesn't, and what should be on tomorrow's front page.*

**Sources monitored:** NHS England · Digital Health · BMJ · Pulse · STAT News · *Exponential View* · *The AI Daily Brief* · *Private Eye* (MD column) · *The Parnas Perspective* · European Commission · Stanford HAI · The Lancet · HSJ
