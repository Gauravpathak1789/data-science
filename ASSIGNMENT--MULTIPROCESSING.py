#!/usr/bin/env python
# coding: utf-8

# Q1. What is multiprocessing in python? Why is it useful? 

# In[1]:


#Multiprocessing is the execution of multiple concurrent processes in a computer system with multiple processors or CPU cores. 
#use--Improved performance: By distributing the workload across multiple processors or cores, multiprocessing can significantly improve the performance of a Python program.


# Q2. What are the differences between multiprocessing and multithreading

# In[2]:


#The main difference between multiprocessing and multithreading is that multiprocessing creates multiple independent processes, each with their own memory space, while multithreading creates multiple threads within a single process, all sharing the same memory space.


# 3. Write a python code to create a process using the multiprocessing module.

# In[3]:


import multiprocessing

def worker():
    """Simple worker function to print some text."""
    print("Worker started")
    print("Worker finished")

if __name__ == '__main__':
    # Create a new process
    process = multiprocessing.Process(target=worker)

    # Start the process
    process.start()

    # Wait for the process to finish
    process.join()

    print("Process finished")


# 4. What is a multiprocessing pool in python? Why is it used?

# In[4]:


#A multiprocessing pool in Python is a group of worker processes that can execute tasks concurrently. It allows you to parallelize the execution of a function across multiple input values by distributing the workload across the available CPU cores
#Multiprocessing pools are used to speed up the execution of CPU-bound tasks, such as intensive mathematical calculations or image processing, that can benefit from parallel execution. By distributing the workload across multiple processes, you can significantly reduce the time it takes to complete the task.


# Q5. How can we create a pool of worker processes in python using the multiprocessing module?

# In[ ]:


import multiprocessing

def my_function(x):
    return x * x

if __name__ == '__main__':
    with multiprocessing.Pool() as pool:
        results = pool.map(my_function, [1, 2, 3, 4, 5])
    print(results)


# Q6. Write a python program to create 4 processes, each process should print a different number using the 
# multiprocessing module in python

# In[ ]:


import multiprocessing

def print_number(num):
    print(f"Process {num}: {num}")

if __name__ == '__main__':
    processes = []
    for i in range(4):
        p = multiprocessing.Process(target=print_number, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()


# In[ ]:




