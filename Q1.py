import numpy as np

a=[int(x) for x in input('Enter elements: ').split()]
a=np.array(a)
uni,count=np.unique(a,return_counts=True)
for i,j in zip(uni,count):
	print(i,':',j,end='\n')