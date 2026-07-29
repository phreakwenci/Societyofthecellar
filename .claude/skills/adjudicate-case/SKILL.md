---
name: adjudicate-case
description: Given a hypothetical fact pattern in the United States of Christ, produce a structured legal memo — possible charges, available defenses, which scripture each side would cite, how the four denominational blocs would split, and a predicted ruling from the Covenant Courts / CSC. Use when asked what charges a character could face, how a scene would play out legally, or "what would happen if..." Argument: a fact pattern (free text), optionally a PlayBible SCENE-### id.
---

# Adjudicate a Case

Work inside `UnitedStatesOfChrist/`. This is the "legal counsel" capability
of the project: not just storing statutes, but *reasoning* over a fact
pattern the way a lawyer, a defense counsel, and four rival denominational
scholars would — grounded entirely in canon already on file.

## Inputs

1. The fact pattern itself (from the user, or a `PlayBible.md` `SCENE-###`).
2. `data/laws/INDEX.md` + `data/json/*.json` — deep law records (the
   source of truth for any statute you cite).
3. `data/catalog/CATALOG.md` — the full 613+109 catalog, for statutes
   without a deep record yet.
4. `docs/ConstitutionalModel.md` — the Four Schools (Theonomist/Reformed,
   Evangelical, Magisterialist/Liturgical, Old Republican) and their
   interpretive tendencies.
5. `docs/StateDoctrine.md` — governance mechanics: §3 (Degrees of
   Sanctity/class), §10 (due process, variable by class, the household-
   informant exception), §5 (the Manna's surveillance).
6. `docs/DenominationalNotes.md` — standing CSC rulings (1-01…1-04) and
   how each bloc actually holds power.
7. `docs/CaseLaw.md` — prior `CASE-###` memos. Check for precedent before
   writing a new one; a later case may cite an earlier one, the way real
   courts do.

## Ground every move in canon — never invent free-floating

- **Charges** must cite an actual law record or catalog entry (its id,
  citation, penalty, enforcing agency). If no record exists yet for a
  statute you need, run `/extract-biblical-law` first rather than
  asserting a penalty from nothing.
- **Defenses** should be reasoned the way the Bible actually argues with
  itself: a counter-precedent (scripture vs. scripture — e.g. Mark 2:25-27's
  "David ate the showbread" against a strict ritual reading), an
  intent/mens rea argument, or a **procedural** defense grounded in the
  two-witness rule (Deut 19:15, Const. Art. IV §2) — was the offense
  actually witnessed by two qualified parties, or does the case rely on
  the household-informant exception (StateDoctrine §10)?
- **Denominational splits** must track each School's established character
  (`ConstitutionalModel.md`): Theonomists read the plain text and control
  the CSC; Evangelicals read pastorally/publicly and own the media
  (StateDoctrine §5); Magisterialists reason from real Catholic/Orthodox
  moral theology (equity, proportionality, *epikeia* — the virtue of
  departing from the letter when it betrays the lawgiver's true intent);
  Old Republicans fight on process, not merits.
- **The class prediction is mandatory** (StateDoctrine §3, §10): state
  plainly what a low-sanctity-tier defendant actually gets versus what an
  identical fact pattern would get a high-tier defendant. This is the
  play's central mechanism — never omit it.
- **The predicted ruling** must follow from how the CSC/Council actually
  behaves in established canon (selective certification, "eschatological
  counsel" harmonizations, cert denied to cases without doctrinal stakes),
  not from what would be dramatically convenient.

## Procedure

1. Restate the facts; flag any assumption you're inferring.
2. List every charge the prosecution (name the agency — DOR, BDB, FPA,
   SSC, etc.) could plausibly bring, most serious first, each with its
   statute id and stated penalty.
3. List every defense, in the same grounded way.
4. Walk all four Schools' likely position, in character.
5. State the class/tier prediction explicitly.
6. Trace the procedural path (Covenant Court → possible CSC certification)
   and give a predicted outcome — with reasoning, not just a verdict.
7. Add a short "Dramatic notes" pointer back to the relevant PlayBible
   scene/beat, if any.

## Output

Append the memo to `docs/CaseLaw.md` under the next free `CASE-###` id
(check the ID registry there first — never reuse or renumber). Add a row
to that file's Revision Log with the date. If the memo resolves or informs
a `PlayBible.md` scene, add a cross-link there too and bump its version per
that file's own change protocol (§0).

If reasoning here reveals a real gap in the doctrine (as the household-
informant exception did) — propose it as a short, cited addition to
`StateDoctrine.md` rather than leaving it implicit in the memo alone.
