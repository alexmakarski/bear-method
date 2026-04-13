---
name: bear
version: 4.0.0
description: "BEAR (Buyer Environment Analysis & Repositioning). Diagnoses why business development stopped working by analyzing market shifts, competitive convergence, and buyer environment changes. Covers all symptom types: ad performance decline, close rate collapse, referral source drought, and pipeline stall. Produces a temporal market diagnosis with repositioning recommendations. Use when results changed but the business didn't, or when entering a new market and needing competitive landscape intelligence."
interface: "invoke: /bear diagnose {client-name}"
modes: [diagnose]
author: Alex Makarski
---

# BEAR: Buyer Environment Analysis & Repositioning

## What This Skill Does

BEAR answers: "Your business development stopped working. Here's why, and the cause isn't inside your business."

It reads market signals, analyzes the client's competitive environment, identifies what shifted, and produces a diagnosis with repositioning recommendations.

BEAR is not an ad grader. It's not an operational audit. It diagnoses the market environment outside the client's business: the forces that changed what buyers want, who they compare you to, and why they say yes or no.

---

## Symptom Taxonomy

BEAR diagnoses multiple presenting symptoms. The symptom type determines which signals to prioritize.

### Type A: Acquisition Decline
"Leads dried up. Traffic dropped. CPAs doubled."

The top of funnel broke. Fewer people are entering the pipeline. This is the classic ad performance problem, the one most graders and agencies focus on.

**Signal priority:** Google Trends demand data, competitive ad landscape, platform changes, CPC/CPM trends.

### Type B: Close Rate Collapse
"Leads are still coming in, but deals aren't closing like before."

The top of funnel still works. The buyer's evaluation environment changed. By the time they're comparing options, something shifted in their decision criteria, competitive alternatives, or risk tolerance. They enter the pipeline on the old desire but the close requires addressing a new one.

**Signal priority:** Competitive positioning convergence (are all proposals sounding the same?), demand shifts at the decision stage (what do buyers care about NOW when evaluating?), new market entrants changing expectations, external shocks affecting buyer confidence.

### Type C: Referral Drought
"Referrals used to be our main source. They've gone quiet."

Referral sources dry up when the referrer's confidence in recommending you erodes. This happens when: the market shifted and the referrer isn't sure you're still the best fit, a new competitor gave the referrer a better experience, the referrer's own network changed what they value, or external conditions made the referrer more cautious about putting their name on a recommendation.

**Signal priority:** What changed for the referrer's audience (not just yours), new competitors the referrer might be hearing about, shifts in what "safe recommendation" means in the vertical, economic/regulatory changes that make referrers risk-averse.

### Type D: Pipeline Stall
"We have leads. We have proposals out. Nothing is moving."

