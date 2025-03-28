#!/usr/bin/env python
# coding: utf-8

# # KNN K Nearest Neighbour

# In[3]:


#Name: Shantanu Achyut Mohod
#RolL no. :47
#Sub : ET 1
#section:3C 
#Date:20/09/2024


# In[4]:


#Aim: To Perform Operation on KNN K Nearest Neighbour


# In[6]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')


# In[8]:


df=pd.read_csv("C:\\Users\\prite\\OneDrive\\Desktop\\framingham.csv")


# In[10]:


df.head()


# In[12]:


df.describe


# In[14]:


df.info()


# In[16]:


df.isna().sum()


# In[18]:


df


# # Missing Value Treatment

# In[75]:


df['education'].fillna(value = df['education'].mean(),inplace=True)


# In[87]:


df['glucose'].fillna(value = df['glucose'].mean(),inplace=True)


# In[99]:


df['heartRate'].fillna(value = df['heartRate'].mean(),inplace=True)


# In[101]:


df['BMI'].fillna(value = df['BMI'].mean(),inplace=True)


# In[103]:


df['cigsPerDay'].fillna(value = df['cigsPerDay'].mean(),inplace=True)


# In[105]:


df['totChol'].fillna(value = df['totChol'].mean(),inplace=True)


# In[107]:


df['BPMeds'].fillna(value = df['BPMeds'].mean(),inplace=True)


# In[109]:


df.isna().sum()


# In[115]:


x = df.drop("TenYearCHD",axis=1)
y = df['TenYearCHD']


# In[117]:


x


# # Train Test Split

# In[120]:


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)


# In[122]:


y_train


# # KNN Classifier

# In[125]:


from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5, p=2, metric='minkowski')
knn.fit(x_train, y_train)
acc = knn.score(x_test,y_test)*100
print(acc)


# In[ ]:




