#!/usr/bin/env python
# coding: utf-8

# ## Getting Started with Pandas

# In[1]:


import pandas as pd


# In[2]:


totals = pd.read_csv('totals.csv').set_index(keys=['name'])


# In[3]:


counts = pd.read_csv('counts.csv').set_index(keys=['name'])


# In[4]:


lowest_precip = totals.sum(axis=1).idxmin()
print("City with lowest total precipitation:\n",lowest_precip)


# In[5]:


total_precipitation_month = totals.sum(axis=0)
total_observation_month = counts.sum(axis=0)
print("Average precipitation in each month:\n",total_precipitation_month/total_observation_month)


# In[6]:


total_precipitation_daily = totals.sum(axis=1)
total_observation_daily = counts.sum(axis=1)
print("Average precipitation in each city:")
print(total_precipitation_daily/total_observation_daily)


# In[ ]:




