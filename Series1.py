import pandas as pd
import numpy as np

"""
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
print (s)

data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data,index=['b','c','d','a'])
print (s)

s = pd.Series(5, index=[0, 1, 2, 3])
print(s)

data = np.array(['N', 'I', 'E', 'L', 'I', 'T'])
ser = pd.Series(data)
print(ser[:4])
print(type(ser[:4]))

ser = pd.Series(data,index=['N', 'I', 'E', 'L', 'I', 'T'])
print(ser['I'])
print(ser[:3])
print(ser[3:5])

ser = pd.Series(data,index=[10,11,12,13,14,15])
print(ser[14])
print(ser[:3])
print(ser[3:5])

data = np.array(['N', 'I', 'E', 'L', 'I', 'T'])
ser1 = pd.Series(data,index=[10,11,12,13,14,15])
print(ser1.loc[13:15])

ser2 = pd.Series(data,index=['N', 'I', 'E', 'L', 'I', 'T'])
print(ser2.loc['N':'L'])

#Error is produced : print(ser2.loc['I':'I']) or print(ser2.loc['I':'T'])

data = np.array(['N', 'I', 'E', 'L', 'I', 'T'])
ser1 = pd.Series(data,index=[10,11,12,13,14,15])
print(ser1.iloc[3:5])

ser2 = pd.Series(data,index=['N', 'I', 'E', 'L', 'I', 'T'])
print(ser2.iloc[3:5])

print(type(ser2.iloc[3:5]))

"""

#retrieve a single element
data = np.array(['N', 'I', 'E', 'L', 'I', 'T'])
ser2 = pd.Series(data,index=['a', 'b', 'c', 'd', 'e', 'f'])
print(ser2.iloc[3:5])
print (ser2['a'])
print (ser2[['a', 'd', 'c']])

