import numpy as np
import pandas as pd

arr=np.array([[" ",'A','B','C'], [0,1,2,3], [1,4,5,6],[2,7,8,9]])

df=pd.DataFrame(data=arr[1:,1:], index=arr[1:,0], columns=arr[0,1:])

df.head()
df.iloc[0][0]
df.loc['2']['C']
df.at['0', 'A']
df.iat[0,0]

# getting a row or column
print(df.iloc[0]) #Row
print(type(df.iloc[0]))

print(df.loc[:,'B']) #Column
print(type(df.loc[:,'B']))

index=2
df.iloc[index]
df.iloc[:index]
df.iloc[-index]
df.iloc[-index:]
df.iloc[:,0:2]

