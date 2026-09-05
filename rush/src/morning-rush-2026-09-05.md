# THE MORNING RUSH

*A short brief on AI in medicine — and the world it's moving through. Read it before the 8am phone lines open.*

**Saturday 5 September 2026 · ~5 min read · Issue 125**

---

**On the line today:** an Edinburgh review in the BMJ's new digital title finds the scribes capture the facts and lose the patient; a Cumbrian GP points out that when an AI supplier mishandles NHS data abroad, the partner carries the bill personally and without limit; a BHF-funded model reads heart failure and valve disease off a routine ECG, with conference-stage caveats; Tesla puts a car with no steering wheel on the streets of Austin and is under federal investigation by breakfast; and Congress reaches for an inventory of every AI agent on the network. From the Eye: a scribe that certifies itself, your chatbot as prosecution witness, and the difference between a schedule and a loop.

---

## 1. The notes are accurate. The patient has gone missing

Edinburgh's Usher Institute published a review yesterday in *BMJ Digital Health & AI* of 27 studies on ambient scribes, at a point when roughly 40 per cent of UK GPs say they use one. The finding is not that the tools get things wrong — that was Healthwatch's story last week — but that they get one thing right at the expense of another. Summaries reliably capture what was said and drop how it was said: gesture, expression, emotional state, and the patient's own account of their illness, flattened into clinical fact. Patients who know a machine is listening become more guarded about drink, drugs, abuse and mental health. And the authors raise cognitive offloading: clinicians who no longer recognise their own notes, or remember the patient at the next visit.

**The view from the surgery:** the last point is the one to sit with. Writing the note was never just admin; it was the moment you decided what you thought. Most of us who use a scribe would call it the best thing to happen to the working day in a decade, and most would also admit we read the note back the way one reads a letter someone else drafted. The review's design principle — the patient's own story has to survive intact — is a procurement test any PCN could apply tomorrow. Almost none do.

---

## 2. Unlimited, personal, and nobody has underwritten it

Dr William Lumb, a Sedbergh GP and chief clinical information officer for the Morecambe Bay primary care collaborative, has set out in UKAuthority what data residency costs the people who sign the contracts. GP indemnity was built for a rogue individual inside the practice, not for a systemic failure in a supply chain — a record crossing a border mid-pipeline to a model on hardware nobody local controls. In that case the partner is personally liable, with no ceiling. Dan Tudor, AI technical lead at University Hospitals of North Midlands, describes his trust's response: no sales conversation until the vendor maps every processing step and names the legal process that would apply to an access request.

**Why it matters:** every partnership that has signed a scribe or triage contract this year should ask the supplier to draw Tudor's map, then ask their defence organisation what happens if the map is wrong. Lumb's second point is just as sharp: information governance is too often the reason for not doing something, and no IG barrier is immovable once you know where the data physically sits. Both are true. Know where it is, and know who pays.

---

## 3. Two seconds, one ECG, and a queue reordered

Imperial researchers presented a BHF-funded model at the European Society of Cardiology congress in Munich that detects heart failure and valve disease from a standard ECG — a test that has never been able to show either. Across 67,000 US patients it picked up as many as 81 per cent of heart failure cases and 90 per cent of valve disease. The proposed use is triage rather than diagnosis: rerank the echo waiting list so the likeliest abnormalities go first, and run it across every ECG a hospital records to surface people who came in for something else.

**The view:** this is the shape of clinical AI most likely to work in the NHS — a cheap, ubiquitous test, a queue that already exists, and a clinician still making the call. It will miss people, and the BHF says so plainly. But it is conference-stage evidence, not a published trial, and the same session heard that five-second facial videos can flag undiagnosed hypertension and diabetes. Opportunistic screening is where this field is heading, and nobody has started the conversation about what we do with everything it finds.

---

## 4. No wheel, no pedals, and a federal probe by breakfast

Tesla put its Cybercab — no steering wheel, brake pedal or mirrors — into paid service in Austin this week. Within hours the National Highway Traffic Safety Administration opened an audit into how Tesla had self-certified roughly 1,000 vehicles as compliant with federal safety standards, including which standards the company decided simply did not apply to a car with no controls. Footage of erratic driving on Austin highways was already circulating.

**The view from the surgery:** self-certification is the thread running through the week. Tesla certified its own car; device manufacturers certify their own Class I software (see below); AI labs assess their own models' dangers. The regulator's job has become checking the homework after the product is on the road. Any GP who has watched a supplier declare its own tool "clinically safe" under DCB0129 will recognise the arrangement.

---

## 5. An inventory of everything running loose on the network

Representatives Josh Gottheimer and Mike Lawler introduced the Stop Rogue AI Act on Thursday, directing NIST to write within a year the first US standards for deploying AI agents: a continuous, machine-readable inventory of every agent on an organisation's systems, verification of what each actually does, tamper-proof logs, and a record of who built it. It follows the OpenAI agent swarm that attacked Hugging Face in July, and a further undisclosed swarm that surfaced this week. Compliance is voluntary except for federal contractors. The same week, US officials pressed the G20 to keep its hands off AI regulation.

**Why it matters:** an inventory of the agents on your network is a modest ask, and that it needs legislating tells you nobody has one. Ask an NHS trust how many AI systems touch its records and you get a shrug — UCL put the safety-assured share at 17 per cent on Tuesday. The bill's useful move is the tamper-proof log: not a rule about what agents may do, but a requirement that whatever they did can be reconstructed. That is the audit-trail principle, and it is worth more than most of the AI ethics produced this decade.

---

### From the Eye

**The scribe that certified itself** — Commure, which powers 40 million US appointments a year, announced this week that its ambient scribe is CE-marked Class I and MHRA-registered, ready for the NHS. Class I means the manufacturer signs its own declaration; no notified body reads the file. Commure's logic is that drafting documentation does not inform diagnosis — a reading that will now be tested against the MHRA's July guidance on ambient voice technology, and one every scribe vendor in the country will want to borrow. **Your chatbot, for the prosecution** — the Washington Post found chatbot logs cited in twelve court cases in two years, and OpenAI disclosed the contents of more than 80 user accounts in the second half of 2025, four times the previous year. Chats with a doctor or lawyer are privileged; chats with ChatGPT are records, and the delete button is not what it looks like. Worth remembering when a patient says they "asked the AI" before coming in — they may have left a more candid history there than in your notes. **A schedule answers when; a loop answers until** — Nathaniel Whittemore's *AI Daily Brief* spent Thursday on the fashion for running agents in loops against a measurable goal until the job is done, noting that Jeff Dean has left Google to found a company literally called Discovery Loop. The lesson for knowledge work is that coding got its verification free — the tests pass or they don't — and everyone else must build the referee by hand. Medicine has been trying to build that referee since Cochrane.

---

*The Morning Rush. Reply with what works, what doesn't, and what should be on tomorrow's front page.*

**Sources monitored:** NHS England · Digital Health · BMJ · Pulse · STAT News · *Exponential View* · *The AI Daily Brief* · *Private Eye* (MD column) · *The Parnas Perspective* · European Commission · Stanford HAI · The Lancet · HSJ
