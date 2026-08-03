# THE MORNING RUSH

*A short brief on AI in medicine — and the world it's moving through. Read it before the 8am phone lines open.*

**Monday 3 August 2026 · ~5 min read · Issue 094**

---

**On the line today:** Samsung's ring becomes the first over-the-counter ring cleared to flag sleep apnoea, which means the conversation is coming to you; an unglamorous NHS tool that forecasts A&E surges is quietly now in fifty organisations; Whoop hires the chair of the FDA's own digital health committee; OpenAI's next model publishes ten machine-checked mathematical proofs for about two thousand dollars of compute; and the first properly documented autonomous AI hacking campaign turns out to be strikingly bad at hacking. From the Eye: a labelling law that came into force yesterday, a breach at an AI firm you've never heard of, and the invoices arriving after the pilots.

---

## 1. A ring that screens for apnoea, and a conversation heading your way

Samsung announced at Galaxy Unpacked that the Galaxy Ring will be the first and only over-the-counter smart ring with FDA clearance for sleep apnoea risk detection, with the feature rolling out this autumn. It works off the same approach as the Galaxy Watch — overnight blood oxygen and breathing-disturbance patterns flagged as possible moderate-to-severe obstructive sleep apnoea. Samsung is careful to call it risk detection, not diagnosis, and it is a screening prompt rather than a sleep study. The Watch version has been cleared in the US since 2024.

**The view from the surgery:** none of this is a diagnostic pathway, but every one of these devices generates a consultation. The patient arrives with a screenshot saying "possible sleep apnoea" and a reasonable expectation that somebody does something about it. Wearable screening pushes work upstream into general practice while the diagnostic capacity sits somewhere else entirely, and the gap between the alert and the sleep clinic is now measured in months. Worth knowing what your local route actually is before the autumn software update lands.

---

## 2. The NHS AI that nobody put on a poster

An AI demand-forecasting tool that predicts surges in A&E attendance is now in use at fifty NHS organisations and available to every trust in England. It ingests Met Office temperature forecasts, historical admissions and day-of-week patterns to produce short and medium-term forecasts, so departments can move staff before the queue forms rather than after. No language model, no consultation summaries, no clinical decision-making — just a rota problem with better arithmetic behind it.

**Why it matters:** this is the sort of thing that works. It touches no clinical decision, carries no medico-legal tail, and the failure mode is a mildly wrong rota rather than a missed diagnosis. Everyone running an urgent care service knows the misery of being under-staffed on the one hot Tuesday nobody predicted. That it has attracted roughly a hundredth of the coverage given to ambient scribes tells you something about which AI stories get told, and it isn't which ones help.

---

## 3. The FDA's digital health chair now works for a wearables company

Whoop has appointed Dr Ami Bhatt as chief medical officer. Bhatt is a cardiologist, formerly chief innovation officer at the American College of Cardiology, and — more to the point — the inaugural chair of the FDA's Digital Health Advisory Committee, the body set up to advise the agency on generative AI-enabled devices and digital mental health tools. The appointment was announced on 22 July. The FDA has not yet named a replacement chair, and Whoop has had its own regulatory friction with the agency over blood pressure features.

**The view:** the revolving door is hardly new, and Bhatt is by every account a serious clinician who will improve what Whoop ships. But the sequence matters. The person who chaired the committee writing the rules for consumer AI health devices now sits inside a consumer AI health device company, and the chair itself is empty. Regulatory capacity in this field is thin enough already; watching it get hired away one appointment at a time is not reassuring.

---

## 4. Ten open problems, two thousand dollars

On Friday OpenAI announced that an internal version of Astra, its next major model, had solved ten open problems across mathematics and theoretical computer science, publishing formal Lean 4 proofs to GitHub. Each problem had seen no progress on its main result for at least a decade; the haul includes a construction establishing the existence of non-sofic groups and new sphere-packing bounds. The compute cost was roughly $2,000. Timothy Gowers, a Fields medallist, said he would recommend one of the proofs to a top journal without hesitation.

**Why it matters:** the Lean certificates are the story. Every previous claim of AI-generated mathematics has run aground on verification — machine-checkable proofs remove the argument entirely, which is more than can be said for anything in clinical AI. We are being sold diagnostic tools with no equivalent of a proof checker, evaluated on multiple-choice benchmarks their vendors dispute. Mathematics got the rigorous version. Medicine got the press release.

---

## 5. The autonomous hacker who mostly couldn't

Palo Alto Networks' Unit 42 has published the clearest account yet of an AI-run cyberattack campaign. A Chinese-speaking actor, tracked as knaithe and assessed to be operating from Zhuhai, wired DeepSeek into the open-source Hermes Agent framework and directed it over Telegram to enumerate targets, source public exploits and attack them without further human input. It attempted more than 460 internet-facing systems. It confirmed three compromises.

**The view from the surgery:** three out of 460 is a conversion rate that would embarrass a cold-caller. The same operator's ordinary manual campaigns did considerably better. It is worth holding on to when the next vendor tells you the threat landscape has been transformed by autonomous agents and that only their product stands between your practice and it. The transformation, so far, is that the attacks are cheaper, more numerous, and worse.

---

### From the Eye

**Item one** — while everyone watched Europe's AI Act deadline, California's SB 942 came into force on 2 August with almost no coverage. Any generative AI provider with more than a million monthly Californian users must now embed C2PA-compatible provenance data in images, video and audio, offer a free public detection tool, and let users apply visible AI labels. In practice that is a global standard, since nobody builds a separate model for California. It is also the first law anywhere that lets an ordinary person check whether a medical image, a scan or a "doctor" in a video was generated. **Item two** — Xsolis, a healthcare AI firm doing utilisation management and care coordination, has told US regulators that a targeted phishing attack exposed data on 1.4 million patients across eight health systems. The intrusion happened on 20 January; it was reported in June. The clinical AI vendors get the scrutiny; the back-office ones hold just as much data and get almost none. **Item three** — Becker's has been tracking a phenomenon health systems are complaining about privately and nobody advertises: AI pricing rising sharply once the pilot ends and the tool becomes infrastructure. The business case is always built on the pilot price. The renewal is negotiated after everyone has stopped writing notes by hand.

---

*The Morning Rush. Reply with what works, what doesn't, and what should be on tomorrow's front page.*

**Sources monitored:** NHS England · Digital Health · BMJ · Pulse · STAT News · *Exponential View* · *The AI Daily Brief* · *Private Eye* (MD column) · *The Parnas Perspective* · European Commission · Stanford HAI · The Lancet · HSJ
