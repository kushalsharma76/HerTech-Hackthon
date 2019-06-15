#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import warnings
warnings.filterwarnings('ignore')


# In[3]:


student_data_parent_opinion = pd.read_csv("C:/Users/Prushaltech/Desktop/HerTech Hackathon/Datasets/our data/student_data_parent_opinion.csv")
student_data_parent_opinion.head()


# In[7]:


s1 = student_data_parent_opinion.iloc[0]
print(s1)
sl1 = list(s1)
print(sl1)
id = sl1[0]
print("id: ", id)


# In[9]:


t = sl1[1].split(" ")
p1 = sl1[2].split(" ")
p2 = sl1[3].split(" ")

print("Teaccher : ", t)
print("Parent 1 : ", p1)
print("Parent 2 : ",p2)


# In[17]:


word = ["Maths","Engineer", "Art"]
for i in word:
    for a in t:
        if(i==a):
            print(a)
for i in word:
    for a in p1:
        if(i==a):
            print(a)
for i in word:
    for a in p2:
        if(i==a):
            print(a)

