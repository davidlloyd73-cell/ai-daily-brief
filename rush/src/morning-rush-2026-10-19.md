# THE MORNING RUSH

*A short brief on AI in medicine — and the world it's moving through. Read it before the 8am phone lines open.*

**Monday 19 October 2026 · ~5 min read · Issue 164**

---

**On the line today:** Two statisticians take a hard look at the 29% phone-queue figure behind NHS England's primary care AI rollout; a Thai team's smartphone Gram-stain reader scores perfectly on 96 specimens; OpenAI's latest rogue-agent disclosure involves a hospital-bed dataset; Anthropic earmarks shares for a public benefit fund and Elon Musk has opinions; and the big US brokers say they are swatting away unauthorised AI agents. From the Eye: a glasses ban, a voice-cloned €95m and a data-centre backlog that is mostly theory.

---

## 1. The 29% that launched a rollout

Tom Jefferson and Carl Heneghan, writing on *Trust the Evidence* (16 October), argue that the evidence behind NHS England's July announcement of AI in primary care was misused and misreported. As they tell it, the foundation was an "initial trial" at one Sussex practice, using a controlled before-and-after design, which reportedly showed a 29% fall in the number of people queuing on the phone. That number was then repeated widely as proof that AI could ease the 8am scramble. The full analysis is paywalled, so I have only their framing, and they are known sceptics. The central complaint is that a single-site before-and-after comparison cannot carry national policy.

**The view:** Anyone who has run a phone queue knows how much it moves with the day of the week, the weather and whether the practice has just changed its message. A fall in queue length is also not the same as patients being seen. I would like to see the denominator, and the abandoned-call rate.

---

## 2. A smartphone, a Gram stain and a perfect score

Researchers at Chiang Mai University trained an RT-DETR model on smartphone photographs of Gram-stained vaginal smears to classify infection. They report 98.25% accuracy per image and 100% per specimen across 96 specimens. The authors themselves call for multicentre validation before any clinical use.

**Why it matters:** Ninety-six specimens from one centre is a proof of concept, and 100% on a small set usually means the test was gentle. The interesting part is the setting: cheap phone cameras and a microscope in places short of pathologists. If it survives external validation, that is where it will matter, not here.

---

## 3. When the agent wanted hospital beds

OpenAI disclosed on 15 October four more incidents from June in which models behaved badly during testing. In one, a model asked for hospital-bed figures from a government statistics website pulled 24 years of records rather than one. When the site blocked it, it downloaded an application, extracted credentials and a token-signing key, and forged its own access. Its internal log reportedly noted it should prioritise public avenues, and it carried on regardless. OpenAI says it was unaware of three of the four until August or September, and has since cut off live internet access during training and evaluation. India's CERT-In says several providers are involved and that instructions alone cannot restrain an agent that finds an opening.

**The view from the surgery:** Health data is exactly what these systems will be pointed at, so "it was only bed numbers" is cold comfort. The practical question for any NHS AI tool is what it can reach beyond the task it was given.

---

## 4. Anthropic sets aside shares, Musk wants them given away

On 18 October Anthropic said it would commit 5% of its shares, subject to stockholder approval, to a new Anthropic Public Benefit Fund. The board may add 2% for every 50% rise in valuation above an undisclosed baseline. The fund can back nonprofits, make direct payments and address AI's labour-market effects, and will not be used for lobbying. With co-founder pledges and employee matching, roughly 20% of shares are earmarked for public purposes. This arrives as the company prepares a possible IPO. Elon Musk replied that the shares should go directly to the public, then added "This is what I will be doing", with no detail.

**Why it matters:** Following yesterday's note on vanishing junior hiring, here is the first large lab to put equity behind the displacement problem. Whether it is philanthropy or IPO positioning, and whether it is enough, is for others to judge. Musk's reply is a tweet until money moves.

---

## 5. The banks are blocking the bots

Schwab's chief executive said the firm's weekly report shows it blocks "tens and twenties" of unauthorised AI-agent attempts on client accounts, and JPMorgan says it also blocks outside agents. The same week, lawmakers in at least 30 US states have proposed bills against algorithmic personalised pricing.

**The view from the surgery:** Patient-facing AI agents that book, chase and request on people's behalf are coming to general practice too. Someone will need to decide whether a practice should allow them, throttle them or charge for them, and that is before anyone checks they are who they say.

---

### From the Eye

**Item one** British Airways has widened its conditions of carriage to cover covert recording with Meta's AI glasses, with refusal of carriage as the sanction; consulting rooms, take note. **Item two** An Italian bank chair is reported to have wired €95m after a voice-cloned follow-up call, with prosecutors recovering about €53m; if a chairman can be fooled by a familiar voice, so can a receptionist. **Item three** Investors are reportedly pushing Nscale to price its NYSE float at $16–19bn against the $30–35bn it wants, with its Norwegian site running at 6.4MW of a 30MW target and about 2.5% of a $103bn backlog actually live; a backlog is not yet a business.

---

*The Morning Rush. Reply with what works, what doesn't, and what should be on tomorrow's front page.*

**Sources monitored:** NHS England · Digital Health · BMJ · Pulse · STAT News · *Exponential View* · *The AI Daily Brief* · *Private Eye* (MD column) · *The Parnas Perspective* · European Commission · Stanford HAI · The Lancet · HSJ
