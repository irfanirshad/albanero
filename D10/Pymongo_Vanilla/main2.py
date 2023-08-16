from pymongo import MongoClient
import os
import pandas as pd
import sys
import io
import numpy as np
import json
from pymongo import MongoClient
    
#     print("All modules loaded")
# except ImportError as e:
#     print(f"Import Errors ::  {e}" )

    

client = MongoClient("localhost", 27017)
client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000")

# Getting all DB names
print(client.list_database_names())



# # Creating a new DB and a new collection(Table) on the go ...
# client['LangDB']['language'].insert_one({
#     "_id" : 1,
#     "name": "Irfan Irshad",
#     "age": 25,
#     "language": ["Python", "C++", "Java"]
# })

# data = [{
#     "_id": "2",
#     "name": "Irfan Irshad",
#     "age": 25,
#     "language": ["x86", "C", "Embedded Core ESP"]
# },
# {
#     "_id": "3",
#     "name": "Irfan Irshad",
#     "age": 28,
#     "language": ["LISP", "Ocaml", "Bash"]
# }]


# # Insert many data 
# client['LangDB']['language'].insert_many(data)


# Update a record
new = {
    "name": "Hacked",
    "age": 19,
    "language":["Python3", "Clojure"]
}


client['LangDB']['language'].find_one_and_update(
    {"_id": "3"},
    {"$set": new}
)

