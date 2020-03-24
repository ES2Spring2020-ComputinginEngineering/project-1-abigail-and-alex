# Project 1 --- ES2
# Step 3: Collection of Real World Data: Logger Code

#*****************************************
#
# YOUR NAMES:Abigail Imiolek and Alex Bayzk
#
#*****************************************

# IMPORT STATEMENTS
import microbit as mb
import radio


# MAIN SCRIPT
radio.on()  #Turn on radio
radio.config(channel=2, length=100)

print('Program Started')
mb.display.show(mb.Image.HAPPY) #Displays a happy face before logging

while not mb.button_a.is_pressed():  #Wait for button A to be pressed to begin logging
    mb.sleep(10)

radio.send('start') #Send the word 'start' to start the receiver
mb.sleep(1000)
mb.display.show(mb.Image.HEART)  #Display Heart while logging


# Read and send accelerometer data repeatedly until button A is pressed again
while not mb.button_a.is_pressed():
    ######################################################
    # Collect accelerometer and time measurements
    #Formats into a single string
    time= mb.running_time()
    X=mb.accelerometer.get_x()
    Y=mb.accelerometer.get_y()
    Z=mb.accelerometer.get_z()
    message= str(time)+ " "+str(X)+ " " +str(Y)+ " "+ str(Z)

    ######################################################

    radio.send(message) # Send the string over the radio
    mb.sleep(10)



mb.display.show(mb.Image.SQUARE)  # Display Square when program ends