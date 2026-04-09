# BEAR Method v3.16.0

**Buyer Environment Analysis & Repositioning**

BEAR is a diagnostic method for Claude Code that answers two questions most businesses never ask:

1. **Is your category still growing?**
2. **Are you differentiated within it?**

If the answer to both is yes, you're a star. Invest. If the answer to both is no, you're a dog. No amount of internal optimization will save you.

Most businesses skip this determination entirely. They assume the category is fine and the problem is execution. They fire the agency, rewrite the ads, restructure the team. Six months later, nothing improved. They do it again. BEAR makes the determination they skip.

## How it works

```
Phase 0:  Workspace Setup
Phase 1:  Signal Collection (demand, competitive landscape, economic context, industry signals)
Phase 2A: Shift Diagnosis (what changed, classified into 6 categories)
Phase 2B: Evidence Weighing (stress-test the diagnosis before acting on it)
Phase 2C: Market Position Assessment (Star, Cash Cow, Question Mark, or Dog)
Phase 3:  Repositioning Recommendation (based on the quadrant, not one-size-fits-all)
Phase 4:  Scenario Modeling (three conditional projections tied to observable indicators)
Phase 5:  SimPanel Validation (optional buyer panel testing via simpanel.ai)
```

## Five symptom types

BEAR isn't just for ad performance decline. It handles:

- **Type A: Acquisition decline** (leads dried up, CPAs doubled)
- **Type B: Close rate collapse** (leads come in but deals don't close)
- **Type C: Referral drought** (referral sources went quiet)
- **Type D: Pipeline stall** (proposals out, nothing moving)
- **Type E: Mixed** (everything slowed down)

## Six shift categories

When a business moves from star toward dog, one of six external forces is usually responsible:

- **Competitive Convergence (Mimetic Crisis)**: everyone says the same thing, market collapses into price competition
- **Demand Shift (Desire Migration)**: buyers want something different now
- **Platform Change**: the channel repriced
- **External Shock**: regulation, economy, geopolitics changed the rules
- **Model Disruption (New Mediator)**: a new player redirected buyer attention
- **Category Dissolution**: the service category itself is losing viability (supply flood + price anchor collapse + buyer migration to adjacent categories)

## Market Position Assessment

After diagnosing what shifted, BEAR determines where the client sits:

| | Category Growing | Category Not Growing |
|---|---|---|
| **Differentiated** | **Star.** Adapt to the shift, keep investing. | **Cash Cow.** Harvest, explore adjacent categories. |
| **Undifferentiated** | **Question Mark.** Differentiate now or become a dog. | **Dog.** Fundamental repositioning or exit. |

The quadrant determines the type of recommendation. What you tell a dog is fundamentally different from what you tell a star having a bad quarter.

## Signal Registry

14 industry tags with pre-mapped data sources: home services, roofing, HVAC, tree service, shutters/blinds, ecommerce, agency, SaaS, professional services, healthcare, restaurant, real estate, auto, fitness. Plus a general fallback.

## Chart generation

Five chart types ship with BEAR, generated from JSON data:

- Confidence/indicator timeline
- Search vs. lead gap
- Competitive convergence map
- Cost pressure bars
- Pulse sparklines

## What makes BEAR different

BEAR uses Girardian mimetic theory natively. It doesn't just count competitors and compare messaging. It maps what desires each competitor mediates, identifies suppressed desires nobody will name, traces the direction of imitation, and recommends anti-mimetic positioning that competitors can't easily copy.

The repositioning framework includes an "imitation trap" test: if competitors copy your new positioning, does it still work? If not, it's not defensible. BEAR finds the positioning that is.

## Install

```bash
git clone https://github.com/alexmakarski/bear-method.git
cd bear-method
./install-bear.sh
```

See [INSTALL.md](INSTALL.md) for details.

## Quick start

```
/bear diagnose {client-name}    # Full market shift diagnosis
/bear pulse {client-name}       # Weekly monitoring check
```

## Optional: buyer validation

BEAR's Phase 5 integrates with [SimPanel](https://simpanel.ai) to test repositioning recommendations against synthetic buyer panels before presenting to clients. This phase is optional and human-gated.

## Open source vs. operational

This is the open source methodology. Same diagnostic framework, same shift categories, same evidence standards. Works as a standalone Claude Code skill using manual web research.

The operational version (used internally at [ClickMakers](https://clickmakers.io)) automates the data collection and delivery:

| | Open source | Operational |
|---|---|---|
| Methodology | Full | Full |
| Market position assessment | Star/Dog grid from manual research | Star/Dog grid confirmed by leading AND trailing government data |
| Google Trends | Manual WebSearch | Structured API with timeseries data |
| Competitive landscape | Manual WebSearch | Google Maps (competitor counts, ratings), Shopping (price landscape), Autocomplete (buyer intent signals) |
| Sector health data | Manual WebSearch | 16 live data feeds: GDP by industry, employment by county, sector revenue, FRED, BLS JOLTS, commodity prices, shipping rates, news volume, wage trends, Polymarket, and more |
| Chart data | Manual JSON assembly | Auto-populated from API responses |
| Client delivery | Local files | One-command publish to shared wiki |
| Team workflow | Single user | Sync diagnoses across team members |
| Diagnosis comparison | Manual | `/bear diff` compares any two diagnoses side by side |
| Weekly pulse | ~15 min (manual lookups) | ~5 min (automated data pulls) |

The methodology is identical. The difference is data depth and delivery speed. [Learn more at clickmakers.io](https://clickmakers.io)

## Ecosystem

BEAR is part of a family of open-source diagnostic methods:

| Method | What it diagnoses | Repo |
|--------|-------------------|------|
| **SEAL** | "What's actually true here, verified against evidence?" | [seal-method](https://github.com/alexmakarski/seal-method) |
| **SONAR** | "Where is the margin going and what's the highest-leverage operational fix?" | [sonar-method](https://github.com/alexmakarski/sonar-method) |
| **BEAR** | "What changed in your market and what does it mean for your positioning?" | This repo |

These feed into commercial products ([AdGradr](https://adgradr.com), ECHO, [SimPanel](https://simpanel.ai)) but work independently as standalone diagnostic tools.

## License

MIT. See [LICENSE](LICENSE).
