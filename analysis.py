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

i = 9 # Sort data by column i


filename = "data/" + sys.argv[1] + ".csv"
data = csv.reader(open(filename), delimiter=',')
header = next(data) # Skip header
sortedlist = sorted(data, key=operator.itemgetter(i), reverse=True)

print(header)
for row in sortedlist:
	print(row)

