#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/Chaganti-Reddy/US-Accidents-EDA/blob/main/US_Accidents_EDA.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# In[1]:


# Jovian Commit Essentials
# Please retain and execute this cell without modifying the contents for `jovian.commit` to work
get_ipython().system('pip install jovian --upgrade -q')
import jovian
jovian.set_project('us-accidents-eda')
jovian.set_colab_id('1TzuBPqc9BzSEJeWaL-jhiqadtlVNB08H')


# # US Accidents Exploratory Data Analysis

# ## Download the Dataset

# In[2]:


pip install opendatasets --upgrade --quiet


# In[3]:


import opendatasets as od

download_url = 'https://www.kaggle.com/sobhanmoosavi/us-accidents'

od.download(download_url)


# In[4]:


data_filename = './us-accidents/US_Accidents_Dec21_updated.csv'


# ## Data Preparation and Cleaning

# In[5]:


# Imports

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")
get_ipython().run_line_magic('pip', 'install folium --quiet')
import folium
from folium.plugins import HeatMap


# In[6]:


df = pd.read_csv(data_filename)
df


# In[7]:


df.info()


# In[8]:


df.describe()


# In[9]:


numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

numeric_df = df.select_dtypes(include=numerics)
len(numeric_df.columns)


# In[10]:


numeric_df.head()


# ### Percentage of missing values per column

# In[11]:


missing_percentages = df.isna().sum().sort_values(ascending=False) / len(df)
missing_percentages


# In[12]:


type(missing_percentages)


# In[13]:


missing_percentages[missing_percentages != 0].plot(kind='barh', figsize=(20,10))


# In[14]:


df.City


# In[15]:


cities = df.City.unique()
len(cities)


# In[16]:


cities_by_accident = df.City.value_counts()
cities_by_accident


# In[17]:


cities_by_accident[:20]


# In[18]:


type(cities_by_accident)


# In[19]:


cities_by_accident[:25].plot(kind='barh', figsize=(20,10))


# In[20]:


fig, ax = plt.subplots(figsize=(20, 10))
sns.histplot(cities_by_accident, log_scale=True, ax=ax)


# In[21]:


cities_by_accident[cities_by_accident == 1]


# In[22]:


df.Start_Time


# In[23]:


df.Start_Time = pd.to_datetime(df.Start_Time)

sns.distplot(df.Start_Time.dt.hour, bins=24, kde=False, norm_hist=True)


# + A high percentage of accidents occur between 6 am to 10 am (probably people in a hurry to get to work)
# + Next higest percentage is 3 pm to 6 pm.

# In[24]:


sns.distplot(df.Start_Time.dt.dayofweek, bins=7, kde=False, norm_hist=True)


# Is the distribution of accidents by hour the same on weekends as on weekdays.

# In[25]:


sundays_start_time = df.Start_Time[df.Start_Time.dt.dayofweek == 6]
sns.distplot(sundays_start_time.dt.hour, bins=24, kde=False, norm_hist=True)


# In[26]:


monday_start_time = df.Start_Time[df.Start_Time.dt.dayofweek == 0]
sns.distplot(monday_start_time.dt.hour, bins=24, kde=False, norm_hist=True)


# On Sundays, the peak occurs between 10 am and 3 pm, unlike weekdays

# In[29]:


df.Start_Lat


# In[30]:


df.Start_Lng


# In[31]:


sample_df = df.sample(int(0.1 * len(df)))


# In[32]:


sns.scatterplot(x=sample_df.Start_Lng, y=sample_df.Start_Lat, size=0.001)


# In[33]:


lat, lon = df.Start_Lat[0], df.Start_Lng[0]
lat, lon


# In[34]:


for x in df[['Start_Lat', 'Start_Lng']].sample(100).iteritems():
    print(x[1])


# In[35]:


zip(list(df.Start_Lat), list(df.Start_Lng))


# In[36]:


sample_df = df.sample(int(0.001 * len(df)))
lat_lon_pairs = list(zip(list(sample_df.Start_Lat), list(sample_df.Start_Lng)))


# In[37]:


map = folium.Map()
HeatMap(lat_lon_pairs).add_to(map)
map


# ## Summary and Conclusion
# Insights:
# 
# + No data from New York
# + The number of accidents per city decreases exponentially
# + Less than 5% of cities have more than 1000 yearly accidents.
# + Over 1200 cities have reported just one accident (need to investigate)

# In[38]:


jovian.commit()


# In[ ]:




