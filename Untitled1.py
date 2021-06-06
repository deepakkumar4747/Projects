#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


# In[2]:


s = os.path.sep

df = pd.read_csv('C:'+s+'Users'+s+'deepak'+s+'Downloads'+s+'adult_data.csv')
#removing white spaces
df.columns = df.columns.str.strip()
columns_to_keep= {'age','workclass','fnlwgt','education','occupation','sex','capital-gain','capital-loss','hours-per-week','salary'}
df = df[columns_to_keep]

df = df.fillna(0)


# In[3]:


df.head()


# In[90]:


for i in columns_to_keep:
    if df.dtypes[i]==np.object:
        y1 = dict(df[ df['salary']==' <=50K'][i].value_counts())
        y2 = dict(df[ df['salary']==' >50K'][i].value_counts())
        x = y1.keys() if len(y1.keys()) >= len(y2.keys()) else y2.keys() #keys() are the list of keys of the dictionary
        if len(y1.keys()) != len(y2.keys()):
            for i in x:
                if i not in y2.keys():
                    y2[i] = 0
                if i not in y1.keys():
                    y1[i] = 0
        
        plt.bar(x, list(y1.values()), color='r', label = 'Lower than 50k')
        plt.bar(x, list(y2.values()), bottom=list(y1.values()), color='b', label = 'more than 50k')
        plt.xticks(rotation=90)
        plt.legend()
        plt.title(i)
        plt.show()


# In[ ]:





# In[ ]:



         


# In[ ]:





# In[81]:





# In[ ]:




