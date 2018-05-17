# newton_intermediate.py
#
# complete the code below, where indicated
# LEVEL: ADVANCED
# - write complete energy functions
# - write complete update equation
# - write input
# - write output

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
SpringConstant = 10
Mass = 1

#Simulation Parameters
Dt      = 0.005    # stepsize for numerical integration of Newtons Equation
NSteps  = 10000    # number of steps of simulation
NSave   = 10       # save positions every NSave steps to .xyz file
NScreen = 1000     # print energies every NScreen steps on screen

#Read input
f = open(infilename,'r')
lines = f.readlines()
f.close()

# get r & v from input file
r = [0.0,0.0,0.0] # << YOUR CODE HERE
v = [0.0,0.0,0.0] # << YOUR CODE HERE

def Upot(r): 
    # Potential energy (input: list r=[x,y,z], output: scalar)
    E = 0.0 # << YOUR CODE HERE
    return E

def Ukin(v):
    # Kinetic energy (input: list v = [vx,vy,vz], output: scalar)
    E = 0.0 # << YOUR CODE HERE
    return E
   
#open data file 
f = open(datfilename,'w')
header = "step, ukin, upot,utot\n"
f.write(header)

# open trajectory file
g = open(trajfilename,'w')

# header on screen
print "starting run"
print "step, ukin, upot, utot \n"

# Integrate Newtons Equation
for step in range(NSteps):
    
    # YOUR INTEGRATION PROCEDURE HERE
    # WHAT ARE r AND v AFTER TIMESTEP Dt ?
    # UPDATE r AND v COMPONENT-WISE
    # eg r[0] = r[0]+ ... 

    # print energies to screen
    if (step%NScreen==0):
        print ""
    
    # save coordinates and energies
    if (step%NSave==0):
        # ..energies to datfile (.csv, terminate line with newline char '\n')
        line = ""
        f.write(line)
        # ...coordinates to trajfile (.xyz, terminate each line with newline character '\n')
        # four lines per step:
        # 1. number of particles
        # 2. scene header
        # 3. particletype + coordinates center (fixed)
        # 4. particletype + coordinates particle
        g.write("\n") # << YOUR CODE HERE
        g.write("\n") # << YOUR CODE HERE
        g.write("\n") # << YOUR CODE HERE
        g.write("\n") # << YOUR CODE HERE
        
f.close()
g.close()

print "done ...."
print "...trajectory saved to ", trajfilename
print "...energy data saved to ",datfilename

