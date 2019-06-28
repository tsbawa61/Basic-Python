
import numpy as np
a=np.arange(12).reshape(3,4)
print(a.shape)
print(a)

b=np.array([False, True, True])
c=np.array([False, True, True, False])
print(b,c)

print(a[b,:])
print(a[:,c])

d=np.arange(10)*3
print(d[2:5])
d[2:5]=10
d[2:8:2]=0

print(d[8:2:-1])
print(d[ : :-1])

def f(x,y):
    return 10*x+y

g=np.fromfunction(f,(5,4))
print(g)

print(g[1:4,2])
print(g[1:4,:])
print(g[:,1:2])

print(g[(0,1,2),(0,2,3)])
print(g[-2])
print(g[1,...])
