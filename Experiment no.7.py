#!/usr/bin/env python
# coding: utf-8

# # Data Visualization

# In[2]:


#Name: Shantanu Achyut Mohod
#RolL no. :47
#Sub : ET 1
#section:3C 
#Date:23/08/2024


# In[4]:


# Aim: To Perform Data Visualization 


# In[6]:


import numpy as np
from matplotlib import pyplot as plt 


# In[8]:


x=np.arange(1,11) 


# In[11]:


x


# In[13]:


y=2*x 


# In[15]:


y


# In[17]:


plt.plot(x,y)
plt.title("line chart")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show() 


# In[19]:


plt.bar(x,y)
plt.title("bar chart")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show() 


# In[21]:


plt.scatter(x,y)
plt.title("bar chart")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show() 


# In[23]:


H=[1,2,3,3,4,6,7,4,3,2,1,2,3,4,5,5,6,6,5,4,3,3,3,3,3,3,3,5,6,3,2,1,1,2]


# In[25]:


plt.hist(H)
plt.show() 


# In[ ]:




