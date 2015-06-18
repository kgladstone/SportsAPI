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

with open(f1) as f:
    s2 = f.read()

h = getHeader(s1)

s1clean = rmHeader(s1)
s2clean = rmHeader(s2)

# Open the file with writing permission
path = "data/" + fn
myfile = open(path, 'w')

# Write to file
myfile.write(h + s1clean + s2clean)

# Close the file
myfile.close()
