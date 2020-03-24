# Project 1 --- ES2
# Step 3: Collection of Real World Data: Reciever Code

#*****************************************
#
# YOUR NAMES:Abigail Imiolek and Alex Bayzk
#
#*****************************************

# IMPORT STATEMENTS
import microbit as mb
import radio


# MAIN SCRIPT
radio.on()  # Turn on radio
radio.config(channel=2, length =100)

print('Program Started')
mb.display.show(mb.Image.HAPPY, delay=1000, clear=True) #Displays a happy face before logging


# Wait for start message before beginning printing
incoming = ''
while not incoming == 'start':
    incoming = radio.receive()
print('start')


while True:
    incoming = radio.receive() # Read from radio

    if incoming is not None: # message was received
        mb.display.show(mb.Image.HEART, delay=100, clear=True, wait=False)
        x = incoming.split(' ')
        x[0]=int(x[0])
        x[1]=int(x[1])
        x[2]=int(x[2])
        x[3]=int(x[3])
        print(tuple(x))
        #Splits the incoming string from into a tuple



        mb.sleep(10)