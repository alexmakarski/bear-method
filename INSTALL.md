# Installing BEAR

## Quick install

```bash
git clone https://github.com/alexmakarski/bear-method.git
cd bear-method
./install-bear.sh
```

This copies the BEAR skill into `~/.claude/skills/bear/`.

## What gets installed

| Component | Location | Purpose |
|-----------|----------|---------|
| BEAR skill | `~/.claude/skills/bear/SKILL.md` | The diagnostic methodology |
| Snapshot schema | `~/.claude/skills/bear/references/snapshot-schema.md` | Market state capture format |

## Usage

Open Claude Code in any project directory:

```
/bear diagnose {client-name}    # Full market shift diagnosis
/bear snapshot {client-name}    # Single market state capture
/bear compare {client-name}     # Compare two existing snapshots
```

BEAR will ask for the required inputs (client details, keywords, geography, symptom description) before starting.

## Google Trends data

BEAR uses Google Trends data for demand signal analysis. The open source version uses WebSearch to gather this data manually. For automated structured access, consider a Google Trends API service.

## Ecosystem

BEAR is part of a family of diagnostic products:

- **[SEAL](https://github.com/alexmakarski/seal-method)** -- Forensic evidence review and strategic analysis
- **[SONAR](https://github.com/alexmakarski/sonar-method)** -- Operational diagnostics and automation readiness
- **BEAR** -- Market shift diagnosis and repositioning
- **AdGradr** -- Ad account grading (ClickMakers)
- **ECHO** -- Competitive ad messaging analysis (ClickMakers)
- **SimPanel** -- Synthetic buyer panel validation (Orchestratr.ai)
