#!/usr/bin/env python
# coding: utf-8

# # Data Manipulation

# In[2]:


#Name: Shantanu Achyut Mohod
#RolL no. :47
#Sub : ET 1
#section:3C 
#Date:2/08/2024


# In[4]:


# Aim: To Perform Data Manipulation using Pandas


# In[6]:


import pandas as pd


# In[8]:


import os


# In[10]:


os.getcwd()


# In[12]:


os.chdir("C:\\Users\\prite\\OneDrive\\Desktop")


# In[14]:


data=pd.read_csv("Titanic.csv")


# In[16]:


data


# In[18]:


data.head()


# In[20]:


data.tail()


# In[24]:


data.describe()


# In[26]:


data.info()


# In[28]:


data.shape


# In[30]:


data.size


# In[32]:


data.ndim


# In[34]:


data.columns


# In[36]:


data.drop(labels="Age",axis=1)


# In[38]:


data.drop(labels=2,axis=0)


# In[ ]:




