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

def scrapeDivision(div):
	prefix = "http://www.cbssports.com/collegebasketball/stats/teamsort/"
	suffix = "/SCORING/regularseason/yearly"
	URL = prefix + div + suffix
	scrape(URL, div)

URL = "http://www.cbssports.com/collegebasketball/stats/leaders/NCAAB/PTSAVG/regularseason/yearly"
f = "ncaa1"
scrape(URL, f)


# Test scrape by division
scrapeDivision("ACC")
scrapeDivision("IVY")
scrapeDivision("PAT")


