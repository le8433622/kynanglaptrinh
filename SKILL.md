# SKILL: Fullstack Product Delivery (AI-Assisted)

## Purpose
This skill guides developers and AI assistants to build commercial-grade software with strict quality gates.

## Non-negotiable rule added by user
After **every task**, you must produce a **Missing Points Conclusion** (thiếu sót) before moving on.

## Required output format per task
1. **Task Result**
   - What was completed.
   - What was verified (tests/checks).
2. **Missing Points Conclusion (Bắt buộc)**
   - What is still missing.
   - Why it was missed (root cause).
   - Impact if left unresolved.
   - Exact next action with owner and deadline.

## Mandatory checklist for each task
- Business rule(s) explicitly stated.
- Contract/types/schema defined before logic.
- Dependency existence verified.
- Tests included (happy path + edge cases + security).
- Missing Points Conclusion written.

## Scoring
Each task is scored 0-2 on five axes:
- Correctness
- Security
- Performance
- Maintainability
- Completeness

If any axis < 2, task cannot be marked "done"; move to follow-up queue.

## Task closure template
Use this exact section at the end of every task report:

### Missing Points Conclusion
- Missing:
- Root cause:
- Risk:
- Action:
- Owner:
- Deadline:


## Automation enforcement
- Run `python scripts/check_missing_points.py reports/tasks` before merge.
- CI must fail if a task report misses the mandatory section or fields.
