---
name: detect-contradictions
description: Analyze how the United States of Christ resolves a scriptural contradiction — Old Testament law vs New Testament teaching vs historical Christian interpretation — and what the resolution reveals about the regime. Argument: a law id, an SAB contradiction id (e.g. "con101"), or a topic (e.g. "sabbath", "usury").
---

# Detect Contradictions

Work inside `UnitedStatesOfChrist/`.

## Inputs

- `data/sab/contradictions.json` — 472 indexed contradictions, each with
  id, title, stances, and citation lists. If given a topic, search titles;
  if given a law id, read the record's `internal_contradictions`.
- The cited passages in `data/books/`.
- Existing rulings in `docs/DenominationalNotes.md` (CSC table) — stay
  consistent with them or explicitly overturn with a new ruling number.

## For each contradiction, produce

1. **Literal conflict?** — quote both sides (KJV, public domain), state
   whether the conflict is real, apparent, or manufactured.
2. **Historical resolution** — how the tension was actually handled
   (rabbinic, patristic, Reformation-era), briefly and accurately.
3. **Denominational readings** — Evangelical, Catholic, Orthodox,
   Mainline: one honest paragraph each.
4. **How the authoritarian state resolves it** — the CSC ruling: which
   side becomes law, which becomes "eschatological counsel," and the
   official reasoning (deadpan).
5. **Political advantages** — who benefits from this resolution.
6. **Possible hypocrisy** — the fingerprint: what the resolution reveals
   the regime actually worships.
7. **Scene ideas** — 2-3 dramatic beats.

## Output

Append to `docs/DenominationalNotes.md` under "Contradiction analyses"
with a new CSC ruling number (continue the sequence), and add/update the
`internal_contradictions` entries of any affected law records in
`data/json/` (then rerun `python3 tools/build_index.py`).

Accuracy discipline: real theology and history must be represented
fairly — the fiction only lands if the interpretive moves are ones real
traditions actually made. Invent the regime, not the scholarship.
