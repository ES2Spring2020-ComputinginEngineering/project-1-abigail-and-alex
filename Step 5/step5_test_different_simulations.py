# IMPORT STATEMENTS
import numpy as np
import matplotlib.pyplot as plt
import math 
import scipy.signal as sig


# GLOBAL VARIABLES
lengths=np.array([5,9,13,17.25, 21.25])*0.0254
time = np.linspace(0,10,200001)


def update_system(acc,pos,vel,time1,time2,length):
#This function takes six arguments, six floats: the acceleration, position, velocity, and the length at the times gives
#This function uses the Euler method to find the position, velocity, and calculates the next acceleration
#This function returns the found values for the position, velocity, and acceleration.
    dt = time2-time1
    posNext = pos+vel*dt
    velNext = vel+acc*dt
    accNext = -9.8*math.sin(pos)/length
    return posNext,velNext,accNext

def print_system(time,pos,vel,acc):
#This function takes four arguments, time, position, velocity, and acceleration
#It prints the values for each of the four variables
#The function has no return value.
    print("TIME:     ", time)
    print("POSITION: ", pos)
    print("VELOCITY: ", vel)
    print("ACCELERATION ", acc, "\n")
    
def new_functions(theta,length, descriptor):
    pos = [theta]
    vel = [0]
    acc = [-9.8*math.sin(theta)/length]
    
    i = 1
    t=[0]
    while i < len(time):
    # Updates position, velocity, and acceleration using previous values and time steps
        posNext, velNext, accNext = update_system(acc[i-1],pos[i-1],vel[i-1],time[i-1],time[i],length)
        pos.append(posNext)
        vel.append(velNext)
        acc.append(accNext)
        t.append(i)
        #print_system(time[i],pos[i],vel[i],acc[i])
        i += 1
        #Graphs position, velocity, and acceleration vs time
        
    plt.plot(t,pos,color="green", label='Position of Pendulum (in theta)')
    plt.plot(t,vel,"red", label='Velocity of Pendulum (in theta per second)')
    plt.plot(t,acc, "blue", label='Acceleration of Pendulum (in theta per second squared)')
    plt.title('Pendulum Function vs Time with ' + descriptor)
    plt.legend(loc="lower center")
    plt.show()
    return pos


new_functions(2*math.pi/3,.5, "Theta of 2pi/3")
new_functions(math.pi,.5, "Theta of pi")

time = np.linspace(0,10,2001)
new_functions(math.pi/2,.5, "With Low Timestamp")

time = np.linspace(0,120,200001)
new_functions(math.pi/2,.5, "With Long Runtime" )

time = np.linspace(0,10,200000000001)
new_functions(math.pi/2,.5, "With High Timestamp")