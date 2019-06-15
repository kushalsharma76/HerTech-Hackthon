import pandas as pd 
import numpy as np
import warnings
warnings.filterwarnings('ignore')
student_data_extra_curricular = pd.read_csv("C:/Users/Prushaltech/Desktop/HerTech Hackathon/Datasets/our data/student_data_extra_curricular.csv")
# student_data_extra_curricular.head()
student_data_behaviour = pd.read_csv("C:/Users/Prushaltech/Desktop/HerTech Hackathon/Datasets/our data/student_data_behaviour.csv")
# student_data_behaviour.head()
student_data_academic = pd.read_csv("C:/Users/Prushaltech/Desktop/HerTech Hackathon/Datasets/our data/student_data_academic.csv")
# student_data_academic.head()
student_data_parent_opinion = pd.read_csv("C:/Users/Prushaltech/Desktop/HerTech Hackathon/Datasets/our data/student_data_parent_opinion.csv")
# student_data_parent_opinion.head()
student_data_sm_hobbies = pd.read_csv("C:/Users/Prushaltech/Desktop/HerTech Hackathon/Datasets/our data/student_data_sm_hobbies.csv")
# student_data_sm_hobbies.head()
student_data_academic.describe()
# print(student_data_academic.iloc(1))
#type(student_data_academic)
#student_data_academic[1:2,"":"",:]
#student_data_academic.head()
#print(student_data_academic['Student ID'])

#student_data_academic.loc[0:2,"Student ID"]
#GET the column names in from the data frame
col1 = list(student_data_academic.columns)
print(col1[0])

s1 = list(student_data_academic.iloc[0])
s2 = list(student_data_academic.iloc[0])

print(s1)

# to find largest of a column
#student_data_academic.nlargest(4,'Bio')

# find largest n values from a row
##-- not yet found
# finds for each column
#student_data_academic.max(axis = 0)

student = []
print(len(s1))
id = s1[0]
max1 = max(s1)
sub1 = s2.index(max1)
subname1 = col1[sub1]
print("id: ",id, "\nsub1: ", sub1, "\nSubject: ", subname1, "\nmax1: ",max1)
s1.remove(max(s1))
#print(s1)

id = s1[0]
max2 = max(s1)
sub2 = s2.index(max2)
subname2 = col1[sub2]
print("id: ",id, "\nsub2: ", sub2, "\nSubject: ", subname2, "\nmax1: ",max2)

s1.remove(max(s1))

id = s1[0]
max3 = max(s1)
sub3 = s2.index(max3)
subname3 = col1[sub3]
print("id: ",id, "\nsub3: ", sub3, "\nSubject: ", subname3, "\nmax1: ",max3)
