# THE MORNING RUSH

*A short brief on AI in medicine — and the world it's moving through. Read it before the 8am phone lines open.*

**Sunday 2 August 2026 · ~5 min read · Issue 093**

---

**On the line today:** the medical chatbots sold to doctors as the safe alternative have lost a head-to-head against the ordinary ones, and the industry is arguing about the scoreboard; the FTC sues a telehealth giant for handing patients' conditions to Meta and Snap; Mayo opens its data platform to a São Paulo hospital in a quiet fix for a real problem; Microsoft says its own small models are 89% cheaper than the frontier it helped build; and Zuckerberg tells investors billions of us will soon have an agent managing our health. From the Eye: adverts written for machines to read, a forum caught with 100,000 posts by a colleague who doesn't exist, and 83 jobs going in a health system's analytics department.

---

## 1. The clinical chatbots lost to the ordinary ones

Hundreds of thousands of American doctors now use purpose-built clinical large language models — OpenEvidence, Doximity, UpToDate Expert AI — sold explicitly as the grown-up alternative to hallucination-prone general models. In June, researchers at NYU Langone put them head-to-head against general frontier models across three sets of clinical questions and published the result in *Nature Medicine*: the clinical tools performed worse. STAT reported on Wednesday that the paper has caused more argument in the health-AI community than anything in recent memory, with Kaiser Permanente's VP for AI saying he'd never seen a single paper trigger reactions like it. Vendors are now disputing the benchmarks themselves — the questions, the scoring, whether multiple-choice sets resemble clinical work at all.

**The view from the surgery:** the vendors have a point about benchmarks, and it is a point that cuts both ways. If the tests can't tell a good clinical model from a bad one, then every reassuring number in every sales deck is worth exactly as little as this one. What the study really punctures is the premise we've all been sold — that a medical wrapper round a general model is inherently safer than the model underneath. On this evidence the wrapper may just be adding cost and confidence.

---

## 2. The FTC sues Hims & Hers over what it did with the diagnoses

On Wednesday the Federal Trade Commission, joined by Utah and California, sued Hims & Hers. The complaint alleges the telehealth company shared customers' sensitive health information with third-party advertising platforms including Meta and Snap — both by handing over customer lists and via tracking pixels that fired "events" as people moved through the site — while promising privacy. It also alleges the sign-up flow buried the fact that filling in a medical history enrolled you in an auto-renewing subscription, and that before 2023 you could only cancel by phone, email or chat. The claims run under the FTC Act and the Restore Online Shoppers' Confidence Act.

**Why it matters:** the tracking pixel is the mechanism to understand here, because it is on a great many health websites and it does not care what you promised in your privacy policy. Nobody at Hims had to decide to tell Meta that a particular man was seeking treatment for erectile dysfunction; the tag did it automatically the moment he loaded the page. Worth remembering when a patient tells you they've ordered something online — the transaction may have had more parties to it than they know.

---

## 3. Mayo opens the door to São Paulo

Mayo Clinic Platform announced on Thursday that de-identified clinical data from Hospital Israelita Albert Einstein in São Paulo is now available through its privacy-preserving research ecosystem — data stays put, models travel to it. The stated aim is blunt: South America is barely represented in the datasets on which medical AI is being built, and adding a large Brazilian cohort widens the population these tools have ever seen.

**The view:** this is the least glamorous and possibly most useful item this week. Every algorithm we are being offered was trained somewhere, on someone, and the "someone" has overwhelmingly been North American and northern European. In a Harrow surgery that matters more than most places in England. A dermatology model that has never seen the skin on my afternoon list is not a clinical tool, it's a liability — and no amount of headline AUROC fixes it.

---

## 4. Microsoft says the frontier is now optional

Microsoft released two in-house models last week — MAI-Image-2.5-Pro and MAI-Voice-2-Flash — and disclosed how far its own models have quietly spread through Bing, PowerPoint, OneDrive, Dynamics 365, GitHub Copilot and Azure. The claim attached is the interesting part: up to 89% lower GPU costs than the OpenAI models they replace in some production deployments, with many workloads now running on older hardware. Microsoft is also packaging the method as an Azure product.

**Why it matters:** for two years the assumption has been that serious work needs the biggest available model. Microsoft — which owns a large slice of the company selling the biggest available model — is now saying out loud that most tasks don't. If a purpose-trained small model can do transcription or summarising at a tenth of the running cost, the economics of putting AI into an NHS trust change completely, and so does the argument that the NHS can't afford it. The 89% is a vendor's number. The direction isn't.

---

## 5. Zuckerberg puts health on the agent list

Meta told investors last week it expects billions of people to have personal AI agents within five years, continuously managing finances, health, relationships and household admin, with WhatsApp as the place they meet. The company has already started shipping the shallow end: Meta AI now runs recurring tasks — daily briefings, calendar summaries, weekly meal planning — on a model called Muse Spark 1.1, in selected markets first.

**The view from the surgery:** note the platform. WhatsApp is where a very large number of my patients already conduct their lives, and an assistant that manages "health" inside it will not be a regulated medical device, will not have been evaluated by anyone, and will not think of itself as giving advice. It'll just be the thing that reminds you about your tablets and then, one evening, offers a view on your chest pain. Meal planning is the wedge.

---

### From the Eye

**Item one** — *Time* has begun serving advertisements to machines. Working with ad-tech firm Mobian, it now inserts sponsored FAQ-style content into the markdown versions of its articles that AI crawlers ingest — copy written to be read by a model, not a human, and to shape what the model later says about a brand. Nobody has yet asked what happens when a supplement company does this to health content, but somebody will. **Item two** — Google has issued a manual "thin content" penalty against a long-running forum that had, according to SEO observers, more than 100,000 replies generated by a chatbot presented to users as a member of staff. Not a rogue user: house policy. The penalty is for thinness, incidentally, not for the impersonation, which nobody seems to regulate at all. **Item three** — MaineHealth is cutting 83 posts from its IT and analytics departments in a consolidation. That is the version of the AI jobs story you won't see on a conference slide: not clinicians replaced by robots, but the people who look after the data quietly reorganised away, in the same season everyone insists data is the strategic priority.

---

*The Morning Rush. Reply with what works, what doesn't, and what should be on tomorrow's front page.*

**Sources monitored:** NHS England · Digital Health · BMJ · Pulse · STAT News · *Exponential View* · *The AI Daily Brief* · *Private Eye* (MD column) · *The Parnas Perspective* · European Commission · Stanford HAI · The Lancet · HSJ
