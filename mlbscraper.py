# /***************************************************************
#  * MLB HTML Table Webscraper
#  * By: Keith Gladstone (keithag@princeton.edu)
#  * Created in June 2015
#  * 
#  * This file scrapes MLB player data using the generic scraper
#  *
#  * Requires Python to execute.
#  *
#  * Dependencies: tbl2csv.py
#  ***************************************************************/
import os.path
import sys

# Send URL to generic scraper
URL = "http://espn.go.com/mlb/stats/batting/_/sort/avg/league/nl/year/2015/seasontype/2"
os.system("python tbl2csv.py " + URL)
