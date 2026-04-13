# Syncing BEAR Open Source from Internal

**Purpose:** When the internal BEAR skill (clickmakers-io/bear) gets updated, use this recipe to sync changes to the open-source version (alexmakarski/bear-method). This avoids re-deciding what to include every time.

---

## The rule

The internal SKILL.md is the source of truth. The open-source version is a subset: same methodology, different data collection (WebSearch instead of MCP), and no operational features.

**Never patch the open-source file independently.** Always start from the internal version and strip down.

---

## What stays in open source

### Methodology (copy directly, adapt data collection only)

- Symptom Taxonomy (Type A-E) -- copy verbatim
- Phase 1A: Google Trends Research -- replace `google_trends` MCP calls with WebSearch on trends.google.com
- Phase 1B: Competitive Landscape Research -- replace `google_search`/`google_maps` MCP calls with WebSearch. Keep invisible competitor assessment, desire landscape mapping, convergence analysis, mimetic intensity
- Phase 1C: Economic and Platform Context -- replace `fred_data`, `country_macro`, `commodity_prices`, `news_volume`, `polymarket`, `shipping_rates` MCP calls with WebSearch equivalents. Keep the per-country routing logic (US/CA/AU) but express as "search for X" instead of "call tool X"
- Phase 1D: Client Position Analysis -- copy verbatim
- Phase 1E: Industry-Specific Signals -- copy verbatim (already uses WebSearch)
- Phase 2A: Shift Diagnosis -- copy verbatim. All 6 shift categories including Category Dissolution
- Phase 2B: Evidence Weighing -- copy the **non-SEAL** version only (the "When SEAL integration is NOT active" path). This includes evidence scoring, symmetric weighing, actor analysis, asymmetry check, and verdict
- Phase 2C: BEAR Position Grid -- copy verbatim. Both measured axes, all four quadrants (Grizzly, Roaming, Hibernating, Bear Trap), government trailing data confirmation via WebSearch
- Phase 3: Repositioning Recommendation -- copy the **standard format** (Format A). All shift-type response frameworks. Repositioning principles. No tiered output (that's SEAL-dependent)
- Phase 4: Scenario Modeling -- copy verbatim
- Signal Registry -- copy all 14 industry tags with WebSearch query templates
- Quality Standards -- copy verbatim
- Deliverable template -- copy Format A only

### Features (copy with minor adaptation)

- `/bear diagnose` mode -- the only mode in open source
- Phase 0: Workspace Setup -- adapt file paths if needed
- Locale awareness -- copy the locale rules
- Supply-side validation protocol -- copy verbatim

### Charts

- **Position Grid only.** Include the chart generation instructions for the position grid.
- Remove all other chart types (timeline, search-lead-gap, convergence map, cost pressure bars, pulse sparklines)
- Remove bear-charts.py references for non-grid charts

### SimPanel (Phase 5) -- tease, don't enable

- Keep the Phase 5 section explaining what SimPanel validation does and why
- Gate it: "Requires SimPanel MCP server. See simpanel.ai for access."
- Keep the BEAR Signal Summary format (it's useful documentation even without SimPanel)
- Keep the "What SimPanel validation does NOT do" section

---

## What gets stripped out

### Modes

- **Pulse mode** -- remove entirely (section, template, cadence notes, all references)
- **Sync mode** -- remove entirely
- **Diff mode** -- remove entirely
- Remove these from the `modes:` frontmatter line. Only `[diagnose]` remains.

### SEAL integration

- **Phase 1F** (Evidence Package Assembly) -- remove entirely
- **Phase 2D** (Recommendation Package / SEAL safety gate) -- remove entirely
- **Phase 2A "When SEAL integration is active"** conditional block -- remove. Keep only the standard Phase 2A flow.
- **Phase 2B "When SEAL integration is active"** conditional block -- remove. Keep only the non-SEAL evidence weighing path.
- **Phase 3 "Tiered output"** section -- remove. Keep Format A only.
- **Phase 3 deliverable Format B** -- remove entirely
- All references to evidence tiers, Cynefin domains, safety tiers, human gates A/B

### Automation

- Walk-away automation (MCP auto-approve, PostToolUse error hook, circuit breaker) -- remove entirely
- Any references to MCP auto-approve or error hooks

### Publishing

- Outline auto-publishing -- remove entirely
- Upload integrity protocol -- remove
- Any references to Outline

### Charts (except Position Grid)

- bear-charts.py references for non-grid charts
- Timeline chart instructions and references
- Search-lead-gap chart instructions and references
- Convergence map chart instructions and references
- Cost pressure bars chart instructions and references
- Pulse sparklines chart instructions and references
- Keep Position Grid chart instructions only

### Deliverable template sections

- "What Changed Since Last Diagnosis" section -- remove (requires Diff/prior engagement)
- Pulse output template -- remove
- Format B (tiered/SEAL) template -- remove

---

## MCP-to-WebSearch translation table

When you encounter an MCP tool call in the internal version, replace it with the WebSearch equivalent:

| Internal (MCP) | Open source (WebSearch) |
|---|---|
| `google_trends(keyword="X", geo="US", date="today 12-m")` | WebSearch: "Google Trends {keyword}" and manually check trends.google.com |
| `google_search(query="X")` | WebSearch: "{query}" |
| `google_maps(query="X", location="Y")` | WebSearch: "{query} near {location}" |
| `google_autocomplete(query="X")` | WebSearch: type "{query}" in Google and note autocomplete suggestions |
| `google_shopping(query="X")` | WebSearch: "{query}" on Google Shopping |
| `fred_data("consumer_sentiment")` | WebSearch: "FRED consumer sentiment index current" |
| `commodity_prices("aluminium")` | WebSearch: "aluminium price LME current" |
| `shipping_rates(lane="X")` | WebSearch: "container shipping rates {lane} current" |
| `news_volume(query="X")` | WebSearch: "{query} news" and assess volume/sentiment manually |
| `polymarket(query="X")` | WebSearch: "Polymarket {query}" |
| `bls_jolts(industry="X")` | WebSearch: "BLS JOLTS {industry} latest" |
| `business_formation(sector="X")` | WebSearch: "Census business formation {sector} latest" |
| `wage_trends(industry="X")` | WebSearch: "BLS median wages {industry} latest" |
| `bea_gdp_by_industry(industry="X")` | WebSearch: "BEA GDP by industry {industry} latest quarter" |
| `bls_qcew(industry="X", area="Y")` | WebSearch: "BLS QCEW {industry} {area} latest" |
| `census_sector_revenue(industry="X")` | WebSearch: "Census sector revenue {industry} latest" |
| `country_macro("CA", "central_bank_rate")` | WebSearch: "Bank of Canada overnight rate current" |
| `country_macro("CA", "exchange_rate")` | WebSearch: "USD CAD exchange rate" |
| `country_macro("AU", "central_bank_rate")` | WebSearch: "RBA cash rate current" |
| `country_macro("AU", "building_approvals")` | WebSearch: "ABS building approvals latest" |

The pattern: replace the structured API call with a WebSearch that finds the same data point. The methodology doesn't change, only the retrieval method.

---

## Sync process

1. Read the internal SKILL.md (`01-Products/bear-full/skills/bear/SKILL.md`)
2. Copy the full file
3. Walk through the "What gets stripped out" list above. Remove each item.
4. Walk through the MCP-to-WebSearch table. Replace each MCP call with its WebSearch equivalent.
5. Update the frontmatter: `modes: [diagnose]`, version number to match internal
6. Update README.md if any feature descriptions changed
7. Read the result end to end. Verify a user with no MCP tools could follow every step using only WebSearch.
8. Commit with a message referencing the internal version being synced from (e.g., "Sync with internal v4.0.0")

---

## Version numbering

Open source tracks the internal version number. When internal ships v4.1.0, open source syncs and also becomes v4.1.0. The content differs (subset) but the version tells you which internal release it's derived from.
