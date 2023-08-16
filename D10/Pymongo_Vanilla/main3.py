import pymongo

# Connect to the MongoDB instance
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

# Create a document
data = {"name": "John", "age": 30, "interests": ["programming", "gaming"]}
collection.insert_one(data)

# Read a document
result = collection.find_one({"name": "John"})
print("Read:", result)



# Update a document (CRUD - Update)
update_data = {"$set": {"age": 31}}
collection.update_one({"name": "John"}, update_data)

# Upsert a document
upsert_data = {"name": "Alice", "age": 25}
collection.update_one({"name": "Alice"}, {"$set": upsert_data}, upsert=True)

# Bulk operations - insert many
bulk_data = [
    {"name": "Bob", "age": 28},
    {"name": "Eve", "age": 22}
]
collection.insert_many(bulk_data)

# Delete a document
collection.delete_one({"name": "Bob"})




# Aggregation Pipeline
pipeline = [
    {"$match": {"age": {"$gte": 25}}},
    {"$group": {"_id": "$age", "count": {"$sum": 1}}},
    {"$sort": {"_id": 1}},
    {"$limit": 2},
    {"$skip": 1},
    {"$project": {"_id": 0, "age": "$_id", "count": 1}}
]
agg_result = collection.aggregate(pipeline)
print("Aggregation Result:")
for item in agg_result:
    print(item)

# Working with arrays
collection.update_one({"name": "John"}, {"$push": {"interests": "painting"}})

# Print updated document
updated_result = collection.find_one({"name": "John"})
print("Updated:", updated_result)




'''
-x-x-x--x
'''

# Bulk Write Operations - Update/Insert
bulk_operations = [
    pymongo.UpdateOne({"name": "John1"}, {"$set": {"age": 32}}),
    pymongo.UpdateOne({"name": "Alice1"}, {"$set": {"age": 26}}, upsert=True),
    pymongo.UpdateOne({"name": "Bob1"}, {"$set": {"age": 29}}, upsert=True)
]
bulk_result = collection.bulk_write(bulk_operations)
print("Bulk Write Result:")
print("Matched Count:", bulk_result.matched_count)
print("Modified Count:", bulk_result.modified_count)
print("Upserts Count:", bulk_result.upserted_count)

# Bulk Delete Operations
bulk_delete_operations = [
    pymongo.DeleteOne({"name": "Eve"}),
    pymongo.DeleteOne({"name": "Bob1"})
]
bulk_delete_result = collection.bulk_write(bulk_delete_operations)
print("Bulk Delete Result:")
print("Deleted Count:", bulk_delete_result.deleted_count)



'''
:::RESULT OUTPUT:::

Read: {'_id': ObjectId('64dc5138c3ea983396476fa4'), 'name': 'John', 'age': 30, 'interests': ['programming', 'gaming']}
Aggregation Result:
{'count': 1, 'age': 31}
Updated: {'_id': ObjectId('64dc5138c3ea983396476fa4'), 'name': 'John', 'age': 31, 'interests': ['programming', 'gaming', 'painting']}
Bulk Write Result:
Matched Count: 0
Modified Count: 0
Upserts Count: 2
Bulk Delete Result:
Deleted Count: 2


'''

# UPSERT: More info 

'''
Upsert

1) db.employee.findAndModify({query:{name:"Ram"}, 
                            update:{$set:{department:"Development"}},
                            upsert:true})

no document matches the name “Ram”, so the findAndModify() method 
inserts a new document that contains two fields(i.e., name: “Ram” and department: “Development”) 
because the value of the upsert option is set to true.


2) Upsert with Operator Expression

db.example.update({Name: "Rekha"},   // Query parameter  
                  {$set: {Phone: '7841235468 '}, // Update document
                   $setOnInsert: {Gender: 'Female'}},
                  {upsert: true})

If no document matches the filter from the given collection and 
the update parameter is a document that contains update operators,
also the value of upsert option is set to true, then the update operation 
creates new documents from the equality clauses in the given query parameter
and applies the expressions from the update parameter


'''