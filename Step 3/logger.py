##################
# FILL IN HEADER
#################

import microbit as mb
import radio  # Needs to be imported separately

# Change the channel if other microbits are interfering. (Default=7)
radio.on()  # Turn on radio
radio.config(channel=7, length=100)

print('Program Started')
mb.display.show(mb.Image.HAPPY)

while not mb.button_a.is_pressed():  # wait for button A to be pressed to begin logging
    mb.sleep(10)

radio.send('start') # Send the word 'start' to start the receiver
mb.sleep(1000)
mb.display.show(mb.Image.HEART)  # Display Heart while logging


# Read and send accelerometer data repeatedly until button A is pressed again
while not mb.button_a.is_pressed():
    ######################################################
    # FILL In HERE
    # Need to collect accelerometer and time measurements
    # Need to format into a single string
    # Send the string over the radio
    ######################################################
    acc_x = microbit.accelerometer.get_x() #acceleration in the x-direction
    acc_y = microbit.accelerometer.get_y() #acceleration in the y-direction
    acc_z = microbit.accelerometer.get_z() #acceleration in the z-direction
    while True:
        time0 = microbit.running_time()
        while not microbit.button_a.is_pressed():#waiting loop
            microbit.display.show(microbit.Image.HAPPY)
        while microbit.button_a.is_pressed(): #timing loop
            microbit.display.show(microbit.Image.CLOCK1)
            time1 = microbit.running_time()
        time1 = microbit.running_time()
        elapsed_time = (time1 - time0)/1000

    radio.send(message)
    mb.sleep(10)



mb.display.show(mb.Image.SQUARE)  # Display Square when program ends