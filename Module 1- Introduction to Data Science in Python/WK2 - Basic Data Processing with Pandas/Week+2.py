
# coding: utf-8

# ---
# 
# _You are currently looking at **version 1.0** of this notebook. To download notebooks and datafiles, as well as get help on Jupyter notebooks in the Coursera platform, visit the [Jupyter Notebook FAQ](https://www.coursera.org/learn/python-data-analysis/resources/0dhYG) course resource._
# 
# ---

# # The Series Data Structure

# In[1]:

import pandas as pd
get_ipython().magic('pinfo pd.Series')


# In[2]:

animals = ['Tiger', 'Bear', 'Moose']
pd.Series(animals)


# In[3]:

numbers = [1, 2, 3]
pd.Series(numbers)


# In[21]:

animals = ['Tiger', 'Bear', None]
pd.Series(animals)
pd.Series(animals).index


# In[19]:

numbers = [1, 2, None]
pd.Series(numbers)


# In[2]:

import numpy as np
np.nan == None


# In[11]:

np.nan == np.nan


# In[12]:

np.isnan(np.nan)


# In[13]:

sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
s


# In[14]:

s.index


# In[16]:

s = pd.Series(['Tiger', 'Bear', 'Moose'], index=['India', 'America', 'Canada'])
s


# In[18]:

sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports, index=['Golf', 'Sumo', 'Hockey'])
s.index


# # Querying a Series

# In[22]:

sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
s


# In[23]:

s.iloc[3]


# In[24]:

s.loc['Golf']


# In[25]:

s[3]


# In[26]:

s['Golf']


# In[27]:

sports = {99: 'Bhutan',
          100: 'Scotland',
          101: 'Japan',
          102: 'South Korea'}
s = pd.Series(sports)


# In[29]:

s[99] #This won't call s.iloc[0] as one might expect, it generates an error instead


# In[57]:

s = pd.Series([100.00, 120.00, 101.00, 3.00])
s


# In[31]:

total = 0
for item in s:
    total+=item
print(total)


# In[58]:

import numpy as np

total = np.sum(s)
print(total)


# In[33]:

#this creates a big series of random numbers
s = pd.Series(np.random.randint(0,1000,10000))
s.head()


# In[59]:

len(s)


# In[39]:

get_ipython().run_cell_magic('timeit', '', 'summary = 0\nfor item in s:\n    summary+=item')


# In[43]:

get_ipython().run_cell_magic('timeit', '', 'summary = np.sum(s)')


# In[44]:

s+=2 #adds two to each item in s using broadcasting
s.head()


# In[45]:

for label, value in s.iteritems():
    s.set_value(label, value+2)
s.head()


# In[60]:

get_ipython().run_cell_magic('timeit', '-n 10', 's = pd.Series(np.random.randint(0,1000,10000))\nfor label, value in s.iteritems():\n    s.loc[label]= value+2')


# In[48]:

get_ipython().run_cell_magic('timeit', '-n 10', 's = pd.Series(np.random.randint(0,1000,10000))\ns+=2')


# In[49]:

s = pd.Series([1, 2, 3])
s.loc['Animal'] = 'Bears'
s


# In[50]:

original_sports = pd.Series({'Archery': 'Bhutan',
                             'Golf': 'Scotland',
                             'Sumo': 'Japan',
                             'Taekwondo': 'South Korea'})
cricket_loving_countries = pd.Series(['Australia',
                                      'Barbados',
                                      'Pakistan',
                                      'England'], 
                                   index=['Cricket',
                                          'Cricket',
                                          'Cricket',
                                          'Cricket'])
all_countries = original_sports.append(cricket_loving_countries)


# In[51]:

original_sports


# In[52]:

cricket_loving_countries


# In[53]:

all_countries


# In[54]:

all_countries.loc['Cricket']


# # The DataFrame Data Structure

# In[61]:

import pandas as pd
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
df.head()


# In[62]:

df.loc['Store 2']


# In[63]:

