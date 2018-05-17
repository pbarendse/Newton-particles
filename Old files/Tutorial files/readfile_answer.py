import math
import sys

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

f= open(infilename,'r')
lines=f.readlines()
f.close()

coordinates=[]
for line in lines:
    items=line.split(",")
    x=float(items[0])
    y=float(items[1])
    z=float(items[2])
    coordinates.append([x,y,z])

f=open(outfilename,'w')
f.write(str(len(coordinates))+"\n")
f.write("bla \n")
for c in coordinates:
    f.write("particle "+str(c[0])+" "+str(c[1])+" "+str(c[2])+"\n")
f.close()

print "...output written to ", outfilename
