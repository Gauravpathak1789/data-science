#!/usr/bin/env python
# coding: utf-8

# Q1. Create a function which will take a list as an argument and return the product of all the numbers 
# after creating a flat list.
# 
# Use the below-given list as an argument for your function.
# 
# 
# list1 = [1,2,3,4, [44,55,66, True], False, (34,56,78,89,34), {1,2,3,3,2,1}, {1:34, "key2": [55, 67, 78, 89], 4: (45, 
# 22, 61, 34)}, [56, 'data science'], 'Machine Learning']

# In[7]:


def flatten(container):
    for i in container:
        if isinstance(i, (list,tuple,dict,set)):
            for j in flatten(i):
                yield j
        else:
            yield i


list1 = [1,2,3,4, [44,55,66, True], False, (34,56,78,89,34), {1,2,3,3,2,1}, {1:34, "key2": [55, 67, 78, 89], 4: (45, 22, 61, 34)}, [56, 'data science'], 'Machine Learning']

new=list(flatten(list1))

s=[]

for k in new:
    if type(k)==int:
        s.append(k)
        
from functools import reduce
print(reduce(lambda x,y:x*y,s))


        
      

            


# Q2. Write a python program for encrypting a message sent to you by your friend. The logic of encryption 
# should be such that, for a the output should be z. For b, the output should be y. For c, the output should 
# be x respectively. Also, the whitespace should be replaced with a dollar sign. Keep the punctuation 
# marks unchanged.
# 
# 
# Input Sentence: I want to become a Data Scientist.
# 
# 
# Encrypt the above input sentence using the program you just created.
# 
# 
# Note: Convert the given input sentence into lowercase before encrypting. The final output should be 
# lowercase

# In[3]:


def encrypt_message(message):
    message = message.lower()
    
  
    translation = str.maketrans('abcdefghijklmnopqrstuvwxyz ', 'zyxwvutsrqponmlkjihgfedcba$')
    

    encrypted_message = message.translate(translation)
  
    return encrypted_message


# In[4]:


input_sentence = 'I want to become a Data Scientist.'
encrypted_sentence = encrypt_message(input_sentence)
print(encrypted_sentence)


# In[ ]:




