#!/usr/bin/env python
# coding: utf-8

# # ----------------------------------Exploratory Data Analysis--------------------------------------
# 
# # -------For this EDA data is taken from Kaggle, This data set is about HR---------

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[72]:


hr = pd.read_csv("C:/Users/DELL/Desktop/Atomcamp Python/data_science.csv")


# In[22]:


hr.head(10)


# In[23]:


hr.shape


# In[34]:


hr.drop(['Unnamed: 0', 'salary'], axis= 1, inplace= True)


# In[35]:


hr


# # Average Salary by each job title

# In[41]:


average_salaries = hr.groupby('job_title')['salary_in_usd'].mean().reset_index().sort_values(by='salary_in_usd', ascending=False)


# In[42]:


average_salaries


# # Top 10 job titles by salary 

# In[43]:


top_10_salaries = average_salaries.sort_values(by='salary_in_usd', ascending=False).head(10)


# In[44]:


top_10_salaries


# # Bar Chart for top 10 job title by salary 

# In[45]:


plt.figure(figsize=(10, 8))
plt.barh(top_10_salaries['job_title'], top_10_salaries['salary_in_usd'], color='skyblue')
plt.xlabel('Average Salary in USD')
plt.ylabel('Job Title')
plt.title('Top 10 Job Titles by Average Salary')
plt.gca().invert_yaxis() 
plt.show()


# # Ratio of remote employees based on company size

# In[57]:


remt_ratio = hr.groupby('company_size')['remote_ratio'].mean().reset_index().round(2)


# In[58]:


remt_ratio


# In[62]:


work_years = hr.groupby('work_year')['salary_in_usd'].mean().reset_index().round(2)


# In[63]:


work_years


# In[69]:


work_years = hr.groupby('work_year')['salary_in_usd'].mean().round(2)
work_years.plot(kind='bar')
plt.show()


# In[76]:


df3 = hr.company_size.value_counts()
df3


# In[77]:


df3.index.to_list()


# In[82]:


values2 = df3.to_list()
values2


# In[88]:


labels_for_company = ['Medium','Small','Large']


# In[92]:


plt.figure(figsize=(8,6))
plt.pie(x=values2, labels=None, autopct='%1.2f%%', shadow=True)  
plt.legend(labels_for_company, loc = 'upper right')
plt.axis('equal')
plt.title('Company Size')
plt.show()


# In[99]:


df4= hr.job_title.value_counts().head(5)
df4


# In[104]:


plt.figure(figsize=(12,6))
sns.barplot(x=df4.index, y=df4.values,palette='viridis')
plt.title('Top Five Job Title')
plt.ylabel('Count')
plt.xticks(rotation = -20)
plt.show()


# In[142]:


df5= hr.experience_level.value_counts()
df5


# In[144]:


exp_map = {
    'SE': 'Senior level',
    'MI': 'Middle Level',
    'EN': 'Entry Level',
    'EX': 'Executive Level'
}


# In[150]:


df5.index.to_list()


# In[145]:


hr['experience_level'].replace(exp_map, inplace=True)


# In[151]:


values = df5.values
values


# In[155]:


plt.figure(figsize=(6,12))
plt.pie(x = values, labels= labels, autopct = '%1.2f%%',shadow=True)
plt.show()


# In[ ]:




