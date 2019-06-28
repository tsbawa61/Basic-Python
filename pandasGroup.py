#Group By
import pandas as pd

df=pd.read_csv(r'f:\pythonprogs\nba.csv')
df.head()
df.columns
df1=df.groupby('Team')
print(type(df1))
print(df1.groups.keys())
df1.mean() #One can use count(), min(), max(), median(), std()
y=df1.mean()
y['Number']
y.columns
y.head()

df2=df.groupby(['Team', 'Position'])
df2.std()

lst=['Position','Team']
df3=df.groupby(lst)
df3.median()


for name,group in df3:
   print (name) # Contains the all possible values of 'lst'
   print (group) #group contains corresponding rows
   break

df = df.drop(df[df['Age'] < 25].index)
print(df.shape)

df=df.drop(df.index[[0, 5]])
print(df.shape)

df[df['Age'] < 25].index

