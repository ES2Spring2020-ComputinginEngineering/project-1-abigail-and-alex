import matplotlib.pyplot as plt
import numpy as np
import math

import os
path="C:/Users/abbyi/Documents/Freshman/ES2/GitHub/project-1-abigail-and-alex/Step 4"
os.chdir(path)
print(os.getcwd())

def acc_time (file):
    len_1= np.loadtxt(file,  delimiter=",")
    t=len_1[0:,0]
    x=len_1[0:,1]
    plt.plot(t/1000,x)
    plt.xlabel('Time')
    plt.ylabel('Acceleration of Pendulum')
    plt.title('Acceleration vs Time of Pendulum' + " at Length " + file[7])
    plt.show()
    
    
def angle_time (file):
    len_1= np.loadtxt(file,  delimiter=",")
    acc_y=len_1[0:,1]
    acc_z=len_1[0:,3]
    t=len_1[0:,0]
    a=np.exp(acc_y)
    b=np.exp(acc_z)
    c=np.add(a,b)
    theta=np.sqrt(c)
    plt.plot(t/1000,theta)
    plt.xlabel('Time')
    plt.ylabel('Angle of Pendulum')
    plt.title('Angle vs Time of Pendulum' + " at Length " + file[7])
    plt.show()

fin =open("Length 1.txt",encoding='utf8')
fin2 =open("Length 2.txt",encoding='utf8')
fin3 =open("Length 3.txt",encoding='utf8')
fin4 =open("Length 4.txt",encoding='utf8')
fin5 =open("Length 5.txt",encoding='utf8')

angle_time ("Length 2.txt") 



plt.show()
fin.close()
fin2.close()
fin3.close()
fin4.close()
fin5.close()