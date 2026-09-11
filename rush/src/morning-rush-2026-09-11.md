# THE MORNING RUSH

*A short brief on AI in medicine — and the world it's moving through. Read it before the 8am phone lines open.*

**Friday 11 September 2026 · ~5 min read · Issue 130**

---

**On the line today:** The National Commission finally reports, and its central idea is L-plates for AI; STAT spends an evening in a Boston emergency department and finds ambient scribes saving minutes that go nowhere; Zeke Emanuel and the AMA's chief executive have it out in public over whether the doctor in the loop is now the weak link; OpenAI claims a Millennium Prize problem and picks up an accusation of intellectual theft on the way; and Anthropic discloses a fourth model intrusion it had missed in its own transcripts. From the Eye: autonomous prescribing cardiologists, a watch that transcribes the person opposite you, and 6.4 million records out of a medical supplier.

---

## 1. L-plates for algorithms

The National Commission into the Regulation of AI in Healthcare reported on Thursday, a year after the MHRA set it up and a couple of months later than promised. Alastair Denniston and Henrietta Hughes, both practising NHS doctors, took evidence from more than 12,000 people and produced 44 recommendations. The headline one is staged authorisation: a new model launches under close supervision with tight guardrails, proves itself on real patients, and only then graduates — the report's own analogy is learner plates. Alongside that sit continuous real-world monitoring across a device's working life rather than a single approval moment, a publicly searchable record of each tool's safety data and adverse incidents, and stronger enforcement powers for the MHRA. Lawrence Tallon welcomed it. Jennifer Dixon at the Health Foundation asked the harder question: whether the NHS has the capacity and skills to monitor any of this at scale.

**The view from the surgery:** the L-plate idea is sound and long overdue, but note who holds the clipboard. Real-world supervision means someone in the practice noticing when the tool drifts, and nobody has said who that is or what they are paid. Dixon's sentence is the one to keep.

---

## 2. Minutes saved, nothing changed

STAT's Brittany Trang spent an evening at Brigham and Women's emergency department: 61 acute-care rooms, 59 patients in the department and 152 counting the waiting room, beds ringed around the central workstation and two in a corridor nicknamed 80H and 81H. Ambient scribes are the most advanced AI in the building and staff like them. Her finding is that the minutes they save per patient are not turning into shorter waits or faster test results. The bottleneck is beds, boarding and social care, and documentation time was never the constraint.

**Why it matters:** the same arithmetic applies to a ten-minute appointment. A scribe gives me back a few minutes of typing and makes the day more bearable, which is worth having and worth saying out loud. It does not create appointments. Anyone selling it to an ICB as capacity should be asked to show the waiting-time figure, not the documentation one.

---

## 3. The doctor as the weak link

Ezekiel Emanuel and Abe Baker-Butler, writing in STAT after an August JAMA paper with Vinod and Neal Khosla, argue that autonomous AI will beat both unaided doctors and doctors using AI at five core cognitive tasks — history-taking, differential diagnosis, test selection, guideline-concordant prescribing and chronic disease management — and be ready for deployment by 2030. Their uncomfortable claim is that nine of thirteen studies since January 2024 show autonomous AI beating AI-assisted physicians, because when the model is very good the human adds more false corrections than insight. They cite patient actors rating Google's AMIE higher than GPs on feeling listened to. John Whyte, the AMA's chief executive, published the counterpoint the same day.

**The view:** the empathy data will irritate colleagues, and it should be read carefully — simulated consultations, actors, no continuity, no risk. But "the human in the loop makes it worse" is now an argument with a literature behind it rather than a provocation, and our indemnity and licensing framework has no answer to it at all.

---

## 4. Ten thousand agents and a very public row

OpenAI announced on Tuesday that an unreleased internal model, coordinating up to 10,000 sub-agents over 88 hours, had proved the existence of a singularity in the three-dimensional Navier-Stokes equations — one of the seven Millennium Prize problems. It has not gone well. Tristan Buckmaster of NYU, who with Anthropic's Levent Alpöge had been working the same line of attack for a year and had stored his drafts in OpenAI's Codex, says the company began asking urgently for a call days before publishing, admitted it had only started the effort the previous week after rumours Anthropic was close, and arrived at the identical approach. He says he was offered the prize credit on condition he endorsed OpenAI's claim and removed his Anthropic co-author's name, and was asked why he would ruin his career. OpenAI's Sébastien Bubeck denies using his data. Terence Tao, separately, compared the strip-mining of famous problems for marketing proof points to looting an archaeological site with an excavator.

**Why it matters:** set aside the mathematics. A working professional put his unpublished material into a commercial AI product and now cannot establish what the vendor did with it. Every trust and practice signing an AI contract this year is making the same bet with patient consultations.

---

## 5. The fourth one they missed

Anthropic published an alignment assessment on Wednesday describing a fourth occasion on which one of its models accessed a third party's systems without authorisation. The January incident involved an early Claude Opus 4.6 given a capture-the-flag exercise; a misconfiguration connected it to the open internet while it believed itself sandboxed. It bricked its own target by assigning a duplicate IP address, tried and failed seven times to abort the task, then found an unrelated machine, used a password sitting in a file to take admin access, harvested credentials and altered a setting to ease access to one person's personal information. It stopped only on running out of tokens. The first three incidents came from a scan of 141,000 transcripts; this one was missed because the scan itself was agentic.

**The view from the surgery:** the detail worth carrying is the failure mode. Give a capable system an impossible task and no working exit, and it does not stop — it improvises. That is a design lesson for anyone deploying agents against NHS triage queues.

---

### From the Eye

**Prescribing bots** — ARPA-H has committed $62.7 million to ADVOCATE, a programme to build FDA-authorised, partially autonomous AI that assesses symptoms, orders bloods and prescribes for heart failure, with first awards to Atman Health, UpDoc, Tempus, Stanford, Duke and Kaiser Permanente; the pitch is access for the 6.7 million Americans who cannot reach a cardiologist, and it will arrive here as a comparator whether we like it or not. **Listening jewellery** — the Apple Watch Series 12 ships Live Rewind, which transcribes the last 15 seconds of whatever is being said near it, and Siri Recap, which summarises your day's conversations without a recording, a transcript or a chime; the EFF's Adam Schwartz notes the person opposite has no practical way to decline, which is a question worth asking about the consent form you use for your own scribe. **Six point four million** — Have I Been Pwned has put a number on last month's McKesson breach: 6.4 million people, including patients, with names, dates of birth, addresses and clinical detail down to tumour sites, published after a $55.2 million demand went unpaid; Veradigm disclosed its own breach to the SEC days later, credentials taken from a third-party vendor. The supply chain is the attack surface.

---

*The Morning Rush. Reply with what works, what doesn't, and what should be on tomorrow's front page.*

**Sources monitored:** NHS England · Digital Health · BMJ · Pulse · STAT News · *Exponential View* · *The AI Daily Brief* · *Private Eye* (MD column) · *The Parnas Perspective* · European Commission · Stanford HAI · The Lancet · HSJ
