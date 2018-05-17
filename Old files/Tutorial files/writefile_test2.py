import math
import sys

# writefile_test2.py
#
# for the final assignment you also need to write to .csv files
# that can be read by Excel.
#
# Start from your results from "functions_test.py"
# This time, do not print on the screen but send the data to a .csv file
# with a filename that you can specify in the script itself (so
# you can also run from within IDLE)

A = ['A',1,2,3]
B = ['B',1,2,3]
C = ['C',2,3,4]
sampleparticles = [A,B,C]

def writetocsv(particles, filename):
    f = open(filename,'w')
    for item in particles:
        f.write(str(item[0])+","+str(item[1])+","+str(item[2])+","+str(item[3])+"\n")
    f.close()    

