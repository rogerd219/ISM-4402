#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
Location = "all_040_in_12.P1.csv"
df = pd.read_csv(Location, header=None)
df.head()

