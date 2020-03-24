# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 11:08:40 2020

@author: alexb
"""
import numpy as np
import matplotlib.pyplot as plt
import math 

# GLOBAL VARIABLES
lengths=np.array([5,9,13,17.25, 21.25])*0.0254


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
l = 5*0.0254
theta = math.pi/2
pos = [theta]
vel = [0]
acc = [0,-9.8*math.sin(theta)/l]
time = np.linspace(0,10,201)


print_system(time[0],pos[0],vel[0],acc[0])
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


plt.plot(t,vel)
plt.plot(t,pos)
plt.plot(t,acc)
plt.show()