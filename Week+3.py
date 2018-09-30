
# coding: utf-8

# ---
# 
# _You are currently looking at **version 1.0** of this notebook. To download notebooks and datafiles, as well as get help on Jupyter notebooks in the Coursera platform, visit the [Jupyter Notebook FAQ](https://www.coursera.org/learn/python-data-analysis/resources/0dhYG) course resource._
# 
# ---

# # Merging Dataframes
# 

# In[1]:

import pandas as pd

df = pd.DataFrame([{'Name': 'Chris', 'Item Purchased': 'Sponge', 'Cost': 22.50},
                   {'Name': 'Kevyn', 'Item Purchased': 'Kitty Litter', 'Cost': 2.50},
                   {'Name': 'Filip', 'Item Purchased': 'Spoon', 'Cost': 5.00}],
                  index=['Store 1', 'Store 1', 'Store 2'])
df


# In[2]:

df['Date'] = ['December 1', 'January 1', 'mid-May']
df


# In[3]:

df['Delivered'] = True
df


# In[4]:

df['Feedback'] = ['Positive', None, 'Negative']
df


# In[7]:

adf = df.reset_index()
adf['Date'] = pd.Series({0: 'December 1', 2: 'mid-May'})
adf


# In[8]:

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])
staff_df = staff_df.set_index('Name')
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])
student_df = student_df.set_index('Name')
print(staff_df.head())
print()
print(student_df.head())


# In[12]:

pd.merge(staff_df, student_df, how='outer', left_index=True,right_index=True)


# In[13]:

pd.merge(staff_df, student_df, how='inner', left_index=True, right_index=True)


# In[14]:

pd.merge(staff_df, student_df, how='left', left_index=True, right_index=True)


# In[15]:

pd.merge(staff_df, student_df, how='right', left_index=True, right_index=True)


# In[16]:

staff_df = staff_df.reset_index()
student_df = student_df.reset_index()
pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name')


# In[19]:

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR', 'Location': 'State Street'},
                         {'Name': 'Sally', 'Role': 'Course liasion', 'Location': 'Washington Avenue'},
                         {'Name': 'James', 'Role': 'Grader', 'Location': 'Washington Avenue'}])
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business', 'Location': '1024 Billiard Avenue'},
                           {'Name': 'Mike', 'School': 'Law', 'Location': 'Fraternity House #22'},
                           {'Name': 'Sally', 'School': 'Engineering', 'Location': '512 Wilson Crescent'}])
pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name')


# In[20]:

staff_df = pd.DataFrame([{'First Name': 'Kelly', 'Last Name': 'Desjardins', 'Role': 'Director of HR'},
                         {'First Name': 'Sally', 'Last Name': 'Brooks', 'Role': 'Course liasion'},
                         {'First Name': 'James', 'Last Name': 'Wilde', 'Role': 'Grader'}])
student_df = pd.DataFrame([{'First Name': 'James', 'Last Name': 'Hammond', 'School': 'Business'},
                           {'First Name': 'Mike', 'Last Name': 'Smith', 'School': 'Law'},
                           {'First Name': 'Sally', 'Last Name': 'Brooks', 'School': 'Engineering'}])
staff_df
student_df
pd.merge(staff_df, student_df, how='inner', left_on=['First Name','Last Name'], right_on=['First Name','Last Name'])


# # Idiomatic Pandas: Making Code Pandorable

# In[21]:

import pandas as pd
df = pd.read_csv('census.csv')
df


# In[22]:

