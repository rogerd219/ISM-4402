#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)

df.head()


# In[3]:


def gen_to_num(x):
    if x == 'female':
        return 1
    if x == 'male':
        return 0


# In[4]:


df['gender_val'] = df['gender'].apply(gen_to_num)
df.tail()


# In[7]:


import statsmodels.formula.api as sm
result = sm.ols(formula='grade ~ age + exercise + hours + gender_val', data=df).fit()
result.summary()


# In[9]:


import statsmodels.formula.api as sm
result = sm.ols(formula='grade ~ age + exercise + hours', data=df).fit()
result.summary()


# In[ ]:




