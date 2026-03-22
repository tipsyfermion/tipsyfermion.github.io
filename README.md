# Debaditya Bhattacharya Website

Personal academic website built on Jekyll (Academic Pages base), customized for research-focused content.

## Current Site Structure

- Home/About page: `_pages/about.md`
- Projects page: `_pages/projects.md`
- Publications page: `_pages/publications.html`
- Talks page placeholder: `_pages/talks.html`
- Posts page placeholder: `_pages/year-archive.html`
- CV download page: `_pages/cv.md`
- Main navigation: `_data/navigation.yml`

## Publications Workflow

Publications are generated from BibTeX sources:

- `publications.bib` -> peer-reviewed articles
- `preprint.bib` -> preprints
- `proceedings.bib` -> conference papers

Generator script:

- `scripts/generate_publications_from_bib.py`

Run this command after updating any BibTeX file:

```bash
python scripts/generate_publications_from_bib.py --root . --overwrite
```

Generated output is written to `_publications/`.

## Publication Display Notes

- Publication titles link directly to DOI (when DOI exists).
- Authors are rendered on the publication list.
- Name highlighting is supported for Debaditya Bhattacharya.
- Numbering is separate by section on the publications page (peer-reviewed, preprints, conference papers).
- Math rendering is enabled through MathJax for publication title LaTeX.

## CV

- Primary CV file: `files/Debaditya_CV.pdf`
- Navigation and CV page are configured to link directly to this PDF.

## Run Locally

```bash
bundle install
bundle exec jekyll serve -l -H localhost
```

Open: `http://localhost:4000`

If `_config.yml` is changed, restart the server.

## Docker

```bash
docker compose up
```

Then open: `http://localhost:4000`

## Notes

- Keep BibTeX files in UTF-8 to avoid mojibake issues.
- For any publication/title formatting updates, regenerate `_publications/` with the script above.

## Future Me: Maintenance Playbook

This section is a quick operational guide for future updates.

### Move Items in Top Navigation

Edit `_data/navigation.yml`.

- `main:` controls order in the header.
- Move blocks up/down to reorder items.
- Example item:

```yml
- title: "Projects"
	url: /projects/
```

### Rename Menu Labels Without Changing URLs

Edit only `title` in `_data/navigation.yml` and keep `url` the same.

### Add a New Top-Level Page

1. Create a file in `_pages/`.
1. Add front matter:

```md
---
layout: archive
title: "New Page"
permalink: /new-page/
author_profile: true
---
```

1. Add a corresponding nav item in `_data/navigation.yml`.

### Move/Restructure Projects Content

Current projects content is in `_pages/projects.md`.

- Use `##` headings for project themes.
- Keep paragraphs concise and technical.
- Justified formatting is currently applied directly in markdown with inline `<div style="text-align: justify;">` wrappers.

### Update About Page Content

Edit `_pages/about.md`.

- Keep opening paragraph short.
- Keep major profile details in plain markdown text.
- About text is also wrapped in a justified `<div>` block.

### Publications: Normal Update Cycle

1. Edit source bib files:
	 - `publications.bib`
	 - `preprint.bib`
	 - `proceedings.bib`
1. Run generator:

```bash
python scripts/generate_publications_from_bib.py --root . --overwrite
```

1. Verify output in `_publications/`.

### Publications: Formatting Rules Already Implemented

- Titles can include LaTeX math (MathJax enabled globally).
- Publication title links go to DOI when available.
- Authors are rendered and your name is highlighted.
- Numbering is separate by category section on `_pages/publications.html`.

### If LaTeX Stops Rendering

Check `_includes/footer/custom.html`:

- MathJax config block must appear before MathJax script include.
- Inline math delimiters should include `$...$` and `\(...\)`.

Then rebuild/restart Jekyll.

### If New Publications Do Not Appear

Checklist:

1. Bib entry has a valid `@article`, `@inproceedings`, or `@misc` style entry.
1. `author` and `title` fields exist.
1. Generator was run with `--overwrite`.
1. Jekyll server was refreshed (restart if config/layout changed).

### CV File Updates

- Current CV target: `files/Debaditya_CV.pdf`
- Links are set in:
	- `_data/navigation.yml`
	- `_pages/cv.md`

If file name changes, update both places.

### Common Pitfalls

- Encoding issues (mojibake): keep all bib files UTF-8.
- Config changes in `_config.yml` require a server restart.
- Template/include changes may need hard refresh in browser.

### Quick Verify Commands

```bash
python scripts/generate_publications_from_bib.py --root . --overwrite
bundle exec jekyll serve -l -H localhost
```
