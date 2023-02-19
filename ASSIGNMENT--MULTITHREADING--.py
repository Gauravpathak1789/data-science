#!/usr/bin/env python
# coding: utf-8

# what is multithreading in python? why is it used? Name the module used to handle threads in python

# In[1]:


#Multithreading is a way of executing multiple threads or parts of a program concurrently, in parallel, on a CPU. In Python, multithreading is the ability of a program to run multiple threads or parts of a program concurrently, in parallel, on a CPU.
# Multithreading in Python is used to improve the performance of a program by utilizing the available CPU resources effectively. 
#The threading module provides the Thread class, which is used to create a new thread. 


# why threading module used? write the use of the following functions
# *activeCount()
# *currentThread()
# *enumerate()

# In[2]:


#The threading module in Python is used for creating and managing threads in a program. It provides a simple and consistent API for working with threads, and it supports both low-level and high-level thread management operations.
#activeCount(): This function returns the number of thread objects that are active. It is used to get a count of the currently active threads in a program.
#currentThread(): This function returns a reference to the current thread object. It is used to get a reference to the thread object that is currently running the function.
#enumerate(): This function returns a list of all thread objects that are active. It is used to get a list of all the currently active threads in a program.


# 3. Explain the following functions
# *run()
# *start()
# *join()
# *isAlive()

# In[3]:


#run(): This function is used to define the code that should be executed by the thread. It is typically overridden in a custom thread class to provide the thread's behavior.
#start(): This function is used to start a new thread. When this function is called, a new thread is created and the code defined in the run() method of the thread is executed.
#join(): This function is used to wait for a thread to complete. When this function is called, the program waits for the specified thread to finish executing before continuing.
#isAlive(): This function is used to check if a thread is still running. When this function is called, it returns a boolean value indicating whether the specified thread is still executing.


# 4.  write a python program to create two threads. Thread one must print the list of squares and thread 
# two must print the list of cubes

# In[4]:


import threading

# Define a function to print the list of squares
def print_squares():
    for i in range(1, 11):
        print(f"Square of {i} is {i**2}")

# Define a function to print the list of cubes
def print_cubes():
    for i in range(1, 11):
        print(f"Cube of {i} is {i**3}")

# Create two threads, one to print the squares and the other to print the cubes
t1 = threading.Thread(target=print_squares)
t2 = threading.Thread(target=print_cubes)

# Start the threads
t1.start()
t2.start()

# Wait for the threads to complete
t1.join()
t2.join()

# Print a message to indicate that the program has completed
print("Program completed.")


# 5. State advantages and disadvantages of multithreading

# In[5]:


#Advantages of multithreading:
#Improved program performance: Multithreading can improve the performance of a program by allowing it to make use of multiple CPU cores and execute tasks in parallel.
#Increased responsiveness: Multithreading can make a program more responsive by allowing it to execute multiple tasks simultaneously. This can be especially useful for programs that involve user interaction, such as GUI applications or web servers.
#Disadvantages of multithreading:
#Increased complexity: Multithreading can increase the complexity of a program, making it more difficult to design, implement, and debug.
#Synchronization issues: Multithreading can introduce synchronization issues, such as race conditions, deadlocks, and priority inversions, that can be difficult to detect and resolve.


# 6. Explain deadlocks and race conditions.

# In[6]:


#-Deadlock occurs when two or more threads are waiting for each other to release resources that they have acquired, resulting in a situation where none of the threads can make progress
 #Race conditions occur when the behavior of a program depends on the order in which threads execute, and that order is not guaranteed or predictable.


# In[ ]:




