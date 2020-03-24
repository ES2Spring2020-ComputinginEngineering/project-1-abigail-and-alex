# Project 1 --- ES2
# Step 1: Theoretical Periods

#*****************************************
#
# YOUR NAMES:Abigail Imiolek and Alex Bayzk
#
#*****************************************


# IMPORT STATEMENTS
import numpy as np
import matplotlib.pyplot as plt


# GLOBAL VARIABLES
lengths=np.array([5,9,13,17.25, 21.25])*0.0254


# CUSTOM FUNCTION DEFINTIONS
def estimated_period (length):
#This function takes one argurment, an array of pendulum lengths.
#The function then completes the calculations required to give the estimated period of each pendulum length in the array.
#The function returns an array, called period, of the estimated periods for each lengths.
        length=np.divide (length,9.81)
        length=np.sqrt (length)
        period=length* 2.0 * 3.14
        return period


# MAIN SCRIPT
#The main script finds the estimated period for the array lengths, and graphs the length vs the period of the pendulum.
period = estimated_period(lengths)

plt.plot(lengths,period)
plt.xlabel('Length of Pendulum (in meters)')
plt.ylabel('Period of Pendulum (in seconds)')
plt.title('Length vs Period of a Pendulum')
plt.show()


#This assumes no air resistance or frictions
# or any outside factors effect the period of
# the pendulum
# In the real world there is friciton and air resistance so the pendulum
# would eventually slow down and come to a stop but it would not in our 
# calculations.