import numpy as np 

A = np.array([0,10,20,40,60])
B = np.array([0,40])

ans = np.in1d(A,B)

print(ans)