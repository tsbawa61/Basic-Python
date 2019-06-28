
import numpy as np
a=np.random.random((3,4))
print(a)
a=10*a
a=np.floor(a)
print(a)
print(a.shape)

print(a.ravel())
print(a)

b=a.ravel()
print(b)
print(b.shape)

c=a.reshape(2,6)
print(c)
print(c.shape)


d=a.T
print(a)
print(d)
print(d.shape,a.shape)

print(a)
a.resize(6,2)
print(a)

print(a.shape)
print(a.reshape(3,-1))
print(a.reshape(-1,3))

p=np.arange(30)
p.shape=2,-1,3
print(p.shape)
print(p)

x=np.random.random((2,2))
y=np.random.random( (2,2))

x=np.floor(10*x)
y=np.floor(10*y)

p=np.vstack((x,y))
print(p)
q=np.hstack((x,y))
print(q)
