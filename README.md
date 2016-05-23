SportsScraper
-----------

The files "mlbscraper.py" and "ncaascraper.py" are the main files that makes use of a generic webscraper and generic CSV concatenator to extract player and team data from the Internet (as of right now, using ESPN and CBS Stats). The data is stored within the "data" subdirectory. The scraper is becoming more and more versatile, so it could ideally scrape any conceivable HTML table on the web. All of these operations are done in Python.

Execution (Python Scrapers)
---------
Pull the latest hitter data from ESPN

```python mlbscraper.py ESPN```

Pull the latest hitter data for any team (using the appropriate abbrev.) from CBS. This example pulls from the New York Mets (NYM)

```python mlbscraper.py CBS NYM```

Pull the latest NCAA Men's Basketball data for any division (using the appropriate abbrev.) This example pulls from the ACC

```python ncaascraper.py ACC```

MLB Player Weight Scraper (R)
----------
Since there isn't a site where MLB player weights are listed conveniently, the R script `player_weights.R` scrapes many pages of FanGraphs to compile a dataset

Simulator
----------
Pipes the scraped data into a work-in-progress Baseball Game Simulator, currently in Java.

Future plans
----------
Select a pitcher-hitter matchup and use probability to predict the outcome
Requires: Pitching stats, probability modelling functions
