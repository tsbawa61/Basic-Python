#Importing pyplot
from matplotlib import pyplot as plt
x = [5,8,10] ; y = [12,16,6]  
x2 = [6,9,11] ;y2 = [6,15,7] 
plt.bar(x, y, label='Team India')
plt.bar(x2, y2, label='Team England', color = 'g') 

plt.title('Bar graph') 
plt.ylabel('Y axis') 
plt.xlabel('X axis')
plt.legend()
plt.show()

import numpy as np

a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27]) 
plt.hist(a, bins = [0,20,40,60,80,100]) 
plt.title("histogram") 
plt.show()

hist,bins = np.histogram(a,bins = [0,20,40,60,80,100]) 
print (hist )
print (bins)

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3, label='Type 1')
plt.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^',label='Type 2')
plt.legend()
plt.show()


from random import random, seed

seed(0)
x = [ int(10*random()) for i in range(15) ]
y = [ int(10*random()) for i in range(15) ]

print(x,y)
plt.scatter(x, y, color='darkgreen', marker='^')
plt.show()

x=range(0,15)
y=[2*i+int(10*random()) for i in x ]
plt.scatter(x, y, color='darkgreen', marker='^',label='Positive')

x=range(0,15)
y=[30-2*i+int(10*random()) for i in x ]
plt.scatter(x, y, color='r', marker='+', label='Negative')
plt.legend()
plt.show()
