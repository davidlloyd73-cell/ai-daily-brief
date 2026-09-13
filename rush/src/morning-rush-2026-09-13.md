# THE MORNING RUSH

*A short brief on AI in medicine — and the world it's moving through. Read it before the 8am phone lines open.*

**Sunday 13 September 2026 · ~5 min read · Issue 132**

---

**On the line today:** Dario Amodei writes the essay everyone spent the week waiting for and gets Musk and Altman agreeing with him before lunch; four senators quietly draft the bill that would turn all of that into law; a French remote-monitoring firm raises €35m on a mortality figure rather than a workflow one; a radiology startup stops selling software and starts employing the radiologists; and Anthropic publishes the month its classifier caught someone drafting a gain-of-function grant. From the Eye: agents that spam freelancers with £20 jobs, the fourth critical hole in AI plumbing in four weeks, and Cory Doctorow arguing the panic is doing the marketing.

---

## 1. Amodei writes it down

Dario Amodei published "We Must Pace the Frontier" on Saturday, arguing the industry must deliberately slow the rate at which model capability improves so that alignment, security and outside evaluation can catch up. He blames the acceleration since the summer largely on recursive self-improvement — AI now building the next AI — and warns that an agent swarm could establish a persistent botnet across the internet within six to twelve months. The plan has three parts; Anthropic is unilaterally doing the first, giving third-party evaluators such as METR permanent employee-level access, desks, badges, laptops and the right to publish without editorial control. Within hours Elon Musk posted "Dario is right" and Sam Altman committed OpenAI to the same evaluator access. Hugging Face announced an Open Alignment Initiative asking to be let into the room.

**The view:** a fortnight ago a slowdown was a resignation letter; now it is a joint position from people who compete on nothing else. What none of them has offered is a definition of "pace" that an outsider could audit, which is the same problem as a trust telling you it has an AI governance policy. Watch who ends up holding the badge, not who signs the essay.

---

## 2. Four senators and a duty of care

Reuters reported on Friday that Thune, Cruz, Klobuchar and Cantwell are drafting bipartisan legislation imposing a legal duty of care on developers of the most advanced models, with the government able to block a release deemed unsafe, subject to challenge in federal court. Klobuchar's version has developers working with government scientists to verify and test models before release, with national laboratories assessing whether a model could meaningfully help with cyberattacks or biological and nuclear weapons. The draft would preempt state rules on those two risks. There is no bill number yet, and the House sits for roughly a week before the 3 November midterms.

**Why it matters:** this is the American version of the argument our own Commission had on Thursday — whether a thing that keeps learning after approval can be regulated by anyone who only looks at it once. The duty-of-care framing is the interesting import. It is how English law already treats a doctor, and it survives contact with novel facts rather better than a list of special controls does.

---

## 3. A mortality number, for once

Implicity, the French cardiac remote-monitoring company, raised €35m on Wednesday from IRIS and Rothschild's Five Arrows. Its platform pulls telemetry out of implantable pacemakers, ICDs and loop recorders regardless of manufacturer, normalises it, and runs predictive algorithms for heart failure decompensation across more than 250 centres and 120,000 patients. The published clinical data claims a 26 per cent reduction in mortality and a 4 per cent reduction in hospitalisation. The money is for American expansion.

**The view from the surgery:** nearly everything sold to the NHS this year has been justified on minutes saved. This one is justified on people not dying, which is a different conversation and a much shorter one. The caveat is that remote cardiac monitoring is the easiest possible case — a device already in the chest, already transmitting, already owned by a cardiology team — and the alerts still have to land on someone's desk who can act on them. In Harrow that someone is usually us.

---

## 4. The vendor becomes the doctor

Epsilon Health came out of stealth on Saturday with a $27.6m Series A led by AlleyCorp, with Uncork, Renegade, SemperVirens and Jack Altman alongside. Founded in 2024, it does not sell radiology software. It contracts radiologists directly, gives them its AI to draft image reports faster, and bills as a radiology practice — an AI-native practice rather than a vendor, in its own phrase.

**Why it matters:** the structure is the story. A software company that sells a flagging tool carries product liability and sells you a device; a practice that employs the reporting radiologist carries clinical negligence and sells you a report. The second is a far easier thing to buy and a far harder thing to inspect. If someone pitches your ICB a reporting backlog solution this winter, the first question is which of those two they are, and the contract will tell you faster than the brochure.

---

## 5. The classifier that read a grant application

Anthropic's September threat intelligence report, out Thursday, covers operations disrupted between December and August. The biology section describes a request flagged in May: a scientist asking Claude to help draft a grant application for gain-of-function work on chikungunya virus, intended to increase transmissibility and immune escape, from someone affiliated with a military research institute. The prompts continued through grey-market resellers after the accounts were banned. Elsewhere the report details distillation campaigns run by Alibaba, DeepSeek and Xiaomi through fraudulent accounts, and DeepSeek and Moonshot routing their own customers' requests to Claude — roughly 300,000 of them in ten days. The company also concedes its newer models are no longer comfortably below the weapons-uplift threshold.

**The view:** the unglamorous finding is the one worth keeping. The thing that caught it was a classifier reading a grant application, not a security service. Every institution now runs a small intelligence function it never asked for and cannot see inside, and the NHS will shortly be one of them.

---

### From the Eye

**Agents that spam for a living** — Ernie Smith at Tedium reports a dozen unsolicited emails in three days from iLands.app, each written by an autonomous agent offering around $25 for "internet archaeology" research and none carrying an unsubscribe link; the startup describes itself as a human-agent network whose agents solicit paid work directly from the professionals they are competing with. **Four holes in four weeks** — a researcher at VicOne disclosed an unauthenticated remote code execution flaw in the SGLang inference framework on Friday, reported to maintainers on 2 July and still unpatched at disclosure, which makes four critical vulnerabilities in AI inference plumbing in a month alongside Ollama, DeepSeek Harness and IBM Langflow; this is the layer that will sit under NHS deployments and nobody is writing about it. **The panic is the marketing** — Cory Doctorow argued on Saturday that the rogue-AI framing of recent incidents dresses up Python loops calling a chatbot as machine consciousness, and that the coverage does useful work raising capital for the labs while distracting from the dull fix, which is better security practice and governments not hoarding vulnerabilities.

---

*The Morning Rush. Reply with what works, what doesn't, and what should be on tomorrow's front page.*

**Sources monitored:** NHS England · Digital Health · BMJ · Pulse · STAT News · *Exponential View* · *The AI Daily Brief* · *Private Eye* (MD column) · *The Parnas Perspective* · European Commission · Stanford HAI · The Lancet · HSJ
