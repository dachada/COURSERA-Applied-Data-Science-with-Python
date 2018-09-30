
# coding: utf-8

# ---
# 
# _You are currently looking at **version 1.0** of this notebook. To download notebooks and datafiles, as well as get help on Jupyter notebooks in the Coursera platform, visit the [Jupyter Notebook FAQ](https://www.coursera.org/learn/python-data-analysis/resources/0dhYG) course resource._
# 
# ---

# # Distributions in Pandas

# In[1]:

import pandas as pd
import numpy as np


# In[2]:

np.random.binomial(1, 0.5)


# In[3]:

np.random.binomial(1000, 0.5)/1000


# In[4]:

chance_of_tornado = 0.01/100
np.random.binomial(100000, chance_of_tornado)


# In[8]:

chance_of_tornado = 0.01

tornado_events = np.random.binomial(1, chance_of_tornado, 1000000)
    
two_days_in_a_row = 0
for j in range(1,len(tornado_events)):
    if tornado_events[j]==1 and tornado_events[j-1]==1:
        two_days_in_a_row+=1

print('{} tornadoes back to back in {:.2f} years'.format(two_days_in_a_row, 1000000/365))


# In[10]:

np.random.uniform(0, 1,10)


# In[11]:

np.random.normal(0.75)


# Formula for standard deviation
# $$\sqrt{\frac{1}{N} \sum_{i=1}^N (x_i - \overline{x})^2}$$

# In[12]:

distribution = np.random.normal(0.75,size=1000)

np.sqrt(np.sum((np.mean(distribution)-distribution)**2)/len(distribution))


# In[13]:

np.std(distribution)


# In[14]:

import scipy.stats as stats
stats.kurtosis(distribution)


# In[15]:

stats.skew(distribution)


# In[23]:

chi_squared_df2 = np.random.chisquare(2, size=10000)
stats.skew(chi_squared_df2)


# In[24]:

chi_squared_df5 = np.random.chisquare(5, size=10000)
stats.skew(chi_squared_df5)


# In[25]:

get_ipython().magic('matplotlib inline')
import matplotlib
import matplotlib.pyplot as plt

output = plt.hist([chi_squared_df2,chi_squared_df5], bins=50, histtype='step', 
                  label=['2 degrees of freedom','5 degrees of freedom'])
plt.legend(loc='upper right')


# # Hypothesis Testing

# In[26]:

df = pd.read_csv('grades.csv')


# In[27]:

df.head()


# In[28]:

len(df)


# In[29]:

early = df[df['assignment1_submission'] <= '2015-12-31']
late = df[df['assignment1_submission'] > '2015-12-31']


# In[30]:

early.mean()


# In[31]:

late.mean()


# In[32]:

from scipy import stats
get_ipython().magic('pinfo stats.ttest_ind')


# In[33]:

stats.ttest_ind(early['assignment1_grade'], late['assignment1_grade'])


# In[34]:

stats.ttest_ind(early['assignment2_grade'], late['assignment2_grade'])


# In[35]:

stats.ttest_ind(early['assignment3_grade'], late['assignment3_grade'])


# In[ ]:



