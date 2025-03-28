#!/usr/bin/env python
# coding: utf-8

# # Simple Linear Regression

# In[2]:


#Name: Shantanu Achyut Mohod
#RolL no. :47
#Sub : ET 1
#section:3C 
#Date:6/09/2024


# In[4]:


# Aim: To Perform Simple Linear Regression


# In[6]:


import pandas as pd


# In[106]:


df=pd.read_csv("C:\\Users\\prite\\OneDrive\\Desktop\\Salary.csv")


# In[108]:


df.head(10)


# In[110]:


df.tail()


# In[112]:


df.info()


# In[114]:


df.describe()


# In[116]:


df.shape


# In[118]:


df.size


# In[120]:


df.ndim


# In[122]:


data.isnull()


# In[124]:


df.isnull().any()


# In[126]:


df.isnull().sum()


# In[128]:


a="ashish"


# In[130]:


print(a)


# In[132]:


a[0]


# In[134]:


a[-1]


# In[136]:


a[1:3]


# In[138]:


a[1:4]


# In[150]:


#Assiging values in X & Y
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values



#X = df['YearsExperience']
#y = df['Salary']


# In[154]:


print(X)


# In[156]:


print(y)


# In[158]:


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[160]:


#Splitting testdata into X_train,X_test,y_train,y_test
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=.3,random_state=42) 


# In[162]:


print(X_train)


# In[164]:


print(X_test)


# In[166]:


print(y_train)


# In[168]:


print(y_test)


# In[170]:


from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train, y_train)


# In[172]:


#Assigning Coefficient (slope) to m
m = lr.coef_  


# In[174]:


print("Coefficient  :" , m)


# In[176]:


#Assigning Y-intercept to a
c = lr.intercept_


# In[178]:


print("Intercept : ", c)


# In[180]:


lr.score(X_test,y_test) * 100


# In[ ]:




