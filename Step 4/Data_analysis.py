# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 13:44:48 2020

@author: Yang
"""
import numpy as np
import matplotlib.pyplot as plt

def find_file_length(file):
    ln = 0
    for i in file:
        ln += 1
    return ln

data1_10in = open("Pendulum 10 inches Trial 1.csv")
data2_12in = open("Pendulum 12 inches Trial 1.csv")
data3_14in = open("Pendulum 14 inches Trial 1.csv")
data4_16in = open("Pendulum 16 inches Trial 1.csv")
data5_18in = open("Pendulum 18 inches Trial 1.csv")

x = find_file_length(data1_10in)
data1 = np.zeros((x//2, 4))

data1_10in.seek(0)

counter = 0
for ln in data1_10in:
    separate = ln.strip().split(",")
    print(separate)
    if len(separate) != 1:
        time = float(separate[0].strip())
        x_acc = float(separate[1].strip())
        y_acc = float(separate[2].strip())
        z_acc = float(separate[3].strip())
        data1[counter, 0]=time
        data1[counter, 1]=x_acc
        data1[counter, 2]=y_acc
        data1[counter, 3]=z_acc
        counter += 1

plt.plot(data1[50:400, 0], data1[50:400, 1], 'r-')
plt.show()