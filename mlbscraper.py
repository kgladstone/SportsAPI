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

# NL URL
URL1 = "http://espn.go.com/mlb/stats/batting/_/league/nl/count/1/qualified/true"
f1 = "nl1.csv"
os.system("python tbl2csv.py " + URL1 + " " + f1)

URL2 = "http://espn.go.com/mlb/stats/batting/_/league/nl/count/41/qualified/true"
f2 = "nl2.csv"
os.system("python tbl2csv.py " + URL2 + " " + f2)

fn = "nl.csv"
os.system("python combinecsv.py " + fn + " data/" + f1 + " data/" + f2)

# AL URL
URL1 = "http://espn.go.com/mlb/stats/batting/_/league/al/count/1/qualified/true"
f1 = "al1.csv"
os.system("python tbl2csv.py " + URL1 + " " + f1)

URL2 = "http://espn.go.com/mlb/stats/batting/_/league/al/count/41/qualified/true"
f2 = "al2.csv"
os.system("python tbl2csv.py " + URL2 + " " + f2)

fn = "al.csv"
os.system("python combinecsv.py " + fn + " data/" + f1 + " data/" + f2)

# Combine AL and NL into MLB
f1 = "nl.csv"
f2 = "al.csv"
fn = "mlb.csv"
#os.system("python combinecsv.py " + fn + " data/" + f1 + " data/" + f2)