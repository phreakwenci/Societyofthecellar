# Prompt: Parse Book

Read the supplied book text (`data/books/<book>.md`) sequentially, with its
SAB annotation index (`data/sab/<book>.json`) open alongside.

Whenever you encounter a command, prohibition, statute, ritual requirement,
punishment, obligation, legal precedent, judicial instruction, permission,
ideal, leadership qualification, or governmental principle: create **one
record**, conforming to `tools/schema/law.schema.json`, written to
`data/json/<id>.json`.

Rules:

- Do not combine laws. One law per record, even when verses share a topic.
  Exodus 20:4 (no images) and 20:5 (don't bow to them) are two records.
- Do not skip laws because they are boring, repetitive, or embarrassing.
  Boring is the point; embarrassing is the plot.
- A narrative can contain a law (precedent). Genesis 9:6 is a statute
  inside a story. Extract it.
- Broad exhortations count as `law_type: "ideal"` — the USofC turns ideals
  into administrative policy, so capture them.
- Where the SAB index flags the passage, copy its categories into
  `sab_categories` and its contradiction refs into `internal_contradictions`.
- Continue until the end of the assigned range. Report verse coverage when
  done: which chapters were walked, how many records emitted, what was
  deliberately judged non-normative.

After emitting records, run `python3 tools/build_index.py`.
