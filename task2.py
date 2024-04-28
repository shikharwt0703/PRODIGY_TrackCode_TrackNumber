#!/usr/bin/env python
# coding: utf-8

# # Task -02 Data Cleaning and EDA

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


data = pd.read_csv('covid.csv')


# In[4]:


data


# In[5]:


data.count()


# In[6]:


data.isnull().sum()


# In[7]:


# We can see this null values results in the form of heatmap

sns.heatmap(data.isnull())
plt.show()


# # Performing EDA on the covid dataset

# # 1. Show the number of confirmed, Deaths and Recovered cases in each Region

# In[8]:


#df.groupby('Region').sum().head(50)
#df.groupby('Region')['Confirmed'].sum().sort_Values(ascending=False).head(20)
#df.groupby('Region')['Confirmed, 'Recovered].sum()


# In[9]:


data.head(2)


# In[10]:


data.groupby('Region').sum().head(20)


# In[11]:


data.groupby('Region')['Confirmed'].sum().sort_values(ascending = False).head(10)


# In[12]:


data.groupby('Region')['Confirmed', 'Recovered'].sum()


# # 2. Remove all the records where Confirmed Cases is Less Than 10.

# In[13]:


#df.Confirmed < 10
#df[df.Confirmed < 10]
#df[~(df.Confirmed < 10)]
#df = df{~(df.Confirmed < 10)}


# In[14]:


data.head(2)


# In[16]:


data[data.Confirmed < 10] 


# In[17]:


data[(data.Confirmed < 10)]


# In[18]:


data = data[~(data.Confirmed < 10)]  # To remove the records satisfying a particular condition


# In[19]:


data


# In[20]:


data.head(20)


# # 3. In which Region, maximum number of Confirmed cases were recorded?

# In[21]:


#df.groupby('Region').Confirmed.sum().sort_values(ascending = False).head(20)


# In[22]:


data.head(2)


# In[23]:


data.groupby('Region').Confirmed.sum().sort_values(ascending = False).head(20)


# # 4. In which Region, minimum number of Deaths cases were recorded ?

# In[25]:


data.head(2)


# In[26]:


data.groupby('Region').Deaths.sum().sort_values(ascending = True).head(50)


# # 5. How many Confirmed, Deaths and Recovered cases were reported from India till 29 April 2020?

# In[27]:


data.head(2)


# In[28]:


data[data.Region == 'India']


# # 6.a  Sort the entire data wrt No. of Confirmed cases in ascending order.

# In[29]:


#df.sort_values(by = ['Confirmed'], ascending = True)


# In[30]:


data.head(2)


# In[31]:


data.sort_values(by = ['Confirmed'],ascending = True)


# # 6.b Sort the entire data wrt No. of Recovered cases in descending order

# In[32]:


data.sort_values(by = ['Recovered'], ascending = False)


# In[ ]:




