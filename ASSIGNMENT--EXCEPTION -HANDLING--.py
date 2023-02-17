#!/usr/bin/env python
# coding: utf-8

# what is an Exception in python?write the difference between exception and syntax error.

# In[1]:


#ans:-Exceptions are runtime errors in Python that occur during program execution.
#ans:-The main difference is that exceptions are caused by both programming mistakes and unexpected events, while syntax errors are  the result of programming mistakes


# what happen when exception is not handled?explain wth an example.

# In[2]:


#When an exception is not handled, the program will terminate abruptly and display an error message to the user.
#and after this exception if any programme is there then it willnot going to execute
#example:--
def func(num):
    print(num/0)
    print("ok")
func(9)


# which python statements is used to handle exceptions?explain with examples.

# In[3]:


#the statements which is used to cach and handle the exceptions are:--try and exception in built function
#example:--
try:
    import ram
except ImportError as e:
    print(e)


# Explain with an example:
# a. try and else
# b. finally
# c. raise

# In[2]:


#(a)--ans:- try and else both used together in exception handling when try block will 
#run without haaving exception then else block will executed otherwise else block will not executed.
try:
    x=int(inputjenter the value"))
except ValueError as e:
    print(e)
else:
    print(x)


# In[3]:


#(b) the finally block will execute whether programme have exception or not.
try:
    import tag
except ModuleNotFoundError as e:
    print(e)
finally:
    print("this block will going to execute every time")


# In[4]:


#(c) this raise statement is used to raise an exception.
x = -1
if x < 0:
    raise ValueError("Invalid input. Please enter a positive number.")


# what are custom  exceptions in python? why do we need custom  exceptions? explain with examples.

# In[6]:


#ans:-Custom exceptions in Python are user-defined exceptions that extend the built-in Exceptionclass.
#These exceptions allow you to define your own specific exception types for your program that canbe raised in response to certain conditions.
#Custom exceptions are useful when you need to handle specific errors that are not covered by the built-in exceptions.
class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)

def some_function(some_arg):
    if some_arg < 0:
        raise MyException("argu must be non-negative")
try:
    some_function(-1)
except MyException as e:
    print(e)  


# create custom exception class?use this class to handle an exception.

# In[7]:


class NegativeNumberError(Exception):
    def __init__(self, message):
        super().__init__(message)

def square_root(n):
    if n < 0:
        raise NegativeNumberError("Cannot calculate the square root of a negative number")
    return n ** 0.5

try:
    result = square_root(-1)
except NegativeNumberError as e:
    print("Error:", e)


# In[ ]:




