#!/usr/bin/env python
# coding: utf-8

# # Logistic Regression

# In[3]:


#Name: Shantanu Achyut Mohod
#RolL no. :47
#Sub : ET 1
#section:3C
#Date:13/09/2024


# In[5]:


#Aim: To Perform Operation on Logistic Regression


# In[7]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')


# In[9]:


import os


# In[13]:


os.getcwd()


# In[20]:


os.chdir("C:\\Users\\prite\\OneDrive\\Desktop")


# In[22]:


df=pd.read_csv("C:\\Users\\prite\\OneDrive\\Desktop\\framingham.csv")


# In[24]:


df.head()


# In[26]:


df.describe()


# In[28]:


df.info()


# In[30]:


df.isna().sum()


# In[32]:


df


# # Missing Value Treatment

# In[35]:


df['glucose'].fillna(value = df['glucose'].mean(),inplace=True)


# In[37]:


df['education'].fillna(value = df['education'].mean(),inplace=True)


# In[52]:


df['heartRate'].fillna(value = df['heartRate'].mean(),inplace=True)


# In[41]:


df['BMI'].fillna(value = df['BMI'].mean(),inplace=True)


# In[45]:


df['cigsPerDay'].fillna(value = df['cigsPerDay'].mean(),inplace=True)


# In[48]:


df['totChol'].fillna(value = df['totChol'].mean(),inplace=True)


# In[50]:


df['BPMeds'].fillna(value = df['BPMeds'].mean(),inplace=True)


# In[54]:


df.isna().sum()


# In[56]:


#Splitting the dependent and independent variables.
x = df.drop("TenYearCHD",axis=1)
y = df['TenYearCHD']


# In[60]:


x


# # Train Test Split

# In[63]:


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,train_size=42)


# In[65]:


y_train


# # Logistic Regression Algorithm

# In[68]:


from sklearn.linear_model import LogisticRegression
model = LogisticRegression().fit(x_train,y_train)
model.score(x_train, y_train)


# In[ ]:




