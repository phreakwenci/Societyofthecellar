#!/usr/bin/env python3
"""Convert the Skeptic's Annotated Bible EPUB into the project's working corpus.

Produces three tiers of output, split by copyright status:

  data/books/<nn>-<book>.md        KJV verse text (public domain)      -> committed
  data/sab/<nn>-<book>.json        Annotation index: per-verse SAB
                                   category flags + contradiction
                                   cross-references (factual metadata) -> committed
  data/sab/contradictions.json     Contradiction index: id, title,
                                   stances, citations                  -> committed
  data/sab_full/<nn>-<book>.md     Full SAB commentary prose
                                   (copyright Steve Wells)             -> gitignored

Usage:
    python3 tools/convert_epub.py /path/to/TheSkepticchive.epub

The EPUB itself is never committed. Run this once per session against a
locally supplied copy of the book.
"""

import html
import json
import re
import sys
import tempfile
import zipfile
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent

# Inline annotation icons -> SAB categories.
# Mapping was derived by correlating icon usage with the category legend in
# "About the Categories" and spot-checking flagship verses (Gen 1:3,
# Lev 18:22, Lev 18:23, Ex 20:3, Ex 20:5, Mt 1:23). 00016/00019 are the
# best-effort residue of that process: 00016 fits "Science and History" by
# count and co-occurrence, leaving 00019 as "Interpretation" by elimination.
ICON_CATEGORIES = {
    "00018": "Absurdity",
    "00022": "Injustice",
    "00025": "Cruelty and Violence",
    "00027": "Intolerance",
    "00028": "Good Stuff",
    "00016": "Science and History",  # best-effort
    "00024": "Family Values",
    "00019": "Interpretation",       # best-effort
    "00021": "Misogyny",
    "00023": "Sex",
    "00020": "False Prophecy",
    "00029": "Language",
    "00026": "Homosexuality",
    # 00017 is the arrow icon that precedes contradiction hyperlinks, not a category.
}

FRONT_MATTER_LABELS = {
    "THE OLD TESTAMENT", "THE NEW TESTAMENT",
}


def strip_tags(s: str) -> str:
    s = re.sub(r"<[^>]+>", " ", s)
    return html.unescape(re.sub(r"\s+", " ", s)).strip()


def load_epub(epub_path: Path) -> Path:
    workdir = Path(tempfile.mkdtemp(prefix="sab-epub-"))
    with zipfile.ZipFile(epub_path) as z:
        z.extractall(workdir)
    return workdir


def book_map(workdir: Path):
    """Return ordered list of (book_title, [content files]) from toc.ncx."""
    ncx = (workdir / "toc.ncx").read_text(encoding="utf-8")
    points = re.findall(
        r"<navLabel>\s*<text>([^<]+)</text>\s*</navLabel>\s*<content src=\"([^\"#]+)",
        ncx,
    )
    books = []
    seen_parts = set()
    for label, src in points:
        label = html.unescape(label).strip()
        if re.search(r"\d+$", label):          # chapter-level entry
            continue
        if not label.isupper() or label in FRONT_MATTER_LABELS:
            continue
        part = re.search(r"(part\d+)", src)
        if not part:
            continue
        stem = part.group(1)
        if stem in seen_parts:
            continue
        seen_parts.add(stem)
        files = sorted(workdir.glob(f"text/{stem}*.html"))
        books.append((label, files))
    return books


def title_case(book: str) -> str:
    small = {"OF", "THE", "AND"}
    words = []
    for w in book.split():
        if w in small:
            words.append(w.lower())
        elif re.match(r"^\d", w):
            words.append(w)
        else:
            words.append(w.capitalize())
    return " ".join(words)


