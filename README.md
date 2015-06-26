SportsScraper
-----------

The files "mlbscraper.py" and "ncaascraper.py" are the main files that makes use of a generic webscraper and generic CSV combinator to extract player data from the Internet (as of right now, using ESPN and CBS Stats). The data is stored within the "data" subdirectory. The scraper is becoming more and more versatile, where ideally it could scrape any conceivable HTML table on the web. All of these operations are done in Python.

Simulator
----------
Pipes the scraped data into a work-in-progress Baseball Game Simulator, currently in Java.

Future plans
----------
Select a pitcher-hitter matchup and use probability to predict the outcome
Requires: Pitching stats, probability modelling functions