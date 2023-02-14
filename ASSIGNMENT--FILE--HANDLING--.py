#!/usr/bin/env python
# coding: utf-8

# Q1. Which function is used to open a file? What are the different modes of opening a file? Explain each mode 
# of file opening.

# In[5]:


#ans:-open() is the function used to open file.
#ans:-* open("file.name","r") here r shows that file opens in read mode
#ans:-* open("file.name","w") here w shows that file opens in writting mode
#ans:-* open("file.name","a") here a shows that file opens in append or update to udating without clearing previous contents.


# Q2. Why close() function is used? Why is it important to close a file?

# In[6]:


#ans:-close() function i s used to close the file after writing or reading etc.
# it is important to close the fi;e after oppening in different mode so that the data get stored without it data will not permanently get stored


# 3. Write a python program to create a text file. Write ‘I want to become a Data Scientist’ in that file. Then 
# close the file. Open this file and read the content of the file.  

# In[7]:


f=open("text2.file","w")


# In[8]:


f.write("I want to become a Data Scientist")


# In[9]:


f.close()


# In[10]:


f=open("text2.file","r")


# In[11]:


f.read()


# Q4. Explain the following with python code: read(), readline() and readlines().

# In[12]:


#ans:- read() function return all the content of file.
#ans:-readline()  method return only single line from stored data.
#ans:-readlines() function return set of lines from stored file data


# Q5. Explain why with statement is used with open(). What is the advantage of using with statement and 
# open() together?

# In[13]:


#ans:-with statement with open is used to open the file and automatically italso close the file.
#we should use with statement and open together because with statement close the file for us as well we have to write less code


# Q6. Explain the write() and writelines() functions. Give a suitable example

# In[14]:


#ans:-The difference between Write() and WriteLine() method is based on new line character. Write() method displays the output but do not provide a new line character. WriteLine() method displays the output and also provides a new line character it the end of the string, This would set a new line for the next output.


# In[ ]:




