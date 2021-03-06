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

TODOs
----------
- Convert scrapers from hard-coding to [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- Make more scrapers
- Expand the Baseball Game Simulator
- Data analysis: Select a pitcher-hitter matchup and use probability to predict the outcome. Requires: Pitching stats, probability modelling functions
- Expand the README 
