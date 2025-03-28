#!/usr/bin/env python
# coding: utf-8

# # Data Aquisition

# In[2]:


#Name: Shantanu Achyut Mohod
#RolL no. :47
#Sub : ET 1
#section:3C 
#Date:19/07/2024


# In[5]:


# Aim: To Study Data Aquisition using Pandas


# In[15]:


import pandas as pd


# In[17]:


import os


# In[19]:


os.getcwd()


# In[23]:


os.chdir("C:\\Users\\prite\\OneDrive\\Desktop")


# In[25]:


data=pd.read_csv("diabetes.csv")


# In[27]:


data.head()


# In[29]:


data.tail()


# In[ ]:




