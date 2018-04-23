
# coding: utf-8

# In[8]:


from pymongo import MongoClient
import pprint
from IPython.display import clear_output


# In[9]:


client = MongoClient("mongodb://localhost:27017/practice_work")


# In[12]:


# KPI #4 No. of Bags that are in the EBS

#for testing purposes only
pipeline1 = [
    {
        '$sortByCount' : "$BAGSTATUS"
    }
  
]

#first half
#No. of Bags that are EARLY in System
pipeline2 = [
    {
        '$match' : { 'BAGSTATUS' : "EARLY" }  
    },
    {
        '$group': {  '_id': '$BAGTAGID'}
    },
    {
        '$group': {
                  '_id': 1,
                  'count': {  '$sum': 1 }
                }
    }
]

#print output of specified pipeline applied to practice_lbt
pprint.pprint(list(client.practice_work.practice_lbt.aggregate(pipeline1)))
pprint.pprint(list(client.practice_work.practice_lbt.aggregate(pipeline2)))

