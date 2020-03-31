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
    
def new_functions(theta,length, len_name, theta_name):
#This function takes four arguments, two floats: time and position and two strings: the name of the length of the string, and the theta.
#The graph applies update_system() to calculate the position, velocity, and acceleration for the functions given.
#It then graphs the functions.
#The function returns list of the positions.
    
    pos = [theta]
    vel = [0]
    acc = [-9.8*math.sin(theta)/length]
    
    i = 1
    t=[0]
    while i < len(time):
        posNext, velNext, accNext = update_system(acc[i-1],pos[i-1],vel[i-1],time[i-1],time[i],length)
        pos.append(posNext)
        vel.append(velNext)
        acc.append(accNext)
        t.append(i)
        i += 1
    plt.plot(t,pos,color="green", label='Position of Pendulum (in theta)')
    plt.plot(t,vel,"red", label='Velocity of Pendulum (in theta per second)')
    plt.plot(t,acc, "blue", label='Acceleration of Pendulum (in theta per second squared)')
    plt.title('Pendulum Function vs Time at Length' + len_name + " and Theta " + theta_name   )
    plt.legend(loc="lower center")
    plt.show()
    return pos

def wave_period(pos):
#The function takes one argument, list of the positions.
#It uses the positions to find the difference between peaks and calculate the period.
#The function returns the value of the period.
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
            counter +=1
            diff = new_max - old_max
            per.append(diff)
            old_max = i

    sum = 0
    for i in range(len(per)):
        sum += per[i]
    #Converts Arbitrary Time into seconds
    sum = sum/(len(peaks)-1)
    sum /= len(pos)
    return sum
        
def period_length(pos1, pos2, pos3, pos4, pos5):
#The function takes five arguments, lists of the positions.
#It calls the wave_period() function for all five lists, and then graphs the period vs lengths.
#The function has no return value.
    p1=wave_period(pos1)
    p2=wave_period(pos2)
    p3=wave_period(pos3)
    p4=wave_period(pos4)
    p5=wave_period(pos5)
    period=np.array([p1,p2,p3,p4,p5])
    print(period)
    lengths=np.array([5,9,13,17.25, 21.25])*0.0254
   
    plt.scatter(lengths, period)
    plt.xlabel('Lengths (in meters)')
    plt.ylabel('Period (in seconds)')
    plt.title('Period vs Length')
    plt.show()

#MAIN SCRIPT
x1=new_functions(math.pi/4,5*0.0254, " 1", "pi/4")
x11=new_functions(3*math.pi/4,5*0.0254, " 1" , "3pi/4")

x2=new_functions(math.pi/4,9*0.0254, " 2" , "pi/4")
x22=new_functions(3*math.pi/4,9*0.0254, " 2", "3pi/4")

x3=new_functions(math.pi/4,13*0.0254, " 3" , "pi/4")
x33=new_functions(3*math.pi/4,13*0.0254, " 3", "3pi/4")

x4=new_functions(math.pi/4,17.25*0.0254,  " 4" , "pi/4")
x44=new_functions(3*math.pi/4,17.25*0.0254,  " 4", "3pi/4")

x5=new_functions(math.pi/4,21.25*0.0254,  " 5" , "pi/4")
x55=new_functions(3*math.pi/4,21.25*0.0254,  " 5" , "3pi/4")

period_length(x1, x2, x3, x4, x5)
period_length(x11, x22, x33, x44, x55)