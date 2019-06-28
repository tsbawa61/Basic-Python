#Conditional Selection
import pandas as pd
import numpy as np

df=pd.read_csv(r'f:\pythonprogs\nba.csv')
df.head() ; df.columns
print(df[df['Age']>36])
print(df[df['Position']=="PG"])

print(df[(df['Age']>36) & (df['Position']=="PG")]) #And Operator
print(df[(df['Age']==40) | (df['Weight']==231)]) #OR Operator

print(df[~(df['Age']>19)]) #Not Operator


df=pd.read_csv(r'f:\pythonprogs\nba.csv')
print(df.columns)

# Define the new names of your columns
newcols = { 'Weight': 'Wt', 'Salary': 'Sal' }

# Use `rename()` to rename your columns
df.rename(columns=newcols, inplace=True)
print(df.columns)

df['flag']=1; df.head()

"""
#Group By
import pandas as pd

df=pd.read_csv(r'f:\pythonprogs\nba.csv')
df.head(); df.columns
df1=df.groupby('Position')
type(df1)
df1.mean() #One can use count(), min(), max(), median(), std()
y=df1.mean()
y['Number']
y.columns ; y.head()

df2=df.groupby(['Team', 'Position'])
df2.std()

lst=['Position','Team']
df3=df.groupby(lst)
df3.median()

"""
