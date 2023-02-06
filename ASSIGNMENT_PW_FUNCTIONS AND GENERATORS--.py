#!/usr/bin/env python
# coding: utf-8

# Q1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the 
# range of 1 to 25.

# In[4]:


#ans:-def is the keyword to create a function.
def odd_number(n):
    for i in range(1,n+1):
        if i%2!=0:
            print(i)
num=int(input())
odd_number(num)
        


# In[6]:


#Q2. Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs to 
#demonstrate their use.


# In[23]:


#ans:-we use *args in some function because it will provide that user can pass any no of argument to the function
#**kwargs provide that whenever user want to  create dictionary from function then by applying key argument user is eleigible to do it.
def test1(*args,a):
    return args,a
print(test1("monster","educator",[1,2,3],a=9))
####
def test2(**kwargs):
    return kwargs
print(test2(name="gaurav",course="datascience masters",roll=[23,24,67]))
    


# Q3.  What is an iterator in python? Name the method used to initialise the iterator object and the method 
# used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14, 16, 
# 18, 20].

# In[27]:


# ans:-iterator is an object which can be iterated upon,meaning that you can go through all values one by one.
#iter is the method to intialise the iterator object.
given_list=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
myit=iter(given_list)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


# Q4.  What is a generator function in python? Why yield keyword is used? Give an example of a generator 
# function.

# In[41]:


# ans:-generator is a function which is used to produce large sequence of values ,but it doesnot store all the values at once.
#yield keyword is used to create a generator function.
def even_no(x):
    for i in range(x):
        if i%2==0:
            yield i


# In[42]:


n=int(input())
for y in (even_no(n)):
    print(y)


# Q5. Create a generator function for prime numbers less than 1000. Use the next() method to print the 
# first 20 prime numbers.

# In[14]:


def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
        return True

            


# In[15]:


def prime_generator():
    n = 1
    while True:
        n += 1
        if is_prime(n):
            yield n


# In[17]:


generator = prime_generator()

for i in range(20):
    print(next(generator))


# In[ ]:




