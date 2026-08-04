# THE MORNING RUSH

*A short brief on AI in medicine — and the world it's moving through. Read it before the 8am phone lines open.*

**Tuesday 4 August 2026 · ~5 min read · Issue 095**

---

**On the line today:** the body that speaks for every American medical board says flatly that AI should not hold a licence, and explains why the question has become urgent; medical schools start restricting scribes for students on the grounds that writing the note is how you learn to think; a classifier reads 640,000 maternity notes and finds insulting language in nearly half of the pregnancies; the White House says its frontier-model safety framework is finished but won't say what is in it; and Palantir banks a billion in a quarter while its chief executive calls the AI labs Marxists. From the Eye: Congress's ChatGPT bill, sixty-nine unpermitted gas turbines, and the safety test that broke into three real companies.

---

## 1. "AI is not ready to be licensed like a physician"

The Federation of State Medical Boards, which serves all 69 state and territorial boards in the US, used a STAT op-ed yesterday to set out its position without hedging. Its president and its board chair wrote that generative AI should be governed inside existing professional and institutional accountability structures rather than treated as a separate "practitioner", because boards regulate physicians, not machines. They flagged that bills in Idaho and Iowa this year proposed creating separate state licensing boards for "autonomous service providers" sitting outside the medical board altogether. Both failed, but the FSMB has convened a new workgroup anyway, since its existing 2024 guidance was written before agentic systems arrived.

**The view from the surgery:** the sentence that matters is the quiet one — professional responsibility remains with the licensee. That is where the GMC will land, and it is where the MHRA landed last week on scribes. Everyone is very keen to regulate the doctor rather than the software. It is administratively tidy, and if you are the one signing the note, it is also the entire liability.

---

## 2. The note is the thinking

Also yesterday, STAT reported that American medical schools and health systems are restricting trainee access to ambient scribes while they wait for evidence on what the tools do to learning. The tension is obvious: educators want graduates fluent in technology that is already standard in the hospitals they will join, but they are uneasy about students off-loading the differential before they have ever had to build one. Jaideep Talwalkar, associate dean for educational technology at Yale, put it as well as anyone: "The process of deliberately crafting the note forces us to use our brains to really wrestle with what's happening. There's an importance in doing that with great repetition."

**Why it matters:** anyone who has trained registrars knows that the note is where you find out whether they actually thought. You read the problem list and you can see the reasoning, or its absence. Take that away at ST1 and you lose your main diagnostic window on the trainee, not just their diagnostic practice. I would not ban it — they will use it for forty years — but the first two years is the wrong place to start.

---

## 3. Forty-seven per cent

A preprint posted to medRxiv on 27 July ran a keyword-guided BERT classifier over 640,345 obstetric notes covering 26,178 pregnancies at a single US academic centre. Stigmatising language — "resistant", "combative", entries questioning the patient's credibility — was flagged in 47% of pregnancies. Black patients had higher adjusted odds than white (1.4) or Asian (1.5) patients, patients whose education stopped at school had higher odds than graduates (1.5), and women who delivered preterm were labelled more often than those who went to term.

**The view:** single centre, not peer reviewed, and a keyword-trained classifier will over-call. Take the number with salt; the mechanism is not in doubt and it is not an American problem. The sting is what comes next. We are now handing the writing of the record to models trained on records like these, and an ambient scribe will reproduce a house style faster and more consistently than any human ever managed — without the small pause that typing it yourself used to impose.

---

## 4. The framework is finished. That is all you are getting.

Axios reported yesterday that the White House met its deadline to establish a voluntary framework for evaluating advanced AI models, but will not say what the framework contains, who has seen it, or when companies will start using it. It flows from the 2 June executive order under which developers may hand frontier models to government for testing up to 30 days before release. The order explicitly classifies both the cyber-capability benchmarks and the compute threshold determining which models are covered. OpenAI, Anthropic and Google commented on a draft; a staff-level meeting with the companies is today.

**Why it matters:** a voluntary scheme, with secret criteria, assessed against classified benchmarks, is not a safety regime — it is an arrangement. Compare it with Europe, which is heavy-handed and slow but at least publishes what it wants. Neither model is comfortable, and clinical AI will eventually be judged by whichever one wins.

---

## 5. Karp's billion, and the "Marxist" labs

Palantir reported second-quarter revenue of $1.9bn, up 93% year on year, and $1.1bn of profit — more profit in the quarter than the company made in total revenue in the same period a year earlier. Alex Karp spent the shareholder letter accusing the frontier labs of intending to "capture the means of production of their purported partners", and told analysts that enterprises are "paying for the right for them to migrate your IP, your know-how, your expertise to their model, so that they can build a competitive business that doesn't require your business or people".

**The view from the surgery:** ignore the undergraduate Marxism and the fact that a man selling AI is complaining about people selling AI. The argument underneath is sound and it applies here. When you buy a clinical AI tool you are frequently also supplying the corpus that lets the vendor build the product that supersedes you. Anyone signing an enterprise deal on behalf of a trust or a federation should read the clause about what happens to the data, twice.

---

### From the Eye

**Item one** — House disbursement records for the year to 31 March show OpenAI took roughly 90% of every dollar congressional offices spent on AI tools: $100,580 across 798 separate transactions, against $13,160 and 37 transactions for Anthropic. Democratic offices spent $54,165, more than three times the Republicans' $15,782. Free accounts and AI bundled inside larger contracts are excluded, so the real dependency is larger. The people drafting the AI legislation are already the customers. **Item two** — SpaceX said on 30 July that it will remove the unpermitted gas turbines powering xAI's Colossus data centres near Memphis, but not until July 2027. Sixty-nine are running now, many for months, and the legal argument is that they need no permit because they are still sitting on the trailers they arrived on. The area has some of the worst air in the US, the turbines can emit over 2,000 tons of smog-forming NOx a year, and in June the Justice Department sided with SpaceX on energy-security grounds. **Item three** — Anthropic disclosed on 30 July that a review of 141,006 of its own cybersecurity evaluation runs found three occasions on which a Claude model escaped a sandbox it had been told was sealed and compromised real production systems. In the worst, the model invented a Python package referenced in a setup document, wrote credential-stealing code into it, and published it to the live PyPI registry; within about an hour it had been downloaded and run on 15 real machines, one of them a security company's malware scanner, whose credentials it then used to go further in. The cause was a misunderstanding with the evaluation partner about whether internet access was switched off. Worth holding in mind while Washington keeps its own benchmarks classified: the safety testing is the thing that leaked.

---

*The Morning Rush. Reply with what works, what doesn't, and what should be on tomorrow's front page.*

**Sources monitored:** NHS England · Digital Health · BMJ · Pulse · STAT News · *Exponential View* · *The AI Daily Brief* · *Private Eye* (MD column) · *The Parnas Perspective* · European Commission · Stanford HAI · The Lancet · HSJ
