# Prompt: Classify Laws

Given one or more law records in `data/json/`, verify and correct
classification fields:

- `categories`: one or more of Civil, Moral, Ceremonial, Dietary, Judicial,
  Family, Economic, Religious, Military, Property, Sexual, Purity,
  Festival, Governmental. Use multiple when genuinely multiple; do not pad.
- `law_type`: command, prohibition, statute, ritual, punishment,
  obligation, precedent, judicial_instruction, governmental_principle,
  permission, ideal, qualification.
- `testament`: Old or New.
- `confidence`: high (explicit imperative/statute), medium (norm inferred
  from precedent or strong exhortation), low (ideal, disputed reading, or
  norm inferred from narrative alone).

Also check the classical Jewish/Christian taxonomies where useful:
apodictic vs. casuistic form; moral/civil/ceremonial trichotomy (note:
the USofC's Committee on Scriptural Consistency treats the trichotomy as
official doctrine — see docs/DenominationalNotes.md CSC 1-01 — so a law's
trichotomy slot determines how loudly the regime enforces it).

Rerun `python3 tools/build_index.py` after edits.
