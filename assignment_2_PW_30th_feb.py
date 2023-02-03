#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#write a programme to accept the percentage from user and display the grades according to it.
percentage=int(input("enter the percentage gain:-"))
if percentage>90:
    print("grade:- A")
elif percentage>80 and percentage<=90:
    print("grade:- B")
elif percentage>=60 and percentage<=80:
    print("grade:- C")
else:
    print("grade:- D")


# In[ ]:


#write a programme to accept the cost price of a bike and display the road text to be paid according to the folowing criteria:
cost_price_bike=int(input("enter the price of bike:-"))
if cost_price_bike>100000:
    print("Road tax to be paid :15%")
elif cost_price_bike>50000 and cost_price_bike<=100000:
    print("Road tax to be paid :10%")
else:
    print("Road tax to be paid :5%")


# In[ ]:


#accept any city from  the user and display the monuments of that city.
city=input("enter the city name :")
if city=="Delhi":
    print("Monument of delhi is :Red Fort")
elif city=="Agra":
    print("Monument of delhi is :Taj Mahal")
elif city=="Jaipur":
    print("Monument of delhi is :Jal Mahal")
else:
    print("wrong input")


# In[ ]:


#check how may  times a number can be divided by 3 before it is the less than or equal to 10.
i=1
no_dividedby_3=[]
while i<=11:
    if i%3==0:
        print(i)
        no_dividedby_3.append(i)
    i+=1
print("no of  digitsget divided by three :",len(no_dividedby_3))
        


# #why and when to use while loop in python give detail description with examples.
# ans:-we use while loop to run a block of code until we not reach to the required condition.
#     we use while loop when we have to repeat or want to iterate the items upto certain condition

# In[2]:


#use nested looop to print 3 different pattern
n=7
i = 1
while i <= n :
    j = 1
    while j <= i:
        print("*", end = " ")
        j += 1
    print()
    i += 1


# In[3]:


#reverse a while loop to display numbers from 10 to 1.
i=10
while i>0:
    print(i)
    i-=1


# In[ ]:




