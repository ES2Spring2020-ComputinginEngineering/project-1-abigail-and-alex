import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.signal as sig

#import os
#path="C:/Users/abbyi/Documents/Freshman/ES2/GitHub/project-1-abigail-and-alex/Step 4"
#os.chdir(path)
#print(os.getcwd())

def acc_time (file):
    len_1= np.loadtxt(file,  delimiter=",")
    t=len_1[0:,0]
    x=len_1[0:,1]
    plt.plot(t,x)
    plt.xlabel('Time')
    plt.ylabel('Acceleration of Pendulum')
    plt.title('Acceleration vs Time of Pendulum' + " at Length " + file[7])
    plt.show()
    
    
def angle_time (file):
    len_1= np.loadtxt(file,  delimiter=",")
    acc_x =len_1[0:,1]
    acc_y=len_1[0:,2]
    acc_z=len_1[0:,3]
    t=len_1[0:,0]
    y = acc_y**2
    z = acc_z**2
    bottom_half = y+z
    bottom_half = np.sqrt(bottom_half)
    theta = acc_x/bottom_half
    theta = np.arctan(theta)
    
    plt.plot(t,theta)
    plt.xlabel('Time')
    plt.ylabel('Angle of Pendulum')
    plt.title('Angle vs Time of Pendulum' + " at Length " + file[7])
    plt.show()

def Period_of_Wave(file):
    data = np.loadtxt(file, delimiter = ",")
    t = data[0:,0]
    x = data[0:,1]
    smoothed = sig.medfilt(x)
    peaks = sig.find_peaks(smoothed)
    new_peaks = tuple(peaks[0])
    counter = 0
    max_iterations = len(new_peaks) -1
    time_between_periods = 0
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
            print("old max: " , old_max)
            print("new max: ", new_max)
            print("diff: ", new_max-old_max)
            time_between_periods += (new_max - old_max)
            old_max = t[i]
    time_between_periods = time_between_periods / (max_iterations+1)
    return time_between_periods
    

fin =open("Length 1.txt",encoding='utf8')
fin2 =open("Length 2.txt",encoding='utf8')
fin3 =open("Length 3.txt",encoding='utf8')
fin4 =open("Length 4.txt",encoding='utf8')
fin5 =open("Length 5.txt",encoding='utf8')

angle_time ("Length 1.txt") 
acc_time("Length 1.txt")
x = Period_of_Wave("Length 1.txt")
print("the Time Between Periods is: ", x)


plt.show()
fin.close()
fin2.close()
fin3.close()
fin4.close()
fin5.close()