#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


data = np.load('monthdata.npz')
totals = data['totals']
counts = data['counts']


# In[18]:


lowest_total_precipitation = np.argmin(totals.sum(axis=1))
print("Row with lowest total precipitation:\n",lowest_total_precipitation)


# In[17]:


total_precipitation_month = totals.sum(axis=0)
total_observation_month = counts.sum(axis=0)
print("Average precipitation in each month:\n",total_precipitation_month/total_observation_month)


# In[20]:


total_precipitation_daily = totals.sum(axis=1)
total_observation_daily = counts.sum(axis=1)
print("Average precipitation in each city:\n",total_precipitation_daily/total_observation_daily)


# In[21]:


#print(totals.shape)


# In[22]:


quarter_total = np.reshape(totals, (4*totals.shape[0], 3))


# In[25]:


quarter_total_sum = quarter_total.sum(axis=1)


# In[26]:

#print(quarter_total_sum)


# In[27]:


quarter_total = np.reshape(quarter_total_sum, (totals.shape[0],4))


# In[28]:

print("Quarterly precipitation totals:")
print(quarter_total)




