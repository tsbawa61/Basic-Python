import pandas as pd
# making data frame from csv file 
data = pd.read_csv(r'f:\PythonProgs\nba.csv')
print(data.info)

"""
# creating bool series True for NaN values 
bool_series = pd.isnull(data["College"]) 
print(bool_series.head())

# filtering data : displaying data only with team = NaN 
data1=data[bool_series] 
print(data1.head())

bool_series1 = pd.notnull(data["College"]) 
data2=data[bool_series1] 
print(data2.head())
"""


data3=data.fillna(0)
print(data3.head(10))


