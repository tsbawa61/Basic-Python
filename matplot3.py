from matplotlib import pyplot as plt
import numpy as np 
## Create data
from random import random, seed

seed(0)
x = [ int(10*random()) for i in range(16) ]
plt.boxplot(x)
plt.show()

y=x.copy()
y.sort()
print(y)

import statistics as st
print(st.median(x))



