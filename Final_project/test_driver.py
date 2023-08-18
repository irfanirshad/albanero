
import sys
# sys.path.append('/home/albanero/github_repos/albanero/Final_project/MongoDB')


import os
print("Current directory:", os.getcwd())
print("Python path:", sys.path)

import pymongo
# from flask_app.models.User import Address, PersonalDetails, User
from flask_app.models.User import User

# Create instances of User, PersonalDetails, and Address
personal_details = PersonalDetails(id=1, name="John Doe", phone=1234567890)
address = Address(id=1, address_line_1="123 Main St", pincode=123456, city="Sample City", state="DLH")
user = User(personal_details=personal_details, address=address)


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]


# db = DB()
db.save_user(user)

# Retrieve all users
all_users = db.get_all_users()
for user in all_users:
    print(user)


# /home/albanero/github_repos/albanero/Final_project/MongoDB
# Current directory: /home/albanero/github_repos/albanero/Final_project/MongoDB
# Python path: ['/home/albanero/github_repos/albanero/Final_project/MongoDB', '/usr/lib/python38.zip', '/usr/lib/python3.8', '/usr/lib/python3.8/lib-dynload', '/home/albanero/github_repos/albanero/Final_project/venv/lib/python3.8/site-packages']