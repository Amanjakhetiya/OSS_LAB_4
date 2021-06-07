import numpy as np  

A = np.array([0,10,20,40,60,80])
B = np.array([10,30,40,50,70])

ans=np.setxor1d(A,B)

print(ans)