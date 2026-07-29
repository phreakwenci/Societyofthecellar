---
name: extract-biblical-law
description: Parse Biblical material and extract every legal, ritual, civil, moral, ceremonial, familial, dietary, governmental, judicial, military, and religious law into a structured database for the fictional United States of Christ. Use when asked to extract laws from a book, chapter, or verse range of the Bible. Argument: book name or range, e.g. "Exodus 21-23" or "Leviticus 19".
---

# Extract Biblical Law

Work inside `UnitedStatesOfChrist/`. Read `CLAUDE.md` there first if you
haven't this session.

## Inputs

1. `data/books/<nn>-<book>.md` — KJV text, `## Book N` chapter headers.
2. `data/sab/<nn>-<book>.json` — SAB annotation index: per-verse category
   flags and contradiction cross-refs (`ref` is `chapter.verse`).
3. `data/sab/contradictions.json` — full contradiction index by `con` id.
4. If `data/books/` is missing, ask for the EPUB and run
   `python3 tools/convert_epub.py <path>`.

## Procedure

Read the assigned range **sequentially**. Whenever you encounter a
command, prohibition, statute, ritual requirement, punishment, obligation,
legal precedent, judicial instruction, governmental principle, permission,
ideal, or leadership qualification: **create one record.**

- **Do not combine laws.** One law per record. Adjacent verses on one
  topic are still separate records if they state separate norms.
- Extract norms embedded in narrative (precedents) and broad exhortations
  (`law_type: "ideal"`) — the regime turns ideals into policy.
- Do not skip anything for being tedious, redundant, or ugly.

## Record

Write each record to `data/json/<id>.json`, conforming to
`tools/schema/law.schema.json`. ID scheme:
`<3-letter bookslug>-<chapter 3 digits>-<first verse 3 digits>-<kebab-title>`
(slug table in `CLAUDE.md`). Fields cover: identity/citation, testament,
categories (Civil, Moral, Ceremonial, Dietary, Judicial, Family, Economic,
Religious, Military, Property, Sexual, Purity, Festival, Governmental),
law_type, KJV text, summary, original audience, immediate context,
historical context (Ancient Near East scholarship — cite comparanda like
Hammurabi where real), penalty, exceptions, cross references, related NT
passages, internal contradictions (use SAB `con` ids), SAB categories,
USofC implementation, agency (registered in `docs/Agencies.md` — reuse
before inventing), constitutional analogue, scene ideas, satirical uses,
bureaucratic uses, confidence (high/medium/low).

Ground `internal_contradictions` and `sab_categories` in the SAB index for
the passage — copy what's there, add scholarly contradictions it misses.

## After emitting records

Run `python3 tools/build_index.py`. It validates every record against the
schema, regenerates `data/laws/*.md` (Markdown tables), and rebuilds
`data/json/laws.json`, `data/csv/laws.csv`, and `data/laws/INDEX.md`.
Fix validation errors before finishing.

Report coverage: chapters walked, records emitted, passages judged
non-normative and why.
