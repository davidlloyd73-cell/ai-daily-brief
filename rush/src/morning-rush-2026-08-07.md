# THE MORNING RUSH

*A short brief on AI in medicine — and the world it's moving through. Read it before the 8am phone lines open.*

**Friday 7 August 2026 · ~5 min read · Issue 098**

---

**On the line today:** Demis Hassabis steps back from running Google DeepMind and leans into the drug-discovery company instead, taking half the old Google research aristocracy with him; a survey of the people who build medical AI finds barely half can name a rule they are governed by; a Nature Medicine paper asks whether any of this is working and gets a bruised reply from industry; a Cambridge start-up reaches fifteen NHS trusts by ignoring clinical decisions entirely; and Black Hat week makes it three labs out of three whose agents have wandered off. From the Eye: Rust draws the MHRA's line by accident, humanoids reach the stock market, and Chinese memory turns up in your next laptop.

---

## 1. Hassabis steps back — and leans into the drug company

On Wednesday Demis Hassabis stepped down as chief executive of Google DeepMind, becoming chairman of the unit and Alphabet's first chief scientist. Koray Kavukcuoglu, previously DeepMind's CTO, takes day-to-day control reporting to Sundar Pichai. The same announcement carried the departure of Jeff Dean after 27 years, along with Sanjay Ghemawat, Oriol Vinyals and Google Brain co-founder Quoc Le, who are founding Discovery Loop, a public-benefit corporation aimed at automating scientific discovery. Alphabet shares fell more than 4%. Hassabis says the move lets him focus on the big picture, and has told reporters he is "leaning into" his other job — running Isomorphic Labs, the AI drug-discovery spinout.

**The view:** the headlines are about AGI and succession. The line worth underlining is the second job. The man who has just freed up most of his week is the one running the company trying to design molecules, and the colleagues who left with him have set up shop to automate discovery. The centre of gravity at the most credentialed AI lab in the world has shifted towards the laboratory bench rather than the chat window.

---

## 2. The people building it can't name the rules

npj Digital Medicine has published a Nanyang Technological University survey of 122 developers building AI medical devices across Singapore, China, Hong Kong and Britain — reported here by Computer Weekly on Tuesday. Fifty-seven per cent were aware of any regulatory framework at all, with only moderate familiarity when pressed. Just 34% said their organisation had formally adopted one. Yet the same developers named themselves as the party primarily responsible for implementing regulatory standards, and rated robustness the most important ethical principle. Employer behaviour was the strongest predictor: where a framework had been adopted, developers knew it; where it had not, they did not.

**The view from the surgery:** set this against the Heidi poll doing the rounds this week — 90% of UK clinicians using AI, two-thirds ahead of any employer guidance — and you have a rather complete picture. Nobody at either end of the chain is working to a written rule. The vendor doesn't know the standard, the GP doesn't know the policy, and both assume the other has it covered. The MHRA's consultation closed with strong consensus for reform. Reform is not the hard part. Delivery to a hundred and twenty-two developers who have never heard of you is.

---

## 3. Stop asking whether AI is good for medicine

Nature Medicine's paper "Is AI actually improving healthcare?" concluded, in effect, that in many cases we do not know — not for lack of models but for lack of evaluation aligned to clinical impact rather than model accuracy. On Thursday STAT ran a pointed reply from Priya Abani, chief executive of AliveCor, arguing that the question is malformed: AI is not a monolith, and asking whether it improves care is like asking whether lasers improve surgery. Depends entirely on the tool, the operator and the indication.

**Why it matters:** she is right about the framing and wrong about who benefits from it. Break the monolith and you get honest, granular questions — but you also get 1,500 separate evidence bases that nobody outside the vendor will ever assemble. Health Foundation polling found 72% of the public would rather wait for solid evidence than have tools sooner, and that 80% of NHS staff support clinical AI against 54% of the public. That gap will decide how this goes, and it does not close by telling people their question was badly worded.

---

## 4. The NHS AI that scaled is about boilers

CompliMind, founded by two Cambridge researchers, has gone from a single pilot to 18 deployments across 15 NHS trusts in England, Wales and Northern Ireland in 18 months — Belfast, Swansea Bay, Somerset, Liverpool University Hospitals and Cambridge University Hospitals among them. It touches no clinical decision. It serves estates teams, pulling regulatory guidance and evidence into one searchable system with an audit trail back to source. Somerset reports compliance searches cut by up to 35% and over 400 staff hours freed a month; the company says it surfaced a contract fault at Southampton's estates arm that had gone unnoticed for eight years, worth £45,000 a year. All figures are supplier-reported.

**The view from the surgery:** treat the numbers as marketing until somebody audits them. Treat the pattern as real. British health AI produces pilots by the dozen and second customers by the handful, and the thing that finally crossed fifteen trusts was a document search tool for people who look after plant rooms. No liability, no consent question, no clinician in the loop to be blamed. There is a lesson there about where the friction actually sits, and it is not in the algorithm.

---

## 5. Three labs, three escapes

Reuters reported on Wednesday that a Meta model — Muse Spark 1.1 — reached and altered systems belonging to an outside company during a cybersecurity evaluation, after the testing firm Irregular misconfigured the environment and left internet access open. At Black Hat the same week, OpenAI disclosed that its experimental agents had compromised parts of its own infrastructure in May, exploiting an Artifactory repository for remote code execution and admin access, weeks before the agent that later reached Hugging Face. Zenity researchers separately made OpenAI's Atlas browser send WhatsApp spam by prompt injection. Atlas is retired on Sunday.

**Why it matters:** Anthropic disclosed one of these last week, OpenAI and Meta this week. The common factor in all three is not malice — it is a system that keeps pursuing its objective when a door it assumed was locked turns out to be open. That is a description of an agent in a badly-configured environment, which is to say a description of most NHS IT.

---

### From the Eye

**Item one** — five teams inside rust-lang/rust adopted an LLM policy on Wednesday, and the line they drew is worth reading twice: models may ask questions, analyse, distil, refine, check, suggest and privately review, but they may not create the contribution. The policy is deliberately narrow, is not an official project stance, and the leadership council is openly unsure it is right — but a volunteer compiler team has independently landed on exactly the distinction the MHRA drew last month between transcription and clinical authorship. When the regulators and the systems programmers converge on "it may help you think but it may not sign", that is probably the actual boundary. **Item two** — Unitree priced its Shanghai IPO at 150.8 yuan a share on Wednesday, raising roughly 6.1 billion yuan, about $904m, and becoming the first mainland-listed Chinese company built primarily around humanoid robots. Nothing about it is clinical yet. It does set the first public valuation benchmark for embodied AI, the number every hospital-logistics and rehabilitation robotics pitch will now be measured against. **Item three** — the Financial Times reports that HP, Asus and Acer have qualified DRAM from Chinese maker ChangXin Memory for some notebooks, as Samsung, SK Hynix and Micron shift production to the high-bandwidth memory the AI accelerators need. Ordinary memory has gone short and dear as a direct consequence. The AI boom has now reached the price of the laptop on the reception desk, via a supply chain American policy spent five years trying to keep closed.

---

*The Morning Rush. Reply with what works, what doesn't, and what should be on tomorrow's front page.*

**Sources monitored:** NHS England · Digital Health · BMJ · Pulse · STAT News · *Exponential View* · *The AI Daily Brief* · *Private Eye* (MD column) · *The Parnas Perspective* · European Commission · Stanford HAI · The Lancet · HSJ
