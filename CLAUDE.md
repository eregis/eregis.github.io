# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Academic blog built with Jekyll, hosted on GitHub Pages at https://eregis.github.io. The blog "Critical Points" focuses on statistical physics, probability theory, and machine learning topics.

## Common Commands

```bash
# Serve locally for development
bundle exec jekyll serve

# Install dependencies (first time setup)
bundle install
```

## Content Structure

- `blog/_posts/` - Published posts using Jekyll naming: `YYYY-MM-DD-title.md`
- `_drafts/` - Work-in-progress posts (gitignored, kept locally only)
- `assets/` - Images and Python visualization scripts organized by post topic
- `_layouts/` - Jekyll HTML templates (default.html is the main template)
- `_includes/` - Reusable HTML partials (e.g., google-analytics.html)

## Drafting Subagents

Six subagents in `.claude/agents/` support the drafting workflow. The author brings a rough draft; the main agent polishes it into a finished post. The subagents are the research layer — they read the corpus, the math, and the sources, and report back. **All are read-only except `figure-smith`; the main agent applies the edits**, so the author sees the diff.

| Agent | Use it when |
|---|---|
| `blog-style-analyst` | Before drafting or polishing. Reads published posts and returns the author's voice, notation, and structural conventions, per genre. Given a draft, returns line-anchored rewrites for passages that read off-voice. |
| `blog-archivist` | Before drafting. Searches the back catalogue for prior coverage — related posts with paste-ready `{% post_url %}` links, derivations already done (link instead of repeating), notation already committed to. |
| `derivation-checker` | On any draft with math. Independently re-derives each step; flags sign errors, dropped factors, unstated assumptions. Verifies with sympy/numpy. |
| `fact-checker` | On any draft citing papers, people, or facts. Verifies attributions, dates, and numbers against primary sources; checks blockquotes are verbatim; flags claims that will go stale. |
| `post-linter` | Before publishing. Front matter, kramdown/MathJax rendering hazards, asset paths, cross-link validity, dead external links. |
| `figure-smith` | When a post needs a figure. Reads existing `assets/*/*.py` to match the house matplotlib idiom, writes and renders the script, returns the embed snippet. The only agent that writes files. |

The three checkers (`derivation-checker`, `fact-checker`, `post-linter`) have disjoint jobs by design: is the *math* right, is the *world* right, does it *render*. Run them in parallel.

## Post Front Matter

Posts require this front matter format:
```yaml
---
layout: post
title: "Post Title"
date: YYYY-MM-DD
mathjax: true
description: "SEO description"
keywords: keyword1, keyword2, keyword3
---
```

## Math Rendering

MathJax 3 is configured for mathematical notation:
- Inline math: `$...$` or `\(...\)`
- Display math: `$$...$$` or `\[...\]`

## Analytics

Google Analytics is enabled with Measurement ID `G-M8TE1MHJ0G`. The tracking script is in `_includes/google-analytics.html` and only loads in production (not during local development).

## CI/CD

When posts are pushed to `blog/_posts/` on master, GitHub Actions automatically submits URLs to Google Indexing API.

## Windows Troubleshooting

If `bundle exec jekyll serve` crashes with `Permission denied @ apply2files - _site/./nul`, a file literally named `nul` exists in the repo. On Windows, `nul` is a reserved device name (like `/dev/null` on Unix), so standard file operations can't delete it. To remove it, use the Windows API via Python:

```python
import ctypes
ctypes.windll.kernel32.DeleteFileW("\\\\?\\C:\\Users\\ericf\\critical-points\\nul")
```

The `\\?\` prefix bypasses Windows device name resolution. This file is typically created accidentally by scripts that redirect to `/dev/null` on a Windows shell.

## Recent Changes (January 2026)

- Removed unused `_layouts/head.html` (contained outdated MathJax v2)
- Created `_includes/google-analytics.html` and enabled Google Analytics
- Added SEO metadata (description, keywords) to 10 posts from 2025
- Added `_drafts/`, `.DS_Store`, `Thumbs.db` to `.gitignore`
- Added `title_separator: ""` to remove site title suffix from search results
