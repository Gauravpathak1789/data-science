#!/usr/bin/env python
# coding: utf-8

# Q1. Explain Class and Object with respect to Object-Oriented Programming. Give a suitable example.

# In[8]:


#ans:-Class is blueprint or we can say that it is the layout of object or real world entity.
#ans:- Object is the real world entity .
#ans:-Examples of Class are like the architcture model of biuldings in a particular university 
#or it can be car ,student etc,"""
#ans:- Examples of Object are the biuldings inside that particular university ,in car class 
#it is particular car that have different color ,brand model,etc."""


# Q2. Name the four pillars of OOPs.

# In[9]:


#ans:-the four pillars of oops are:-*inheritance,*polymorphism,*abstractin,*encapsulation.


# Q3. Explain why the __init__() function is used. Give a suitable example.

# In[15]:


#ans:-init() function is used in class because it work as a constructor which takes the value from
#function arguments and then it pass to class variable The task of constructors is to 
# initialize(assign values) to the data members of the class when an object of the class is created
class car:
    def __init__(self,model,color,price):
        self.model=model
        self.color=color
        self.price=price
    def car_details(self):
        return self.model,self.color,self.price
Tata=car("harrier","white",1500000)
Mahindra=car("thar","black",1600000)


# In[16]:


Tata.model


# Q4. Why self is used in OOPs?

# #ans:-self is used to The self parameter is a reference to the current instance of the class, 
# #and  used to access variables that belongs to the class.
# 

# Q5. What is inheritance? Give an example for each type of inheritance

# In[1]:


#ans:-inheritance is the property to inherit the atrributes from its higher or parent class by child or lower class.
#1.single level inheritence 2.multilevel inheritence 3. multiple inheritance


# In[ ]:




