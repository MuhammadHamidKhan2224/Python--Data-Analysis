#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[5]:


import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# In[9]:


df = pd.read_csv(r"C:/Users/DELL/Desktop/Atomcamp Python/homicide_by_countries.csv")


# In[94]:


df.head


# In[95]:


df['Region'].replace('Americas', 'N/S America', inplace=True)


# In[96]:


df.head


# In[97]:


df.shape


# In[98]:


df.dropna(inplace=True)


# In[99]:


df.isnull().sum()


# In[20]:


df["Location"].count()


# In[100]:


df["Location"].unique()


# In[101]:


df.columns


# # Unique count by each column/attribute

# In[24]:


df['Location'].nunique()


# In[25]:


df['Region'].nunique()


# In[26]:


df['Subregion'].nunique()


# In[28]:


df['Year'].nunique()


# # Data Types of each variable 

# In[33]:


df.dtypes


# # Converting datatype from float to integer 

# In[35]:


df['Rate'] = df['Rate'].astype(int)


# In[37]:


df.dtypes


# In[103]:


df1 = df.sort_values("Count", ascending = False).reset_index(drop= True)


# In[102]:


df1


# In[104]:


df2 = df[['Location', 'Count']].sort_values(by = 'Count', ascending = False).head(5)


# In[105]:


df2


# In[113]:


df2.plot(kind='pie', y='Count', labels=df2['Location'],  autopct='%1.1f%%', figsize=(8, 4))
plt.legend(loc='upper left', bbox_to_anchor=(1.5, 1), title='Location')
plt.show()


# In[107]:


df3 = df.groupby('Region')['Count'].sum().sort_values(ascending=False)


# In[108]:


df3


# In[112]:


df3.plot(kind = 'bar')
plt.show()


# In[117]:


df4 = df.groupby('Subregion')['Count'].sum().sort_values(ascending=False)
df4


# In[118]:


df4.values


# In[119]:


df4.index


# In[121]:


sns.barplot(x= df4.index, y = df4.values)
plt.xticks(rotation = "vertical")


# In[122]:


df


# In[123]:


df.Year.value_counts()


# In[126]:


df[df['Region'].isin(['Asia','Europe'])]


# In[129]:


df5 = df[(df['Region'] == 'Asia') | (df['Region'] == 'Europe') ]


# In[133]:


df5 = df5[df ['Year']> 2016][['Region', 'Year', 'Count']]


# In[134]:


df5


# In[135]:


df5 = df5.groupby(['Region', 'Year']).sum()['Count']


# In[136]:


df5


# In[143]:


df_unstacked = df5.unstack(level=0)


# In[144]:


df_unstacked


# In[150]:


df_unstacked.index = df_unstacked.index.astype(int).astype(str)


# In[152]:


df_unstacked.plot(kind='line', figsize = (10,6))
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Count of Asia and Europe over years')
plt.show()


# In[153]:


df


# In[157]:


df6 = df.groupby('Year')['Rate'].sum().sort_values(ascending=False)


# In[158]:


df6


# In[164]:


df6.plot(kind = "bar", figsize = (7,3), color = 'skyblue', edgecolor = 'black')
plt.xlabel('Region, Year')
plt.ylabel('Sum of Rate')
plt.title('Sum of rate by region and year ')
plt.show()


# In[167]:


df7 = df[['Year', 'Region','Count']]
df7 =df7.groupby(['Year','Region']).sum().sort_values(by='Year', ascending = False).head(40)


# In[168]:


df7


# In[172]:


df7.plot(kind='bar', figsize=(12,6),color = 'skyblue', edgecolor = 'black')
plt.xlabel('Year, Region')
plt.ylabel('Sum of count')
plt.title('Sum of count by year and region')
plt.show()


# In[177]:


df8 = df.groupby('Subregion')['Count'].mean().sort_values(ascending = False).round(2)
df8


# In[178]:


df8.index


# In[179]:


df8.values


# In[180]:


data = {
    'category':df8.index,
    'values': df8.values,
    'info': df8.values
}
df = pd.DataFrame(data)
df


# In[184]:


fig = px.treemap(df, path=['category'], values='values', title='TreeMap')
fig.update_traces(hovertemplate='category:%{label}<br>value:%{value}')
fig.show()


#   #                                                     The End

# In[ ]:




