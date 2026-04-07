---
name: bear
version: 2.0.0
description: "BEAR (Buyer Environment Analysis & Repositioning). Diagnoses why business development stopped working by analyzing market shifts, competitive convergence, and buyer environment changes. Covers all symptom types: ad performance decline, close rate collapse, referral source drought, and pipeline stall. Produces a temporal market diagnosis with repositioning recommendations. Use when results changed but the business didn't, or when entering a new market and needing competitive landscape intelligence."
interface: "invoke: /bear {mode} {client-name}"
modes: [diagnose, snapshot, compare]
author: Alex Makarski / Click Makers
---

# BEAR: Buyer Environment Analysis & Repositioning

## What This Skill Does

BEAR answers: "Your business development stopped working. Here's why, and the cause isn't inside your business."

It reads market signals, captures structured snapshots of a client's competitive environment, compares those snapshots over time, and diagnoses what shifted. The output is a shift diagnosis with repositioning recommendations.

BEAR is not an ad grader (that's AdGradr). It's not an operational audit (that's SONAR). It diagnoses the market environment outside the client's business -- the forces that changed what buyers want, who they compare you to, and why they say yes or no.

---

## Symptom Taxonomy

BEAR diagnoses multiple presenting symptoms. The symptom type determines which signals to prioritize.

### Type A: Acquisition Decline
"Leads dried up. Traffic dropped. CPAs doubled."

The top of funnel broke. Fewer people are entering the pipeline. This is the classic ad performance problem -- the one most graders and agencies focus on.

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

Deals are entering the pipeline but stalling at evaluation or decision stage. Buyers aren't saying no -- they're not saying anything. This is often a combination of competitive convergence (all options look the same so there's no urgency to choose) and external shock (economic uncertainty, regulatory changes, or macro anxiety causing decision paralysis).

**Signal priority:** Competitive convergence at the proposal level, economic indicators affecting buyer confidence, external events causing decision paralysis across the vertical, whether stall is industry-wide or client-specific.

### Type E: Mixed / Unclear
"Everything just... slowed down."

Multiple symptoms present simultaneously, or the client can't isolate which part of the funnel broke. Run signal collection across all priority areas and let the evidence determine the diagnosis.

**Signal priority:** Broad scan across all signal types. The diagnosis will surface which symptom type(s) are actually in play.

---

## Modes

### `/bear diagnose {client-name}`
Full engagement. Captures current market state, reconstructs baseline from historical data, diffs the two, classifies the shift, and produces repositioning recommendations. This is the standard BEAR deliverable.

### `/bear snapshot {client-name}`
Captures a single market state snapshot without comparison. Use this to establish a baseline for future comparison, or when a client wants a competitive landscape analysis without temporal diagnosis.

### `/bear compare {client-name}`
Compares two existing snapshots. Use when snapshots were captured at different times and you need to produce the shift diagnosis.

---

## Inputs Required

Collect from the user before starting:

### Must have
1. **Client name and website URL**
2. **Market/vertical** (e.g., "plantation shutters in Melbourne", "B2B SaaS for HR teams")
3. **5-10 target keywords** the client competes on (paid or organic -- these drive the Trends and competitive research)
4. **Target geography** (city, state/province, country)
5. **Symptom description** -- classify into Type A-E from the Symptom Taxonomy above. Ask:
   - What specifically changed? (leads down? close rate down? referrals stopped? pipeline frozen?)
   - When did it start?
   - How bad is it? (numbers if possible: "close rate went from 40% to 15%", "referrals dropped from 8/month to 1")
   - Did anything change inside the business during that period? (new sales rep, pricing change, service change)

### Should have
6. **Competitor list** (5-15 competitors, or permission to identify them via research)
7. **Performance data** -- varies by symptom type:
   - Type A (acquisition decline): CPA, ROAS, CPC, impression share over last 3-12 months
   - Type B (close rate collapse): close rate by month/quarter, average deal cycle length, proposal win rate
   - Type C (referral drought): referral volume by month/quarter, referral source breakdown, when each source went quiet
   - Type D (pipeline stall): pipeline stage duration, deals stuck by stage, proposal-to-close timeline
   - Type E (mixed): whatever they have
8. **Current positioning / messaging** (ads, website, pitch deck, proposals -- whatever the buyer sees)
9. **Timeframe of decline** (when did it start? "since Q3 2025", "last 6 months", etc.)

### Nice to have
10. **Historical positioning** (what they said/pitched before the decline)
11. **Industry context** (anything the client suspects changed -- new competitors, regulation, platform updates)
12. **Previous AdGradr or ECHO reports** (if they exist)
13. **Sales conversation notes** (for Type B/D: what are buyers saying when they stall or say no? what objections changed?)

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

Use Google Trends directly via WebSearch. For each keyword, search for current interest levels, seasonal patterns, and related rising queries in the target geography.

**What to search for per keyword:**
- `site:trends.google.com "{keyword}"` for trending context
- `"{keyword}" search trends {year} {geography}` for recent coverage of demand shifts
- Google Trends UI manually at `trends.google.com/trends/explore` for visual inspection

**Geo targeting:**
- Set the geography in the Google Trends interface to match the client's market
- Compare national vs. regional interest to identify geographic shifts
- Use 12-month and 5-year views to separate seasonal patterns from structural changes

**Limitations:**
- WebFetch on trends.google.com rate-limits (429s). Use WebSearch to find Trends data discussed in articles, or pull data from the Trends UI manually.
- For higher-volume automated access, consider a Trends API service.

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
   - **Desire mediated**: What desire does this competitor's positioning promise to fulfill? Not the feature -- the underlying want. A shutters company selling "50% off" mediates the desire for a deal. One selling "the last blinds you'll ever buy" mediates the desire for permanence. Different desires, same product.
   - **Model presented**: Who or what does the competitor hold up as the aspirational model? Their founder? Their customers? A lifestyle? A standard? This is who the buyer is invited to become by choosing this provider.

**Desire landscape mapping** (do this after documenting all competitors):
- Map which desires each competitor mediates. Group them.
- Identify **contested desires**: 3+ competitors fighting to mediate the same desire (e.g., everyone promises "peace of mind")
- Identify **underserved desires**: desires no competitor addresses (e.g., nobody speaks to the desire for independence from ongoing maintenance)
- Identify **suppressed desires**: desires the market actively avoids naming (e.g., status, fear of judgment, envy of neighbors) -- these are often the most powerful positioning territory because competitors won't go there
- Note the **direction of imitation**: who is copying whom? Is there a market leader everyone else mimics? Has the client been pulled into imitating competitors, or have competitors converged on the client's original positioning?

**Convergence analysis** (layer on top of desire mapping):
- What messaging angle do most competitors use? Count them.
- Are there angles NO competitor is using? List them.
- Are there angles 3+ competitors fight over? List them.
- How does the client's messaging compare to the field?
- Calculate a convergence assessment: low (varied messaging), moderate (some clustering), high (most say similar things), extreme (indistinguishable)
- Assess **mimetic intensity**: Is the market in early differentiation (competitors still distinct), active convergence (competitors copying the leader), or mimetic crisis (everyone indistinguishable, competing only on price)?

### 1C. Economic and Platform Context

**Do as much as available data allows.**

- Search for industry-specific news in the client's vertical (last 6-12 months)
- Check for Google Ads platform changes that affected the vertical (auction changes, AI features, policy updates)
- Check for economic indicators relevant to the vertical (if B2C: consumer confidence, housing starts, employment. If B2B: industry growth, funding trends, hiring trends)
- Check for regulatory or policy changes affecting the vertical
- Check for geopolitical or macro events affecting buyer psychology (tariffs, trade policy, AI disruption anxiety, etc.)

### 1D. Client Position Analysis

**From client-provided data + research.**

- Document the client's current messaging (from their ads, website, landing pages)
- Document their performance trend (CPA, ROAS, CPC, conversion rate -- whatever they can provide)
- Note when the decline started and any events they associate with it
- Compare their messaging to the competitive landscape captured in 1B
- Assess differentiation: Is the client saying something different, or the same thing as everyone else?

---

## Phase 2: Snapshot Capture

Structure all Phase 1 findings into a market state snapshot. Use the schema in `references/snapshot-schema.md`.

**Save the snapshot** as a markdown file in the engagement folder:
`{engagement-folder}/snapshots/{client-name}-{period-label}-{date}.md`

For a `diagnose` engagement, capture TWO snapshots:
1. **Current snapshot**: From the research just completed
2. **Baseline snapshot**: Reconstructed from historical data

The baseline can be reconstructed from:
- Google Trends historical data (it goes back 5 years)
- Wayback Machine captures of competitor websites
- Client's historical ad copy and performance data
- Previous AdGradr/ECHO reports if they exist
- Industry reports or news from the baseline period

The baseline will be less complete than the current snapshot. That's fine. Capture what you can reconstruct. Flag what you couldn't find.

---

## Phase 3: Shift Diagnosis

Compare the two snapshots and classify what changed. A market shift is rarely one thing. Most real shifts are a combination of factors. Identify which are contributing and estimate their relative weight.

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

In Girardian terms: the desires buyers are imitating shifted. The models they look to changed. A market that used to desire "the cheapest option" now desires "the option that makes me feel in control." The old desire didn't disappear -- it was displaced by a more urgent one. Businesses still mediating the old desire wonder why their messaging stopped working.

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

In Girardian terms: a new mediator appeared. Buyers don't desire autonomously -- they desire through models (people or brands they want to be like). When a new model enters and captures attention, desire redirects toward whatever that model mediates. The existing players didn't get worse. A new model made them feel outdated by redefining what buyers should want.

Diagnostic criteria:
- A new competitor appeared in the landscape that wasn't there before
- The new entrant's messaging or positioning is pulling buyers away
- Auction insights show new impression share competitors
- The new entrant introduced a positioning angle that made existing messaging feel outdated
- The new entrant presents a different aspirational model than incumbents (e.g., tech-forward vs. traditional, transparent vs. opaque, founder-led vs. corporate)
- Buyer language is shifting to mirror the new entrant's framing (they're adopting the disruptor's vocabulary)

### Producing the Diagnosis

For each contributing shift category:
1. State the finding with specific evidence (not speculation)
2. Cite the data source (Google Trends, competitive research, client data, news)
3. Estimate relative contribution (primary driver, contributing factor, minor factor)
4. Explain the mechanism: how does this shift cause the symptoms the client sees?

**Important:** Do not diagnose shifts you can't support with evidence. "We couldn't determine..." is a valid finding. Speculation disguised as diagnosis destroys credibility.

---

## Phase 4: Repositioning Recommendation

Based on the shift diagnosis, recommend how the client should reposition. Different shift types call for different responses.

### Response Framework by Shift Type

**For Competitive Convergence (Anti-Mimetic Repositioning):**
- Identify the open positioning territory from the desire landscape map (desires no competitor mediates)
- Look especially at suppressed desires -- the ones competitors avoid naming. These are often the strongest repositioning territory precisely because competitors won't follow you there.
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

### Repositioning Principles

1. **Diagnose before prescribing.** The recommendation must flow from the diagnosis. Never recommend messaging changes without explaining which shift they address.
2. **One primary move.** Multiple small changes dilute impact. Identify the single highest-leverage repositioning move and make it the headline recommendation. Supporting moves are secondary.
3. **Concrete, not abstract.** "Differentiate your messaging" is not a recommendation. "Lead your Google Ads with [specific angle] instead of [current angle], because [specific evidence from the competitive analysis]" is a recommendation.
4. **Testable.** Every recommendation should be something the client can implement and measure within 30-90 days.
5. **Honest about uncertainty.** If the diagnosis is ambiguous, say so. If the recommendation is a hypothesis that needs testing, say so. Overconfident recommendations on weak evidence are worse than honest uncertainty.

---

## Deliverable Structure

The BEAR deliverable is a single document with these sections. Save to:
`{engagement-folder}/BEAR-diagnosis-{client-name}-{date}.md`

```markdown
# BEAR Diagnosis: {Client Name}
## {One-sentence summary of what shifted}

**Prepared:** {date}
**Market:** {vertical} in {geography}
**Period analyzed:** {baseline period} vs. {current period}
**Keywords analyzed:** {list}

---

## Executive Summary
{3-5 sentences. What changed, why it matters, what to do about it. A busy executive should be able to read only this section and understand the situation.}

---

## The Symptom
{What the client is experiencing. Performance data showing the decline. When it started. How severe it is. This is the "presenting problem" -- the reason they came to us.}

---

## The Diagnosis

### Primary Shift: {Category Name}
{Detailed findings with evidence. What changed, when, how we know.}

### Contributing Factor: {Category Name} (if applicable)
{Secondary shift contributing to the problem.}

### Ruled Out
{Shifts we investigated and found no evidence for. This builds credibility -- it shows we looked at everything, not just confirmed our first guess.}

---

## The Evidence

### Demand Signals
{Google Trends data, keyword interest changes, rising/declining queries. Charts or tables if available.}

### Competitive Landscape
{Competitor positioning table. Convergence analysis. What changed in the competitive field.}

### Economic and Platform Context
{Relevant macro factors, platform changes, regulatory shifts.}

### Client Position
{Where the client sits relative to the field. Performance data over time.}

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

## Appendix: Market State Snapshots
{Current and baseline snapshots, full data.}
```

---

## Quality Standards

### Evidence requirements
- Every diagnostic claim must cite a specific data source
- "The market shifted" requires evidence of what it shifted FROM and TO
- Competitor analysis must include actual quotes/screenshots/URLs, not summaries from memory
- Google Trends data must include specific numbers or directional data, not vague "interest is declining"

### What BEAR does NOT do
- Score accounts (that's AdGradr)
- Write new ad copy (that's a creative engagement)
- Audit operations (that's SONAR)
- Verify claims against evidence tiers (that's SEAL)
- Monitor competitors over time (BEAR is a point-in-time diagnosis, not ongoing monitoring)

### Confidence protocol
- **HIGH CONFIDENCE**: 3+ independent data sources confirm the finding. State it directly.
- **MODERATE CONFIDENCE**: 1-2 data sources support it, no contradicting evidence. State it with the evidence cited.
- **LOW CONFIDENCE**: Suggestive but not confirmed. Flag it explicitly: "Possible contributing factor, but we lack sufficient data to confirm."
- **INSUFFICIENT DATA**: We looked and couldn't find enough to diagnose. Say so. Don't speculate.

### Engagement folder structure
```
BEAR/{client-name}/
  BEAR-diagnosis-{client-name}-{date}.md    # The deliverable
  snapshots/
    {client-name}-current-{date}.md          # Current market state
    {client-name}-baseline-{date}.md         # Reconstructed baseline
  research/
    competitors/                              # Raw competitive research notes
    trends/                                   # Google Trends data captures
    context/                                  # Economic, platform, news research
  sources/                                    # Client-provided data (ad exports, screenshots)
```

---

## Integration Points

### With AdGradr (when available)
- Pull the client's top keywords by spend/impressions from their AdGradr audit
- Pull CPA/ROAS/CPC trends from the audit data
- Use auction insights data for competitor identification
- BEAR diagnosis can be linked from the AdGradr report as "why your numbers changed"

### With ECHO (when built)
- ECHO provides real-time competitive ad messaging for the client's keywords
- ECHO corpus provides historical competitive messaging for temporal comparison
- BEAR can trigger an ECHO pull as part of Phase 1B competitive research

### Standalone (always works)
- BEAR works without AdGradr or ECHO
- All data can be gathered via web research and client-provided exports
- This is the mode for first engagements and for clients who haven't run AdGradr

---

## Version History

- **1.0.0** (2026-04-06): Initial build. Self-contained market shift diagnosis skill. Four phases: signal collection, snapshot capture, shift diagnosis, repositioning. Five shift categories. Structured deliverable template. No external skill dependencies.
- **1.1.0** (2026-04-06): Added Symptom Taxonomy (Types A-E). BEAR now handles close rate collapse, referral drought, and pipeline stall -- not just ad performance decline. Inputs section updated with symptom-specific performance data requirements and sales conversation notes. Signal collection priorities now vary by symptom type.
- **1.2.0** (2026-04-06): Integrated Girardian analysis natively. Competitive research now includes desire mediation mapping, model identification, suppressed desire detection, and direction-of-imitation tracking. Shift categories deepened with mimetic theory. Anti-mimetic repositioning framework added.
- **1.3.0** (2026-04-06): Replaced vague "use WebSearch for Trends" with proper Google Trends research protocol. WebFetch URLs with geo-targeting and date parameters, multi-keyword comparison URLs, SerpAPI integration path, structured capture table, fallback chain when Trends blocks. Snapshot schema enriched with category-vs-niche divergence and geographic shift tracking. Competitive research now includes desire mediation mapping, model identification, suppressed desire detection, and direction-of-imitation tracking. Shift categories deepened: Competitive Convergence reframed as Mimetic Crisis, Demand Shift as Desire Migration, Model Disruption as New Mediator. Repositioning framework upgraded with anti-mimetic strategy (imitation trap test, suppressed desire territory, defensibility analysis). All Girardian concepts are our own implementation from public theory -- no external skill dependencies.
- **1.4.0** (2026-04-07): First real engagement (Titan Shutters, Melbourne) validated the full workflow. Improved Google Trends research guidance.
- **2.0.0** (2026-04-07): Forked into open source (methodology) and closed source (operational tooling). Open source version uses manual Google Trends research via WebSearch. Removed SerpAPI dependency.
