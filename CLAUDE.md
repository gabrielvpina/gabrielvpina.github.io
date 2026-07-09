# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

`me.log` — a personal Quarto website/blog (https://gabrielvpina.github.io) published via GitHub Pages. Content is authored in Quarto Markdown (`.qmd`) and rendered to static HTML in `docs/`, which is what GitHub Pages serves. There is no application code or test suite; the "build" is the Quarto render.

## Commands

```bash
quarto preview          # live-reloading local dev server
quarto render           # render the whole site into docs/
quarto render posts/why_use_linux/post.qmd   # render a single document
```

Requires the Quarto CLI (developed against v1.9.x). Posts with executable code chunks (R/Python) need the corresponding engine installed.

## Publishing workflow (important)

- `docs/` holds the **committed build output** (`output-dir: docs` in `_quarto.yml`) and is served directly by GitHub Pages. After changing any `.qmd`, CSS, or asset, run `quarto render` and commit the regenerated `docs/` alongside the source — otherwise the live site won't reflect the change.
- `execute: freeze: true` caches computation results in `_freeze/`. Code chunks are re-run only when their source changes; `_freeze/` is committed so renders are reproducible without re-executing everything. `.quarto/` and `**/*.quarto_ipynb` are gitignored (Quarto scratch state).

## Structure & conventions

- **`_quarto.yml`** — single source of site config: navbar, footer, theme (`flatly` + `styles/retro.css`), colors. Section landing pages are `<section>/index.qmd`.
- **`index.qmd`** — the homepage uses `page-layout: custom` with hand-written HTML (a "retro desktop" UI) inside a `` ```{=html} `` block, plus a Quarto `listing` that renders the 3 most recent posts through the EJS template `assets/recent-posts.ejs`. Editing the homepage layout means editing that raw HTML and its CSS, not standard Quarto components.
- **Posts** live in `posts/<slug>/` — one folder per post containing the `.qmd` plus its images/`figures/`. `posts/index.qmd` auto-generates the grid via a `listing` over `*/*.qmd`, so a new post just needs a folder with a properly-fronted `.qmd`. Post frontmatter drives the listing: `title`, `image` (path relative to the post folder), `categories`, `date`, `author`, and optionally `bibliography: refs.bib` + `csl: abnt.csl` for citations.
- **`styles/retro.css`** — all custom styling (neo-brutalist/retro theme, purple accents, homepage desktop windows). This layers on top of the `flatly` Bootstrap theme.
- **`removeBackground.py`** — standalone one-off utility (uses `rembg` + Pillow) to strip backgrounds from profile images; not part of the site build.
