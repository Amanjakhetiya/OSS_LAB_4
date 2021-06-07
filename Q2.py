import numpy as np

a = input("Enter the binary string : ")

l1 = list(map(int,a))

l1=np.array(l1)

ans=np.sum(l1)
# print(ans)
l1[:ans]=1
l1[ans:]=0
# l1=list(l1)
# print(''.join(l1))
# print("".join(l1))
print(l1)

