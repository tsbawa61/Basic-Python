import numpy as np
a = np.ones((2,3), dtype=int)
b = np.random.random((2,3))
b 
a *= 3 
a 
b += a 
b 

a +=b
a=a.astype(float)+b
b=a+b.astype(int)