type(df.loc['Store 2'])


# In[66]:

df.loc['Store 1']
type(df.loc['Store 1'])


# In[65]:

df.loc['Store 1', 'Cost']


# In[67]:

df.T


# In[68]:

df.T.loc['Cost']


# In[69]:

df['Cost']


# In[70]:

df.loc['Store 1']['Cost']


# In[71]:

df.loc[:,['Name', 'Cost']]


# In[72]:

df.drop('Store 1')


# In[73]:

df


# In[74]:

copy_df = df.copy()
copy_df = copy_df.drop('Store 1')
copy_df


# In[75]:

get_ipython().magic('pinfo copy_df.drop')


# In[76]:

del copy_df['Name']
copy_df


# In[77]:

df['Location'] = None
df


# # Dataframe Indexing and Loading

# In[78]:

costs = df['Cost']
costs


# In[79]:

costs+=2
costs


# In[80]:

df


# In[3]:

get_ipython().system('cat olympics.csv')


# In[4]:

df = pd.read_csv('olympics.csv')
df.head()


# In[28]:

df = pd.read_csv('olympics.csv', index_col = 0, skiprows=1)
df.head()


# In[9]:

df.columns


# In[29]:

for col in df.columns:
    if col[:2] == '01':
        df.rename(inplace=True,columns={col:'Gold'+col[4:]})
    if col[:2] == '02':
        df.rename(inplace=True,columns = {col:'Silver'+col[4:]})
    if col[:2] =='03':
        df.rename(inplace=True,columns = {col:'Bronze'+col[4:]})
    if col[:1] == '№':
        df.rename(inplace=True,columns = {col:'# '+col[2:]})

df.head()


# # Querying a DataFrame

# In[11]:

df['Gold'] > 0


# In[12]:

only_gold = df.where(df['Gold'] > 0)
only_gold.head()


# In[13]:

only_gold['Gold'].count()


# In[89]:

df['Gold'].count()


# In[14]:

only_gold = only_gold.dropna()
only_gold.head()


# In[91]:

only_gold = df[df['Gold'] > 0]
only_gold.head()


# In[16]:

len(df[(df['Gold']>0)| (df['Gold.1']>0)])


# In[17]:

df[(df['Gold.1'] > 0) & (df['Gold'] == 0)]


# # Indexing Dataframes

# In[21]:

df['country'] = df.index
df.head()


# In[22]:

df = df.set_index('Gold')
df.head()


# In[31]:

df = df.reset_index()
df.head()


# In[48]:

df = pd.read_csv('census.csv')
df.head()


# In[49]:

df['SUMLEV'].unique()


# In[50]:

df=df[df['SUMLEV']==50]
df.head()


# In[52]:

columns_to_keep = ['STNAME',
                   'CTYNAME',
                   'BIRTHS2010',
                   'BIRTHS2011',
                   'BIRTHS2012',
                   'BIRTHS2013',
                   'BIRTHS2014',
                   'BIRTHS2015',
                   'POPESTIMATE2010',
                   'POPESTIMATE2011',
                   'POPESTIMATE2012',
                   'POPESTIMATE2013',
                   'POPESTIMATE2014',
                   'POPESTIMATE2015']
df = df[columns_to_keep]
df.head()


# In[53]:

df = df.set_index(['STNAME', 'CTYNAME'])
df.head()


# In[69]:

df.loc['Michigan', 'Washtenaw County']['BIRTHS2010']


# In[72]:

df.loc[[('Michigan', 'Washtenaw County'), ('Michigan',  'Wayne County')]][['BIRTHS2010','BIRTHS2011']]


# # Missing values

# In[73]:

df = pd.read_csv('log.csv')
df


# In[77]:

get_ipython().magic('pinfo df.fillna')


# In[75]:

df = df.set_index('time')
df = df.sort_index()
df


# In[76]:

df = df.reset_index()
df = df.set_index(['time', 'user'])
df


# In[81]:

df = df.fillna(method='ffill')
df


# In[ ]:



