# /***************************************************************
#  * NCAAM HTML Table Webscraper
#  * By: Keith Gladstone (keithag@princeton.edu)
#  * Created in June 2015
#  * 
#  * This file scrapes NCAAM player data using the generic scraper
#  *
#  * Requires Python to execute.
#  *
#  * Dependencies: tbl2csv.py
#  ***************************************************************/
import os.path
import sys

# Send URL to generic scraper
def scrape(URL, f):
	tableClass = "data"
	filename = f + ".csv"
	query = "python tbl2csv.py " + URL + " " + filename + " " + tableClass
	os.system(query)
	return filename

def scrapeDivision(div):
	prefix = "http://www.cbssports.com/collegebasketball/stats/teamsort/"
	suffix = "/SCORING/regularseason/yearly"
	URL = prefix + div + suffix
	filename = scrape(URL, div)
	return filename

######################### MAIN FUNCTION ####################
argv = sys.argv
argc = len(argv)

filename = ""

if argc > 1:
	div = argv[1]
	filename = scrapeDivision(div)
else:
	URL = "http://www.cbssports.com/collegebasketball/stats/leaders/NCAAB/PTSAVG/regularseason/yearly"
	f = "ncaa1"
	filename = scrape(URL, f)

# Open finished file
os.system("open data/" + filename)


