# /***************************************************************
#  * Generic HTML Table Webscraper
#  * By: Keith Gladstone (keithag@princeton.edu)
#  * Created in June 2015
#  * 
#  * This file scrapes data from an HTML table on the Web
#  * and outputs it into a CSV file. 
#  * Requires Python to execute.
#  ***************************************************************/
import urllib
import datetime
import sys

# Apply generic webscraper to MLB hitting stats
URL = "http://espn.go.com/mlb/stats/batting/_/sort/avg/league/nl/year/2015/seasontype/2"
fn = "test.csv"

# Scraping functions

# Return table from the HTML source code
def getTable(content):
	start = content.index("<table class=\"tablehead\"")
	end = content.index("</table>", start)
	return content[start:end]

# Return header of table
def getHeader(content):
	exp1 = "<tr"
	exp2 = "align=\"right\">"
	exp3 = "</tr>"
	start = content.index(exp1)
	mid = content.index(exp2, start) + len(exp2)
	end = content.index(exp3, mid)
	return content[mid:end]

# Return row x of table
def getRow(content, x):
	exp1 = "<tr"
	exp2 = "align=\"right\">"
	exp3 = "</tr>"
	end = 0
	for i in range(0, x + 1): # do not scrape header
		if end >= len(content) - 10:
			return -1
		start = content.index(exp1, end)
		mid = content.index(exp2, start) + len(exp2)
		end = content.index(exp3, mid)
	result = content[mid:end]
	if result.find(getHeader(content)) == -1:
		return result
	else:
		return -1

# Return element y of table
def getElement(row, y):
	exp1 = "<td"
	exp2 = "</td>"
	end = 0
	for i in range(0, y):
		start = row.index(exp1, end)
		mid = row.index(">", start) + 1
		end = row.index(exp2, mid)
	result = cleanStr(row[mid:end])
	return result

# Return string within link tag
def stripLink(s):
	if s.find("<a ") == -1:
		return s
	else:
		start = s.index(">") + 1
		end = s.index("<", start)
		return s[start:end]

# Return string within span tag
def stripSpan(s):
	if s.find("<span ") == -1:
		return s
	else:
		start = s.index(">") + 1
		end = s.index("<", start)
		return s[start:end]

# Compose stripping functions 
def cleanStr(s):
	noLink = stripLink(s)
	noSpan = stripSpan(noLink)
	return noSpan

# Return number of columns in row
def getWidth(row):
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

# Return number of rows of table
def getHeight(table):
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
sock = urllib.urlopen(URL)
content = sock.read()
sock.close()

# Get items from content of HTML page
table = getTable(content)

# Open the file with writing permission
filename = "data/" + fn
myfile = open(filename, 'w')

# Write items to CSV file
header = getHeader(content)
cols = getWidth(header)
rows = getHeight(table)

# Write header first
myfile.write(getElement(header, 2))
for k in range(3, cols):
	myfile.write("," + getElement(header, k))
myfile.write("\n")

# Write rows
for i in range(0, rows):
	row = getRow(table, i)
	if (row != -1):
		myfile.write(getElement(row, 2))
		for k in range(3, cols):
			myfile.write("," + getElement(row, k))
		myfile.write("\n")

# Close the file
myfile.close()