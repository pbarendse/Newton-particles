import math
import sys
from writetofilefunctions import *

# readfile_test
# write a script that reads a column of (x,y,z) coordinates from a
# .csv file and converts that to an .xyz format. You may choose anything
# you want for the header and particle type names.
# sample input data is coordinates.csv
# script should run from commandline as
# C:>python.exe readfile_test.py coordinates.csv
# output:
# C:>...output written to coordinates.xyz


# use this as input and output filenames
infilename = sys.argv[1]
outfilename = infilename.split(".")[0]+".xyz"

f = open(infilename,'r')
filedata = f.readlines()
f.close()

xyzdata = []
i=0
for line in filedata:
    strings = line.split(',')
    xyz = [i, float(strings[0]),float(strings[1]),float(strings[2])]
    xyzdata.append(xyz)
    i = i+1
    
writetoxyz(xyzdata, outfilename)
