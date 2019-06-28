from filterFn import *
list=[1,2,3,4,5,6]
#chk=lambda x: (x%2==0)
list2=filter1(lambda x: (x%2==0), list)
print(list2)
