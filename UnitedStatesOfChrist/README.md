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

## Status

- [x] Corpus pipeline (66 books converted, 472 contradictions indexed)
- [x] Schema + skills + agency registry
- [x] Seed extraction: Exodus 20 (Decalogue) + Exodus 21 (Covenant Code)
- [ ] Exodus 22–23, Leviticus, Deuteronomy
- [ ] New Testament norms (household codes, qualifications, Sermon on the Mount)
- [ ] Federal Code expansion per law
