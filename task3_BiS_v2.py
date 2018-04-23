
# coding: utf-8

# In[1]:


from pymongo import MongoClient
import pprint
from IPython.display import clear_output


# In[2]:


client = MongoClient("mongodb://localhost:27017/dbOps_18_04_17")


# In[4]:


# KPI #3 Bags in System
# version 2

# We're using the LMX table here. 
# version 1 used lbt.



#pipeline1 for testing purposes only
pipeline1 = [
    {
        '$sortByCount' : "$KEY"
    }
  
]



pipeline3 = [
    {
        '$match' : { 'KEY' : "ALL" }  
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
# ^ this prints a list of times and values, where the values indicate the number of bags in the whole system at that time.
# This includes the bags in ebs also. 

# But we want the number of bags in the system exlusing the ones in ebs. so,
# We need to subtract the value of 'value' when key=inebs at a particular time from 
#the value of 'value' when key=all at the same time 


