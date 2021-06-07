import numpy as np
a = input("Enter string : ")
nth = int(input("Enter nth: "))
if len(a)<nth:
	print("Not Possible")
else:
	f=np.array([a[:nth]])
	l=np.array([a[nth+1:]])

	print(np.concatenate((f,l),axis=0))