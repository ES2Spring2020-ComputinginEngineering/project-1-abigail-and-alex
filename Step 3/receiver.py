##################
# FILL IN HEADER
#################

import microbit as mb
import radio  # Needs to be imported separately

# Change the channel if other microbits are interfering. (Default=7)
radio.on()  # Turn on radio
radio.config(channel=2, length =100)

print('Program Started')
mb.display.show(mb.Image.HAPPY, delay=1000, clear=True)


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



        mb.sleep(10)