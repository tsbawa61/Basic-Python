#Importing pyplot
from matplotlib import pyplot as plt
#Plotting to our canvas
plt.title('First Example')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.plot([1,2,3],[4,5,1])

#Showing what we plotted
plt.show()

plt.plot([1,2,3,4], [1,4,9,16], '.-r',label='Coordinates A')
plt.plot([1,2,3,4], [1,5,8,15], 'bo--', label='Coordinates B')
plt.axis([0, 6, 0, 20])
plt.legend()
plt.show()

import numpy as np 

x = np.arange(1,11) 
y = 2 * x + 5 
plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(x,y) 
plt.show()

plt.suptitle("Matplotlib Example") 
plt.xlim(0, 7) 
plt.ylim(-0.5, 18)
plt.xticks(np.arange(0, 7, step=0.5))
plt.yticks(np.arange(-0.5, 7, step=1.5),('L1','L2','L3','L4','L5'))


# Compute the x and y coordinates for points on a sine curve 
x = np.arange(0, 3 * np.pi, 0.1) 
y = np.sin(x) 
plt.title("sine wave form") 

plt.plot(x, y) 
plt.show() 

x = np.arange(0, 3 * np.pi, 0.1) 
y_sin = np.sin(x) 
y_cos = np.cos(x)  
# Set up a subplot grid that has height 2 and width 1, 
# and set the first such subplot as active. 
plt.subplot(2, 1, 1)  
plt.plot(x, y_sin) # Make the first plot 
plt.title('Sine')  
plt.subplot(2, 1, 2) # Set the second subplot as active, and make the second plot. 
plt.plot(x, y_cos) 
plt.title('Cosine')  
plt.show()
