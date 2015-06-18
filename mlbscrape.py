# /***************************************************************
#  * MLB Data Webscraper
#  * By: Keith Gladstone (keithag@princeton.edu)
#  * Created in June 2015
#  * 
#  * This file scrapes MLB player data from reliable and update
#  * website, XXX.com, and outputs it into a CSV file. 
#  * Requires Python to execute.
#  ***************************************************************/
import urllib
import datetime
import sys

# Scraping functions
def getTable(content):
	start = content.index("<table class=\"tablehead\"")
	end = content.index("</table>", start)
	return content[start:end]

def getHeader(content):
	exp1 = "<tr"
	exp2 = "align=\"right\">"
	exp3 = "</tr>"
	start = content.index(exp1)
	mid = content.index(exp2, start) + len(exp2)
	end = content.index(exp3, mid)
	return content[mid:end]

# Return a row containing player information
def getPlayer(content, num):
	exp1 = "<tr"
	exp2 = "align=\"right\">"
	exp3 = "</tr>"
	end = 0
	for i in range(0, num + 1): # do not scrape header
		if end >= len(content) - 10:
			return -1
		start = content.index(exp1, end)
		mid = content.index(exp2, start) + len(exp2)
		end = content.index(exp3, mid)
	result = content[mid:end]
	if result.find("<span title=\"Rank\">") == -1:
		return result
	else:
		return -1

def getStat(player, num):
	exp1 = "<td"
	exp2 = "</td>"
	end = 0
	for i in range(0, num):
		start = player.index(exp1, end)
		mid = player.index(">", start) + 1
		end = player.index(exp2, mid)
	result = stripLink(stripSpan(player[mid:end]))
	return result

# Clean out the link tag if present
def stripLink(s):
	if s.find("<a ") == -1:
		return s
	else:
		start = s.index(">") + 1
		end = s.index("<", start)
		return s[start:end]

def stripSpan(s):
	if s.find("<span ") == -1:
		return s
	else:
		start = s.index(">") + 1
		end = s.index("<", start)
		return s[start:end]

def getNumCols(row):
	result = 1
	exp1 = "<td"
	exp2 = "</td>"
	end = 0
	while True:
		if row.find(exp1, end) == -1:
			return result
		else:
			start = row.index(exp1, end)
			mid = row.index(">", start) + 1
			end = row.index(exp2, mid)
			result += 1
	return result

def getNumRows(table):
	result = 0
	exp1 = "<tr"
	exp2 = "align=\"right\">"
	exp3 = "</tr>"
	end = 0
	while True: 
		if table.find(exp1, end) == -1:
			return result
		else:
			start = table.index(exp1, end)
			mid = table.index(exp2, start) + len(exp2)
			end = table.index(exp3, mid)
			result += 1

# This scrapes the HTML
URL = "http://espn.go.com/mlb/stats/batting/_/sort/avg/league/nl/year/2015/seasontype/2"
sock = urllib.urlopen(URL)
content = sock.read()
sock.close()

# Get items from content of HTML page
table = getTable(content)

# Open the file with writing permission
fn = "test.csv"
filename = "data/" + fn
myfile = open(filename, 'w')

# Write items to CSV file
header = getHeader(content)
cols = getNumCols(header)
rows = getNumRows(table)

# Write header first
myfile.write(getStat(header, 2))
for k in range(3, cols):
	myfile.write("," + getStat(header, k))
myfile.write("\n")

# Write players
for i in range(0, rows):
	player = getPlayer(table, i)
	if (player != -1):
		myfile.write(getStat(player, 2))
		for k in range(3, cols):
			myfile.write("," + getStat(player, k))
		myfile.write("\n")

# Close the file
myfile.close()