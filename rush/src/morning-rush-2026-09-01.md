# THE MORNING RUSH

*A short brief on AI in medicine — and the world it's moving through. Read it before the 8am phone lines open.*

**Tuesday 1 September 2026 · ~5 min read · Issue 121**

---

**On the line today:** Healthwatch England says AI scribes are writing the wrong drugs and diagnoses into records — and it's patients who are catching the mistakes; American nurses stage their biggest protest yet against Palantir in hospitals; a new benchmark finds that when AI polishes the words of paralysed patients it sometimes changes what they meant, confidently; OpenAI is buying Macs by the tens of thousands to teach agents to use computers; and an NPR test finds chatbots surprisingly good at swatting foreign propaganda — better than search engines, anyway. From the Eye: a $199 toilet seat that knows your blood pressure, a $105m bet that point solutions are dead, and the compliance headache hiding inside "AI PCs".

---

## 1. The scribe wrote Prozac. Nobody prescribed Prozac

Healthwatch England warned yesterday that ambient AI scribes — now used across general practice and hospital clinics, with some 27 different tools in NHS service — are mis-recording medicines and diagnoses, and that it is often patients, not clinicians, who spot the errors. The collected examples are instructive: a scribe that dropped the word "null" from "null demyelination", handing a patient nerve damage they didn't have; a summary that swapped a prescribed medicine for a similarly named one; a letter that lost a consultant's instruction to arrange a repeat migraine prescription. The MHRA has decided scribes are not medical devices, so no regulator tests them before deployment.

**The view from the surgery:** those of us who use these tools daily know the failure mode — the note reads beautifully and is wrong in one load-bearing word. The fix is boring: read the note before you sign it, and send patients their letters, because they are apparently our most reliable quality-assurance layer. The regulatory gap is less boring, and "not a medical device" will not survive the first serious harm.

---

## 2. The nurses take on Palantir

On 27 August, National Nurses United staged its largest coordinated action to date against Palantir — civil disobedience in eight cities from Palo Alto to New Orleans, with over a hundred nurses blocking traffic outside the company's old headquarters. Their complaint: automated staffing systems and opaque data practices inside hospitals, from a company simultaneously holding a $10bn defence agreement and a $1bn Homeland Security contract that includes AI tooling for identifying deportees.

**The view:** strip the theatre and there's a serious governance question — the same vendor running your ward staffing algorithm and the state's surveillance infrastructure is, at minimum, a conflict worth naming. British nurses haven't marched about hospital AI yet. Given Palantir holds the NHS Federated Data Platform contract, it would be brave to assume they never will.

---

## 3. Fluent, confident, and not what the patient said

A new benchmark study tested what happens when large language models "clean up" the noisy output of brain–computer interfaces — the systems that let paralysed patients type or speak. Across 20 open-weight models and more than four million generations of corrupted text, the models produced fluent corrections that changed the intended meaning — and were badly calibrated about it: 28.4 per cent of outputs the models rated at 90 per cent confidence or higher were unfaithful to the original message. No mitigation policy eliminated the problem; the best still drifted on 18 messages per hundred.

**Why it matters:** this is the scribe problem in miniature, at maximum stakes. LLMs are trained to produce plausible language, not faithful language, and confidence scores measure neither. Anyone building "AI tidies up the clinical record" should read this twice.

---

## 4. Agents learn to type on tens of thousands of Macs

DigiTimes reported yesterday that OpenAI has bought tens of thousands of Mac minis and Mac Studios — headless, rack-mounted — to run reinforcement learning for computer-use agents: systems that learn to navigate software, edit code and clear inboxes by doing it repeatedly and being scored. Anthropic is renting Mac mini capacity through AWS for the same purpose, and enterprise demand reportedly pushed Apple to release new models early.

**The view:** yesterday this brief noted Apple quietly arming the run-your-own-model era; today its desktops turn out to be the training gym for everyone else's agents. The medical translation is direct — agents trained to operate ordinary software don't need an NHS integration project, just a login. That will arrive faster than the governance for it.

---

## 5. The chatbots hold the line, mostly

NPR and NewsGuard tested six major chatbots against 30 false narratives pushed by China, Iran and Russia. The bots debunked them about three-quarters of the time, failing outright in only 12 of 180 responses — and outperformed the AI summaries sitting atop conventional search engines. Less cheering: Meta AI attributed one claim to a Le Point report that Le Point never published — debunking one fabrication by inventing another.

**The view from the surgery:** patients arrive with chatbot-sourced health beliefs daily, so it matters that the machines resist manufactured narratives better than the search engines they're replacing. Three-quarters is a decent mark and a poor ceiling; the sourcing habit is the thing to watch.

---

### From the Eye

**The throne report** — Casana has launched its $199 Smart Seat, a toilet seat measuring blood pressure trends, heart rate and oxygen saturation, recognising up to five household members by means best not dwelt on, with a $19.99 monthly subscription thereafter. It ships under the FDA's January "general wellness" carve-out — vital signs without the tiresome business of being a medical device — and every anomalous reading it generates will be brought to a GP near you. **The roll-up** — Hinge Health, the digital musculoskeletal firm, paid $105m for Cylinder, a digital digestive-health company; the thesis is that employers no longer buy an app per organ. Somewhere in that sentence is the future of NHS app procurement, and nobody has told the apps. **The endpoint problem** — healthcare IT departments deploying "AI PCs" are being warned that on-device models quietly accumulate caches of patient data outside the systems anyone monitors — the confidentiality argument for local AI, inverted. Worth asking your practice IT lead where, precisely, the scribe's drafts live.

---

*The Morning Rush. Reply with what works, what doesn't, and what should be on tomorrow's front page.*

**Sources monitored:** NHS England · Digital Health · BMJ · Pulse · STAT News · *Exponential View* · *The AI Daily Brief* · *Private Eye* (MD column) · *The Parnas Perspective* · European Commission · Stanford HAI · The Lancet · HSJ
