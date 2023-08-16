'''Working with array fields 

url: https://www.codementor.io/@prasadsaya/working-with-arrays-in-mongodb-16s303gkd3

Working with arrays in MongoDB documents using pymongo in vanilla Python
involves using array-specific operators like $push, $pull, $addToSet, etc. 

$push, $pull, $addToSet, $set, and $unset operators are used to 
modify the array field in the documents.

'''
'''




# say we have this array 
Concept of '''
{
    "_id": 1,
    "name": "John",
    "interests": ["programming", "gaming"]
}


import pymongo
from pprint import pprint

# Connect to the MongoDB instance
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

# Adding an element to an array using $push
collection.update_one({"name": "John"}, {"$push": {"interests": "painting"}})

# Removing an element from an array using $pull
collection.update_one({"name": "John"}, {"$pull": {"interests": "gaming"}})

# Adding unique elements to an array using $addToSet
collection.update_one({"name": "John"}, {"$addToSet": {"interests": "reading"}})

# Updating a specific element in an array
collection.update_one(
    {"name": "John", "interests": "programming"},
    {"$set": {"interests.$": "coding"}}
)

# Removing all elements from an array using $unset
collection.update_one({"name": "John"}, {"$unset": {"interests": ""}})

# Replacing an array with a new one
new_interests = ["swimming", "cooking"]
collection.update_one({"name": "John"}, {"$set": {"interests": new_interests}})



# ---x---x---x---x---x---x---x---x---x---x---x

# Assuming you have a collection with documents representing users and their favorite books with 
# additional information like authors and ratings...
{
    "_id": 1,
    "name": "Alice",
    "favorite_books": [
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "rating": 4},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "rating": 5}
    ]
}

collection1 = db["mycollection1"]

# Adding New Books to the Array of Nested Dictionaries:
new_books = [
    {"title": "1984", "author": "George Orwell", "rating": 4},
    {"title": "Brave New World", "author": "Aldous Huxley", "rating": 4}
]
collection1.update_one({"name": "Alice"}, {"$push": {"favorite_books": {"$each": new_books}}}, upsert=True)


# updating ratings # error when upstream=True
collection1.update_one(
    {"name": "Alice", "favorite_books.title": "The Great Gatsby"},
    {"$set": {"favorite_books.$.rating": 5}}
)

# remove a doc
collection1.update_one({"name": "Alice"}, {"$pull": {"favorite_books": {"title": "1984"}}})


# removing  docs with less than threshold
# collection1.update_one({"name": "Alice"}, {"$pull": {"favorite_books": {"rating": {"$lt": 5}}}})


# updating authors

collection1.update_one(
    {"name": "Alice", "favorite_books.title": "Brave New World"},
    {"$set": {"favorite_books.$.author": "Updated NEW Author", "favorite_books.$.title": "Hacked title"}}
)

'''If you have multiple books with the same title but different authors in your array of 
nested dictionaries, the query you provided might not work as expected because the positional 
operator $ will only update the first matching element in the array. To update all matching elements 
with the same title, you need to use the aggregation framework to identify the matching documents and then update them.

Here's how you can update all occurrences of "Brave New World" with a new author using the aggregation 
framework and the $out stage:
'''
# pipeline = [
#     {"$match": {"name": "Alice", "favorite_books.title": "Brave New World"}},
#     {"$unwind": "$favorite_books"},
#     {"$match": {"favorite_books.title": "Brave New World"}},
#     {"$set": {"favorite_books.author": "Updated NEW Author"}},
#     {"$group": {"_id": "$_id", "favorite_books": {"$push": "$favorite_books"}}},
#     {"$out": "mycollection"}
# ]

# db.command('aggregate', 'mycollection1', pipeline=pipeline)



# To read all the docs in the collection
all_records = collection1.find()
list_all_records = list(all_records)
pprint(list_all_records)

