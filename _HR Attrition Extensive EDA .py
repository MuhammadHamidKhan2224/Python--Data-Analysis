#!/usr/bin/env python
# coding: utf-8

# # --------------Human Resource Attrition Dataset Exploratory Data Analysis----------

# In[2]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


# In[5]:


hr = pd.read_csv('HR-Attrition.csv')


# In[8]:


hr


# In[11]:


hr_numeric = hr.select_dtypes(include=[np.number])
mean_values = hr_numeric.groupby(['WorkLifeBalance']).mean()


# In[13]:


mean_values.head()


# In[210]:


hr.describe().T


# In[207]:


des_sta = hr.describe(include = ['object'])


# In[209]:


des_sta.T


# In[191]:


# Convert 'OverTime' column to numeric: 1 for 'Yes' and 0 for 'No'

hr['overtime_num'] = hr['OverTime'].apply(lambda x: 1 if x == 'Yes' else 0)


# In[14]:


gbwg = hr.groupby(['WorkLifeBalance'])['HourlyRate'].mean()


# In[203]:


gbwg.head()


# In[16]:


gbwg1 = hr.groupby(['WorkLifeBalance'])[['HourlyRate','Age']].mean()


# In[17]:


gbwg1.head()


# In[21]:


hr.columns


# In[39]:


hr.head()


# In[33]:


hr['Education'].count()


# In[37]:


dfgf =hr.groupby(['JobRole'])[['Attrition','Education']]


# In[25]:


dfgf.head()


# In[49]:


dbef = hr.groupby(['EducationField'])['DailyRate'].mean().round(2)


# In[50]:


dbef.head()


# In[61]:


dbef.plot(kind='hist')
plt.title('Histogram for Average Education Field')
plt.xlabel('Avg Daily Rate')
plt.ylabel('Frequency')
plt.show()


# In[62]:


hr.head()


# In[81]:


unique_departments = hr['Department'].unique()
unique_departments


# In[83]:


unique_EducationField =  hr['EducationField'].unique()
unique_EducationField


# In[91]:


same_dpt_field = hr[(hr['EducationField']== 'Human Resources') & (hr['Department']=='Human Resources')]
indexes = same_dpt_field.index
indexes


# In[87]:


same_dpt_filed


# In[67]:


Total_year_more_than_five = hr[hr['TotalWorkingYears'] > 5][['Department', 'TotalWorkingYears']]


# In[68]:


Total_year_more_than_five.head()


# In[92]:


hr.columns


# # Group by 'Department' and calculate mean 'Attrition' rate
# 

# In[151]:


# Convert 'Attrition' column to numeric: 1 for 'Yes' and 0 for 'No'

hr['Attrition_num'] = hr['Attrition'].apply(lambda x: 1 if x == 'Yes' else 0)


# In[154]:


dpt_attr_rate = hr.groupby('Department')['Attrition_num'].mean()


# In[164]:


dpt_attr_rate


# # Correlation analysis between 'DistanceFromHome' and 'JobSatisfaction'
# 

# In[182]:


corr1 = hr[['DistanceFromHome','JobSatisfaction']].corr


# In[183]:


corr1()


# # Group by 'JobRole' and 'Education' to analyze 'MonthlyIncome'
# 

# In[173]:


mnt_salary =  hr.groupby(['JobRole', 'Education'])['MonthlyIncome'].mean()


# In[178]:


mnt_salary


# # Group by 'Department' and calculate average 'WorkLifeBalance'
# 

# In[179]:


avg_work_life_balance =  hr.groupby( 'Department' )['WorkLifeBalance'].mean()


# In[181]:


avg_work_life_balance


# # Correlation or comparison between 'YearsWithCurrManager' and 'YearsSinceLastPromotion'
# 

# In[184]:


corr2 = hr[['YearsWithCurrManager','YearsWithCurrManager']].corr


# In[186]:


corr2()


# # Use correlation or groupby analysis with 'PerformanceRating', 'JobInvolvement', and 'OverTime'
# 

# In[196]:


corr3= hr[['PerformanceRating', 'JobInvolvement']].corr()


# In[198]:


corr3


# # Correlation analysis between 'TrainingTimesLastYear' and 'PerformanceRating'
# 

# In[199]:


corr4 = hr[['TrainingTimesLastYear','PerformanceRating']].corr


# In[201]:


corr4()


# In[101]:


pd.set_option('display.max_columns', None)


# In[102]:


hr.head()


# In[140]:


emply_count = hr.groupby('Department')['EmployeeCount'].count()


# In[146]:


emply_count.T


# In[131]:


gndr_by_dpt = hr.groupby('Department')['Gender'].value_counts().unstack()


# In[132]:


gndr_by_dpt


# In[129]:


count_over_time_martial_status = hr.groupby('MaritalStatus')['OverTime'].value_counts().unstack()


# In[123]:


count_over_time_martial_status


# In[124]:


joblevel_by_gender = hr.groupby('Gender')['JobLevel'].value_counts().unstack()


# In[126]:


joblevel_by_gender.T


# In[ ]:




