#!/usr/bin/env python
# coding: utf-8

# # SVM Classifier

# In[3]:


#Name: Shantanu Achyut Mohod
#RolL no. :47
#Sub : ET 1
#section:3C 
#Date:27/09/2024


# In[4]:


#Aim: To Perform Operation on SVM Classifier


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

# In[21]:


df['education'].fillna(value = df['education'].mean(),inplace=True)


# In[23]:


df['glucose'].fillna(value = df['glucose'].mean(),inplace=True)


# In[25]:


df['heartRate'].fillna(value = df['heartRate'].mean(),inplace=True)


# In[27]:


df['BMI'].fillna(value = df['BMI'].mean(),inplace=True)


# In[29]:


df['cigsPerDay'].fillna(value = df['cigsPerDay'].mean(),inplace=True)


# In[31]:


df['totChol'].fillna(value = df['totChol'].mean(),inplace=True)


# In[33]:


df['BPMeds'].fillna(value = df['BPMeds'].mean(),inplace=True)


# In[35]:


df.isna().sum()


# In[37]:


x = df.drop("TenYearCHD",axis=1)
y = df['TenYearCHD']


# In[39]:


x


# In[41]:


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)


# In[43]:


y_train


# # SVM Classifier

# In[46]:


from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
svc=SVC()
svc.fit(x_test,y_test)
acc = svc.score(x_test,y_test)*100
print(acc)


# In[ ]:




