import math
import sys
import numpy as np
import random


# commandline arguments
#datfilename = sys.argv[1]
#trajfilename = sys.argv[3]

#Model Parameters
SpringConstant = 10
Mass = 1
Attraction = 3
ExclusionRadius = 0.75
EquilibriumDistance = 2
AttractionDistance = 3.5

#Simulation Parameters
Dt      = 0.00001    # stepsize for numerical integration of Newtons Equation
NSteps  = 200000    # number of steps of simulation
NSave   = 100       # save positions every NSave steps to .xyz file
NScreen = 10000      # print energies every NScreen steps on screen

# Generate points
numOfPoints = 4
boxSize = 20
# Positions = np.matrix([[round(random.uniform(0, boxSize),9) for j in range(3)] for i in range(numOfPoints)])
Positions = np.matrix([[0,0,0],[3,0,0],[3,3,0],[0,3,0]])
Velocities = np.zeros((numOfPoints,3))

# Bonded and nonbonded matrix
# in this case, a polymer A-B-C-D
Bonds = np.matrix([[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]])
Nonbonds = np.absolute(Bonds - 1) - np.identity(numOfPoints)

h = open("output.xyz",'w')

# Integrate Newtons Equation
for step in range(NSteps):
    Forces = np.zeros((numOfPoints,3))
    for particle_id in range(numOfPoints):
        
        PointUnit = [0] * numOfPoints
        PointUnit[particle_id] = 1
        PointUnit = np.matrix(PointUnit)
        Bonding = Bonds*np.transpose(PointUnit)
        Nonbonding = Nonbonds*np.transpose(PointUnit)
        
        for j in range(numOfPoints):
            # skip if it is not a pair (i =/= j)
            if particle_id == j:
                continue
            # calculate interparticle distance
            R_ij = (Positions[j]-Positions[particle_id])
            r_ij = np.linalg.norm(R_ij)
            R_ij = R_ij*(1/r_ij)
            # calculate non-bonding force by this interaction
            Forces[particle_id] = Forces[particle_id] + ( int(Nonbonding[j]) * Attraction * ( 6*(AttractionDistance/r_ij)**7 - 12*(AttractionDistance/r_ij)**13) ) * R_ij
            # calculate bonding force by this interaction
            Forces[particle_id] = Forces[particle_id] + ( int(Bonding[j]) * ( 12*(ExclusionRadius/r_ij)**13 + SpringConstant*r_ij ) ) * R_ij 
            
            
    # YOUR INTEGRATION PROCEDURE HERE
    Positions = Positions + Velocities*Dt
    Velocities = Velocities + Forces*Dt/Mass

    # print energies to screen
##    if (step%NScreen==0):
##        ukin = Ukin(v)
##        upot = Upot(r)
##        utot = ukin+upot
##        line = str(step)+", "+str(ukin)+", "+str(upot)+", "+str(utot)
##        print line
    
    # save coordinates and energies
    if (step%NSave==0):
        # ..to datfile
##        ukin = Ukin(v)
##        upot = Upot(r)
##        utot = ukin+upot
##        line = str(step)+", "+str(ukin)+", "+str(upot)+", "+str(utot)+"\n"
##        f.write(line)
        h.write(str(numOfPoints)+"\n"+str(step*Dt)+"\n")
        for particle_id in range(numOfPoints):
            these_positions = Positions[particle_id].tolist()
            these_positions = these_positions[0]
            h.write(str(particle_id+1)+" "+str(these_positions[0])+" "+str(these_positions[1])+" "+str(these_positions[2])+"\n")
        print step,"/",NSteps,"(",(round(100*step/NSteps)),"%)" 

h.close()
