#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# Consider following code to answer further questions:
# 
# import pandas as pd
# 
# course_name = [‘Data Science’, ‘Machine Learning’, ‘Big Data’, ‘Data Engineer’]
# 
# duration =  [2,3,6,4]
# 
# df = pd.DataFrame(data = {‘course_name’ : course_name, ‘duration’ : duration})
#    
#    
#    Q1. Write a code to print the data present in the second row of the dataframe, df.

# In[ ]:


course_name = ['Data Science', 'Machine Learning', 'Big Data', 'Data Engineer']
duration =  [2,3,6,4]

df = pd.DataFrame(data = {'course_name' : course_name, 'duration' : duration})
   
   


# In[ ]:


df


# In[ ]:


df.iloc[[1]]


# Q2. What is the difference between the functions loc and iloc in pandas.DataFrame?

# In[ ]:


#The main difference between pandas loc[] vs iloc[] is loc gets DataFrame rows & columns by labels/names and iloc[] gets by integer Index/position


# Q3. Reindex the given dataframe using a variable, reindex = [3,0,1,2] and store it in the variable, new_df 
# then find the output for both new_df.loc[2] and new_df.iloc[2].

# In[ ]:


new_df=df.reindex( [3,0,1,2])


# In[ ]:


new_df.loc[2]


# In[ ]:


new_df.iloc[2]


# In[ ]:


new_df


# In[ ]:


import pandas as pd

import numpy as np

columns = ['column_1', 'column_2', 'column_3', 'column_4', 'column_5', 'column_6']

indices = [1,2,3,4,5,6]

#Creating a dataframe:

df1 = pd.DataFrame(np.random.rand(6,6), columns = columns, index = indices)


# In[ ]:


df1


# Q4. Write a code to find the following statistical measurements for the above dataframe df1:
# 
# (i) mean of each and every column present in the dataframe.
# 
# (ii) standard deviation of column, ‘column_2’

# In[ ]:


df1.mean(axis=1)#columnwise mean--


# In[ ]:


df1.mean(axis=0)#rowwise mean--


# In[ ]:


df1['column_2'].std()#standard deviation of column_2--


# Q5. Replace the data present in the second row of column, ‘column_2’ by a string variable then find the 
# mean of column, column_2

# In[ ]:


df1.loc[2,'column_2']='string_variable'


# In[ ]:


df1


# In[ ]:


df1.mean()


# Q6. What do you understand about the windows function in pandas and list the types of windows 
# functions?

# In[ ]:


#Windows function in Pandas can be broadly divided into three categories namely- Aggregate, Ranking, and Value. The group by aggregate function can be used to partition and group the entire data frame by some column. We can specify the column name in the parameter of the pandas.


# Q7. Write a code to print only the current month and year at the time of answering this question.
# 
# [Hint: Use pandas.datetime function]

# In[ ]:


current=pd.DataFrame({''})


# In[ ]:


c_d=pd.DataFrame(current)


# Q8. Write a Python program that takes in two dates as input (in the format YYYY-MM-DD) and 
# calculates the difference between them in days, hours, and minutes using Pandas time delta. The 
# program should prompt the user to enter the dates and display the result.

# In[ ]:


date1_str=input("enter the first date :")
date2_str=input("enter the second date :")
d1=pd.to_datetime(date1_str)
d2=pd.to_datetime(date2_str)
delta=d1-d2
days=delta.days
hours=delta.seconds//3600
minutes=(delta.seconds%3600)//60
print(f"The difference between {date1_str} and {date2_str} is {days} days, {hours} hours, and {minutes} minutes.")


# Q9. Write a Python program that reads a CSV file containing categorical data and converts a specified 
# column to a categorical data type. The program should prompt the user to enter the file path, column 
# name, and category order, and then display the sorted data.

# In[ ]:


import pandas as pd

# Prompt the user to enter the file path
file_path = input("Enter the file path: ")

# Prompt the user to enter the column name
column_name = input("Enter the column name: ")

# Prompt the user to enter the category order
category_order = input("Enter the category order (comma-separated): ").split(",")

# Read the CSV file into a DataFrame
data = pd.read_csv(file_path)

# Convert the specified column to a categorical data type
data[column_name] = pd.Categorical(data[column_name], categories=category_order, ordered=True)

# Sort the data by the specified column
data = data.sort_values(by=column_name)

# Display the sorted data
print(data)


# Q10. Write a Python program that reads a CSV file containing sales data for different products and 
# visualizes the data using a stacked bar chart to show the sales of each product category over time. The 
# program should prompt the user to enter the file path and display the chart.

# In[ ]:


file_path=input("enter the file path :")

df=pd.read_csv(file_path)
grouped_data = df.groupby(['Product Category', 'Year']).sum()

pivot_data = grouped_data.pivot_table(index='Year', columns='Product Category', values='Sales', aggfunc='sum')
pivot_data.plot(kind='bar', stacked=True)


# Q11. You are given a CSV file containing student data that includes the student ID and their test score. Write 
# a Python program that reads the CSV file, calculates the mean, median, and mode of the test scores, and 
# displays the results in a table.

# In[3]:


df=pd.read_csv("C:\\Users\\Gaurav Pathak\\OneDrive\\Documents\\s.csv")


# In[4]:


df.head()


# In[12]:


mean=df['test_score'].mean()


# In[14]:


median=df['test_score'].median()


# In[22]:


from scipy import stats
mode=stats.mode(df['test_score'])


# In[24]:


result=pd.DataFrame({"mean":mean,"median":median,"mode":mode})


# In[25]:


result


# In[ ]:




