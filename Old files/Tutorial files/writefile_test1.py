import math
import sys

# typeconversion_writefile_test.py
#
# for the assignment you need to write to so-called xyz files
# that can be read by many molecular visualization programs.
# See Wikipedia for the format.
#
# make a script that writes the positions (x,y,z) of three atoms/particles
# of type A B and C, to an xyz file, the filename being obtained from
# the commandline:
# C:>python typeconversion_writefile_test.py myparticles.xyz
# output:
# C:>...xyz file written to myparticles.xyz
A = ['A',1,2,3]
B = ['B',1,2,3]
C = ['C',2,3,4]

particles = [A,B,C]

def writetoxyz (particles, filename):
    f = open(filename,'w')
    f.write(str(len(particles))+'\n \n')
    for item in particles:
        f.write(str(item[0])+" "+str(item[1])+" "+str(item[2])+" "+str(item[3])+"\n")
    f.close()
