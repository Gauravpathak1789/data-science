#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# Q1. List any five functions of the pandas library with execution.

# In[52]:


df1=pd.DataFrame({"key1":[1,2,3,4],"key2":[78,90,35,2],"key3":[88,80,4,1]})


# In[53]:


df2=pd.DataFrame({"key1":[0,3,2,5],"key4":[7,8,9,10],"key5":[77,1,2,3]})


# In[54]:


df1.merge(df2,how="right")


# In[55]:


df1.merge(df2,how='left')


# In[56]:


df1.merge(df2,how='cross')


# In[57]:


pd.concat([df1,df2],axis=1)


# In[58]:


p=pd.concat([df1,df2],axis=1)


# In[59]:


p


# In[19]:


pd.concat([df1,df2],join='inner')


# In[44]:


df1=pd.DataFrame({"key11":[1,2,3,4],"key22":[78,90,35,2],"key33":[88,80,4,1]},index=["a","b","c","d"],dtype='object')


# In[65]:


df2=pd.DataFrame({"key1":[1,2,3,4],"key4":[78,90,35,2],"key5":[88,80,4,1]},index=["a","b","g","h"],dtype='object')


# In[66]:


df1


# In[67]:


df2


# In[70]:


pd.Categorical(df2['key1'])


# Q2. Given a Pandas DataFrame df with columns 'A', 'B', and 'C', write a Python function to re-index the 
# DataFrame with a new index that starts from 1 and increments by 2 for each row

# In[2]:


df=pd.DataFrame({'A':["abhi","sattu","shivam"],"B":[23,45,67],"C":[True,False,None]})


# In[3]:


df


# In[54]:


t=len(df.index)


# In[79]:


l1=[]
for i in range(1,2*x,2):
    l1.append(i)
       


# In[80]:


df.reindex(l1)


# Q3. You have a Pandas DataFrame df with a column named 'Values'. Write a Python function that 
# iterates over the DataFrame and calculates the sum of the first three values in the 'Values' column. The 
# function should print the sum to the console.

# In[108]:


df=pd.DataFrame({"Values":[10,20,30,40,50]})


# In[109]:


df


# In[110]:


t=df[0:3]


# In[111]:


t


# In[112]:


t['Values'].sum()


# 4. Given a Pandas DataFrame df with a column 'Text', write a Python function to create a new column 
# 'Word_Count' that contains the number of words in each row of the 'Text' column.

# In[113]:


df=pd.DataFrame({"Text":["makes","me","annoying"]})


# In[114]:


df


# In[122]:


df['Word_Count']=df['Text'].apply(lambda x:len(x))


# In[123]:


df


# Q5. How are DataFrame.size() and DataFrame.shape() different?

# In[131]:


df.shape##it used to display the no of  rows and columns-


# In[132]:


df.size##it is used to dislay the no of data prsents in datframe-


# Q6. Which function of pandas do we use to read an excel file?

# In[133]:


#pd.read_excel


# Q7. You have a Pandas DataFrame df that contains a column named 'Email' that contains email 
# addresses in the format 'username@domain.com'. Write a Python function that creates a new column 
# 'Username' in df that contains only the username part of each email address.

# In[136]:


df=pd.DataFrame({"Email":["gaurav.pathak@lpu.in","abhi.shah@lpu.in","satyam.tiwari@lpu.in"]})


# In[137]:


df


# In[140]:


df['Username']=df['Email'].apply(lambda x:x.removesuffix("@lpu.in"))


# In[141]:


df


# Q8. You have a Pandas DataFrame df with columns 'A', 'B', and 'C'. Write a Python function that selects 
# all rows where the value in column 'A' is greater than 5 and the value in column 'B' is less than 10. The 
# function should return a new DataFrame that contains only the selected rows.

# In[144]:


df=pd.DataFrame({'A':[3,8,6,9,2],"B":[5,2,9,3,1],"C":[1,7,4,5,2]})


# In[145]:


df


# In[155]:


df_new=df[(df['A']>5) &(df['B']<10)]


# In[156]:


df_new


# Q9. Given a Pandas DataFrame df with a column 'Values', write a Python function to calculate the mean, 
# median, and standard deviation of the values in the 'Values' column.

# In[157]:


df=pd.DataFrame({"Values":[10,20,30,40,50,10,20,20]})


# In[158]:


df


# In[160]:


df.mean()


# In[161]:


df.median()


# In[162]:


df.mode()


# Q10. Given a Pandas DataFrame df with a column 'Sales' and a column 'Date', write a Python function to 
# create a new column 'MovingAverage' that contains the moving average of the sales for the past 7 days 
# for each row in the DataFrame. The moving average should be calculated using a window of size 7 and 
# should include the current day.

# In[2]:


dat=pd.date_range(start="14-04-2023",end="27-04-2023")


# In[7]:


d=[23,4,5,6,7,8,9,12,33,4,5,6,67,43]


# In[8]:


df=pd.DataFrame({"Sales":d,"Date":dat})


# In[9]:


df


# In[15]:


df.dtypes


# In[22]:


df['MovingAverage']=df.rolling(window=7).mean()


# In[23]:


df


# Q11. You have a Pandas DataFrame df with a column 'Date'. Write a Python function that creates a new 
# column 'Weekday' in the DataFrame. The 'Weekday' column should contain the weekday name (e.g. 
# Monday, Tuesday) corresponding to each date in the 'Date' column

# In[25]:


df=pd.DataFrame({"Date":["2023-01-01","2023-01-02","2023-01-03","2023-01-04","2023-01-05"]})


# In[27]:


df.dtypes


# In[28]:


df['updated_day']=pd.to_datetime(df['Date'])


# In[30]:


df


# In[38]:


df['Weekday']=pd.to_datetime(df['updated_day']).dt.strftime('%A')


# In[39]:


df


# Q12. Given a Pandas DataFrame df with a column 'Date' that contains timestamps, write a Python 
# function to select all rows where the date is between '2023-01-01' and '2023-01-31'

# In[40]:


df=pd.date_range(start="2023-01-01",end="2023-01-31")


# In[48]:


df1=pd.DataFrame(df)


# In[49]:


df1['Date']=df1[0]


# In[54]:


del (df1[0])


# In[55]:


df1


# Q13. To use the basic functions of pandas, what is the first and foremost necessary library that needs to 
# be imported?

# In[56]:


import pandas as pd


# In[ ]:




