#!/usr/bin/env python
# coding: utf-8

# # Statistical Description

# In[2]:


#Name: Shantanu Achyut Mohod
#RolL no. :47
#Sub : ET 1
#section:3C 
#Date:26/07/2024


# In[5]:


# Aim: To Perform Statistical Description on Data 


# In[9]:


import pandas as pd


# In[11]:


import os


# In[13]:


os.getcwd()


# In[15]:


os.chdir("C:\\Users\\prite\\OneDrive\\Desktop")


# In[17]:


data=pd.read_csv("framingham.csv")


# In[19]:


data.head()


# In[21]:


data.head(10)


# In[23]:


data.tail()


# In[27]:


data.tail(10)


# In[31]:


data.describe()


# In[33]:


data.info()


# In[35]:


data.shape


# In[37]:


data.size


# In[39]:


data.ndim


# In[ ]:




