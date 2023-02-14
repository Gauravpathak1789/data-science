#!/usr/bin/env python
# coding: utf-8

# Q1. You are writing code for a company. The requirement of the company is that you create a python 
# function that will check whether the password entered by the user is correct or not. The function should 
# take the password as input and return the string “Valid Password” if the entered password follows the 
# below-given password guidelines else it should return “Invalid Password”.
# 
# 
# Note: 1. The Password should contain at least two uppercase letters and at least two lowercase letters.
# 
# 2. The Password should contain at least a number and three special characters.
# 
# 3. The length of the password should be 10 characters long.

# In[70]:


n=input()
l1=[]
l2=[]
l3=[]
special_char=["&","*","%","$","#"]
for i in n:
    if i in (special_char):
        l3.append(i)
    else:
        for j in i:
            if "A"<=j<="Z":
                l1.append(j)
            else:
                if "a"<=j<="z":
                    l2.append(j)
upper2=len(l1)
lowr2=len(l2)
special=len(l3)



        

        
        


# In[72]:



if any(k.isdigit() for k in n)==True:
    if len(n)==10 and upper2>=2:
        if lowr2>=2 and special>=3:
            print("Valid Password")
else:
    print("Invalid Password")


# In[ ]:





# In[ ]:


# Q2. Solve the below-given questions using at least one of the following: 

# 1. Lambda functioJ
# 2. Filter functioJ
# 3. Zap functioJ
# 4. List Comprehension
# B Check if the string starts with a particular letter
# B Check if the string is numeric
# B Sort a list of tuples having fruit names and their quantity. [("mango",99),("orange",80), ("grapes", 1000)]
# B Find the squares of numbers from 1 to 10
# B Find the cube root of numbers from 1 to 10
# B Check if a given number is evenY
# B Filter odd numbers from the given list.

#  [1,2,3,4,5,6,7,8,9,10-
# B Sort a list of integers into positive and negative integers lists.

#  [1,2,3,4,5,6,-1,-2,-3,-4,-5,0]


# In[17]:


# B Check if the string starts with a particular letter
string_input=input()

l=[x[0] for x in string_input if x[0]=="s"]
for i in l:
    if i=="s":
        print("true")


# In[2]:


#B Check if the string is numeric
s=input()
print(s.isdigit())
        


# In[38]:


# B Sort a list of tuples having fruit names and their quantity. [("mango",99),("orange",80), ("grapes", 1000)]
list1= [("mango",99),("orange",80), ("grapes", 1000)]
list1.sort(key=lambda x:x[0])
list1


# In[40]:


# B Find the squares of numbers from 1 to 10.
r=range(1,11)
sq=[x**2 for x in r]
sq


# In[42]:


# B Find the cube root of numbers from 1 to 10
r=range(1,11)
cube_root=[x**(1/3) for x in r]
cube_root


# In[45]:


# B Check if a given number is even
num=int(input())
even=(lambda x:x%2==0)
even(num)


# In[47]:


# B Filter odd numbers from the given list.

list2= [1,2,3,4,5,6,7,8,9,10]
odd_no=list(filter(lambda i:i%2!=0,list2))
odd_no


# In[51]:


# B Sort a list of integers into positive and negative integers lists.

list3= [1,2,3,4,5,6,-1,-2,-3,-4,-5,0]
positive_list=sorted(list(filter(lambda k:k>=0,list3)))
negative_list=sorted(list(filter(lambda y:y<0,list3)))
print(positive_list)
print(negative_list)


# In[ ]:




