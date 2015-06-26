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

###################### CONTENT OPS ###########################

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

###################### TABLE OPS ############################

# Return row x of table
def getRow(table, x):
	row = getRowWithTags(table, x)
	if row == -1:
		return -1
	else:
		return stripTag(row, "tr")

# Return row x of table and include full <tr> tags
def getRowWithTags(table, x):
	exp1 = "<tr"
	exp2 = ">"
	exp3 = "</tr>"
	end = 0
	for i in range(0, x + 1): 
		start = table.index(exp1, end)
		mid = table.index(exp2, start) + len(exp2)
		end = table.index(exp3, mid) + len(exp3)
	result = table[start:end]
	return result

# Strip the first row of the table
def stripRow(table, x):
	row = getRowWithTags(table, x)
	start = table.index(row)
	end = start + len(row)
	return table[0:start] + table[end:len(table)]

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

# Return number of columns in table
def getWidth(table):
	row = getRow(table, 0)
	return int(getColSpan(row))

###################### ROW OPS ##############################

# Returns True if row doesn't contain a hardcoded "colspan" value
def isNormalRow(row):
	hasColSpan = row.find("colspan")
	return hasColSpan == -1

# Returns the number of columns in a row
def getColSpan(row):
	hasColSpan = row.find("colspan")
	colspan = 0
	if hasColSpan != -1: # Option 1) Pull value directly
		start = row.index("colspan") + len("colspan") + 2
		end = row.index("\"", start)
		colspan = row[start:end]
		return colspan
	else: # Option 2) Need to count elements
		if (row.find("<th") == -1):
			exp1 = "<td"
			exp2 = "</td>"
		else:
			exp1 = "<th"
			exp2 = "</th>"
		end = 0
		while True:
			if row.find(exp1, end) == -1:
				return colspan
			else:
				start = row.index(exp1, end)
				mid = row.index(">", start) + 1
				end = row.index(exp2, mid)
				colspan += 1
		return colspan

# Return element y of table
def getElement(row, y):
	if isNormalRow(row) == -1:
		return -1
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

###################### STRING OPS ###########################

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

#################### MAIN FUNCTION  #########################

# Process arguments
argv = sys.argv
argc = len(argv)

URL = ""
filename = ""
tableClass = ""

if argc > 1:
	URL = argv[1]
	if argc > 2:
		filename = argv[2]

		# Scrape HTML
		sock = urllib.urlopen(URL)
		content = sock.read()
		sock.close()
		if argc > 3:

			# Table class specified
			tableClass = argv[3]
			table = getTableWithTag(content, tableClass)	

		else:

			# Table class unspecified
			table = getTable(content)

		nrow = getHeight(table)
		ncol = getWidth(table)

		print("height")
		print(nrow)
		print("width")
		print(ncol)

		# Open the file with writing permission
		path = "data/" + filename
		myfile = open(path, 'w')

		# Write rows
		for i in range(0, nrow):
			row = getRow(table, i)
			#print("Row: " + str(row) + "\n")
			if row != -1: # if it is a row
				if isNormalRow(row) != False:
					for k in range(1, ncol):
						element = getElement(row, k)
						myfile.write(element)
						if k < ncol - 1:
							myfile.write(",")
					myfile.write("\n")

		# Close the file
		myfile.close()

	else: # Filename not specified
		print("Error: Output filename not specified")
else:
	print("Error: Scraper URL not specified")