# BEAR Open Source Roadmap

**Last updated:** 2026-04-13
**Repo:** alexmakarski/bear-method
**Current version:** 4.0.0

---

## Current state

Open-source SKILL.md is fully synced with internal v4.0.0 as of 2026-04-13.

### What was synced

| Feature | Status |
|---|---|
| Category Dissolution (6th shift category) | Synced with full diagnostic criteria, invisible competitor assessment, workforce redistribution |
| Supply-side validation protocol | Synced with demand-side queries, supply-side queries, adjacent category migration, validation table |
| Invisible competitor assessment | Synced: provider count, freelancer/solo competition, AI tool substitutes, workforce redistribution |
| Desire landscape mapping | Synced with full Girardian framework: contested, underserved, suppressed desires, direction of imitation |
| Evidence Weighing (Phase 2B) | Synced with actor analysis, asymmetry check, verdict system (Confirmed/Revised/Inconclusive/Rejected) |
| BEAR Position Grid (Phase 2C) | Synced: measured-axis methodology (Performance Gap formula, Positioning Overlap calculation), government trailing data confirmation, four quadrant interpretations |
| Scenario Modeling (Phase 4) | Synced with WebSearch for all indicator lookups |
| Locale awareness | Synced: US/CA/AU spelling, terminology, currency, data source routing |
| Position Grid chart | Standalone `tools/position-grid.py` (replaced `bear-charts.py`) |
| SimPanel Phase 5 | Gated: methodology documented, requires SimPanel MCP server |

### What was removed

| Feature | Why |
|---|---|
| Pulse mode | Operational feature requiring API access for 5-minute runs. Without MCP, it's a 15-minute manual slog. |
| Sync mode | Team workflow feature requiring Outline wiki. |
| Diff mode | Agency workflow for QBRs/renewals, requires multiple engagements over time. |
| Walk-away automation | MCP auto-approve, PostToolUse error hook, circuit breaker. Requires MCP infrastructure. |
| Outline publishing | One-command publish to shared wiki. Requires Outline. |
| SEAL integration | Phase 1F evidence package, SEAL grading, tiered recommendations. Internal product integration. |
| Non-grid charts | Timeline, search-lead-gap, convergence map, cost pressure bars, pulse sparklines. Markdown tables tell the same story. |

### What was changed

| Item | Change |
|---|---|
| `tools/bear-charts.py` | Replaced with `tools/position-grid.py` (Position Grid only, simpler CLI) |
| Chart Generation section | Simplified to single chart type with JSON schema documented |
| Phase 0 | Removed tool availability check (no MCP tools to check) |
| Phase 1C | MCP tool calls replaced with WebSearch equivalents for all geographies |
| Phase 2C | Government trailing data confirmation uses WebSearch instead of MCP tools |
| Phase 4 | All indicator lookups use WebSearch instead of MCP tools |
| Frontmatter modes | Changed from `[diagnose, pulse, sync, diff]` to `[diagnose]` |
| Version history | Condensed to major milestones |

---

## Future

| Item | Notes |
|---|---|
| Back-testing examples | Run BEAR on known crises (COVID, tariffs, AI disruption) and publish the results as example engagements. Good for marketing and methodology validation. |
| Install script improvements | Current install.sh may need updating for the new structure (position-grid.py instead of bear-charts.py). |
| Example engagement | Ship one complete example engagement (anonymized) so users can see what the output looks like before running their own. |
