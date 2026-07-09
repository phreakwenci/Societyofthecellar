# United States of Christ

Worldbuilding database for a fictional American Christian theocracy.

The premise: what happens when a government actually tries to enforce the
Bible — all of it — as federal law. Every command, prohibition, statute,
ritual requirement, punishment, obligation, judicial instruction, and
governmental principle in Scripture is extracted as a structured record,
then translated into the Federal Code of the United States of Christ,
complete with agencies, inspection regimes, licensing, black markets, and
the selective enforcement that gives a regime its fingerprints.

This is a work of fiction and satire.

## How it works

```
Skeptic's Annotated Bible (local EPUB, not committed)
        │  tools/convert_epub.py
        ▼
data/books/   KJV text (public domain)
data/sab/     annotation index: category flags + 472 contradictions
        │  /extract-biblical-law   (Claude skill)
        ▼
data/json/    one JSON record per law  ←  source of truth
        │  tools/build_index.py
        ▼
data/laws/    one Markdown record per law
data/csv/     flat index
        │  /convert-to-federal-law  (Claude skill)
        ▼
docs/FederalCode.md    the statute book of the USofC
        │  /detect-contradictions   (Claude skill)
        ▼
docs/DenominationalNotes.md    how the regime picks and chooses
```

See `CLAUDE.md` for conventions and `docs/WorldBible.md` for the world.

## The Catalog and the Constitution

`data/catalog/CATALOG.md` enumerates the **complete legal corpus**: all
**613 commandments of the Torah** (classical enumeration, thematic order)
plus **109 enforceable New Testament norms** — each with citation,
category, Federal Code Title, responsible agency, and enforcement status
(enforced / adapted / deferred / abeyance / classified / omitted /
counsel). The status distribution is the regime's fingerprint.

`docs/Constitution.md` is the full Constitution of the United States of
Christ built on that corpus — every clause cites its scriptural warrant,
with the contradictions deliberately embedded for dramatic use. Two
companion docs analyze it: `docs/ConstitutionalModel.md` (what real
traditions it's built from — American/Confederate form, Iranian clerical
machinery, Puritan franchise, a Brexit-style referendum origin, and the
four scholarly schools that fought over it) and `docs/ConstitutionalHistory.md` (how its
meaning drifts toward clerical supremacy over the first decade without a
word of the text changing).

Rebuild after editing catalog parts: `python3 tools/build_catalog.py`
(fails unless the OT count is exactly 613).

## Status

- [x] Corpus pipeline (66 books converted, 472 contradictions indexed)
- [x] Schema + skills + agency registry
- [x] Seed deep extraction: Exodus 20 (Decalogue) + Exodus 21 (Covenant Code)
- [x] Full catalog: 613 Torah commandments + 109 NT norms, all assigned
- [x] Constitution of the United States of Christ
- [x] Constitutional model + 10-year drift history (Brexit origin)
- [x] State Doctrine (governance model) + Play Bible (`United States of Christ`)
- [ ] Deep records for remaining catalog entries (use `/extract-biblical-law`)
- [ ] Federal Code sections per law (use `/convert-to-federal-law`)
