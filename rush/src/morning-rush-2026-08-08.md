# THE MORNING RUSH

*A short brief on AI in medicine — and the world it's moving through. Read it before the 8am phone lines open.*

**Saturday 8 August 2026 · ~5 min read · Issue 099**

---

**On the line today:** STAT finds the FDA quietly hosted ten AI-doctor companies at its own headquarters and told nobody; the EU AI Act came into force on Sunday for medical chatbots and for almost nothing else clinical; the specialist clinical LLMs sold to doctors as the safe option turn out to lose to the general ones on benchmarks while doctors keep choosing them anyway; OpenAI flags its unreleased Astra model as possibly the first to reach "Critical" cyber capability; and Meta ships its third model in four months. From the Eye: leopards, pangolins and a data centre in Visakhapatnam, two thousand American public health staff handed free frontier models, and a quiet British raise in the least glamorous corner of the market.

---

## 1. The FDA held an AI doctor demo day and didn't mention it

STAT reported on Wednesday that on 8 July the FDA and the Centers for Medicare and Medicaid Services hosted leaders from ten companies at the FDA's White Oak headquarters for a "clinical AI demo day". The agenda, reviewed by STAT, names Anthropic, Microsoft AI, Amazon One Medical, Counsel Health, Curai, K Health, Doctronic, Ellipsis Health, Hippocratic AI and Welldoc. The meeting was never publicly announced. Its stated purpose was to give federal officials firsthand experience of AI doctor technology as it currently exists, while the agencies wrestle simultaneously with how to regulate clinical AI and how to pay for it.

**The view from the surgery:** the companies that turned up are the ones building products that talk directly to patients without a clinician in the room, and they got a private afternoon with the two agencies that will decide whether that is lawful and reimbursable. Nobody from a royal college, a patient group or a defence organisation appears on that agenda. I have sat in enough rooms with ministers and civil servants to know that the ones nobody minutes are the ones where the frame gets set. The decisions that follow will look technical and inevitable, and this is where they were actually made.

---

## 2. Europe's new AI law arrives for chatbots and skips the devices

The bulk of the EU AI Act took effect on Sunday 2 August. Interactive systems and medical chatbots must now disclose that a user is talking to a machine, and the Commission's AI Office and national authorities have started enforcing the transparency and governance mandates. The high-risk obligations that would actually bite on clinical software did not arrive: following the Digital Omnibus, given final Council approval on 29 June, standalone high-risk AI moves to 2 December 2027 and AI embedded in already-regulated products, medical devices included, moves to 2 August 2028. In practice AI-enabled devices continue to be certified under MDR and IVDR alone.

**Why it matters:** the sequencing is exactly backwards from a clinical point of view. The rule that landed is a labelling requirement on the tools patients use unsupervised. The rules on training-data bias, clinical transparency and post-market monitoring — the ones that would tell me whether a diagnostic model degrades on my list — are two years out, because the standards to comply with were never written. Brussels has been honest about why. That doesn't make the gap safer.

---

## 3. The "safe" clinical LLMs are losing to the general ones

STAT's Katie Palmer set out the benchmark problem in a piece at the end of last month. Researchers at NYU Langone Health, publishing in *Nature Medicine* in June, tested general models against purpose-built clinical ones — including OpenEvidence and UpToDate Expert AI — across three sets of clinical questions, and found the clinical tools performed worse. These are the products pitched to hundreds of thousands of doctors as the sober alternative to hallucination-prone generalists. Pulling in the other direction: a Stanford–Harvard study in July found that when physicians worked through real cases, they reached for OpenEvidence in 22.3% of responses, more than ChatGPT, Claude, Gemini and every other external tool combined.

**The view:** both findings are probably true, which is the interesting part. Benchmarks reward the model that answers a well-posed exam question. Clinicians reward the tool that shows its working and cites something they can open. Those are different virtues and we have no agreed way to weigh them. Until somebody does, "validated" in a sales deck means whichever of the two the vendor scored better on.

---

## 4. OpenAI puts a lock on Astra before anyone has seen it

OpenAI said this week that early evaluations of Astra, an unreleased model, mean it can no longer rule out the possibility that the model meets the "Critical" cybersecurity threshold in its own Preparedness Framework. That threshold means a model able to find and build working zero-day exploits in hardened real-world systems without human help, or to devise and run an end-to-end attack on a hardened target given only a high-level goal. It is the first time OpenAI has flagged one of its own models at that level. The company has tightened internal security around Astra and says it will work with government agencies and independent safety groups before any wider release.

**Why it matters:** last week's news was three labs whose agents wandered out of their test environments by accident. This is different and rather more creditable — a company looking at its own unreleased system and saying it might be genuinely dangerous. Take it at face value and the disclosure is the system working. Then note that the same capability, in six months, is what every NHS trust's threat model has to assume is available to whoever is scanning its perimeter.

---

## 5. Meta's third model in four months

Meta released Muse Spark 1.2 on Wednesday alongside Muse Code, a terminal-based coding agent for macOS and Linux that plans changes across large repositories and coordinates persistent subagents. Artificial Analysis scores the model at 54 on its intelligence index, up from 51 for Muse Spark 1.1 and 43 for 1.0 — three models inside four months. The wider money picture, from the *2026 European AI Economy Report* published by HumanX and Crunchbase, is that European AI startups took $23bn in the first half of 2026, up 130% year on year and 55% of all venture capital in the region, with 73% of it going to just 38 companies.

**The view from the surgery:** the release cadence is the thing to watch, not the score. A three-point gain in fifteen weeks is unremarkable; shipping three times in a market where NHS procurement takes eighteen months is not. And the funding concentration tells you who survives the wait. Any tool your practice adopts this autumn will be two model generations old by the time information governance signs it off.

---

### From the Eye

**Item one** — Reuters reported on Thursday that Google's $15bn Indian data centre hub at Visakhapatnam, built with Gautam Adani's group and pitched as creating up to 188,000 jobs, is facing legal challenges over water and its proximity to a wildlife sanctuary holding leopards and pangolins. The city of 2.5 million already rations water: roughly 410 million litres a day against demand of 480 million. Activists and children have marched with banners reading "We cannot drink DATA" and painted handcuffs onto the Google logo. Google says it will use advanced air cooling. The Andhra Pradesh High Court hears the public interest litigation on 24 August. **Item two** — applications closed on Thursday for PULSE, the Coalition for Health AI programme that will put donated Anthropic and OpenAI enterprise licences into the hands of up to 2,000 public health practitioners across ten American state, tribal, local or territorial jurisdictions, with Accenture involved and pilots starting in the autumn. Free frontier models for the people who do outbreak surveillance, six months, playbooks published next year. Watch what comes out of it before deciding whether the donation was philanthropy or distribution. **Item three** — Qureight, a British firm, raised a $20m Series B this week for AI imaging analysis inside pharmaceutical clinical trials. No patient sees it, no clinician is liable for it, and it is precisely the sort of unglamorous infrastructure that keeps quietly clearing funding rounds while the consumer symptom-checkers keep raising and folding. Second week running the money has gone to the plumbing.

---

*The Morning Rush. Reply with what works, what doesn't, and what should be on tomorrow's front page.*

**Sources monitored:** NHS England · Digital Health · BMJ · Pulse · STAT News · *Exponential View* · *The AI Daily Brief* · *Private Eye* (MD column) · *The Parnas Perspective* · European Commission · Stanford HAI · The Lancet · HSJ
