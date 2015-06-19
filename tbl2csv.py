# /***************************************************************
#  * Generic HTML Table Webscraper
#  * By: Keith Gladstone (keithag@princeton.edu)
#  * Created in June 2015
#  * 
#  * This file scrapes data from an HTML table on the Web
#  * and outputs it into a CSV file. 
#  * A richer logic will allow for more versatility.
#  * Requires Python to execute.
#  ***************************************************************/
import urllib
import sys
import os.path

# Scraping functions

# Return table from the HTML source code
def getTable(content):
	start = content.index("<table class=")
	end = content.index("</table>", start)
	return content[start:end]

# Return table from the HTML source code given class tag
def getTableWithTag(content, tag):
	start = content.index("<table class=\"" + tag)
	end = content.index("</table>", start)
	return content[start:end]

# Return header of table
def getHeader(content):
	exp1 = "<tr"
	exp2 = ">"
	exp3 = "</tr>"
	start = content.index(exp1)
	mid = content.index(exp2, start) + len(exp2)
	end = content.index(exp3, mid)
	return content[mid:end]

# Return row x of table
def getRow(content, x, header):
	row = getRowWithTags(content, x, header)
	if row == -1:
		return -1
	else:
		return stripTag(row, "tr")

# Return row x of table and include full <tr> tags
def getRowWithTags(content, x, header):
	exp1 = "<tr"
	exp2 = ">"
	exp3 = "</tr>"
	end = 0
	for i in range(0, x + 1): # do not scrape header
		#if end >= len(content) - 10:
		#	return -1
		start = content.index(exp1, end)
		mid = content.index(exp2, start) + len(exp2)
		end = content.index(exp3, mid) + len(exp3)
	result = content[start:end]
	if header == "" or result.find(header) == -1: # if not equal to header
		return result
	else:
		return -1 # indicates row x is a header

# Return element y of table
def getElement(row, y):
	if (row.find("<th") == -1):
		exp1 = "<td"
		exp2 = "</td>"
	else:
		exp1 = "<th"
		exp2 = "</th>"
	end = 0
	for i in range(0, y):
		start = row.index(exp1, end)
		mid = row.index(">", start) + 1
		end = row.index(exp2, mid)
	result = cleanStr(row[mid:end])
	return result

# Return string within link tag
def stripTag(s, tag):
	if s.find("<" + tag + " ") == -1:
		return s
	else:
		start = s.index(">")
		end = s.index("</" + tag, start)
		return s[start + 1:end]

# Compose stripping functions 
def cleanStr(s):
	noLink = stripTag(s, "a")
	noSpan = stripTag(noLink, "span")
	return noSpan

# Strip the first row of the table
def stripRow(table, x):
	row = getRowWithTags(table, x, "") # blank header
	start = table.index(row)
	end = start + len(row)
	return table[0:start] + table[end:len(table)]


# Return number of columns in row
def getWidth(row):
	result = 1
	if (row.find("<th") == -1):
		exp1 = "<td"
		exp2 = "</td>"
	else:
		exp1 = "<th"
		exp2 = "</th>"
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
	exp2 = ">"
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

# Apply generic webscraper to MLB hitting stats
if len(sys.argv) > 2:
	URL = sys.argv[1] 
	filename = sys.argv[2]
	
	sock = urllib.urlopen(URL)
	content = sock.read()
	sock.close()

	# Get items from content of HTML page
	if len(sys.argv) > 3:
		tag = sys.argv[3]
		table = getTableWithTag(content, tag)
	else:
		table = getTable(content)

	if len(sys.argv) > 4:
		if (sys.argv[4] == "1"):
			table = stripRow(table, 0)
		if (sys.argv[4] == "2"): # Parameter to strip a row of table
			table = stripRow(table, 0)
			table = stripRow(table, 0)

	# Open the file with writing permission
	path = "data/" + filename
	myfile = open(path, 'w')

	# Write items to CSV file
	header = getHeader(table)
	cols = getWidth(header)

	if len(sys.argv) > 5:
		rows = int(sys.argv[5])
	else:
		rows = getHeight(table)

	# Write header first
	myfile.write(getElement(header, 1))
	for k in range(3, cols):
		myfile.write("," + getElement(header, k))
	myfile.write("\n")

	# Write rows
	for i in range(0, rows):
		row = getRow(table, i, header)
		if (row != -1):
			myfile.write(getElement(row, 1))
			for k in range(3, cols):
				myfile.write("," + getElement(row, k))
			myfile.write("\n")

	# Close the file
	myfile.close()

	# Print file contents
	#os.system("cat " + path)

# Throw error message
else:
	print("Error: No URL specified")