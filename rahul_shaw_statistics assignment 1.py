#!/usr/bin/env python
# coding: utf-8

# In[56]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as sts


# In[2]:


#Q1
#You have to create a function that receives a list of numbers like [23,14,13,56,78,98,12] and returns it's Interquartile range(IQR)

#Note: You have to code the logic from scratch


# In[34]:


def iqr(a):
    a=[23,14,13,56,78,98,12]
    return sts.iqr(a)


# In[35]:


iqr(a)


# In[ ]:


#Q2

#Plot a histogram for total team scores for all IPL games.

#Note: Per match 2 teams will play hence total number scores would be = no. of matches * 2


# In[36]:


delivery=pd.read_csv('deliveries.csv')


# In[37]:


delivery


# In[40]:


delivery.info()


# In[38]:


ts=delivery.groupby('inning')['total_runs'].sum().sort_values()


# In[39]:


plt.hist(ts)


# In[ ]:


#Q3
#Find the skewness of bowler economy data where the bowler has bowled a minimum of 300 balls.

#Note : if you don't know about economy read this https://en.wikipedia.org/wiki/Economy_rate_(cricket)


# In[79]:


bo=delivery[delivery['extra_runs']==0][['ball','bowler']]
bowler_balls=bo.groupby('bowler')['ball'].count().reset_index().sort_values(by='ball',ascending=False).reset_index(drop=True)


# In[113]:


bowler_balls


# In[77]:


bowler_runs=delivery.groupby('bowler')['total_runs'].sum().reset_index().sort_values(by='total_runs',ascending=False).reset_index(drop=True)


# In[78]:


bowler_runs


# In[107]:


bowler_balls['no_of_overs']=(bowler_balls['ball']/6)


# In[108]:


bowler_balls


# In[110]:


bowler_economy= pd.merge(bowler_runs,bowler_balls,on="bowler")


# In[111]:


bowler_economy=bowler_economy[bowler_economy['no_of_overs']>50]


# In[112]:


bowler_economy['economy_rate']=bowler_economy['total_runs']/bowler_economy['no_of_overs']
bowler_economy=bowler_economy.sort_values(by='economy_rate').reset_index(drop=True)
bowler_economy


# In[114]:


sns.kdeplot(bowler_economy['economy_rate'])


# In[ ]:


#Q4
#Give three examples of negatively skewed data and 3 examples of positively skewed data


# In[125]:





# In[130]:


sns.kdeplot(delivery[''])


# In[ ]:




