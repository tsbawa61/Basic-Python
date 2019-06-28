import pandas
df=pandas.read_excel('pandasExcel.xlsx', 'Sheet1')
print(type(df)) #Output is <class 'pandas.core.frame.DataFrame'>
print(df.head())

pandas.read_csv(‘nba.csv')
print(df.head())

import pandas as pd
df=pd.read_csv(r'f:\pythonprogs\nba.txt')
print(df.head())

df=pd.read_csv(r'f:\pythonprogs\nbaSC.txt',delimiter=';')
print(df.shape)
print(df.columns)



df=pd.read_csv(r'f:\pythonprogs\iris.csv')
df.head()

df.columns
df['spieces']
type(df['spieces'])   #pandas.core.series.Series
df[['spieces']]
type(df[['spieces']]) #pandas.core.frame.DataFrame
df[['spieces', 'sepal width']] #type: pandas.core.frame.DataFrame

df.loc[df['spieces']=='Iris-setosa']
df.dtypes
