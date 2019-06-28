
import numpy as np
a=np.array([1,2,3,4])
print(a)
print(a.shape)
print(a.dtype)
print(a.ndim)
print(a.size)
print(a.itemsize)
print(a.data)

b=np.array([(1.1,2),(3,4)])
print(b)
b.shape
b.dtype
b.itemsize
b.ndim

c=np.array([[(1,2,3),(3,4,5)],[(1,2,3),(3,4,5)]])
print(c)
print(c.shape)
print(c.dtype)
print(c.ndim)
print(c.size)
print(c.itemsize)

d=np.array([(1,2,3),(3,4,5)], dtype=complex)
print(d)
d.shape
d.dtype
d.itemsize

x=np.array([(1.2,2,3),(3,4,5)], dtype=int)
print(x)
x.shape
x.dtype

x=np.array([(12,2,3),(3,4,5)], dtype=float)
print(x)
x.shape
x.dtype

p=np.zeros((3,4))

q=np.zeros((3,4), dtype=int)

s=np.ones((3,4), dtype=int)

y=np.empty((3,4))
print(y)

g=np.arange(10,20,5)
h=np.arange(0,3,.5)
print(h)

k=np.linspace(0,2,8)
print(k)

from numpy import pi
m=np.linspace(0,2*pi,13)
fn=np.sin(m)
print(fn)

c = np.arange(24).reshape(2,3,4) # 3d array 
print(c) 
