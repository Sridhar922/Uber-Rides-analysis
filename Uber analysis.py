#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd # Data processing
import numpy as np # Numerical python i.e Linear Algebra
import matplotlib.pyplot as plt # data visualization
import seaborn as sns # Stastical Visualization


# In[2]:


# import the Data
uber_data= pd.read_csv(r"C:\Users\sridh\Documents\projects\uber analysis\uber-raw-data-apr14.csv")
uber_data


# In[3]:


# checking the null values
uber_data.isnull().sum()


# In[4]:


# checking the Datatypes information in the given dataset
uber_data.info()


# In[5]:


#checking the Stats information
uber_data.describe()


# In[6]:


#Convert the datatype of the Date/Time from object to Datetime and creating the minute, hour, day and dayname
uber_data['Date/Time'] = pd.to_datetime(uber_data['Date/Time'], format="%m/%d/%Y %H:%M:%S")
uber_data['Weekday_name'] = uber_data['Date/Time'].dt.day_name()
uber_data['MonthDayNum'] = uber_data['Date/Time'].dt.day
uber_data['HourOfDay'] = uber_data['Date/Time'].dt.hour
uber_data['MinuteOfDay'] = uber_data['Date/Time'].dt.minute
uber_data


# In[7]:


#datatype object changed to datetime64
uber_data.info()


# In[8]:


weekday= uber_data.pivot_table( index=['Weekday_name'], values= 'Base', aggfunc='count' )
weekday


# In[9]:


weekday.plot(kind='bar')


# In[10]:


weekday_avg= round(weekday/30,2)
weekday_avg


# In[11]:


weekday_avg.plot(kind= 'bar')


# In[12]:


hours= uber_data.pivot_table(index=['HourOfDay'], values= 'Base', aggfunc='count')
hours


# In[13]:


hours.plot(kind='bar')
plt.xlabel('Hour of the Day')
plt.ylabel( 'count')
plt.title('Rides per Hour')


# In[ ]:




