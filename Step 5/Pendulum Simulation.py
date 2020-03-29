# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 11:08:40 2020

@author: alexb
"""
import numpy as np
import matplotlib.pyplot as plt
import math 
import scipy.signal as sig


# GLOBAL VARIABLES
lengths=np.array([5,9,13,17.25, 21.25])*0.0254


def update_system(acc,pos,vel,time1,time2,length):
    # position and velocity update below
    dt = time2-time1
    posNext = pos+vel*dt
    velNext = vel+acc*dt
    accNext = -9.8*math.sin(pos)/l
    return posNext,velNext,accNext

def print_system(time,pos,vel,acc):
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
theta = math.pi/2
pos = [theta]
vel = [0]
acc = [-9.8*math.sin(theta)/l]
time = np.linspace(0,10,200001)


i = 1
t=[0]
while i < len(time):
    # update position and velocity using previous values and time step
    posNext, velNext, accNext = update_system(acc[i-1],pos[i-1],vel[i-1],time[i-1],time[i],l)
    pos.append(posNext)
    vel.append(velNext)
    acc.append(accNext)
    t.append(i)
    #print_system(time[i],pos[i],vel[i],acc[i])
    i += 1


plt.plot(t,pos,color="green")
plt.show()
plt.plot(t,vel,"red")
plt.show()
plt.plot(t,acc, "blue")
plt.show()

print("period ", wave_period(pos))
