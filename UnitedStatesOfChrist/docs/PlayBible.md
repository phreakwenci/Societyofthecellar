# Play Bible — *United States of Christ*

*The living reference for the stage play. Unlike the rest of `docs/` (which
describes the fixed world), this document is **built to change**: scenes and
characters will be added and revised constantly. It is structured so that
updates are easy and every update is dated and tracked.*

**Status:** v0.3 — draft · **Last updated:** 2026-07-09

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
| 2026-07-09 | v0.3 | **Named cast + full timeline revision.** Father→**Mark** (a Law Enforcement Officer), Mother→**Constance** (teacher), Teenage Son→**Chris** (ROTC/national pilgrimage), Teenage Daughter→**Laura** (debate captain/valedictorian), Youngest Son→**Able**. New characters CH-10 (the girl Laura kissed) and CH-11 (the classmate who recorded/reported them). Beat sheet rewritten as a causal Year-5 cascade. Three new grounded doctrines added to `StateDoctrine.md` (§2a Returning Citizens, §10b Juvenile Sanctity Emergency Custody, §10c the Sanctity Environment Finding) and three new deep law records (Ezra 9-10, Haggai 2:11-13, Romans 1:26). Four new case memos (`CaseLaw.md` CASE-003…006) plus an update to CASE-002. SCENE-001 corrected to match the authoritative character dossier (Laura dies at 7 months **pregnant**, not after a live birth; her note quotes Judges 19). New SCENE-004 (Chris's tribunal). Resolved: "letter of concern" → **Remonstrance**; recommended Able's Act-3 age → **16**, with 11 kept as a flagged alternate. |

---

## 2. Logline & premise

A devout Christian family cheers the referendum that turns the nation into
a Christian theocracy — and then, over ten years, is destroyed one member
at a time by the very laws they voted for. Each is punished by a doctrine
they once believed in. At the end only the father, Mark, and his youngest
son, Able, remain; Mark voices a quiet doubt, and Able reports him. The
child is left to be raised wholly by the state — taken in, at the last, by
the priest who deported his mother and sentenced his father.

**The engine (see `StateDoctrine.md`):** a middle-sanctity family that
**voted for all of it** (§0 of StateDoctrine — the Brexit-style Covenant
Referendum) and **could not afford to survive it** (§3, Degrees of
Sanctity). The cruelty is lawful, procedural, and — until Act 2 — invisibly
class-tiered: *they would have been fine with more money.* Mark's badge
bought the family more time than they ever knew they were living on.

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

### CH-01 · Mark (the Father)
*Added 2026-07-09 · Updated 2026-07-09 · Status: draft*
A Law Enforcement Officer — a believer who enforces the very Code that
will end him, which the play should let the audience feel from his first
scene. His badge is not incidental: professional courtesy among fellow
officers bought the family real, if invisible, protection for years (see
`CaseLaw.md` CASE-002). In the wake of Laura's death and Able's removal
(Year 5), grieving and furious, he writes a formal **Remonstrance** — the
Puritan-era term for a written protest to authority, chosen over a modern
phrase because Mark, a professional, knows how to file a thing properly —
and is fined by the church-state for it. By Year 10 he smuggles letters
past the border to Constance and Chris, and bakes Constance's old
cookies during Holy Week while playing music the Sacred Speech Commission
has listed as "worldly" contraband (1 John 2:15) — the combination that
destroys him when Able reports him. **Arc:** enforcer → griever → doubter
→ disappeared. **Destroyed by:** StateDoctrine §10a (his own son is a
sufficient sole witness) + §5 (the Manna logs the letters and the music)
+ §3 (a badge is a tier, but not a permanent one).

### CH-02 · Constance (the Mother)
*Added 2026-07-09 · Updated 2026-07-09 · Status: draft*
A "trad wife" turned public schoolteacher — she wants the home catechism
she gave her own children carried further, to every classroom she can
reach. That ambition alone puts her under quiet factional watch before
anything else happens to her family (StateDoctrine §8, the public-teaching
trap: Evangelicals would showcase her, the Reformed/CSC reads any woman's
doctrinal reach as a live 1 Tim 2:12 exposure). After Mark is fined, she
**intervenes** on his behalf; the intervention is secretly recorded and she
is **deported to Liberia for sedition** — which reads as sedition not
because of what she said but because a wife acting outside headship has no
lawful civic voice at all (Numbers 30; StateDoctrine §8). She is deported
the same day Chris's letter about his own child arrives. **Destroyed by:**
§8 (already watched; the intervention is read as confirmation, not a first
offense) + §9 (race — the Liberia choice; Open Thread OT-2). **Note:** the
Year-10 cookies Mark bakes are hers.

### CH-03 · Chris (the Teenage Son, twin)
*Added 2026-07-09 · Updated 2026-07-09 · Status: draft*
ROTC, and about to leave on a national "pilgrimage" — a state-sanctioned
missionary service circuit spreading the word across the country (ties to
the Ministry of Covenant Defense and the National Devotion Service). He
falls for an immigrant girl (CH-08) and, at the end of Act 1, leaves for
California, the "bastion of sin," and cannot come back. **Act 2:** the
family petitions for his return at a courthouse tribunal; because he has
resided among "the heathen nations," he is held to be **contaminated by
proxy** (StateDoctrine §2a — grounded in Ezra 9-10 and Haggai 2:11-13, not
any specific act) and is offered only a purification-and-renunciation rite
or indefinite limbo holding. He **chooses neither** — he goes back to her.
See **SCENE-004** and `CaseLaw.md` CASE-003. He sends postcards and updates
throughout, especially after Laura dies. **Destroyed/defined by:** §2a
(contact, not conduct, is the charge) + §11 (immigration — Title XI) + §1
(tribal geography: the west as the only mercy, and the one he chooses over
reinstatement).

### CH-04 · Laura (the Teenage Daughter, twin)
*Added 2026-07-09 · Updated 2026-07-09 · Status: draft*
Debate captain, cheerleader, valedictorian — the "ideal" public-school
daughter of the new order, which is exactly why her fall is legible to
everyone watching. Caught kissing a classmate (CH-10) by a male classmate
(CH-11), who records and reports them; both girls are removed to
re-education the same day under the **Juvenile Sanctity Emergency
Custody** doctrine (StateDoctrine §10b) — parents are *notified*, not
consulted, resolving what looks like a contradiction in the record but
isn't (see §10b). Months in the camp; she is raped and impregnated there,
and characterizes the pregnancy in her own words as **her sentence** —
not a gift of life, a punishment. Sent home to carry to term. **At seven
months pregnant** — not after a live birth — she fills her pockets with
stones and walks off the family pier. Her note quotes **Judges 19** (the
Levite's concubine — gang-raped, killed, dismembered and sent in twelve
pieces to provoke the tribes to war) and is written, deliberately, like a
valedictorian's closing argument against the Christian nation. Able reads
or overhears it. See **SCENE-001** (updated) and `CaseLaw.md` CASE-004
(the arrest) and CASE-005 (the legal/theological autopsy of her death).
**Destroyed by:** §10b (removed same day, no hearing) + §7 (Fetal Life
Act; `exo-021-022-injury-to-pregnant-woman` + `num-005-011-jealousy-
ordeal-sotah`) + the new female-conduct extension (`rom-001-026-vile-
affections-women`) + §8 (the autonomous-woman problem).

### CH-05 · Able (the Youngest Son)
*Added 2026-07-09 · Updated 2026-07-09 · Status: draft*
Curious, inquisitive, sentimental — repeats what his family says, without
yet understanding what repeating can do. Early on, is threatened with
death by Mark over a disobedience (the Genesis-22 / "get him first before
he gets you" dynamic); Mark relents, but Able **distrusts him from then
on** and has already glimpsed what a report can do. After Laura's death, he
repeats **the truth of her suicide note** at school; his **teacher** — an
NDS mandatory reporter, not a peer this time — reports him. Mark and
Constance are administratively **scolded for "reproving"** (defending,
mourning) what happened to their daughter — a **Sanctity Environment
Finding** (StateDoctrine §10c), civil, not criminal, and it is this
finding, not any conviction, that takes Able from them, years before Mark
is ever arrested. **Act 3, open fork (see OT-9):** Able returns at **16**
(recommended — old enough to serve as a citizen, and has chosen to train
as a lawyer for the cause, which folds beautifully into the play's whole
legal-reasoning conceit; he could plausibly inherit Mark's house) **or at
11** (the more purely devastating option — betrayal by someone so young,
for loving them). Either way, he reports Mark for the prohibited music and
the unleavened cookies; Mark is arrested; Able is left alone in state
custody, taken in by the Priest (CH-06) as an acolyte. **Destroyed/made
by:** §10c (taken years before any parent is charged with a crime) → §6
(his own teacher is the reporting mechanism) → §5 (the Manna raises him) →
he *becomes* the state.

### CH-06 · The Reverend Father (the Priest)
*Added 2026-07-09 · Updated 2026-07-09 · Status: seed*
The antagonist and the play's throughline of the regime. A Reformed-bloc
cleric (StateDoctrine §4 — the faction that holds the CSC and sentences
people): he **deports Constance**, **sentences Mark**, and at the end
**takes Able as an acolyte** ("Now, tell me young man, what makes a good
soldier for Christ?"). The human face of the church-state merge. **Note:**
consider whether he profits (prosperity grift) or is a true ascetic
believer — the choice sets the play's theory of evil (see OT-4).

### CH-07 · Jeff (the Neighbor)
*Added 2026-07-09 · Updated 2026-07-09 · Status: draft*
The friendly neighbor — dog (Eva), a wife, a baby "due any day." Warm,
active in the congregation — and, established explicitly in **Year 1**
(not left as a late reveal), a man who **installs surveillance cameras**
aimed at his neighbors' yards and windows, in the sincere belief he is
helping keep the block pure (the Manna makes every neighbor a potential
witness, §5). This early establishment is deliberate — it means his
near-catch of Mark's smuggled letters in Year 10 lands as the payoff of a
habit the audience has watched for a decade, not a coincidence. His
expecting a child ties him quietly to the reproductive-law theme (a
"lawful" pregnancy beside Laura's punished one). **Function:** the
ordinary, sweet face of the panopticon.

### CH-08 · The Immigrant Girl
*Added 2026-07-09 · Updated 2026-07-09 · Status: seed*
Chris's beloved; her family's status is adjudicated under Title XI
(immigration). It is for her sake Chris chooses exile over reinstatement
in **SCENE-004**. **Carries the immigration theme** and the real Christian-
immigration debate (StateDoctrine §11). *Name and background: TBD (OT-3,
partially resolved — Chris's own fate is now decided; her name is not).*

### CH-09 · The Brownshirt Friend
*Added 2026-07-09 · Updated 2026-07-09 · Status: seed*
A friend who joins the youth enforcement corps (the NDS, `Agencies.md`) —
models assimilation, a possible mirror/foil for Able's arc into the state.
*Consider merging with CH-11 (below) — see OT-10.*

### CH-10 · The Girl (Laura's classmate)
*Added 2026-07-09 · Updated 2026-07-09 · Status: seed*
The classmate Laura is caught kissing. Removed to re-education alongside
her the same day (StateDoctrine §10b). *Name, background, and fate after
the camp: TBD (OT-11).* Consider whether her fate is shown at all, or
remains — like the whereabouts of many removed minors in this world —
deliberately unresolved, which may be the more honest choice.

### CH-11 · The Classmate (who recorded and reported)
*Added 2026-07-09 · Updated 2026-07-09 · Status: seed*
The male classmate who records Laura and CH-10 kissing and reports them —
the recording itself functions as documentary evidence strong enough to
satisfy the two-witness concern without anyone needing to invoke §10a (see
`CaseLaw.md` CASE-004). *Name: TBD. Consider merging with CH-09 the
Brownshirt Friend (OT-10) — a single recurring peer-informant character
may land harder than two thin ones.*

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
  (education), §2/§2a (citizenship / circumcision / returning citizens).
- **Custody and process without a criminal conviction:** §10a (the
  household-informant exception — Mark), §10b (juvenile emergency custody
  — Laura), §10c (the Sanctity Environment Finding — Able).
- **The law itself:** `data/laws/INDEX.md` and `data/catalog/CATALOG.md`.

---

## 6. Beat Sheet (Year 1 / 5 / 10)

*Each beat has a stable ID. Add new beats as `B<year>.<n>`; do not renumber.
Each beat links the law/agency/doctrine that drives it. The Year 5 block is
written as a **causal cascade** — each beat follows from the one before,
not a disconnected list — with Chris's tribunal (B5.7) available to
crosscut/interleave with the household's collapse rather than play strictly
in sequence.*

### Year 1 — the Leave becomes law
- **B1.1** — The referendum's Leave takes legal effect; the Manna becomes
  the only broadcast, cycling the laws ("Daily Obedience, Daily Manna");
  news must be "Christ-Aligned." → StateDoctrine §5.
- **B1.2** — Enforcement begins: the **Bread Laws** and family restrictions.
  → `exo-012-015-purge-the-leaven`, `exo-016-019-daily-bread-no-hoarding`
  (BDB).
- **B1.3** — Moral Authority / church-state merge; **moral credits and
  merit badges** introduced ("no badges = worthless"); re-education begins.
  Jeff (CH-07) installs his first surveillance cameras this year, sincerely,
  as a good neighbor. → StateDoctrine §3, §5. *Plant the Chekhov's-exemption
  here (§3 rule).*
- **B1.4** — Chris (CH-03), ROTC, is about to leave on his national
  pilgrimage; he and the immigrant girl (CH-08) have already fallen for
  each other outside approved bounds. He leaves for California at the
  act's end and cannot return. → StateDoctrine §11, §1.

### Year 5 — the cascade
- **B5.1** — Laura (CH-04) is caught kissing CH-10; CH-11 records and
  reports them. Both girls are removed to re-education the same day.
  Parents are **notified**, not consulted. → StateDoctrine §10b;
  `rom-001-026-vile-affections-women`. See `CaseLaw.md` CASE-004.
- **B5.2** — In the camp, Laura is raped and impregnated; she calls it her
  **sentence**. Months pass. She is sent home to carry to term. → §7;
  `exo-021-022-injury-to-pregnant-woman`, `num-005-011-jealousy-ordeal-
  sotah`.
- **B5.3** — **At seven months pregnant**, Laura fills her pockets with
  stones and walks off the family pier. Her note quotes Judges 19 and reads
  like a valedictorian's closing argument against the nation. → **SCENE-001**
  (updated); `CaseLaw.md` CASE-005.
- **B5.4** — Able (CH-05) reads or overhears the note and repeats its truth
  at school; his teacher (an NDS mandatory reporter) reports him. → §6.
- **B5.5** — Mark and Constance are administratively scolded for
  "reproving" — mourning, defending — what happened to Laura. A **Sanctity
  Environment Finding** is entered against the household. Able is taken.
  No one has been criminally charged with anything yet. → §10c;
  `CaseLaw.md` CASE-006.
- **B5.6** — Grieving and furious, Mark writes a formal **Remonstrance** —
  fined by the church-state. → `CaseLaw.md` CASE-002 (background).
- **B5.7** *(may be staged interleaved with the above, not strictly after)*
  — Chris and the family petition for his return at a courthouse tribunal;
  he is held **contaminated by proxy** and offered purification-and-
  renunciation or indefinite limbo. He chooses to return to California, to
  the girl, instead. He begins sending postcards and updates, especially
  after learning of Laura's death. → **SCENE-004**; StateDoctrine §2a;
  `CaseLaw.md` CASE-003.
- **B5.8** — Constance intervenes on Mark's behalf; the intervention is
  recorded; she is **deported to Liberia** for sedition. The same day, a
  letter from Chris arrives announcing his own child. Mark reads it alone
  in the living room. → §8, §9.

### Year 10 — the last two
- **B10.1** — Able returns, increasingly assimilated; a gulf opens between
  him and Mark; he is becoming "big brother." (Open fork on his age — see
  OT-9.) → StateDoctrine §5, §6.
- **B10.2** — Mark smuggles letters to Constance and Chris, outside the
  union; nearly caught by Jeff (CH-07) — the payoff of B1.3's cameras. → §5.
- **B10.3** — **Climax:** grieving Constance's absence, Mark bakes her old
  cookies during the unleavened holy week while playing music the SSC has
  listed as worldly contraband; Able reports him. Authorities find the
  cookies, the music, *and* the letters. → **SCENE-002** (updated);
  `exo-012-015-purge-the-leaven`; `CaseLaw.md` CASE-002 (updated).
- **B10.4** — Mark is taken. Able is left in state custody. The Priest
  (CH-06) takes him as an acolyte ("what makes a good soldier for
  Christ?"). If Able is 16: he inherits Mark's house. If 11: he is escorted
  out by the Priest himself. → the ending.

---

## 7. Scene Briefs

*Detailed working briefs. Add as `SCENE-###`. Each names the statutes the
characters can cite, so the legal machinery is exact.*

### SCENE-001 · The Ordeal (Laura)
*Added 2026-07-09 · Updated 2026-07-09 · Status: draft · Beats: B5.1–B5.3*

**Situation, corrected to the authoritative character dossier.** Laura is
not removed for "protesting injustice" — she is removed for being caught
kissing a classmate (CH-10), recorded and reported by CH-11 (B5.1). Raped
and impregnated in the camp (B5.2), she is sent home to carry to term. She
does **not give birth**: at seven months pregnant, she fills her pockets
with stones and walks off the family pier (B5.3). Her note quotes
**Judges 19** — the Levite's concubine, gang-raped through the night at
Gibeah, found dead by her master, who cuts her body into twelve pieces and
sends them to the tribes to provoke a war of outrage. Laura, debate
captain and valedictorian, is not quoting it as decoration: she is
positioning herself as both the concubine (a body used and then made into
a political instrument) *and* the one who dismembers and sends the
message — her own note, addressed to the nation, is her twelve pieces. Her
prose should read like a closing argument, not a confession.

**The two statutes that detonate together:**
- `exo-021-022-injury-to-pregnant-woman` (Ex 21:22-25). The regime's
  fetal-personhood law reads "if harm follow, life for life." Laura's own
  act, at seven months, is — under the state's own maximalist doctrine —
  simultaneously her suicide *and*, by the state's own theology, the
  ending of a legal person's life. The law that was built to convict
  others of harming a fetus has no framework for a mother's final refusal
  that takes both at once; see `CaseLaw.md` CASE-005 for the full
  reasoning.
- `num-005-011-jealousy-ordeal-sotah` (Num 5) and the new
  `rom-001-026-vile-affections-women`. The state's charge against her was
  never really about the pregnancy — it was about the kiss. The pregnancy
  is the "sentence" her own note names it as: what the camp did to her in
  place of, or alongside, the female-conduct charge.

**The collision.** The same covenant (1) removed her for a kiss under a
statute (Romans 1:26) whose own next verse forbids using it to judge, (2)
let its custody produce the pregnancy it then calls her sentence, and
(3) has no legal category for what she does at the end — not martyrdom,
not merely suicide, but an act that indicts the fetal-personhood doctrine
by fulfilling and refusing it in the same motion.

**Staging logic.** Keep the bureaucracy warm and quiet where it appears —
the intake at the camp, a kind functionary — but let Laura's own voice
(the note) carry the weight. She is the character built to argue, and her
last words should sound like the best closing argument of her life,
because they are.

**Target.** This is the play's argument in one body: the covenant's
contradictions, written on a girl until she chooses the water herself, and
articulated, at the end, by the sharpest mind in the family.

*Resolved (2026-07-09): the mechanism is suicide at seven months pregnant,
not violence ending a completed pregnancy or death after a live birth —
this supersedes the earlier draft. See OT-5.*

### SCENE-002 · The Cookies (climax)
*Added 2026-07-09 · Updated 2026-07-09 · Status: draft · Beats: B10.3*
Mark bakes Constance's old cookies during the unleavened holy week
(`exo-012-015-purge-the-leaven`) while playing music the SSC has listed as
worldly contraband — the tenderest act in the play, a man grieving through
a recipe and a song — and Able reports him. Authorities arrive, find the
cookies, the music, *and* the smuggled letters. The smallest, most
domestic laws destroy the deepest love.

**Legal skeleton drafted:** see `CaseLaw.md` **CASE-002** (updated with
real names and the music charge), which works the full charges/defenses/
denominational-split/predicted-ruling for this exact scene — including why
the two-witness rule doesn't save him (Able is a sufficient sole witness
under the household-informant exception, `StateDoctrine.md` §10a), why
Mark's LEO status bought him years of quiet professional-courtesy
protection that finally runs out, and why the smuggled letters, not the
cookies, are what actually seal the sentence. Compare **CASE-001** (a
hypothetical "dying wife" necessity variant of the same leaven statute) to
see that even the *strongest* available defense likely still loses at this
family's tier — this scene is the weaker-defense version, confirming the
ending is legally overdetermined, not a plot hole.

### SCENE-003 · Referendum Night (possible opening)
*Added 2026-07-09 · Updated 2026-07-09 · Status: seed*
The family gathered, the Leave result called, "Take Back the Nation for
Christ" on the screen — joy, relief, belief. The original sin, played as a
celebration (StateDoctrine §0; `ConstitutionalHistory.md`, "Before Year 0").
Everything after is the bill for this night. *Consider as the cold open, so
Act 2's revelations land as the cost of this joy. To draft.*

### SCENE-004 · The Tribunal (Chris)
*Added 2026-07-09 · Updated 2026-07-09 · Status: draft · Beats: B5.7*

**Situation.** The family petitions a Covenant Court tribunal for Chris's
return. He has broken no specific statute — he has only resided among
"the heathen nations" (California), in a relationship with an immigrant
woman. Under the **Returning Citizen** doctrine (StateDoctrine §2a,
grounded in Ezra 9-10 and Haggai 2:11-13), this alone is treated as
contamination by contact. The tribunal cannot accuse him of any act; it
can only rule on his *status*. He is offered a purification rite paired
with formal renunciation of the relationship, or indefinite residence in
a Returning Citizen holding zone. He chooses neither, and returns to
California and to her.

**Staging logic.** Structure the scene as pure procedure — the tribunal
reads like a licensing hearing, not a trial, because that is exactly what
makes it horrifying: there is no crime to argue against, only a status to
contest, and status cannot be defended, only renounced or not. Consider
staging Chris's choice as a silence rather than a speech — he simply does
not take either offered door, and walks out the one that was never on the
table. See `CaseLaw.md` **CASE-003** for the full doctrinal reasoning,
including the Ruth/Ezra contradiction defense counsel could raise (and
which the tribunal is not required to consider).

**Target.** The clearest illustration in the whole play of contamination-
by-proxy as a legal theory: no charge, no defense possible in the ordinary
sense, only a door chosen or declined.

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
- **Female same-sex conduct** (FPA): `rom-001-026-vile-affections-women`
  (the textual extension of the male-only Levitical statute).
- **Citizenship / the covenant sign** (BRC):
  `gen-017-010-circumcision-covenant-sign`.
- **Returning citizens / contamination by proxy** (DOR):
  `ezr-009-001-holy-seed-mingled`, `hag-002-011-contagious-uncleanness`.
- **Governance the play assumes:** `StateDoctrine.md` in full, especially
  §2a, §8, §10a, §10b, §10c (new this revision).
- **Legal reasoning over any scene:** `CaseLaw.md` — CASE-001 (necessity
  hypothetical), CASE-002 (Mark's climax, updated), CASE-003 (Chris's
  tribunal), CASE-004 (Laura's arrest), CASE-005 (Laura's death), CASE-006
  (Able's report and the Sanctity Environment Finding). Run
  `/adjudicate-case` on any beat to generate charges, defenses,
  denominational split, and a predicted ruling.

*When the play needs a new law, run `/extract-biblical-law` to add a deep
record, then link it here. When a scene needs its legal mechanics worked
out, run `/adjudicate-case` and log the result in `CaseLaw.md`.*

---

## 9. ID Registry (check before minting new IDs)

- **Characters:** CH-01 Mark (Father) · CH-02 Constance (Mother) ·
  CH-03 Chris (Teenage Son) · CH-04 Laura (Teenage Daughter) · CH-05 Able
  (Youngest Son) · CH-06 The Priest · CH-07 Jeff (neighbor) · CH-08
  Immigrant Girl · CH-09 Brownshirt Friend · CH-10 The Girl (Laura's
  classmate) · CH-11 The Classmate (recorder/reporter). *Next free: CH-12.*
- **Scenes:** SCENE-001 The Ordeal (Laura) · SCENE-002 The Cookies ·
  SCENE-003 Referendum Night · SCENE-004 The Tribunal (Chris).
  *Next free: SCENE-005.*
- **Beats:** B1.1–B1.4 · B5.1–B5.8 · B10.1–B10.4.

---

## 10. Open Threads / TODO

*Add as `OT-#`; resolve by editing and noting the resolution + date.*

- **OT-1** — Title of the state broadcast / the platform. Working name:
  **the Manna**. Confirm.
- **OT-2** — The **Liberia** deportation: intentional racial statement, or
  reconsider? (StateDoctrine §9 flags this as heavy-loaded — an audience
  will read it hard.) Author to decide knowingly.
- **OT-3** — *Partially resolved 2026-07-09:* Chris's fate is now decided
  — he chooses California and the girl over reinstatement (SCENE-004).
  Still open: CH-08's name, country of origin, faith.
- **OT-4** — CH-06 (the Priest): prosperity-grifter or true-believer
  ascetic? Sets the play's theory of evil.
- **OT-5** — *Resolved 2026-07-09:* the mechanism is suicide at seven
  months pregnant (per the authoritative character dossier), not violence
  ending a completed pregnancy or death after a live birth. SCENE-001
  updated accordingly.
- **OT-6** — The immigration article ("The Bible is not a policy manual"):
  wire real quotes into Title XI and a dissident character's lines (paste
  or pull).
- **OT-7** — Beat sheet → full **scene-by-scene outline**; then a tone map
  and propaganda-poster visuals (author's original "Next Steps").
- **OT-8** — *Resolved 2026-07-09:* "letter of concern" → **Remonstrance**
  (the historical Puritan/English term for a formal written protest to
  authority — fits Mark's LEO precision and the Massachusetts Bay layer of
  `ConstitutionalModel.md`). Alternate on file if a softer register is
  wanted: **"Supplication"** (Phil 4:6, Acts 25:24).
- **OT-9** — Able's age at his Act 3 return: **11 or 16?** Recommended: 16
  (old enough to be a citizen and to have chosen to train as a lawyer for
  the cause — dovetails with the play's whole legal-reasoning conceit, and
  he could plausibly inherit Mark's house). Kept open: 11 is the more
  purely devastating option — betrayal by someone that young, for loving
  them. Author to decide; both branches are drafted in the Beat Sheet and
  SCENE notes above.
- **OT-10** — Should CH-11 (the classmate who reports Laura) be merged
  with CH-09 (the Brownshirt Friend) into a single recurring peer-
  informant character? May land harder as one figure than two thin ones.
- **OT-11** — Names needed: CH-10 (the girl Laura kissed) and CH-11 (the
  reporting classmate), and (carried from OT-3) CH-08.
