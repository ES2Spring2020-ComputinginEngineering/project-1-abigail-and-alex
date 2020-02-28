import numpy as np
import math


lengths=np.array([5,9,13,17.25, 21.25])

def estimated_period (length):
        a=np.divide (length,9.81)
        b=np.sqrt (a)
        c=b* 2.0
        d=3.14*c
        return d
        
print(estimated_period(lengths))
        
