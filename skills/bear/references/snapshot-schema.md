# BEAR Market State Snapshot Schema

A snapshot captures the state of a client's market at a single point in time. Two snapshots compared = a BEAR diagnosis.

---

## Snapshot Structure

```yaml
snapshot:
  metadata:
    client: "Business name"
    market: "Industry / vertical / niche"
    geography: "Target geography"
    captured: "YYYY-MM-DD"
    period_label: "current | baseline | YYYY-QN"
    keywords: ["keyword1", "keyword2", "keyword3", "keyword4", "keyword5"]
    sources_used: ["google_trends", "serp_analysis", "client_data", "web_research", "economic_data"]

  demand_signals:
    # Google Trends data for each keyword
    # Source URLs: https://trends.google.com/trends/explore?q={keyword}&geo={geo}&date=today%2012-m
    keyword_trends:
      - keyword: "keyword1"
        interest_12m_direction: "rising | declining | stable | volatile"
        interest_5y_direction: "rising | declining | stable | volatile"
        current_vs_peak: "XX% of 12-month peak"
        peak_period: "Month YYYY"
        trends_url: "https://trends.google.com/trends/explore?q=..."
    # Rising related queries (from Google Trends "Related queries" > "Rising")
    rising_queries: ["query1", "query2", "query3"]
    # Declining related queries
    declining_queries: ["query1", "query2"]
    # Breakout queries (>5000% growth, flagged "Breakout" by Google Trends)
    breakout_queries: ["query1"]
    # Category vs keyword divergence (is the broader category healthy while client's niche shrinks?)
    category_vs_niche: "aligned | diverging | unknown"
    # Geographic interest shifts
    geographic_shifts: "description of any regional changes in interest"

  competitive_landscape:
    # Who is advertising and what they're saying
    competitors_identified: 5-15
    competitor_positions:
      - name: "Competitor A"
        domain: "competitor-a.com"
        primary_message: "What their ads/positioning lead with"
        messaging_angle: "discount | expertise | speed | trust | fear | transformation | other"
        proof_type: "social_proof | authority | guarantee | none"
        offer_structure: "Description of their offer"
        channels_observed: ["google_ads", "meta_ads", "organic", "linkedin"]
    # Convergence analysis
    convergence:
      dominant_angle: "The messaging angle most competitors use"
      convergence_score: "low | moderate | high | extreme"
      pct_using_dominant: "XX% of competitors lead with the same angle"
      underserved_angles: ["angles no competitor is using"]
      contested_angles: ["angles 3+ competitors fight over"]

  client_position:
    current_messaging: "What the client's ads/positioning/proposals say"
    messaging_angle: "discount | expertise | speed | trust | fear | transformation | other"
    differentiation_vs_field: "differentiated | partially_differentiated | indistinguishable"
    symptom_type: "A_acquisition | B_close_rate | C_referral | D_pipeline_stall | E_mixed"
    # Acquisition metrics (Type A)
    acquisition_indicators:
      cpa_trend: "rising | declining | stable"
      roas_trend: "rising | declining | stable"
      impression_share_trend: "rising | declining | stable"
      cpc_trend: "rising | declining | stable"
      lead_volume_trend: "rising | declining | stable"
    # Close/pipeline metrics (Types B, D)
    pipeline_indicators:
      close_rate: "XX% (current) vs XX% (baseline)"
      close_rate_trend: "rising | declining | stable"
      avg_deal_cycle_days: "XX days (current) vs XX days (baseline)"
      proposal_win_rate: "XX%"
      deals_stalled_by_stage: {"discovery": X, "proposal": X, "negotiation": X}
      common_stall_reason: "Description of what buyers say or do when they stall"
    # Referral metrics (Type C)
    referral_indicators:
      referral_volume: "X/month (current) vs X/month (baseline)"
      referral_sources_active: X
      referral_sources_gone_quiet: X
      referral_quality_change: "same | declining | unknown"
    # If ad data available
    ad_performance:
      avg_cpa: "$XX"
      avg_roas: "X.Xx"
      avg_cpc: "$X.XX"
      top_keywords_by_spend: ["kw1", "kw2", "kw3"]

  economic_context:
    # Industry-specific indicators
    industry_health: "growing | stable | contracting"
    relevant_indicators:
      - indicator: "e.g., housing starts, consumer confidence, employment in sector"
        direction: "up | down | flat"
        magnitude: "description of change"
    # Platform changes
    platform_changes:
      - platform: "Google Ads | Meta | LinkedIn"
        change: "Description of algorithm/feature/policy change"
        impact: "Description of impact on advertisers"
    # External events
    external_events:
      - event: "Description"
        impact_on_market: "How this affects buyer behavior or advertiser costs"

  buyer_psychology:
    # What buyers in this market care about now
    primary_concerns: ["concern1", "concern2", "concern3"]
    # What they used to care about (if different)
    shifted_from: ["old_concern1", "old_concern2"]
    # Decision factors in priority order
    decision_hierarchy: ["factor1", "factor2", "factor3"]
    # Trust signals that matter
    trust_requirements: ["requirement1", "requirement2"]
```

---

## Usage Notes

- Not every field will be populated for every snapshot. Use what's available.
- The baseline snapshot can be reconstructed from historical data (Google Trends has 5 years of history, Wayback Machine has historical pages, client may have old reports).
- Snapshots are stored as markdown files with YAML frontmatter in the engagement folder.
- The diff between two snapshots is what produces the shift diagnosis.

## Minimum Viable Snapshot

For a first engagement, you need at minimum:
1. `demand_signals.keyword_trends` (from Google Trends)
2. `competitive_landscape.competitor_positions` (from web research)
3. `competitive_landscape.convergence` (from analyzing the positions)
4. `client_position.current_messaging` (from client input)
5. `client_position.symptom_type` + the matching indicator block:
   - Type A: `acquisition_indicators`
   - Type B: `pipeline_indicators` (especially close_rate and common_stall_reason)
   - Type C: `referral_indicators`
   - Type D: `pipeline_indicators` (especially deals_stalled_by_stage and avg_deal_cycle_days)
   - Type E: whatever they have

Everything else enriches the diagnosis but isn't blocking.
