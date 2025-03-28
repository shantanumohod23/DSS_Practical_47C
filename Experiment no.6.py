#!/usr/bin/env python
# coding: utf-8

# # Missing Value Treatment

# In[2]:


#Name: Shantanu Achyut Mohod
#RolL no. :47
#Sub : ET 1
#section:3C 
#Date:16/08/2024


# In[4]:


#Aim : To Find out the Missing Value, Data Cleaning


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


data.head(25)


# In[20]:


data.info()


# In[22]:


data.describe()


# In[24]:


data.shape


# In[28]:


data.size


# In[30]:


data.ndim


# In[32]:


data.isna()


# In[34]:


data.isna().any()


# In[36]:


data.isna().sum()


# In[38]:


data=data.dropna()


# In[40]:


data


# In[42]:


data["Age"].fillna(30.272590)


# In[44]:


data.isna().sum()


# In[ ]:




