#!/usr/bin/env python
# coding: utf-8

# ## Task 1: Dictionary Operations 

# ###### Added the dictionay which has Countries name with their capitals.

# In[2]:


capitals = {'Pakistan':'Islamabad','India': 'Dehli','Bangadesh':'Dhaka','Afghanistan': 'Kabul', 'Australia': 'Canberra','Azerbaijan':'Baku','Brazil':'Brasilia'}


# In[62]:


capitals


# ##### Added new countries and their capitals in the existing list 

# In[8]:


capitals['Germany']='Berlin City'


# In[9]:


capitals


# In[10]:


capitals['France'] = 'Paris'


# In[11]:


capitals


# ##### Applied the IF Condition to check if the desired country exist is the dictionay and print appropriate messege fot it.

# In[13]:


if 'France' in capitals:
    print('Yes France is in the dictionay and its capital is Paris')
else:
    print('Sorry I could not find it')


# ## Task 2: Comparison Operators, Logical Operators, and If/Else 

# ##### Applied the conditional formating to check the even and odd number and print messges based on their nature

# In[24]:


user_input = input("Enter a number: ")

number = int(user_input)

if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")


# ##### Applied the If condition to check the admission eligibilty based on two factors AGE and GPA

# In[32]:


Age_input = input("Your age at the time of application: ")
age = int(Age_input)  

GPA_input = input("Your GPA in latest Degree: ")
gpa = float(GPA_input.strip(']'))  


if 18 <= age <= 35 and gpa >= 2.5:
    print(" Your are wellcome ): You are eligible for admission")
else:
    print("Soryy! You are not eligible for admission, try next time")




# ## Task 3: Advanced Data Types

# #### Fruit Basket 

# In[33]:


fruits_set = {
    'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 
    'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine', 
    'orange', 'papaya', 'quince'
}

print(fruits_set)


# #### Sets and application of various operation on them

# In[34]:


Set1 = {1,2,3,4,5,6,7,8,9,10,11,12,2,3,1,3,4,2,4,2,22,33,22,12,11,14,13,13,}


# In[36]:


Set2 = { 32,22,21,1,2,3,4,5,7,9,2,4,1,2,1,3,1,4,1,12,14,14,12,14,14,14,12,14}


# In[39]:


union_result = Set1.union(Set2)


# In[45]:


intersection_result = Set1.intersection(Set2)
 


# In[40]:


difference_result_1 = Set1.difference(Set2)


# In[41]:


difference_result_2 = Set2.difference(Set1)  


# In[42]:


is_subset_result_1 = Set1.issubset(Set2)  


# In[43]:


is_subset_result_2 = Set2.issubset(Set1) 


# In[46]:


union_result, intersection_result, difference_result_1, difference_result_2, is_subset_result_1, is_subset_result_2


# ## Task 4: Strings Manipulation 

# In[47]:


sentence = "My name is good M.Hamid Khan, I am the student of Data Science at Atomcamp"


# In[48]:


length = len(sentence)  


# In[49]:


uppercase_sentence = sentence.upper() 


# In[50]:


replaced_sentence = sentence.replace("good", "excellent")  


# In[51]:


check_substring = "Data Science" in sentence 


# In[53]:


split_sentence = sentence.split() 


# In[56]:


length


# In[57]:


uppercase_sentence


# In[58]:


replaced_sentence


# In[59]:


check_substring


# In[60]:


split_sentence


# In[ ]:




