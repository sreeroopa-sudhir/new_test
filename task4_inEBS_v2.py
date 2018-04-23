
# coding: utf-8

# In[31]:


from pymongo import MongoClient
import pprint
from IPython.display import clear_output
import matplotlib.pyplot as plt
import numpy as np


# In[32]:


client = MongoClient("mongodb://localhost:27017/dbOps_18_04_17")


# In[50]:


# KPI #4 No. of Bags that are in the EBS
# We're using the LMX table here


#pipeline1 for testing purposes only
pipeline1 = [
    {
        '$sortByCount' : "$CATEGORY"
    }
  
]

pipeline3 = [
    {
        '$match' : { 'KEY' : "INEBS" }  
    },
    {
        '$match' : { 'SUBKEY' : "TOTAL" }  
    },
    {
        '$match' : { 'CATEGORY' : "BAGSINSYSTEM" }  
    },
    {
        '$project' : { 'EVENTTIME' : 1, 'VALUE':1 }
    }
    
]


stats= list(client.dbOps_18_04_17.lmx.aggregate(pipeline3))
pprint.pprint(stats)
# ^ this prints a list of times and values, where the values indicate the number of bags in the EBS at that time.


labels = []
counts = []

l = stats

for item in l:
    labels.append(item["EVENTTIME"])
    counts.append(item["VALUE"])

plt.clf()

fig, ax = plt.subplots()

ax.scatter(labels, counts)

plt.show()



    

