# Installing BEAR

## Quick install

```bash
git clone https://github.com/alexmakarski/bear-method.git
cd bear-method
./install-bear.sh
```

This copies the BEAR skill and chart tool into your Claude Code directories.

## What gets installed

| Component | Location | Purpose |
|-----------|----------|---------|
| BEAR skill | `~/.claude/skills/bear/SKILL.md` | The diagnostic methodology |
| Chart generator | `~/.claude/tools/bear-charts.py` | Produces PNG charts for diagnoses and pulses |

## Requirements

- Claude Code CLI
- Python 3.8+ with matplotlib (for chart generation)

```bash
pip install matplotlib
```

## Usage

Open Claude Code in any project directory:

```
/bear diagnose {client-name}    # Full market shift diagnosis
/bear pulse {client-name}       # Weekly monitoring check (requires prior diagnosis)
```

BEAR will ask for the required inputs (client details, keywords, geography, symptom description) before starting.

## Google Trends data

BEAR uses Google Trends data for demand signal analysis. The open source version uses WebSearch to gather this data manually. For automated structured access, consider a Google Trends API service.

## Chart generation

BEAR includes a chart generator (`bear-charts.py`) that produces five chart types from JSON input:

```bash
python3 ~/.claude/tools/bear-charts.py timeline data.json output.png
python3 ~/.claude/tools/bear-charts.py convergence data.json output.png
python3 ~/.claude/tools/bear-charts.py search-lead-gap data.json output.png
python3 ~/.claude/tools/bear-charts.py cost-pressure data.json output.png
python3 ~/.claude/tools/bear-charts.py sparkline data.json output.png
```

## Optional: SimPanel integration

BEAR's Phase 5 optionally validates repositioning recommendations against synthetic buyer panels via [SimPanel](https://simpanel.ai). This is not required for a complete BEAR diagnosis.

## Going further

This open source version gives you the full BEAR methodology. If you find yourself running diagnoses regularly, the operational version at [ClickMakers](https://clickmakers.io) removes the manual data collection work:

- **16 live data feeds** including Google Trends, Maps, Shopping, Autocomplete, GDP by industry, employment by county, sector revenue, FRED, BLS JOLTS, commodity prices, shipping rates, news sentiment, wage trends, Polymarket, and more
- **Leading + trailing signal stack** that confirms the Star/Dog determination with both real-time Trends data and government economic data
- **One-command publishing** to a shared wiki your clients can access
- **Team sync** so any team member can pulse a client another team member diagnosed
- **Diagnosis diffs** that compare two diagnoses side by side for QBRs

The methodology you're running is the same one. The operational version just makes the data collection faster and the delivery smoother.

## Ecosystem

BEAR is part of a family of diagnostic products:

- **[SEAL](https://github.com/alexmakarski/seal-method)** : Forensic evidence review and strategic analysis
- **[SONAR](https://github.com/alexmakarski/sonar-method)** : Operational diagnostics and automation readiness
- **BEAR** : Market shift diagnosis and repositioning
- **[SimPanel](https://simpanel.ai)** : Synthetic buyer panel validation
