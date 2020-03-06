# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 11:08:40 2020

@author: alexb
"""
import numpy as np
import matplotlib.pyplot as plt
import math 



def update_system(acc,pos,vel,time1,time2,length):
    # position and velocity update below
    dt = time2-time1
    posNext = pos+vel*dt
    velNext = vel+acc*dt
    accNext = -9.8*math.sin(posNext)/l
    return posNext,velNext,accNext

def print_system(time,pos,vel,acc):
    print("TIME:     ", time)
    print("POSITION: ", pos)
    print("VELOCITY: ", vel)
    print("ACCELERATION ", acc, "\n")

# initial conditions
l = 2
theta = 3.14/4
pos = [theta]
vel = [0]
acc = [0,0]
acc[1] = -9.8*math.sin(theta)/l
time = np.linspace(0,20,201)


print_system(time[0],pos[0],vel[0],acc[0])
i = 1
while i < len(time):
    # update position and velocity using previous values and time step
    posNext, velNext, accNext = update_system(acc[i],pos[i-1],vel[i-1],time[i-1],time[i],l)
    pos.append(posNext)
    vel.append(velNext)
    acc.append(accNext)
    #print_system(time[i],pos[i],vel[i],acc[i])
    i += 1


plt.plot(time,vel)
plt.show()