##################
# Names: Vicky Yang
#        Tessa Grasseschi
# Project 1, Part 3
# Logger
#################

import microbit as mb
import radio  # Needs to be imported separately
import math

# Change the channel if other microbits are interfering. (Default=7)
radio.on()  # Turn on radio
radio.config(channel=13, length=100)

print('Program Started')
mb.display.show(mb.Image.HAPPY)

while not mb.button_a.is_pressed():  # wait for button A to be pressed to begin logging
    mb.sleep(10)

radio.send('start') # Send the word 'start' to start the receiver
mb.sleep(1000)
mb.display.show(mb.Image.HEART)
# Display Heart while logging
mb.sleep(1000)


# Read and send accelerometer data repeatedly until button A is pressed again
message = ""
time0 = mb.running_time()
while not mb.button_a.is_pressed():
    ######################################################
    # FILL In HERE
    # Need to collect accelerometer and time measurements
    # Need to format into a single string
    # Send the string over the radio
    ######################################################
    mb.display.show(mb.Image.HOUSE, wait=False)
    acc_x = mb.accelerometer.get_x() #acceleration in the x-direction
    acc_y = mb.accelerometer.get_y() #acceleration in the y-direction
    acc_z = mb.accelerometer.get_z() #acceleration in the z-direction
    time1 = mb.running_time()
    elapsed_time = (time1 - time0)/1000
    message = str(elapsed_time) + ", " + str(acc_x) + ", " + str(acc_y) + ", " +  str(acc_z) + ","
    radio.send(message)
    mb.sleep(20)
mb.display.show(mb.Image.SQUARE)  # Display Square when program ends