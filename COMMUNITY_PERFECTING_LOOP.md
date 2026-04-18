# Community Perfecting Loop

This document defines how to continuously collect and apply community feedback so the skill gets better over time.

## Reality check
You cannot collect "all" opinions from the entire community.
The practical goal is to capture **representative, high-signal feedback** from multiple communities and convert it into measurable improvements.

## 1) Feedback sources (minimum set)
- GitHub Issues / Discussions (users of this repo)
- Reddit communities related to programming and AI engineering
- Hacker News threads on AI coding workflows
- Developer Discord/Slack groups
- Internal team retrospectives after each shipped feature

## 2) Intake schema (required fields)
Every feedback item must include:
- Source channel
- Link or reference
- User persona (beginner/intermediate/lead/team)
- Problem category (accuracy, speed, security, DX, scalability)
- Evidence (screenshot/log/repro steps)
- Severity (S0-S3)
- Frequency (how often reported)

## 3) Prioritization model
Use score = `(severity x frequency x business impact) / implementation effort`.

Priority bands:
- P0: score >= 24 (fix immediately)
- P1: score 16-23 (next sprint)
- P2: score 8-15 (backlog)
- P3: score <= 7 (defer or reject)

## 4) Change gates before adopting any suggestion
A community suggestion is accepted only if:
1. It maps to a clear business rule.
2. It does not weaken security controls.
3. It includes at least one reproducible test scenario.
4. It is validated by at least two independent reports OR one trusted maintainer review.

## 5) Implementation cadence
- Daily: triage new feedback.
- Weekly: prioritize and plan updates.
- Bi-weekly: release skill patch with changelog.
- Monthly: run a quality benchmark against previous versions.

## 6) Success metrics
Track before/after for each release:
- Prompt failure rate
- Hallucinated dependency rate
- Missing-test rate
- Time to first valid architecture decision
- Escaped production defects

## 7) “Perfecting” definition
The skill is considered closer to "perfect" when:
- Failure rate trends down for 3 consecutive releases.
- No P0 security/process gaps remain open > 7 days.
- 80%+ of new feedback is enhancement (not bug/regression).

## 8) Artifact checklist per iteration
For each improvement cycle, produce:
- Updated prompt section
- Updated examples/templates
- Added/updated tests/checklists
- Release notes with before/after metrics
