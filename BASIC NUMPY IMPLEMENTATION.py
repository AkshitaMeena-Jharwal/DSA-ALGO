#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


arr1 =np.arange(100,200,2)
arr1


# In[4]:


print(arr1[10:])


# In[5]:


print(arr1[:20])


# In[6]:


print(arr1[10:20])


# In[7]:


print(arr1[10:50:5])


# In[8]:


print(arr1[::10])


# In[10]:


print(arr1[::-10])


# In[11]:


arr_slice = slice(1,10,2)


# In[12]:


a = np.arange(30)
a


# In[13]:


b= a.reshape(6,5)
b


# In[14]:


b[2:4,1:4]


# In[15]:


b.ndim


# In[16]:


print(arr1.itemsize)


# In[17]:


print(arr1.dtype)


# In[18]:


print(arr1.size)


# In[19]:


print(b.min())


# In[21]:


print(b.max())


# In[22]:


print(b.sum())


# In[23]:


print(np.sqrt(b))


# In[24]:


print(np.std(arr1))


# In[25]:


arr5 = np.empty([3,2],dtype=int)
print(arr5)


# In[26]:


arr5 = np.empty([3,2],dtype=float)
print(arr5)


# In[17]:


dir(np)


# In[27]:


a = np.array([','])
a


# In[28]:


a = np.array(['day'])
a


# In[29]:


arr1 = np.array([1,2,3],dtype=np.float64)
arr1


# In[30]:


arr1 = np.array([1.5,2,0,555,3],dtype=bool)
arr1


# In[32]:


arr = np.array([1.5,2,0,5555,4])
arr


# In[34]:


arr = np.array([1, 2, 3, 4, 5]) 
arr


# In[35]:


float_arr = arr.astype(np.float64)
float_arr


# In[36]:


arr.astype(bool)


# In[37]:


numeric_strings = np.array(['1.25','-9.6','42'],dtype =str)
numeric_strings 


# In[38]:


m = numeric_strings.astype(float)
m


# In[39]:


m = numeric_strings.astype(float)
m


# In[ ]:


m.astype(int)


# In[40]:


numeric_strings = np.array(['1.25','-9.6','42'], dtype=np.string_)
print (numeric_strings)
print (numeric_strings.dtype)
print ('\n')
float_values = numeric_strings.astype(float)
print (float_values)
print (float_values.dtype)


# In[41]:


arr = np.array([3, 2, 0, 1])
arr


# In[42]:


arr = np.array([3,2,0,1])
print(np.sort(arr))


# In[43]:


arr= np.array(['banana','cherry','apple'])
print(np.sort(arr))


# In[44]:


arr= np.array(['banana','cherry','apple'])
print(np.sort(arr)[::-1])


# In[45]:


arr = np.array([[3,2,4],[5,0,1]])
print(np.sort(arr))


# In[39]:


arr = np.array([[3,2,4],[5,0,1]])
print(arr)
print()
print(np.sort(arr,axis=0))


# In[40]:


print(np.sort(arr,axis=1))


# In[41]:


import numpy as np
arr = np.arange(10,19)
print(arr)


# In[42]:


arr = np.delete(arr,2)
print(arr)


# In[45]:


arr = np.arange(10,19)
arr = np.delete(arr,[2,5])
print(arr)


# In[47]:


arr = np.arange(10,22)
arr2 = np.reshape(arr,[3,4])
print(arr2)


# In[48]:


a = np.delete(arr2,1,0)
print(a)


# In[49]:


a = np.delete(arr2,0,1)
print(a)


# In[ ]:




