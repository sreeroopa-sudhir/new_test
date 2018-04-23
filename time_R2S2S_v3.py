
# coding: utf-8

# In[25]:


from datetime import date, datetime
import time
timeRaw1 = "27-MAR-18 11.30.11.000000000 PM"
timeRaw2 = "01-APR-18 09.20.07.000000000 AM"


# In[26]:


date_string1 = timeRaw1[:18] + timeRaw1[-2:]
date_string2 = timeRaw2[:18] + timeRaw2[-2:]
a = datetime.strptime(date_string1, "%d-%b-%y %I.%M.%S%p")
b = datetime.strptime(date_string2, "%d-%b-%y %I.%M.%S%p")
tts = (b-a).total_seconds()
print(tts)

