#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import pandas as pd
import matplotlib.pyplot as plt
filename1 = sys.argv[1]
filename2 = sys.argv[2]
#filename1 = 'pagecounts-20190509-120000.txt'
#filename2 = 'pagecounts-20190509-130000.txt'


# In[2]:


print(filename1)


# In[3]:


data1 = pd.read_csv(filename1, sep=' ', header=None, index_col=1, names=['lang', 'page', 'views', 'bytes'])
data2 = pd.read_csv(filename2, sep=' ', header=None, index_col=1, names=['lang', 'page', 'views', 'bytes'])


# In[4]:


series1 = data1['views']

series2 = data2['views']

newdf = pd.DataFrame(dict(views1 = series1, views2 = series2))
newdf


# In[5]:


data1_desc_views = data1.sort_values(by='views', ascending = False)
data2_desc_views = data2.sort_values(by='views', ascending = False)


# In[21]:


plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Popularity Distribution')
plt.xlabel('Rank')
plt.ylabel('Views')
plt.plot(data1_desc_views['views'].values, 'r-' )
plt.subplot(1, 2, 2)
plt.title('Daily Correlation')
plt.xlabel('Day 1 views')
plt.ylabel('Day 2 views')
plt.plot(newdf['views1'].values, newdf['views2'].values, 'b.')
plt.xscale('log')
plt.yscale('log')
plt.savefig('wikipedia.png')