def slug(book: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", book.lower()).strip("-")


def parse_book(book: str, files):
    """Parse one book's files into verses and annotations."""
    verses = []       # (chapter, verse_line_text)
    notes = []        # dicts
    chapter = 0
    for f in files:
        raw = f.read_text(encoding="utf-8")
        # Walk headings, bible text, and notes in document order.
        pattern = re.compile(
            r"<h\d[^>]*>(?P<head>[^<]*?%s\s+(?P<chnum>\d+)[^<]*)</h\d>"
            r"|<p class=\"(?P<cls>Bible-Text[^\"]*|Notes-Text[^\"]*)\"(?:[^>]*)>(?P<body>.*?)</p>"
            % re.escape(book),
            re.S,
        )
        for m in pattern.finditer(raw):
            if m.group("head"):
                chapter = int(m.group("chnum"))
                continue
            body = m.group("body")
            if m.group("cls").startswith("Bible-Text"):
                text = strip_tags(body)
                if text:
                    verses.append((chapter, text))
            else:
                ref_m = re.search(r"\((\d+\.[\d\s,.\-–]*)\)", body)
                pre = body[: ref_m.start()] if ref_m else body
                cats = sorted(
                    {
                        ICON_CATEGORIES[i]
                        for i in re.findall(r"images/(\d+)\.jpeg", pre)
                        if i in ICON_CATEGORIES
                    }
                )
                cons = [
                    {"id": f"con{cid}", "title": strip_tags(t)}
                    for cid, t in re.findall(
                        r'href="part0077\.html#con(\d+)">(.*?)</a>', body, re.S
                    )
                ]
                notes.append(
                    {
                        "chapter": chapter,
                        "ref": ref_m.group(1).strip() if ref_m else None,
                        "categories": cats,
                        "contradictions": cons,
                        "text": strip_tags(body),
                    }
                )
    return verses, notes


def parse_contradictions(workdir: Path):
    raw = (workdir / "text" / "part0077.html").read_text(encoding="utf-8")
    out = []
    for m in re.finditer(
        r'<li class="contradict" id="con(\d+)"[^>]*>(.*?)</li>', raw, re.S
    ):
        cid, body = m.groups()
        title_m = re.search(r'<span class="bold">(.*?)</span>', body, re.S)
        title = strip_tags(title_m.group(1)) if title_m else ""
        stances = []
        for sm in re.finditer(
            r'<span class="italic">(.*?)</span>(.*?)(?=<span class="italic">|$)',
            body,
            re.S,
        ):
            stance = strip_tags(sm.group(1))
            refs = [strip_tags(t) for _, t in re.findall(r'<a href="([^"]+)">(.*?)</a>', sm.group(2), re.S)]
            stances.append({"stance": stance, "refs": refs})
        out.append({"id": f"con{cid}", "title": title, "stances": stances})
    return out


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    epub = Path(sys.argv[1])
    if not epub.exists():
        sys.exit(f"EPUB not found: {epub}")

    workdir = load_epub(epub)
    books = book_map(workdir)
    print(f"Found {len(books)} books")

    (PROJECT / "data" / "books").mkdir(parents=True, exist_ok=True)
    (PROJECT / "data" / "sab").mkdir(parents=True, exist_ok=True)
    (PROJECT / "data" / "sab_full").mkdir(parents=True, exist_ok=True)

    for idx, (book, files) in enumerate(books, start=1):
        verses, notes = parse_book(book, files)
        name = f"{idx:02d}-{slug(book)}"
        pretty = title_case(book)

        # Public-domain KJV text, chapter-headed, one verse per line.
        lines = [f"# {pretty}", ""]
        cur = None
        for ch, text in verses:
            if ch != cur:
                cur = ch
                lines += [f"## {pretty} {ch}", ""]
            lines.append(text)
        (PROJECT / "data" / "books" / f"{name}.md").write_text(
            "\n".join(lines) + "\n", encoding="utf-8"
        )

        # Committed annotation index: metadata only, no commentary prose.
        index = [
            {
                "chapter": n["chapter"],
                "ref": n["ref"],
                "categories": n["categories"],
                "contradictions": n["contradictions"],
            }
            for n in notes
            if n["categories"] or n["contradictions"]
        ]
        (PROJECT / "data" / "sab" / f"{name}.json").write_text(
            json.dumps({"book": pretty, "annotations": index}, indent=1),
            encoding="utf-8",
        )

        # Gitignored full commentary for local analysis.
        full = [f"# SAB notes: {pretty}", ""]
        for n in notes:
            cats = ", ".join(n["categories"])
            full.append(f"**({n['ref']})** [{cats}] {n['text']}")
            full.append("")
        (PROJECT / "data" / "sab_full" / f"{name}.md").write_text(
            "\n".join(full), encoding="utf-8"
        )
        print(f"  {name}: {len(verses)} verses, {len(notes)} notes, {len(index)} indexed")

    cons = parse_contradictions(workdir)
    (PROJECT / "data" / "sab" / "contradictions.json").write_text(
        json.dumps(cons, indent=1), encoding="utf-8"
    )
    print(f"Contradictions indexed: {len(cons)}")


if __name__ == "__main__":
    main()
