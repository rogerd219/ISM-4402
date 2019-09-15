#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np

f = "weekly_call_data/weekdata_000.xlsx"
df = pd.read_excel(f)
df.describe()


# In[7]:


import pandas as pd
import numpy as np
import glob
all_data = pd.DataFrame()
for f in glob.glob("weekly_call_data/weekdata_*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)
    
all_data.describe()


# In[ ]:




