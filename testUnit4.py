#!/usr/bin/env python
# coding: utf-8

#To run use ipython .\testUnit4.py
print("Hello World!")
# In[3]:


import numpy as np


# In[4]:


ones = np.ones(10)


# In[5]:


ones


# In[6]:


ones+ones


# In[7]:


ones*3


# In[8]:


ones+2


# In[9]:


rand= np.random.rand(10)


# In[10]:


rand[0]
# In[12]:


rand[9]




# In[14]:


rand[-3:]


# In[15]:


rand[3:]


# In[16]:


rand[np.where(rand<0.5)]


# In[17]:


rand+ones


# In[18]:



np.concatenate((rand, ones))


# In[24]:


np.array([ones,rand])


# In[25]:


np.array([ones,rand])[:,:3]


# In[26]:


np.array([ones,rand])[:,3:]


# In[27]:


myList=range(int(1e4))
myArray=np.array(int(1e4))


# In[29]:


get_ipython().run_cell_magic('timeit', '', '[i*2 for i in myList]')


# In[30]:


get_ipython().run_cell_magic('timeit', '', 'myArray*2')

