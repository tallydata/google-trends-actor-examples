# Google Trends Actor: examples and compatibility test

Examples for `tallydata/google-trends-interest-over-time`, a Google Trends Actor on Apify, and the test that checks its output against the official `apify/google-trends-scraper`.

The Actor is published on the Apify Store: https://apify.com/tallydata/google-trends-interest-over-time ("Google Trends Scraper: Compare Keywords Over Time"). Its output matched the official Actor's golden outputs (same keys, order and types) in the pre-release check; Google samples its data, so values differ slightly between runs.

Unofficial. Not affiliated with or endorsed by Google.

## What's here

| Path | What it is |
|---|---|
| `examples/run_actor.py` | Run the Actor from Python with the Apify client |
| `examples/run_actor.sh` | Run it with `curl` |
| `notebooks/quickstart.ipynb` | Colab notebook: run it and plot the result, nothing to install |
| `compat/check_output.py` | Compares an Actor's output with a saved official output: keys, key order and types, ignoring values |
| `fixtures/official/` | Real output of `apify/google-trends-scraper`, one item per captured input |

## Compatibility test

```bash
python compat/check_output.py your-dataset-items.json fixtures/official/b-compare5-us.items.json
```

| Input | Official output saved | Our output checked |
|---|---|---|
| 5 compared terms, US | Yes (2026-11-01) | Pending |
| Single term, worldwide | Not yet | Pending |
| Start URL, `geo=US-CA` | Not yet | Pending |
| Single term, Greece, 5 years | Not yet | Pending |
| Nonsense term | Not yet | Pending |

## Use it from an AI agent

Add this MCP server to your client, with your Apify token:

```
https://mcp.apify.com?tools=actors,docs,tallydata/google-trends-interest-over-time
```

## Known gaps

Related topics are not fetched: the field stays empty. US city data is not available.

## License

MIT
