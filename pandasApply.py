#Apply Function 
import pandas as pd

df=pd.read_csv(r'f:\pythonprogs\iris.csv')
df.head(-10)
df.columns

import numpy as np
df['sepal length'].apply(np.sqrt)
df['sepal width'].apply(np.sum)
df[:4] # Gives 4 Rows
df.iloc[:,:4].apply(np.sum) # Here axis=0
df.iloc[:,:4].apply(np.sum,axis=1)
df.iloc[:,1:3].apply(np.sum, axis=0)

doubler = lambda x: x*2
# Apply the `doubler` function to the `A` DataFrame column
df['sepal length'].apply(doubler)

def dbl(x):
    return x*3

df['sepal width'].apply(dbl)

df.loc[0].apply(doubler)

doubled_df = df.applymap(doubler)
print(doubled_df)
