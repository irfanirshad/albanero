from pymongo import MongoClient 

client = MongoClient("localhost", 27017)
client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000")

db = client.neuraldb

people = db.people

people.insert_one({"name": "irfan", "age": 30})


for person in people.find():
    print(person)
    