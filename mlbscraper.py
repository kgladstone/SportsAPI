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
def tbl2csvESPN(league, rank):
	# Build URL
	prefix = "http://espn.go.com/mlb/stats/batting/_/league/"
	middle = "/count/"
	suffix = "/qualified/true"
	URL = prefix + league + middle + rank + suffix
	f = league + rank + ".csv"
	tableClass = "tablehead"
	query = "python tbl2csv.py " + URL + " " + f + " " + tableClass
	os.system(query)

	# Post-process: remove RK element
	import csv
	path = "data/" + f
	with open(path,"rb") as source:
	    rdr= csv.reader( source )
	    with open("tmp" + f,"wb") as result:
	        wtr= csv.writer( result )
	        for r in rdr:
				r.remove(r[0])
				wtr.writerow( r )	
	os.system("mv tmp" + f + " " + path)
	return f

def tbl2csvCBS(URL, league, rank):
	f = league + rank + ".csv"
	tableClass = "data"
	query = "python tbl2csv.py " + URL + " " + f + " " + tableClass
	os.system(query)
	return f

def tbl2csvCBSbyTeam(team, rank):
	URL = "http://www.cbssports.com/mlb/stats/playersort/mlb/year-2015-season-regularseason-category-batting-team_abbr-" + team
	f = team + ".csv"
	tableClass = "data"
	query = "python tbl2csv.py " + URL + " " + f + " " + tableClass
	os.system(query)
	return f

def combinecsv(f1, f2, league):
	fn = league + ".csv"
	os.system("python combinecsv.py " + fn + " data/" + f1 + " data/" + f2)
	return fn

######################### ESPN SCRAPER ######################

def espn():

	# NL URL
	league = "nl"
	# First page
	rank = "1"
	f1 = tbl2csvESPN(league, rank)
	# Second page
	rank = "41"
	f2 = tbl2csvESPN(league, rank)

	combinecsv(f1, f2, league)

	########################################

	# NL URL
	league = "al"
	# First page
	rank = "1"
	f1 = tbl2csvESPN(league, rank)
	# Second page
	rank = "41"
	f2 = tbl2csvESPN(league, rank)

	combinecsv(f1, f2, league)

	########################################

	# Combine AL and NL into MLB
	f = combinecsv("nl.csv", "al.csv", "mlb")
	return f

######################### CBS SCRAPER #######################

def cbs(team):
	f = tbl2csvCBSbyTeam(team, "1")
	return f

######################### MAIN FUNCTION ####################

argv = sys.argv
argc = len(argv)

filename = ""

if argc > 1:
	site = argv[1]
	if site.lower() == "espn":
		filename = espn()
	elif site.lower() == "cbs":
		if argv > 2:
			team = argv[2]
		else:
			team = "NYM"
		filename = cbs(team.upper())
	else:
		print("Error: Invalid site")
else:
	print("Error: No site specified")

# Open finished file
if filename != "":
	os.system("open data/" + filename)




