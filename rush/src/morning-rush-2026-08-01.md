# THE MORNING RUSH

*A short brief on AI in medicine — and the world it's moving through. Read it before the 8am phone lines open.*

**Saturday 1 August 2026 · ~5 min read · Issue 092**

---

**On the line today:** tomorrow the EU starts enforcing the one bit of the AI Act it didn't postpone, and it's the bit about telling people they're talking to a machine; a Singapore-led team publishes a foundation model that reads seven kinds of image across a dozen specialties; Maine becomes the fourth US state to make AI therapy illegal; the FDA clears an AI that reads breast ultrasound; and OpenAI starts handing frontier models to a hundred thousand academics for nothing. From the Eye: a classified benchmarking deadline that falls today, five billion dollars for a company with no product, and the four words that let a wearable escape regulation entirely.

---

## 1. Europe's AI Act finally bites — on the honesty clause

From tomorrow, 2 August 2026, Article 50 of the EU AI Act applies. Anything that talks to a person must say plainly and upfront that it is software; synthetic audio, image and video must be machine-readably marked; deepfakes must be labelled *even where there was no intent to deceive*; and AI-generated text on matters of public interest must be disclosed. The Commission adopted its final guidelines on 20 July. Penalties run to €15m or 3% of worldwide turnover. This is the residue of a much larger law: the Digital Omnibus deal pushed the high-risk obligations back to December 2027 for standalone Annex III systems and August 2028 for AI embedded in regulated products — medical devices among them. The Commission's enforcement powers over general-purpose models also switch on tomorrow.

**Why it matters:** note what survived the great deferral. Europe delayed the rules about whether the machine is safe and kept the rules about whether it lies about being a machine. There's a lesson in that. The clause worth reading twice is the narrow exception for editorially reviewed AI text: a human glancing over the output is explicitly *not* enough — it requires substantive oversight with named accountability. That is a far better description of what verifying a scribe letter should look like than anything we've been handed domestically.

---

## 2. One model, seven imaging modalities

*The Lancet Digital Health* published MerMED-FM on 27 July — a multimodal, multidisease imaging foundation model pretrained by self-supervision on around 3.3 million unlabelled images from 53 public datasets, spanning chest radiographs, CT, ultrasound, histopathology, colour fundus photography, OCT and dermatoscopy across more than ten specialties. With only 10% of images labelled, mean AUROCs came in at 0.962 for OCT, 0.908 for histopathology, 0.906 for CT, 0.844 for chest films, 0.827 for dermatoscopy, 0.818 for ultrasound and 0.810 for fundus photography.

**The view from the surgery:** the significance isn't the numbers, which are respectable rather than startling. It's the label fraction. Every AI project I've watched founder in the NHS died on the cost of annotating data, and this says you can get most of the way there with a tenth of it. Note also which modality it's best at and which it's worst at — OCT at 0.962, fundus photography at 0.810. Two eye tests, fifteen points of AUROC apart. Retrospective, benchmark-only, no patients harmed or helped yet.

---

## 3. Maine makes it four

Maine's ban on AI delivering therapy to the public came into force on Wednesday, joining Illinois, Nevada and Rhode Island. Fifteen states have now signed chatbot-specific legislation of some kind, and the approaches diverge sharply: outright prohibition in Illinois and Nevada; Utah's disclosure regime, which forces a mental-health chatbot to state that it is software and limits what it may do with the intimate data users hand it; California's SB 243, requiring companion bots to detect suicidal ideation and signpost help; and Tennessee's SB 1580, live since 1 July, banning any claim that an AI is qualified to act as a licensed mental health professional.

**The view:** a patchwork, and patchworks leak — but the direction is unmistakable, and Britain has nothing equivalent. Our patients are already using these products. They arrive having been talked to for six weeks by something that agreed with everything they said, and nobody has told them it wasn't a clinician. Utah's model is the most transportable: not a ban, just a requirement to be honest about what you are and what you're keeping.

---

## 4. The FDA clears an AI for breast ultrasound

DeepHealth announced 510(k) clearance on 30 July for an AI system that automates lesion detection, characterisation and reporting in breast ultrasound, aimed at standardising a modality notoriously dependent on who is holding the probe. It lands months after the MASAI trial's full results in *The Lancet* — the first randomised evidence in breast AI — showed AI-supported mammography reading was non-inferior on interval cancer rate, produced fewer interval cancers with unfavourable characteristics, matched specificity, improved sensitivity, and cut screen-reading workload by around 44%.

**Why it matters:** ultrasound is the harder problem, because the image doesn't exist until someone acquires it. Standardising the read does nothing about the sweep. Still, MASAI has changed the temperature of these conversations: we now have one randomised trial in this space, and everything else is being sold in its shadow.

---

## 5. OpenAI gives a hundred thousand academics the keys

OpenAI opened ChatGPT for Academic Researchers on 30 July — free frontier access, starting with 10,000 researchers this summer and scaling to 100,000 through 2027, each able to bring in four institutional collaborators. Early sites include the Institute for Advanced Study and the École normale supérieure. Business-grade privacy applies and data isn't used for training by default. It sits inside a stated commitment of over $250m to external research through 2027, alongside the $50m NextGenAI programme. The same week, the company cut prices on its two cheaper GPT-5.6 models by up to 80%.

**The view from the surgery:** generous, and not disinterested. Give a generation of researchers free access during training and you have bought the default tool of the next decade — the pharmaceutical industry worked this out with free samples about sixty years ago. Take the offer, by all means. Just don't mistake it for philanthropy, and read the retention terms before anyone puts patient-derived data anywhere near it.

---

### From the Eye

**Item one** — today, quietly, is a deadline. Under the US executive order of 2 June, the NSA and CISA are due by 1 August to deliver a classified frontier-model benchmarking process and a voluntary pre-release framework. A classified benchmark is an interesting object: a safety standard the public cannot read, applied to products the public will use, by agencies whose day job is signals intelligence. It is the only confirmed governance milestone on the calendar this month and roughly nobody has written about it. **Item two** — NVIDIA has put around $5bn into Safe Superintelligence, giving it access to the Vera Rubin platform and a tenfold compute increase within a year. SSI has no product, no revenue and no stated release date; its entire proposition is that it will build one thing, safely, and ship nothing until then. Five billion dollars is now the price of a promise, and the chip vendor is the one paying it. **Item three** — the FDA's line on wearables, as set out by Commissioner Makary at CES in January and firmed up by the 5 June *Federal Register* guidance on exempting unclassified devices from premarket notification, comes down to a phrase: if you don't claim to be **medical grade**, you're not a medical device. Say your ring tracks sleep, and you're free. Say it measures clinical-grade blood pressure, and you're regulated. The patient reading the number cannot see the difference, and will bring it to you regardless.

---

*The Morning Rush. Reply with what works, what doesn't, and what should be on tomorrow's front page.*

**Sources monitored:** NHS England · Digital Health · BMJ · Pulse · STAT News · *Exponential View* · *The AI Daily Brief* · *Private Eye* (MD column) · *The Parnas Perspective* · European Commission · Stanford HAI · The Lancet · HSJ
