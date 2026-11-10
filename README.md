# FutureYSM Catalog

Public metadata catalog for [FutureYSM](https://futureysm.st/), a free YSM (Yes Steve Model) model library for Minecraft Java Edition.

- **Site**: https://futureysm.st/
- **Human-readable catalog**: https://futureysm.st/catalog.html
- **JSON catalog**: https://futureysm.st/catalog.json
- **Models**: 2,204
- **Author groups**: 196
- **Language**: Simplified Chinese

## What is this repo?

This repository contains **metadata only** (model names, authors, descriptions, versions, license info, preview image URLs, and links back to the site). It does **not** contain model files.

It exists so that developers, researchers, and AI agents can query the public catalog without scraping the website. The canonical source is always https://futureysm.st/catalog.json.

## Update

The catalog is refreshed weekly by a GitHub Action:

```bash
python scripts/update_catalog.py
```

## Disclaimer

Model copyrights belong to their original authors. FutureYSM only indexes publicly shared content and provides a takedown/claim path on the website. This repo does not grant any license to the models themselves.
