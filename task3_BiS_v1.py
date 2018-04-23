
# coding: utf-8

# In[50]:


from pymongo import MongoClient
import pprint
from IPython.display import clear_output


# In[51]:


client = MongoClient("mongodb://localhost:27017/dbOps_18_04_17")


# In[53]:


# KPI #3 Bags in System

#includes duplicates.
#Grouping by status, counts the number of documents. This can include duplicate BAG_IDs.
pipeline1 = [
    {
        '$sortByCount' : "$STATUS"
    }
  
]

#Use this one!
#For specified status, counts the number of documents with unique BAG_ID, i.e. counts the number of bags ()
pipeline2 = [
    {
        '$match' : { 'STATUS' : "TRA" }  
    },
    {
        '$group': {
                  '_id': '$BAGTAGID',
                  'count': {  '$sum': 1 }
                }
    }
    
]

#print output of specified pipeline applied to practice_lbt
pprint.pprint(len(list(client.dbOps_18_04_17.lbt.aggregate(pipeline2))))

