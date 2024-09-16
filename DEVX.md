# TODO

- Create public data dumps files that can be accessed via URL and also without access key. Remove :9000 port number in s3 endpoints if possible.
- Fix publisher data in README.md and demo.ipynb
- FINISH PREFECT WORKFLOW!!!!
- Run the scraper as prefect flow
- Scraping mode - Update/dump
- While running the test, if it fails, prevent scrapy from showing the entire output
- moneycontrol and indianexpress have very aggressive protection.
  - they don't seem to allow usage of even floating ips from hetzner. but ips of brightdata seem to work
  - pytest fails for these spiders on hetzner server.
