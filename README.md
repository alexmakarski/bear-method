# BEAR Method v3.12.0

**Buyer Environment Analysis & Repositioning**

BEAR is a diagnostic method for Claude Code that answers: "Your business development stopped working. Here's why, and the cause isn't inside your business."

Markets shift. Competitors converge. Buyer priorities change. Platform algorithms reprice. External shocks rewrite the rules. The business owner sees symptoms (CPA doubled, close rate collapsed, referrals dried up, pipeline stalled) but the cause isn't in their account or their operations. It's in their market.

No existing product diagnoses this systematically. BEAR does.

## How it works

```
Phase 0: Workspace Setup (folder structure + data placement guide)
Phase 1: Signal Collection (Google Trends, competitive landscape, economic context, client data, industry signals)
Phase 2: Shift Diagnosis (what changed, classified into 6 categories)
Phase 2.5: Evidence Weighing (stress-test the diagnosis before acting on it)
Phase 3: Repositioning Recommendation (concrete, testable, one primary move)
Phase 4: Scenario Modeling (three forward-looking scenarios tied to observable indicators)
Phase 5: SimPanel Validation (optional buyer panel testing via simpanel.ai)
```

## Five symptom types

BEAR isn't just for ad performance decline. It handles:

- **Type A: Acquisition decline** (leads dried up, CPAs doubled)
- **Type B: Close rate collapse** (leads come in but deals don't close)
- **Type C: Referral drought** (referral sources went quiet)
- **Type D: Pipeline stall** (proposals out, nothing moving)
- **Type E: Mixed** (everything slowed down)

## Six shift categories

- **Competitive Convergence (Mimetic Crisis)** : everyone says the same thing, market collapses into price competition
- **Demand Shift (Desire Migration)** : buyers want something different now
- **Platform Change** : the channel repriced
- **External Shock** : regulation, economy, geopolitics changed the rules
- **Model Disruption (New Mediator)** : a new player redirected buyer attention
- **Category Dissolution** : the service category itself is losing viability (supply flood + price anchor collapse + buyer migration to adjacent categories)

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

This is the open source methodology. It teaches the diagnostic framework and works as a standalone Claude Code skill using manual web research.

The operational version (used internally at [ClickMakers](https://clickmakers.io)) adds automated data pipelines (SerpAPI, FRED, commodity feeds), MCP server integrations, and publishing workflows. The methodology is the same. The tooling is different.

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
