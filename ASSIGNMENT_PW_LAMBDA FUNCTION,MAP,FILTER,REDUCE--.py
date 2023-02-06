#!/usr/bin/env python
# coding: utf-8

# 1. Create a python program to sort the given list of tuples based on integer value using a 
# lambda function. 
# 
# 
# [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]

# In[14]:


d=[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
sorted_list=list((lambda x:sorted(x[1]),d))
print(sorted_list)


# Q2. Write a Python Program to find the squares of all the numbers in the given list of integers using 
# lambda and map functions.
# 
# 
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# In[15]:


list1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sq_list=list(map(lambda x:x**2,list1))
sq_list


# Q3. Write a python program to convert the given list of integers into a tuple of strings. Use map and 
# lambda functions
# 
# 
# Given String: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 
# Expected output: ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')

# In[17]:


Given_String=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(tuple(map(lambda x:str(x),Given_String)))


# Q4.  Write a python program using reduce function to compute the product of a list containing numbers 
# from 1 to 25.

# In[19]:


from functools import reduce
list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
print(reduce(lambda x,y:x+y,list1))


# 5. Write a python program to filter the numbers in a given list that are divisible by 2 and 3 using the 
# filter function.
# 
# 
# [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]

# In[22]:


list2=[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
filter_list=list(filter(lambda x:x%2==0 and x%3==0,list2))
filter_list


# Q6. Write a python program to find palindromes in the given list of strings using lambda and filter 
# function.
# 
# 
# ['python', 'php', 'aba', 'radar', 'level']

# In[23]:


given_list=['python', 'php', 'aba', 'radar', 'level']
palindrome_list=list(filter(lambda x:x[::-1]==x,given_list))
print(palindrome_list)


# In[ ]:




