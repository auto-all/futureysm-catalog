#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fetch the public FutureYSM catalog JSON and save it locally."""
import json
import os
import urllib.request

URL = "https://futureysm.st/catalog.json"
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "catalog.json")


def main():
    req = urllib.request.Request(URL, headers={"User-Agent": "futureysm-catalog/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.load(resp)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print(f"updated {OUT}: {data.get('count')} models / {data.get('authors_count')} authors")


if __name__ == "__main__":
    main()
