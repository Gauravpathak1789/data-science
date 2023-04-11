#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Consider the below code to answer further questions:


import numpy as np


list_ = [ "1" , "2" , "3" , "4" , "5" ]

array_list = np.array(object = list_)


# Q1. Is there any difference in the data type of variables list_ and array_list? If there is then write a code 
# to print the data types of both the variables.

# In[9]:


#yes there is the difference in the datatype of th variable list and array_list because variable list have list datatype
#and array_list has np.array datatype.
print(type(list))#code for finding datatype of list
print(array_list.dtype)#code for finding array_list


# Q2. Write a code to print the data type of each and every element of both the variables list_ and 
# arra_list.

# In[10]:


for i in list_:
    print(i,"=",type(i))
for j in array_list:
    print(j,"=",type(j))
    


# In[11]:


#Q3. Considering the following changes in the variable, array_list:

array_list = np.array(object = list_, dtype = int)

#Will there be any difference in the data type of the elements present in both the variables, list_ #and 
#arra_list? If so then print the data types of each and every element present in both the variables, #list_ 
#and arra_list.


# In[14]:


#yes there is the diference between the datatypes of elements present in both the variable and  list_array
for k in list_:
    print(k,"=",type(k))
for x in array_list:
    print(x,"=",type(x))
    


# In[15]:


#Consider the below code to answer further questions

num_list = [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] ]

num_array = np.array(object = num_list)


# Q4. Write a code to find the following characteristics of variable, num_array:
# 
# (i)	 shape
# 
# (ii) size

# In[26]:


print(num_array.shape)#shape of num_array
print(num_array.size)#size of num_array

sum_of_n=0
for i in num_list:
    for j in i:
        sum_of_n+=j
print("size of num_list=",sum_of_n)


# Q5. Write a code to create numpy array of 3*3 matrix containing zeros only, using a numpy array 
# creation function

# In[28]:


zero_array=np.zeros((3,3))
print(zero_array)


# Q6. Create an identity matrix of shape (5,5) using numpy functions

# In[34]:


identity_matrix=np.eye((5))
print(identity_matrix)


# In[ ]:




