# Project 1, Part 2
# Theorectical Period of the Pendulum
# Name(s): Tessa Grasseschi and Vicky Yang

import numpy as np
import matplotlib.pyplot as plt

def pendulum(lengths):
# This function calculates the period of the pendulum with the theorectical information
# This function takes one parameter, which is the length
# This function returns the period of the pendulum
    period = 2*np.pi*np.sqrt(lengths/9.80)
    return period

arr1d = np.array([0.2540, 0.3048, 0.3556, 0.4064, 0.4572]) #in meters
period = pendulum(arr1d)

plt.plot(arr1d, period)
plt.ylabel("Period (seconds)")
plt.xlabel("Length (meters)")
plt.title("Period vs. Length of a Pendulum")
plt.show()