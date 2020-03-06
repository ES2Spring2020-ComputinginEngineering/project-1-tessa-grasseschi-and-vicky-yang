# -*- coding: utf-8 -*-
"""
Project 1, Part 4
Data Analysis
Name(s): Tessa Grasseschi & Vicky Yang

"""

# IMPORT STATEMENTS
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
# CUSTOM FUNCTIONS
def find_file_length(file):
# Purpose is to find the length of the file so the we can create the array
# knowing how many rows to create it with.
# This function takes one parameter, which is the file where the data is in.
# This function returns the number of lines in the number of lines in the file.
    ln = 0
    for i in file:
        ln += 1
    return ln

def arrays_for_acc_time_graphs(file):
# The purpose of this function is to create an array with zeros
# and correct dimensions. Then, the function parses the data and replaces 
# the zeros in the arrays with their corresponding data.
# This function takes one parameter, which is the file where the data is in.
# This function returns the numpy array with the data from the files.
    a = find_file_length(file) #calling previous function
    data = np.zeros((a//2, 4)) #creating array with zeros

    file.seek(0) #reset to read starting from the beginning of file

    counter = 0
    for ln in file:
        separate = ln.strip().split(",")
        if len(separate) != 1:
            time = float(separate[0].strip())
            x_acc = float(separate[1].strip())
            y_acc = float(separate[2].strip())
            z_acc = float(separate[3].strip())
            data[counter, 0]=time
            data[counter, 1]=x_acc
            data[counter, 2]=y_acc
            data[counter, 3]=z_acc
            counter += 1
    return data

def find_tilt_x(acc_x, acc_y, acc_z):
#This function calculates and returns the angle of the tilt in the x direction
#Takes three parameters: acceleration in the x-direction, acceleration in the y-direction, acceleration in the z-direction
#Returns tilt_x (x-angle)
    y = np.sqrt((acc_y)**2+(acc_z**2))
    x = acc_x
    tilt_x = np.arctan2(x,y)
    x_angle = (tilt_x *57.29) - 90
    return x_angle # in degrees

def find_tilt_y(acc_x, acc_y, acc_z):
#This function calculates and returns the angle of the tilt in the y direction
#Takes three parameters: acceleration in the x-direction, acceleration in the y-direction, acceleration in the z-direction
#Returns tilt_y (y-angle)
    y = np.sqrt(((acc_x)**2)+((acc_z**2)))
    x = acc_y
    tilt_y = np.arctan2(x,y)
    y_angle = (tilt_y * 57.29)
    return y_angle # in degrees

def pendulum(lengths, acceleration):
# This function calculates the period of the pendulum with the actual data
# This function takes one parameter, which is acceleration
# This function returns an array of the periods of the pendulum
    period = 2*np.pi*np.sqrt(lengths/acceleration)
    return period

# MAIN SCRIPT
    
# opening data files
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

theta_filt_10 = sig.medfilt(x_angle_10_in)
peak_10 = sig.find_peaks(theta_filt_10)
peak_10_times = []
for index in peak_10[0]:
   # if peak_10[0[index]] in theta_filt_10:
   time = data1[index+50,0]
   peak_10_times.append(time)


#SAVE FOR NOW 
#so find_peaks returns a list/array(?) of the indexes
    #then withing each index there are four numbers (time and 3 accel)
    #so within that index, we just want the first index (0)
    #I got that to work with just looking at the data 
    #but I couldn't get a working loop 
    
#so for this, I printed all of the indices it returns 
    #because my window isn't showing anything so I gotta print
#the first index it gave is 11, which is index 11 in data 1
    #so then i printed that index from data 1 to see what happened
    #and it gave back time, accel, accel, accel
    #so then I took the zero-eth index of the 11th index and got back that time
    #but I just can't make it into a loop because i try something like
        #peak_10 = sig.find peaks(y_angle_10_in)
        #x = data1[peak_10, 0] 
        #because I want to take the index from the returned list from find_peaks
        #and then take the that index from data1
        #and then get the time from that index
        #but it won't work because peak_10 isn't an number
        
    #so when we use find_peaks, we get back either a list or array of indices
    #then we need to take each index from that list (peak_10) and 
    #get the corresponding data from data1
    #then we need the 0=eth index of that data which will be the time
    
#print(sig.find_peaks(y_angle_10_in))
#print(data1[11])
#print(data1[11,0])





        
#length = np.array([0.2540, 0.3048, 0.3556, 0.4064, 0.4572]) #in meters
# Accelerations from actual data (in m/s^2)
#acceleration1 = (np.sqrt(data1[50:390, 1]**2 + data1[50:390, 2]**2 + data1[50:390, 3]**2)/1000)*9.8
#acceleration2 = (np.sqrt(data2[:425, 1]**2 + data2[:425, 2]**2 + data2[:425, 3]**2)/1000)*9.8
#acceleration3 = (np.sqrt(data3[25:340, 1]**2 + data3[25:340, 2]**2 + data3[25:340, 3]**2)/1000)*9.8
#acceleration4 = (np.sqrt(data4[30:460, 1]**2 + data4[30:460, 2]**2 + data4[30:460, 3]**2)/1000)*9.8
#acceleration5 = (np.sqrt(data5[10:465, 1]**2 + data5[10:465, 2]**2 + data5[10:465, 3]**2)/1000)*9.8

#x_filt = sig.medfilt(data1[50:390,:])
#x_pks = sig.find_peaks(data1)
#plt.plot(x_pks, 'r-')
#plt.show()


#period1 = sum(pendulum(0.2540, acceleration1))/340
#period2 = sum(pendulum(0.3048, acceleration2))/425
#period3 = sum(pendulum(0.3556, acceleration3))/315
#period4 = sum(pendulum(0.4064, acceleration4))/430
#period5 = sum(pendulum(0.4572, acceleration5))/455
#period = np.array([period1, period2, period3, period4, period5])
#
## Period vs. Length Graph for All Lengths
#plt.plot(length, period, "o-")
#plt.title("Period vs. Length")
#plt.ylabel("Period(s)")
#plt.xlabel("Length(m)")
#plt.show()