# THE MORNING RUSH

*A short brief on AI in medicine — and the world it's moving through. Read it before the 8am phone lines open.*

**Wednesday 12 August 2026 · ~5 min read · Issue 103**

---

**On the line today:** the single statistic holding up the national AI triage rollout has been referred to the statistics watchdog, because nobody outside NHS England can see how it was calculated; a very large study of what doctors actually change in ambient scribe drafts finds we spend our time putting the uncertainty back in; twelve American health systems have stopped piloting alone and formed a diagnostic AI club with the vendor sitting inside it; OpenAI has shipped a model built to write working exploits; and the electricity AI drinks is now physically wrecking the buildings it's drunk in. From the Eye: Interpol counts the machines in African cybercrime, the scribe turns out politer than the doctor, and America grows a patchwork of laws on AI therapists while we grow none.

---

## 1. The 29 per cent that nobody can check

When NHS England announced national AI triage through the NHS App, one figure did the heavy lifting: a Sussex pilot practice cutting the number of people queuing on the phone by 29 per cent. Carl Heneghan and Tom Jefferson went looking for it. The published preprint on that pilot reports concordance between the AI and GP decisions, clinician interviews and patient satisfaction — but no call volumes, no queue analysis, no 29 per cent. After weeks of chasing by the Sunday Express's Lucy Johnston, NHS England confirmed the number came from an unpublished internal evaluation of GP telephony data comparing two five-month periods. The pair wrote again on 29 July asking whether there had been a pre-specified protocol. No reply. They have now referred it to the Office for Statistics Regulation.

**The view from the surgery:** a single-practice before-and-after with no published protocol and no stated denominator is the sort of thing we'd take apart in a journal club before the coffee got cold. It may well be true — that isn't the point. It is being used to justify a rollout reaching every NHS App user by 2028, and nobody outside the building can see the working. If the evaluation is sound, publishing it costs nothing.

---

## 2. Doctors are putting the doubt back in

A paired analysis of 62,811 ambient AI draft note sections against the clinician-finalised versions finds we add hedging language considerably more often than we remove it. "Possible", "likely", "appears" get introduced into text the machine wrote flat and certain, and where clinicians swap one phrase for another the direction of travel is systematically towards greater uncertainty, not less. The effect varied widely between vendors and specialties.

**Why it matters:** the scribe writes like a confident F1 — everything asserted, nothing qualified. Clinical hedging isn't padding; it's the record of what you did and didn't know at 9.40 on a Tuesday, and it's what protects you two years later. We're catching it, which is reassuring. It also means safety currently rests on tired clinicians reading every line, and raises an obvious question about the notes signed off by whoever isn't.

---

## 3. Twelve health systems stop piloting alone

Yesterday twelve US health systems announced a Diagnostic AI Consortium with Aidoc: co-designed diagnostic workflows, shared measurement of safety, quality and speed to diagnosis across member sites, and common implementation and governance practice. Aidoc supplies the plumbing — its CARE foundation model and aiOS platform. First results promised in 2027.

**The view:** the instinct is right and overdue. Everyone has been evaluating the same tools separately, badly, and calling it a pilot. The flaw is that the vendor supplies the technology and sits inside the body assessing it, so the governance framework and the sales channel are the same object. Still, a joint evaluation across NW London providers would beat fifteen separate ones.

---

## 4. OpenAI ships a model built to break things

On Monday OpenAI released GPT-5.6-Cyber, built on GPT-5.6-Sol and trained to find zero-days and construct exploit chains, with a deliberately lowered refusal rate for dual-use requests. Its own testing reports 95% completion on prompts covering exploit chains, privilege escalation and authentication bypass, against 1.5% for the general model, and it answers up to 98.5% of security queries otherwise blocked. It has already turned up two unknown Chrome vulnerabilities. Access is limited to a "Daybreak Red" tier — the big consultancies and security vendors: Accenture, IBM, PwC, EY, KPMG, Capgemini, CrowdStrike, Palo Alto, Sophos, Fortinet, Akamai, Cloudflare.

**Why it matters:** the defensive case is real — better your side finds the hole first. But an offence-grade capability now exists as a product with a customer list, and the gap to an equivalent open-weights model is measured in months. Trusts are still running kit that fell over in 2017.

---

## 5. The power swings are eating the buildings

Training runs make hundreds of thousands of GPUs ramp up and down within milliseconds, and Bloomberg reported last week that the resulting swings — exceeding equipment design tolerances by up to 50% — are physically damaging data centre plant. Batteries, generators, transformers and cooling are failing far earlier than planned; cranks have snapped off gas engines, and turbines at xAI's Colossus site in Memphis developed cracks. Lenders already nervous about hyperscaler spending now have a depreciation question as well as a demand one.

**The view from the surgery:** the least glamorous constraint on AI turns out to be metallurgy. Everyone modelled chips, power contracts and water; nobody modelled what a decade of millisecond load cycling does to a transformer. The physical layer under all this is younger and more fragile than the confidence attached to it.

---

### From the Eye

**Item one** — Interpol's African Cyberthreat Assessment, drawing on 36 member countries, finds AI now enabling up to 55% of reported cybercrime on the continent, losses more than doubling since 2024 to $484m, and scam centres operating in 72% of countries surveyed; deepfakes and synthetic identities are routinely defeating biometric checks, which should give pause to anyone piloting face-based patient ID. **Item two** — the companion paper to today's item two is the uncomfortable one: across 66,297 paired note sections, stigmatising language appeared in 21.4% of AI drafts and 24.0% of the clinician-finalised versions, doctors introducing such terms more often than removing them. The machine was the more courteous author, and the human in the loop was the one making the note worse. **Item three** — America is quietly assembling a patchwork on AI therapists: four states now bar AI from delivering therapy to the public, Illinois and Nevada joined by Rhode Island and Maine as of late July, while Utah mandates disclosure and New York, California and Nebraska impose crisis-referral and minor-protection duties; 36 states filed more than 70 chatbot bills in the first quarter alone. We have nothing equivalent, and your sixteen-year-old with low mood has all of them on her phone this morning.

---

*The Morning Rush. Reply with what works, what doesn't, and what should be on tomorrow's front page.*

**Sources monitored:** NHS England · Digital Health · BMJ · Pulse · STAT News · *Exponential View* · *The AI Daily Brief* · *Private Eye* (MD column) · *The Parnas Perspective* · European Commission · Stanford HAI · The Lancet · HSJ
