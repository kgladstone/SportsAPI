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

# Send URLs to generic scraper

# Build URL
prefix = "http://espn.go.com/mlb/stats/batting/_/league/"
middle = "/count/"
suffix = "/qualified/true"

# NL URL
league = "nl"

# First page
rank = "1"
URL = prefix + league + middle + rank + suffix
f1 = "nl1.csv"
os.system("python tbl2csv.py " + URL + " " + f1 + " tablehead 1")

# Second page
rank = "41"
URL = prefix + league + middle + rank + suffix
f2 = "nl2.csv"
os.system("python tbl2csv.py " + URL + " " + f2 + " tablehead 1")

fn = "nl.csv"
os.system("python combinecsv.py " + fn + " data/" + f1 + " data/" + f2)

########################################

# AL URL
league = "al"

# First page
rank = "1"
URL = prefix + league + middle + rank + suffix
f1 = "al1.csv"
os.system("python tbl2csv.py " + URL + " " + f1 + " tablehead 1")

# Second page
rank = "41"
URL = prefix + league + middle + rank + suffix
f2 = "al2.csv"
os.system("python tbl2csv.py " + URL + " " + f2 + " tablehead 1")

fn = "al.csv"
os.system("python combinecsv.py " + fn + " data/" + f1 + " data/" + f2)

# Combine AL and NL into MLB
f1 = "nl.csv"
f2 = "al.csv"
fn = "mlb.csv"
os.system("python combinecsv.py " + fn + " data/" + f1 + " data/" + f2)