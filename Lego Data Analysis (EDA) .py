#!/usr/bin/env python
# coding: utf-8

# # ----------------------------------Exploratory Data Analysis----------------------------------------

# # ------------------------------------Import Basic Libraries-------------------------------------------

# In[27]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # ---------------------------------------Import both Datasets------------------------------------------

# In[30]:


lego = pd.read_csv('lego_sets.csv')


# In[31]:


lego.head(5)


# In[32]:


theme = pd.read_csv('parent_themes.csv')


# In[38]:


theme.head(5)


# In[95]:


lego.columns


# In[96]:


theme.columns


# In[97]:


lego.shape


# In[98]:


theme.shape


# In[101]:


lego.describe().T


# In[102]:


theme.describe().T


# In[104]:


lego.info()


# In[105]:


theme.info()


# In[111]:


lego.isnull().sum()


# In[113]:


lego.duplicated().sum()


# In[114]:


theme.duplicated().sum()


# In[112]:


theme.isnull().sum()


# In[109]:


max_df = summed_df.sort_values('num_parts', ascending=False).drop_duplicates(['year'])
max_df.head()


# In[110]:


summed_df['count'] = summed_df.groupby('year')['year'].transform('count')
max_df = summed_df.sort_values('count', ascending=False).drop_duplicates(['year'])
max_df.head()


# # --------------------------------------Merged the dataset----------------------------------------------

# In[94]:


merged = df.merge(theme, left_on='parent_theme', right_on='name')


# In[ ]:


merged.drop(columns='name_y', inplace=True)


# In[43]:


merged.head(5)


# In[44]:


licensed = merged[merged['is_licensed']]
licensed.head()


# In[47]:


star_wars = licensed[licensed['parent_theme'] == 'Star Wars']
star_wars.head(50)


# In[53]:


merged['set_num'].isnull().sum()


# In[54]:


licensed = licensed.dropna(subset=['set_num'])


# In[49]:


star_wars.shape[0]


# In[73]:


the_force = int(star_wars.shape[0]/licensed.shape[0]*100)
the_force


# In[62]:


licensed_sorted = licensed.sort_values('year')
licensed_sorted


# In[63]:


licensed_sorted.groupby(['year','parent_theme']).head(50)


# In[80]:


licensed_sorted['count '] = 1
licensed_sorted.head()


# In[84]:


summed_df = licensed_sorted.groupby(['year','parent_theme']).sum().reset_index()


# In[85]:


summed_df.head()


# # 1. Year-wise Distribution of LEGO Sets

# In[88]:


plt.figure(figsize=(14, 7))
sns.countplot(data=lego, x='year', color='skyblue')
plt.xticks(rotation=90)
plt.title('Year-wise Distribution of LEGO Sets')
plt.xlabel('Year')
plt.ylabel('Number of Sets Released')
plt.tight_layout()
plt.show()


# # 2. Top LEGO Themes by Set Count

# In[89]:


top_themes = lego['theme_name'].value_counts().head(10)
plt.figure(figsize=(14, 7))
sns.barplot(x=top_themes.index, y=top_themes.values, palette="viridis")
plt.xticks(rotation=45)
plt.title('Top LEGO Themes by Set Count')
plt.xlabel('Theme Name')
plt.ylabel('Number of Sets')
plt.tight_layout()
plt.show()


# # 3. Top LEGO Themes by Set Count

# In[90]:


plt.figure(figsize=(14, 7))
yearly_avg_parts = lego.groupby('year')['num_parts'].mean()
sns.lineplot(x=yearly_avg_parts.index, y=yearly_avg_parts.values, color='tomato')
plt.title('Year-wise Average Number of Parts in LEGO Sets')
plt.xlabel('Year')
plt.ylabel('Average Number of Parts')
plt.tight_layout()
plt.show()


# # 4. Distribution of Licensed vs. Non-Licensed Sets

# In[91]:


plt.figure(figsize=(7, 7))
licensed_counts =merged['is_licensed'].value_counts()
plt.pie(licensed_counts, labels=['Non-Licensed', 'Licensed'], autopct='%1.1f%%', startangle=140, colors=['lightgreen', 'lightblue'])
plt.title('Distribution of Licensed vs. Non-Licensed Sets')
plt.tight_layout()
plt.show()


# # 5. Number of Sets by Parent Theme for Licensed Themes Only

# In[93]:


licensed_sets = merged[merged['is_licensed'] == True]
sets_by_parent_theme = licensed_sets['parent_theme'].value_counts().head(10)

plt.figure(figsize=(14, 7))
sns.barplot(x=sets_by_parent_theme.index, y=sets_by_parent_theme.values, palette="coolwarm")
plt.xticks(rotation=45)
plt.title('Number of Sets by Parent Theme for Licensed Themes')
plt.xlabel('Parent Theme')
plt.ylabel('Number of Sets')
plt.tight_layout()
plt.show()


# # -------------------------------------------- The End -----------------------------------------------------

# In[ ]:




