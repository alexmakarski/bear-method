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

## Optional: SerpAPI for Google Trends

BEAR works without SerpAPI. It falls back to WebFetch and WebSearch for Google Trends data. But structured API data is more reliable.

To set up SerpAPI:

1. Sign up at [serpapi.com](https://serpapi.com) ($25/mo for 1,000 searches)
2. Copy `.env.example` to `.env` in your project root
3. Add your API key
4. Copy `tools/serpapi.sh` to your project's `.claude/tools/` directory

The SerpAPI tool is a shared utility. It serves both BEAR (Google Trends engine) and ECHO (Google Search engine) if you use both products.

## Usage

Open Claude Code in any project directory:

```
/bear diagnose {client-name}    # Full market shift diagnosis
/bear snapshot {client-name}    # Single market state capture
/bear compare {client-name}     # Compare two existing snapshots
```

BEAR will ask for the required inputs (client details, keywords, geography, symptom description) before starting.

## Ecosystem

BEAR is part of a family of diagnostic products:

- **[SEAL](https://github.com/alexmakarski/seal-method)** -- Forensic evidence review and strategic analysis
- **[SONAR](https://github.com/alexmakarski/sonar-method)** -- Operational diagnostics and automation readiness
- **BEAR** -- Market shift diagnosis and repositioning
- **AdGradr** -- Ad account grading (ClickMakers)
- **ECHO** -- Competitive ad messaging analysis (ClickMakers)
- **SimPanel** -- Synthetic buyer panel validation (Orchestratr.ai)
