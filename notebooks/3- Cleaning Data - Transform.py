#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Name : Ahmed Tarek 
# Date : 8/8/2022 
# Company : Tagaddod 
# Tagaddod Data Engineer Position Task 


# # Cleaning Data (Transform) 
# 

# In[2]:


import os  #Using For Directory Path 
import json #For Loading JSON files
import pandas as pd #Pandas Library For Working with Dataframes
from datetime import datetime #for Converting date & Time to datetime type for using it in data analysis



# In[3]:


cwd = os.getcwd() #Getting the Current Path 
print(cwd)

BASE_DIR = os.path.dirname(cwd) # Going back for All Folders 
print(BASE_DIR)

DATA_DIR = os.path.join(BASE_DIR, 'data') #Going to the Data Folder
print(DATA_DIR)

CACHE_DIR = os.path.join(BASE_DIR, 'cache') #Cash Folder For Saving Merged data & Cleaned Merged Data 
os.makedirs(CACHE_DIR, exist_ok=True) #Creating the CACHE Folder 

working_file = os.path.join(CACHE_DIR, 'Company_Dataset.csv') #Merged Data path 
my_list=[] #List for Appending Differant Dict (That Comes From JSON) → to be Used in Merging Data

output_file = os.path.join(CACHE_DIR, 'Company_Dataset_cleaned.csv') #Cleaned data CSV File 



# In[4]:


#All of JSON files Names
files = os.listdir(DATA_DIR) 
print(files)


# In[5]:


#converting date time from string to date_time for using it in data Analysis
def clean_string_date():
    
            try:
                data[k]['snapshot_datetime'] = datetime.strptime(data[k]['snapshot_datetime'][2:] , '%y-%m-%d %H:%M:%S.%f')
            except KeyError:
                print("")
            except ValueError:
                try:
                    data[k]['snapshot_datetime'] = datetime.strptime(data[k]['snapshot_datetime'] , '%y-%m-%d %H:%M:%S.%f')
                except ValueError:
                    try:
                        data[k]['snapshot_datetime'] = datetime.strptime(data[k]['snapshot_datetime'][2:] , '%y-%m-%d %H:%M:%S')
                    except ValueError:
                        data[k]['snapshot_datetime'] = datetime.strptime(data[k]['snapshot_datetime'] , '%y-%m-%d %H:%M:%S')


# In[6]:


for f in files: #iterating throgh All file Names
    filename=f.replace(".json"," ") #Getting Files Names For Using it as a New Coulmn "Without JSON"
    
    #Getting the Full path
    f= os.path.join(DATA_DIR,f)
    print(f)
    #openinng All JSON Files 
    with open(f) as json_file:
        data = json.load(json_file)
        #Making a New Key:Value for a Dict {"file_name ": File name } to be added as a Coulmn 
        for k in data:
            data[k]['file_name']=filename
            clean_string_date() #Converting date str → date_time
            my_list.append(data[k])

#print(my_list)


# In[8]:


df=pd.DataFrame(my_list) #Converting the Combined list to Dataframe
#Saving cleaned_Combined data to CSV file

#Dropping any Row that didn't has device_id
df = df[df['device_id'].notna()]

#Saving Combined_Cleaned data to CSV
dataset = os.path.join(CACHE_DIR, 'Company_Dataset_cleaned.csv') 
df.to_csv(dataset, index=False)




# In[9]:


#Checking data types
df.dtypes


# In[ ]:




