import pandas as pd

df=pd.read_csv(r'f:\pythonprogs\nba.csv')

print(df.shape)

df.drop('Name', axis=1, inplace=True)
print(df.shape)

df.drop(['Age'], axis=1, inplace=True)
print(df.shape)

df.drop(['Weight', 'Salary'], axis=1, inplace=True)
print(df.shape)

df.drop(df.columns[[1]], axis=1, inplace=True)
print(df.shape)

df.drop(0, axis=0, inplace=True)
print(df.shape)

for index, row in df.iterrows() :
    print(type(index), type(row)  )
    break

for index, row in df.iterrows() :
    print('Index:', index)
    print('Value of row-->',row)
    break

for index, row in df.iterrows() :
    #print(df.iloc[index])
    print(row['Team'])
    break