(df.where(df['SUMLEV']==50)
    .dropna()
    .set_index(['STNAME','CTYNAME'])
    .rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'}))


# In[ ]:

df = df[df['SUMLEV']==50]
df.set_index(['STNAME','CTYNAME'], inplace=True)
df.rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'})


# In[23]:

import numpy as np
def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    return pd.Series({'min': np.min(data), 'max': np.max(data)})


# In[24]:

df.apply(min_max, axis=1)


# In[39]:

import numpy as np
def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    row['max'] = np.max(data)
    row['min'] = np.min(data)
    return row
df.apply(min_max,axis=1)


# In[33]:

cdf = df[df['SUMLEV']==50][['STNAME','CTYNAME','POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']]
cdf = cdf.set_index(['STNAME','CTYNAME'])
cdf['maxpop'] = cdf.max(axis=1)
cdf['minpop'] = cdf.min(axis=1)
cdf


# In[40]:

rows = ['POPESTIMATE2010',
        'POPESTIMATE2011',
        'POPESTIMATE2012',
        'POPESTIMATE2013',
        'POPESTIMATE2014',
        'POPESTIMATE2015']
df.apply(lambda x: np.max(x[rows]), axis=1)


# # Group by

# In[10]:

import pandas as pd
import numpy as np
df = pd.read_csv('census.csv')
df = df[df['SUMLEV']==50]
df


# In[2]:

get_ipython().run_cell_magic('timeit', '-n 10', "for state in df['STNAME'].unique():\n    avg = np.average(df.where(df['STNAME']==state).dropna()['CENSUS2010POP'])\n    print('Counties in state ' + state + ' have an average population of ' + str(avg))")


# In[3]:

get_ipython().run_cell_magic('timeit', '-n 10', "for group, frame in df.groupby('STNAME'):\n    avg = np.average(frame['CENSUS2010POP'])\n    print('Counties in state ' + group + ' have an average population of ' + str(avg))")


# In[66]:




# In[11]:

def fun(item):
    print(item)
    if item[0]<'M':
        return 0
    if item[0]<'Q':
        return 1
    return 2

for group, frame in df.groupby(fun):
    print('There are ' + str(len(frame)) + ' records in group ' + str(group) + ' for processing.')


# In[12]:

df = pd.read_csv('census.csv')
df = df[df['SUMLEV']==50]


# In[13]:

df.groupby('STNAME').agg({'CENSUS2010POP': np.average})


# In[14]:

df.groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011']
print(type(df.groupby(level=0)['POPESTIMATE2010']))


# In[20]:

(df.set_index(['STNAME','CTYNAME']).groupby(level=0)['CENSUS2010POP']
    .agg({'avg': np.average, 'sum': np.sum}))


# In[21]:

(df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011']
    .agg({'avg': np.average, 'sum': np.sum}))


# In[22]:

(df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011']
    .agg({'POPESTIMATE2010': np.average, 'POPESTIMATE2011': np.sum}))


# # Scales

# In[25]:

df = pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
                  index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good', 'ok', 'ok', 'ok', 'poor', 'poor'])
df.rename(columns={0: 'Grades'}, inplace=True)
df


# In[26]:

df['Grades'].astype('category').head()


# In[33]:

grades = df['Grades'].astype('category',
                             categories=['F','D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'],
                             ordered=True)
grades.head()


# In[35]:

pd.get_dummies(grades)


# In[39]:

df = pd.read_csv('census.csv')
df = df[df['SUMLEV']==50]
df = df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg({'avg': np.average})
pd.cut(df['avg'],10)


# # Pivot Tables

# In[40]:

#http://open.canada.ca/data/en/dataset/98f1a129-f628-4ce4-b24d-6f16bf24dd64
df = pd.read_csv('cars.csv')


# In[41]:

df.head()


# In[42]:

df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=np.mean)


# In[45]:

df.pivot_table(values=['(kW)'], index=['YEAR','TYPE'], columns='Make', aggfunc=[np.mean,np.min], margins=True)


# # Date Functionality in Pandas

# In[46]:

import pandas as pd
import numpy as np


# ### Timestamp

# In[52]:

pd.Timestamp('9/1/2016 15:05:07')


# ### Period

# In[55]:

pd.Period('2018/8/1 15')


# In[56]:

pd.Period()


# ### DatetimeIndex

# In[63]:

t1 = pd.Series(list('abc'), [pd.Timestamp('2016-09-01'), pd.Timestamp('2016-09-02'), pd.Timestamp('2016-09-03')])
t1


# In[64]:

t1.index


# ### PeriodIndex

# In[68]:

t2 = pd.Series(list('def'), [pd.Period('2016-09-01'), pd.Period('2016-9-2'), pd.Period('2016-9-3')])
t2


# In[69]:

t2.index


# ### Converting to Datetime

# In[10]:

d1 = ['2 June 2013', 'Aug 29, 2014', '2015-06-26', '7/12/16']
ts3 = pd.DataFrame(np.random.randint(10, 100, (4,2)), index=d1, columns=list('ab'))
ts3


# In[11]:

ts3.index = pd.to_datetime(ts3.index)
ts3


# In[12]:

pd.to_datetime('4.7.12', dayfirst=True)


# ### Timedeltas

# In[13]:

pd.Timestamp('9/3/2016')-pd.Timestamp('9/1/2016')


# In[14]:

pd.Timestamp('9/2/2016 8:10AM') + pd.Timedelta('12D 3H')


# ### Working with Dates in a Dataframe

# In[70]:

dates = pd.date_range('10-01-2016', periods=9, freq='2W-SUN')
dates


# In[72]:

df = pd.DataFrame({'Count 1': 100 + np.random.randint(-5, 10, 9).cumsum(),
                  'Count 2': 120 + np.random.randint(-5, 10, 9)}, index=dates)
df


# In[73]:

df.index.weekday_name


# In[74]:

df.diff()


# In[75]:

df.resample('M').mean()


# In[20]:

df['2017']


# In[21]:

df['2016-12']


# In[22]:

df['2016-12':]


# In[76]:

df.asfreq('W', method='ffill')


# In[77]:

import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

df.plot()


# In[ ]:



