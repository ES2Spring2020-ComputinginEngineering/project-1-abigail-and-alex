import numpy as np
import matplotlib.pyplot as plt



lengths=np.array([5,9,13,17.25, 21.25])*0.0254

def estimated_period (length):
        length=np.divide (length,9.81)
        length=np.sqrt (length)
        length=length* 2.0 * 3.14
        return length
        
period = estimated_period(lengths)

plt.plot(lengths,period)
plt.xlabel('Length of Pendulum')
plt.ylabel('Period of Pendulum')
plt.title('length vs Period of a Pendulum')
plt.show()

print(period)
        
#This assumes no air resistance or frictions
# or any outside factors effect the period of
# the pendulum
# In the real world there is friciton and air resistance so the pendulum
# would eventually slow down and come to a stop but it would not in our 
# calculations.