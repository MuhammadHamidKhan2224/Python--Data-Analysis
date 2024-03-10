#!/usr/bin/env python
# coding: utf-8

# # --------------                  The data analysis focuses on a dataset related to health, specifically a case study of life expectancy in Afghanistan. This dataset is sourced from Kaggle.-------------

# # --------------------------------------Import Libraries--------------------------------------------------

# In[44]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# # ----------------------------------------Read Dataset----------------------------------------------------

# In[45]:


data = pd.read_csv('C:/Users/DELL/Desktop/Atomcamp Python/Life Expectancy Data.csv')


# In[46]:


data.head(10)


# In[48]:


data.describe()


# In[49]:


data.isnull().sum()


# In[50]:


data.dropna(inplace=True)


# In[52]:


data.isnull().sum()


# In[53]:


data.head()


# In[54]:


data.tail()


# # --------------------------------------Data Sanity Check----------------------------------------------

# In[55]:


data.shape # Clean data without missing and duplicate values


# In[56]:


data.info() # Cleaned data without any error


# In[57]:


df.duplicated().sum()


# In[63]:


for i in df.select_dtypes(include='object').columns:
    print(df[i].value_counts())
    print("-----"*10)


# # ---------------------------------Exploratory Data Analysis ----------------------------------------

# In[65]:


data.describe().T


# In[67]:


data.describe(include='object').T


# In[69]:


for i in data.select_dtypes(include='number').columns:
    sns.histplot(data=data,x=i)
    plt.show()


# In[70]:


for i in data.select_dtypes(include='number').columns:
    sns.boxplot(data=data,x=i)
    plt.show()


# In[71]:


data.select_dtypes(include='number').columns


# In[83]:


cols = ['Year', 'Adult Mortality', 'infant deaths', 'Alcohol', 'percentage expenditure', 
        'Hepatitis B', 'Measles ', ' BMI ', 'under-five deaths ', 'Polio', 
        'Total expenditure', 'Diphtheria ', ' HIV/AIDS', 'GDP', 'Population', 
        ' thinness  1-19 years', ' thinness 5-9 years', 
        'Income composition of resources', 'Schooling']

for col in cols: 
    sns.scatterplot(data=data, x=col, y='Life expectancy ')
    plt.title(f'Scatter Plot for {col}')
    plt.xlabel(col)
    plt.ylabel('Life expectancy')
    plt.show()


# In[84]:


corelation = data.select_dtypes(include='number').corr()


# In[85]:


corelation


# In[86]:


plt.figure(figsize=(15,15))
sns.heatmap(corelation, annot=True, fmt=".2f",linewidths=.5)


# # Outliers Treatment

# In[100]:


def wisker(cpl):
    q1, q3 = np.percentile(cpl, (25, 75))
    iqr = q3 - q1
    lw = q1 - 1.5 * iqr
    uw = q3 + 1.5 * iqr  
    return lw, uw


# In[101]:


wisker(data[ 'Life expectancy '])


# # ------------------------------------------THE END --------------------------------------------------------

# In[ ]:




