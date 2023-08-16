'''

Aggregation Pipeline more examples...
'''
import pymongo
from pprint import pprint

''' Suppose we have this data structure, 

{
    "_id": 1,
    "name": "Alice",
    "favorite_books": [
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "rating": 4},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "rating": 5}
    ]
}
'''

# Connect to the MongoDB instance
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection1"]


# Grouping by Author and Counting Books:
pipeline = [
    {"$unwind": "$favorite_books"},
    {"$group": {"_id": "$favorite_books.author", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}}
]
result = collection.aggregate(pipeline)
print("GROUPING by author and counting Books ... ")
for item in result:
    print(item)

# sort by book ratings
pipeline = [
    {"$unwind": "$favorite_books"},
    {"$sort": {"favorite_books.rating": -1}},
    {"$project": {"_id": 0, "name": 1, "book_title": "$favorite_books.title", "rating": "$favorite_books.rating"}}
]
result = collection.aggregate(pipeline)
print("Sort by book RATINGS ")
for item in result:
    print(item)

# project selected fields
pipeline = [
    {"$project": {"_id": 0, "name": 1, "num_books": {"$size": "$favorite_books"}}}
]
result = collection.aggregate(pipeline)
print("Projecting selected fields ")
for item in result:
    print(item)


# filtering based on ratings and pagination
pipeline = [
    {"$unwind": "$favorite_books"},
    {"$match": {"favorite_books.rating": {"$gte": 4}}},
    {"$skip": 1},
    {"$limit": 2},
    {"$project": {"_id": 0, "name": 1, "book_title": "$favorite_books.title", "rating": "$favorite_books.rating"}}
]
result = collection.aggregate(pipeline)
print("Filtering based on ratings and pagination ")
for item in result:
    print(item)
