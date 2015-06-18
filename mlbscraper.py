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

# MLB URL
URL1 = "http://espn.go.com/mlb/stats/batting/_/league/nl/count/1/qualified/true"
f1 = "mlb1.csv"
os.system("python tbl2csv.py " + URL1 + " " + f1)


URL2 = "http://espn.go.com/mlb/stats/batting/_/league/nl/count/41/qualified/true"
f2 = "mlb2.csv"
os.system("python tbl2csv.py " + URL2 + " " + f2)

fn = "mlb.csv"
os.system("python combinecsv.py " + fn + " data/" + f1 + " data/" + f2)