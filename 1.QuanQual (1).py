#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


dataset=pd.read_csv("Placement.csv")


# In[3]:


dataset


# In[4]:


dataset.info()


# In[5]:


quan=["ssc_p","hsc_p","etest","degree_P","mba_p","salary"]
qual=["gender","ssc_b","hsc_b","degree_t"]


# In[6]:


dataset.columns


# In[7]:


dir(dataset)


# In[8]:


dataset["ssc_p"].dtypes


# In[9]:


for columnName in dataset.columns:
    print(columnName)


# In[ ]:





# In[10]:


if(dataset["gender"].dtype=='O'):
    print("qual")
else:
    print("quan")


# In[11]:


qual


# In[12]:


quan


# In[13]:


def quanQual(dataset):
    quan=[]
    qual=[]
    for columnName in dataset.columns:
        print(columnName)
        if(dataset[columnName].dtype=='O'):
            print("qual")
            qual.append(columnName)
        else:
            print("quan")
            quan.append(columnName)
            return quan,qual


# In[14]:


quanQual(dataset)


# In[15]:


quan,qual=quanQual(dataset)


# In[16]:


qual


# In[17]:


quan


# In[ ]:




