# Fullstack Engineer Skill Builder Prompt

This repository stores a reusable **Fullstack Engineer Skill Builder** prompt.

## Files
- `FULLSTACK_ENGINEER_SKILL_BUILDER.md`: canonical prompt text, normalized and deduplicated.

## How to use
1. Copy the prompt into your assistant/system context.
2. Fill in the kickoff template fields.
3. Start with **Phase 1** before writing any code.

## Phase 1 kickoff questions
- What problem does this solve (business outcome)?
- Who are the users, and what are they forbidden from doing?
- What happens when it fails?
- What existing systems must it integrate with?
- What is the smallest useful version to ship?

## Kế hoạch đề xuất
- Xem `GOAL_COMPLETION_PROPOSAL.vi.md` để có kế hoạch hành động cụ thể theo Phase/Layer.


## Audience & objective
- Audience: programmers and AI-assisted product teams.
- Objective: use this skill as a company-grade engineering playbook to ship commercial products with strong quality gates.


## Community-driven improvement
- `COMMUNITY_PERFECTING_LOOP.md`: process to collect and apply community feedback continuously.
- `feedback/FEEDBACK_LOG_TEMPLATE.md`: standard table to capture and triage signals.


## Skill package
- `SKILL.md`: executable skill rules including mandatory post-task missing-points conclusion.
- `templates/TASK_RETRO_TEMPLATE.md`: template to report result + shortcomings after each task.


## Automation
- CI workflow: `.github/workflows/validate-missing-points.yml`
- Local check: `python scripts/validate_missing_points.py --path task_reports --strict`
- Purpose: fail validation if any task report is missing the required `Missing Points Conclusion` block fields.
