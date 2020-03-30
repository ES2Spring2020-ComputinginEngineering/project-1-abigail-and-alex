# Project 1 --- ES2
# Step 5: Numerical Simulation

#*****************************************
#
# YOUR NAMES: Abigail Imiolek and Alex Bayzk
#
#*****************************************


# IMPORT STATEMENTS
import numpy as np
import matplotlib.pyplot as plt
import math 
import scipy.signal as sig


# GLOBAL VARIABLES
lengths=np.array([5,9,13,17.25, 21.25])*0.0254


def update_system(acc,pos,vel,time1,time2,length):
#This function takes six arguments, six floats: the acceleration, position, velocity, and the length at the times gives
#This function uses the Euler method to find the position, velocity, and calculates the next acceleration
#This function returns the found values for the position, velocity, and acceleration.
    dt = time2-time1
    posNext = pos+vel*dt
    velNext = vel+acc*dt
    accNext = -9.8*math.sin(pos)/l
    return posNext,velNext,accNext

def print_system(time,pos,vel,acc):
#This function takes four arguments, time, position, velocity, and acceleration
#It prints the values for each of the four variables
#The function has no return value.
    print("TIME:     ", time)
    print("POSITION: ", pos)
    print("VELOCITY: ", vel)
    print("ACCELERATION ", acc, "\n")

def wave_period(pos):
    peaks = sig.find_peaks(pos)
    peaks = tuple(peaks[0])
    old_max = 0
    new_max = 0
    counter = 0
    per = []
    diff = 0
    
    for i in range(len(pos)):
        if(i == peaks[counter]):
            if(counter == len(peaks)-1):
                break
            if(counter == 0):
                old_max = i
            new_max = i
            print("peak ", new_max)
            counter +=1
            diff = new_max - old_max
            per.append(diff)
            old_max = i

    sum = 0
    for i in range(len(per)):
        print("diff in peaks, ", per[i])
        sum += per[i]
    #You have to convert this time into seconds. I think this is the way to do it.
    sum = sum/(len(peaks)-1)
    sum /= len(pos)
    
    return sum
        

# initial conditions
l = .5
theta = math.pi/3
pos = [theta]
vel = [0]
acc = [-9.8*math.sin(theta)/l]
time = np.linspace(0,10,200001)


i = 1
t=[0]
while i < len(time):
# Updates position, velocity, and acceleration using previous values and time steps
    posNext, velNext, accNext = update_system(acc[i-1],pos[i-1],vel[i-1],time[i-1],time[i],l)
    pos.append(posNext)
    vel.append(velNext)
    acc.append(accNext)
    t.append(i)
    #print_system(time[i],pos[i],vel[i],acc[i])
    i += 1

#Graphs position, velocity, and acceleration vs time
plt.plot(t,pos,color="green")
plt.xlabel('Time (in milliseconds)')
plt.ylabel('Position of Pendulum (in theta)')
plt.title('Position of Pendulum vs Time')
plt.show()

plt.plot(t,vel,"red")
plt.xlabel('Time (in milliseconds)')
plt.ylabel('Velocity of Pendulum (in theta per second)')
plt.title('Velocity of Pendulum vs Time')
plt.show()

plt.plot(t,acc, "blue")
plt.xlabel('Time (in milliseconds)')
plt.ylabel('Acceleration of Pendulum (in theta per second squared)')
plt.title('Acceleration of Pendulum vs Time')
plt.show()

plt.scatter(l,wave_period(pos))
plt.xlabel('Lengths (in meters)')
plt.ylabel('Period (in seconds)')
plt.title('Period vs Length')
plt.show()
