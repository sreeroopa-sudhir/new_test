
# coding: utf-8

# In[1]:


from pymongo import MongoClient
import pprint
from IPython.display import clear_output


# In[2]:



client = MongoClient("mongodb://localhost:27017/practice_work")


# In[3]:


# To add UID field to each document, 
# as a concatenated string of GID + bagTagID + FLIGHTNum + FLIGHTDateTime.

#using global id (bag id), bagtag id, flight number and flight date/time.

#currently code is with just global id and bagtag id.
#to change to just bag tag id, flight nuumber and flight date/time.


pipeline = [
   # {
    #    '$limit': 2
   # },
    {
        '$addFields': {
            'UID': {
                '$concat': [
                    { "$substr": [ "$BAG_ID", 0, -1 ] }, { "$substr": [ "$BAGTAGID", 0, -1 ] } 
                            ]
                    }
                        }
    },
    {
        '$project': {
            'EVENTTIME': 1,
            'BAGTAGID': 1,
            'BAG_ID': 1,
            'STATUS': 1,
            'BAGSTATUS': 1,
            'BAGPROFILE': 1,
            'HBSSTATUS': 1,
            'HBSCURLEVEL': 1,
            'HBSRESULT': 1,
            'CUSTSTATUS': 1,
            'BSM_ID': 1,
            'TTR_ID': 1,
            'TDP_IDFINAL': 1,
            'TDP_IDCURR': 1,
            'TDP_IDOPER': 1,
            'TNP_IDFIRSTPOS': 1,
            'TNP_IDLASTPOS': 1,
            'FIRSTPOSTIME': 1,
            'LASTPOSTIME': 1,
            'EXPIRATIONTIME': 1,
            'SECTODEST': 1,
            'REASON': 1,
            'STORINGREASON': 1,
            'ISNPBASEDHBSSTATUS': 1,
            'ISPROCESSED': 1,
            'UID': 1,
            
                  } #closing project method
    },
    {
        '$out': "practice_lbt2"
    }
]



pprint.pprint(list(client.practice_work.practice_lbt.aggregate(pipeline)))