Deals are entering the pipeline but stalling at evaluation or decision stage. Buyers aren't saying no. They're not saying anything. This is often a combination of competitive convergence (all options look the same so there's no urgency to choose) and external shock (economic uncertainty, regulatory changes, or macro anxiety causing decision paralysis).

**Signal priority:** Competitive convergence at the proposal level, economic indicators affecting buyer confidence, external events causing decision paralysis across the vertical, whether stall is industry-wide or client-specific.

**B vs D disambiguation:** These two look similar but the buyer behavior is different. In Type B, buyers evaluate and choose someone else. They're saying no. In Type D, buyers go silent after receiving a proposal. They're not saying no; they're not saying anything. The diagnostic question: "Are prospects choosing competitors, or are they going quiet?" Choosing competitors = B (something changed in how they compare you). Going quiet = D (something is stopping them from deciding at all). If both are happening, classify as E and let the evidence sort it out.

### Type E: Mixed / Unclear
"Everything just... slowed down."

Multiple symptoms present simultaneously, or the client can't isolate which part of the funnel broke. Run signal collection across all priority areas and let the evidence determine the diagnosis.

**Signal priority:** Broad scan across all signal types. The diagnosis will surface which symptom type(s) are actually in play.

---

## Modes

### `/bear diagnose {client-name}`
Full engagement. Captures current market state, reconstructs baseline from historical data, diffs the two, classifies the shift, and produces repositioning recommendations. This is the standard BEAR deliverable. If a prior diagnosis exists locally, produces a What Changed section comparing the two.

---

## Inputs Required

Collect from the user before starting:

### Must have
1. **Client name and website URL**
2. **Market/vertical** (e.g., "window coverings in a major metro", "B2B SaaS for HR teams")
3. **Industry tag**: select from the Signal Registry below. This determines which additional data sources to pull in Phase 1E. If the client doesn't fit a predefined tag, use `general` and rely on the baseline signals only. Ask the user to confirm or correct the tag.
4. **5-10 target keywords** the client competes on (paid or organic; these drive the Trends and competitive research)
5. **Target geography** (city, state/province, country). This also sets the **locale** for the entire engagement: spelling, terminology, currency, and data sources. See the Locale rule in Quality Standards.
6. **Symptom description**: classify into Type A-E from the Symptom Taxonomy above. Ask:
   - What specifically changed? (leads down? close rate down? referrals stopped? pipeline frozen?)
   - When did it start?
   - How bad is it? (numbers if possible: "close rate went from 40% to 15%", "referrals dropped from 8/month to 1")
   - Did anything change inside the business during that period? (new sales rep, pricing change, service change)

### Should have
7. **Competitor list** (5-15 competitors, or permission to identify them via research)
8. **Performance data** (varies by symptom type):
   - Type A (acquisition decline): CPA, ROAS, CPC, impression share over last 3-12 months
   - Type B (close rate collapse): close rate by month/quarter, average deal cycle length, proposal win rate
   - Type C (referral drought): referral volume by month/quarter, referral source breakdown, when each source went quiet
   - Type D (pipeline stall): pipeline stage duration, deals stuck by stage, proposal-to-close timeline
   - Type E (mixed): whatever they have
9. **Current positioning / messaging** (ads, website, pitch deck, proposals, whatever the buyer sees)
10. **Timeframe of decline** (when did it start? "since Q3 2025", "last 6 months", etc.)

### Nice to have
11. **Historical positioning** (what they said/pitched before the decline)
12. **Industry context** (anything the client suspects changed: new competitors, regulation, platform updates)
13. **Previous audit reports** (if they exist)
14. **Sales conversation notes** (for Type B/D: what are buyers saying when they stall or say no? what objections changed?)

---

## Signal Registry

The signal registry maps industry tags to additional data sources beyond the baseline (Google Trends, competitive landscape, economic context). When an industry tag is set, Phase 1E automatically expands to include the relevant signals.

### Baseline signals (every engagement)

These always run regardless of industry tag:
- **1A. Google Trends**: keyword interest, rising/declining queries, breakout terms
- **1B. Competitive Landscape**: positioning, convergence, desire mapping
- **1C. Economic and Platform Context**: macro indicators, platform changes, news
- **1D. Client Position**: messaging, performance data, differentiation

### Supply flood signals (run when Category Dissolution is suspected)

When symptoms suggest a supply flood (provider count growing, price resistance at historical levels, referral drought that is industry-wide), pull these before concluding the diagnosis:

| Signal | What it tells you | How to pull | When to use |
|--------|-------------------|-------------|-------------|
| Industry layoffs | How many workers were laid off in the sector recently | WebSearch: "BLS JOLTS {industry} layoffs {year}" or visit bls.gov JOLTS data | Validates whether workforce displacement is real and quantified |
| Job openings vs. workers | How many jobs are available vs. how many workers exist | WebSearch: "BLS JOLTS {industry} job openings {year}" | Low openings + high layoffs = workers becoming freelancers |
| New business formation | How many new businesses were formed in the sector | WebSearch: "Census business formation {industry} {year}" or visit census.gov BFS data | A surge here is the leading indicator of competitive flood, 6-12 months ahead |

**For Canadian clients:**
WebSearch for StatCan labour force data by industry and business openings/closures by sector. Search: "StatCan employment by industry {sector} {year}", "StatCan business openings closures {sector} {year}".

**For Australian clients:**
WebSearch for ABS labour force data by industry and ASIC new business registrations. Search: "ABS labour force {industry} {year}", "ASIC new company registrations {year}".

**The Category Dissolution pattern in data:** BLS JOLTS layoffs surging + Census business formation applications surging in the same sector = the supply flood is confirmed with hard numbers, not just anecdote. These two data points together make the diagnosis defensible.

### Industry-specific signals (Phase 1E)

| Tag | Industry | Additional signals | How to pull |
|---|---|---|---|
| `home_services` | General home services (plumbing, electrical, cleaning, etc.) | Housing starts/permits, home sale volume, seasonal demand patterns, local regulation changes | WebSearch: "{geo} housing starts {year}", "{geo} building permits {quarter}" |
| `roofing` | Roofing and exterior | Storm/hail data, disaster declarations (FEMA/state), insurance claim volumes, seasonal weather patterns | WebSearch: "{geo} storm damage {year}", "{geo} FEMA disaster declaration", "{geo} hail reports {month}" |
| `hvac` | Heating, ventilation, AC | Temperature anomalies (heat waves, cold snaps), energy prices (natural gas, electricity), building permits, refrigerant regulations | WebSearch: "{geo} temperature records {year}", "{geo} energy prices {quarter}", "HVAC refrigerant regulation {year}" |
| `tree_service` | Tree care and removal | Storm data, municipal tree ordinances, seasonal patterns, emerald ash borer / pest outbreaks | WebSearch: "{geo} storm damage trees {year}", "{geo} tree removal ordinance", "{geo} emerald ash borer" |
| `shutters_blinds` | Window coverings | Housing starts, energy prices, commodity prices (aluminium, PVC), bushfire/hurricane season data, building code changes | WebSearch: "aluminium price LME {month} {year}", "{geo} energy prices", "{geo} bushfire season" |
| `ecommerce` | Online retail / DTC | Tariff schedules and changes, shipping cost indices, Strait of Hormuz / supply chain status, FX rates, consumer spending indices | WebSearch: "US tariff schedule {year}", "container shipping rates {month} {year}", "consumer spending index {geo} {quarter}" |
| `agency` | Marketing/creative/dev agencies | AI adoption surveys (agency-specific), platform revenue changes, agency M&A activity, client churn benchmarks, freelancer marketplace growth | WebSearch: "agency AI adoption {year}", "agency revenue benchmark {year}", "{vertical} agency consolidation" |
| `saas` | Software as a Service | VC funding trends (Crunchbase/PitchBook coverage), tech layoffs, churn benchmarks by category, platform dependency risk (API changes, pricing), enterprise budget surveys | WebSearch: "SaaS funding {quarter} {year}", "tech layoffs {month} {year}", "{category} SaaS churn rate" |
| `professional_services` | Law, accounting, consulting | Regulatory changes, licensing requirements, market consolidation (M&A), billable rate benchmarks, AI displacement anxiety | WebSearch: "{profession} regulation changes {geo} {year}", "{profession} M&A {year}", "{profession} AI impact survey" |
| `healthcare` | Medical practices, dental, specialists | Insurance reimbursement changes, CMS/Medicare policy updates, demographic shifts, telehealth adoption rates, malpractice insurance trends | WebSearch: "{specialty} reimbursement changes {year}", "telehealth adoption rate {year}", "{geo} population growth demographics" |
| `restaurant` | Food service and hospitality | Food cost indices, labor market (minimum wage changes, staffing shortages), delivery platform commission changes, health inspection trends, tourism/foot traffic data | WebSearch: "food cost index {month} {year}", "{geo} minimum wage {year}", "{geo} restaurant closures {year}" |
| `real_estate` | Agents, brokers, property management | Mortgage rates (current + forecast), inventory levels, days on market, commission structure changes (NAR settlement), migration patterns | WebSearch: "mortgage rate forecast {year}", "{geo} housing inventory {month}", "NAR commission settlement impact" |
| `auto` | Dealerships, repair shops, detailing | New/used car price indices (Manheim), EV adoption rates, parts supply chain, manufacturer incentive programs, right-to-repair legislation | WebSearch: "Manheim used car index {month} {year}", "EV adoption rate {geo} {year}", "auto parts supply chain {year}" |
| `fitness` | Gyms, studios, personal training | Seasonal membership patterns, competitor pricing, boutique vs. big-box trends, at-home fitness market, wellness spending indices | WebSearch: "gym membership trends {year}", "fitness industry revenue {year}", "at-home fitness market {year}" |
| `general` | Anything not listed above | No additional signals beyond baseline. The 1C Economic and Platform Context phase handles general macro research. | n/a |

### How to use the registry

1. During input collection, identify the industry tag. If the client's vertical doesn't match a specific tag, use `general`.
2. In Phase 1E, run the WebSearch queries listed for the matched tag, substituting `{geo}` with the client's geography, `{year}` with the current and prior year, `{month}` and `{quarter}` with the relevant period.
3. Not every search will return useful results. That's fine. The registry tells you what to look for, not what you'll find. Capture what's available and note gaps.
4. If a signal turns out to be irrelevant to the specific engagement (e.g., no storms hit the market during the analysis period), note it in Ruled Out rather than forcing it into the diagnosis.

---

## Phase 0: Workspace Setup

**Run this immediately after collecting inputs, before any research begins.** This creates the folder structure so the user can place client data files while research phases run in parallel.

### Steps

1. **Determine the run folder name.** Check if `clients/{clientname}/bear/bear{YYYYMMDD}/` already exists.
   - If it does not exist: use `bear{YYYYMMDD}`
   - If it exists: append a letter suffix. Check `bear{YYYYMMDD}a`, then `b`, etc. Use the first that doesn't exist.

2. **Create the folder structure:**
   ```
   clients/{clientname}/
     bear/
       bear{YYYYMMDD}/
         charts/
         from-client/
   ```

3. **Write a placement guide** to `from-client/PLACE-FILES-HERE.md`:

   ```markdown
   # Data Files for BEAR Diagnosis

   Drop client-provided files into this folder. BEAR will incorporate them during analysis.

   ## What to place here

   **Ad account exports (highest value)**
   - Google Ads: Campaigns > Download as CSV (last 6-12 months, segment by month)
   - Meta Ads Manager: Export campaign data as CSV
   - Bing/Microsoft Ads: Campaign export CSV
   - Any other paid channel exports

   **Performance data**
   - Monthly CPA, ROAS, CPC, conversion rate (spreadsheet or CSV)
   - Close rate by month/quarter (for Type B symptoms)
   - Referral volume by month (for Type C symptoms)
   - Pipeline stage duration data (for Type D symptoms)

   **Creative assets**
   - Screenshots of current ads
   - Screenshots of landing pages
   - Website homepage screenshot
   - Pitch deck or proposals (PDF)

   **Sales context (for Type B/D symptoms)**
   - Call recordings or transcripts
   - Common objections list
   - Recent proposal examples

   **Previous reports**
   - Any third-party audits or reports

   ## File naming

   No strict naming required. Use descriptive names so they're identifiable at a glance:
   - `google-ads-export-jan-jun-2026.csv`
   - `landing-page-screenshot.png`
   - `pitch-deck-current.pdf`
   ```

4. **Confirm with the user.** Print the created folder path and ask:
   > Workspace ready at `clients/{clientname}/bear/bear{YYYYMMDD}/`
   >
   > Drop any client files into `from-client/` now or as they become available.
   >
   > Ready to begin research? (y/n)

   If the user says yes, proceed to Phase 1. If they need time to gather files, wait. Research can also start in parallel while files are being placed.

---

## Phase 1: Signal Collection

Gather data from multiple sources. Not every source will be available for every engagement. Use what you can get.

### 1A. Google Trends Research

**Required for every engagement.**

For each of the client's 5-10 keywords:
- Pull interest-over-time data (12-month and 5-year views)
- Note direction: rising, declining, stable, volatile
- Capture rising related queries (what's gaining search interest)
- Capture declining related queries (what's losing interest)
- Flag breakout queries (new terms appearing with rapid growth)

**How to pull Google Trends data:**

**Use WebSearch to find Google Trends data for each keyword.** Search for `Google Trends "{keyword}" {geo}` and interpret the results. Look for articles, reports, or data summaries that reference Google Trends data for your keywords. For direct exploration, search for `site:trends.google.com "{keyword}"` or look for recent analyses of search interest in the client's vertical.

For each keyword, try these searches:
- `Google Trends "{keyword}" {geo} {year}` to find trend data and analyses
- `"{keyword}" search interest {geo} rising declining` to find commentary on trends
- `"{keyword}" Google Trends data {month} {year}` for recent snapshots

If you have access to Google Trends directly, navigate to `trends.google.com/trends/explore?q={keyword}&geo={geo}&date=today%2012-m` for 12-month views and `today%205-y` for 5-year views.

> **Note:** The [operational version](https://clickmakers.io) pulls structured timeseries data via API, returning actual index values per week that feed directly into charts. The methodology is the same; the data fidelity is higher.

**What to capture per keyword:**

| Keyword | 12m Direction | 5y Direction | Peak Period | Current vs Peak | Notable Related Queries |
|---------|--------------|-------------|-------------|----------------|----------------------|
| kw1     | declining    | stable      | Mar 2025    | 62% of peak    | "kw1 alternative" rising |

**What to look for:**
- Declining interest in the client's core keywords = possible demand shift
- Rising interest in adjacent/substitute terms = desire is migrating
- Breakout queries in the vertical = new entrants or new buyer concerns
- Seasonal patterns that don't match the client's performance decline = rules out seasonality
- Divergence between the client's keywords and category keywords = the market is healthy but the client's niche within it is shrinking
- Geographic shifts in interest = demand migrating to different regions

**Supply-side validation (required for every engagement):**

Google Trends data is ambiguous. A surge in "X agency" could mean more buyers looking to hire, more job seekers looking for work, or more people learning to become providers. BEAR must disambiguate before treating Trends data as demand signal.

After collecting the primary keyword data, run these additional checks:

1. **Explicitly demand-side queries.** Search for "hire {keyword}" or "looking for {keyword}" variants. If these have volume and trend in the same direction as the primary keywords, the Trends data is demand-side. If they are flat or zero while primary keywords surge, the surge is contaminated.

2. **Supply-side queries.** Search for "{vertical} course", "learn {vertical}", "{vertical} certification", "become a {vertical} freelancer", "start a {vertical} agency" (substitute the client's vertical). If supply-side queries are surging at the same rate as the primary keywords, a significant portion of the Trends signal is people entering the market as providers, not as buyers.

3. **Adjacent category migration.** Search for "fractional {role}" (e.g., "fractional CMO", "fractional marketing director"), "{vertical} consultant" (e.g., "google ads consultant"), "{vertical} freelancer". If these substitute terms are growing faster than the "agency" terms, buyers are migrating from the agency category to the expert/freelancer/fractional category.

**Capture in a supply-side validation table:**

| Query | Type | 2024 Avg | Current | Direction | Interpretation |
|-------|------|----------|---------|-----------|---------------|
| "hire {kw}" | Demand-side | ? | ? | ? | Real buyer intent |
| "{vertical} course" | Supply-side | ? | ? | ? | People learning to become providers |
| "fractional {role}" | Category migration | ? | ? | ? | Buyers choosing experts over agencies |

**If supply-side queries are growing faster than or at the same rate as primary keywords, flag the Trends data as unreliable for demand estimation.** Note this prominently in the Demand Signals section of the deliverable. Do not present Trends data as "demand is surging" without this validation.

**Why this exists:** In a real engagement with a mid-size PPC agency, the initial analysis interpreted surging "google ads agency" Trends as demand signal. Supply-side validation revealed "google ads course" (6.7x), "learn google ads" (5.7x), and "marketing freelancer" (2.5x) surging at equal or higher rates, while "hire google ads agency" was at zero. Tens of thousands of agency layoffs had created a supply flood that inflated Trends data.

### 1B. Competitive Landscape Research

**Required for every engagement.**

For each competitor (5-15):
1. Visit their website and note current positioning, messaging, headline, value proposition
2. Search for their ads (Google `{competitor name} ads`, check Meta Ad Library if relevant)
3. Document:
   - **Primary message**: What do they lead with?
   - **Messaging angle**: Discount/price, expertise/authority, speed/convenience, trust/safety, transformation/results, fear/urgency, other
   - **Proof type**: Social proof, authority/credentials, guarantee, case studies, none visible
   - **Offer structure**: What's the offer? Free consultation, discount, trial, etc.
   - **Differentiation**: What (if anything) makes them different from the rest?
   - **Desire mediated**: What desire does this competitor's positioning promise to fulfill? Not the feature, the underlying want. A shutters company selling "50% off" mediates the desire for a deal. One selling "the last blinds you'll ever buy" mediates the desire for permanence. Different desires, same product.
   - **Model presented**: Who or what does the competitor hold up as the aspirational model? Their founder? Their customers? A lifestyle? A standard? This is who the buyer is invited to become by choosing this provider.

**Desire landscape mapping** (do this after documenting all competitors):
- Map which desires each competitor mediates. Group them.
- Identify **contested desires**: 3+ competitors fighting to mediate the same desire (e.g., everyone promises "peace of mind")
- Identify **underserved desires**: desires no competitor addresses (e.g., nobody speaks to the desire for independence from ongoing maintenance)
- Identify **suppressed desires**: desires the market actively avoids naming (e.g., status, fear of judgment, envy of neighbors). These are often the most powerful positioning territory because competitors won't go there
- Note the **direction of imitation**: who is copying whom? Is there a market leader everyone else mimics? Has the client been pulled into imitating competitors, or have competitors converged on the client's original positioning?

**Invisible competitor assessment** (do this after profiling visible competitors):

The 5-15 profiled competitors are the visible tip of the competitive landscape. In many markets, the real competitive pressure comes from providers you can't profile individually because there are thousands of them. Assess:

- **Provider count.** WebSearch for total number of businesses in the client's vertical (IBISWorld, Statista, industry reports). Is the provider count growing or shrinking? A market with 100,000+ providers growing 16%/year is a fundamentally different competitive environment than 500 stable competitors.
- **Freelancer/solo competition.** WebSearch for the client's service type on Upwork, Fiverr, and curated platforms (MarketerHire, Mayple, etc.). What are freelancers charging for equivalent work? This establishes the price floor the client competes against, whether they know it or not.
- **AI tool substitutes.** WebSearch for AI tools that claim to replace the client's service (e.g., "AI {service type}", "AI {vertical} tool"). What do they cost? Even if they don't fully work yet, their pricing sets the buyer's price anchor.
- **Workforce redistribution.** Check for recent layoffs in the client's industry vertical. If large companies are shedding workers (holding company restructuring, tech layoffs), those workers become freelancers and micro-agencies. WebSearch: "{vertical} layoffs {year}", "{vertical} industry job cuts".

Capture in a market structure summary:

| Dimension | Finding |
|-----------|---------|
| Visible competitors profiled | {count} |
| Estimated total providers in market | {count, source} |
| Provider count trend | Growing/shrinking, {rate} |
| Freelancer price floor | ${range}/mo for equivalent work |
| AI tool price anchor | ${range}/mo for automated alternative |
| Recent workforce displacement | {count} laid off, becoming competitors |

**Why this matters:** If the visible competitor landscape looks moderately competitive but thousands of laid-off workers are flooding the market as freelancers, the real competitive pressure is far greater than the profiled competitors suggest. Price compression, referral drought, and "everything just slowed down" symptoms are often caused by this invisible supply flood, not by the named competitors.

**Why this exists:** In a real engagement with a mid-size PPC agency, the initial analysis profiled 15 competitors and assessed convergence as "high but manageable." Subsequent research revealed tens of thousands of industry layoffs, provider count growing 16%/year, and the freelancer marketplace up 90% in four years. The real competitive pressure was invisible to the standard competitor profile.

**Convergence analysis** (layer on top of desire mapping):
- What messaging angle do most competitors use? Count them.
- Are there angles NO competitor is using? List them.
- Are there angles 3+ competitors fight over? List them.
- How does the client's messaging compare to the field?
- Calculate a convergence assessment: low (varied messaging), moderate (some clustering), high (most say similar things), extreme (indistinguishable)
- Assess **mimetic intensity**: Is the market in early differentiation (competitors still distinct), active convergence (competitors copying the leader), or mimetic crisis (everyone indistinguishable, competing only on price)?

### 1C. Economic and Platform Context

**Do as much as available data allows.** Pull macro data from the correct country source via WebSearch.

**For US clients:**
- WebSearch: "FRED consumer sentiment index current", "FRED housing starts current", "FRED unemployment rate current"
- WebSearch for commodity prices relevant to the vertical: "{commodity} price current"

**For Canadian clients:**
- WebSearch: "Bank of Canada overnight rate current"
- WebSearch: "USD CAD exchange rate" (import cost pressure)
- WebSearch: "StatCan housing starts {year}" for housing/construction verticals
- WebSearch for commodity prices: "{commodity} price current"

**For Australian clients:**
- WebSearch: "RBA cash rate current"
- WebSearch: "ABS building approvals latest" for housing/construction verticals
- WebSearch for commodity prices: "{commodity} price current"

**All geographies:**
- WebSearch for industry-specific news in the client's vertical (last 6-12 months)
- WebSearch for container shipping rates if the client's supply chain involves imports
- WebSearch for prediction market probabilities on relevant economic/political events: "Polymarket {event}"
- Check for Google Ads platform changes that affected the vertical (auction changes, AI features, policy updates)
- Check for regulatory or policy changes affecting the vertical
- Check for geopolitical or macro events affecting buyer psychology (tariffs, trade policy, AI disruption anxiety, etc.)

### 1D. Client Position Analysis

**From client-provided data + research.**

- Document the client's current messaging (from their ads, website, landing pages)
- Document their performance trend (CPA, ROAS, CPC, conversion rate, whatever they can provide)
- Note when the decline started and any events they associate with it
- Compare their messaging to the competitive landscape captured in 1B
- Assess differentiation: Is the client saying something different, or the same thing as everyone else?

### 1E. Industry-Specific Signals

**Run if industry tag is not `general`.**

Look up the client's industry tag in the Signal Registry above. Run the listed WebSearch queries for that tag, substituting the client's geography and relevant time periods.

**What to capture:**

| Signal | Finding | Source | Relevance to symptom |
|--------|---------|--------|---------------------|
| e.g., "Aluminium price surge" | LME hit $3,585/t, 4-year high | CNBC, LME data | Direct input cost increase for shutter manufacturing |

**Processing rules:**
- Capture the data point, the source, and a one-line assessment of how it connects (or doesn't) to the client's symptom.
- If a signal turns out irrelevant, move it to Ruled Out in the diagnosis. Don't discard it silently. Showing what you checked and dismissed builds credibility.
- If a signal reveals something unexpected that isn't in the registry (e.g., a local regulation change nobody mentioned), capture it. The registry is a starting list, not a ceiling.
- Industry-specific signals most commonly contribute to External Shock or Demand Shift diagnoses. But they can also surface Contributing Factors that compound a Competitive Convergence or Model Disruption finding.

---

## Phase 2A: Shift Diagnosis

Compare the current market state against the baseline (pre-decline) period and classify what changed. The baseline is reconstructed from historical data (Google Trends history, Wayback Machine, client records, previous reports). A market shift is rarely one thing. Most real shifts are a combination of factors. Identify which are contributing and estimate their relative weight.

### Shift Categories

**1. Competitive Convergence (Mimetic Crisis)**
Everyone is saying the same thing. The market has become undifferentiated noise. Buyers have no reason to choose one provider over another based on messaging alone.

This is what Girard calls mimetic crisis: competitors unconsciously imitate each other until all differences dissolve. It starts with one successful player. Others copy what worked. The copies copy the copies. Eventually every ad, every proposal, every pitch deck leads with the same angle. The market collapses into pure price competition because messaging no longer differentiates.

Diagnostic criteria:
- Convergence score moved from low/moderate to high/extreme
- Number of competitors using the dominant messaging angle increased
- The number of underserved angles decreased (open territory is shrinking)
- The client's messaging became less differentiated over time (either they converged toward competitors, or competitors converged toward them)
- The desire landscape shows most competitors mediating the same 1-2 desires
- Direction of imitation is traceable: you can identify who started the pattern and how it spread
- The market has entered price competition as a symptom (when messaging is identical, price is all that's left)

**2. Demand Shift (Desire Migration)**
Buyers want something different now. The desire hierarchy changed. What used to matter (price, speed) matters less than what now matters (security, independence, control).

In Girardian terms: the desires buyers are imitating shifted. The models they look to changed. A market that used to desire "the cheapest option" now desires "the option that makes me feel in control." The old desire didn't disappear. It was displaced by a more urgent one. Businesses still mediating the old desire wonder why their messaging stopped working.

Diagnostic criteria:
- Google Trends shows declining interest in core keywords
- Rising/breakout queries indicate desire migrating to adjacent terms
- Buyer concerns shifted (visible in forums, reviews, social media)
- The client's value proposition addresses a desire that's weakening
- New models are emerging that buyers imitate (influencers, thought leaders, or early adopters setting new expectations)
- The suppressed desires identified in the landscape analysis are becoming unsuppressed (previously taboo concerns are now openly discussed)

**3. Platform Change**
The advertising platform repriced the channel. Algorithm changes, auction dynamics, ad format deprecation, quality score recalibration, privacy changes.

Diagnostic criteria:
- CPC/CPM increases not explained by competitive entry or demand changes
- Platform announced changes during the decline period
- Performance drop correlates with known platform update dates
- Impression share changed without budget or bid changes

**4. External Shock**
Something outside the market changed the rules. Regulation, economic shift, geopolitical event, pandemic aftermath, AI disruption, tariff policy.

Diagnostic criteria:
- A specific event or policy change coincides with the performance decline
- The event affects buyer psychology or purchasing behavior in the vertical
- Multiple businesses in the vertical experienced similar declines simultaneously
- The client's internal operations didn't change, but results did

**5. Model Disruption (New Mediator)**
A new player entered the market and is redirecting buyer desire. New competitor, new category entrant, new influencer reshaping expectations, new technology redefining what "good" looks like.

In Girardian terms: a new mediator appeared. Buyers don't desire autonomously; they desire through models (people or brands they want to be like). When a new model enters and captures attention, desire redirects toward whatever that model mediates. The existing players didn't get worse. A new model made them feel outdated by redefining what buyers should want.

Diagnostic criteria:
- A new competitor appeared in the landscape that wasn't there before
- The new entrant's messaging or positioning is pulling buyers away
- Auction insights show new impression share competitors
- The new entrant introduced a positioning angle that made existing messaging feel outdated
- The new entrant presents a different aspirational model than incumbents (e.g., tech-forward vs. traditional, transparent vs. opaque, founder-led vs. corporate)
- Buyer language is shifting to mirror the new entrant's framing (they're adopting the disruptor's vocabulary)

**6. Category Dissolution (Supply Glut + Price Anchor Collapse)**
The service category itself is losing viability at its historical price point. This is different from competitive convergence (where everyone says the same thing) and different from demand shift (where buyers want something different). In category dissolution, the *category boundary* breaks down: what was once a distinct, premium service becomes indistinguishable from cheaper alternatives in the buyer's mind.

Three forces typically converge:
- **Supply glut:** Provider count explodes (layoffs create freelancers, low barriers to entry attract new entrants, AI tools lower the skill threshold). The number of people offering the service grows faster than the number of buyers.
- **Price anchor collapse:** A cheaper substitute (AI tool, freelancer, platform automation) resets the buyer's reference price. Even when the substitute doesn't fully work, its existence changes what buyers believe the service should cost. The market "prices in" efficiencies that may not exist yet.
- **Category migration:** Buyers stop searching for the old category label and start using a new one. "Agency" becomes "consultant" or "fractional CMO." The old label carries baggage (expensive, slow, overhead) and the new label carries desire (expert, lean, embedded).

Diagnostic criteria:
- Provider count in the vertical is growing significantly (10%+/year)
- Recent workforce displacement events (layoffs, restructuring) created a flood of new competitors
- AI tools or platform automation set a new price floor far below historical pricing
- The client reports price resistance that didn't exist before ("we used to charge $X, now nobody will pay it")
- Supply-side Google Trends queries (courses, certifications, "how to become") are surging at the same rate as or faster than the primary service queries
- Explicitly demand-side queries ("hire X", "looking for X") are flat or declining while ambiguous queries surge
- Adjacent category terms (consultant, fractional, freelancer) are growing faster than the traditional category term (agency, firm)
- Industry benchmarks show rising churn, declining retention, shrinking budgets per provider, or referral ecosystem degradation that is industry-wide (not client-specific)

**This is the hardest shift to diagnose because it looks like several other shifts simultaneously.** It can masquerade as competitive convergence (there are more competitors), as demand shift (buyers want something different), or as external shock (the economy changed). The distinguishing feature is that the *category itself* is the problem, not the client's position within it. The correct response is not to reposition within the category but to escape it.

**Why this exists:** In a real engagement with a mid-size PPC agency, the initial diagnosis identified competitive convergence and acquisition channel failure. The founder's market intelligence (referral drought is industry-wide, buyers want experts not agencies, pricing resistance at historical levels) triggered deeper research revealing: tens of thousands of agency layoffs created a supply flood, supply-side search terms surging faster than demand-side, and 60% of marketing leaders already cutting agency spend due to AI. The service category was dissolving, not just becoming more competitive.

### Producing the Diagnosis

For each contributing shift category:
1. State the finding with specific evidence (not speculation)
2. Cite the data source (Google Trends, competitive research, client data, news)
3. Estimate relative contribution (primary driver, contributing factor, minor factor)
4. Explain the mechanism: how does this shift cause the symptoms the client sees?

**Important:** Do not diagnose shifts you can't support with evidence. "We couldn't determine..." is a valid finding. Speculation disguised as diagnosis destroys credibility.

### Prior diagnosis check

After producing the diagnosis, check whether a prior BEAR diagnosis exists for this client:

1. Check locally: does `clients/{clientname}/bear/` contain any folder other than the current run?

If a prior diagnosis is found, read it and produce the What Changed section of the deliverable (see Deliverable Structure). If no prior diagnosis exists, omit the What Changed section entirely.

**What to compare:**
- Shift category: same, intensified, shifted to a different category, or partially resolved?
- Competitive landscape: new entrants, departed competitors, convergence level movement
- Demand signals: keyword interest direction, supply/demand balance, breakout queries from last time
- Repositioning recommendation: still valid, needs refinement, or now points in a different direction?

The comparison is structured, not a prose summary. Use the What Changed tables from the deliverable template. The goal is to show the client that the market is moving and BEAR is tracking it.

---

## Phase 2B: Evidence Weighing

**Mandatory. Run after Phase 2A and before Phase 2C.**

The diagnosis from Phase 2A is a hypothesis, not a finding. This phase stress-tests it before repositioning recommendations are built on top of it. The goal is not to disprove the diagnosis. The goal is to make sure it can survive scrutiny.

### Step 1: State the claim

Restate the primary diagnosis from Phase 2A as a single falsifiable claim:

> "The primary cause of {client}'s decline is {shift category} driven by {specific mechanism}."

Do this before running the steps below. Having a crisp claim makes the weighing concrete.

### Step 2: Score the evidence

List every piece of evidence used to reach the diagnosis. For each one, score it:

| Evidence | Source | Sponsor Bias | Sample | Methodology | Score |
|----------|--------|-------------|--------|-------------|-------|
| {data point} | {who produced it} | High / Low / None | {N} | {how it was gathered} | Strong / Moderate / Weak |

**Scoring rules:**
- **Strong:** Large sample, no sponsor interest in the conclusion, clear methodology (e.g., Google Trends, government data, peer-reviewed research)
- **Moderate:** Reasonable sample, some potential bias, methodology disclosed (e.g., industry association surveys)
- **Weak:** Small sample, sponsor has interest in the conclusion, methodology unclear (e.g., vendor-commissioned surveys, press releases)
- **Anecdote:** Accurate observation, not representative. Flag explicitly. Anecdotes can illustrate a pattern but cannot establish one. If anecdotes are the primary evidence driving the diagnosis, that is a red flag, not a finding.

### Step 3: Weigh both sides symmetrically

Apply the same scoring rubric to evidence FOR the diagnosis and evidence AGAINST it. Do not treat confirming evidence as "the data" and disconfirming evidence as "the exception."

| Direction | Evidence | Score | Weight |
|-----------|----------|-------|--------|
| FOR | {supporting finding} | Strong / Moderate / Weak | High / Medium / Low |
| AGAINST | {counter-finding} | Strong / Moderate / Weak | High / Medium / Low |

**Asymmetry check:** If all the strong-scored evidence is FOR and all the weak-scored evidence is AGAINST, ask: did you actually search for strong counter-evidence, or did you only find what you were looking for?

If you cannot find strong counter-evidence, note it: "We searched for disconfirming evidence and did not find it. The diagnosis holds." That is a valid outcome. The step is about requiring the search, not requiring you to find something.

### Step 4: Actor analysis

For each key data point that drives the diagnosis, ask: **who else could generate this signal?**

List all plausible actors and their motivations:

| Data Point | Actor A | Actor B | Actor C |
|------------|---------|---------|---------|
| {observed signal} | {who + why} | {who + why} | {who + why} |

Then ask: **if Actor B is dominant rather than Actor A, what would we expect to see differently?** Go check. This is the test that disambiguates supply from demand, correlation from causation, and real shifts from artifacts of the data source.

**Why this exists:** In a real engagement, "google ads" search volume was surging. The initial read was demand growth. Actor analysis revealed the surge could equally be generated by buyers, by people learning to become providers, or by laid-off agency workers seeking re-employment. Checking demand-side queries ("hire google ads agency") showed they had trended to zero. The surge was supply, not demand. The diagnosis changed entirely.

### Step 5: Verdict

After running all four steps, state the verdict:

- **Confirmed:** The diagnosis holds. Strong evidence on the FOR side, weak or absent counter-evidence, actor analysis supports the primary actor interpretation.
- **Revised:** The evidence supports a modified version of the diagnosis. State what changed and why.
- **Inconclusive:** The evidence is genuinely mixed. State what is known, what is uncertain, and what additional data would resolve it.
- **Rejected:** The disconfirmation search found stronger evidence against the diagnosis than for it. Return to Phase 2A with the new information.

Carry the verdict and confidence level into Phase 2C. If the verdict is Inconclusive or Rejected, do not proceed to repositioning recommendations until the diagnosis is resolved or explicitly flagged as provisional.

---

## Phase 2C: BEAR Position Grid

**Mandatory. Run after Phase 2B, before Phase 3.**

The diagnosis tells you what shifted. The Position Grid tells you what that means strategically. Two measured axes, four quadrants.

### Two axes

**X-axis: Performance Gap** (client-specific)

How much the client's performance change deviates from the market's demand change. This separates "the market hurt everyone" from "the market hurt you specifically."

Formula: `client performance change % - market demand change %`

- **Client performance change:** from the client's own data (lead volume, close rate, revenue, whatever metric best matches their symptom type). Use the same time period as the market measurement.
- **Market demand change:** from the validated demand-side Google Trends queries collected in Phase 1A (after supply-side filtering). Confirm with government trailing data where available via web research (search for recent GDP-by-industry data, employment trends by sector, sector revenue reports).

**Government trailing data for market demand confirmation:**

Pull trailing confirmation from government sources to validate the Trends-based demand measurement. These lag by 2 to 6 months but measure actual economic activity, not search interest.

**For US clients:**
- WebSearch: "BEA GDP by industry {sector} latest quarter" for quarterly GDP growth/contraction.
- WebSearch: "BLS QCEW {industry} {area} latest" for quarterly employment and wages.
- WebSearch: "Census sector revenue {industry} latest" for monthly or quarterly sector revenue.

**For Canadian clients:**
- WebSearch: "StatCan GDP by industry monthly latest" for GDP by industry.
- WebSearch: "StatCan Labour Force Survey {industry} latest" for employment by industry.
- WebSearch: "StatCan retail trade latest" for retail trade data.

**For Australian clients:**
- WebSearch: "ABS National Accounts GDP quarterly latest" for GDP.
- WebSearch: "ABS Labour Force {industry} latest" for employment by industry.
- WebSearch: "ABS retail business turnover monthly latest" for retail turnover.
- WebSearch: "ABS building approvals latest" for construction verticals.

**When Trends and government data disagree**, re-validate. If Trends says "surging" but GDP and sector revenue show contraction, the Trends signal is likely supply-side contamination. If Trends says "declining" but government data shows the sector still growing, the decline may be a keyword shift rather than a category contraction. Note the discrepancy in the deliverable.

Examples:
- Market demand down 10%, client leads down 40%. Gap = -30%. Deep left.
- Market demand down 10%, client leads down 12%. Gap = -2%. Near center.
- Market demand down 10%, client leads down 5%. Gap = +5%. Slightly right. Client is outperforming a declining market.

Midpoint: **0%.** Left of zero = underperforming the market. Right of zero = tracking with or beating the market.

**Y-axis: Positioning Overlap** (client-specific)

% of profiled competitors sharing the client's primary messaging angle. Calculated from Phase 1B competitive landscape research.

Formula: `competitors sharing client's angle / total competitors profiled`

Examples:
- 3 of 12 competitors share the client's angle = 25%. Low overlap.
- 9 of 12 competitors share the client's angle = 75%. High overlap.

Midpoint: **50%.** Below = differentiated. Above = converged.

### The four quadrants

| | Performance gap negative (underperforming market) | Performance gap near zero or positive (tracking/beating market) |
|---|---|---|
| **Low overlap** (differentiated) | **Hibernating** | **Grizzly** |
| **High overlap** (converged) | **Bear Trap** | **Roaming** |

**Grizzly** (tracking market + differentiated): You stand out and your results reflect it. The market may be tough but you're keeping pace or beating it. Protect what's working, lean into differentiation.

**Roaming** (tracking market + converged): Your numbers aren't worse than the market, but you sound like everyone else. Growth or market conditions are masking a positioning problem. When conditions tighten, you have nothing to fall back on. Differentiate now.

**Hibernating** (underperforming + differentiated): You're positioned differently but bleeding faster than the market. Something is off. The differentiation isn't landing, or it's aimed at the wrong desire. Repoint the differentiation, don't abandon it.

**Bear Trap** (underperforming + converged): Losing faster than the market and nothing distinguishes you. Hardest position. Incremental fixes won't work. Fundamental repositioning or category exit.

### How to produce it

Do not guess. Build it from the data already collected:

1. **Calculate the Performance Gap.** State both numbers and the formula: "Market demand changed {X}% (source: demand-side Trends, confirmed by {government source}). Client {metric} changed {Y}%. Performance gap: {Y - X}%."

2. **Calculate the Positioning Overlap.** State the count: "{N} of {total} profiled competitors share the client's primary messaging angle ({angle name}). Overlap: {N/total as %}."

3. **Plot and name the quadrant:** Grizzly, Roaming, Hibernating, or Bear Trap.

4. **State the strategic implication in one sentence.** This governs the entire Phase 3 recommendation. Example: "This is a Bear Trap. The client is underperforming a declining market by 30 points and their messaging is indistinguishable from 75% of competitors. The recommendation must address fundamental repositioning, not incremental improvement."

### How this changes the recommendation

| Quadrant | What Phase 3 should recommend |
|---|---|
| **Grizzly** | Protect and extend. The differentiation is working. Adapt to the specific shift identified in Phase 2A without abandoning the positioning that's keeping results above market. |
| **Roaming** | Differentiate before the window closes. Results track the market only because conditions allow it. Find and claim positioning territory from the desire landscape before conditions tighten and this becomes a Bear Trap. |
| **Hibernating** | Repoint, don't abandon. The differentiation exists but isn't converting. Diagnose why: wrong desire, wrong audience, wrong channel, or right message but poor execution. The fix is aim, not identity. |
| **Bear Trap** | Fundamental change. Not better ads. Not new landing pages. New positioning, new category framing, or category exit. Every dollar spent optimizing within the current position is wasted. |

---

## Phase 3: Repositioning Recommendation

Based on the shift diagnosis and the BEAR Position Grid, recommend how the client should reposition. The quadrant from Phase 2C determines the type of recommendation. The shift type determines its specific content.

### Response Framework by Shift Type

**For Competitive Convergence (Anti-Mimetic Repositioning):**
- Identify the open positioning territory from the desire landscape map (desires no competitor mediates)
- Look especially at suppressed desires, the ones competitors avoid naming. These are often the strongest repositioning territory precisely because competitors won't follow you there.
- Recommend messaging that breaks from the dominant pattern by mediating a different desire entirely, not just saying the same thing differently
- Test the recommendation against the "imitation trap": if competitors copy this positioning, does it still work? If your repositioning depends on being unique, it has a shelf life. If it's rooted in something only the client can authentically claim (history, founder story, local presence, specific expertise), it's defensible.
- The goal: escape the mimetic crisis by stepping outside the desire that everyone is fighting over
- Specific: "Every competitor in your space mediates [contested desire]. The open territory is [underserved desire]. Lead with [specific angle] because [evidence from desire landscape]. Competitors won't follow because [reason]."

**For Demand Shift:**
- Map where desire is migrating (from the rising/breakout query data)
- Recommend repositioning the value proposition toward the emerging desire
- The goal: align messaging with what buyers care about now, not what they cared about before
- Specific: "Buyers in your market are shifting from [old concern] to [new concern]. Your messaging should address [new concern] directly."

**For Platform Change:**
- Diagnose whether the platform change is temporary or permanent
- If permanent: recommend channel diversification or format adaptation
- If temporary: recommend riding it out with budget adjustments
- The goal: adapt to the new platform reality instead of fighting it
- Specific: "Google's [specific change] permanently repriced [specific auction]. Your options are [A, B, C]."

**For External Shock:**
- Assess whether the shock is temporary or structural
- If structural: recommend repositioning for the new reality
- If temporary: recommend defensive positioning until conditions normalize
- The goal: acknowledge the changed environment and adapt, not pretend it hasn't changed
- Specific: "[Event] changed [buyer behavior]. Your messaging should acknowledge [reality] instead of ignoring it."

**For Model Disruption:**
- Analyze what the disruptor is doing differently
- Recommend differentiation that the disruptor can't easily copy (often rooted in the client's unique strengths, history, or local presence)
- The goal: find positioning that's defensible even as the market imitates the new model
- Specific: "The new entrant is winning with [positioning]. Competing head-on loses. Your defensible angle is [X] because [reason they can't copy it]."

**For Category Dissolution (Escape the Category):**
- The standard repositioning advice (differentiate within the category) won't work. If the category itself is dissolving, differentiating within it is like rearranging deck chairs. The recommendation must help the client *exit the dying category* and establish presence in an adjacent one.
- **Identify what the client sells that has no pre-set price.** In a dissolving category, every service with a known label has a compressed price anchor. The escape is to sell something the buyer hasn't priced yet: a diagnostic, a proprietary methodology, an outcome the category term doesn't describe.
- **Match the buyer's migration.** If buyers are moving from "agency" to "consultant" or "fractional," the client must move there too, not fight the migration. Use the language buyers are searching for, not the language the client is used to. Check the supply-side validation table for the fastest-growing adjacent category terms.
- **Reframe the team as an expert.** In category dissolution, buyers want "one expert" not "an agency." If the client has a founder or principal with credible expertise, the positioning should center on that person. The team operates behind the scenes, assembled on demand. This matches the "covert agency" or "embedded expert" model buyers now prefer.
- **Productize diagnostics as the entry point.** Every competitor in the dissolving category offers "free audits" as lead gen. None offer paid, genuine diagnostics. A paid diagnostic ($2K-$10K) accomplishes three things: it escapes the price anchor (consulting, not agency), it qualifies buyers by willingness to pay, and it creates educated buyers who understand the problem before engaging.
- **Do not compete on the dissolving category's terms.** Don't try to be the "best X agency." Don't list on directories that rank "best X agency." Don't write content about "how to choose an X agency." Every piece of content should use the new category language.
- Specific: "The category '{old term}' is dissolving. Buyers are migrating to '{new term}.' Your service should be repackaged as [specific new framing] because [evidence from Trends/supply-side data]. The entry point is [diagnostic product] priced at [range], which escapes the ${old price} anchor entirely."

### Repositioning Principles

1. **Diagnose before prescribing.** The recommendation must flow from the diagnosis. Never recommend messaging changes without explaining which shift they address.
2. **One primary move.** Multiple small changes dilute impact. Identify the single highest-leverage repositioning move and make it the headline recommendation. Supporting moves are secondary.
3. **Concrete, not abstract.** "Differentiate your messaging" is not a recommendation. "Lead your Google Ads with [specific angle] instead of [current angle], because [specific evidence from the competitive analysis]" is a recommendation.
4. **Testable.** Every recommendation should be something the client can implement and measure within 30-90 days.
5. **Honest about uncertainty.** If the diagnosis is ambiguous, say so. If the recommendation is a hypothesis that needs testing, say so. Overconfident recommendations on weak evidence are worse than honest uncertainty.

---

## Phase 4: Scenario Modeling

After completing the repositioning recommendation, build three forward-looking scenarios. These are conditional projections, not predictions.

### How to build scenarios

1. **Identify 3-5 observable indicators** from the diagnosis. These are the variables that will determine which scenario plays out. Choose indicators that:
   - Were significant in the diagnosis (they explained the shift)
   - Are regularly updated (weekly or monthly, not annually)
   - Are publicly accessible (the client can watch them too)
   - Examples: consumer confidence indices, Google Trends for primary keywords, commodity prices, interest rate forecasts, prediction market probabilities

2. **Pull current values** for each indicator using WebSearch:
   - For US macro indicators (consumer confidence, unemployment, inflation, etc.): WebSearch for "FRED {indicator name} {month} {year}" or visit fred.stlouisfed.org directly
   - For commodity prices: WebSearch for "{commodity} price today" or "{commodity} LME price {month} {year}"
   - For prediction market probabilities: WebSearch for "Polymarket {event}" or visit polymarket.com to find current odds
   - For industry employment data (layoffs, job openings, hires): WebSearch for "BLS JOLTS {industry} {metric} {year}" or visit bls.gov
   - For new business formation data: WebSearch for "Census business formation statistics {industry} {year}" or visit census.gov
   - For Google Trends values: use the same WebSearch approach from Phase 1A
   - For any other indicators: WebSearch for the specific data point and source

   > **Note:** The [operational version](https://clickmakers.io) pulls all of these via API in a single pass: FRED indicators, BLS labor data, commodity prices, Polymarket probabilities, and Census business formation stats. Same indicators, structured JSON instead of manual lookups.

3. **Define three scenarios** based on how those indicators could move:
   - **Scenario A (Quick Recovery):** The favorable case. Key indicators improve. Define the specific thresholds (e.g., "confidence above 70").
   - **Scenario B (Slow Grind):** The base case. Indicators hold steady or improve slowly. The current situation persists.
   - **Scenario C (Extended Crisis):** The adverse case. Indicators worsen. New shocks compound existing ones.

4. **Project business metrics** for each scenario. Use the client's current data as the starting point and project based on the relationship between the indicators and the client's performance observed in the diagnosis. This is directional estimation, not financial modeling. Be explicit about the logic:
   - "Victoria search interest dropped 35% and your leads dropped 60%. If search recovers to 80% of baseline, leads should recover to roughly 35-40/month, assuming the conversion gap partially closes."
   - Never present projections as precise numbers. Use ranges.

5. **Assess probability** for each scenario. Use Polymarket data if available (WebSearch for relevant prediction markets). Otherwise, use the current indicator trajectory:
   - All indicators moving in the recovery direction = Quick Recovery is medium-high probability
   - Mixed signals = Slow Grind is most likely
   - Indicators still deteriorating = Extended Crisis is the concern

### Scenario rules

- **Every scenario must be tied to observable indicators.** "Things get better" is not a scenario. "Consumer confidence recovers above 70 and aluminium drops below $3,000/t" is a scenario.
- **Never predict timelines.** Say "IF this happens" not "WHEN this happens."
- **Be honest about uncertainty.** If you can't reasonably project a metric, say so. "Close rate projection uncertain, insufficient data to correlate with macro indicators" is better than a made-up number.
- **Projections are ranges, not points.** "20-30 leads/month" not "25 leads/month."

---

## Phase 5: SimPanel Validation (Optional, Human-Gated)

After completing the repositioning recommendation, optionally validate the proposed messaging against synthetic buyer panels via SimPanel (simpanel.ai).

**Requires SimPanel MCP server. See [simpanel.ai](https://simpanel.ai) for access.**

**This phase is human-gated.** Do not run it automatically. Ask the strategist whether they want to validate the repositioning recommendation before presenting it to the client.

### When to use SimPanel validation

- The repositioning recommendation proposes a significant messaging change
- The client is risk-averse and needs evidence that the new positioning will land
- The diagnosis identified a desire migration and the new target desire hasn't been tested
- There are multiple viable repositioning options and you need to pick one

### How it works

1. **Produce a BEAR signal summary.** After the diagnosis, generate a structured summary of the key findings that affect buyer psychology:

```markdown
## BEAR Signal Summary for SimPanel

**Market:** {vertical} in {geography}
**Date:** {date}
**Diagnosis:** {primary shift category}

### Key findings that affect buyer psychology:
- {finding 1, e.g., "Consumer confidence at 50-year low, survival concerns dominating"}
- {finding 2, e.g., "Aluminium prices up 55%, driving sticker shock on quotes"}
- {finding 3, e.g., "9 of 12 competitors mediating the same desire (security), causing comparison paralysis"}

### Proposed repositioning:
- {the primary move from the recommendation}

### Purchase-relevance assessment:
- {finding 1}: HIGH proximity, HIGH magnitude. Directly changes how buyers evaluate this purchase.
- {finding 2}: HIGH proximity, MEDIUM magnitude. Affects price perception but not purchase intent.
- {finding 3}: MEDIUM proximity, HIGH magnitude. Affects urgency but not desire.
```

2. **Hand off to SimPanel.** The strategist takes this summary and uses SimPanel (simpanel.ai) to build or update buyer personas with the BEAR findings injected as market conditions. SimPanel's purchase-relevance scoring filter prevents dramatic world events from hijacking unrelated personas.

3. **Run SimPanel validation.** Use SimPanel to test the proposed repositioning messaging against the context-aware panel. Compare variants if multiple repositioning options exist.

4. **Add results to the deliverable.** If SimPanel validation was run, add a "Buyer Validation" section after the Repositioning Recommendation:

```markdown
## Buyer Validation (SimPanel)

{Summary of SimPanel results. Which persona types responded positively to the repositioning? Which had objections? What was the overall conversion likelihood?}

**Key insight:** {The most actionable finding from the SimPanel test.}
```

### What SimPanel validation does NOT do

- It doesn't replace the diagnosis. SimPanel tests messaging, not market analysis.
- It doesn't validate the diagnosis itself. The diagnosis is evidence-based. SimPanel validates the response to the diagnosis.
- It doesn't run automatically. The strategist decides whether it adds value for this specific engagement.

---

## Chart Generation

After completing the diagnosis, generate the BEAR Position Grid chart to embed in the deliverable. The chart is produced by `tools/position-grid.py` which reads JSON input and outputs a PNG.

### When to generate

Generate the chart at the END of the diagnosis, after all research is complete and findings are written. The chart data comes from your findings, not the other way around.

### Position Grid chart

| Chart | Command | When to use | Embed in section |
|---|---|---|---|
| Position Grid | `python3 tools/position-grid.py data.json output.png` | Every diagnosis (plots client on the Grizzly/Roaming/Hibernating/Bear Trap 2x2) | BEAR Position Grid |

### How to generate

1. Create a JSON file with the chart data:
   ```json
   {
     "title": "BEAR Position Grid",
     "subtitle": "Acme Roofing, April 2026",
     "client_name": "Acme Roofing",
     "performance_gap": -30,
     "positioning_overlap": 75,
     "quadrant": "Bear Trap"
   }
   ```
2. Run: `python3 tools/position-grid.py data.json output.png`. Output is a PNG at 150 DPI.
3. Save the JSON and PNG to `{engagement-folder}/charts/`.
4. Reference the PNG in the deliverable markdown: `![BEAR Position Grid](charts/position-grid-{date}.png)`

### Chart data rules

- Use real numbers from the research, not estimates or averages of averages.
- The chart must have a title and subtitle that makes it self-explanatory without reading the surrounding text.

### File structure

```
clients/{clientname}/bear/bear{YYYYMMDD}/
  charts/
    position-grid-{date}.json          # Input data
    position-grid-{date}.png           # Generated chart
```

---

## Deliverable Structure

The BEAR deliverable is a single document with these sections. Save to:
`clients/{clientname}/bear/bear{YYYYMMDD}/BEAR-diagnosis-{clientname}.md`

```markdown
# BEAR Diagnosis: {Client Name}
## {One-sentence summary of what shifted}

| | |
|---|---|
| **Prepared** | {date} |
| **Market** | {vertical} in {geography} |
| **Period analyzed** | {baseline period} vs. {current period} |
| **Keywords analyzed** | {list} |
| **Symptom type** | {Type A-E from taxonomy} |
| **Industry tag** | {tag from Signal Registry} |

---

## Executive Summary
{3-5 sentences. What changed, why it matters, what to do about it. A busy executive should be able to read only this section and understand the situation.}

---

## The Symptom
{What the client is experiencing. Performance data showing the decline. When it started. How severe it is. This is the "presenting problem," the reason they came to us.}

---

## The Diagnosis

### Primary Shift: {Category Name}
{Detailed findings with evidence. What changed, when, how we know.}

### Contributing Factor: {Category Name} (if applicable)
{Secondary shift contributing to the problem.}

### Ruled Out
{Shifts we investigated and found no evidence for. This builds credibility. It shows we looked at everything, not just confirmed our first guess.}

---

## The Evidence

### Demand Signals
{Google Trends data, keyword interest changes, rising/declining queries.}

### Competitive Landscape
{Competitor positioning table. Convergence analysis. What changed in the competitive field.}

### Economic and Platform Context
{Relevant macro factors, platform changes, regulatory shifts.}

### Client Position
{Where the client sits relative to the field. Performance data over time.}

---

## BEAR Position Grid

**Performance Gap:** {X}%
Client {metric} changed {Y}% over {period}. Market demand changed {Z}% (source: {source}). Gap: {Y - Z}%.

**Positioning Overlap:** {N}%
{N} of {total} profiled competitors share the client's primary messaging angle ({angle name}).

![BEAR Position Grid](charts/position-grid-{date}.png)

**Position:** {Grizzly / Roaming / Hibernating / Bear Trap}

**What this means:** {One sentence. Example: "This is a Bear Trap. The client is underperforming a declining market by 30 points and their messaging is indistinguishable from 75% of competitors. The recommendation that follows addresses fundamental repositioning, not incremental improvement."}

---

## The Repositioning Recommendation

### The Primary Move
{Single highest-leverage recommendation. What to change, why, and what it looks like implemented.}

### Supporting Moves
{1-3 secondary recommendations that reinforce the primary move.}

### What NOT to Do
{Common reactions to this type of shift that would make things worse. "Don't double down on [X] because [reason]."}

### Implementation Roadmap
{30/60/90 day view. What to do first, what to measure, when to reassess.}

---

## What Changed Since Last Diagnosis

{Include this section only if a prior BEAR diagnosis exists for this client. Omit entirely for first-time engagements.}

**Prior diagnosis:** {date of prior diagnosis}
**This diagnosis:** {today's date}

### Shift Category

| | Prior | Current |
|---|---|---|
| Primary shift | {e.g., Competitive Convergence} | {e.g., Category Dissolution} |
| Contributing factors | {list} | {list} |
| Ruled out | {list} | {list} |

{One paragraph: what the category change means. If the shift category is the same, say so and explain whether it intensified, stabilized, or partially resolved.}

### Competitive Landscape

{What changed in the competitive field since the prior diagnosis. New entrants, departed competitors, messaging shifts. If convergence score changed, note the direction.}

| | Prior | Current |
|---|---|---|
| Competitors profiled | {N} | {N} |
| Convergence level | {Low/Moderate/High/Extreme} | {Low/Moderate/High/Extreme} |
| New entrants | n/a | {names or "none detected"} |
| Messaging angle dominant | {angle} | {angle} |

### Demand Signals

{Did keyword interest move? Did supply-side vs. demand-side balance shift? Are breakout queries from last time still rising or have they plateaued?}

### Repositioning Recommendation

| | Prior | Current |
|---|---|---|
| Primary move | {summary of prior recommendation} | {summary of current recommendation} |
| Direction | {same / refined / reversed} | |

{One paragraph: is the prior recommendation still valid? If the shift category changed, the recommendation likely changes too. If it stayed the same, has the urgency increased or decreased?}

---

## Scenario Outlook

{Three scenarios tied to observable indicators. NOT predictions. Conditional planning.}

### Indicators to Watch

| Indicator | Current Value | Source | Update Frequency |
|-----------|--------------|--------|-----------------|
| {e.g., Consumer Confidence Index} | {current} | {source} | {weekly/monthly} |
| {e.g., Google Trends for primary keyword} | {current} | Google Trends | Weekly |
| {e.g., Aluminium LME price} | {current} | LME | Monthly |
| {e.g., Polymarket: "Rate cut by Q3"} | {probability} | Polymarket | Daily |

### Scenario A: Quick Recovery

**Conditions:** {e.g., Confidence index recovers above 70. Commodity prices stabilize. No further rate hikes.}

| Metric | Current | Projected (60 days) | Projected (90 days) |
|--------|---------|-------------------|-------------------|
| Lead volume | {current} | {projected} | {projected} |
| Qualified rate | {current} | {projected} | {projected} |
| Close rate | {current} | {projected} | {projected} |

**Probability assessment:** {Low/Medium/High based on current indicator trajectory and Polymarket data if available.}

### Scenario B: Slow Grind

**Conditions:** {e.g., Confidence stays 55-70. Rates hold. Supply chain slowly normalizes.}

| Metric | Current | Projected (60 days) | Projected (90 days) |
|--------|---------|-------------------|-------------------|
| Lead volume | {current} | {projected} | {projected} |
| Qualified rate | {current} | {projected} | {projected} |
| Close rate | {current} | {projected} | {projected} |

**Probability assessment:** {Low/Medium/High.}

### Scenario C: Extended Crisis

**Conditions:** {e.g., Confidence drops below 55. Further rate hikes. Supply disruption continues or worsens.}

| Metric | Current | Projected (60 days) | Projected (90 days) |
|--------|---------|-------------------|-------------------|
| Lead volume | {current} | {projected} | {projected} |
| Qualified rate | {current} | {projected} | {projected} |
| Close rate | {current} | {projected} | {projected} |

**Probability assessment:** {Low/Medium/High.}

### How to Read This Section

These are not predictions. Nobody can predict when a war ends or when rates peak. Each scenario is conditional: "IF these indicators move this way, THEN expect these business outcomes." Watch the indicators. When they move, you'll know which scenario you're tracking toward.

```

---

## Quality Standards

### Writing standards
- **Never use em-dashes, en-dashes, or double dashes (--) in any output.** Rephrase the sentence instead. Use colons, semicolons, commas, periods, or parentheses. If a sentence needs a dash to work, rewrite the sentence. This applies to the diagnosis, research files, and all generated content.

### Locale rule
- **All output must use the client's regional English.** The target geography from the inputs determines the locale for the entire engagement: spelling, terminology, currency, and units. This applies to the diagnosis, research files, chart labels, and all generated content. Apply consistently throughout; do not mix locales.
  - **US clients:** American English. aluminum, color, labor, analyze, defense. Currency in USD ($).
  - **Canadian clients:** Canadian English (British-leaning). aluminium, colour, labour, analyse, defence. Currency in CAD ($) with "CAD" qualifier where USD amounts also appear.
  - **Australian clients:** Australian English (British-leaning). aluminium, colour, labour, analyse, defence. Currency in AUD ($) with "AUD" qualifier where USD amounts also appear.
  - **When quoting data sources** that use a different locale (e.g., a US government report in an AU engagement), keep the original source's spelling in the citation but use the client's locale in your analysis text.

### Evidence requirements
- Every diagnostic claim must cite a specific data source
- "The market shifted" requires evidence of what it shifted FROM and TO
- Competitor analysis must include actual quotes/screenshots/URLs, not summaries from memory
- Google Trends data must include specific numbers or directional data, not vague "interest is declining"

### What BEAR does NOT do
- Score accounts (that's an ad grader)
- Write new ad copy (that's a creative engagement)
- Audit operations (that's an operational diagnostic)
- Monitor competitors over time (BEAR is a point-in-time diagnosis, not ongoing surveillance)

### Confidence protocol
- **HIGH CONFIDENCE**: 3+ independent data sources confirm the finding. State it directly.
- **MODERATE CONFIDENCE**: 1-2 data sources support it, no contradicting evidence. State it with the evidence cited.
- **LOW CONFIDENCE**: Suggestive but not confirmed. Flag it explicitly: "Possible contributing factor, but we lack sufficient data to confirm."
- **INSUFFICIENT DATA**: We looked and couldn't find enough to diagnose. Say so. Don't speculate.

### File storage

All client work lives under `clients/{clientname}/` in the working directory. BEAR files go in `clients/{clientname}/bear/`.

**Run folder naming:** Each full run gets its own folder named `bear{YYYYMMDD}`. If a second run happens the same day, append a letter: `bear{YYYYMMDD}a`, then `b`, etc. Check if the folder exists before creating it.

```
clients/{clientname}/
  bear/
    bear20260407/                               # First engagement
      BEAR-diagnosis-{clientname}.md            # The deliverable
      competitive-landscape.md                  # Competitor research
      google-trends.md                          # Search interest data
      economic-context.md                       # Macro/platform/regulatory findings
      industry-signals.md                       # Industry-specific signals (from registry)
      client-position.md                        # Client messaging and performance data
      charts/                                   # Generated chart PNGs and their JSON inputs
      from-client/                              # Client-provided data (ad exports, screenshots, CSVs)
    bear20260715/                               # Quarterly refresh
      BEAR-diagnosis-{clientname}.md
      competitive-landscape.md
      google-trends.md
      economic-context.md
      charts/
```

All research files are flat in the run folder. No nesting. Charts stay as a folder because there are multiple PNGs plus JSON inputs. `from-client/` holds anything the client provided (ad exports, screenshots, CSVs, PDFs).

---

## Integration Points

### Standalone (always works)
- BEAR works as a standalone diagnostic tool
- All data can be gathered via WebSearch and client-provided exports
- No external tool dependencies required

### With other diagnostic methods
- BEAR diagnoses the market environment. Operational audits diagnose internal processes. Evidence verification methods validate claims. These are complementary, not dependent.

---

## Version History

- **1.0.0** (2026-04-06): Initial build. Self-contained market shift diagnosis skill. Four phases: signal collection, snapshot capture, shift diagnosis, repositioning. Five shift categories. Structured deliverable template.
- **2.0.0** (2026-04-07): Forked into open source (methodology) and closed source (operational tooling). Open source uses WebSearch for all data collection.
- **3.0.0** (2026-04-07): Added Phase 5 (Scenario Modeling) with three-scenario conditional projections, Phase 6 (SimPanel Validation) with human-gated workflow. Added Signal Registry with 14 industry tags. Added Pulse mode for weekly monitoring.
- **3.12.0** (2026-04-08): Full methodology sync. All shift categories, evidence weighing, repositioning frameworks, scenario modeling, and SimPanel validation current.
- **4.0.0** (2026-04-13): Full methodology sync with internal v4.0.0. Added: Category Dissolution shift category with full diagnostic criteria, supply-side validation protocol, invisible competitor assessment, desire landscape mapping with Girardian framework, actor analysis in evidence weighing, measured-axis BEAR Position Grid (Performance Gap formula, Positioning Overlap calculation, four quadrants with strategic implications), government trailing data confirmation for market demand, locale awareness (US/CA/AU), Position Grid chart via `tools/position-grid.py`. Removed: Pulse mode (operational feature requiring API access), all chart types except Position Grid. Streamlined to single mode: diagnose.
