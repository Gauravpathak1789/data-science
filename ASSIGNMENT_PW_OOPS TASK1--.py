#!/usr/bin/env python
# coding: utf-8

# Q1, Create a vehicle class with an init method having instance variables as name_of_vehicle, max_speed 
# and average_of_vehicle. 

# In[ ]:


class vehicle:
    def __init__(self,name_of_vehicle,max_speed,average_of_vehicle):
        self.name_of_vehicle1=name_of_vehicle
        self.max_speed1=max_speed
        self.average_of_vehicle1=average_of_vehicle


# Q2.  Create a child class car from the vehicle class created in Que 1, which will inherit the vehicle class. 
# Create a method named seating_capacity which takes capacity as an argument and returns the name of 
# the vehicle and its seating capacity

# In[ ]:


class car(vehicle):
    def seating_capacity(self,capacity):
        return self.name_of_vehicle1, capacity


# Q3. What is multiple inheritance? Write a python code to demonstrate multiple inheritance

# In[ ]:


#ans:-multiple inheritance is in which one child class inherit two or mare  than two parent class at the same time.
class parent1:
    def fuction_parent1(self):
        print("this is parent class1")


# In[ ]:


class parent2:
    def function_parent2(self):
        print("this is parent calss2")


# In[ ]:


class child(parent1,parent2):
    def func_child(self):
        print("this is child class")


# In[ ]:


c=child()


# In[ ]:


c.fuction_parent1()


# In[ ]:


c.function_parent2()


# Q4. What are getter and setter in python? Create a class and create a getter and a setter method in this
# class.

# In[2]:


#ans:-getter is the function made by user to give the acces to the end users to get only that particular value.
#ans:-setter is the function which is also made by user to  give the acces of data  to do some udatation or setting .
class bike:
    def __init__(self,name,avg_speed):
        self.__name=name
        self.__avg_speed=avg_speed
    @property
    def bike_avg_speed(self):
        return self.__avg_speed
    
    @bike_avg_speed.setter
    def set_avg_speed(self,speed):
        if speed<50:
            pass
        else:
            self.__avg_speed=speed
   
        


# Q5.What is method overriding in python? Write a python code to demonstrate method overriding

# In[3]:


#ans:-Two or more methods have the same name but different numbers of parameters or different types of parameters or bothand both can be accesible.

class Lpu:
    def __init__(self,name,email):
        self.name=name
        self.email=email
    @classmethod
    def details(cls,name1,email1):
        return cls(name1,email1)
l1=Lpu.details("sattu","sattu@gmail")
        
        


# In[ ]:




