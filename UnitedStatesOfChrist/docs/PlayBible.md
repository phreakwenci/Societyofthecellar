# Play Bible — *United States of Christ*

*The living reference for the stage play. Unlike the rest of `docs/` (which
describes the fixed world), this document is **built to change**: scenes and
characters will be added and revised constantly. It is structured so that
updates are easy and every update is dated and tracked.*

**Status:** v0.2 — seed · **Last updated:** 2026-07-09

---

## 0. How to use and update this document

This file uses **stable IDs** and a **revision log** so it can grow without
losing its history. When you change it:

1. **Add a row to the Revision Log** (§1) with the date, the new version,
   and a one-line summary.
2. **Bump the version** in the header (`v0.1 → v0.2`) and the `Last updated`
   date.
3. **Stamp the entry** you touched: every Character and Scene has an
   `Added:` and `Updated:` date — update the latter.
4. **Never reuse or renumber an ID.** New characters take the next free
   `CH-##`; new scenes take the next free `SCENE-###`; new beats slot into
   the Beat Sheet by year (e.g. `B5.5`). Retired material is marked
   `Status: retired`, not deleted, so the trail survives.
5. **Status tags** on entries: `seed` (sketch), `draft` (written up),
   `stable` (locked), `needs-revision`, `retired`.

The **ID Registry** (§9) is the index of every ID in use — check it before
minting a new one.

*Cross-references:* the world these people live in is defined in
`StateDoctrine.md` (governance), `Constitution.md` (law),
`ConstitutionalHistory.md` (the Brexit-to-drift timeline), `Agencies.md`
(the org chart), and the law records in `data/laws/` (linked by id).

---

## 1. Revision Log

| Date | Version | Change |
|---|---|---|
| 2026-07-09 | v0.1 | Initial seed: logline, themes, 9 characters (CH-01…CH-09), Year 1/5/10 beat sheet, SCENE-001 (the Ordeal) drafted, SCENE-002/003 seeded, doctrine cross-refs, open threads, ID registry. Built from the author's rough play outline. |
| 2026-07-09 | v0.2 | New capability: `/adjudicate-case` skill + `CaseLaw.md` reporter. SCENE-002 bumped seed→draft with a full legal brief (CASE-002) and a comparison hypothetical (CASE-001). Companion addition to `StateDoctrine.md` §10a (household-informant exception, Deut 13:8-9) formalizing why the two-witness rule doesn't save the father. |

---

## 2. Logline & premise

A devout Christian family cheers the referendum that turns the nation into
a Christian theocracy — and then, over ten years, is destroyed one member
at a time by the very laws they voted for. Each is punished by a doctrine
they once believed in. At the end only the father and his youngest son
remain; the father voices a quiet doubt, and the son reports him. The child
is left to be raised wholly by the state — taken in, at the last, by the
priest who deported his mother and sentenced his father.

**The engine (see `StateDoctrine.md`):** a middle-sanctity family that
**voted for all of it** (§0 of StateDoctrine — the Brexit-style Covenant
Referendum) and **could not afford to survive it** (§3, Degrees of
Sanctity). The cruelty is lawful, procedural, and — until Act 2 — invisibly
class-tiered: *they would have been fine with more money.*

---

## 3. Themes & tone

**Themes:** betrayal by belief · authoritarianism wrapped in sanctity ·
state-enforced morality · the internal collapse of a family via external
obedience · the vote as original sin.

**Tone:** warm, nostalgic Americana filtered through brutal bureaucracy.
Surveillance baked into churches, schools, and grocery stores. The horror
is in the forms, the ration lines, the neighbor, the child — and in how
sincerely everyone means it.

**Influences:** *The Handmaid's Tale* · *But I'm a Cheerleader* (tonal
dissonance / satire) · *1984* / *Equilibrium* / *Brazil* · Christian-
nationalist rhetoric + prosperity-gospel grift.

**Structural rule (locked):** the two-tier, buy-your-way-out nature of
justice is **hidden until Act 2** (StateDoctrine §3, §10). Plant a
Chekhov's-exemption early — a wealthy family's identical infraction quietly
waved through — that the family and audience only understand later.

---

## 4. Characters

*Format: ID · Name · one-line · dossier. Stamp `Updated:` when changed.*

### CH-01 · The Father
*Added 2026-07-09 · Updated 2026-07-09 · Status: seed*
The last remaining parent. A sincere believer who voted Leave. Writes an
earnest **letter of concern** and is fined by the church-state; by Year 10
smuggles letters to his exiled wife and son and bakes his late wife's
cookies — the tender act that, under the leaven-purge law
(`exo-012-015-purge-the-leaven`), destroys him. Taken after his own
youngest son reports his quiet doubt. **Arc:** true believer → doubter →
disappeared. **Destroyed by:** StateDoctrine §10 (lawful, tiered due
process) + §5 (the Manna's surveillance) + §3 (never rich enough).

### CH-02 · The Mother / Wife
*Added 2026-07-09 · Updated 2026-07-09 · Status: seed*
A "trad wife." Tries to **intervene** on her husband's behalf; is secretly
recorded and **deported to Liberia for sedition.** Her intervention reads
as sedition precisely because a wife acting outside male headship has no
lawful civic voice (`1 Tim 2:12`; Numbers 30 vow-annulment; StateDoctrine
§8). **Destroyed by:** §8 (headship) + §9 (race — the Liberia choice; see
Open Thread OT-2). **Note:** the loving cookies the father bakes in Year 10
are *hers*.

### CH-03 · The Teenage Son (twin)
*Added 2026-07-09 · Updated 2026-07-09 · Status: seed*
One of the paternal twins. Falls in love **outside approved bounds** — with
an immigrant girl (CH-08) — who flees the USOC to the west-coast "bastion
of sin"; he follows / is separated. **Destroyed by:** §11 (immigration —
Title XI) + §1 (tribal geography: the west as the only mercy). **Status of
his fate:** open (fled / disappeared — see Open Thread OT-3).

### CH-04 · The Teenage Daughter (twin)
*Added 2026-07-09 · Updated 2026-07-09 · Status: draft*
One of the paternal twins. **Protests injustice** → sent to a re-education
camp → **raped and impregnated there** (by the camp/state) → sent home to
bear the child under fetal-personhood law → days after the birth walks into
the sea off the pier, stones in her pockets, with the baby. Her body is
where the regime's reproductive contradictions detonate (see **SCENE-001**).
**Destroyed by:** §7 (Fetal Life Act; `exo-021-022-injury-to-pregnant-woman`
+ `num-005-011-jealousy-ordeal-sotah`) + §8 (the autonomous-woman problem).

### CH-05 · The Youngest Son
*Added 2026-07-09 · Updated 2026-07-09 · Status: seed*
A small child at the start. Early on, is threatened with death by the
father for a disobedience (the Genesis-22 / "get him first before he gets
you" dynamic) — and, though the father relents, the son **distrusts him
forever** and learns what the power of reporting can do. Says something
controversial at Sunday school → re-education. Returns assimilated; by the
end **reports his father** and is taken in by the priest to become an
acolyte — the state's fully-made child, a "big brother" in the making.
**Destroyed / made by:** §6 (school = church) → §5 (the Manna raises him) →
he *becomes* the state.

### CH-06 · The Reverend Father (the Priest)
*Added 2026-07-09 · Updated 2026-07-09 · Status: seed*
The antagonist and the play's throughline of the regime. A Reformed-bloc
cleric (StateDoctrine §4 — the faction that holds the CSC and sentences
people): he **deports the mother**, **sentences the father**, and at the
end **takes the youngest son as an acolyte** ("Now, tell me young man, what
makes a good soldier for Christ?"). The human face of the church-state
merge. **Note:** consider whether he profits (prosperity grift) or is a
true ascetic believer — the choice sets the play's theory of evil
(see OT-4).

### CH-07 · Jeff (the Neighbor)
*Added 2026-07-09 · Updated 2026-07-09 · Status: seed*
The friendly neighbor — dog (Eva), a wife, a baby "due any day." Warm,
active in the congregation, and a **surveillance vector**: the Manna makes
every neighbor a potential witness (§5, and the two-witness rule). His
expecting a child ties him quietly to the reproductive-law theme (a
"lawful" pregnancy beside the daughter's punished one). Nearly catches the
father with the smuggled letters. **Function:** the ordinary, sweet face of
the panopticon.

### CH-08 · The Immigrant Girl
*Added 2026-07-09 · Updated 2026-07-09 · Status: seed*
CH-03's beloved; her family's status is adjudicated under Title XI
(immigration). Flees to the west coast. **Carries the immigration theme**
and the real Christian-immigration debate (StateDoctrine §11). *Name and
background: TBD (OT-3).*

### CH-09 · The Brownshirt Friend
*Added 2026-07-09 · Updated 2026-07-09 · Status: seed*
A friend of one of the sons who joins the youth enforcement corps (the NDS,
`Agencies.md`) — the peer who models assimilation, a possible mirror/foil
for the youngest son's arc into the state. *Role size: TBD.*

---

## 5. The world, in one page (pointers)

The play does not need to restate the world — it lives in these files:

- **How power works / who rules:** `StateDoctrine.md` §4 (the wealth
  triangle: Evangelical cash+media / frozen Catholic assets / Reformed
  doctrinal veto). The Priest (CH-06) is Reformed; prosperity pastors are
  Evangelical.
- **Daily life / class:** StateDoctrine §3 (Degrees of Sanctity / moral
  credit), §5 (the Manna platform: broadcast + rations + surveillance).
- **The bodies at stake:** §7 (reproductive doctrine), §8 (women), §6
  (education), §2 (citizenship / circumcision).
- **The law itself:** `data/laws/INDEX.md` and `data/catalog/CATALOG.md`.

---

## 6. Beat Sheet (Year 1 / 5 / 10)

*Each beat has a stable ID. Add new beats as `B<year>.<n>`; do not renumber.
Each beat links the law/agency that drives it.*

### Year 1 — the Leave becomes law
- **B1.1** — The referendum's Leave takes legal effect; the Manna becomes
  the only broadcast, cycling the laws ("Daily Obedience, Daily Manna");
  news must be "Christ-Aligned." → StateDoctrine §5.
- **B1.2** — Enforcement begins: the **Bread Laws** and family restrictions.
  → `exo-012-015-purge-the-leaven`, `exo-016-019-daily-bread-no-hoarding`
  (BDB).
- **B1.3** — Moral Authority / church-state merge; **moral credits and
  merit badges** introduced ("no badges = worthless"); re-education begins.
  → StateDoctrine §3. *Plant the Chekhov's-exemption here (§3 rule).*
- **B1.4** — The twins begin forbidden relationships; CH-03 falls for CH-08,
  who flees west. → Title XI, StateDoctrine §11, §1.

### Year 5 — the family cracks
- **B5.1** — **The daughter (CH-04):** raped and impregnated at the camp,
  sent home to bear the child, then the pier. → **SCENE-001**;
  `num-005-011-jealousy-ordeal-sotah`, `exo-021-022-injury-to-pregnant-woman`.
- **B5.2** — The youngest son (CH-05) says something controversial at Sunday
  school → re-education. → StateDoctrine §6.
- **B5.3** — The father (CH-01) writes his **letter of concern** → fined by
  the church-state.
- **B5.4** — The mother (CH-02) tries to intervene → recorded → **deported
  to Liberia** for sedition. → StateDoctrine §8, §9.

### Year 10 — the last two
- **B10.1** — The youngest son returns, assimilated; a gulf opens between
  father and son; the boy is becoming "big brother." → StateDoctrine §5, §6.
- **B10.2** — The father smuggles letters to his exiled wife and son;
  nearly caught by the neighbor (CH-07). → §5.
- **B10.3** — **Climax:** the father bakes his late wife's cookies during
  the unleavened holy week; the youngest son reports him; authorities find
  the cookies *and* the letters. → **SCENE-002**;
  `exo-012-015-purge-the-leaven`.
- **B10.4** — The father is taken; the child is left in state custody; the
  Priest (CH-06) takes him as an acolyte ("what makes a good soldier for
  Christ?"). → the ending.

---

## 7. Scene Briefs

*Detailed working briefs. Add as `SCENE-###`. Each names the statutes the
characters can cite, so the legal machinery is exact.*

### SCENE-001 · The Ordeal (the daughter)
*Added 2026-07-09 · Updated 2026-07-09 · Status: draft · Beats: B5.1*

**Situation.** CH-04, raped and impregnated inside a re-education camp — by
the camp, i.e. by the state — is sent home under the Fetal Life Act to bear
"the gift of life." When violence (a beating at the camp, or a "purity"
procedure) ends the pregnancy, the regime must adjudicate its own
contradiction on her body.

**The two statutes that detonate together:**
- `exo-021-022-injury-to-pregnant-woman` (Ex 21:22-25). The regime's
  fetal-personhood law reads "if harm follow, life for life." So the death
  of the fetus demands *a life* — **but the killer is the state.** The plain
  Hebrew, which prices the fetus as a *fine* (property, not person), sits in
  the same inerrant text, unspeakable in court.
- `num-005-011-jealousy-ordeal-sotah` (Num 5). The ordeal puts **her** on
  trial: was she unchaste? It needs no witness (the inversion of the
  two-witness rule). The rape becomes her adultery hearing; the state that
  impregnated her by force now examines her for guilt, and the ritual's own
  "curse" is a reproductive ruin — the state performing what Exodus calls
  murder.

**The collision.** The same covenant (1) forced her to carry it, (2) cannot
decide whether its death is a murder (someone must die — but that indicts
the state) or a fine (a receipt), and (3) tries *her* for it. Every road the
law offers ends in her. The stones in her pockets and the walk off the pier
(the Woolf echo) are the only verdict the state cannot appeal.

**Staging logic.** Keep the bureaucracy warm and quiet — a screening room,
a form, a kind administrator (a possible FPA functionary who has stopped
believing). The horror is procedural, not gothic. Her few lines should be
plain. The audience should feel the machine close, not hear a speech about
it.

**Target.** This is the play's argument in one body: the covenant's
contradictions, written on a girl until she chooses the water herself.
Handle with gravity; nothing gratuitous — the violence is *legal*, and that
is the point.

*Open: exact mechanism that ends the pregnancy (camp violence vs. an
ordered "ordeal"); how much is shown vs. reported. See OT-5.*

### SCENE-002 · The Cookies (climax)
*Added 2026-07-09 · Updated 2026-07-09 · Status: draft · Beats: B10.3*
The father bakes his late wife's cookies during the unleavened holy week
(`exo-012-015-purge-the-leaven`) — the tenderest act in the play, a man
grieving through a recipe — and the youngest son reports him. Authorities
arrive, find the cookies (a "cutting off" offense) *and* the smuggled
letters. The smallest, most domestic law destroys the deepest love.

**Legal skeleton drafted:** see `CaseLaw.md` **CASE-002**, which works the
full charges/defenses/denominational-split/predicted-ruling for this exact
scene — including why the two-witness rule doesn't save him (the son is a
sufficient sole witness under the household-informant exception,
`StateDoctrine.md` §10a) and why the smuggled letters, not the cookies,
are what actually seals the sentence. Compare **CASE-001** (a hypothetical
"dying wife" necessity variant of the same statute) to see that even the
*strongest* available defense likely still loses at this family's tier —
this scene is the weaker-defense version, confirming the ending is legally
overdetermined, not a plot hole.

### SCENE-003 · Referendum Night (possible opening)
*Added 2026-07-09 · Updated 2026-07-09 · Status: seed*
The family gathered, the Leave result called, "Take Back the Nation for
Christ" on the screen — joy, relief, belief. The original sin, played as a
celebration (StateDoctrine §0; `ConstitutionalHistory.md`, "Before Year 0").
Everything after is the bill for this night. *Consider as the cold open, so
Act 2's revelations land as the cost of this joy. To draft.*

---

## 8. Doctrine used by the play (cross-reference)

The specific statutes the play leans on, all now in the catalog with full
records and USOC-implementation notes:

- **The Bread Laws** (BDB — `Agencies.md`):
  `exo-012-015-purge-the-leaven` (holy-week purge; the cookies),
  `exo-016-019-daily-bread-no-hoarding` (same-day rations; dependence),
  `lev-024-005-bread-of-the-presence` (clergy-only sacred bread).
- **The Biological Sanctity Act / Fetal Life Act** (FPA):
  `gen-038-009-seed-not-spilled-onan` (IVF-destroyed / IUI-husband-only),
  `exo-021-022-injury-to-pregnant-woman` (fetal personhood),
  `num-005-011-jealousy-ordeal-sotah` (the ordeal).
- **Citizenship / the covenant sign** (BRC):
  `gen-017-010-circumcision-covenant-sign`.
- **Governance the play assumes:** `StateDoctrine.md` in full.
- **Legal reasoning over any scene:** `CaseLaw.md` — CASE-001 (necessity
  hypothetical), CASE-002 (SCENE-002's actual legal brief). Run
  `/adjudicate-case` on any beat to generate charges, defenses,
  denominational split, and a predicted ruling.

*When the play needs a new law, run `/extract-biblical-law` to add a deep
record, then link it here. When a scene needs its legal mechanics worked
out, run `/adjudicate-case` and log the result in `CaseLaw.md`.*

---

## 9. ID Registry (check before minting new IDs)

- **Characters:** CH-01 Father · CH-02 Mother · CH-03 Teenage Son ·
  CH-04 Teenage Daughter · CH-05 Youngest Son · CH-06 The Priest ·
  CH-07 Jeff (neighbor) · CH-08 Immigrant Girl · CH-09 Brownshirt Friend.
  *Next free: CH-10.*
- **Scenes:** SCENE-001 The Ordeal · SCENE-002 The Cookies ·
  SCENE-003 Referendum Night. *Next free: SCENE-004.*
- **Beats:** B1.1–B1.4 · B5.1–B5.4 · B10.1–B10.4.

---

## 10. Open Threads / TODO

*Add as `OT-#`; resolve by editing and noting the resolution + date.*

- **OT-1** — Title of the state broadcast / the platform. Working name:
  **the Manna**. Confirm.
- **OT-2** — The **Liberia** deportation: intentional racial statement, or
  reconsider? (StateDoctrine §9 flags this as heavy-loaded — an audience
  will read it hard.) Author to decide knowingly.
- **OT-3** — CH-08 (immigrant girl): name, country of origin, faith; and
  CH-03's final fate (fled / caught / disappeared).
- **OT-4** — CH-06 (the Priest): prosperity-grifter or true-believer
  ascetic? Sets the play's theory of evil.
- **OT-5** — SCENE-001: exact mechanism ending the pregnancy; how much is
  staged vs. reported.
- **OT-6** — The immigration article ("The Bible is not a policy manual"):
  wire real quotes into Title XI and a dissident character's lines (paste
  or pull).
- **OT-7** — Beat sheet → full **scene-by-scene outline**; then a tone map
  and propaganda-poster visuals (author's original "Next Steps").
