#!/usr/bin/env python
# coding: utf-8

# # -------------------------------Exploratory Data Analysis-------------------------------------------
#                                            
#                                           

# # --------------------------------------Importing libraries-----------------------------------------------

# In[6]:


import pandas as pd
import numpy as np


# In[25]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# # -------------------------------------Importing Dataset------------------------------------------------ 

# In[4]:


covid = pd.read_csv("C:/Users/DELL/Desktop/Atomcamp Python/COVID_cinical.csv")


# # 1.	Read Dataset and Explore the dataset by checking shape, columns, see the first/last 'n' rows using head/tail. 

# # Top rows of the dataset  (n= 5,15,30) 

# In[80]:


covid.head(5)        # Top 5 Rows


# In[81]:


covid.head(15)   # Top 15 rows      


# In[82]:


covid.head(30) # Top 30 Rows


# # Bottom rows of the dataset    (n= 5,15,30) 

# In[87]:


covid.tail(5)   # Bottom 5 rows 


# In[88]:


covid.tail(15)   # Bottom 15 rows


# In[89]:


covid.tail(30)  # Bottom 30 rows


# # To get columns with their title in the dataset 

# In[5]:


covid.columns


# # To check total number of columns and rows in the dataset

# In[6]:


covid.shape


# # To get filimar with dataset, Wholestic overview of the data

# In[8]:


covid.info()


# # To get the summary statictics of the numerical data 

# In[13]:


covid.describe().T


# # Enrollment mean value is 18319.48860. The Maximum enrollment rate in 20000000.0. So, comparatively average rate in minimal.

# # To get the summary statictics of the non-numerical data 

# In[85]:


covid.describe(include=[object])


# # -------------Select all columns for the first clinical trial in the dataset.-----------------

# In[5]:


x = covid.loc[0]
df_1 = pd.DataFrame(x)

df_1


# # Setting a custom indexing

# In[76]:


covid.set_index('NCT Number', inplace=True)


# # Retrieve the Title and Status of the clinical trial with the NCT Number 'NCT04595136'.

# In[78]:


x = covid.loc['NCT04595136', ['Title', 'Status']]
df2 = pd.DataFrame(x)
df2


# # Get the Sponsor/Collaborators and Start Date for clinical trials that are Recruiting.

# In[70]:


covid[covid['Status'] == 'Recruiting'][['Sponsor/Collaborators','Start Date']]


# # Select the first 5 rows and columns Title, Conditions, and Outcome Measures.

# In[63]:


covid.iloc[0:5, [2,6,8]]


# # -Find the Completion Date and URL for the last 3 clinical trials in the dataset.-

# In[60]:


covid.iloc[-3:,[20,26]]


# # -----Determine the missing values in the whole dataset and analyze missing values in each column.---

# In[14]:


covid.isnull().sum()


# # --------------------------Calculate the sum of duplicate rows----------------------------------

# In[15]:


covid.duplicated().sum()


# # ------------Solve following question by using conditional statements-----------------

# # Mean of the Enrollment

# In[56]:


covid["Enrollment"].mean()


# # 1:How many studies have an enrollment greater than a certain threshold? 

# In[19]:


mean = covid["Enrollment"].mean()
num_studies = (covid["Enrollment"] > mean).sum()
print(f"Number of studies with enrollment rate higher than the mean: {num_studies}")


# # 2:How many clinical trials have 'No Results Available'? 

# In[32]:


no_rst_count = (covid['Study Results'] == 'No Results Available').sum()
print(f'Number of Study Results: {no_rst_count}')


# # 3:How many clinical trials are in an "Completed" and "Recruiting" status? 

# In[44]:


completed_count = (covid['Status'] == "Completed").sum()
recruiting_count = (covid['Status'] == "Recruiting").sum()
print(f'Number of Clinical Trials (Completed): {completed_count}')
print(f'Number of Clinical Trials (Recruiting): {recruiting_count}')


# # 4:How many clinical trials are related to 'COVID-19'? 

# In[51]:


covid_cases = (covid['Conditions'] == 'Covid 19').sum()
print(f'Number of Covid 19 Cases: {covid_cases}')


# # 5:How many clinical trials started after January 1, 2020?

# In[54]:


strt_date = (covid['Start Date'] == 'January 1, 2020').sum()
print(f'Number of days with stating date in Jan: {strt_date}')


# # 1. Distribution of Study Statuses
# 

# In[10]:


study_statuses = covid['Status'].value_counts()


# In[11]:


print(study_statuses)


# In[19]:


plt.figure(figsize=(10, 6))
study_statuses.plot(kind='bar')
plt.title('Distribution of Study Statuses')
plt.xlabel('Status')
plt.ylabel('Number of Studies')
plt.xticks(rotation=45)
plt.show()


# # 2. Number of Studies Over Time

# In[20]:


covid['Start Date'] = pd.to_datetime(covid['Start Date'], errors='coerce')
covid['YearMonth'] = covid['Start Date'].dt.to_period('M')
studies_over_time = covid['YearMonth'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
studies_over_time.plot(kind='line')
plt.title('Number of Studies Over Time')
plt.xlabel('Time (Year-Month)')
plt.ylabel('Number of Studies')
plt.xticks(rotation=45)
plt.show()


# # 3. Top Conditions Studied

# In[21]:


top_conditions = covid['Conditions'].value_counts().head(10)
plt.figure(figsize=(10, 6))
top_conditions.plot(kind='bar')
plt.title('Top 10 Conditions Being Studied')
plt.xlabel('Condition')
plt.ylabel('Number of Studies')
plt.xticks(rotation=45)
plt.show()


# # 4. Intervention Types Analysis

# In[23]:


covid['Intervention Type'] = covid['Interventions'].str.split(':').str[0]
intervention_types = covid['Intervention Type'].value_counts()
plt.figure(figsize=(10, 6))
intervention_types.plot(kind='bar')
plt.title('Common Types of Interventions')
plt.xlabel('Intervention Type')
plt.ylabel('Number of Studies')
plt.xticks(rotation=45)
plt.show()


# # 5. Outcome Measures Frequency

# In[27]:


covid['Outcome Measures Count'] = covid['Outcome Measures'].apply(lambda x: len(str(x).split('|')))
plt.figure(figsize=(10, 6))
sns.histplot(covid['Outcome Measures Count'], bins=20)
plt.title('Frequency of Outcome Measures Count')
plt.xlabel('Number of Outcome Measures')
plt.ylabel('Frequency')
plt.show()


# # 6. Study Locations Distribution

# In[28]:


covid['Country'] = covid['Locations'].str.split(',').str[-1]
top_countries = covid['Country'].value_counts().head(10)
plt.figure(figsize=(10, 6))
top_countries.plot(kind='bar')
plt.title('Top 10 Study Locations')
plt.xlabel('Country')
plt.ylabel('Number of Studies')
plt.xticks(rotation=45)
plt.show()


# # 7. Study Sponsors and Collaborators Analysis

# In[30]:


top_sponsors = covid['Sponsor/Collaborators'].value_counts().head(10)
plt.figure(figsize=(10, 6))
top_sponsors.plot(kind='bar')
plt.title('Top Sponsors and Collaborators')
plt.xlabel('Sponsor/Collaborator')
plt.ylabel('Number of Studies')
plt.xticks(rotation=45)
plt.show()


# # --------------------------------------------THE END------------------------------------------------------

# In[ ]:




