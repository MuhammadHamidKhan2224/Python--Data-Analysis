#!/usr/bin/env python
# coding: utf-8

# ## Task 1: Variables and Data Types

# In[1]:


age = 21


# In[2]:


age


# In[3]:


type(age)


# In[4]:


name = 'M_Hamid  Niazi'


# In[5]:


name


# In[6]:


type(name)


# In[7]:


student = True


# In[8]:


type(student)


# In[9]:


age = age + 25


# In[10]:


age


# In[11]:


name += " Smith"


# In[12]:


name


# In[13]:


name = name.replace("NiaziSmith", "Niazi")


# In[14]:


print(name)


# In[15]:


type(name)


# In[16]:


student = True


# In[17]:


student = not student 


# In[18]:


student


# ##  Task 2: Expressions and Operators

# In[2]:


width = 5.5
height = 3.25


# In[20]:


area = width * height


# In[21]:


print('Total given area is:', area)


# In[24]:


celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(fahrenheit)


# In[25]:


radius = 5
area = 3.14159 * radius ** 2
area


# ## Task 3: Introduction to Data Structures

# In[26]:


fruits = ["apple", "banana", "orange", "grape", "kiwi"]

fruits


# In[28]:


type(fruits)


# In[27]:


months = ("January", "February", "March")
months


# ## Task 4: List Manipulation

# In[31]:


from math import*
numbers = [12, 34, 45, 67, 89, 100, 23, 56]
sum_numbers = sum(numbers)
average_numbers = sum_numbers / len(numbers)
(sum_numbers, average_numbers)


# In[38]:


del fruits[0]  
del fruits[-1]  

print(fruits)


# In[ ]:




