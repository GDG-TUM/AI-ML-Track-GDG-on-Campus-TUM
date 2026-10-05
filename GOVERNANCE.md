# Governance

This page explains who does what in the AI/ML Track and how decisions get made. It exists so that the track **keeps working when people graduate, get busy or change roles**. Student communities turn over every year, and clear rules are what make a track outlive its founders.

The track is part of **GDG on Campus TUM** and operates under the chapter's core team and organization-level policies. Where this repository is silent, the [organization-level documents](https://github.com/GDG-TUM/.github) apply.

## Roles

| Role | Who | What they do | Repo permission |
|------|-----|--------------|-----------------|
| **Track Lead** | One person, appointed by the chapter's core team | Owns the vision and semester plan, runs sessions, makes the final call when consensus fails, keeps the track healthy | Admin |
| **Co-Lead** | Optional, up to two | Shares the lead's work, acts as backup, is the planned successor | Admin |
| **Maintainer** | Active members trusted with the repo | Review and merge pull requests, triage issues, help run sessions, mentor newcomers | Write |
| **Mentor** | Senior students, alumni, industry guests | Coach a project team, review work, give talks. May not need repo access. | Triage |
| **Member** | Anyone in the GDG-TUM organization taking part | Attend, learn, build, help each other, contribute by pull request | Fork and PR |
| **Contributor** | Anyone who has had a pull request merged | Credited in the project and in release notes | n/a |

> [!NOTE]
> **Current team:** Track Lead: Lewis Kagiri ([@10kwise](https://github.com/10kwise)). Maintainers and mentors are listed in [`.github/CODEOWNERS`](.github/CODEOWNERS) and announced in the track channel. Update this note whenever the team changes.

## How decisions are made

We use **lazy consensus**: a proposal goes ahead if nobody raises a reasoned objection in the discussion period.

| Kind of decision | Where | Who decides | Discussion period |
|---|---|---|---|
| Typos, small fixes, new resources | Pull request | One maintainer approves | None |
| New session content, notebooks, projects | Pull request | One maintainer approves, lead informed | About 3 days |
| Changes to workflow, tooling, CI, labels | Pull request | Lead plus one maintainer | 3 to 7 days |
| Curriculum shape, schedule, tools we teach | Issue, then a [decision record](docs/decisions/README.md) | Track Lead after consulting maintainers | 7 days |
| Governance, Code of Conduct changes | Pull request | Track Lead with chapter core team | 7 days |
| Conduct reports | Private, via [gdgtum@gmail.com](mailto:gdgtum@gmail.com) | Chapter core team, per the [Code of Conduct](CODE_OF_CONDUCT.md) | n/a |

When people disagree, we:

1. Discuss on the issue or pull request, focusing on the goal (what helps learners most).
2. Try to find a compromise or run a small experiment.
3. If still stuck, the **Track Lead decides** and writes down why in a decision record. Anyone may ask for the decision to be revisited next semester.

Important decisions go in [`docs/decisions/`](docs/decisions/README.md) so the next cohort knows *why*, not just *what*.

## Becoming a maintainer

You can be nominated by any maintainer, or nominate yourself with an issue, after you have:

- been active for **at least one semester** (or about 10 weeks)
- had **several pull requests merged** across more than one area (docs, notebooks, projects)
- **helped others**: reviews, answers, helping run a session
- shown you understand and live the [Code of Conduct](CODE_OF_CONDUCT.md)

The Track Lead decides after checking with current maintainers. Being a maintainer is a service, not a prize. It means reviewing work, answering questions and showing up.

## Stepping down and inactivity

Life happens: exams, attachments, graduation. Step down any time by telling the lead, and nobody will think less of you. After **one semester of inactivity**, a maintainer is moved to Member with thanks and can return at any time. Access is reviewed at every handover.

## Handover (every academic year)

Before a lead or co-lead leaves:

1. Name and **mentor the successor** for at least one month.
2. Work through the **handover checklist** in the [maintainers guide](docs/maintainers-guide.md#handover).
3. Transfer admin access, API keys and accounts to the chapter's shared owners, **never to a personal-only account**.
4. Update this page, `CODEOWNERS` and the roadmap.

**The rule of two:** the track should always have at least **two people with admin access**, so nothing depends on one person.

## Changing this document

Open a pull request. Governance changes need a 7-day discussion period and approval from the Track Lead and the chapter core team.
