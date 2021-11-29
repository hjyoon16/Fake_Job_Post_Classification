#!/usr/bin/env python
# coding: utf-8

# In[20]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[21]:


data = pd.read_csv('/Users/yi/Desktop/fake_job_postings.csv')


# In[22]:


data.shape


# In[23]:


data.describe()


# In[24]:


data.info()


# In[25]:


sns.countplot(data.fraudulent).set_title('Real and Fradulent')
data.groupby('fraudulent').count()['title'].reset_index().sort_values(by='title',ascending=False)


# In[26]:


corr = data.corr()
sns.heatmap(corr)
plt.show()


# In[ ]:





# In[ ]:




