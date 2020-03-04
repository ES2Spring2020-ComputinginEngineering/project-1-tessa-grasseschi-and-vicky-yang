# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 13:44:48 2020

@author: Yang
"""
import numpy as np
import matplotlib.pyplot as plt

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

data1_10in = open("Pendulum 10 inches Trial 1.csv")
data2_12in = open("Pendulum 12 inches Trial 2.csv")
data3_14in = open("Pendulum 14 inches Trial 1.csv")
data4_16in = open("Pendulum 16 inches Trial 1.csv")
data5_18in = open("Pendulum 18 inches Trial 1.csv")

#Acceleration vs. Time Graph for 10 inches
data1 = arrays_for_acc_time_graphs(data1_10in)
plt.plot(data1[50:390, 0], data1[50:390, 1], 'r-', data1[50:390, 0], data1[50:390, 2], 'b-')
plt.title('Acceleration vs. Time for 10-inch Pendulum Length')
plt.ylabel('Acceleration')
plt.xlabel('Time(s)')
plt.show()

#Acceleration vs. Time Graph for 12 inches
data2 = arrays_for_acc_time_graphs(data2_12in)
plt.plot(data2[:425, 0], data2[:425, 1], 'r-', data2[:425, 0], data2[:425, 2], 'b-')
plt.title('Acceleration vs. Time for 12-inch Pendulum Length')
plt.ylabel('Acceleration')
plt.xlabel('Time(s)')
plt.show()

#Acceleration vs. Time Graph for 14 inches
data3 = arrays_for_acc_time_graphs(data3_14in)
plt.plot(data3[25:340, 0], data3[25:340, 1], 'r-', data3[25:340, 0], data3[25:340, 2], 'b-')
plt.title('Acceleration vs. Time for 14-inch Pendulum Length')
plt.ylabel('Acceleration')
plt.xlabel('Time(s)')
plt.show()

#Acceleration vs. Time Graph for 16 inches
data4 = arrays_for_acc_time_graphs(data4_16in)
plt.plot(data4[30:460, 0], data4[30:460, 1], 'r-', data4[30:460, 0], data4[30:460, 2], 'b-')
plt.title('Acceleration vs. Time for 16-inch Pendulum Length')
plt.ylabel('Acceleration')
plt.xlabel('Time(s)')
plt.show()

#Acceleration vs. Time Graph for 18 inches
data5 = arrays_for_acc_time_graphs(data5_18in)
plt.plot(data5[10:465, 0], data5[10:465, 1], 'r-', data5[10:465, 0], data5[10:465, 2], 'b-')
plt.title('Acceleration vs. Time for 18-inch Pendulum Length')
plt.ylabel('Acceleration')
plt.xlabel('Time(s)')
plt.show()