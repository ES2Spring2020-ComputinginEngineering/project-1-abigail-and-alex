# Project 1 --- ES2
# Step 4: Analysis of Results

#*****************************************
#
# YOUR NAMES:Abigail Imiolek and Alex Bayzk
#
#*****************************************


# IMPORT STATEMENTS
import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.signal as sig

#import os
#path="C:/Users/abbyi/Documents/Freshman/ES2/GitHub/project-1-abigail-and-alex/Step 4"
#os.chdir(path)
#print(os.getcwd())

# CUSTOM FUNCTION DEFINTIONS
def acc_time (file):
#This function takes one argument, a text file containing the pendulum data from step 3
#This function then takes that data to plot the Acceleration of the Pendulum vs the Time
#This function has no return value
    len_1= np.loadtxt(file,  delimiter=",")
    t=len_1[0:,0]
    x=len_1[0:,1]
    y=len_1[0:,2]
    plt.plot(t/1000,x, label="Acceleration in X Direction")
    plt.plot(t/1000,y, label="Acceleration in Y Direction")
    plt.legend(loc="best")
    plt.xlabel('Time (in seconds)')
    plt.ylabel('Acceleration of Pendulum (in milli-g)')
    plt.title('Acceleration vs Time of Pendulum' + " at Length " + file[7])
    plt.show()
    
    
def angle_time (file):
#This function takes one argument, a text file containing the pendulum data from step 3
#This function takes that data and completes the computations to find the angle of the pendulum from the acceleration
#This function then  plots the Acceleration of the Pendulum vs the Time
#This function has no return value
    len_1= np.loadtxt(file,  delimiter=",")
    acc_x =len_1[0:,1]
    acc_y=len_1[0:,2]
    acc_z=len_1[0:,3]
    t=len_1[0:,0]
    x= acc_x**2
    y = acc_y**2
    z = acc_z**2
    bottom_half = y+z
    bottom_half = np.sqrt(bottom_half)
    theta = acc_x/bottom_half
    theta = np.arctan(theta)
    
    bottom_half2 = x+z
    bottom_half2 = np.sqrt(bottom_half2)
    theta2 = acc_y/bottom_half2
    theta2 = np.arctan(theta2)
    
    plt.plot(t/1000,theta, label="Angle in X Direction")
    plt.plot(t/1000, theta2, label="Acceleration in Y Direction")
    plt.legend(loc="best")
    plt.xlabel('Time (in seconds)')
    plt.ylabel('Angle of Pendulum (in radians)')
    plt.title('Angle vs Time of Pendulum' + " at Length " + file[7])
    plt.show()

def Period_of_Wave(file):
#This function takes one argument, a text file containing the pendulum data from step 3.
#The function then finds the period of the pendulum by smoothing out the data and finding the time between the peaks.
#The function returns a float, which is the period for the length of pendulum given by the file.
    data = np.loadtxt(file, delimiter = ",")
    t = data[0:,0]
    x = data[0:,1]
    print(t)
    smoothed = sig.medfilt(x)
    peaks = sig.find_peaks(smoothed)
    new_peaks = tuple(peaks[0])
    counter = 0
    max_iterations = len(new_peaks) -1
    time_of_periods = 0
    new_max = 0;
    old_max = 0;
    
    for i in range(len(t)):
        if (i == new_peaks[counter]):
            if(counter == max_iterations):
               break
            if(counter == 0):
               old_max = t[i]
            new_max = t[i]
            counter +=1
            time_of_periods += (new_max - old_max)
            old_max = t[i]
    time_of_periods = time_of_periods / (max_iterations+1)
    return time_of_periods/1000
    
def period_length(file1, file2, file3, file4, file5):
#This function takes five arguments, all text files containing the pendulum data from step 3.
#The function calls the previous function to find the period of the pendulum from each trial.
#The function then graphs all the periods vs length as a scatterplot.
#The function has no return value
    p1=Period_of_Wave(file1)
    p2=Period_of_Wave(file2)
    p3=Period_of_Wave(file3)
    p4=Period_of_Wave(file4)
    p5=Period_of_Wave(file5)
    period=np.array([p1,p2,p3,p4,p5])
    print(period)
    lengths=np.array([5,9,13,17.25, 21.25])*0.0254
   
    plt.scatter(lengths, period)
    plt.xlabel('Lengths (in meters)')
    plt.ylabel('Period (in seconds)')
    plt.title('Period vs Length')
    plt.show()
    
# MAIN SCRIPT    
#The main script graphs the angle and acceleration vs time for each of the data sets
#It also graphs the periods on one graph.
fin =open("Length 1.txt",encoding='utf8')
fin2 =open("Length 2.txt",encoding='utf8')
fin3 =open("Length 3.txt",encoding='utf8')
fin4 =open("Length 4.txt",encoding='utf8')
fin5 =open("Length 5 New.txt",encoding='utf8')

angle_time ("Length 1.txt") 
acc_time("Length 1.txt")
angle_time ("Length 2.txt") 
acc_time("Length 2.txt")
angle_time ("Length 3.txt") 
acc_time("Length 3.txt")
angle_time ("Length 4.txt") 
acc_time("Length 4.txt")
angle_time ("Length 5 New.txt") 
acc_time("Length 5 New.txt")
period_length("Length 1.txt", "Length 2.txt", "Length 3.txt", "Length 4.txt", "Length 5 New.txt")


plt.show()
fin.close()
fin2.close()
fin3.close()
fin4.close()
fin5.close()
