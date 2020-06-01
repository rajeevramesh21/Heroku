#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px


# In[4]:


df=pd.read_excel('New Microsoft Excel Worksheet.xlsx')


# In[5]:


df


# In[7]:


df['YOE'].value_counts().plot(kind='pie')


# In[8]:


fig = px.histogram(df, x='Salary')
fig.show()


# In[12]:


fig = px.pie(df,'Age')
fig.show()


# In[13]:


from sklearn.linear_model import LinearRegression


# In[14]:


y=df['Salary']


# In[15]:


x=df.drop('Salary',axis=1)


# In[19]:


lreg=LinearRegression()


# In[20]:


lreg.fit(x,y)


# In[22]:


lreg.predict(x)


# In[23]:


import pickle


# In[27]:


pickle.dump(lreg,open('salmodel.pkl','wb'))


# In[28]:


model=pickle.load(open('salmodel.pkl','rb'))


# In[33]:


model.predict([[1,25,5]])


# In[ ]:




