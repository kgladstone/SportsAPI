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
def tbl2csvESPN(prefix, middle, suffix, league, rank):
	URL = prefix + league + middle + rank + suffix
	f = league + rank + ".csv"
	os.system("python tbl2csv.py " + URL + " " + f + " tablehead 1")
	return f

def tbl2csvCBS(URL, league, rank):
	f = league + rank + ".csv"
	nrow = "31"
	os.system("python tbl2csv.py " + URL + " " + f + " data 1 " + nrow)
	return f

def tbl2csvCBSbyTeam(team, rank):
	URL = "http://www.cbssports.com/mlb/stats/playersort/mlb/year-2015-season-regularseason-category-batting-team_abbr-" + team
	f = team + ".csv"
	nrow = "31"
	os.system("python tbl2csv.py " + URL + " " + f + " data 1 " + nrow)
	return f

def combinecsv(f1, f2, league):
	fn = league + ".csv"
	os.system("python combinecsv.py " + fn + " data/" + f1 + " data/" + f2)
	return fn

def espn():
	# Build URL
	prefix = "http://espn.go.com/mlb/stats/batting/_/league/"
	middle = "/count/"
	suffix = "/qualified/true"

	# NL URL
	league = "nl"
	# First page
	rank = "1"
	f1 = tbl2csvESPN(prefix, middle, suffix, league, rank)
	# Second page
	rank = "41"
	f2 = tbl2csvESPN(prefix, middle, suffix, league, rank)

	combinecsv(f1, f2, league)

	########################################

	# NL URL
	league = "al"
	# First page
	rank = "1"
	f1 = tbl2csvESPN(prefix, middle, suffix, league, rank)
	# Second page
	rank = "41"
	f2 = tbl2csvESPN(prefix, middle, suffix, league, rank)

	combinecsv(f1, f2, league)

	########################################

	# Combine AL and NL into MLB
	combinecsv("nl.csv", "al.csv", "mlb")

	########################################

def cbs():
	team = "NYM"
	tbl2csvCBSbyTeam(team, "1")
	team = "PHI"
	tbl2csvCBSbyTeam(team, "1")

# Run ESPN scraper: 
#espn()

# Run CBS scraper
# URL = "http://www.cbssports.com/mlb/stats/playersort/mlb/year-2015-season-regularseason-category-batting-qualifying-1"
cbs()


