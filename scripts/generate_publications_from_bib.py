#!/usr/bin/env python3
"""Generate Jekyll publication markdown files from BibTeX files.

This script is intentionally independent of external BibTeX parsers so it can
handle imperfect exports with minor formatting issues.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path


DEFAULT_INPUTS = {
    "publications.bib": "peer_reviewed",
    "proceedings.bib": "conferences",
    "preprint.bib": "preprints",
}


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "publication"


def split_entries(text: str) -> list[str]:
    entries = []
    i = 0
    n = len(text)
    while i < n:
        at = text.find("@", i)
        if at == -1:
            break

        open_brace = text.find("{", at)
        if open_brace == -1:
            break

        depth = 0
        j = open_brace
        while j < n:
            ch = text[j]
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    entries.append(text[at : j + 1])
                    i = j + 1
                    break
            j += 1
        else:
            entries.append(text[at:])
            break
    return entries


def _read_balanced_value(s: str, start: int) -> tuple[str, int]:
    # Supports nested braces and quoted values.
    if start >= len(s):
        return "", start

    if s[start] == "{":
        depth = 0
        i = start
        out = []
        while i < len(s):
            ch = s[i]
            out.append(ch)
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    return "".join(out), i + 1
            i += 1
        return "".join(out), i

    if s[start] == '"':
        i = start + 1
        escaped = False
        out = ['"']
        while i < len(s):
            ch = s[i]
            out.append(ch)
            if ch == '"' and not escaped:
                return "".join(out), i + 1
            escaped = (ch == "\\") and not escaped
            if ch != "\\":
                escaped = False
            i += 1
        return "".join(out), i

    i = start
    while i < len(s) and s[i] not in ",\n":
        i += 1
    return s[start:i], i


def parse_entry(entry: str) -> dict[str, str] | None:
    head_match = re.match(r"@\s*(\w+)\s*\{\s*([^,]+)\s*,", entry, flags=re.IGNORECASE | re.DOTALL)
    if not head_match:
        return None

    entry_type = head_match.group(1).strip().lower()
    key = head_match.group(2).strip()
    body = entry[head_match.end() :]
    if body.endswith("}"):
        body = body[:-1]

    fields: dict[str, str] = {"entrytype": entry_type, "key": key}

    i = 0
    while i < len(body):
        while i < len(body) and body[i] in " \t\r\n,":
            i += 1
        if i >= len(body):
            break

        name_match = re.match(r"([A-Za-z][A-Za-z0-9_\-]*)\s*=", body[i:])
        if not name_match:
            # Skip malformed fragments.
            i += 1
            continue

        name = name_match.group(1).lower()
        i += name_match.end()
        while i < len(body) and body[i] in " \t\r\n":
            i += 1

        raw_value, next_i = _read_balanced_value(body, i)
        i = next_i

        value = raw_value.strip()
        if value.startswith("{") and value.endswith("}"):
            value = value[1:-1].strip()
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1].strip()

        if name not in fields:
            fields[name] = value

    return fields


def clean_latex(text: str) -> str:
    text = text.replace("\\textbf{", "").replace("\\textit{", "")
    text = text.replace("\\_", "_")
    text = text.replace("{", "").replace("}", "")
    text = re.sub(r"\\[A-Za-z]+", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def normalize_doi(doi_or_url: str) -> str:
    value = doi_or_url.strip()
    value = re.sub(r"^https?://(dx\.)?doi\.org/", "", value, flags=re.IGNORECASE)
    value = re.sub(r"^doi:\s*", "", value, flags=re.IGNORECASE)
    return value.strip()


def extract_year(year_raw: str) -> int | None:
    m = re.search(r"(19|20)\d{2}", year_raw)
    if not m:
        return None
    return int(m.group(0))


def build_markdown(fields: dict[str, str], category: str) -> tuple[str, str]:
    title = clean_latex(fields.get("title", fields["key"]))
    venue = clean_latex(fields.get("journal") or fields.get("booktitle") or "")
    year_raw = fields.get("year", "")
    year = extract_year(year_raw)
    date_str = f"{year}-01-01" if year else "1900-01-01"

    doi = ""
    if fields.get("doi"):
        doi = normalize_doi(fields["doi"])
    elif fields.get("url") and "doi.org" in fields["url"].lower():
        doi = normalize_doi(fields["url"])

    slug_base = f"{year or 'undated'}-{slugify(fields['key'])}"
    permalink = f"/publication/{slug_base}"

    lines = [
        "---",
        f'title: "{title.replace("\"", "\\\"")}"',
        "collection: publications",
        f"category: {category}",
        f"permalink: {permalink}",
        "excerpt: ''",
        f"date: {date_str}",
        f"venue: '{venue.replace("'", "''")}'",
    ]

    if doi:
        lines.append(f"doi: '{doi}'")

    lines.extend(
        [
            "---",
            "",
            "",
        ]
    )

    filename = f"{slug_base}.md"
    return filename, "\n".join(lines)


def generate(bib_path: Path, category: str, output_dir: Path, overwrite: bool) -> tuple[int, int]:
    text = bib_path.read_text(encoding="utf-8")
    entries = split_entries(text)

    written = 0
    skipped = 0

    for raw in entries:
        parsed = parse_entry(raw)
        if not parsed:
            skipped += 1
            continue

        filename, markdown = build_markdown(parsed, category)
        target = output_dir / filename

        if target.exists() and not overwrite:
            skipped += 1
            continue

        target.write_text(markdown, encoding="utf-8")
        written += 1

    return written, skipped


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate _publications markdown files from BibTeX.")
    parser.add_argument("--root", default=".", help="Repository root path")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing markdown files")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    output_dir = root / "_publications"
    output_dir.mkdir(parents=True, exist_ok=True)

    total_written = 0
    total_skipped = 0

    for bib_name, category in DEFAULT_INPUTS.items():
        bib_path = root / bib_name
        if not bib_path.exists():
            continue
        written, skipped = generate(bib_path, category, output_dir, args.overwrite)
        total_written += written
        total_skipped += skipped

    print(
        f"Generated {total_written} files, skipped {total_skipped} entries at {dt.datetime.now().isoformat(timespec='seconds')}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
