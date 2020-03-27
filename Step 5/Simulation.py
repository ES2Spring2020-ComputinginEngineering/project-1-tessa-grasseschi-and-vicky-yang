"""
Project 1, Part 5
Simulation
Name(s): Vicky Yang & Tessa Grasseschi
"""

# IMPORT STATEMENTS
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import statistics

#global variables
num_samples = 100000

# CUSTOM FUNCTIONS
def update_system(L,acc,vel,pos,t):
    dt = 0.001
    tNext=t+dt
    accNext = ((-9.81)/L)*(np.sin((pos*np.pi)/180))
    velNext = vel+acc*dt
    posNext = pos+vel*dt
    return posNext, velNext, accNext, tNext

# MAIN SCRIPT
sim_state = np.zeros((num_samples,4))
# Initializing
# make sure in radians
# pos = angle
# all values are angular, dealing with circular motion

#L = [0.2540, 0.3048, 0.3556, 0.4064, 0.4572]
L1 = 0.2540
L2 = 0.3048
L3 = 0.3556
L4 = 0.4064
L5 = 0.4572

sim_state[0,0] = 0 #time
sim_state[0,1] = 0 #accel
sim_state[0,2] = 0 #v
sim_state[0,3] = 70 #pos

for i in range(num_samples-1):
     posNext, velNext, accNext, tNext = update_system(L1, sim_state[i,1], sim_state[i,2], sim_state[i,3],sim_state[i,0])
     sim_state[i+1,0] = tNext #time
     sim_state[i+1,1] = accNext #accel
     sim_state[i+1,2] = velNext #v
     sim_state[i+1,3] = posNext #pos
     
plt.plot(sim_state[:,0],sim_state[:,3])
plt.show()

peak_10 = sig.find_peaks(sim_state[:,3], distance=11)
peak_10_times = []
for index in peak_10[0]:
   time = sim_state[index,0]
   peak_10_times.append(time)
period_10 = []
for i in range(len(peak_10_times)-1):
    time_difference = peak_10_times[i+1] - peak_10_times[i]
    period_10.append(time_difference)
peak_10_mean = statistics.mean(period_10)
plt.figure()
plt.subplot(3, 1, 1)
plt.plot(sim_state[:,0], sim_state[:,3], 'r-', sim_state[peak_10[0],0], sim_state[peak_10[0],3], 'b.')
plt.title('Angular Position, Velocity, & Acceleration of 10-inch Pendulum')
plt.ylabel('Position')
plt.subplot(3, 1, 2)
plt.plot(sim_state[:,0], sim_state[:,1], 'g-')
plt.ylabel('Acceleration')
plt.subplot(3, 1, 3)
plt.plot(sim_state[:,0], sim_state[:,2], 'y-')
plt.ylabel('Velocity')
plt.xlabel('Time (s)')
plt.show()










