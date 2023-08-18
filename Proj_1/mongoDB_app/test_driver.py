import pymongo

from flask_app.models.user import PersonalDetails

# from mongodb_service import DB

# import flask_app.models.user.PersonalDetails, flask_app.models.user.Address, flask_app.models.user.User

# Create instances of User, PersonalDetails, and Address
personal_details = PersonalDetails(id=1, name="John Doe", phone=1234567890)
address = Address(id=1, address_line_1="123 Main St", pincode=123456, city="Sample City", state="DLH")
user_obj = User(personal_details=personal_details, address=address)


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]


# db = DB()
db.save_user(user_obj)


# Retrieve all users
all_users = db.get_all_users()
for users in all_users:
    print(users)