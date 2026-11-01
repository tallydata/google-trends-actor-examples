#!/usr/bin/env bash
# Run the Actor and print its dataset items. Needs APIFY_TOKEN.
set -euo pipefail
curl -sS -X POST \
  -H "Authorization: Bearer ${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"searchTerms": ["web scraping"], "geo": "US"}' \
  "https://api.apify.com/v2/acts/tallydata~google-trends-interest-over-time/run-sync-get-dataset-items"
