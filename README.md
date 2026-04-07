# BEAR Method v2.0.0

**Buyer Environment Analysis & Repositioning**

BEAR is a diagnostic method for Claude Code that answers: "Your business development stopped working. Here's why, and the cause isn't inside your business."

Markets shift. Competitors converge. Buyer priorities change. Platform algorithms reprice. External shocks rewrite the rules. The business owner sees symptoms (CPA doubled, close rate collapsed, referrals dried up, pipeline stalled) but the cause isn't in their account or their operations. It's in their market.

No existing product diagnoses this systematically. BEAR does.

## How it works

```
Phase 1: Signal Collection (Google Trends, competitive landscape, economic context, client data)
Phase 2: Snapshot Capture (structured market state at two points in time)
Phase 3: Shift Diagnosis (what changed, classified into 5 categories)
Phase 4: Repositioning Recommendation (concrete, testable, one primary move)
```

## Five symptom types

BEAR isn't just for ad performance decline. It handles:

- **Type A: Acquisition decline** -- leads dried up, CPAs doubled
- **Type B: Close rate collapse** -- leads come in but deals don't close
- **Type C: Referral drought** -- referral sources went quiet
- **Type D: Pipeline stall** -- proposals out, nothing moving
- **Type E: Mixed** -- everything slowed down

## Five shift categories

- **Competitive Convergence (Mimetic Crisis)** -- everyone says the same thing, market collapses into price competition
- **Demand Shift (Desire Migration)** -- buyers want something different now
- **Platform Change** -- the channel repriced
- **External Shock** -- regulation, economy, geopolitics changed the rules
- **Model Disruption (New Mediator)** -- a new player redirected buyer attention

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
/bear snapshot {client-name}    # Single market state capture
/bear compare {client-name}     # Compare two existing snapshots
```

## Open source vs. operational

This is the open source methodology. It teaches the diagnostic framework and works as a standalone Claude Code skill using manual web research.

The operational version (used internally at [ClickMakers](https://clickmakers.io)) adds automated data pipelines, structured API integrations, monitoring, and visual output. The methodology is the same. The tooling is different.

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
