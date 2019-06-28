import numpy as np
import pandas as pd
df = pd.DataFrame(index=[0,1,2,3], columns=['A'])
print(df)
print(type(df))
print(df.info())

df1 = pd.DataFrame(index=range(4,7),columns=['A'], dtype='float')
print(df1)
df2 = pd.DataFrame(index=['A','B', 'C'],columns=[1,2], dtype='int')
print(df2)
