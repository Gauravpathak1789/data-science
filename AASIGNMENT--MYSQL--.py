#!/usr/bin/env python
# coding: utf-8

# Q1. What is a database? Differentiate between SQL and NoSQL databases.

# In[1]:


#ans:--a database is the collection of structured and organised interrelated information or meaningful data.
#SQL---it is structured query language.it is domain specific and help in manulation of data related  to relation database management system.
#NoSQL--it is not only structred query language.it is the database which is uesd to store unstructered data in the form of collections


# Q2. What is DDL? Explain why CREATE, DROP, ALTER, and TRUNCATE are used with an example.

# In[2]:


#ans:-- DDL stands for data definition language.it consists of the commands which is used for creating database ,table and dropinng tables and databases.

#CREATE--it ist the command used for craeting database or table ,,ex--create database demostration,create table my work.

#DROP--it is also related to ddl it help us to delete com pletely above created database or table after that there is no existence of database.

#ALTER--it is also related to ddl commmands,it help us to udate or delete certain column of the table or database,,,ex--alter TABLE table_nameADD column_name datatype;

#TRUNCATE--it also related to ddl commands,itTRUNCATE is a SQL command that removes all the rows from a table without using any condition.


# Q3. What is DML? Explain INSERT, UPDATE, and DELETE with an example.

# In[3]:


#DML--dmlis the data manipulation language which consists of insert,update and delete it is used for aminly data related operation in tables.

#INSERT--- insert is the dml command  which is used to to insert values into tables. ex--insert into table_name values ()

#UPDATE---UPDATE is the dml command to update the data related in tuples.ex--- udate table_name set column1=column_new where something.

#DELETE--delete is the dml command to delete the data in tables.ex---delete from table_name where something.


# Q4. What is DQL? Explain SELECT with an example.

# In[6]:


#DQL stands for Data Query Language. It is a type of computer language used to retrieve, manipulate, and manage data in a relational database. The most commonly used DQL is SQL (Structured Query Language).

#SELECT is a command in SQL that is used to retrieve data from one or more tables. The basic syntaxis like that;--



#SELECT column1, column2, FROM table_nameWHERE condition;




# Q5. Explain Primary Key and Foreign Key.

# In[7]:


#In a relational database, a primary key is a column or a set of columns that uniquely identify each row in a table. A primary key is used to enforce the integrity and consistency of the data in the table, as well as to ensure that each row can be uniquely identified and accessed. 
#The primary key constraint is used to define the primary key of a table.
#
#A foreign key, on the other hand, is a column or a set of columns that refers to the primary key of another table.
#A foreign key is used to establish a relationship between two tables, where the values in the foreign key column of one table must match the values in the primary key column of the other table. This ensures that the data in both tables are consistent and that they are connected in a meaningful way.
#
#


# Q6. Write a python code to connect MySQL to python. Explain the cursor() and execute() method.

# In[8]:


import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  password="password",
  database="database_name"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM employees")


result = mycursor.fetchall()

for row in result:
  print(row)
#we create a cursor object using the cursor() method of the connection object. A cursor is an object that allows us to execute SQL queries and fetch results.
# execute() method is used to execute an SQL query on the database. It takes an SQL query as a parameter and returns the number of rows affected by the query. If the query returns data, we can fetch it using the fetchall(), fetchone(), or fetchmany() methods of the cursor object. The execute() method can also take parameters, which allows us to use dynamic values in our SQL queries.


# Q7. Give the order of execution of SQL clauses in an SQL query.

# In[9]:


FROM clause: This clause specifies the table or tables from which data is to be selected.

JOIN clause: If the query involves a join between two or more tables, the JOIN clause is executed next to combine the data from the specified tables.

WHERE clause: This clause specifies the conditions that must be met for a row to be included in the result set.

GROUP BY clause: This clause is used to group the data by one or more columns and perform aggregate functions on each group.

HAVING clause: This clause is used to filter the groups created by the GROUP BY clause based on specified conditions.


# In[ ]:




