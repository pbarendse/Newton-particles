import math
import sys

A = ['A',1,2,3]
B = ['B',1,2,3]
C = ['C',2,3,4]
sampleparticles = [A,B,C]

def writetoxyz (particles, filename):
    f = open(filename,'w')
    f.write(str(len(particles))+'\n \n')
    for item in particles:
        f.write(str(item[0])+" "+str(item[1])+" "+str(item[2])+" "+str(item[3])+"\n")
    f.close()

def writetocsv(particles, filename):
    f = open(filename,'w')
    for item in particles:
        f.write(str(item[0])+","+str(item[1])+","+str(item[2])+","+str(item[3])+"\n")
    f.close()    
