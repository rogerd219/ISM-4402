#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

Location = "gradedata.csv"
df = pd.read_csv(Location)

df.head


# In[4]:


bins = [0,80,100]
status_names = ['Fail', 'Pass']
df['status'] = pd.cut(df['grade'], bins, labels=status_names)
df


# In[ ]:




