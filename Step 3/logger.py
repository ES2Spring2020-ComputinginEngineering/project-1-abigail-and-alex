##################
# FILL IN HEADER
#################

import microbit as mb
import radio  # Needs to be imported separately

# Change the channel if other microbits are interfering. (Default=7)
radio.on()  # Turn on radio
radio.config(channel=2, length=100)

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
    time= microbit.running_time()
    X=microbit.accelerometer.get_x()
    Y=microbit.accelerometer.get_y()
    Z=microbit.accelerometer.get_z()
    message= str(time)+ str(X) +str(Y)+ str(Z)
    # Need to format into a single string
    # Send the string over the radio
    ######################################################

    radio.send(message)
    mb.sleep(10)



mb.display.show(mb.Image.SQUARE)  # Display Square when program ends