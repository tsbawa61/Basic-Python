
import numpy as np
a=np.zeros((1,10))
a[0,5]=11

b=np.arange(37)
b[::-1]

c=np.array([1,2,3,4],dtype=float)
print(c)

d=np.zeros((4,4))
print(d)
d[0,...]=1
d[3,...]=1
d[...,3]=1
d[...,0]=1
print(d)

d=np.zeros((2,2))
p=np.ones((1,2))
q=np.ones((4,1))
print(p)
print(q)

d=np.vstack((d,p))
d=np.vstack((p,d))
d=np.hstack((q,d))
d=np.hstack((d,q))

print(d)

d=np.ones((4,4))
d[1:3,1:3]=0
print(d)

