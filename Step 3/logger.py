##################
# FILL IN HEADER
#################

import microbit as mb
import radio  # Needs to be imported separately
import math

# Change the channel if other microbits are interfering. (Default=7)
radio.on()  # Turn on radio
radio.config(channel=7, length=100)

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
while not mb.button_a.is_pressed():
    ######################################################
    # FILL In HERE
    # Need to collect accelerometer and time measurements
    # Need to format into a single string
    # Send the string over the radio
    ######################################################
    #for i in range(1000):
    #time0 = mb.running_time()
    mb.display.show(mb.Image.ALL_ARROWS)
    acc_x = mb.accelerometer.get_x() #acceleration in the x-direction
    acc_y = mb.accelerometer.get_y() #acceleration in the y-direction
    acc_z = mb.accelerometer.get_z() #acceleration in the z-direction
    # acceleration = math.sqrt(acc_x**2 + acc_y**2 + acc_z**2)
    # while mb.button_a.is_pressed(): #timing loop
#         mb.display.show(mb.Image.CLOCK1)
#         time1 = mb.running_time()
#     time1 = mb.running_time()
#     elapsed_time = (time1 - time0)/1000
    message = " x: " + str(acc_x) + " y: " + str(acc_y) + " z: " + str(acc_z)
    radio.send(message)
    mb.sleep(100)



mb.display.show(mb.Image.SQUARE)  # Display Square when program ends