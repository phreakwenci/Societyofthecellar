---
name: convert-to-federal-law
description: Convert one extracted Biblical law record into a section of the Federal Code of the United States of Christ, with agency, inspection process, licensing, punishments, black markets, corruption, propaganda, and scene ideas. Argument: a law id from UnitedStatesOfChrist/data/json/, e.g. "exo-020-008-remember-the-sabbath".
---

# Convert Biblical Law into Federal Law

Work inside `UnitedStatesOfChrist/`. Input: one record from
`data/json/<id>.json` (run `/extract-biblical-law` first if it doesn't
exist). Follow `prompts/expand_law.md`.

Append the drafted section to `docs/FederalCode.md` under the correct
Title (structure is defined at the top of that file), containing:

- Federal Code Section number (`USC-C <title>.<chapter>.<section>`) with
  source record id + scripture citation
- Agency Responsible — must be registered in `docs/Agencies.md`; register
  new agencies there first, with acronym, parent, mandate, one telling
  detail
- Inspection Process
- Citizen Requirements
- Licensing (permits, exemptions, fees, renewal cadence)
- Punishments (graded; note where the biblical penalty was commuted and
  where — pointedly — it wasn't)
- Appeals Process (Covenant Courts; the two-witness rule warps appeals)
- Technology Used
- Black Market Opportunities
- Common Corruption
- Propaganda (poster verse + slogan)
- Examples (2-3 one-line enforcement vignettes)
- Scene Ideas

Voice: deadpan statutory prose. The satire is the gap between verse and
paperwork — never wink. Keep continuity with existing sections and the
world rules in `docs/WorldBible.md` (enforced-loudly vs.
deferred-indefinitely lists are canon).

Afterward, add a `federal_code_section` note to the source JSON record's
`bureaucratic_uses` if absent, and rerun `python3 tools/build_index.py`.
