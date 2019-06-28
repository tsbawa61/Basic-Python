import pandas as pd
df=pd.read_table('f:\\PythonProgs\\salary.dat',delim_whitespace=True)
df.head()
dummy=pd.get_dummies(df['sx'])
dummy.head()

df1=pd.concat([df,dummy],axis=1)
df1.head()
import pandas as pd 
raw_data = { 'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Ram', 'Sham', 'Ashok', 'Satish', 'Rajnish']}
df_a = pd.DataFrame(raw_data, columns = ['subject_id', 'first_name'])
print(df_a.head())
raw_data = { 'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Jivitesh', 'Reetika', 'Sanjeev', 'Ritu', 'Sonia']}
df_b = pd.DataFrame(raw_data, columns = ['subject_id', 'first_name'])
df_b.head()
#Join the two dataframes along rows
df_new = pd.concat([df_a, df_b])
df_new.head(10)

#Join the two dataframes along columns
df_new_1=pd.concat([df_a, df_b], axis=1)
df_new_1.columns
print(df_new_1['subject_id'])
df_new_1.head()

raw_data = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
df_c = pd.DataFrame(raw_data, columns = ['subject_id','test_id'])
df_c

#Merge two dataframes along the subject_id value
pd.merge(df_new, df_c, on='subject_id')

#Merge two dataframes with both the left and right dataframes using the subject_id key
pd.merge(df_new, df_c, left_on='subject_id', right_on='subject_id')

#Merge with outer join
#Full outer join produces the set of all records in Table A and Table B, with matching records from both sides where available. If there is no match, the missing side will contain null
pd.merge(df_a, df_b, on='subject_id', how='outer')

#Merge with inner join
#Inner join produces only the set of records that match in both Table A and Table B
pd.merge(df_a, df_b, on='subject_id', how='inner')

#Merge with right join
pd.merge(df_a, df_b, on='subject_id', how='right')

#Merge with left join
#Left outer join produces a complete set of records from Table A, with the matching records (where available) in Table B. If there is no match, the right side will contain null
pd.merge(df_a, df_b, on='subject_id', how='left')

#Merge while adding a suffix to duplicate column names
pd.merge(df_a, df_b, on='subject_id', how='left', suffixes=('_left', '_right'))
