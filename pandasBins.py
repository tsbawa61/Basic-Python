import pandas as pd
# making data frame from csv file 
df = pd.read_csv(r'f:\PythonProgs\diabetes.csv') 

ranges=[0,18,30,50,60,80,120]
range_names=['Children','Youth','Middle Age','Senior','Retired','Eighty+']

df['age_cat'] =pd.cut(df['Age'], bins=ranges, labels=range_names)



