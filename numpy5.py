
import numpy as np
a=np.arange(12)**2
print(a.shape)
print(a)

i=np.array([1,2,1,10])
print(i.shape)
print(i)

b=a[i]
print(b.shape)
print(b)

j=np.array([[3,4],[9,7]])
print(j)

c=a[j]
print(c.shape)
print(c)

k=np.array([3,5,8,2])
print(k)
a[k]=0
print(a)

d=a>16
print(d)
g=a[d]
print(g)

a[d]=1
print(a)
