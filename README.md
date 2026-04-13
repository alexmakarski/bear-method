# BEAR Method v4.0.0

**Buyer Environment Analysis & Repositioning**

BEAR is a diagnostic method for Claude Code that answers: "Your business development stopped working. Here's why, and the cause isn't inside your business."

It reads market signals, analyzes the competitive environment, identifies what shifted, and produces a diagnosis with repositioning recommendations.

## How it works

```
Phase 0:  Workspace Setup
Phase 1:  Signal Collection (demand, competitive landscape, economic context, industry signals)
Phase 2A: Shift Diagnosis (what changed, classified into 6 categories)
Phase 2B: Evidence Weighing (stress-test the diagnosis before acting on it)
Phase 2C: BEAR Position Grid (two measured axes, four quadrants)
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

When a business stops growing, one of six external forces is usually responsible:

- **Competitive Convergence (Mimetic Crisis)**: everyone says the same thing, market collapses into price competition
- **Demand Shift (Desire Migration)**: buyers want something different now
- **Platform Change**: the channel repriced
- **External Shock**: regulation, economy, geopolitics changed the rules
- **Model Disruption (New Mediator)**: a new player redirected buyer attention
- **Category Dissolution**: the service category itself is losing viability (supply flood + price anchor collapse + buyer migration to adjacent categories)

## BEAR Position Grid

After diagnosing what shifted, BEAR plots the client on two measured axes:

- **X-axis: Performance Gap** -- how much the client's decline exceeds (or trails) the market's demand change
- **Y-axis: Positioning Overlap** -- what percentage of competitors share the client's primary messaging angle

| | Underperforming market | Tracking/beating market |
|---|---|---|
| **Differentiated** (low overlap) | **Hibernating.** Positioned differently but bleeding. The differentiation isn't landing or it's aimed at the wrong desire. Repoint, don't abandon. | **Grizzly.** Differentiated and performing. Protect what's working, adapt to the shift. |
| **Converged** (high overlap) | **Bear Trap.** Losing faster than the market and nothing distinguishes you. Incremental fixes won't work. Fundamental repositioning or category exit. | **Roaming.** Tracking the market but without territory of your own. Differentiate now before conditions tighten. |

The quadrant determines the type of recommendation. What you tell someone in a Bear Trap is fundamentally different from what you tell a Grizzly having a rough quarter.

## Signal Registry

Each engagement is tagged with an industry. The tag determines which additional data sources BEAR pulls beyond the baseline (Trends, competitive landscape, economic context).

| Tag | Industry | Additional signals |
|-----|----------|--------------------|
| `home_services` | Plumbing, electrical, cleaning | Housing starts, permits, home sale volume |
| `roofing` | Roofing and exterior | Storm/hail data, FEMA disaster declarations, insurance claims |
| `hvac` | Heating, ventilation, AC | Temperature anomalies, energy prices, refrigerant regulations |
| `tree_service` | Tree care and removal | Storm data, municipal ordinances, pest outbreaks |
| `shutters_blinds` | Window coverings | Aluminium/PVC prices, energy prices, building codes |
| `ecommerce` | Online retail / DTC | Tariffs, shipping costs, FX rates, consumer spending |
| `agency` | Marketing / creative / dev | AI adoption, platform revenue, freelancer marketplace growth |
| `saas` | Software as a Service | VC funding trends, tech layoffs, churn benchmarks |
| `professional_services` | Law, accounting, consulting | Regulatory changes, M&A activity, AI displacement |
| `healthcare` | Medical, dental, specialists | Insurance reimbursement, telehealth adoption, demographics |
| `restaurant` | Food service and hospitality | Food costs, labor/minimum wage, delivery platform commissions |
| `real_estate` | Agents, brokers, property mgmt | Mortgage rates, inventory, days on market, NAR settlement |
| `auto` | Dealerships, repair, detailing | Used car price indices, EV adoption, parts supply chain |
| `fitness` | Gyms, studios, personal training | Membership trends, boutique vs. big-box, at-home fitness |
| `general` | Anything not listed | Baseline signals only |

## Chart generation

Six chart types ship with BEAR, generated from JSON data:

- Confidence/indicator timeline
- Search vs. lead gap
- Competitive convergence map
- Cost pressure bars
- Pulse sparklines
- BEAR Position Grid

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

The operational version (used internally at [ClickMakers](https://clickmakers.io)) is powered by **market-signals MCP**, a remote MCP server with 18 live data tools across three layers:

**Global tools (any country):**

| Tool | What it provides |
|------|------------------|
| `google_trends` | Search interest timeseries (0-100 index, weekly) |
| `google_search` | Organic results + ads for competitive research |
| `google_maps` | Local competitor counts, ratings, review volumes |
| `google_autocomplete` | Buyer intent signals, category migration queries |
| `google_shopping` | Price landscape, seller counts, product ratings |
| `commodity_prices` | 9 commodities (aluminium, oil, copper, natural gas, etc.) |
| `wb_commodity_prices` | 29 commodities from World Bank (timber, metals, fertilizers, rubber, agriculture) |
| `shipping_rates` | Container shipping rates by trade lane |
| `news_volume` | Article count and sentiment by keyword over time |
| `polymarket` | Prediction market probabilities on economic/political events |

**US macro tools:**

| Tool | What it provides |
|------|------------------|
| `fred_data` | 13 US macro indicators (consumer sentiment, CPI, unemployment, etc.) |
| `bls_jolts` | Monthly layoffs, job openings, hires by industry |
| `business_formation` | New business applications by sector (leading indicator of supply flood) |
| `wage_trends` | Annual median wages by industry (wage compression = supply flood) |
| `bea_gdp_by_industry` | Quarterly GDP growth/contraction by sector |
| `bls_qcew` | Quarterly employment and wages by industry and county |
| `census_sector_revenue` | Monthly/quarterly actual revenue by sector |

**Country-specific tools (CA + AU):**

| Tool | What it provides |
|------|------------------|
| `country_macro` | Routes to the correct government data source by country. Canada: Bank of Canada rate, USD/CAD, StatCan GDP/employment/retail/housing/business formation. Australia: RBA cash rate, ABS GDP/unemployment/retail/building approvals. |

The open source version gathers equivalent data via manual WebSearch. The methodology is identical. The difference:

| | Open source | With market-signals MCP |
|---|---|---|
| Data collection | Manual WebSearch per source | 18 structured API calls |
| Country coverage | Any (manual research) | US, Canada, Australia (structured data), any (WebSearch fallback) |
| Position assessment | Leading indicators only | Leading + trailing government data |
| Locale awareness | Manual | Automatic (spelling, currency, data sources route by geography) |
| Chart data | Manual JSON assembly | Auto-populated from API responses |
| Client delivery | Local files | One-command publish to shared wiki |
| Team workflow | Single user | Sync diagnoses across team members |
| Diagnosis comparison | Manual | `/bear diff` compares any two side by side |
| Weekly pulse | ~15 min | ~5 min |

[Learn more at clickmakers.io](https://clickmakers.io)

## Ecosystem

BEAR is part of a family of open-source diagnostic methods:

| Method | What it diagnoses | Repo |
|--------|-------------------|------|
| **SEAL** | "What's actually true here, verified against evidence?" | [seal-method](https://github.com/alexmakarski/seal-method) |
| **ORCA** | "Where is the margin going and what's the highest-leverage operational fix?" | [orca-method](https://github.com/alexmakarski/orca-method) |
| **BEAR** | "What changed in your market and what does it mean for your positioning?" | This repo |

These feed into commercial products ([AdGradr](https://adgradr.com), ECHO, [SimPanel](https://simpanel.ai)) but work independently as standalone diagnostic tools.

## License

MIT. See [LICENSE](LICENSE).
