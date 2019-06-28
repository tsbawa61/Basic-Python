
import numpy as np
a=np.arange(0,6)
print(a)

a.shape=2,3
print(a)

b=a.reshape(2,3)
print(b)

c=a.reshape(3,2)
print(c)

d=np.arange(1,13)
print(d)
g=d.reshape(4,3)
print(g)

h=d.reshape(2,3,2)

print(h)

a=np.array([24,12,78,90])
b=np.arange(15,19)
c=a-b
d=b**2
print(d)

g=10*d
print(g)

h=a<50
print(h)

k=np.sin(b)
print(k)

A = np.array( [[1,1], [0,1]] ) 
B = np.array( [[2,0], [3,1]] )
C=A*B
print(A);print(B);print(C)


A.dot(B)

np.dot(A,B)

A*=3
B+=A
a = np.ones((2,3), dtype=int)
b = np.random.random((2,3)) 
b+=a
a+=b
a=a+b 
