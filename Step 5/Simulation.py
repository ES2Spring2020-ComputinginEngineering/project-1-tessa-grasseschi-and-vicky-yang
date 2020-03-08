"""
Project 1, Part 5
Simulation
Name(s): Vicky Yang & Tessa Grasseschi
"""

# IMPORT STATEMENTS
import numpy as np

# CUSTOM FUNCTIONS
def update_system(L,acc,vel,pos):
    dt = 0.1
    accNext = ((-9.8)/L)*(np.sin(pos))
    posNext = pos+vel*dt
    velNext = vel+acc*dt
    return posNext, velNext, accNext, dt

# MAIN SCRIPT

# Initializing
# make sure in radians
# pos = angle
# all values are angular, dealing with circular motion

#L = [0.2540, 0.3048, 0.3556, 0.4064, 0.4572]
L = 0.2540
t0 = 0
acc0 = 0
vel0 = 0
pos0 = 45

time = [t0]
acc = [acc0]
vel = [vel0]
pos = [pos0]

#x = update_system(L,acc0,vel0,pos0)
#i = 1
#for element in time:
#    if element < 20:
#        posNext, velNext = update_system(0.2540, acc[i], vel[i-1], pos[i-1])
#        pos.append(posNext)
#        vel.append(velNext)
