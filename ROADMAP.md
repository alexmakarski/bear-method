# BEAR Open Source Roadmap

**Last updated:** 2026-04-13
**Repo:** alexmakarski/bear-method
**Current version:** 4.0.0 (version number only -- methodology not yet synced)

---

## Current state

The open-source SKILL.md is significantly behind the internal (ClickMakers) version. The version number was bumped to 4.0.0 for the Position Grid rename, but the methodology content is still at roughly v3.12.0. This sync is the priority.

---

## Next: Full methodology sync to v4.0.0

**Priority:** CRITICAL
**Target:** Next build session

### What needs to be added

These features exist in the internal BEAR v4.0.0 but are missing from open source:

| Feature | Internal version | What to sync |
|---|---|---|
| Category Dissolution | v3.18.0 | 6th shift category with full diagnostic criteria. Supply glut + price anchor collapse + category migration. Already partially present but missing the invisible competitor assessment and workforce redistribution sections. |
| Supply-side validation | v3.5.0+ | The full protocol with demand-side queries, supply-side queries, adjacent category migration, and the validation table. Partially present but incomplete. |
| Invisible competitor assessment | v3.12.0 | Provider count, freelancer/solo competition, AI tool substitutes, workforce redistribution. The "invisible tip of the competitive landscape" section. |
| Desire landscape mapping | v3.5.0+ | Contested desires, underserved desires, suppressed desires, direction of imitation. Partially present but needs the full Girardian framework. |
| Evidence Weighing (Phase 2B) | v3.10.0 | Actor analysis, asymmetry check, verdict system (Confirmed/Revised/Inconclusive/Rejected). Current open-source version has the basics but is missing actor analysis. |
| BEAR Position Grid | v3.21.0 | Already renamed to the new quadrants. But missing: the measured-axis methodology (Performance Gap formula, Positioning Overlap calculation), government trailing data confirmation, and the grid interpretation per quadrant. Needs full replacement of the old binary questions approach. |
| Scenario Modeling (Phase 4) | v3.10.0 | Three conditional projections with observable indicators. Already present in open source but may need updates. |
| Locale awareness | v3.19.0 | Spelling, terminology, currency adapt to target geography. The open-source version should follow the same locale rules. |
| Chart generation | v3.12.0 | Five chart types. Already present. Add Position Grid as 6th chart type. |

### What to adapt for open source

These features use MCP tools internally. Open-source equivalents use WebSearch.

| Internal feature | Open source adaptation |
|---|---|
| `google_trends` MCP tool | WebSearch on trends.google.com or manual Trends research |
| `fred_data`, `bls_jolts`, etc. | WebSearch for FRED, BLS, Census data |
| `country_macro` (CA, AU) | WebSearch for StatCan, ABS, Bank of Canada, RBA data |
| `commodity_prices` | WebSearch for LME, commodity price sources |
| `google_search`, `google_maps` | Standard WebSearch |
| Government trailing data confirmation | WebSearch for BEA GDP-by-industry, BLS QCEW, Census sector revenue |

The methodology is identical. Only the data retrieval method changes.

### What to remove

These features don't belong in open source:

| Feature | Why remove |
|---|---|
| **Pulse mode** | Account management tool for ongoing client relationships. Without MCP, it's a 15-minute manual slog. Open source is a diagnostic tool, not an account management system. |
| **Sync mode** | Pulls diagnoses from Outline wiki for team use. Open-source users don't have Outline. Team workflow feature. |
| **Diff mode** | Compares two historical diagnoses for QBRs/renewals. Requires multiple engagements over time. Agency workflow, not one-off diagnostic. |
| **Walk-away automation** | MCP auto-approve, PostToolUse error hook, circuit breaker. Requires MCP infrastructure. |
| **Outline publishing** | One-command publish to shared wiki. Requires Outline. |
| **SEAL integration** | Phase 1F evidence package, SEAL grading, tiered recommendations. Internal product integration, not open-source methodology. |

### What to tease but gate

| Feature | How to handle |
|---|---|
| **SimPanel Validation (Phase 5)** | Keep the section. Explain what it does and why. Link to simpanel.ai. But gate it: "Requires SimPanel MCP server. See simpanel.ai for access." Users can see the value but can't run it without the product. |

### Deliverable template changes

- Remove Pulse output template
- Remove "What Changed Since Last Diagnosis" section (requires Diff mode / prior engagement)
- Update Position Grid section (already done)
- Keep Scenario Outlook
- Keep SimPanel Buyer Validation section (gated)

### Version History

Clean up the version history. The open-source version doesn't need to track every internal release. Summarize into meaningful milestones.

---

## Build plan for the sync

1. **Start from the internal SKILL.md as the source of truth.** Don't patch the open-source file. Read the internal version, strip out MCP-specific tooling, SEAL integration, Pulse/Sync/Diff/automation, and replace MCP tool calls with WebSearch equivalents.

2. **Sections to copy from internal, adapting data collection only:**
   - Symptom Taxonomy (should be identical already)
   - Phase 1A-1E signal collection (replace MCP tool calls with WebSearch)
   - Phase 2A shift diagnosis with all 6 categories
   - Phase 2B evidence weighing (full version with actor analysis)
   - Phase 2C BEAR Position Grid (full measured-axis version)
   - Phase 3 repositioning recommendation (standard format only, no SEAL tiered output)
   - Phase 4 scenario modeling
   - Phase 5 SimPanel validation (gated)
   - Signal Registry (keep all 14 industry tags, use WebSearch queries)
   - Chart generation (add position grid)
   - Deliverable template (updated)
   - Quality standards

3. **Sections to remove entirely:**
   - Pulse Mode
   - Sync Mode
   - Diff Mode
   - Walk-away automation
   - Outline publishing
   - Phase 1F (SEAL integration)
   - Phase 2D (SEAL recommendation package)
   - SEAL-specific Phase 2A/2B/3 conditional sections

4. **Modes line in frontmatter:** change from `[diagnose, pulse]` to `[diagnose]`

5. **README.md:** Already updated. May need minor tweaks after SKILL.md sync (remove Pulse/Diff mentions if any remain).

6. **Test:** Read the final open-source SKILL.md end to end. Verify a new user with no MCP tools could follow it and produce a complete BEAR diagnosis using only WebSearch.

---

## Future (not in this sync)

| Item | Notes |
|---|---|
| Back-testing examples | Run BEAR on known crises (COVID, tariffs, AI disruption) and publish the results as example engagements. Good for marketing and methodology validation. |
| Install script improvements | Current install.sh may need updating for the new structure. |
| Example engagement | Ship one complete example engagement (anonymized) so users can see what the output looks like before running their own. |
