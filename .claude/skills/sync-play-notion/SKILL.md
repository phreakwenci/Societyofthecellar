---
name: sync-play-notion
description: Sync United States of Christ play-development content (timeline, characters, relationships, open threads, writing status) into the project's Notion page, built on the Atlas methodology (Timeline / Character Database / Relationship Database / Writing Tracker). Use whenever the user asks to update Notion, sync the play bible, add a character/scene/beat to Notion, or check the play-development board. Requires the `atlas` skill for Atlas philosophy and reference files (timeline.md, character-database.md, relationship-database.md, writing-tracker.md) — load it alongside this one.
---

# Sync USOC Play Development to Notion

The Notion page **"United States of Christ - Play Development"**
(`https://app.notion.com/p/38236b1a5996805e9bccc4251cd6dd48`) is the
Atlas-format mirror of this repo's play-development docs. It exists
**downstream** of the repo, not instead of it.

## Source of truth hierarchy

```
UnitedStatesOfChrist/docs/*.md   ← canon lives here (git-tracked, dated
  PlayBible.md                    revision logs, stable IDs — CH-##,
  CaseLaw.md                      SCENE-###, CASE-###, B<year>.<n>)
  StateDoctrine.md
  ConstitutionalHistory.md
  TheMoscowModel.md
         │  translate into lean Atlas rows, cross-link back with
         │  backtick-quoted doc names (e.g. `CaseLaw.md` CASE-003)
         ▼
Notion "Play Development" page  ← Atlas mirror: Timeline, Character
  (this skill)                    Pages, Romantic Relationships, Writing,
                                   Tasks. Notes point back to the repo doc;
                                   they do not duplicate its full prose.
```

**Never let the two diverge silently.** If you add or change a beat,
character, or scene in the repo docs, update the corresponding Notion
row(s) in the same session. If a fact is decided in Notion first (e.g. an
open thread gets resolved by discussion there), port the resolution back
into the repo doc's Open Threads / Revision Log and commit it — the repo
is still canon.

## Database IDs (data sources) — check before minting new columns

Read these directly; do not re-fetch the parent page to rediscover them.

| Component | Notion DB | Data source ID |
|---|---|---|
| Timeline | `Timeline` | `38236b1a-5996-81ad-abb0-000bc9d80e9c` |
| Character Database | `Character Pages` | `38236b1a-5996-8181-8c32-000be997c4fe` |
| Relationship Database | `Romantic Relationships` | `38236b1a-5996-817b-bff4-000bdb06e972` |
| Writing Tracker | `Writing` | `38236b1a-5996-81aa-bb74-000b46bac29a` |
| To-Do List | `Tasks` | `38236b1a-5996-816f-a083-000bca426276` |

Fetch a data source directly with the Notion `fetch` tool using
`collection://<id>` to see current rows/schema before adding more —
faster than walking the parent page's columns again.

## Schema notes specific to this project (deviations from generic Atlas)

- **Timeline `Character` column** is multi-select, pre-seeded with the
  named cast (Mark, Constance, Chris, Laura, Able, Jeff, The Priest,
  Immigrant Girl) plus a **`The Family`** group tag for beats where all
  five household members are present — use the group tag, not five names.
- **Timeline `Location` column** uses story-specific tags: `Moscow (town)`,
  `Family Home`, `The Camp`, `The Pier`, `Courthouse Tribunal`,
  `California / the Border`, `State Custody`. Add new ones via
  `notion-update-data-source` (`ALTER COLUMN "Location" SET SELECT(...)`)
  — include ALL existing options plus the new one, or the existing ones
  are silently dropped.
- **In-fiction epoch:** Year 0 (Ratification) = **2032** for Timeline
  dating purposes (arbitrary but fixed — do not redate existing rows).
  Year 1 = 2033, Year 5 = 2037, Year 10 = 2042. Pre-history (the Moscow
  Model's founding decade) runs 2016–2031.
- **Writing `Type` column** was extended beyond generic Atlas defaults
  with `Play` and `Scene` (a stage play doesn't fit One Shot/Short
  Story/Novel). Use `Scene` for individual `SCENE-###` tracker cards,
  `Play` for the full-script tracker card.
- **Character Database `Status`** field only has `Alive`/`Dead`/`Alive
  (Officially Dead)` — Mark's ambiguous "disappeared" ending is recorded
  as `Alive` with a Trivia note, not a new status value (avoid schema
  sprawl for a one-off narrative ambiguity; use prose for nuance the
  schema can't hold).
- **Relationship `Relationship Status`** was extended with a custom value,
  `Forcibly Separated (Regime)`, for state-seized relationships (Laura &
  her classmate) that aren't a breakup in the ordinary Atlas sense.

## Adding new select/multi-select option values

The Notion API rejects unregistered select values at page-creation time
(`create-pages` will fail the whole batch, not just the bad row). Always
register new options first with `notion-update-data-source`:

```
ALTER COLUMN "<Column>" SET SELECT('existing1':color, 'existing2':color, 'new value':color)
```

List **every** existing option alongside the new one(s) — the statement
replaces the option set, it doesn't append. Do this for both the
Timeline's `Location`/`Character` columns and any Character/Relationship
select fields before batch-creating pages that use a new value.

## Workflow: "sync Notion" / "update the play board"

1. Read whatever repo doc changed (`PlayBible.md`, `CaseLaw.md`,
   `StateDoctrine.md`, etc.) for the specific new/changed content.
2. Identify which Atlas component(s) it touches (new beat → Timeline; new
   character → Character Pages; new ship/relationship → Romantic
   Relationships; new scene draft or status change → Writing; new/resolved
   Open Thread → Tasks).
3. Keep entries lean (Atlas philosophy: trust the filter, tags do the
   work) — one line per Timeline event, short Trivia bullets on character
   pages, no paragraph dumps in a row. Depth goes on the entry's own page,
   not the row.
4. Cross-link back to the repo with backtick doc names and IDs (e.g.
   `` `CaseLaw.md` CASE-007 ``) so a reader can always find the full
   reasoning.
5. Run the Atlas completeness checklist before ending: Timeline ✓
   Characters ✓ Relationships ✓ Writing ✓ Tasks ✓. Don't leave one stale
   while updating another.
6. If the sync surfaces a decision (an Open Thread got resolved, a name
   got picked), write that resolution back into the repo doc's Open
   Threads/Revision Log too — commit and push as usual. Notion is not a
   substitute for the git-tracked canon.

## Dependency

This skill assumes **`atlas`** is loaded for the general Notion/Atlas
philosophy and reference files. Load both when doing Notion sync work on
this project.
