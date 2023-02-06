#!/usr/bin/env python
# coding: utf-8

# #WHAT ARE THE CHARACTERISTICS OF TUPLE?IS IT  MUTABLE?

# ans:-the characteristics of tuples are:-
#         * it supports indexing
#         *it can stored different data types
#         *it can be iterated using for loop
#         
# No,it is not mutable.

#  Q2. What are the two tuple methods in python? Give an example of each method. Give a reason why 
# tuples have only two in-built methods as compared to Lists

# In[8]:


"""ans:-two tuple method in python is:-
        *count
        *index"""
#examples of each two method:-
t1=("hello","world","gaurav",23,90,"hello","hello")
print(t1.count("hello"))
print(t1.index(23))
#tuples have only two built in method because its structure is different from list and it is different data type.


# Q3.  Which collection datatypes in python do not allow duplicate items? Write a code using a set to remove 
# duplicates from the given list

# In[10]:


#ans:-set is the one of the collection in datatypes in python which do not allow duplicate.
given_list = [1, 1, 1, 2, 1, 3, 1, 4, 2, 1, 2, 2, 2, 3, 2, 4, 3, 1, 3, 2, 3, 3, 3, 4, 4, 1, 4, 2, 4, 3, 4, 4]
set1=set(given_list)
print(list(set1))


# Q4. Explain the difference between the union() and update() methods for a set. Give an example of 
# each method.

# In[13]:


#union method in set used to join all the elements from set1 and set2 into another unique set.
#update method in set used to update the current set, by adding item from other set.
set1={24,44,'michel',90}
set2={77,98,44,'michel'}
set1.update(set2)
print(set1)
set1.union(set2)


# Q5. What is a dictionary? Give an example. Also, state whether a dictionary is ordered or unordered.

# In[14]:


#dictionary is one of the datastructure of python which allows to stored data in key value pair using :operator in between
dict1={"name":"gauarv","registration_id":12578897,"12":"work"}
print(dict1)
#dictionary is oredered in manner.


# 6. Can we create a nested dictionary? If so, please give an example by creating a simple one-level 
# nested dictionary.

# In[16]:


#ans:-yes,we can create nested dictionary.
nested_dict={"name":{"shubham":12,"gaurav":19,"satyam":7}}
print(nested_dict)


# Q7. Using setdefault() method, create key named topics in the given dictionary and also add the value of 
# the key as this list ['Python', 'Machine Learning’, 'Deep Learning']

# In[18]:


dict1 = {'language' : 'Python', 'course': 'Data Science Masters'}
dict1.setdefault("topics",['Python', 'Machine Learning', 'Deep Learning'])


# Q8. What are the three view objects in dictionaries? Use the three in-built methods in python to display 
# these three view objects for the given dictionary.
# 
# 
# dict1 = {'Sport': 'Cricket' , 'Teams': ['India', 'Australia', 'England', 'South Africa', 'Sri Lanka', 'New Zealand']}

# In[28]:


#ans:-the three views of the objects in dictionaries are keys,values and items.
dict1= {'Sport': 'Cricket' , 'Teams': ['India', 'Australia', 'England', 'South Africa', 'Sri Lanka', 'New Zealand']}
print("keys of dictionary  --\n",dict1.keys())
print("values of dictionary --\n",dict1.values())
print("items of dictionary --\n",dict1.items())


# In[ ]:




