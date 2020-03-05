# -*- coding: utf-8 -*-
"""
Project 1, Part 4
Data Analysis Functions
Name(s): Tessa Grasseschi & Vicky Yang
"""

#CUSTOM FUNCTIONS

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
    tilt_x = np.arctan(x,y)
    x_angle = (tilt_x *57.29) - 90
    return x_angle # in degrees

def find_tilt_y(acc_x, acc_y, acc_z):
#This function calculates and returns the angle of the tilt in the y direction
#Takes three parameters: acceleration in the x-direction, acceleration in the y-direction, acceleration in the z-direction
#Returns tilt_y (y-angle)
    y = np.sqrt(((acc_x)**2)+((acc_z**2)))
    x = acc_y
    tilt_y = np.arctan(x,y)
    y_angle = (tilt_y * 57.29)
    return y_angle # in degrees

def pendulum(lengths, acceleration):
# This function calculates the period of the pendulum with the actual data
# This function takes one parameter, which is acceleration
# This function returns an array of the periods of the pendulum
    period = 2*np.pi*np.sqrt(lengths/acceleration)
    return period