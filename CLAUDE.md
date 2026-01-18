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

## Recent Changes (January 2026)

- Removed unused `_layouts/head.html` (contained outdated MathJax v2)
- Created `_includes/google-analytics.html` and enabled Google Analytics
- Added SEO metadata (description, keywords) to 10 posts from 2025
- Added `_drafts/`, `.DS_Store`, `Thumbs.db` to `.gitignore`
- Added `title_separator: ""` to remove site title suffix from search results
