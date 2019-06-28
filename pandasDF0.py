import pandas as pd
import numpy as np

#Take a 2D array as input to your DataFrame 
arr = np.array([[1, 2, 3], [4, 5, 6]])
df1=pd.DataFrame(np.array([[1,2,3],[4,5,6]]))
print(df1,'\n')

print(df1.head()) # Column names are 0,1,2 and Row names are 0,1

#Take a dictionary as input to your DataFrame 
my_dict = {1: ['1', '3'], 2: ['1', '2'], 3: ['2', '4']}
print(pd.DataFrame(my_dict),'\n')

#Take a DataFrame as input to your DataFrame 
my_df = pd.DataFrame(data=[4,5,6,7], index=range(0,4), columns=['A'])
print(pd.DataFrame(my_df),'\n')

#Take a Series as input to your DataFrame
my_series = pd.Series({"United Kingdom":"London", "India":"New Delhi", "United States":"Washington", "Belgium":"Brussels"})
print(pd.DataFrame(my_series),'\n')
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
        "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
        "area": [8.516, 17.10, 3.286, 9.597, 1.221],
        "population": [200.4, 143.5, 1252, 1357, 52.98] }

df=pd.DataFrame(dict)
print(df.head())
df.index=['BR','RU','IN','CH','SA']
print(df.shape)
print(df.shape[1]) # FOR NUMBER OF COLUMNS  OF DF
print(df.shape[0]) # FOR NUMBER OF  ROWS OF DF

print(df.index); print(len(df.index))
print(df.columns) ; print(len(df.columns))

data=np.array([['','col1','col2'],['row1',1,2],['row2',3,4]])

print(data)
print(data[1:,1:])
print(data[1:,0])
print(data[0,1:])

df2=pd.DataFrame(data=data[1:,1:],index=data[1:,0], columns=data[0,1:])
