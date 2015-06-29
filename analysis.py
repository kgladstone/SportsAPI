# /***************************************************************
#  * CSV Data Analysis
#  * By: Keith Gladstone (keithag@princeton.edu)
#  * Created in June 2015
#  * 
#  * This file is used for data analysis
#  *
#  * Requires Python to execute.
#  *
#  * Dependencies: data files
#  ***************************************************************/
import sys
import csv
import operator

# Test if float
def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

############# MAIN FUNCTION ##################

argv = sys.argv
argc = len(argv)

if argc > 1:
	f = sys.argv[1].upper()

	filename = "data/" + f + ".csv"
	data = csv.reader(open(filename), delimiter=',')
	header = next(data) # Skip header
	data = list(data) # Convert data to list type
	data = rmHeaders(data, header) # Remove repeats of header 

	if argc > 2:
		sortby = int(sys.argv[2])
	else:
		sortby = 3

	sortedlist = sorted(data, key=operator.itemgetter(sortby), reverse=True)

	#### ISSUE: FIX SORTING NUMBERS AS STRINGS

	print("Stats: ")
	for i, val in enumerate(header):
		print i, val
	print("-------------------------------")

	# Gather item key
	if "PLAYER" in header:
		key = header.index("PLAYER")
	elif "Player" in header:
		key = header.index("Player")
	elif "TEAM" in header:
		key = header.index("TEAM")
	elif "Team" in header:
		key = header.index("Team")
	else:
		key = 0

	for row in sortedlist:
		name = row[key]
		print(name + "\t\t" + header[sortby] + ": " + row[sortby])

	# Print header again
	for i, val in enumerate(header):
		print i, val

