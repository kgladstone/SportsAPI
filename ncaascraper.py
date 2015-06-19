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
URL1 = "http://www.cbssports.com/collegebasketball/stats/leaders/NCAAB/PTSAVG/regularseason/yearly"
f1 = "ncaa.csv"
tag = "data"
rows = "50"
os.system("python tbl2csv.py " + URL1 + " " + f1 + " " + tag + " " + "2 " + rows)