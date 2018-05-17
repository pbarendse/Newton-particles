# newton_intermediate.py
#
# complete the code below, where indicated
# LEVEL: EASY
# - write part of energy functions
# - write part of update equation

import math
import sys

# commandline arguments
infilename = sys.argv[1]
datfilename = sys.argv[2]
trajfilename = sys.argv[3]

# two particles, center is fixed.
rcenter = [0.0,0.0,0.0]
r = [0.0,0.0,0.0]
v = [0.0,0.0,0.0]

#Model Parameters
SpringConstant0 = 10
Mass = 1

#Simulation Parameters
Dt      = 0.00005    # stepsize for numerical integration of Newtons Equation
NSteps  = 1000000    # number of steps of simulation
NSave   = 10       # save positions every NSave steps to .xyz file
NScreen = 1000      # print energies every NScreen steps on screen

#Read input
f = open(infilename,'r')
lines = f.readlines()
f.close()

# get (x,y,z) from line 1 (index 0)
items = lines[0].split(",")
x = float(items[0])
y = float(items[1])
z = float(items[2])
r = [x,y,z]

# get (vx,vy,vz) from line 2 (index 1)
vparticle = [0.0,0.0,0.0] 
items = lines[1].split(",")
vx = float(items[0])
vy = float(items[1])
vz = float(items[2])
v = [vx,vy,vz]


def Upot(r): 
    # Potential energy (input: list r=[x,y,z], output: scalar)
    x = r[0]
    y = r[1]
    z = r[2]
    rsq = x*x+y*y+z*z
    E = 0.5*SpringConstant0*rsq
    return E

def Ukin(v):
    # Kinetic energy (input: list v = [vx,vy,vz], output: scalar)
    vx = v[0]
    vy = v[1]
    vz = v[2]
    vsq = vx*vx+vy*vy+vz*vz
    E = 0.5*Mass*vsq
    return E
   
#open data file 
f = open(datfilename,'w')
header = "step, ukin, upot,utot\n"
f.write(header)

# open trajectory file
g = open(trajfilename,'w')
h = open("output.xyz",'w')

# header on screen
print "starting run"
print "step, ukin, upot, utot \n"

# Integrate Newtons Equation
for step in range(NSteps):
    
    # YOUR INTEGRATION PROCEDURE HERE
    SpringConstant = SpringConstant0 + (step/NSteps)*400000
    Fx = -SpringConstant*r[0]
    Fy = -SpringConstant*r[1]
    Fz = -SpringConstant*r[2]
    r[0] = r[0] + v[0]*Dt
    r[1] = r[1] + v[1]*Dt
    r[2] = r[2] + v[2]*Dt
    v[0] = v[0] + Fx*Dt/Mass 
    v[1] = v[1] + Fy*Dt/Mass
    v[2] = v[2] + Fz*Dt/Mass

    # print energies to screen
    if (step%NScreen==0):
        ukin = Ukin(v)
        upot = Upot(r)
        utot = ukin+upot
        line = str(step)+", "+str(ukin)+", "+str(upot)+", "+str(utot)
        print line
    
    # save coordinates and energies
    if (step%NSave==0):
        # ..to datfile
        ukin = Ukin(v)
        upot = Upot(r)
        utot = ukin+upot
        line = str(step)+", "+str(ukin)+", "+str(upot)+", "+str(utot)+"\n"
        f.write(line)
        # ...to trajfile
        center_coord_line = "center 0.0  0.0  0.0\n"
        particle_coord_line = "particle "+str(r[0])+"  "+str(r[1])+"  "+str(r[2])+"\n"
        npart = 2
        g.write(str(npart)+"\n")
        g.write("step "+str(step)+"\n")
        g.write(center_coord_line)
        g.write(particle_coord_line)
        h.write(str(npart)+"\n \n")
        h.write("1 "+str(0)+" "+str(0)+" "+str(0)+"\n")
        h.write("2 "+str(r[0])+" "+str(r[1])+" "+str(r[2])+"\n")

f.close()
g.close()
h.close()

print "done ...."
print "...trajectory saved to ", trajfilename
print "...energy data savd to ",datfilename

