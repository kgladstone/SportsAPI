# /***************************************************************
#  * Generic CSV Combinator
#  * By: Keith Gladstone (keithag@princeton.edu)
#  * Created in June 2015
#  * 
#  * This file combines CSV files with the same header 
#  * Requires Python to execute.
#  ***************************************************************/
import sys
import os.path

def getHeader(s):
	return s[0:s.index("\n")]

def rmHeader(s):
	h = getHeader(s)
	return s[len(h) + 1:len(s)]

fn = sys.argv[1]
f1 = sys.argv[2]
f2 = sys.argv[3]

with open(f1) as f:
    s1 = f.read()

with open(f2) as f:
    s2 = f.read()

h = getHeader(s1)

# Open the file with writing permission
path = "data/" + fn
myfile = open(path, 'w')

# Write to file
myfile.write(h + "\n")

# TODO: Iterate over list of csv strings
myfile.write(rmHeader(s1))
myfile.write(rmHeader(s2))

# Close the file
myfile.close()

# Delete src files
os.system("rm " + f1)
os.system("rm " + f2)
