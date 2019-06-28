import matplotlib.pyplot as plt
x1,y1=[1,2,3,4], [1,4,9,16]
x2,y2=[1,3,4,6],[1,4,9,16]
x3,y3=[3,1,6,5],[2,1,7,14]

plt.plot(x1,y1,'b-', x2,y2, 'go',x3,y3,'.-r')
plt.axis([0, 7, 0, 20])
plt.xlabel("x axis ") 
plt.ylabel("y axis ")
plt.text(2,2,'Text',fontsize='large', color='r')
plt.title('Title')
plt.grid(b=True)
plt.suptitle('Sup Title')
plt.show()
