# -*- coding: utf-8 -*-
"""
Project 1, Part 4
Data Analysis
Name(s): Tessa Grasseschi & Vicky Yang

"""

# IMPORT STATEMENTS
from Data_analysis_functions import *

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import statistics

# MAIN SCRIPT

# opening data files (sample files in the Step 4 folder)
data1_10in = open("Pendulum 10 inches Trial 1.csv")
data2_12in = open("Pendulum 12 inches Trial 2.csv")
data3_14in = open("Pendulum 14 inches Trial 1.csv")
data4_16in = open("Pendulum 16 inches Trial 1.csv")
data5_18in = open("Pendulum 18 inches Trial 1.csv")

# Acceleration vs. Time Graph for 10 inches
data1 = arrays_for_acc_time_graphs(data1_10in)
plt.plot(data1[50:390, 0], data1[50:390, 1], 'r-', data1[50:390, 0], data1[50:390, 2], 'b-')
plt.title('Acceleration vs. Time for 10-inch Pendulum Length')
plt.ylabel('Acceleration (milli-G)')
plt.xlabel('Time(s)')
plt.show()

# Acceleration vs. Time Graph for 12 inches
data2 = arrays_for_acc_time_graphs(data2_12in)
plt.plot(data2[:425, 0], data2[:425, 1], 'r-', data2[:425, 0], data2[:425, 2], 'b-')
plt.title('Acceleration vs. Time for 12-inch Pendulum Length')
plt.ylabel('Acceleration (milli-G)')
plt.xlabel('Time(s)')
plt.show()

# Acceleration vs. Time Graph for 14 inches
data3 = arrays_for_acc_time_graphs(data3_14in)
plt.plot(data3[25:340, 0], data3[25:340, 1], 'r-', data3[25:340, 0], data3[25:340, 2], 'b-')
plt.title('Acceleration vs. Time for 14-inch Pendulum Length')
plt.ylabel('Acceleration (milli-G)')
plt.xlabel('Time(s)')
plt.show()

# Acceleration vs. Time Graph for 16 inches
data4 = arrays_for_acc_time_graphs(data4_16in)
plt.plot(data4[30:460, 0], data4[30:460, 1], 'r-', data4[30:460, 0], data4[30:460, 2], 'b-')
plt.title('Acceleration vs. Time for 16-inch Pendulum Length')
plt.ylabel('Acceleration (milli-G)')
plt.xlabel('Time(s)')
plt.show()

# Acceleration vs. Time Graph for 18 inches
data5 = arrays_for_acc_time_graphs(data5_18in)
plt.plot(data5[10:465, 0], data5[10:465, 1], 'r-', data5[10:465, 0], data5[10:465, 2], 'b-')
plt.title('Acceleration vs. Time for 18-inch Pendulum Length')
plt.ylabel('Acceleration (milli-G)')
plt.xlabel('Time(s)')
plt.show()

data1_10in.close()
data2_12in.close()
data3_14in.close()
data4_16in.close()
data5_18in.close()

# FINDING ANGLE OF THE PENDULUM

# Theta vs. Time Graph for 10 inches
x_angle_10_in = find_tilt_x(data1[50:390,1], data1[50:390, 2], data1[50:390,3])
y_angle_10_in = find_tilt_y(data1[50:390,1], data1[50:390, 2], data1[50:390,3])
plt.plot(data1[50:390,0], x_angle_10_in, 'r-', data1[50:390, 0], y_angle_10_in, 'b-')
plt.title('Theta vs. Time for 10-inch Pendulum Length')
plt.ylabel('Theta(degrees)')
plt.xlabel('Time (s)')
plt.show()

# Theta vs. Time Graph for 12 inches
x_angle_12_in = find_tilt_x(data2[:425, 1], data2[:425, 2], data2[:425,3])
y_angle_12_in = find_tilt_y(data2[:425, 1], data2[:425, 2], data2[:425,3])
plt.plot(data2[:425,0], x_angle_12_in, 'r-', data2[:425, 0], y_angle_12_in, 'b-')
plt.title('Theta vs. Time for 12-inch Pendulum Length')
plt.ylabel('Theta(degrees)')
plt.xlabel('Time (s)')
plt.show()

# Theta vs. Time Graph for 14 inches
x_angle_14_in = find_tilt_x(data3[25:340, 1], data3[25:340, 2], data3[25:340,3])
y_angle_14_in = find_tilt_y(data3[25:340, 1], data3[25:340, 2], data3[25:340,3])
plt.plot(data3[25:340,0], x_angle_14_in, 'r-', data3[25:340, 0], y_angle_14_in, 'b-')
plt.title('Theta vs. Time for 14-inch Pendulum Length')
plt.ylabel('Theta(degrees)')
plt.xlabel('Time (s)')
plt.show()

# Theta vs.Time Graph for 16 inches 
x_angle_16_in = find_tilt_x(data4[30:460, 1], data4[30:460, 2], data4[30:460, 3])
y_angle_16_in = find_tilt_y(data4[30:460, 1], data4[30:460, 2], data4[30:460, 3])
plt.plot(data4[30:460, 0], x_angle_16_in, 'r-', data4[30:460,0], y_angle_16_in, 'b-')
plt.title('Theta vs. Time for 16-inch Pendulum Length')
plt.ylabel('Theta(degrees)')
plt.xlabel('Time (s)')
plt.show()

#Theta vs. Time Graph for 18 inches 
x_angle_18_in = find_tilt_x(data5[10:465, 1], data5[10:465, 2], data5[10:465, 3])
y_angle_18_in = find_tilt_y(data5[10:465, 1], data5[10:465, 2], data5[10:465, 3])
plt.plot(data5[10:465, 0], x_angle_18_in, 'r-', data5[10:465,0], y_angle_18_in, 'b-')
plt.title('Theta vs. Time for 18-inch Pendulum Length')
plt.ylabel('Theta(degrees)')
plt.xlabel('Time (s)')
plt.show()


# FINDING PERIOD OF A PENDULUM

# period of 10 inch length
theta_filt_10 = sig.medfilt(x_angle_10_in, 9)
peak_10 = sig.find_peaks(theta_filt_10, distance=11)
peak_10_times = []
for index in peak_10[0]:
   time = data1[index+50,0]
   peak_10_times.append(time)
period_10 = []
for i in range(len(peak_10_times)-1):
    time_difference = peak_10_times[i+1] - peak_10_times[i]
    period_10.append(time_difference)
peak_10_mean = statistics.mean(period_10)

plt.plot(data1[50:390,0], theta_filt_10[:], 'r-', data1[peak_10[0],0], theta_filt_10[peak_10[0]], 'b.')
plt.title('Theta vs. Time for 10 inch Pendulum with Peaks')
plt.ylabel('Theta (degrees)')
plt.xlabel('Time (s)')
plt.show()

# period of 12 inch length
theta_filt_12 = sig.medfilt(x_angle_12_in, 9)
peak_12 = sig.find_peaks(theta_filt_12, distance=10)
peak_12_times = []
for index in peak_12[0]:
   time2 = data2[index,0]
   peak_12_times.append(time2)
period_12 = []
for i in range(len(peak_12_times)-1):
    time_difference2 = peak_12_times[i+1] - peak_12_times[i]
    period_12.append(time_difference2)
peak_12_mean = statistics.mean(period_12)

plt.plot(data2[:425,0], theta_filt_12[:], 'r-', data2[peak_12[0],0], theta_filt_12[peak_12[0]], 'b.')
plt.title('Theta vs. Time for 12 inch Pendulum with Peaks')
plt.ylabel('Theta (degrees)')
plt.xlabel('Time (s)')
plt.show()

# period of 14 inch length
theta_filt_14 = sig.medfilt(x_angle_14_in, 9)
peak_14 = sig.find_peaks(theta_filt_14, distance=11)
peak_14_times = []
for index in peak_14[0]:
   time3 = data3[index+25,0]
   peak_14_times.append(time3)
period_14 = []
for i in range(len(peak_14_times)-1):
    time_difference3 = peak_14_times[i+1] - peak_14_times[i]
    period_14.append(time_difference3)
peak_14_mean = statistics.mean(period_14)

plt.plot(data3[25:340,0], theta_filt_14[:], 'r-', data3[peak_14[0],0], theta_filt_14[peak_14[0]], 'b.')
plt.title('Theta vs. Time for 14 inch Pendulum with Peaks')
plt.ylabel('Theta (degrees)')
plt.xlabel('Time (s)')
plt.show()

# period of 16 inch length
theta_filt_16 = sig.medfilt(x_angle_16_in,11)
peak_16 = sig.find_peaks(theta_filt_16, distance=11)
peak_16_times = []
for index in peak_16[0]:
   time4 = data4[index+30,0]
   peak_16_times.append(time4)
period_16 = []
for i in range(len(peak_16_times)-1):
    time_difference4 = peak_16_times[i+1] - peak_16_times[i]
    period_16.append(time_difference4)
peak_16_mean = statistics.mean(period_16)

plt.plot(data4[30:460,0], theta_filt_16[:], 'r-', data4[peak_16[0],0], theta_filt_16[peak_16[0]], 'b.')
plt.title('Theta vs. Time for 16 inch Pendulum with Peaks')
plt.ylabel('Theta (degrees)')
plt.xlabel('Time (s)')
plt.show()

# period 18 inch length
theta_filt_18 = sig.medfilt(x_angle_18_in, 11)
peak_18 = sig.find_peaks(theta_filt_18, distance=10)
peak_18_times = []
for index in peak_18[0]:
   time5 = data5[index+10,0]
   peak_18_times.append(time5)
period_18 = []
for i in range(len(peak_18_times)-1):
    time_difference5 = peak_18_times[i+1] - peak_18_times[i]
    period_18.append(time_difference5)
peak_18_mean = statistics.mean(period_18)

plt.plot(data5[10:465,0], theta_filt_18[:], 'r-', data5[peak_18[0],0], theta_filt_18[peak_18[0]], 'b.')
plt.title('Theta vs. Time for 18 inch Pendulum with Peaks')
plt.ylabel('Theta (degrees)')
plt.xlabel('Time (s)')
plt.show()

# Period vs. Length for Pendulum
length = np.array([0.2540, 0.3048, 0.3556, 0.4064, 0.4572]) #in meters
plt.plot(length, [peak_10_mean, peak_12_mean, peak_14_mean, peak_16_mean, peak_18_mean], 'ro')
plt.title('Period vs. Length of Pendulum')
plt.ylabel('Period (s)')
plt.xlabel('Length (m)')
plt.show()