#!/usr/bin/env python
# coding: utf-8

# Q1. What is MongoDB? Explain non-relational databases in short. In which scenarios it is preferred to use 
# MongoDB over SQL databases?

# In[1]:


#MongoDB is a cross-platform, document-oriented NoSQL database program that uses JSON-like documents with optional schemas. It is an open-source database management system #that uses a document-oriented database model, which allows for flexible and scalable data storage.
#Non-relational databases, also known as NoSQL databases, are databases that store and retrieve data in ways that are different from traditional relational databases
#Overall, MongoDB is a good choice for applications that require flexibility, scalability, and performance, especially in scenarios where the data is unstructured or has a changing schema. However, it is important to note that SQL databases are still the best choice for applications that require strong consistency and transaction support, such as financial applications or other mission-critical systems.


# Q2. State and Explain the features of MongoDB.

# In[2]:


#MongoDB is a popular NoSQL document-oriented database that provides many features that make it a popular choice for modern applications.
#Document-oriented data model: MongoDB stores data as JSON-like documents, which can include fields with a variety of data types, such as arrays, nested objects, and more. This allows for greater flexibility and scalability than traditional relational databases.

#Dynamic schema: Unlike traditional relational databases, MongoDB does not require a fixed schema, which means that fields can be added or removed from documents as needed, without requiring a schema migration.

#High performance: MongoDB is designed to handle high write loads and high throughput, making it a good choice for applications that require fast data processing.


# Q3. Write a code to connect MongoDB to Python. Also, create a database and a collection in MongoDB.

# In[3]:


import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["mydatabase"]

col = db["customers"]


# Q4. Using the database and the collection created in question number 3, write a code to insert one record, 
# and insert many records. Use the find() and find_one() methods to print the inserted record.

# In[ ]:


import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["mydatabase"]

col = db["customers"]

record = { "name": "John", "address": "Highway 37" }
inserted_record = col.insert_one(record)
print("Inserted record ID:", inserted_record.inserted_id)
records = [
  { "name": "Amy", "address": "Apple st 652" },
  { "name": "Hannah", "address": "Mountain 21" },
  { "name": "Michael", "address": "Valley 345" },
  { "name": "Sandy", "address": "Ocean blvd 2" },
]
inserted_records = col.insert_many(records)



record = col.find_one({ "name": "John" })
print("Found one record:", record)


records = col.find()
print("Found all records:")
for record in records:
  print(record)


# Q5. Explain how you can use the find() method to query the MongoDB database. Write a simple code to 
# demonstrate this.

# In[5]:


#The find() method is used to query the MongoDB database and retrieve documents that match a certain set of criteria. The find() method returns a Cursor object, which can be used to iterate over the documents that match the criteria.
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create a database
db = client["mydatabase"]

# Create a collection
col = db["customers"]

# Query the collection using find()
query = { "address": "Park Lane 38" }
results = col.find(query)

# Print the matching documents
print("Matching documents:")
for result in results:
  print(result)


# Q6. Explain the sort() method. Give an example to demonstrate sorting in MongoDB

# In[6]:


#The sort() method in MongoDB is used to sort the documents in a collection according to one or more fields. The sort() method takes one or more fields as arguments and returns a sorted Cursor object.


# Q7. Explain why delete_one(), delete_many(), and drop() is used

# In[7]:


#In MongoDB, delete_one() and delete_many() methods are used to remove one or multiple documents that match a certain set of criteria from a collection. On the other hand, drop() method is used to remove an entire collection from a database.


# In[ ]:




