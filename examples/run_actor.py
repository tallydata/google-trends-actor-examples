"""Run the Actor and print one row per point. Needs `pip install apify-client` and APIFY_TOKEN."""

import os

from apify_client import ApifyClient

ACTOR = "tallydata/google-trends-interest-over-time"

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor(ACTOR).call(run_input={"searchTerms": ["web scraping"], "geo": "US"})
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["searchTerm"])
    for point in item["interestOverTime_timelineData"]:
        print(point["formattedAxisTime"], point["value"][0], "(partial)" if point.get("isPartial") else "")
